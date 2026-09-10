# -*- coding: utf-8 -*-
"""对重取到的 PDF 做 %PDF 校验 / 身份匹配 / 版本判定，并输出可审计证据。

用法:
  python nonfinal_audit.py <batch_out_dir> [<batch_out_dir> ...]
输出:
  skill-runs/nonfinal_2026-09-10/audit.json
  skill-runs/nonfinal_2026-09-10/audit.md
"""
import csv
import hashlib
import json
import os
import re
import sys

import fitz  # PyMuPDF

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nonfinal_registry import REGISTRY, BY_DOI  # noqa: E402

ROOT = r"D:\codex\博客网站"
OUT = os.path.join(ROOT, "skill-runs", "nonfinal_2026-09-10")

MARKERS = [
    ("journal_pre_proof", "journal pre-proof"),
    ("accepted_manuscript", "accepted manuscript"),
    ("preprint_submitted", "preprint submitted to"),
    ("under_review", "under review"),
    ("submitted_to", "submitted to "),
    ("manuscript_note", "this manuscript"),
    ("early_access_ieee", "this article has been accepted for publication"),
    ("elsevier_not_final", "this is a pdf file of an article that has not undergone"),
    ("arxiv_preprint", "arxiv preprint"),
    ("author_manuscript", "author manuscript"),
]

STOP = {"a", "an", "the", "of", "for", "and", "or", "to", "in", "on",
        "with", "via", "from", "by", "is", "are", "at", "as"}


def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def read_first_pages(path, n=2):
    doc = fitz.open(path)
    try:
        txt = "\n".join(doc[i].get_text("text") for i in range(min(n, doc.page_count)))
        return txt, doc.page_count
    finally:
        doc.close()


def version_of(txt):
    low = txt.lower()
    hits = [k for k, m in MARKERS if m in low]
    arxiv_id = re.search(r"arxiv:\s*(\d{4}\.\d{4,5})(v\d+)?", low)
    if arxiv_id:
        hits.append("arxiv_id:%s" % arxiv_id.group(1))
    return hits


def classify(hits, txt):
    low = txt.lower()
    if "journal_pre_proof" in hits or "elsevier_not_final" in hits:
        return "Journal Pre-proof（非最终版）"
    if "accepted_manuscript" in hits or "early_access_ieee" in hits:
        return "accepted manuscript（已录用未排版）"
    if "preprint_submitted" in hits or "under_review" in hits:
        return "preprint/submitted（投稿中）"
    if any(h.startswith("arxiv_id:") for h in hits) or "arxiv_preprint" in hits:
        return "arXiv 预印本"
    if "author_manuscript" in hits:
        return "author manuscript"
    # 无负面标记 -> 看正面证据
    if "sciencedirect" in low or "elsevier" in low:
        return "Elsevier 页面（未见预出版标记，疑似 VoR，需人工确认卷期页码）"
    if "ieee" in low:
        return "IEEE 页面（未见 early-access 标记，疑似 VoR，需人工确认）"
    if "springer" in low or "nature" in low:
        return "Springer/Nature 页面（未见预出版标记，疑似 VoR，需人工确认）"
    return "未识别（需人工复核首页）"


def pdf_ok(path):
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(dirs):
    found = {}  # doi_lower -> record
    for d in dirs:
        mani = os.path.join(d, "complete", "manifest.csv")
        if not os.path.exists(mani):
            print("skip (no manifest): %s" % d)
            continue
        with open(mani, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                doi = (row.get("doi") or "").strip()
                if not doi:
                    continue
                p = (row.get("pdf_path") or "").strip()
                rec = {
                    "doi_input": doi,
                    "batch": os.path.basename(d.rstrip("\\/")),
                    "status": row.get("status"),
                    "standard_status": row.get("standard_status"),
                    "result_evidence": row.get("result_evidence"),
                    "reason": row.get("reason"),
                    "pdf_url": row.get("pdf_url"),
                    "pdf_path": p,
                    "verified_match": row.get("verified_match"),
                    "size_bytes": row.get("size_bytes"),
                }
                found.setdefault(doi.lower(), []).append(rec)

    results = []
    for doi, cur_pdf, title, cls in REGISTRY:
        key = doi.lower()
        recs = found.get(key, [])
        ok = [r for r in recs if r["status"] == "success" and r["pdf_path"] and os.path.exists(r["pdf_path"])]
        entry = {
            "doi": doi, "current_pdf": cur_pdf, "title": title, "audit_class": cls,
            "fetch_attempts": recs,
        }
        if not ok:
            entry["outcome"] = "no_pdf"
            entry["version"] = "未取到（沿用现有文件）"
            entry["action"] = "保留现有 PDF，标注非最终版本"
            results.append(entry)
            continue
        r = ok[-1]
        path = r["pdf_path"]
        entry["pdf_ok"] = pdf_ok(path)
        try:
            txt, npage = read_first_pages(path)
        except Exception as e:  # noqa: BLE001
            entry["outcome"] = "read_error"
            entry["error"] = str(e)
            results.append(entry)
            continue
        entry.update({
            "outcome": "ok",
            "new_pdf": path,
            "pages": npage,
            "source_url": r["pdf_url"],
            "evidence": r["result_evidence"],
            "marker_hits": version_of(txt),
            "version": classify(version_of(txt), txt),
            "first_page_head": txt[:400].replace("\n", " | "),
        })
        # 身份匹配：标题 token 交集率
        tt = tokens(title)
        pt = tokens(txt[:2500])
        inter = tt & pt
        entry["title_match_ratio"] = round(len(inter) / max(len(tt), 1), 3)
        entry["doi_on_page"] = doi.lower() in txt.lower()
        entry["identity_ok"] = entry["title_match_ratio"] >= 0.5 and entry["doi_on_page"]
        # 与现有文件比较
        cur_abs = os.path.join(ROOT, cur_pdf.replace("/", os.sep))
        if os.path.exists(cur_abs):
            entry["same_as_current"] = md5(cur_abs) == md5(path)
        else:
            entry["same_as_current"] = None
        results.append(entry)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "audit.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    lines = ["| DOI | 类别 | 重取状态 | 证据类型 | %PDF | 身份匹配 | 版本判定 | 与现有文件相同 | 来源 |",
             "|---|---|---|---|---|---|---|---|---|"]
    for e in results:
        lines.append("| `{doi}` | {c} | {o} | {ev} | {p} | {id} | {v} | {s} | {u} |".format(
            doi=e["doi"], c=e.get("audit_class"), o=e.get("outcome"),
            ev=e.get("evidence") or e.get("reason") or "-",
            p=e.get("pdf_ok"), id=e.get("identity_ok"), v=e.get("version"),
            s=e.get("same_as_current"), u=(e.get("source_url") or "-")[:60]))
    with open(os.path.join(OUT, "audit.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ok_n = sum(1 for e in results if e.get("outcome") == "ok")
    vor_n = sum(1 for e in results if e.get("version", "").startswith(("Elsevier 页面", "IEEE 页面", "Springer")))
    same_n = sum(1 for e in results if e.get("same_as_current") is True)
    print("total=%d  refetched_ok=%d 疑似VoR=%d 与现有文件完全相同=%d" % (len(results), ok_n, vor_n, same_n))
    for e in results:
        print(" %-38s %-12s %s | same=%s | %s" % (
            e["doi"], e.get("audit_class"), e.get("version"), e.get("same_as_current"),
            (e.get("marker_hits") or [])[:3]))


if __name__ == "__main__":
    main(sys.argv[1:])
