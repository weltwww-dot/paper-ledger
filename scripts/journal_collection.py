#!/usr/bin/env python3
"""统一收录模块：以 OpenAlex 和 Crossref 对账期刊的新增论文。"""

from __future__ import annotations

from collections import Counter
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

from dedup import is_known, make_known, normalize_doi, normalize_title

UA = {"User-Agent": "paper-ledger/1.2 (mailto:verify.references.user@gmail.com)"}
ARTICLE_TYPES = {"article", "journal-article"}
TITLE_EXCLUSION_PATTERNS = (
    ("editorial", re.compile(r"^editorial(?:\s*[:—-]|\s*$)", re.I)),
    ("call-for-papers", re.compile(r"^call\s+for\s+papers?\b", re.I)),
    ("announcement", re.compile(r"^announcement(?:\s*[:—-]|\s*$)", re.I)),
    ("front-cover", re.compile(r"^front\s+cover\b", re.I)),
    ("back-cover", re.compile(r"^back\s+cover\b", re.I)),
    ("table-of-contents", re.compile(r"^table\s+of\s+contents\b", re.I)),
    ("erratum", re.compile(r"^erratum\b", re.I)),
    ("corrigendum", re.compile(r"^corrigendum\b", re.I)),
    ("correction", re.compile(r"^correction(?:\s+to)?\s*:", re.I)),
)
DATE_RANK = {
    "published-online": 0,
    "openalex-publication-date": 1,
    "published": 2,
    "issued": 3,
    "published-print": 4,
    "created": 5,
    "unknown": 99,
}


def load_catalog(path: Path) -> list[dict]:
    entries = json.loads(path.read_text(encoding="utf-8"))
    required = {"journal", "openalex_issn", "crossref_issn"}
    seen_journals, seen_source_pairs = set(), set()
    for entry in entries:
        missing = required - set(entry)
        if missing:
            raise ValueError(f"期刊目录缺少字段 {sorted(missing)}: {entry}")
        if entry["journal"] in seen_journals:
            raise ValueError(f"期刊目录中重复的期刊名: {entry['journal']}")
        source_pair = (entry["openalex_issn"].lower(), entry["crossref_issn"].lower())
        if source_pair in seen_source_pairs:
            raise ValueError(f"期刊目录中重复的来源 ISSN 组合: {entry['journal']}")
        seen_journals.add(entry["journal"])
        seen_source_pairs.add(source_pair)
    return entries


def get_json(url: str, timeout: int = 30, tries: int = 3) -> dict:
    last = None
    for attempt in range(tries):
        try:
            request = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except Exception as exc:  # noqa: BLE001 - error is captured in the audit
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise last


def _filter_reason(title: str, work_type: str, doi: str) -> str | None:
    text = (title or "").strip()
    if not text:
        return "missing-title"
    if work_type not in ARTICLE_TYPES:
        return f"non-article-type:{work_type or 'missing'}"
    for reason, pattern in TITLE_EXCLUSION_PATTERNS:
        if pattern.search(text):
            return f"title:{reason}"
    if not doi:
        return "missing-doi"
    return None


def _crossref_date(item: dict) -> tuple[str, str]:
    for key in ("published-online", "published", "issued", "published-print", "created"):
        parts = (item.get(key) or {}).get("date-parts") or []
        if parts and parts[0]:
            values = parts[0]
            formatted = f"{str(values[0]).zfill(4)}-{str(values[1] if len(values) > 1 else 1).zfill(2)}-{str(values[2] if len(values) > 2 else 1).zfill(2)}"
            return formatted, key
    return "", "unknown"


def _to_openalex_record(work: dict, journal: str) -> tuple[dict | None, str | None]:
    title = work.get("display_name") or ""
    doi = normalize_doi(work.get("doi"))
    reason = _filter_reason(title, work.get("type") or "", doi)
    if reason:
        return None, reason
    return {
        "doi": doi,
        "title": title,
        "year": work.get("publication_year"),
        "date": work.get("publication_date") or "",
        "date_source": "openalex-publication-date",
        "source": journal,
        "collection_sources": ["openalex"],
    }, None


def _to_crossref_record(work: dict, journal: str) -> tuple[dict | None, str | None]:
    title = (work.get("title") or [""])[0]
    doi = normalize_doi(work.get("DOI"))
    reason = _filter_reason(title, work.get("type") or "", doi)
    if reason:
        return None, reason
    published, date_source = _crossref_date(work)
    return {
        "doi": doi,
        "title": title,
        "year": int(published[:4]) if published[:4].isdigit() else None,
        "date": published,
        "date_source": date_source,
        "source": journal,
        "collection_sources": ["crossref"],
    }, None


def openalex_records(entry: dict, from_date: str, until_date: str, fetch_json=get_json) -> tuple[list[dict], Counter]:
    records, excluded, cursor = [], Counter(), "*"
    while cursor:
        query = urllib.parse.urlencode({
            "filter": f"primary_location.source.issn:{entry['openalex_issn']},type:article,from_publication_date:{from_date},to_publication_date:{until_date}",
            "sort": "publication_date:asc",
            "per-page": "100",
            "cursor": cursor,
            "select": "doi,display_name,publication_year,publication_date,type",
        })
        payload = fetch_json(f"https://api.openalex.org/works?{query}")
        for work in payload.get("results") or []:
            record, reason = _to_openalex_record(work, entry["journal"])
            if record:
                records.append(record)
            else:
                excluded[reason] += 1
        cursor = (payload.get("meta") or {}).get("next_cursor")
    return records, excluded


