#!/usr/bin/env python3
"""把本轮 PDF 探测与下载结果写入闸门记录。

只有已确认的 closed、反爬、无公开链接或无效候选文件会形成跳过证据；网络
错误等暂态失败不记为完成，交给 PDF 闸门阻止后续推进。
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "skill-runs"
ATTEMPTS = RUNS / "pdf_attempts.json"


def main() -> None:
    attempts = {}
    if ATTEMPTS.exists():
        attempts = json.loads(ATTEMPTS.read_text(encoding="utf-8"))
    probe = json.loads((RUNS / "pdf_probe.json").read_text(encoding="utf-8"))
    downloads = json.loads((RUNS / "pdf_downloads.json").read_text(encoding="utf-8"))
    download_by_doi = {item["doi"].lower(): item for item in downloads}

    for item in probe:
        doi = str(item.get("doi") or "").lower()
        status = item.get("status") or ""
        if not doi or status in {"direct", "arxiv", "article-pdf"}:
            continue
        if status == "not-oa":
            attempts[doi] = {"reason": "not-oa", "note": "OpenAlex 标记为 closed，未发现公开 PDF。"}
        elif status == "blocked":
            attempts[doi] = {"reason": "blocked", "note": "PDF 探测时被出版社页面或反爬拦截。"}
        elif status in {"no-link", "not-found"}:
            attempts[doi] = {"reason": "no-file", "note": "已检查 OA、DOI 落地页与 arXiv，未找到公开 PDF。"}

    for doi, item in download_by_doi.items():
        status = item.get("status") or ""
        if status.startswith("error:HTTPError") or status == "blocked":
            attempts[doi] = {"reason": "blocked", "note": "探测到候选 PDF，但下载请求被 HTTP 错误拒绝。"}
        elif status == "bad":
            attempts[doi] = {"reason": "no-file", "note": "候选文件未通过 PDF 文件头/结尾校验，已删除。"}

    ATTEMPTS.write_text(json.dumps(attempts, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"已写入 {len(attempts)} 条 PDF 尝试记录")


if __name__ == "__main__":
    main()
