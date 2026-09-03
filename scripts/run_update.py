#!/usr/bin/env python3
"""「更新」工作流一键执行（机械步骤部分）。

用法:
  python scripts/run_update.py fetch     # 读基准 → 增量抓取 → OA 检查 → 抓摘要 → 打印待处理清单
  python scripts/run_update.py advance   # 总结与同步完成后：推进更新基准（date=今天, dois=全部）

说明:
  - 抓取/总结/PDF/QA 中的「智能」步骤（写六段式总结、方向归类、判断可下载性）由 agent 完成，
    本脚本只自动化确定性步骤，保证可重复、不遗漏。
  - skill 脚本路径: D:/codex/.codex/skills/paper-summarize-fetch/scripts/
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = Path("D:/codex/.codex/skills/paper-summarize-fetch/scripts")
RUNS = ROOT / "skill-runs"
LAST_UPDATE = RUNS / "last_update.json"
DATA_FILE = ROOT / "data" / "papers.js"


def log(msg):
    print(msg, flush=True)


def run(cmd, cwd=ROOT):
    log("  $ " + " ".join(str(c) for c in cmd))
    r = subprocess.run([str(c) for c in cmd], cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.stdout:
        log(r.stdout.rstrip())
    if r.returncode != 0:
        log("[stderr] " + (r.stderr or "").rstrip())
        raise SystemExit(f"命令失败: {' '.join(str(c) for c in cmd)}")


def load_last_update():
    if not LAST_UPDATE.exists():
        raise SystemExit(
            f"缺少 {LAST_UPDATE}。首次运行请先执行一次完整流程并初始化基准"
            "（date + 已收录 DOI 列表）。"
        )
    with open(LAST_UPDATE, encoding="utf-8") as f:
        return json.load(f)


def existing_dois_from_data():
    src = DATA_FILE.read_text(encoding="utf-8")
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
    if not m:
        raise SystemExit("data/papers.js 解析失败")
    arr = json.loads(m.group(1))
    return [p["doi"] for p in arr if p.get("doi")]


def merge_records(records, latest_file, existing, existing_titles=None):
    """把增量抓取结果与「每刊最新」交叉检查结果合并，按 DOI 去重。

    OpenAlex 收录存在延迟：日期较早但刚入库的文章，仅按日期区间抓取会漏掉。
    因此用 fetch_latest.py（每刊最新一篇）做兜底交叉检查。
    同一篇论文可能挂多个 DOI（如正式 DOI 与仓库 DOI），因此再按标题兜底去重。
    """
    recs = json.loads(records.read_text(encoding="utf-8")) if records.exists() else []
    known = {d.lower() for d in existing}
    known_titles = {t.strip().lower() for t in (existing_titles or [])}
    by_doi = {}
    for r in recs:
        k = (r.get("doi") or "").lower()
        if k:
            by_doi[k] = r
    added = 0
    if latest_file.exists():
        for r in json.loads(latest_file.read_text(encoding="utf-8")):
            k = (r.get("doi") or "").lower()
            t = (r.get("title") or "").strip().lower()
            if k and k not in by_doi and k not in known and t not in known_titles:
                by_doi[k] = r
                added += 1
    merged = list(by_doi.values())
    records.write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    if added:
        log(f"交叉检查补回 {added} 篇（OpenAlex 延迟收录，日期早于基准）")
    return merged


def fetch():
    base = load_last_update()
    last_date = base["date"]
    dois = base.get("dois") or []
    log(f"更新基准: 上次日期 {last_date}, 已收录 DOI {len(dois)} 个")

    records = RUNS / "records_inc.json"
    oa = RUNS / "oa_inc.json"
    abstracts = RUNS / "abstracts_inc.json"

    log("Step 1/3 · 增量抓取全部期刊论文…")
    run(
        [
            sys.executable,
            ROOT / "scripts" / "fetch_incremental.py",
            "--last-date",
            last_date,
            "--out",
            records,
            "--existing-dois",
            ",".join(dois),
        ]
    )

    log("Step 1.5/3 · 交叉检查每刊最新一篇（兜底 OpenAlex 延迟收录）…")
    latest_file = RUNS / "records_latest.json"
    run([sys.executable, SKILL_SCRIPTS / "fetch_latest.py", "-o", latest_file])
    known_titles = []
    if DATA_FILE.exists():
        src = DATA_FILE.read_text(encoding="utf-8")
        m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
        if m:
            known_titles = [p.get("title") or "" for p in json.loads(m.group(1))]
    recs = merge_records(records, latest_file, dois, known_titles)
    log(f"合并后待处理: {len(recs)} 篇")

    log("Step 2/3 · OA 检查 + arXiv…")
    run(
        [
            sys.executable,
            SKILL_SCRIPTS / "oa_check.py",
            "-i",
            records,
            "-o",
            oa,
            "--arxiv",
            "--concurrent",
        ]
    )

    log("Step 3/3 · 抓摘要…")
    run(
        [
            sys.executable,
            SKILL_SCRIPTS / "fetch_abstracts.py",
            "-i",
            oa,
            "-o",
            abstracts,
        ]
    )

    with open(records, encoding="utf-8") as f:
        recs = json.load(f)
    ab_map = {}
    if abstracts.exists():
        with open(abstracts, encoding="utf-8") as f:
            ab_map = {x.get("doi"): (x.get("abstract") or "") for x in json.load(f)}

    log(f"\n待处理新增论文: {len(recs)} 篇")
    for r in recs:
        has_ab = "有摘要" if ab_map.get(r.get("doi")) else "无摘要"
        log(f"  [{r.get('date')}] {r.get('title')}  · {r.get('source')}  · {has_ab}  · {r.get('doi')}")

    if not recs:
        log("无新增论文（区间内没有未收录的新文章）。")


def advance():
    dois = existing_dois_from_data()
    today = date.today().isoformat()
    payload = {"date": today, "dois": dois}
    RUNS.mkdir(parents=True, exist_ok=True)
    LAST_UPDATE.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"更新基准已推进: date={today}, 已收录 DOI {len(dois)} 个 → {LAST_UPDATE}")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="「更新」工作流一键执行")
    ap.add_argument("mode", choices=["fetch", "advance"], help="fetch=抓取阶段 / advance=完成阶段推进基准")
    args = ap.parse_args()
    if args.mode == "fetch":
        fetch()
    else:
        advance()


if __name__ == "__main__":
    main()
