# 代理开启时保住「IP 直连」路线

原则：**IP 路线只认出口 IP**。开了普通代理（Clash / V2Ray 等）后，
只要出版社域名的流量走了代理，出口就不再是校园网，IP 授权即失效。
解决方法是让出版社域名**永远直连**（或走学校 VPN），其余流量随便走代理。

## 必须先直连的域名

```text
www.sciencedirect.com
api.elsevier.com
auth.elsevier.com
pdf.sciencedirectassets.com
*.elsevier.com
ieeexplore.ieee.org
doi.org
```

抓取/校验还会访问 `api.openalex.org`、`api.semanticscholar.org`、
`api.crossref.org`、`export.arxiv.org`——同样建议直连（或放 NO_PROXY），
避免代理出口与出版社不一致造成的验证码循环。

## Clash / Mihomo（推荐，规则分流）

在 config 的 rules 里，把出版社域名放在代理规则**之前**：

```yaml
rules:
  - DOMAIN-SUFFIX,sciencedirect.com,DIRECT
  - DOMAIN-SUFFIX,elsevier.com,DIRECT
  - DOMAIN-SUFFIX,ieeexplore.ieee.org,DIRECT
  - DOMAIN-SUFFIX,doi.org,DIRECT
  - DOMAIN-SUFFIX,openalex.org,DIRECT
  - DOMAIN-SUFFIX,semanticscholar.org,DIRECT
  - DOMAIN-SUFFIX,crossref.org,DIRECT
  - DOMAIN-SUFFIX,arxiv.org,DIRECT
  # ……其余规则放后面，按你平时的代理规则继续
```

改完在 Clash 里刷新规则，然后跑出口自检确认：

```powershell
python scripts/route_check.py
```

## V2rayN / 系统代理（PAC 或绕过列表）

Windows 系统代理设置 → 代理服务器 → 高级 → 例外/绕过列表加入：

```text
*.sciencedirect.com;*.elsevier.com;ieeexplore.ieee.org;*.ieee.org;doi.org;*.openalex.org;*.semanticscholar.org;*.crossref.org;*.arxiv.org
```

命令行/脚本环境还要确认 `NO_PROXY` 环境变量包含这些域名，
或直接在跑 instsci 的终端里设置：

```powershell
$env:NO_PROXY = "sciencedirect.com,elsevier.com,ieeexplore.ieee.org,doi.org,openalex.org,semanticscholar.org,crossref.org,arxiv.org"
```

## 跑批前必做

```powershell
python scripts/run_update.py route-check
```

- 判定「无代理/已直连」→ 直接进 instsci（仍会先弹可见浏览器做人机验证）。
- 判定「代理会带走出版社流量」→ 按上文直连后重跑；做不到就改走机构 SSO：

```powershell
python scripts/run_update.py instsci
```

- 最终判定永远以单 DOI 可见浏览器诊断为准（`--mode diagnose --watch-browser focus`）。
