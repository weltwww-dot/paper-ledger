#!/usr/bin/env python3
"""智能 PDF 获取器 —— 针对 paper-summarize-fetch 下载方案的四点改进。

已知问题 → 改进:
  1. oa_check 的 best_pdf_url 常是 DOI 跳转页而非文件直链
     → 先解析重定向，识别最终是 PDF 文件还是文章页 HTML
  2. oa_check 的 arXiv 字段常缺失（实际有 arXiv 全文）
     → 下载失败时按标题回退查询 arXiv API
  3. 文章页不挖 PDF 直链
     → 从文章页 HTML 提取 pdfft / article-pdf / doi/pdf / content/pdf 链接再试
  4. 拿到 HTML 垃圾还傻重试多次
     → 检测到 HTML 立即判 blocked，不重试

用法:
  单条下载: python scripts/smart_pdf.py --doi 10.1007/x --out papers/x.pdf
            [--arxiv 2501.07021] [--title "..." ] [--url https://...]
  批量探测: python scripts/smart_pdf.py --probe skill-runs/oa_inc.json
            （只探测开放获取论文，输出可直接下载 / 需反爬 / 无链接）
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    )
}


def log(msg):
    print(msg, flush=True)


def http_get(url, timeout=30, follow=True):
    """GET 并跟随重定向；返回 (final_url, content_type, body_bytes 前 64KB)。"""
    req = urllib.request.Request(url, headers=UA)
    opener = urllib.request.build_opener()
    if not follow:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *a, **k):
                return None

        opener = urllib.request.build_opener(NoRedirect)
    with opener.open(req, timeout=timeout) as r:
        final = r.geturl()
        ctype = r.headers.get("Content-Type", "")
        body = r.read(65536)
        return final, ctype, body


def looks_pdf(url, ctype):
    if "pdf" in ctype.lower():
        return True
    path = urllib.parse.urlparse(url).path.lower()
    return path.endswith(".pdf") or "/pdf/" in path or "pdfft" in path


def looks_html(url, ctype, body):
    if "html" in ctype.lower() or "text/plain" in ctype.lower():
        return True
    head = body[:512].lower()
    return b"<!doctype" in head or b"<html" in head


def extract_pdf_links(html_text, base_url):
    """从文章页 HTML 中挖 PDF 直链候选（按已知出版社模式）。"""
    cands = []
    hrefs = re.findall(r'href=("|\')([^"\']+)\1', html_text, re.I)
    keywords = (
        "article-pdf",
        "pdfft",
        "/doi/pdf/",
        "content/pdf",
        "/article/pdf/",
        ".pdf",
    )
    for h in hrefs:
        href = h[1] if isinstance(h, tuple) else h
        low = href.lower()
        if any(k in low for k in keywords):
            cands.append(urllib.parse.urljoin(base_url, href))
    # 兜底：正文/脚本/JSON 里裸露的下载端点
    for m in re.findall(
        r"https?://[^\s\"'<>]*(?:pdfft|article-pdf|/doi/pdf/|content/pdf)[^\s\"'<>]*",
        html_text,
        re.I,
    ):
        cands.append(m)
    seen = []
    for c in cands:
        if c not in seen:
            seen.append(c)
    return seen


def arxiv_search(title):
    """arXiv API 按标题查询，返回第一个 arXiv id（无则 None）。"""
    q = urllib.parse.quote(f'ti:"{title}"')
    url = f"https://export.arxiv.org/api/query?search_query={q}&max_results=3"
    try:
        _, _, body = http_get(url, timeout=30)
        xml = body.decode("utf-8", "replace")
        m = re.search(r"<id>https?://arxiv\.org/abs/([\d.]+(?:v\d+)?)</id>", xml)
        return m.group(1) if m else None
    except Exception:
        return None


def linkinghub_pdfft(url):
    """linkinghub.elsevier.com/retrieve/pii/<PII> → ScienceDirect pdfft 直链。"""
    m = re.search(r"/retrieve/pii/([A-Z0-9]+)", url or "", re.I)
    if m:
        return (
            "https://www.sciencedirect.com/science/article/pii/"
            f"{m.group(1)}/pdfft?isDTMRedir=true&download=true"
        )
    return None


def verify_pdf(path):
    try:
        with open(path, "rb") as f:
            head = f.read(5)
            f.seek(max(0, Path(path).stat().st_size - 16))
            tail = f.read(16)
        return head.startswith(b"%PDF") and b"%EOF" in tail
    except Exception:
        return False


def try_download(url, outfile, timeout=180):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            outfile.parent.mkdir(parents=True, exist_ok=True)
            with open(outfile, "wb") as f:
                while True:
                    chunk = r.read(1 << 16)
                    if not chunk:
                        break
                    f.write(chunk)
        if verify_pdf(outfile):
            return "ok"
        outfile.unlink(missing_ok=True)
        return "blocked" if "html" in ctype.lower() else "bad"
    except Exception as e:
        return f"error:{type(e).__name__}"


def probe(rec, outdir=None):
    """对一条记录做探测，返回状态与建议 URL。"""
    doi = rec.get("doi") or ""
    title = rec.get("title") or ""
    arxiv = rec.get("arxiv_id") or ""
    best = rec.get("best_pdf_url") or ""
    if rec.get("is_oa") is False:
        return {"doi": doi, "status": "not-oa", "url": ""}

    # 1) arXiv 直链（最可靠）
    if arxiv:
        aid = arxiv.split("v")[0] if re.match(r"^\d{4}\.\d{4,5}v\d+$", arxiv) else arxiv
        return {"doi": doi, "status": "arxiv", "url": f"https://arxiv.org/pdf/{aid}"}

    # 2) 已有直链（.pdf 结尾）
    if best and looks_pdf(best, ""):
        return {"doi": doi, "status": "direct", "url": best}

    # 3) DOI / best 解析重定向，判断最终类型
    last_state = "no-link"
    for url in ([best] if best else []) + ([f"https://doi.org/{doi}"] if doi and best != f"https://doi.org/{doi}" else []):
        if not url:
            continue
        try:
            final, ctype, body = http_get(url, timeout=30)
        except urllib.error.HTTPError as e:
            last_state = "blocked" if e.code != 404 else "not-found"
            continue
        except Exception as e:
            last_state = f"error:{type(e).__name__}"
            continue
        if looks_pdf(final, ctype):
            return {"doi": doi, "status": "direct", "url": final}
        pdfft = linkinghub_pdfft(final)
        if pdfft:
            return {"doi": doi, "status": "article-pdf", "url": pdfft, "candidates": [pdfft]}
        if looks_html(final, ctype, body):
            links = extract_pdf_links(body.decode("utf-8", "replace"), final)
            if links:
                return {"doi": doi, "status": "article-pdf", "url": links[0], "candidates": links[:5]}
            last_state = "blocked"

    # 4) arXiv 按标题兜底（覆盖 arXiv 字段缺失 + 出版社反爬两类情况）
    if title:
        aid = arxiv_search(title)
        if aid:
            return {"doi": doi, "status": "arxiv", "url": f"https://arxiv.org/pdf/{aid}"}

    # 5) 诚实返回（blocked / error / no-link）
    return {"doi": doi, "status": last_state, "url": ""}


def cmd_probe(args):
    recs = json.loads(Path(args.probe).read_text(encoding="utf-8"))
    results = []
    for r in recs:
        res = probe(r)
        results.append(res)
        log(f"[{res['status']:<10}] {res['doi']}  ·  {(r.get('title') or '')[:60]}")
        if res["url"]:
            log(f"           → {res['url']}")
    out = Path(args.probe).with_name("pdf_probe.json")
    out.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"\n探测结果: {len(results)} 条 → {out}")


def cmd_fetch(args):
    if args.probe:
        cmd_probe(args)
        return
    rec = {
        "doi": args.doi or "",
        "title": args.title or "",
        "arxiv_id": args.arxiv or "",
        "best_pdf_url": args.url or "",
        "is_oa": True,
    }
    res = probe(rec)
    log(f"探测: {res['status']}  {res.get('url', '')}")
    if res["status"] in ("direct", "arxiv", "article-pdf") and res["url"]:
        status = try_download(res["url"], Path(args.out), timeout=args.timeout)
        log(f"下载: {status} → {args.out}")
    else:
        log("无可直接下载的 PDF 链接，跳过。")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="智能 PDF 获取器")
    ap.add_argument("--probe", help="批量探测 oa JSON（如 skill-runs/oa_inc.json）")
    ap.add_argument("--doi", help="DOI")
    ap.add_argument("--arxiv", help="arXiv id")
    ap.add_argument("--title", help="标题（arXiv 兜底搜索用）")
    ap.add_argument("--url", help="候选 PDF URL（best_pdf_url）")
    ap.add_argument("--out", help="输出 PDF 文件路径")
    ap.add_argument("--timeout", type=int, default=180)
    args = ap.parse_args()
    if not args.probe and not args.out:
        ap.error("需要 --probe 或 --out")
    if args.probe:
        cmd_probe(args)
    else:
        cmd_fetch(args)


if __name__ == "__main__":
    main()
