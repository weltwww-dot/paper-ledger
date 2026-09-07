#!/usr/bin/env python3
"""增量抓取入口：通过统一期刊收录模块对账 OpenAlex 与 Crossref。"""

import argparse
import json
from datetime import date, timedelta
from pathlib import Path

from journal_collection import collect_journals, load_catalog

ROOT = Path(__file__).resolve().parent.parent


def effective_start_date(last_date: str, lookback_days: int, today: date | None = None) -> str:
    """Keep a bounded overlap so delayed source records are rechecked safely."""
    if lookback_days < 0:
        raise ValueError("lookback_days 不能小于 0")
    baseline = date.fromisoformat(last_date)
    today = today or date.today()
    return min(baseline, today - timedelta(days=lookback_days)).isoformat()


def write_json_atomically(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--last-date", required=True, help="上次更新日期 YYYY-MM-DD（含当天）")
    parser.add_argument("--out", required=True, help="输出新增 records JSON")
    parser.add_argument("--audit", required=True, help="输出逐刊来源对账 JSON")
    parser.add_argument("--catalog", default=str(ROOT / "data" / "journals.json"))
    parser.add_argument("--existing-dois", default="", help="逗号分隔的已收录 DOI（兼容小清单）")
    parser.add_argument("--existing-dois-file", default="", help="JSON 数组文件：已收录 DOI（避免命令行超长）")
    parser.add_argument("--existing-titles", default="", help="逗号分隔的已收录标题（兼容小清单）")
    parser.add_argument("--existing-titles-file", default="", help="JSON 数组文件：已收录标题（避免命令行超长）")
    parser.add_argument("--lookback-days", type=int, default=7, help="重查近期发表记录的天数（默认 7）")
    args = parser.parse_args()

    effective_start = effective_start_date(args.last_date, args.lookback_days)

    def load_json_list(path: str) -> list[str]:
        if not path:
            return []
        return [str(x) for x in json.loads(Path(path).read_text(encoding="utf-8")) if str(x).strip()]

    existing_dois = [doi for doi in args.existing_dois.split(",") if doi.strip()]
    existing_dois += load_json_list(args.existing_dois_file)
    existing_titles = [title for title in args.existing_titles.split(",") if title.strip()]
    existing_titles += load_json_list(args.existing_titles_file)

    records, audit = collect_journals(
        load_catalog(Path(args.catalog)),
        effective_start,
        existing_dois=existing_dois,
        existing_titles=existing_titles,
    )
    audit["requested_from_date"] = args.last_date
    audit["lookback_days"] = args.lookback_days
    write_json_atomically(Path(args.audit), audit)
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
        Path(args.out).unlink(missing_ok=True)
        raise SystemExit("来源对账未完成，拒绝继续更新：" + ", ".join(failed_sources))
    write_json_atomically(Path(args.out), records)
    print(f"\ndone: {len(records)} new papers; audit → {args.audit}")


if __name__ == "__main__":
    main()
