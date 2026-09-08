#!/usr/bin/env python3
"""中文六段式摘要闸门。

更新不能只把英文机器摘要写入台账。这个闸门确认每份总结都有六段式结构，且
「一句话概括」含中文；「部分」状态还必须有真实的、已翻译的概括，而不是占位符。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SUMMARY_DIR = ROOT / "summaries"
SECTIONS = ("基本信息", "一句话概括", "问题与动机", "方法", "实验与结果", "贡献与局限")
SECTION_RE = re.compile(r"^## ([^\r\n]+)\s*$", re.MULTILINE)
CHINESE_RE = re.compile(r"[\u3400-\u9fff]")
STATE_RE = re.compile(r"^- \*\*内容状态\*\*:\s*([^\r\n]+)", re.MULTILINE)
PLACEHOLDERS = {"摘要待补全。", "待翻译。", "英文机器摘要待翻译。"}


def section_text(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*\r?\n(?:\r?\n)?([\s\S]*?)(?=^## |^---\s*$|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def validate_markdown(name: str, markdown: str) -> list[str]:
    errors: list[str] = []
    headings = set(SECTION_RE.findall(markdown))
    missing = [heading for heading in SECTIONS if heading not in headings]
    if missing:
        errors.append(f"缺少段落：{'、'.join(missing)}")
        return errors

    summary = section_text(markdown, "一句话概括")
    if not summary:
        errors.append("「一句话概括」为空")
        return errors
    if not CHINESE_RE.search(summary):
        errors.append("「一句话概括」未完成中文翻译")

    state = STATE_RE.search(markdown)
    if state and state.group(1).strip().startswith("部分") and summary in PLACEHOLDERS:
        errors.append("内容状态为「部分」但摘要仍是占位符")
    return errors


def check(summary_dir: Path = SUMMARY_DIR) -> int:
    files = sorted(summary_dir.glob("*.md"))
    failures: list[tuple[str, list[str]]] = []
    for file in files:
        errors = validate_markdown(file.name, file.read_text(encoding="utf-8"))
        if errors:
            failures.append((file.name, errors))

    if failures:
        print(f"❌ 中文摘要闸门未通过：{len(failures)}/{len(files)} 份总结不符合要求")
        for name, errors in failures:
            print(f"   - {name}：{'；'.join(errors)}")
        print("处理方式：由当前执行 agent 对照可核验原文亲自撰写中文六段式；缺摘要的文章保留「待补全」状态。")
        return 1
    print(f"✅ 中文摘要闸门通过：{len(files)} 份总结均具备六段式结构，且「一句话概括」为中文")
    return 0


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="中文六段式摘要闸门")
    parser.add_argument("--check", action="store_true", help="校验 summaries/ 下全部总结")
    args = parser.parse_args()
    if args.check:
        raise SystemExit(check())
    parser.print_help()


if __name__ == "__main__":
    main()
