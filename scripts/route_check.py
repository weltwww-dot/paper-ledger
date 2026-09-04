#!/usr/bin/env python3
"""instsci IP 路线 · 代理出口自检。

目标：判断「开了代理之后，还能不能走出版社 IP 授权路线」。
判断依据不是代理开没开，而是**出版社域名的流量会不会被代理带走**：
- 系统/环境代理开着，但出版社域名被 NO_PROXY / 规则分流为直连 → IP 路线仍可用；
- 出版社域名走了普通代理 → 出口 IP 不再是校园网，IP 授权失效，需要规则直连或改 SSO。

用法:
  python scripts/route_check.py

只读检测，不改任何代理配置。最终访问判定仍以 instsci 单 DOI 可见浏览器诊断为准。
"""

import json
import os
import re
import sys
import urllib.request
import winreg

PUBLISHER_DOMAINS = [
    "www.sciencedirect.com",
    "api.elsevier.com",
    "auth.elsevier.com",
    "pdf.sciencedirectassets.com",
    "*.elsevier.com",
    "ieeexplore.ieee.org",
    "doi.org",
    "api.openalex.org",
    "api.semanticscholar.org",
    "api.crossref.org",
    "export.arxiv.org",
]

IP_ECHO_URLS = [
    "https://api-ipv4.ip.sb/ip",
    "https://myip.ipip.net",
    "https://api.ipify.org",
]

NO_PROXY_SUFFIXES = [
    "sciencedirect.com",
    "elsevier.com",
    "ieee.org",
    "doi.org",
    "openalex.org",
    "semanticscholar.org",
    "crossref.org",
    "arxiv.org",
]


def read_env_proxy():
    """返回 (proxy_url, no_proxy_domains)。只读环境变量。"""
    for name in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy"):
        v = os.environ.get(name)
        if v and v.strip():
            return v.strip(), os.environ.get("NO_PROXY", "") or os.environ.get("no_proxy", "") or ""
    return "", ""


def read_system_proxy():
    """读取 Windows 系统代理（WinINET）：是否启用、地址、PAC。"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
        )
        enable, _ = winreg.QueryValueEx(key, "ProxyEnable")
        server, _ = winreg.QueryValueEx(key, "ProxyServer")
        pac = ""
        try:
            pac, _ = winreg.QueryValueEx(key, "AutoConfigURL")
        except FileNotFoundError:
            pass
        winreg.CloseKey(key)
        return bool(enable), server or "", pac or ""
    except OSError:
        return False, "", ""


def egress_ip(proxy_url=None):
    """通过 urllib 取出口 IP（多端点兜底）；proxy_url=None 表示不走任何代理。"""
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({} if proxy_url is None else {"http": proxy_url, "https": proxy_url})
    )
    for url in IP_ECHO_URLS:
        try:
            with opener.open(url, timeout=10) as r:
                text = (r.read().decode("utf-8", "replace") or "").strip()
            if not text:
                continue
            m = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", text)
            if m:
                return m.group(0)
            return text[:80]
        except Exception:
            continue
    return "(无法获取出口 IP)"


def no_proxy_missing(no_proxy):
    """NO_PROXY 里缺少哪些需要直连的域后缀。"""
    tokens = {
        t.strip().lstrip("*.").lower()
        for t in re.split(r"[;,\s]+", no_proxy or "")
        if t.strip()
    }
    return [
        s
        for s in NO_PROXY_SUFFIXES
        if not any(t == s or t.endswith("." + s) for t in tokens)
    ]


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print("instsci IP 路线 · 代理出口自检\n")

    env_proxy, no_proxy = read_env_proxy()
    sys_enable, sys_server, sys_pac = read_system_proxy()

    print(f"[环境变量代理] {'有: ' + env_proxy if env_proxy else '无'}")
    if no_proxy:
        print(f"[NO_PROXY] {no_proxy}")
    print(f"[系统代理] {'启用: ' + (sys_server or sys_pac) if sys_enable or sys_pac else '未启用'}")
    print()

    direct_ip = egress_ip()
    print(f"直连出口 IP（不走代理）: {direct_ip}")
    proxied = ""
    if env_proxy:
        proxied = egress_ip(env_proxy)
        print(f"经代理出口 IP          : {proxied}")

    missing = no_proxy_missing(no_proxy)
    publisher_via_proxy = bool(env_proxy) and bool(missing)

    print("\n" + "=" * 64)
    if not env_proxy and not sys_enable and not sys_pac:
        print("判定: 无代理直连。出版社看到的是本机出口 IP——"
              "若在校园网内即可走 IP 授权（仍需可见浏览器过一遍 WAF 人机验证）。")
    elif env_proxy and publisher_via_proxy:
        print("判定: ⚠️ 环境代理会把出版社域名带走，IP 路线会失效（出口不再是校园 IP）。")
        print("解决办法(任选):")
        print("  1) 关掉代理再跑 instsci；")
        print("  2) 分流/规则直连以下域名（见 proxy-rules/README.md）：")
        for s in missing:
            print(f"     - {s}")
        print("  3) 无法直连时改用机构 SSO（CARSI）路线。")
    elif sys_enable or sys_pac:
        print("判定: ⚠️ Windows 系统代理已启用，浏览器流量可能被带走。")
        print("请确认系统代理的绕过列表包含出版社域名，或跑 instsci 时关闭系统代理；")
        print("规则清单见 proxy-rules/README.md。")
    else:
        print("判定: 代理环境变量存在但 NO_PROXY 已覆盖出版社域名，IP 路线预期可用。")
    print("=" * 64)
    print("\n最终访问判定以单 DOI 可见浏览器为准：")
    print("  instsci papers <one_doi.txt> --publisher auto --mode diagnose --watch-browser focus")


if __name__ == "__main__":
    main()
