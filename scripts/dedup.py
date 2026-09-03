#!/usr/bin/env python3
"""「已收录」判定：DOI 或标题命中即视为重复。

单一实现，供 fetch_incremental.py 与 run_update.py 共用，避免各自打补丁漂移。
同一篇论文可能挂多个 DOI（正式 DOI 与仓库 DOI），因此必须用标题兜底。
"""


def normalize_doi(doi):
    if not doi:
        return ""
    return str(doi).replace("https://doi.org/", "").strip().lower()


def normalize_title(title):
    return (title or "").strip().lower()


def make_known(dois=None, titles=None):
    return {
        "dois": {normalize_doi(d) for d in (dois or []) if d},
        "titles": {normalize_title(t) for t in (titles or []) if t},
    }


def is_known(doi, title, known):
    return normalize_doi(doi) in known["dois"] or normalize_title(title) in known["titles"]
