# -*- coding: utf-8 -*-
"""独立复核 papers/ 顶层现有 49 个 PDF 的首页版本标记，建立基线。"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nonfinal_registry import REGISTRY  # noqa: E402
from nonfinal_audit import read_first_pages, version_of, classify, pdf_ok  # noqa: E402

ROOT = r"D:\codex\博客网站"
OUT = os.path.join(ROOT, "skill-runs", "nonfinal_2026-09-10")

rows = []
for doi, rel, title, cls in REGISTRY:
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    if not os.path.exists(p):
        rows.append({"doi": doi, "path": rel, "exists": False})
        continue
    try:
        txt, n = read_first_pages(p)
        hits = version_of(txt)
        rows.append({
            "doi": doi, "path": rel, "exists": True, "pdf_ok": pdf_ok(p),
            "pages": n, "marker_hits": hits, "version": classify(hits, txt),
            "head": txt[:260].replace("\n", " | "),
        })
    except Exception as e:  # noqa: BLE001
        rows.append({"doi": doi, "path": rel, "exists": True, "error": str(e)})

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "baseline.json"), "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

from collections import Counter
print(Counter(r.get("version") for r in rows))
for r in rows:
    print("%-38s %s | %s" % (r["doi"], r.get("version", "MISSING"), (r.get("marker_hits") or [])[:3]))
