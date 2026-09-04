#!/usr/bin/env python3
"""摘要获取收口（typed outcome + 渠道 attempts 缓存）。

把「摘要/内容获取」收成一个入口：多个渠道依次尝试，不再把失败折叠成 null。
每个渠道的尝试结果（ok / absent / blocked / rate-limited / not-found / error）
记录到 attempts 缓存，供下一轮更新判断「是墙、是没有、还是限流」。

用法:
  python scripts/fetch_content.py -i skill-runs/records_pending.json \
      -o skill-runs/content_retry.json --attempts skill-runs/content_attempts.json

输入 records: [{"doi": "...", "title": "...", "arxiv": "..."}]
输出 content: [{"doi","title","text","source","kind","channels":[...]}]
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from functools import partial

UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
}


def get_bytes(url, timeout=20, tries=2):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(2_000_000)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 404):
                return e.code, b""
            last = e
            time.sleep(1.2 * (i + 1))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.2 * (i + 1))
    if last:
        return None, str(last).encode("utf-8", "replace")
    return None, b""


def get_json(url, timeout=25):
    status, body = get_bytes(url, timeout=timeout)
    if status != 200 or not body:
        return None, (status if isinstance(status, int) else "error")
    try:
        return json.loads(body.decode("utf-8", "replace")), None
    except Exception:
        return None, "bad-json"


def rebuild_openalex(idx):
    if not idx:
        return ""
    pos = {}
    for word, poss in idx.items():
        for p in poss:
            pos[p] = word
    return " ".join(pos[i] for i in sorted(pos)).strip()


def channel_openalex(rec):
    doi = str(rec.get("doi") or "").strip()
    enc = urllib.parse.quote(doi, safe="")
    url = "https://api.openalex.org/works/doi:" + enc + "?select=doi,abstract_inverted_index"
    d, err = get_json(url)
    if d is None:
        return {"channel": "openalex", "kind": "error", "detail": str(err)}
    text = rebuild_openalex(d.get("abstract_inverted_index"))
    if not text:
        return {"channel": "openalex", "kind": "absent", "detail": "no abstract_inverted_index"}
    return {"channel": "openalex", "kind": "ok", "text": text}


def channel_s2(rec):
    doi = str(rec.get("doi") or "").strip()
    enc = urllib.parse.quote(doi, safe="")
    url = "https://api.semanticscholar.org/graph/v1/paper/DOI:" + enc + "?fields=abstract"
    d, err = get_json(url)
    if d is None:
        return {"channel": "semanticscholar", "kind": "error", "detail": str(err)}
    text = (d.get("abstract") or "").strip()
    if not text:
        return {"channel": "semanticscholar", "kind": "absent", "detail": "abstract is null"}
    return {"channel": "semanticscholar", "kind": "ok", "text": text}


def channel_crossref(rec):
    doi = str(rec.get("doi") or "").strip()
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    d, err = get_json(url)
    if d is None:
        return {"channel": "crossref", "kind": "error", "detail": str(err)}
    raw = (d.get("message") or {}).get("abstract") or ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return {"channel": "crossref", "kind": "absent", "detail": "no abstract field"}
    return {"channel": "crossref", "kind": "ok", "text": text}


def channel_arxiv(rec):
    aid = (rec.get("arxiv") or "").strip()
    if not aid:
        title = (rec.get("title") or "").strip()
        if not title:
            return {"channel": "arxiv", "kind": "absent", "detail": "no id or title"}
        url = "https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(
            'ti:"' + title + '"'
        ) + "&max_results=3"
        status, body = get_bytes(url, timeout=25)
        if status != 200:
            return {"channel": "arxiv", "kind": "error" if status is None else "rate-limited", "detail": str(status)}
        xml = body.decode("utf-8", "replace")
        entries = re.findall(r"<entry>[\s\S]*?</entry>", xml)
        for e in entries:
            tm = re.search(r"<title>(.*?)</title>", e)
            if tm and title.lower() in tm.group(1).lower():
                mid = re.search(r"<id>(?:http://arxiv.org/abs/)?([^<]+)</id>", e)
                aid = mid.group(1).rsplit("/", 1)[-1] if mid else ""
                break
        if not aid:
            return {"channel": "arxiv", "kind": "absent", "detail": "no exact title match"}
    url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(aid)
    status, body = get_bytes(url, timeout=25)
    if status != 200:
        return {"channel": "arxiv", "kind": "error", "detail": "http " + str(status)}
    sm = re.search(r"<summary>(.*?)</summary>", body.decode("utf-8", "replace"), re.S)
    text = re.sub(r"\s+", " ", sm.group(1)).strip() if sm else ""
    if not text:
        return {"channel": "arxiv", "kind": "absent", "detail": "no summary"}
    return {"channel": "arxiv", "kind": "ok", "text": text}


def channel_publisher(rec):
    """出版社落地页（含 DOI 解析）。被 WAF 拦时如实标 blocked，不伪装成试过。"""
    doi = str(rec.get("doi") or "").strip()
    url = "https://doi.org/" + urllib.parse.quote(doi, safe="")
    status, body = get_bytes(url, timeout=20, tries=1)
    if status in (403, 202):
        return {"channel": "publisher-page", "kind": "blocked", "detail": "http " + str(status)}
    if status == 429:
        return {"channel": "publisher-page", "kind": "rate-limited", "detail": "http 429"}
    if status != 200:
        return {"channel": "publisher-page", "kind": "error", "detail": "http " + str(status)}
    html = body.decode("utf-8", "replace")
    for pat in (
        r'<meta[^>]+name="citation_abstract"[^>]+content="([^"]*)"',
        r'<meta[^>]+property="og:description"[^>]+content="([^"]*)"',
        r'<meta[^>]+name="description"[^>]+content="([^"]*)"',
    ):
        mm = re.search(pat, html, re.I)
        if mm:
            text = re.sub(r"\s+", " ", mm.group(1)).strip()
            if text:
                return {"channel": "publisher-page", "kind": "ok", "text": text}
    return {"channel": "publisher-page", "kind": "absent", "detail": "landing page has no abstract meta"}


CHANNELS = [channel_openalex, channel_s2, channel_crossref, channel_arxiv, channel_publisher]


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_json(path):
    try:
        with open(path, encoding="utf-8-sig") as f:
            return json.load(f)
    except Exception:
        return []


def process_record(rec, pause=0.3):
    """单篇多渠道获取；返回 (out_item, attempts_entry, doi)。"""
    doi = str(rec.get("doi") or "").strip()
    if not doi:
        return (
            {"doi": "", "title": rec.get("title"), "text": "", "source": None,
             "kind": "not-found", "channels": []},
            None,
            "",
        )
    channels = []
    text, source, kind = "", None, "absent"
    for fn in CHANNELS:
        r = fn(rec)
        channels.append(r)
        if r.get("kind") == "ok":
            text, source, kind = r.get("text", ""), r["channel"], "ok"
            break
        if r["kind"] in ("blocked", "rate-limited") and kind == "absent":
            kind = r["kind"]
        time.sleep(pause)
    entry = {
        "at": now_iso(),
        "final": kind,
        "channels": [{k: v for k, v in c.items() if k != "text"} for c in channels],
    }
    item = {"doi": doi, "title": rec.get("title"), "text": text, "source": source,
            "kind": kind, "channels": channels}
    return item, entry, doi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True)
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--attempts", default=None)
    ap.add_argument("--pause", type=float, default=0.6)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    records = load_json(args.input)
    attempts = {}
    if args.attempts:
        try:
            with open(args.attempts, encoding="utf-8") as f:
                attempts = json.load(f)
        except Exception:
            attempts = {}

    out = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        results = list(ex.map(partial(process_record, pause=args.pause), records))
    for item, entry, doi in results:
        out.append(item)
        if doi and entry is not None:
            attempts[doi] = entry
        print(f"{item['kind']:>13} | {item.get('source') or '-':<16} | {doi}")

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    if args.attempts:
        with open(args.attempts, "w", encoding="utf-8") as f:
            json.dump(attempts, f, ensure_ascii=False, indent=1)
    ok = sum(1 for x in out if x["kind"] == "ok")
    print(f"done: {ok}/{len(out)} content ok")


if __name__ == "__main__":
    main()
