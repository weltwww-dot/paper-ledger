# -*- coding: utf-8 -*-
"""磁盘实体核验：不读日志、不读 manifest，直接 stat + 读魔数 + PyMuPDF 打开取页数。

用法:
  python verify_on_disk.py <dir1> [<dir2> ...]      # 核验目录下的 PDF
  python verify_on_disk.py --doi-map <json>          # 核验 DOI->路径 映射
"""
import hashlib
import json
import os
import sys

import fitz

ROOT = r"D:\codex\博客网站"


def probe(path):
    """对单个文件做实体核验，返回证据字典。"""
    r = {"path": path}
    if not os.path.isfile(path):
        r.update(exists=False, verdict="文件不存在")
        return r
    r["exists"] = True
    st = os.stat(path)
    r["size_bytes"] = st.st_size
    if st.st_size == 0:
        r.update(verdict="空文件")
        return r
    with open(path, "rb") as f:
        head = f.read(8)
        f.seek(max(0, st.st_size - 2048))
        tail = f.read()
    r["magic"] = head[:8].decode("latin-1")
    r["has_pdf_magic"] = head.startswith(b"%PDF-")
    r["has_eof"] = b"%%EOF" in tail
    r["pdf_version"] = head[5:8].decode("latin-1") if r["has_pdf_magic"] else None
    if not r["has_pdf_magic"]:
        r.update(verdict="不是 PDF（魔数错误）")
        return r
    # 真正打开解析
    try:
        doc = fitz.open(path)
        r["pages"] = doc.page_count
        r["needs_pass"] = doc.needs_pass
        txt = doc[0].get_text("text") if doc.page_count else ""
        r["first_page_chars"] = len(txt.strip())
        r["first_line"] = " ".join(txt.split()[:18])
        doc.close()
    except Exception as e:  # noqa: BLE001
        r.update(verdict="PDF 打开失败: %s" % e)
        return r
    # md5
    h = hashlib.md5()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    r["md5"] = h.hexdigest()
    r["verdict"] = "OK" if (r["pages"] > 0 and r["has_eof"]) else "可疑（页数0或缺EOF）"
    return r


def scan_dirs(dirs):
    out = []
    for d in dirs:
        if not os.path.isdir(d):
            out.append({"path": d, "exists": False, "verdict": "目录不存在"})
            continue
        for name in sorted(os.listdir(d)):
            if name.lower().endswith(".pdf"):
                out.append(probe(os.path.join(d, name)))
    return out


def main(argv):
    rows = scan_dirs(argv)
    ok = sum(1 for r in rows if r.get("verdict") == "OK")
    print("扫描 PDF 文件 %d 个；实体核验通过 %d 个" % (len(rows), ok))
    for r in rows:
        if r.get("verdict") == "OK":
            print("  OK  %-11s %-5sp %-9s %s" % (
                os.path.basename(r["path"]), r["pages"], r["pdf_version"],
                r.get("first_line", "")[:58]))
        else:
            print("  !!  %-11s %s" % (os.path.basename(r["path"]), r.get("verdict")))
    return rows


if __name__ == "__main__":
    main(sys.argv[1:])
