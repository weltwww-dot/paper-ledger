#!/usr/bin/env python3
"""PDF 获取闸门：确保每篇无 PDF 的论文都有记录在案的跳过原因。

数据：
  - data/papers.js                论文清单（pdf 字段为空 = 无本地 PDF）
  - skill-runs/pdf_attempts.json  DOI → {"reason": blocked|not-oa|no-file|…, "note": …}

用法:
  python scripts/pdf_gate.py --check   # 列出「无 PDF 且无跳过记录」的论文；有则 exit 1（闸门挡住）
  python scripts/pdf_gate.py --list    # 列出所有无 PDF 论文及其状态
  python scripts/pdf_gate.py --mark <doi> <reason> [--note "…"]   # 记录跳过原因
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "papers.js"
ATTEMPTS_FILE = ROOT / "skill-runs" / "pdf_attempts.json"


def load_papers():
    src = DATA_FILE.read_text(encoding="utf-8")
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
    if not m:
        raise SystemExit(f"解析失败: {DATA_FILE}")
    return json.loads(m.group(1))


def load_attempts():
    if not ATTEMPTS_FILE.exists():
        return {}
    try:
        return json.loads(ATTEMPTS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_attempts(data):
    ATTEMPTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    ATTEMPTS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def check():
    papers = load_papers()
    attempts = load_attempts()
    missing = [
        p for p in papers
        if not p.get("pdf") and (p.get("doi") or "").lower() not in attempts
    ]
    total_no_pdf = sum(1 for p in papers if not p.get("pdf"))
    if missing:
        print(f"❌ PDF 闸门未通过：{len(missing)} 篇论文无 PDF 且无跳过记录（共 {total_no_pdf} 篇无 PDF）")
        for p in missing:
            print(f"   - {p.get('title', '')[:70]}  · {p.get('doi')}")
        print("处理方式：尝试下载；确认不可得后运行 pdf_gate.py --mark <doi> <reason>（blocked/not-oa/no-file）")
        sys.exit(1)
    print(f"✅ PDF 闸门通过：{total_no_pdf} 篇无 PDF 论文全部有记录在案的跳过原因")


def list_state():
    papers = load_papers()
    attempts = load_attempts()
    for p in papers:
        if p.get("pdf"):
            continue
        doi = (p.get("doi") or "").lower()
        rec = attempts.get(doi)
        status = f"记录: {rec['reason']}（{rec.get('note', '')}）" if rec else "⚠️ 无记录"
        print(f"  - {p.get('title', '')[:60]}  · {doi}  · {status}")


def mark(doi, reason, note):
    attempts = load_attempts()
    attempts[doi.lower()] = {"reason": reason, "note": note or ""}
    save_attempts(attempts)
    print(f"已记录 {doi} → {reason}" + (f"（{note}）" if note else ""))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="PDF 获取闸门")
    ap.add_argument("--check", action="store_true", help="检查无 PDF 且无记录的论文（闸门）")
    ap.add_argument("--list", action="store_true", help="列出全部无 PDF 论文及状态")
    ap.add_argument("--mark", nargs=2, metavar=("DOI", "REASON"), help="记录跳过原因")
    ap.add_argument("--note", default="", help="mark 时的备注")
    args = ap.parse_args()

    if args.check:
        check()
    elif args.list:
        list_state()
    elif args.mark:
        mark(args.mark[0], args.mark[1], args.note)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
