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
import time
from datetime import date
from pathlib import Path

from dedup import is_known, make_known

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
    去重语义与 fetch_incremental 共用 scripts/dedup.py（DOI 或标题命中即重复）。
    """
    recs = json.loads(records.read_text(encoding="utf-8")) if records.exists() else []
    known = make_known(existing, existing_titles)
    by_doi = {}
    for r in recs:
        k = (r.get("doi") or "").lower()
        if k:
            by_doi[k] = r
    added = 0
    if latest_file.exists():
        for r in json.loads(latest_file.read_text(encoding="utf-8")):
            k = (r.get("doi") or "").lower()
            if k and k not in by_doi and not is_known(k, r.get("title"), known):
                by_doi[k] = r
                added += 1
    merged = list(by_doi.values())
    records.write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    if added:
        log(f"交叉检查补回 {added} 篇（OpenAlex 延迟收录，日期早于基准）")
    return merged


def titles_from_data():
    titles = []
    if DATA_FILE.exists():
        src = DATA_FILE.read_text(encoding="utf-8")
        m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
        if m:
            titles = [p.get("title") or "" for p in json.loads(m.group(1))]
    return titles


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
            "--existing-titles",
            ",".join(titles_from_data()),
        ]
    )

    log("Step 1.5/3 · 交叉检查每刊最新一篇（兜底 OpenAlex 延迟收录）…")
    latest_file = RUNS / "records_latest.json"
    run([sys.executable, SKILL_SCRIPTS / "fetch_latest.py", "-o", latest_file])
    recs = merge_records(records, latest_file, dois, titles_from_data())
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


def count_papers(js_path):
    src = Path(js_path).read_text(encoding="utf-8")
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
    if not m:
        raise SystemExit(f"解析失败: {js_path}")
    return len(json.loads(m.group(1)))


def publish():
    """推送 → 等待 GitHub Pages 构建完成 → 验证线上内容已更新。"""
    repo = "weltwww-dot/paper-ledger"
    site = "https://weltwww-dot.github.io/paper-ledger"

    # 1 · 确认有待推送的提交
    r = subprocess.run(["git", "log", "origin/main..HEAD", "--oneline"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    pending = [l for l in (r.stdout or "").splitlines() if l.strip()]
    if not pending:
        log("本地没有未推送的提交（线上已是最新）。")
    else:
        log(f"待推送 {len(pending)} 个提交:")
        for l in pending:
            log("  " + l)
        # 2 · push（github.com 网络不稳定，自动重试）
        pushed = False
        for i in range(1, 7):
            log(f"git push 尝试 {i}/6 …")
            pr = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, encoding="utf-8", errors="replace")
            if pr.returncode == 0:
                pushed = True
                break
            log("  push 失败（网络），15s 后重试")
            time.sleep(15)
        if not pushed:
            raise SystemExit("git push 多次失败：github.com 网络被阻断，稍后重跑 publish。")

    # 3 · 等待「本地 HEAD 对应的」Pages 构建完成（最多约 10 分钟）
    hr = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    head_sha = (hr.stdout or "").strip()
    log(f"等待 GitHub Pages 构建 {head_sha[:7]} …")
    built = False
    for _ in range(40):
        br = subprocess.run(
            ["gh", "api", f"repos/{repo}/pages/builds/latest", "--jq", "{status: .status, commit: .commit[0:7]}"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        info = (br.stdout or "").strip()
        if info and head_sha[:7] in info and '"built"' in info:
            built = True
            break
        time.sleep(15)
    if not built:
        log(f"提示: 本次提交 {head_sha[:7]} 的 Pages 构建尚未完成，稍后可再跑 publish 验证。")

    # 4 · 验证线上内容 = 本地内容（带版本参数绕过 CDN 缓存）
    local_count = count_papers(DATA_FILE)
    stamp = re.search(r"data/papers\.js\?v=([a-z0-9]+)", (ROOT / "index.html").read_text(encoding="utf-8"))
    ver = stamp.group(1) if stamp else ""
    remote_url = f"{site}/data/papers.js" + (f"?v={ver}" if ver else "")
    cr = subprocess.run(["curl.exe", "-s", "--connect-timeout", "20", remote_url], capture_output=True, text=True, encoding="utf-8", errors="replace")
    remote_src = cr.stdout or ""
    remote_count = remote_src.count('"id":')
    log(f"本地论文数: {local_count} | 线上论文数: {remote_count}")
    if built and local_count == remote_count:
        log(f"✅ 发布完成，线上已更新: {site}")
    elif local_count == remote_count:
        log(f"⚠️ 线上内容已一致（{local_count} 篇），但 Pages 构建状态未确认完成。")
    else:
        raise SystemExit(f"❌ 线上内容未同步（本地 {local_count} / 线上 {remote_count}），等待构建后重试。")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="「更新」工作流一键执行")
    ap.add_argument(
        "mode",
        choices=["fetch", "advance", "publish", "pdf"],
        help="fetch=抓取 / pdf=探测 PDF 可下载性 / advance=推进基准 / publish=推送并验证线上",
    )
    args = ap.parse_args()
    if args.mode == "fetch":
        fetch()
    elif args.mode == "pdf":
        probe_pdfs()
    elif args.mode == "advance":
        advance()
    else:
        publish()


def probe_pdfs():
    """对最近一次 fetch 的待处理论文做 PDF 可下载性探测（智能获取器）。"""
    oa = RUNS / "oa_inc.json"
    if not oa.exists():
        raise SystemExit(f"缺少 {oa}。请先运行 fetch。")
    log("PDF 探测（smart_pdf.py）…")
    run([sys.executable, ROOT / "scripts" / "smart_pdf.py", "--probe", oa])
    log("按探测结果：direct/arxiv 直链可直接下载；article-pdf/blocked 需人工判断。")


if __name__ == "__main__":
    main()
