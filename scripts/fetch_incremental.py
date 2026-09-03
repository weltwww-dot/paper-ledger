#!/usr/bin/env python3
"""增量抓取：从上次更新日期到现在的全部期刊论文（OpenAlex）。

与 fetch_latest.py（每刊仅取最新一篇）不同，本脚本按日期区间抓取每本
期刊发布的全部论文，确保「上次更新 → 最新」之间的论文一篇不漏。

用法:
  python scripts/fetch_incremental.py --last-date 2026-08-27 --out skill-runs/records_inc.json
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from dedup import is_known, make_known

UA = {"User-Agent": "paper-ledger/1.0 (mailto:verify.references.user@gmail.com)"}

JOURNALS = [
    {"journal": "IEEE Transactions on Information Forensics and Security", "issn": "1556-6013"},
    {"journal": "IEEE Transactions on Dependable and Secure Computing", "issn": "1545-5971"},
    {"journal": "ACM Transactions on Privacy and Security", "issn": "2471-2566"},
    {"journal": "Computers & Security", "issn": "0167-4048"},
    {"journal": "International Journal of Information Security", "issn": "1615-5262"},
    {"journal": "Journal of Computer Security", "issn": "0926-227X"},
    {"journal": "IEEE Security & Privacy", "issn": "1540-7993"},
    {"journal": "Journal of Cybersecurity", "issn": "2057-2085"},
    {"journal": "Journal of Machine Learning Research", "issn": "1532-4435"},
    {"journal": "IEEE Transactions on Pattern Analysis and Machine Intelligence", "issn": "0162-8828"},
    {"journal": "Artificial Intelligence", "issn": "0004-3702"},
    {"journal": "Machine Learning", "issn": "0885-6125"},
    {"journal": "Neural Networks", "issn": "0893-6080"},
    {"journal": "IEEE Transactions on Neural Networks and Learning Systems", "issn": "2162-237X"},
    {"journal": "IEEE Transactions on Knowledge and Data Engineering", "issn": "1041-4347"},
    {"journal": "Nature Machine Intelligence", "issn": "2522-5839"},
    {"journal": "IEEE Transactions on Artificial Intelligence", "issn": "2691-4581"},
]

JUNK_TITLE_HITS = (
    "society",
    "editorial",
    "call for papers",
    "announcement",
    "front cover",
    "back cover",
    "table of contents",
    "erratum",
    "corrigendum",
)


def get_json(url, timeout=30, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def works_by_issn(issn, from_date):
    """抓取 from_date 之后该刊的全部文章（OpenAlex，最多 200 条）。"""
    out = []
    cursor = "*"
    while True:
        url = (
            "https://api.openalex.org/works?"
            + urllib.parse.urlencode(
                {
                    "filter": (
                        f"primary_location.source.issn:{issn},"
                        f"type:article,from_publication_date:{from_date}"
                    ),
                    "sort": "publication_date:asc",
                    "per-page": "100",
                    "cursor": cursor,
                    "select": "doi,display_name,publication_year,publication_date,type",
                }
            )
        )
        d = get_json(url)
        for r in d.get("results") or []:
            title = (r.get("display_name") or "").lower()
            if any(h in title for h in JUNK_TITLE_HITS):
                continue
            if r.get("doi"):
                out.append(r)
        cursor = d.get("meta", {}).get("next_cursor")
        if not cursor:
            break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--last-date", required=True, help="上次更新日期 YYYY-MM-DD（含当天起）")
    ap.add_argument("--out", required=True, help="输出 records JSON")
    ap.add_argument("--existing-dois", default="", help="逗号分隔的已收录 DOI，用于跳过")
    ap.add_argument("--existing-titles", default="", help="逗号分隔的已收录标题，用于跳过（同一论文多 DOI 时按标题兜底）")
    args = ap.parse_args()

    known = make_known(
        [d for d in args.existing_dois.split(",") if d.strip()],
        [t for t in args.existing_titles.split(",") if t.strip()],
    )
    records = []

    def fetch(j):
        try:
            rows = works_by_issn(j["issn"], args.last_date)
        except Exception as e:  # noqa: BLE001
            return j["journal"], [], str(e)[:100]
        recs = []
        for r in rows:
            doi = (r.get("doi") or "").replace("https://doi.org/", "").lower()
            title = r.get("display_name") or ""
            if not doi or is_known(doi, title, known):
                continue
            recs.append(
                {
                    "doi": doi,
                    "title": title,
                    "year": r.get("publication_year"),
                    "date": r.get("publication_date") or "",
                    "source": j["journal"],
                }
            )
        return j["journal"], recs, None

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch, j): j for j in JOURNALS}
        for fut in as_completed(futures):
            journal, recs, err = fut.result()
            if err:
                print(f"[warn] {journal}: {err}", file=sys.stderr)
            else:
                records.extend(recs)
                print(f"{journal:<58} {len(recs):>3} new")

    records.sort(key=lambda r: (r.get("date") or "", r.get("doi") or ""))
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=1)

    print(f"\ndone: {len(records)} papers from {args.last_date} → {args.out}")


if __name__ == "__main__":
    main()
