#!/usr/bin/env python3
"""论文台账总体验收闸门。

三道专项闸门分别检查摘要、主题和 PDF 证据；本闸门检查它们是否仍然
指向同一份台账，防止占位文件删除、大小写 DOI 或失效链接造成静默丢条目。

用法:
  python scripts/workflow_gate.py --check
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "papers.js"
SUMMARY_DIR = ROOT / "summaries"
ATTEMPTS_FILE = ROOT / "skill-runs" / "pdf_attempts.json"
BASELINE_FILE = ROOT / "skill-runs" / "workflow_baseline.json"
SECTIONS = ("基本信息", "一句话概括", "问题与动机", "方法", "实验与结果", "贡献与局限")
ALLOWED_STATES = {"完整": "complete", "部分": "partial", "待补全": "pending"}
ALLOWED_REASONS = {"blocked", "not-oa", "no-file", "non_research_document"}
DOI_RE = re.compile(r"^\s*(?:-\s*)?\*?\*?DOI\*?\*?\s*:\s*([^\s]+)", re.IGNORECASE | re.MULTILINE)
STATE_RE = re.compile(r"^-\s+\*\*内容状态\*\*:\s*([^\r\n]+)", re.MULTILINE)
SECTION_RE = re.compile(r"^## ([^\r\n]+)\s*$", re.MULTILINE)
PLACEHOLDER_LINES = {
    "待补全。",
    "待翻译。",
    "英文机器摘要待翻译。",
    "当前未获取可核验摘要；取得可核验内容后补充。",
    "当前公开材料未覆盖本节；取得全文后补充。",
}


def load_papers() -> list[dict]:
    src = DATA_FILE.read_text(encoding="utf-8")
    match = re.search(r"=\s*(\[.*\])\s*;?\s*$", src, re.S)
    if not match:
        raise ValueError(f"解析失败: {DATA_FILE}")
    value = json.loads(match.group(1))
    if not isinstance(value, list):
        raise ValueError("data/papers.js 顶层不是数组")
    return value


def normalize_doi(value: str) -> str:
    return str(value or "").strip().lower().rstrip(".,;)")


def section_text(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*\r?\n(?:\r?\n)?([\s\S]*?)(?=^## |^---\s*$|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def summary_info(path: Path) -> tuple[str, str, list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    headings = set(SECTION_RE.findall(text))
    missing = [heading for heading in SECTIONS if heading not in headings]
    if missing:
        errors.append("缺少段落：" + "、".join(missing))

    doi_match = DOI_RE.search(text)
    doi = normalize_doi(doi_match.group(1)) if doi_match else ""
    if not doi:
        errors.append("缺少 DOI")

    state_match = STATE_RE.search(text)
    state = ""
    if not state_match:
        errors.append("缺少内容状态")
    else:
        label = state_match.group(1).split("·", 1)[0].strip()
        state = ALLOWED_STATES.get(label, "")
        if not state:
            errors.append(f"内容状态无效：{state_match.group(1).strip()}")

    if state == "complete":
        for heading in SECTIONS[1:]:
            body = section_text(text, heading)
            if body in PLACEHOLDER_LINES:
                errors.append(f"完整总结的「{heading}」仍是占位内容")

    return doi, state, errors


def valid_pdf_path(value: str) -> tuple[bool, str]:
    relative = str(value or "").replace("\\", "/")
    if not relative or not relative.startswith("papers/"):
        return False, "PDF 路径必须位于 papers/ 下"
    target = (ROOT / Path(relative)).resolve()
    papers_root = (ROOT / "papers").resolve()
    try:
        target.relative_to(papers_root)
    except ValueError:
        return False, "PDF 路径越出 papers/"
    if not target.is_file():
        return False, f"PDF 文件不存在：{relative}"
    try:
        with target.open("rb") as stream:
            head = stream.read(5)
            size = target.stat().st_size
            stream.seek(max(0, size - 16))
            tail = stream.read(16)
    except OSError as exc:
        return False, f"PDF 无法读取：{exc}"
    if not head.startswith(b"%PDF") or b"%EOF" not in tail:
        return False, f"PDF 文件头/尾校验失败：{relative}"
    return True, ""


def validate_attempt(doi: str, record: object) -> str | None:
    if not isinstance(record, dict):
        return "跳过记录不是对象"
    reason = str(record.get("reason") or "")
    if reason not in ALLOWED_REASONS:
        return f"跳过原因无效：{reason or '(空)'}"
    if not str(record.get("note") or "").strip():
        return "跳过记录缺少可审计 note"
    if reason == "non_research_document" and not any(
        word in str(record.get("note")) for word in ("非研究", "编委", "投稿", "出版信息", "名单")
    ):
        return "non_research_document 缺少非研究性说明"
    return None


def legacy_partial_pdf_limit() -> int | None:
    if not BASELINE_FILE.exists():
        return None
    try:
        payload = json.loads(BASELINE_FILE.read_text(encoding="utf-8"))
        value = payload.get("legacy_partial_pdf_max")
        return int(value) if value is not None else None
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return None


def check() -> int:
    errors: list[str] = []
    legacy_partial_pdf: list[str] = []
    papers = load_papers()
    attempts = json.loads(ATTEMPTS_FILE.read_text(encoding="utf-8")) if ATTEMPTS_FILE.exists() else {}
    if not isinstance(attempts, dict):
        errors.append("pdf_attempts.json 顶层不是对象")
        attempts = {}

    summary_by_doi: dict[str, Path] = {}
    summary_states: dict[str, str] = {}
    for path in sorted(SUMMARY_DIR.glob("*.md")):
        try:
            doi, state, file_errors = summary_info(path)
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.name}: 无法读取：{exc}")
            continue
        for message in file_errors:
            errors.append(f"{path.name}: {message}")
        if doi:
            if doi in summary_by_doi:
                errors.append(f"DOI 重复于总结：{doi}（{summary_by_doi[doi].name} 与 {path.name}）")
            summary_by_doi[doi] = path
            summary_states[doi] = state

    paper_by_doi: dict[str, dict] = {}
    for index, paper in enumerate(papers):
        doi = normalize_doi(paper.get("doi"))
        if not doi:
            errors.append(f"data/papers.js 第 {index + 1} 条缺少 DOI")
            continue
        if doi in paper_by_doi:
            errors.append(f"DOI 重复于台账：{doi}")
        paper_by_doi[doi] = paper
        if doi not in summary_by_doi:
            errors.append(f"台账 DOI 没有对应总结：{doi}")
        state = str(paper.get("contentState") or "")
        if state not in {"complete", "partial", "pending"}:
            errors.append(f"{doi}: contentState 无效或为空：{state or '(空)'}")
        elif summary_states.get(doi) and summary_states[doi] != state:
            errors.append(f"{doi}: data 状态 {state} 与总结状态 {summary_states[doi]} 不一致")
        if not isinstance(paper.get("tags"), list) or not paper.get("tags"):
            errors.append(f"{doi}: 缺少主题标签")

        pdf = str(paper.get("pdf") or "")
        if pdf:
            ok, detail = valid_pdf_path(pdf)
            if not ok:
                errors.append(f"{doi}: {detail}")
            elif state == "partial":
                legacy_partial_pdf.append(doi)
        else:
            reason_error = validate_attempt(doi, attempts.get(doi))
            if reason_error:
                errors.append(f"{doi}: {reason_error}")

    paper_dois = set(paper_by_doi)
    summary_dois = set(summary_by_doi)
    for doi in sorted(summary_dois - paper_dois):
        errors.append(f"总结 DOI 没有对应台账：{doi}")
    if len(papers) != len(summary_by_doi):
        errors.append(f"台账/总结数量不一致：{len(papers)} / {len(summary_by_doi)}")

    limit = legacy_partial_pdf_limit()
    if limit is not None and len(legacy_partial_pdf) > limit:
        errors.append(
            f"已有 PDF 但 partial 的数量增加：当前 {len(legacy_partial_pdf)}，基线允许最多 {limit}；"
            "请先完成全文六段式总结并升级为 complete。"
        )

    if errors:
        print(f"❌ 工作流总体验收未通过：{len(errors)} 项")
        for error in errors[:80]:
            print("   - " + error)
        if len(errors) > 80:
            print(f"   …其余 {len(errors) - 80} 项略")
        return 1

    print(f"✅ 工作流总体验收通过：{len(papers)} 条台账、{len(summary_by_doi)} 份总结，DOI/状态/主题/PDF/跳过证据一致")
    if legacy_partial_pdf:
        print(f"⚠️ 历史技术债：{len(legacy_partial_pdf)} 篇已有 PDF 但内容状态仍为 partial；新一轮不得继续增加，后续应读全文升级为完整总结。")
    return 0


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="论文台账总体验收闸门")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        parser.print_help()
        return
    raise SystemExit(check())


if __name__ == "__main__":
    main()
