#!/usr/bin/env python3
"""「更新」工作流一键执行（机械步骤部分）。

用法:
  python scripts/run_update.py update    # 完整更新：抓取 → 导入 → 中文总结审校 → PDF 获取 → 同步 → 六道闸门
  python scripts/run_update.py fetch     # 读基准 → 增量抓取 → OA 检查 → 抓摘要 → 打印待处理清单
  python scripts/run_update.py advance   # 全部闸门通过后：推进更新基准（date=今天, dois=全部）

说明:
  - update 是日常更新的唯一完整入口。它强制执行中文总结审校及 PDF 探测、下载、
    校验与跳过证据登记；任何一步失败都会停止，不能推进或发布。
  - skill 脚本路径: D:/codex/.codex/skills/paper-summarize-fetch/scripts/
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

from update_batch import UpdateBatch
from workflow_validation import validate_workflow

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = Path("D:/codex/.codex/skills/paper-summarize-fetch/scripts")
RUNS = ROOT / "skill-runs"
LAST_UPDATE = RUNS / "last_update.json"
DATA_FILE = ROOT / "data" / "papers.js"
COLLECTION_AUDIT = RUNS / "collection_audit.json"
BATCH_INPUTS = (
    ROOT / "data" / "journals.json",
    ROOT / "scripts" / "fetch_incremental.py",
    ROOT / "scripts" / "journal_collection.py",
    ROOT / "scripts" / "fetch_content.py",
    ROOT / "scripts" / "smart_pdf.py",
    ROOT / "scripts" / "download_incremental_pdfs.py",
    ROOT / "scripts" / "record_incremental_pdf_attempts.py",
    ROOT / "scripts" / "verify_papers.py",
    SKILL_SCRIPTS / "oa_check.py",
)


def log(msg):
    print(msg, flush=True)


class PublishVerificationError(RuntimeError):
    """Raised when GitHub Pages has not published the current local release."""


def verify_pages_release(*, build_status, build_commit, head_sha, local_fingerprint, remote_fingerprint):
    """Require a built Pages deployment for HEAD and byte-equivalent online content."""
    if build_status != "built":
        raise PublishVerificationError("Pages 构建尚未完成")
    if build_commit != head_sha:
        raise PublishVerificationError("Pages 尚未针对当前提交完成构建")
    if local_fingerprint != remote_fingerprint:
        raise PublishVerificationError("线上内容与本地内容不一致")
    return True


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


def titles_from_data(baseline_dois=None):
    """Return titles belonging to the baseline, excluding newly staged entries."""
    titles = []
    if DATA_FILE.exists():
        src = DATA_FILE.read_text(encoding="utf-8")
        m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
        if m:
            papers = json.loads(m.group(1))
            if baseline_dois is not None:
                known = {str(doi).strip().lower() for doi in baseline_dois}
                papers = [p for p in papers if str(p.get("doi") or "").strip().lower() in known]
            titles = [p.get("title") or "" for p in papers]
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


def fetch(*, resume=False, with_batch=False):
    base = load_last_update()
    last_date = base["date"]
    dois = base.get("dois") or []
    baseline_titles = titles_from_data(dois)
    batch = UpdateBatch(ROOT, script_inputs=BATCH_INPUTS)
    batch.begin(base, baseline_titles)
    log(f"更新基准: 上次日期 {last_date}, 已收录 DOI {len(dois)} 个")

    records = batch.path("records")
    audit = batch.path("audit")
    oa = batch.path("oa")
    content = batch.path("content")

    if resume and batch.reusable("collection"):
        log("Step 1/3 · 复用今天已验证的双来源抓取与审计。")
    else:
        batch.invalidate_from("collection")
        # 已收录清单可能很大，Windows 命令行有长度上限，统一写临时 JSON。
        tmp_dois = tmp_titles = None
        try:
            tmp_dois = write_temp_json(dois)
            tmp_titles = write_temp_json(baseline_titles)
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
            require_successful_collection_audit(last_date, require_today=True)
            batch.complete("collection")
        finally:
            for p in (tmp_dois, tmp_titles):
                if p:
                    try:
                        os.unlink(p)
                    except OSError:
                        pass

    if resume and batch.reusable("oa"):
        log("Step 2/3 · 复用今天已验证的 OA/arXiv 结果。")
    else:
        batch.invalidate_from("oa")
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
        batch.complete("oa")

    if resume and batch.reusable("content"):
        log("Step 3/3 · 复用今天已验证的多渠道摘要结果。")
    else:
        batch.invalidate_from("content")
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
                batch.path("content_attempts"),
            ]
        )
        batch.complete("content")

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
    return (recs, batch) if with_batch else recs


def update(*, refresh=False):
    """Run the non-optional daily update chain through its publication gates."""
    recs, batch = fetch(resume=not refresh, with_batch=True)
    if not recs:
        log("本轮没有新增论文；仍补齐并检查现有主题、中文摘要与 PDF 记录。")
        if not refresh and batch.reusable("pdf"):
            log("PDF 阶段复用今天已验证的探测、下载与证据记录。")
        else:
            batch.invalidate_from("pdf")
            log("PDF 阶段：探测 → 下载 → 校验 → 跳过证据登记…")
            acquire_pdfs()
            batch.complete("pdf")
        run(["node", ROOT / "scripts" / "sync-papers.js", "--fill-themes", "--python", sys.executable])
        validate_workflow(log=log)
        return

    log("Step 4/9 · 登记新增论文…")
    run(["node", ROOT / "scripts" / "import_incremental.js"])
    log("Step 5/9 · 新增摘要已保存为可核验草稿，中文六段式须由执行 agent 对照原文撰写…")
    if not refresh and batch.reusable("pdf"):
        log("Step 6/9 · 复用今天已验证的 PDF 探测、下载与证据记录。")
    else:
        batch.invalidate_from("pdf")
        log("Step 6/9 · 获取 PDF：探测 → 下载 → 校验 → 跳过证据登记…")
        acquire_pdfs()
        batch.complete("pdf")
    log("Step 7–8/9 · 单次协调主题补全与台账同步…")
    run(["node", ROOT / "scripts" / "sync-papers.js", "--fill-themes", "--python", sys.executable])
    log("Step 9/9 · 更新完成性检查…")
    validate_workflow(log=log)
    log("✅ 本轮中文总结、PDF 获取及证据登记均已完成；复核内容与标签后可运行 advance。")


def advance():
    """推进更新基准前同时验证中文摘要与 PDF 获取闭环。"""
    base = load_last_update()
    require_successful_collection_audit(base["date"], require_today=True)
    validate_workflow(context="advance 前置", log=log)

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
    validate_workflow(context="publish 前置", include_pdf_integrity=True, log=log)

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
    build_status = "unknown"
    build_commit = ""
    for _ in range(40):
        br = subprocess.run(
            ["gh", "api", f"repos/{repo}/pages/builds/latest", "--jq", "{status: .status, commit: .commit}"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        info = (br.stdout or "").strip()
        try:
            pages_build = json.loads(info) if info else {}
        except json.JSONDecodeError:
            pages_build = {}
        build_status = pages_build.get("status", "unknown")
        build_commit = pages_build.get("commit", "") or ""
        if build_status == "built" and build_commit == head_sha:
            built = True
            break
        time.sleep(15)
    if not built:
        log(f"提示: 本次提交 {head_sha[:7]} 的 Pages 构建尚未完成，仍会进行线上指纹校验；未满足全部条件时 publish 将失败。")

    # 4 · 验证线上内容 = 本地内容（带版本参数绕过 CDN 缓存）
    local_count = count_papers(DATA_FILE)
    stamp = re.search(r"data/papers\.js\?v=([a-z0-9]+)", (ROOT / "index.html").read_text(encoding="utf-8"))
    ver = stamp.group(1) if stamp else ""
    remote_url = f"{site}/data/papers.js" + (f"?v={ver}" if ver else "")
    cr = subprocess.run(["curl.exe", "-s", "--connect-timeout", "20", remote_url], capture_output=True, text=True, encoding="utf-8", errors="replace")
    remote_src = cr.stdout or ""
    remote_count = remote_src.count('"id":')
    log(f"本地论文数: {local_count} | 线上论文数: {remote_count}")
    local_src = DATA_FILE.read_text(encoding="utf-8")
    local_fingerprint = hashlib.sha256(local_src.encode("utf-8")).hexdigest()
    remote_fingerprint = hashlib.sha256(remote_src.encode("utf-8")).hexdigest() if remote_src else ""
    try:
        verify_pages_release(
            build_status=build_status,
            build_commit=build_commit,
            head_sha=head_sha,
            local_fingerprint=local_fingerprint,
            remote_fingerprint=remote_fingerprint,
        )
    except PublishVerificationError as exc:
        raise SystemExit(f"❌ 发布未完成：{exc}（本地 {local_count} / 线上 {remote_count}），稍后重试 publish。") from exc
    log(f"✅ 发布完成，线上已更新: {site}")


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
    ap.add_argument(
        "--refresh",
        action="store_true",
        help="忽略同日更新批次缓存，强制重新执行抓取、OA、摘要和 PDF 阶段（仅 update）",
    )
    args = ap.parse_args()
    if args.mode == "update":
        update(refresh=args.refresh)
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
