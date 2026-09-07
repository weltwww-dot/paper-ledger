#!/usr/bin/env python3
"""「更新」工作流一键执行（机械步骤部分）。

用法:
  python scripts/run_update.py update    # 完整更新：抓取 → 导入 → 中文总结审校 → PDF 获取 → 同步 → 五道闸门
  python scripts/run_update.py fetch     # 读基准 → 增量抓取 → OA 检查 → 抓摘要 → 打印待处理清单
  python scripts/run_update.py advance   # 双闸门通过后：推进更新基准（date=今天, dois=全部）

说明:
  - update 是日常更新的唯一完整入口。它强制执行中文总结审校及 PDF 探测、下载、
    校验与跳过证据登记；任何一步失败都会停止，不能推进或发布。
  - skill 脚本路径: D:/codex/.codex/skills/paper-summarize-fetch/scripts/
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = Path("D:/codex/.codex/skills/paper-summarize-fetch/scripts")
RUNS = ROOT / "skill-runs"
LAST_UPDATE = RUNS / "last_update.json"
DATA_FILE = ROOT / "data" / "papers.js"
COLLECTION_AUDIT = RUNS / "collection_audit.json"


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


def run_gate(script, label, failure_message):
    """Run a read-only quality gate and present its report consistently."""
    log(f"{label}…")
    result = subprocess.run(
        [sys.executable, ROOT / "scripts" / script, "--check"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    for line in (result.stdout or "").splitlines():
        log("  " + line)
    for line in (result.stderr or "").splitlines():
        log("  " + line)
    if result.returncode != 0:
        raise SystemExit(failure_message)


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


def titles_from_data():
    titles = []
    if DATA_FILE.exists():
        src = DATA_FILE.read_text(encoding="utf-8")
        m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
        if m:
            titles = [p.get("title") or "" for p in json.loads(m.group(1))]
    return titles


def write_temp_json(items):
    """Write a JSON list to a temp file; returns its path (caller deletes)."""
    fd, path = tempfile.mkstemp(prefix="paperledger-", suffix=".json", text=True)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump([i for i in items if i], f, ensure_ascii=False)
    return path


def require_successful_collection_audit(expected_from_date=None, require_today=False):
    """Prevent state advancement or publishing when source reconciliation failed."""
    if not COLLECTION_AUDIT.exists():
        raise SystemExit("缺少期刊来源审计。请先运行 run_update.py fetch。")
    audit = json.loads(COLLECTION_AUDIT.read_text(encoding="utf-8"))
    failures = [
        f"{journal.get('journal')} ({source})"
        for journal in audit.get("journals") or []
        for source in ("openalex", "crossref")
        if (journal.get(source) or {}).get("error")
    ]
    if failures:
        raise SystemExit("期刊来源审计存在失败，拒绝继续：" + ", ".join(failures))
    if expected_from_date and audit.get("requested_from_date") != expected_from_date:
        raise SystemExit("期刊来源审计不对应当前更新基准。请重新运行 run_update.py fetch。")
    if require_today and audit.get("until_date") != date.today().isoformat():
        raise SystemExit("期刊来源审计不是今天生成的。请重新运行 run_update.py fetch。")


def fetch():
    base = load_last_update()
    last_date = base["date"]
    dois = base.get("dois") or []
    log(f"更新基准: 上次日期 {last_date}, 已收录 DOI {len(dois)} 个")

    records = RUNS / "records_inc.json"
    audit = RUNS / "collection_audit.json"
    oa = RUNS / "oa_inc.json"
    content = RUNS / "content_inc.json"

    # 已收录清单可能很大（586+ 条），Windows 命令行有长度上限，
    # 统一写到系统临时 JSON，由 fetch_incremental 从文件读取（用完即删）。
    tmp_dois = tmp_titles = None
    try:
        tmp_dois = write_temp_json(dois)
        tmp_titles = write_temp_json(titles_from_data())
        log("Step 1/3 · 增量抓取全部期刊论文…")
        run(
            [
                sys.executable,
                ROOT / "scripts" / "fetch_incremental.py",
                "--last-date",
                last_date,
                "--out",
                records,
                "--audit",
                audit,
                "--existing-dois-file",
                tmp_dois,
                "--existing-titles-file",
                tmp_titles,
            ]
        )
    finally:
        for p in (tmp_dois, tmp_titles):
            if p:
                try:
                    os.unlink(p)
                except OSError:
                    pass

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

    log("Step 3/3 · 多渠道抓摘要（typed）…")
    run(
        [
            sys.executable,
            ROOT / "scripts" / "fetch_content.py",
            "-i",
            oa,
            "-o",
            content,
            "--attempts",
            RUNS / "content_attempts.json",
        ]
    )

    with open(records, encoding="utf-8") as f:
        recs = json.load(f)
    res_map = {}
    if content.exists():
        with open(content, encoding="utf-8") as f:
            res_map = {x.get("doi"): x for x in json.load(f)}

    log(f"\n待处理新增论文: {len(recs)} 篇")
    for r in recs:
        c = res_map.get(r.get("doi")) or {}
        kind = c.get("kind") or "无结果"
        src = c.get("source") or "-"
        log(f"  [{r.get('date')}] {r.get('title')}  · {r.get('source')}  · {kind}/{src}  · {r.get('doi')}")

    if not recs:
        log("无新增论文（区间内没有未收录的新文章）。")
    return recs


def update():
    """Run the non-optional daily update chain through its publication gates."""
    recs = fetch()
    if not recs:
        log("本轮没有新增论文；仍补齐并检查现有主题、中文摘要与 PDF 记录。")
        run([sys.executable, ROOT / "scripts" / "fill_theme_tags.py", "--write"])
        run(["node", ROOT / "scripts" / "sync-papers.js"])
        run_gate("summary_gate.py", "中文六段式摘要闸门检查", "中文摘要闸门未通过，不能继续。")
        run_gate("summary_quality_gate.py", "中文文案质量闸门检查", "中文文案质量闸门未通过，不能继续。")
        run_gate("theme_gate.py", "主题标签闸门检查", "主题标签闸门未通过，不能继续。")
        run_gate("pdf_gate.py", "PDF 获取闸门检查", "PDF 闸门未通过，不能继续。")
        run_gate("workflow_gate.py", "论文台账总体验收", "台账总体验收未通过，不能继续。")
        return

    log("Step 4/9 · 登记新增论文…")
    run(["node", ROOT / "scripts" / "import_incremental.js"])
    log("Step 5/9 · 新增摘要已保存为可核验草稿，中文六段式须由执行 agent 对照原文撰写…")
    log("Step 6/9 · 按既有主题方案补齐新增论文主题标签…")
    run([sys.executable, ROOT / "scripts" / "fill_theme_tags.py", "--write"])
    log("Step 7/9 · 获取 PDF：探测 → 下载 → 校验 → 跳过证据登记…")
    acquire_pdfs()
    raise SystemExit(
        "新增记录的 PDF 获取已完成。请先由执行 agent 完成中文六段式总结，"
        "再重新运行 update 收口；自动直译不允许进入发布流程。"
    )
    log("Step 8/9 · 同步总结、主题与 PDF 链接至网站数据…")
    run(["node", ROOT / "scripts" / "sync-papers.js"])
    log("Step 9/9 · 更新完成性检查…")
    run_gate("summary_gate.py", "中文六段式摘要闸门检查", "中文摘要闸门未通过，不能推进或发布。")
    run_gate("summary_quality_gate.py", "中文文案质量闸门检查", "中文文案质量闸门未通过，不能推进或发布。")
    run_gate("theme_gate.py", "主题标签闸门检查", "主题标签闸门未通过，不能推进或发布。")
    run_gate("pdf_gate.py", "PDF 获取闸门检查", "PDF 闸门未通过，不能推进或发布。")
    run_gate("workflow_gate.py", "论文台账总体验收", "台账总体验收未通过，不能推进或发布。")
    log("✅ 本轮中文总结、PDF 获取及证据登记均已完成；复核内容与标签后可运行 advance。")


def advance():
    """推进更新基准前同时验证中文摘要与 PDF 获取闭环。"""
    base = load_last_update()
    require_successful_collection_audit(base["date"], require_today=True)
    run_gate("summary_gate.py", "中文六段式摘要闸门检查（advance 前置）", "中文摘要闸门未通过：先完成中文总结或修复结构再 advance。")
    run_gate("summary_quality_gate.py", "中文文案质量闸门检查（advance 前置）", "中文文案质量闸门未通过：先按原文修复措辞再 advance。")
    run_gate("theme_gate.py", "主题标签闸门检查（advance 前置）", "主题标签闸门未通过：先补齐主题再 advance。")
    run_gate("pdf_gate.py", "PDF 获取闸门检查（advance 前置）", "PDF 闸门未通过：先补 PDF 或记录确认的不可得原因再 advance。")
    run_gate("workflow_gate.py", "论文台账总体验收（advance 前置）", "台账总体验收未通过：先修复 DOI、状态、主题、PDF 或跳过证据的一致性。")

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

    require_successful_collection_audit()

    run_gate("summary_gate.py", "中文六段式摘要闸门检查（publish 前置）", "中文摘要闸门未通过：先完成中文总结或修复结构再 publish。")
    run_gate("summary_quality_gate.py", "中文文案质量闸门检查（publish 前置）", "中文文案质量闸门未通过：先按原文修复措辞再 publish。")
    run_gate("theme_gate.py", "主题标签闸门检查（publish 前置）", "主题标签闸门未通过：先补齐主题再 publish。")

    # 0 · 发布前校验 papers/ 无无效 PDF（防 HTML 垃圾进仓库）
    log("发布前校验 papers/ PDF 有效性…")
    vr = subprocess.run(
        [sys.executable, ROOT / "scripts" / "verify_papers.py"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    for line in (vr.stdout or "").splitlines():
        log("  " + line)
    for line in (vr.stderr or "").splitlines():
        log("  " + line)
    if vr.returncode != 0:
        raise SystemExit("papers/ 存在无效 PDF，请先运行 run_update.py verify 清理。")

    # 0b · PDF 闸门：无 PDF 且无跳过记录的论文阻止发布
    run_gate("pdf_gate.py", "PDF 获取闸门检查（publish 前置）", "PDF 闸门未通过：先补 PDF 或记录确认的不可得原因再 publish。")
    run_gate("workflow_gate.py", "论文台账总体验收（publish 前置）", "台账总体验收未通过：先修复 DOI、状态、主题、PDF 或跳过证据的一致性。")

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
        choices=["update", "fetch", "pdf", "verify", "abstracts", "instsci", "route-check", "advance", "publish"],
        help="update=完整强制流程 / fetch=抓取 / pdf=获取 PDF / verify=校验并清理无效 PDF / abstracts=重试待补全摘要 / instsci=机构全文队列 / route-check=代理出口自检 / advance=推进基准 / publish=发布",
    )
    args = ap.parse_args()
    if args.mode == "update":
        update()
    elif args.mode == "fetch":
        fetch()
    elif args.mode == "pdf":
        probe_pdfs()
    elif args.mode == "verify":
        verify_pdf_files()
    elif args.mode == "abstracts":
        retry_abstracts()
    elif args.mode == "instsci":
        queue_instsci()
    elif args.mode == "route-check":
        route_check()
    elif args.mode == "advance":
        advance()
    else:
        publish()


def papers_from_data():
    src = DATA_FILE.read_text(encoding="utf-8")
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
    if not m:
        raise SystemExit("data/papers.js 解析失败")
    return json.loads(m.group(1))


def pending_papers():
    return [p for p in papers_from_data() if (p.get("contentState") or "").lower() == "pending"]


def retry_abstracts():
    """对待补全论文重跑多渠道摘要获取；失败类型写入 attempts 缓存。"""
    pending = pending_papers()
    if not pending:
        log("没有待补全论文（contentState=pending 为 0）。")
        return
    recs = RUNS / "records_pending.json"
    payload = [{"doi": p.get("doi"), "title": p.get("title"), "arxiv": p.get("arxiv")} for p in pending]
    recs.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"待补全 {len(payload)} 篇 → 多渠道重试…")
    run(
        [
            sys.executable,
            ROOT / "scripts" / "fetch_content.py",
            "-i",
            recs,
            "-o",
            RUNS / "content_retry.json",
            "--attempts",
            RUNS / "content_attempts.json",
        ]
    )
    out = []
    if (RUNS / "content_retry.json").exists():
        out = json.loads((RUNS / "content_retry.json").read_text(encoding="utf-8"))
    blocked = [x["doi"] for x in out if x.get("kind") in ("blocked", "rate-limited")]
    log("重试完成。仍取不到内容（blocked/无摘要）的论文，下一步可走机构全文通道：")
    log("  python scripts/run_update.py instsci")
    if blocked:
        log(f"建议优先走 instsci 的 DOI: {len(blocked)} 篇（详见 fulltext_queue）")


def queue_instsci():
    """生成机构全文补全队列（HITL：需要用户完成 instsci 机构登录）。"""
    pending = pending_papers()
    if not pending:
        log("没有待补全论文。")
        return
    queue = RUNS / "fulltext_queue.txt"
    queue.write_text("\n".join(p.get("doi") or "" for p in pending if p.get("doi")) + "\n", encoding="utf-8")
    out_dir = ROOT / "papers" / "instsci"
    log(f"补全队列已写入: {queue}（{len(pending)} 篇）")
    log("下一步（机构 IP 必须是本机直连出口；可见浏览器的人机验证/登录由你手动完成）：")
    log(
        "  powershell -ExecutionPolicy Bypass -File "
        f"{ROOT / 'scripts' / 'instsci_batch_local_ip.ps1'} "
        f"-DoisFile {queue} -OutputDir {out_dir}"
    )
    log("说明：该包装器会先拒绝代理/PAC 出口；先确保 instsci 已配置机构（instsci setup --school \"你的机构\"）；")
    log("取回 PDF/页面后告诉我，我会更新对应总结并把这些论文的内容状态从待补全改为完整。")


def route_check():
    """代理出口自检：判断开了代理后出版社域名是否仍走直连（IP 路线是否可用）。"""
    run([sys.executable, ROOT / "scripts" / "route_check.py"])


def acquire_pdfs():
    """完整执行本轮 PDF 探测、下载、验证和可追溯跳过登记。"""
    oa = RUNS / "oa_inc.json"
    if not oa.exists():
        raise SystemExit(f"缺少 {oa}。请先运行 fetch。")
    log("PDF 探测（smart_pdf.py）…")
    run([
        sys.executable, ROOT / "scripts" / "smart_pdf.py", "--probe", oa,
        "--workers", "12", "--probe-timeout", "15",
    ])
    log("下载可验证的 PDF 候选…")
    run([sys.executable, ROOT / "scripts" / "download_incremental_pdfs.py"])
    log("记录已确认的不可得原因（不会把网络错误标成已跳过）…")
    run([sys.executable, ROOT / "scripts" / "record_incremental_pdf_attempts.py"])
    log("校验 PDF 文件有效性…")
    run([sys.executable, ROOT / "scripts" / "verify_papers.py", "--check"])


def probe_pdfs():
    """Backward-compatible alias for the complete PDF acquisition workflow."""
    acquire_pdfs()


def verify_pdf_files():
    """校验 papers/ 下 PDF 有效性，删除下载失败的 HTML 残留。"""
    run([sys.executable, ROOT / "scripts" / "verify_papers.py"])


if __name__ == "__main__":
    main()
