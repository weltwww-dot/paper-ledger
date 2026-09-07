#!/usr/bin/env python3
"""下载本轮 PDF 探测出的可靠候选，并回写待处理总结的本地 PDF 路径。"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "skill-runs"
sys.path.insert(0, str(ROOT / "scripts"))
from smart_pdf import try_download  # noqa: E402


DOWNLOADABLE = {"direct", "arxiv", "article-pdf"}


def slug(doi: str) -> str:
    return hashlib.sha1(doi.encode("utf-8")).hexdigest()[:12]


def download_one(item: dict) -> dict:
    doi = str(item.get("doi") or "")
    url = str(item.get("url") or "")
    relative = f"papers/incremental_{slug(doi)}.pdf"
    target = ROOT / relative
    if target.exists():
        return {"doi": doi, "status": "exists", "url": url, "path": relative}
    result = try_download(url, target, timeout=180)
    return {"doi": doi, "status": result, "url": url, "path": relative if result == "ok" else ""}


def update_summary(doi: str, relative: str) -> bool:
    key = doi.lower()
    for file in (ROOT / "summaries").glob("待补全_*.md"):
        text = file.read_text(encoding="utf-8")
        if f"DOI**: {doi}" not in text and f"DOI: {doi}" not in text:
            continue
        updated = text.replace("- **PDF**: 待探测", f"- **PDF**: [incremental.pdf]({relative})")
        if updated != text:
            file.write_text(updated, encoding="utf-8")
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe", default=str(RUNS / "pdf_probe.json"))
    parser.add_argument("--out", default=str(RUNS / "pdf_downloads.json"))
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    probe = json.loads(Path(args.probe).read_text(encoding="utf-8"))
    jobs = [item for item in probe if item.get("status") in DOWNLOADABLE and item.get("url")]
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(download_one, item) for item in jobs]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"[{result['status']}] {result['doi']}", flush=True)

    results.sort(key=lambda item: item["doi"])
    for result in results:
        if result["status"] in {"ok", "exists"}:
            update_summary(result["doi"], result["path"])
    Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    print(f"完成 {len(results)} 个下载候选: {counts}")


if __name__ == "__main__":
    main()
