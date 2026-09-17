#!/usr/bin/env python3
"""Deep module that owns the complete publication validation sequence."""

from __future__ import annotations

import subprocess
from collections.abc import Callable, Iterable
from pathlib import Path

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
    log(f"网站布局、收起、PDF 导航与论文时间顺序检查{suffix}…")
    result = subprocess.run(
        ["node", ROOT / "tests" / "site-regressions-check.js"],
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
        raise SystemExit("网站布局、收起、PDF 导航或论文时间顺序检查未通过，不能继续。")


def _standard_checks(include_pdf_integrity: bool) -> list[Check]:
    """Return the non-browser gates without running a weaker duplicate PDF check."""
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
    # workflow_gate validates PDF existence/header/tail and the stronger
    # no-PDF attempt reason/note contract, so pdf_gate.check would only
    # repeat a weaker subset here. Keep pdf_gate.py --list for human triage.
    checks.append(("论文台账总体验收", workflow_gate.check, "台账总体验收未通过，不能继续。"))
    return checks


def validate_workflow(
    *,
    context: str = "",
    include_pdf_integrity: bool = False,
    log: Callable[[str], None] = print,
) -> None:
    """Run every required gate through one stable orchestration interface."""
    _run_checks(_standard_checks(include_pdf_integrity), context, log)
    _layout_check(log, context)
