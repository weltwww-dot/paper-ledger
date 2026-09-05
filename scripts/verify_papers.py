#!/usr/bin/env python3
"""校验 papers/ 下的 PDF 有效性，防止下载失败的 HTML 垃圾被提交进仓库。

规则：有效 PDF = 文件头 `%PDF` + 文件尾 16 字节内含 `%%EOF`。

用法:
  python scripts/verify_papers.py            # 校验并删除无效残留，打印报告
  python scripts/verify_papers.py --check    # 只检查不删除（供 QA/CI）
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"


def is_valid_pdf(path):
    try:
        with open(path, "rb") as f:
            head = f.read(5)
            size = path.stat().st_size
            f.seek(max(0, size - 16))
            tail = f.read(16)
        return head.startswith(b"%PDF") and b"%EOF" in tail
    except Exception:
        return False


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查不删除")
    args = ap.parse_args()

    if not PAPERS.exists():
        print("papers/ 不存在，跳过。")
        return

    bad = []
    for f in sorted(PAPERS.glob("*.pdf")):
        if not is_valid_pdf(f):
            bad.append(f)

    if not bad:
        total = len(list(PAPERS.glob("*.pdf")))
        print(f"✅ papers/ 全部 {total} 个 PDF 有效")
        return

    for f in bad:
        head = f.read_bytes()[:24] if f.exists() else b""
        print(f"[无效] {f.name}  (头部: {head[:24]!r})")
        if not args.check:
            f.unlink(missing_ok=True)
            print(f"   → 已删除")

    if args.check:
        print(f"发现 {len(bad)} 个无效 PDF（未删除，--check 模式）")
        sys.exit(1)
    print(f"已清理 {len(bad)} 个无效残留文件。")


if __name__ == "__main__":
    main()
