#!/usr/bin/env python3
"""主题标签闸门：网站数据中的每篇 DOI 必须有至少一个主题。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "papers.js"
THEME_FILE = ROOT / "data" / "theme-tags.json"


def missing_tags() -> list[dict]:
    source = DATA_FILE.read_text(encoding="utf-8")
    match = re.search(r"=\s*(\[.*\])\s*;?\s*$", source, re.S)
    if not match:
        raise SystemExit(f"解析失败: {DATA_FILE}")
    papers = json.loads(match.group(1))
    themes = json.loads(THEME_FILE.read_text(encoding="utf-8")) if THEME_FILE.exists() else {}
    return [paper for paper in papers if not themes.get(str(paper.get("doi") or "").lower())]


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="主题标签闸门")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        parser.print_help()
        return
    missing = missing_tags()
    if missing:
        print(f"❌ 主题标签闸门未通过：{len(missing)} 篇论文没有主题标签")
        for paper in missing[:20]:
            print(f"   - {paper.get('title', '')[:70]} · {paper.get('doi')}")
        if len(missing) > 20:
            print(f"   …其余 {len(missing) - 20} 篇略")
        print("处理方式：python scripts/fill_theme_tags.py --write；再人工复核具体主题。")
        raise SystemExit(1)
    print("✅ 主题标签闸门通过：每篇论文均至少有一个主题标签")


if __name__ == "__main__":
    main()
