#!/usr/bin/env python3
"""Deep module that owns the complete publication validation sequence."""

from __future__ import annotations

import subprocess
from collections.abc import Callable, Iterable
from pathlib import Path

import pdf_gate
import summary_gate
import summary_quality_gate
import theme_gate
import verify_papers
import workflow_gate


ROOT = Path(__file__).resolve().parent.parent
Check = tuple[str, Callable[[], int | None], str]


def _run_checks(checks: Iterable[Check], context: str, log: Callable[[str], None]) -> None:
    suffix = f"（{context}）" if context else ""
    for label, check, failure_message in checks:
        log(f"{label}{suffix}…")
        try:
            result = check()
        except SystemExit as exc:
            result = exc.code if isinstance(exc.code, int) else 1
        if result not in (None, 0):
            raise SystemExit(failure_message)


def _layout_check(log: Callable[[str], None], context: str) -> None:
    suffix = f"（{context}）" if context else ""
    log(f"网站布局与收起交互检查{suffix}…")
    for script in ("layout-overflow-check.js", "latest-collapse-check.js"):
        result = subprocess.run(
            ["node", ROOT / "tests" / script],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.stdout:
            log(result.stdout.rstrip())
        if result.stderr:
            log(result.stderr.rstrip())
        if result.returncode != 0:
            raise SystemExit("网站布局或收起交互检查未通过，不能继续。")


def validate_workflow(
    *,
    context: str = "",
    include_pdf_integrity: bool = False,
    log: Callable[[str], None] = print,
) -> None:
    """Run every required gate through one stable orchestration interface."""
    checks: list[Check] = [
        ("中文六段式摘要闸门检查", summary_gate.check, "中文摘要闸门未通过，不能继续。"),
        ("中文文案质量闸门检查", summary_quality_gate.check, "中文文案质量闸门未通过，不能继续。"),
        ("主题标签闸门检查", theme_gate.check, "主题标签闸门未通过，不能继续。"),
    ]
    if include_pdf_integrity:
        checks.append(
            (
                "papers/ PDF 有效性检查",
                lambda: verify_papers.check_pdfs(delete_invalid=True),
                "papers/ 存在无法清理的无效 PDF，不能继续。",
            )
        )
    checks.extend(
        [
            ("PDF 获取闸门检查", pdf_gate.check, "PDF 闸门未通过，不能继续。"),
            ("论文台账总体验收", workflow_gate.check, "台账总体验收未通过，不能继续。"),
        ]
    )
    _run_checks(checks, context, log)
    _layout_check(log, context)
