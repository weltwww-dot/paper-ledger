#!/usr/bin/env python3
"""六段式中文总结的基础文案质量闸门。

该闸门补足结构检查：面向网站展示的总结不得留下要求人工确认的字样，
也不得含有常见乱码或未解码的 HTML 实体。它不把“尚无公开材料”误判为
内容完整；信息缺口必须用可核验、面向事实的中文说明表达。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SUMMARY_DIR = ROOT / "summaries"
FORBIDDEN_PHRASES = ("待人工", "人工确认", "人工核验", "人工补全")
BROKEN_MARKERS = ("\ufffd", "&#", "&lt;", "&gt;")


def validate_markdown(name: str, markdown: str) -> list[str]:
    errors: list[str] = []
    for phrase in FORBIDDEN_PHRASES:
        if phrase in markdown:
            errors.append(f"含有不应展示的流程措辞：{phrase}")
    for marker in BROKEN_MARKERS:
        if marker in markdown:
            errors.append(f"含有未清理的乱码或实体：{marker}")
    return errors


def check(summary_dir: Path = SUMMARY_DIR) -> int:
    failures: list[tuple[str, list[str]]] = []
    files = sorted(summary_dir.glob("*.md"))
    for file in files:
        errors = validate_markdown(file.name, file.read_text(encoding="utf-8"))
        if errors:
            failures.append((file.name, errors))
    if failures:
        print(f"❌ 中文文案质量闸门未通过：{len(failures)}/{len(files)} 份总结存在展示问题")
        for name, errors in failures[:80]:
            print(f"   - {name}：{'；'.join(errors)}")
        if len(failures) > 80:
            print(f"   …其余 {len(failures) - 80} 项略")
        return 1
    print(f"✅ 中文文案质量闸门通过：{len(files)} 份总结未含人工确认措辞、乱码或未解码实体")
    return 0


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="六段式中文文案质量闸门")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        raise SystemExit(check())
    parser.print_help()


if __name__ == "__main__":
    main()
