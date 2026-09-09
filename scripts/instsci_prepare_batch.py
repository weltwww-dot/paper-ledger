#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""InstSci 批次产物 → 入库任务清单。

用法（须用带 fitz 的 InstSci venv 解释器）：
  python scripts/instsci_prepare_batch.py papers/instsci/<batch_dir>

作用：
1. 读取批次 complete/manifest.csv，只取 status=success 且 verified_match 为真、PDF 存在的条目；
2. 按期刊映射 PDF 前缀，按标题生成唯一 ASCII slug；
3. 用 PyMuPDF 提取全文到 skill-runs/txt/<batch>/<slug>.txt；
4. 在 summaries/ 下按 DOI 定位占位总结（待补全_*.md 或已有 _总结.md）；
5. 输出 skill-runs/missing_pdf_2026-09-09/tasks/<batch>_tasks.json。

只做登记与提取，不写中文总结、不改台账。
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JOURNAL_PREFIX = [
    ("Neural Networks", "NN"),
    ("Transactions on Neural Networks and Learning Systems", "TNNLS"),
    ("TNNLS", "TNNLS"),
    ("Transactions on Dependable and Secure Computing", "TDSC"),
    ("Transactions on Pattern Analysis and Machine Intelligence", "TPAMI"),
    ("TPAMI", "TPAMI"),
    ("Transactions on Artificial Intelligence", "TAI"),
    ("TAI", "TAI"),
    ("Transactions on Knowledge and Data Engineering", "TKDE"),
    ("TKDE", "TKDE"),
    ("Transactions on Information Forensics and Security", "TIFS"),
    ("Computers & Security", "COSE"),
    ("Computers and Security", "COSE"),
    ("Artificial Intelligence", "AIJ"),
    ("Nature Machine Intelligence", "NMI"),
    ("Machine Learning", "ML"),
    ("ACM TOPS", "TOPS"),
    ("Cybersecurity", "CYSEC"),
    ("JCS", "JCS"),
]

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "for", "with", "on", "in", "to", "via",
    "from", "by", "at", "is", "are", "be", "using", "based", "towards", "toward",
    "novel", "deep", "learning", "neural", "network", "networks", "via", "your",
    "we", "its", "it", "this", "that", "can", "does", "do",
}


def prefix_of(journal: str) -> str:
    j = (journal or "").strip()
    for key, pref in JOURNAL_PREFIX:
        if key.lower() in j.lower():
            return pref
    # 兜底：取 DOI 无法判断时用期刊首字母大写
    letters = re.findall(r"[A-Za-z]", j)
    return ("".join(letters[:4]).upper() or "MISC")


def slugify(title: str, max_words: int = 4) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title or "")
    kept = [w for w in words if w.lower() not in STOPWORDS][:max_words]
    if not kept:
        kept = words[:max_words]
    slug = "".join(w[:1].upper() + w[1:] for w in kept)
    slug = re.sub(r"[^A-Za-z0-9]", "", slug)
    return slug or "Paper"


def unique_slug(base: str, prefix: str, year: str, taken: set) -> str:
    slug = base
    i = 1
    while f"{prefix}_{year}_{slug}.pdf" in taken:
        i += 1
        slug = f"{base}{i:02d}"
    taken.add(f"{prefix}_{year}_{slug}.pdf")
    return slug


def load_ledger() -> dict:
    """从 data/papers.js 读取 doi -> {journal, year, direction}。"""
    path = os.path.join(ROOT, "data", "papers.js")
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    data = json.loads(src[src.index("["):src.rindex("]") + 1])
    out = {}
    for p in data:
        doi = (p.get("doi") or "").strip().lower()
        if doi:
            out[doi] = {
                "journal": p.get("journal", ""),
                "year": str(p.get("year") or "")[:4] or "2026",
                "direction": p.get("direction", ""),
            }
    return out


def find_placeholder(doi: str) -> str:
    if not doi:
        return ""
    sdir = os.path.join(ROOT, "summaries")
    target = f"DOI: {doi}".lower()
    hits = []
    for name in os.listdir(sdir):
        if not name.endswith(".md"):
            continue
        path = os.path.join(sdir, name)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue
        if target in text.lower():
            hits.append("summaries/" + name)
    # 优先占位文件
    for h in hits:
        if "待补全_" in h:
            return h
    return hits[0] if hits else ""


def extract_text(pdf_path: str, out_path: str) -> int:
    import fitz  # PyMuPDF（InstSci venv 提供）
    doc = fitz.open(pdf_path)
    parts = []
    for page in doc:
        parts.append(page.get_text("text"))
    doc.close()
    text = "\n".join(parts)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return len(text)


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python scripts/instsci_prepare_batch.py papers/instsci/<batch_dir>")
        return 2
    batch_rel = sys.argv[1].replace("\\", "/").rstrip("/")
    batch_dir = os.path.join(ROOT, batch_rel)
    batch_name = os.path.basename(batch_dir)
    manifest = os.path.join(batch_dir, "complete", "manifest.csv")
    if not os.path.isfile(manifest):
        print("找不到 manifest:", manifest)
        return 1

    taken = set(os.listdir(os.path.join(ROOT, "papers")))
    ledger = load_ledger()
    tasks = []
    txt_dir = os.path.join(ROOT, "skill-runs", "txt", batch_name)
    os.makedirs(txt_dir, exist_ok=True)

    with open(manifest, "r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    ok = fail = 0
    for row in rows:
        status = (row.get("status") or "").strip().lower()
        verified = (row.get("verified_match") or "").strip().lower() in ("true", "1", "yes")
        pdf_path = (row.get("pdf_path") or "").strip()
        if status != "success" or not verified or not pdf_path or not os.path.isfile(pdf_path):
            fail += 1
            continue
        doi = (row.get("doi") or "").strip()
        title = (row.get("title") or "").strip()
        meta = ledger.get(doi.lower(), {})
        journal = meta.get("journal") or ""
        year = meta.get("year") or ((row.get("published") or "")[:4]) or "2026"
        prefix = prefix_of(journal)
        slug = unique_slug(slugify(title), prefix, year, taken)
        txt_path = os.path.join(txt_dir, slug + ".txt")
        try:
            n = extract_text(pdf_path, txt_path)
        except Exception as exc:  # 提取失败不阻断登记
            txt_path = ""
            n = 0
            print("[warn] 提取失败", doi, exc)
        tasks.append({
            "doi": doi,
            "title": title,
            "journal": journal,
            "prefix": prefix,
            "year": year,
            "pdf_src": pdf_path.replace("\\", "/"),
            "txt": os.path.relpath(txt_path, ROOT).replace("\\", "/") if txt_path else "",
            "placeholder": find_placeholder(doi),
            "canonical_pdf": f"papers/{prefix}_{year}_{slug}.pdf",
            "text_chars": n,
            "evidence": (row.get("result_evidence") or "").strip(),
        })
        ok += 1

    out_dir = os.path.join(ROOT, "skill-runs", "missing_pdf_2026-09-09", "tasks")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{batch_name}_tasks.json")
    with open(out_file, "w", encoding="utf-8") as fh:
        json.dump(tasks, fh, ensure_ascii=False, indent=2)
    print(f"批次 {batch_name}: 成功登记 {ok} 篇，未通过 {fail} 篇")
    print("任务清单:", os.path.relpath(out_file, ROOT).replace("\\", "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
