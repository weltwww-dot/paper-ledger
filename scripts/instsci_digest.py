#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把一个批次的全文本压缩成"精读摘要"，供执行 agent 对照原文撰写中文六段式。

用法（须用带 fitz 的 InstSci venv 解释器）：
  python scripts/instsci_digest.py skill-runs/missing_pdf_2026-09-09/tasks/<batch>_tasks.json [最大字符数]

输出：skill-runs/txt/<batch>/_digest/<slug>.md
只做机械抽取，不做改写/翻译/总结。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTION_HINTS = [
    ("abstract", r"^\s*a\s*b\s*s\s*t\s*r\s*a\s*c\s*t"),
    ("intro", r"^\s*(i{1,2}|1)[\.\)]\s*(introduction|intro)\b"),
    ("method", r"^\s*(iii|3|iv|4)[\.\)]\s*(method|methodology|approach|proposed)\b"),
    ("experiments", r"^\s*(iv|v|5|6)[\.\)]\s*(experiment|experimental|evaluation|results)\b"),
    ("conclusion", r"^\s*(v|vi|vii|6|7|8)[\.\)]\s*(conclusion|discussion)\b"),
]


def digest(text: str, limit: int) -> str:
    lines = [l.rstrip() for l in text.splitlines()]
    # 段落切分（保留空行结构）
    paras, buf = [], []
    for l in lines:
        if l.strip():
            buf.append(l.strip())
        else:
            if buf:
                paras.append(" ".join(buf))
                buf = []
    if buf:
        paras.append(" ".join(buf))

    head = paras[:6]  # 标题/作者/摘要
    # 结尾优先取真正的结论/贡献章节
    concl_idx = None
    for i, p in enumerate(paras):
        if re.search(r"(^|\s)(v|vi|vii|viii|6|7|8|9)[\.\)]?\s*(conclusion|discussion|summary)s?\b", p, re.I):
            concl_idx = i
    if concl_idx is not None:
        tail = paras[concl_idx:]
    else:
        tail = paras[-(len(paras) // 10 + 6):] if len(paras) > 20 else paras[len(paras) // 2:]

    def clip(items, budget):
        out, n = [], 0
        for p in items:
            room = budget - n
            if room <= 200:
                break
            if len(p) > room:
                out.append(p[:room] + " …")
                n += room
                break
            out.append(p)
            n += len(p)
        return out

    picked, used = [], set()
    def add(items):
        for p in items:
            if p not in used:
                used.add(p)
                picked.append(p)

    # 固定预算：头(摘要)30%、结尾(结论/贡献)30%、章节与方法 25%、量化结果 15%
    add(clip(head, int(limit * 0.30)))
    add(clip(tail, int(limit * 0.30)))
    for key, pat in SECTION_HINTS:
        hits = [p for p in paras if re.search(pat, p, re.I | re.M)][:3]
        add(clip(hits, int(limit * 0.06)))
    num = [p for p in paras if re.search(r"\b\d+\.\d+\s?%|\bimprove[sd]?\b|\boutperform|\bstate-of-the-art|\bSOTA|accuracy of|we achieve", p, re.I)]
    add(clip(num, int(limit * 0.15)))

    body = "\n\n".join(picked)
    if len(body) > limit:
        body = body[:limit] + "\n…[截断]"
    # 折行，避免单行过长被阅读工具截断
    import textwrap
    wrapped = []
    for para in body.split("\n\n"):
        if len(para) <= 160:
            wrapped.append(para)
        else:
            wrapped.append("\n".join(textwrap.wrap(para, 160, break_long_words=False, break_on_hyphens=False)))
    return "\n\n".join(wrapped)


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python scripts/instsci_digest.py <tasks.json> [limit]")
        return 2
    tasks_path = os.path.join(ROOT, sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 9000
    tasks = json.load(open(tasks_path, encoding="utf-8"))
    out_root = None
    n = 0
    for t in tasks:
        txt = t.get("txt")
        if not txt:
            continue
        src = os.path.join(ROOT, txt)
        if not os.path.isfile(src):
            continue
        out_dir = os.path.join(os.path.dirname(src), "_digest")
        os.makedirs(out_dir, exist_ok=True)
        out_root = out_dir
        text = open(src, encoding="utf-8", errors="ignore").read()
        slug = os.path.basename(t["canonical_pdf"]).rsplit(".", 1)[0]
        with open(os.path.join(out_dir, slug + ".md"), "w", encoding="utf-8") as fh:
            fh.write(f"# {t['title']}\n\nDOI: {t['doi']}\n期刊: {t['journal']} {t['year']}\n\n")
            fh.write(digest(text, limit))
        n += 1
    print(f"生成精读摘要 {n} 篇 -> {os.path.relpath(out_root, ROOT) if out_root else '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
