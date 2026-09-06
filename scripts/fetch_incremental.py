#!/usr/bin/env python3
"""增量抓取入口：通过统一期刊收录模块对账 OpenAlex 与 Crossref。"""

import argparse
import json
from pathlib import Path

from journal_collection import collect_journals, load_catalog

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--last-date", required=True, help="上次更新日期 YYYY-MM-DD（含当天）")
    parser.add_argument("--out", required=True, help="输出新增 records JSON")
    parser.add_argument("--audit", required=True, help="输出逐刊来源对账 JSON")
    parser.add_argument("--catalog", default=str(ROOT / "data" / "journals.json"))
    parser.add_argument("--existing-dois", default="", help="逗号分隔的已收录 DOI")
    parser.add_argument("--existing-titles", default="", help="逗号分隔的已收录标题")
    args = parser.parse_args()

    records, audit = collect_journals(
        load_catalog(Path(args.catalog)),
        args.last_date,
        existing_dois=[doi for doi in args.existing_dois.split(",") if doi.strip()],
        existing_titles=[title for title in args.existing_titles.split(",") if title.strip()],
    )
    Path(args.out).write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    Path(args.audit).write_text(json.dumps(audit, ensure_ascii=False, indent=1), encoding="utf-8")
    for journal in audit["journals"]:
        oa, crossref = journal["openalex"]["count"], journal["crossref"]["count"]
        difference = len(journal["crossref_only_dois"]) + len(journal["openalex_only_dois"])
        print(f"{journal['journal']:<58} OA {oa:>3} | Crossref {crossref:>3} | diff {difference:>3}")
    failed_sources = [
        f"{journal['journal']} ({source})"
        for journal in audit["journals"]
        for source in ("openalex", "crossref")
        if journal[source]["error"]
    ]
    if failed_sources:
        raise SystemExit("来源对账未完成，拒绝继续更新：" + ", ".join(failed_sources))
    print(f"\ndone: {len(records)} new papers; audit → {args.audit}")


if __name__ == "__main__":
    main()
