#!/usr/bin/env python3
"""统一收录模块：以 OpenAlex 和 Crossref 对账 17 本期刊的新增论文。"""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

from dedup import is_known, make_known, normalize_doi

UA = {"User-Agent": "paper-ledger/1.1 (mailto:verify.references.user@gmail.com)"}
JUNK_TITLE_HITS = ("society", "editorial", "call for papers", "announcement", "front cover", "back cover", "table of contents", "erratum", "corrigendum", "correction to:", "correction:")


def load_catalog(path: Path) -> list[dict]:
    entries = json.loads(path.read_text(encoding="utf-8"))
    required = {"journal", "openalex_issn", "crossref_issn"}
    for entry in entries:
        missing = required - set(entry)
        if missing:
            raise ValueError(f"期刊目录缺少字段 {sorted(missing)}: {entry}")
    return entries


def get_json(url: str, timeout: int = 30, tries: int = 3) -> dict:
    last = None
    for attempt in range(tries):
        try:
            request = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise last


def _is_article(title: str, work_type: str) -> bool:
    text = (title or "").strip().lower()
    return bool(text) and work_type in {"article", "journal-article"} and not any(hit in text for hit in JUNK_TITLE_HITS)


def _crossref_date(item: dict) -> str:
    for key in ("published-online", "published", "issued", "published-print", "created"):
        parts = (item.get(key) or {}).get("date-parts") or []
        if parts and parts[0]:
            values = parts[0]
            return f"{str(values[0]).zfill(4)}-{str(values[1] if len(values) > 1 else 1).zfill(2)}-{str(values[2] if len(values) > 2 else 1).zfill(2)}"
    return ""


def _to_openalex_record(work: dict, journal: str) -> dict | None:
    title = work.get("display_name") or ""
    if not _is_article(title, work.get("type") or ""):
        return None
    doi = normalize_doi(work.get("doi"))
    if not doi:
        return None
    return {"doi": doi, "title": title, "year": work.get("publication_year"), "date": work.get("publication_date") or "", "source": journal, "collection_sources": ["openalex"]}


def _to_crossref_record(work: dict, journal: str) -> dict | None:
    title = (work.get("title") or [""])[0]
    if not _is_article(title, work.get("type") or ""):
        return None
    doi = normalize_doi(work.get("DOI"))
    if not doi:
        return None
    published = _crossref_date(work)
    return {"doi": doi, "title": title, "year": int(published[:4]) if published[:4].isdigit() else None, "date": published, "source": journal, "collection_sources": ["crossref"]}


def openalex_records(entry: dict, from_date: str, until_date: str, fetch_json=get_json) -> list[dict]:
    records, cursor = [], "*"
    while cursor:
        query = urllib.parse.urlencode({"filter": f"primary_location.source.issn:{entry['openalex_issn']},type:article,from_publication_date:{from_date},to_publication_date:{until_date}", "sort": "publication_date:asc", "per-page": "100", "cursor": cursor, "select": "doi,display_name,publication_year,publication_date,type"})
        payload = fetch_json(f"https://api.openalex.org/works?{query}")
        for work in payload.get("results") or []:
            record = _to_openalex_record(work, entry["journal"])
            if record:
                records.append(record)
        cursor = (payload.get("meta") or {}).get("next_cursor")
    return records


def crossref_records(entry: dict, from_date: str, until_date: str, fetch_json=get_json) -> list[dict]:
    records, cursor = [], "*"
    while cursor:
        # Crossref rejects the combination of type, sort, and cursor. Filter the
        # work type locally so cursor pagination remains valid for busy journals.
        query = urllib.parse.urlencode({"filter": f"from-pub-date:{from_date},until-pub-date:{until_date}", "rows": "100", "cursor": cursor})
        payload = fetch_json(f"https://api.crossref.org/journals/{entry['crossref_issn']}/works?{query}")
        message = payload.get("message") or {}
        for work in message.get("items") or []:
            record = _to_crossref_record(work, entry["journal"])
            if record:
                records.append(record)
        next_cursor = message.get("next-cursor")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    return records


def _merge_sources(source_sets: dict[str, list[dict]]) -> list[dict]:
    merged: dict[str, dict] = {}
    for source, records in source_sets.items():
        for record in records:
            prior = merged.get(record["doi"])
            if prior is None:
                merged[record["doi"]] = {**record, "collection_sources": [source]}
                continue
            prior["collection_sources"] = sorted(set(prior["collection_sources"] + [source]))
            if (record.get("date") or "") > (prior.get("date") or ""):
                prior["date"], prior["year"] = record["date"], record.get("year")
    return sorted(merged.values(), key=lambda record: ((record.get("date") or ""), record["doi"]))


def _collect_one(entry: dict, from_date: str, until_date: str, fetch_json) -> tuple[list[dict], dict]:
    source_sets, errors = {}, {}
    for source, adapter in (("openalex", openalex_records), ("crossref", crossref_records)):
        try:
            source_sets[source] = adapter(entry, from_date, until_date, fetch_json)
        except Exception as exc:  # noqa: BLE001
            source_sets[source], errors[source] = [], str(exc)[:240]
    merged = _merge_sources(source_sets)
    by_source = {name: {record["doi"] for record in records} for name, records in source_sets.items()}
    audit = {"journal": entry["journal"], "openalex": {"count": len(source_sets["openalex"]), "error": errors.get("openalex")}, "crossref": {"count": len(source_sets["crossref"]), "error": errors.get("crossref")}, "union_count": len(merged), "crossref_only_dois": sorted(by_source["crossref"] - by_source["openalex"]), "openalex_only_dois": sorted(by_source["openalex"] - by_source["crossref"])}
    return merged, audit


def collect_journals(catalog: list[dict], from_date: str, until_date: str | None = None, existing_dois: list[str] | None = None, existing_titles: list[str] | None = None, fetch_json=get_json, workers: int = 8) -> tuple[list[dict], dict]:
    """Return uncollected records and a complete, per-journal source-reconciliation audit."""
    until_date = until_date or date.today().isoformat()
    known, collected, audits = make_known(existing_dois, existing_titles), [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_collect_one, entry, from_date, until_date, fetch_json): entry for entry in catalog}
        for future in as_completed(futures):
            records, audit = future.result()
            audits.append(audit)
            collected.extend(record for record in records if not is_known(record["doi"], record["title"], known))
    collected.sort(key=lambda record: ((record.get("date") or ""), record["doi"]))
    audits.sort(key=lambda item: item["journal"])
    return collected, {"from_date": from_date, "until_date": until_date, "journal_count": len(catalog), "new_record_count": len(collected), "journals": audits}