def crossref_records(entry: dict, from_date: str, until_date: str, fetch_json=get_json) -> tuple[list[dict], Counter]:
    records, excluded, cursor = [], Counter(), "*"
    while cursor:
        # Crossref rejects type + sort + cursor together. Type filtering happens
        # locally so cursor pagination remains valid for busy journals.
        query = urllib.parse.urlencode({
            "filter": f"from-pub-date:{from_date},until-pub-date:{until_date}",
            "rows": "100",
            "cursor": cursor,
        })
        payload = fetch_json(f"https://api.crossref.org/journals/{entry['crossref_issn']}/works?{query}")
        message = payload.get("message") or {}
        for work in message.get("items") or []:
            record, reason = _to_crossref_record(work, entry["journal"])
            if record:
                records.append(record)
            else:
                excluded[reason] += 1
        next_cursor = message.get("next-cursor")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    return records, excluded


def _prefer_record(prior: dict, candidate: dict) -> None:
    prior["collection_sources"] = sorted(set(prior["collection_sources"] + candidate["collection_sources"]))
    prior_rank = DATE_RANK.get(prior.get("date_source"), DATE_RANK["unknown"])
    candidate_rank = DATE_RANK.get(candidate.get("date_source"), DATE_RANK["unknown"])
    if candidate_rank < prior_rank or (candidate_rank == prior_rank and candidate.get("date", "") < prior.get("date", "")):
        prior["date"] = candidate.get("date", "")
        prior["year"] = candidate.get("year")
        prior["date_source"] = candidate.get("date_source", "unknown")


def _merge_sources(source_sets: dict[str, list[dict]]) -> list[dict]:
    merged: dict[str, dict] = {}
    for records in source_sets.values():
        for record in records:
            prior = merged.get(record["doi"])
            if prior is None:
                merged[record["doi"]] = {**record}
            else:
                _prefer_record(prior, record)
    return sorted(merged.values(), key=lambda record: ((record.get("date") or ""), record["doi"]))


def _collect_one(entry: dict, from_date: str, until_date: str, fetch_json) -> tuple[list[dict], dict]:
    source_sets, exclusions, errors = {}, {}, {}
    for source, adapter in (("openalex", openalex_records), ("crossref", crossref_records)):
        try:
            source_sets[source], exclusions[source] = adapter(entry, from_date, until_date, fetch_json)
        except Exception as exc:  # noqa: BLE001 - audit must expose a failed adapter
            source_sets[source], exclusions[source], errors[source] = [], Counter(), str(exc)[:240]
    merged = _merge_sources(source_sets)
    by_source = {name: {record["doi"] for record in records} for name, records in source_sets.items()}
    audit = {
        "journal": entry["journal"],
        "openalex": {"count": len(source_sets["openalex"]), "excluded": dict(exclusions["openalex"]), "error": errors.get("openalex")},
        "crossref": {"count": len(source_sets["crossref"]), "excluded": dict(exclusions["crossref"]), "error": errors.get("crossref")},
        "union_count": len(merged),
        "crossref_only_dois": sorted(by_source["crossref"] - by_source["openalex"]),
        "openalex_only_dois": sorted(by_source["openalex"] - by_source["crossref"]),
    }
    return merged, audit


def collect_journals(catalog: list[dict], from_date: str, until_date: str | None = None, existing_dois: list[str] | None = None, existing_titles: list[str] | None = None, fetch_json=get_json, workers: int = 8) -> tuple[list[dict], dict]:
    """Return globally de-duplicated, uncollected records and a source audit."""
    until_date = until_date or date.today().isoformat()
    known = make_known(existing_dois, existing_titles)
    candidates, audits = [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_collect_one, entry, from_date, until_date, fetch_json): entry for entry in catalog}
        for future in as_completed(futures):
            records, audit = future.result()
            candidates.extend(records)
            audits.append(audit)

    collected, collected_by_doi, collected_by_title = [], {}, {}
    for record in sorted(candidates, key=lambda item: (item["doi"], normalize_title(item["title"]), item["source"])):
        if is_known(record["doi"], record["title"], known):
            continue
        prior = collected_by_doi.get(record["doi"]) or collected_by_title.get(normalize_title(record["title"]))
        if prior:
            _prefer_record(prior, record)
            continue
        clean = {**record}
        collected.append(clean)
        collected_by_doi[clean["doi"]] = clean
        collected_by_title[normalize_title(clean["title"])] = clean
    for record in collected:
        record.pop("date_source", None)
    collected.sort(key=lambda record: ((record.get("date") or ""), record["doi"]))
    audits.sort(key=lambda item: item["journal"])
    return collected, {"from_date": from_date, "until_date": until_date, "journal_count": len(catalog), "new_record_count": len(collected), "journals": audits}
