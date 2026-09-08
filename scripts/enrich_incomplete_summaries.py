#!/usr/bin/env python3
"""Replace empty section placeholders with evidence-bounded structured prose.

This tool does not translate or invent findings.  It redistributes an existing
Chinese abstract by semantic cues.  When only catalog metadata exists, it makes
the inference level explicit and refuses to manufacture methods or results.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SUMMARY_DIR = ROOT / "summaries"
THEME_FILE = ROOT / "data" / "theme-tags.json"
PLACEHOLDER = "当前公开材料未覆盖本节"
SOURCE_PLACEHOLDERS = ("当前未获取可核验摘要", "摘要待补全", "取得可核验内容后补充")
SECTION_RE = re.compile(r"(^## {heading}\s*\r?\n(?:\r?\n)?)([\s\S]*?)(?=^## |^---\s*$|\Z)", re.MULTILINE)
INFO_RE = re.compile(r"^- \*\*(?P<key>[^*]+)\*\*:\s*(?P<value>.*)$", re.MULTILINE)

METHOD_CUES = re.compile(r"提出|采用|设计|构建|开发|引入|利用|框架|算法|模型|机制|策略|方法")
RESULT_CUES = re.compile(r"实验|结果|表明|显示|发现|达到|优于|显著|\d+(?:\.\d+)?%|p\s*[<=>]|验证")
CONTRIBUTION_CUES = re.compile(r"贡献|首次|揭示|证明|此外|总体|因此|为.+提供|有助于|意义")
NON_RESEARCH_TITLE = re.compile(
    r"^(editorial board|current events|.*membership.*form|.*publication information|"
    r"ieee computational intelligence society|.*information for authors)$",
    re.I,
)


def info(markdown: str) -> dict[str, str]:
    return {match.group("key").strip(): match.group("value").strip() for match in INFO_RE.finditer(markdown)}


def section(markdown: str, heading: str) -> str:
    match = re.compile(SECTION_RE.pattern.format(heading=re.escape(heading)), SECTION_RE.flags).search(markdown)
    return match.group(2).strip() if match else ""


def replace_section(markdown: str, heading: str, value: str) -> str:
    pattern = re.compile(SECTION_RE.pattern.format(heading=re.escape(heading)), SECTION_RE.flags)
    return pattern.sub(lambda match: match.group(1) + value.strip() + "\n\n", markdown, count=1)


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[。！？])\s*|(?<=[.!?])\s*(?=[A-Z\u3400-\u9fff])", clean)
    return [part.strip() for part in parts if len(part.strip()) >= 6]


def bounded(items: list[str], limit: int, maximum: int = 3) -> str:
    chosen: list[str] = []
    size = 0
    for item in items:
        if item in chosen:
            continue
        if chosen and size + len(item) > limit:
            break
        chosen.append(item)
        size += len(item)
        if len(chosen) == maximum:
            break
    return "".join(chosen)


def matching(parts: list[str], pattern: re.Pattern[str]) -> list[str]:
    return [part for part in parts if pattern.search(part)]


def structured_from_abstract(abstract: str, title: str) -> dict[str, str]:
    parts = sentences(abstract)
    if not parts:
        return structured_from_metadata(title, "人工智能", [])
    question_parts: list[str] = []
    for part in parts:
        if METHOD_CUES.search(part) and question_parts:
            break
        question_parts.append(part)
        if len(question_parts) == 2:
            break
    method_parts = matching(parts, METHOD_CUES)
    result_parts = matching(parts, RESULT_CUES)
    used = set(question_parts + method_parts + result_parts)
    contribution_parts = matching(parts, CONTRIBUTION_CUES)
    contribution_parts += [part for part in parts if part not in used and part not in contribution_parts]
    question = bounded(question_parts or parts[:1], 520, 2)
    method = bounded(method_parts or parts[1:3] or parts[:1], 800, 4)
    results = bounded(result_parts, 800, 4)
    if not results:
        results = (
            f"现有摘要围绕《{title}》描述了研究目标，但没有给出可核验的实验设置、"
            "对照方法或数值结果，因此这里不补写未经证实的结论。"
        )
    contribution = bounded(contribution_parts or parts[-2:], 800, 4)
    summary_parts = [parts[0]]
    if result_parts and result_parts[0] != parts[0]:
        summary_parts.append(result_parts[0])
    return {
        "一句话概括": bounded(summary_parts, 300, 2),
        "问题与动机": question,
        "方法": method,
        "实验与结果": results,
        "贡献与局限": contribution,
    }


def structured_from_metadata(title: str, direction: str, tags: list[str]) -> dict[str, str]:
    topic = "、".join(tags[:3]) or direction or "相关方法"
    quoted = f"《{title}》"
    return {
        "一句话概括": f"该研究围绕{quoted}所描述的任务展开，研究主题涉及{topic}。",
        "问题与动机": f"从题目可判断，论文关注{quoted}对应的{direction or '计算机科学'}问题，重点考察{topic}相关方法在目标场景中的适用性。",
        "方法": f"题目显示其技术路线以{topic}为核心；仅凭现有题录无法可靠确定具体模型结构与实现步骤。",
        "实验与结果": "现有题录没有给出可核验的实验数据、对照方法或评价指标，因此这里不补写未经证实的结果。",
        "贡献与局限": f"可确认的贡献定位是将{topic}用于题目所述任务；具体创新点、适用条件和局限仍需以论文正文为准。",
    }


def structured_nonresearch(title: str) -> dict[str, str]:
    return {
        "一句话概括": f"该 DOI 对应《{title}》期刊事务页面，而不是研究论文；条目仅保留作来源审计。",
        "问题与动机": "不适用：页面用于发布期刊组织、学会动态、会员或投稿信息，不提出研究问题。",
        "方法": "不适用：该页面不包含研究设计、模型或算法。",
        "实验与结果": "不适用：该页面没有研究实验、对照方法或结果。",
        "贡献与局限": "该条目的作用是标明非研究性来源并防止误入论文库，不应据此生成研究结论。",
    }


def transform(markdown: str, themes: dict[str, list[str]], *, restructure_existing=False, normalize_nonresearch=False) -> str:
    metadata = info(markdown)
    title = metadata.get("标题", "该论文")
    is_nonresearch = normalize_nonresearch and bool(NON_RESEARCH_TITLE.fullmatch(title.strip()))
    if PLACEHOLDER not in markdown and not restructure_existing and not is_nonresearch:
        return markdown
    direction = metadata.get("研究方向", "")
    doi = metadata.get("DOI", "").lower()
    abstract = section(markdown, "一句话概括")
    if restructure_existing and PLACEHOLDER not in markdown:
        sources = [section(markdown, heading) for heading in ("一句话概括", "问题与动机", "方法", "实验与结果", "贡献与局限")]
        unique: list[str] = []
        for sentence in sentences(" ".join(sources)):
            if sentence not in unique:
                unique.append(sentence)
        abstract = " ".join(unique)
    has_abstract = abstract and not any(marker in abstract for marker in SOURCE_PLACEHOLDERS)
    if is_nonresearch:
        fields = structured_nonresearch(title)
    else:
        fields = structured_from_abstract(abstract, title) if has_abstract else structured_from_metadata(title, direction, themes.get(doi, []))
    for heading, value in fields.items():
        markdown = replace_section(markdown, heading, value)
    if has_abstract:
        markdown = re.sub(
            r"^- \*\*内容状态\*\*: 部分[^\r\n]*$",
            "- **内容状态**: 部分 · 已依据现有摘要完成中文结构化整理；具体细节以全文为准",
            markdown,
            count=1,
            flags=re.MULTILINE,
        )
    if is_nonresearch:
        markdown = re.sub(
            r"^- \*\*内容状态\*\*: [^\r\n]*$",
            "- **内容状态**: 待补全 · 已识别为非研究性期刊页面，仅保留作来源审计",
            markdown,
            count=1,
            flags=re.MULTILINE,
        )
    return markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="用现有摘要或题录推断替换空段落占位")
    parser.add_argument("--write", action="store_true", help="写回 summaries（默认只报告）")
    parser.add_argument("--restructure-existing", action="store_true", help="重新整理已由本工具处理的 partial 条目")
    parser.add_argument("--normalize-nonresearch", action="store_true", help="把已知事务页面改写为非研究性审计说明")
    parser.add_argument("--source-revision", help="从指定 Git 修订读取原始总结再处理，例如 HEAD")
    args = parser.parse_args()
    themes = json.loads(THEME_FILE.read_text(encoding="utf-8")) if THEME_FILE.exists() else {}
    changed = 0
    for path in sorted(SUMMARY_DIR.glob("*.md")):
        current = path.read_text(encoding="utf-8")
        original = current
        if args.source_revision:
            relative = path.relative_to(ROOT).as_posix()
            result = subprocess.run(
                ["git", "show", f"{args.source_revision}:{relative}"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            if result.returncode == 0:
                original = result.stdout
        should_restructure = args.restructure_existing and "已依据现有摘要完成中文结构化整理" in original
        updated = transform(
            original,
            themes,
            restructure_existing=should_restructure,
            normalize_nonresearch=args.normalize_nonresearch,
        )
        if updated == current:
            continue
        changed += 1
        if args.write:
            path.write_text(updated, encoding="utf-8")
    action = "已更新" if args.write else "可更新"
    print(f"{action} {changed} 份总结；不会生成未经现有摘要或题录支持的实验结论。")


if __name__ == "__main__":
    main()
