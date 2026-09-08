# 论文台账 · Paper Ledger

课题组内部使用的**顶刊论文台账**：把读过的顶刊论文按「基本信息 → 一句话概括 → 问题与动机 → 方法 → 实验与结果 → 贡献与局限」六段式整理成可翻阅、可筛选、可追问的条目。

🔗 **在线访问**: https://weltwww-dot.github.io/paper-ledger/

---

## 功能

- **收录列表**：全部论文按**发表时间倒序**排列（卡片显示具体月日），点击卡片展开六段式详情，附原文与 PDF 链接
- **研究方向筛选**：按「信息安全 / 人工智能」两大方向快速过滤
- **主题标签与热点趋势**：每篇论文带 1–3 个研究主题；「研究热点与趋势」只统计近 90 天发表的论文，
  趋势对比窗口内最新 12 篇 vs 其余（随当天滚动）
- **研究问题清单**：自动汇总各论文的「问题与动机」
- **内容状态徽标**：公开渠道读不到摘要、暂无全文的论文带「待补全」徽标，不伪装成已总结
- **导入总结**：粘贴 `paper-summarize-fetch` 生成的六段式 Markdown 总结，一键解析入库
- **手动录入**：六段式表单直接录入；填写发表日期后按发表时间入位，未填则排在列表末尾
- **数据诚实**：所有数字均来自原文；读不到摘要时按「内容状态：待补全」如实标注并进入补全循环，绝不编造

---

## 技术栈

- 纯静态：HTML + CSS + JS，无后端、无构建步骤
- 字体自托管（Archivo），不依赖外部 CDN
- 数据：`data/papers.js`（内置论文）+ 浏览器 localStorage（个人录入）

## 数据模型（六段式）

```js
{
  title,        // 论文标题（原文语言）
  authors,      // 作者（前 3 位 + et al.）
  journal,      // 期刊 / 会议
  year,         // 年份
  published,    // 论文发表日期（趋势时间轴）
  contentState, // 内容状态：complete / partial / pending（待补全）
  contentNote,  // 待补全原因（可选）
  direction,    // 研究方向：信息安全 / 人工智能
  doi, arxiv, pdf, link,   // 出处链接
  tags,         // 主题标签（同步时由 data/theme-tags.json 合并）
  summary,      // 一句话概括
  question,     // 问题与动机
  method,       // 方法
  experiments,  // 实验与结果
  contribution, // 贡献与局限
}
```

## 更新与维护

更新由 agent 按固定工作流执行（详见 [`更新工作流.md`](更新工作流.md)）：

```
读基准 → OpenAlex + Crossref 双来源增量抓取与逐刊 DOI 对账 → OA 检查 → 多渠道抓摘要
→ 登记六段式总结草稿 → **执行 agent 对照原文写中文六段式** → **按既有主题方案补齐标签** → **PDF 探测、下载、校验与跳过证据登记** → 同步进 data/papers.js
→ 推进基准 → QA → publish 发布并验证
```

日常更新只使用下面的完整入口；它不会省略翻译或 PDF 获取：

```bash
python scripts/run_update.py update    # 抓取 → 导入 → 中文总结审校 → 主题 → PDF 获取 → 同步 → 六道闸门
python scripts/run_update.py update --refresh  # 忽略同日批次成果，强制重跑网络阶段
python scripts/run_update.py advance   # 内容与标签复核后推进基准；任一闸门不通过会拒绝执行
python scripts/run_update.py publish   # 六道闸门 + PDF 文件校验 → 推送 + 当前提交 Pages 构建 + 线上指纹验证
```

排障或内容补全时仍可单独运行 `fetch`、`pdf`、`abstracts`、`instsci` 与 `verify`；其中
`pdf` 现在会完整执行探测、下载、校验和跳过证据登记，不再只是探测。

同一更新基准在同一天重复执行 `update` 时，会复用已经成功且仍可核验的双来源审计、
OA/arXiv、摘要和 PDF 阶段成果，避免人工撰写中文总结期间反复请求相同来源。基准、期刊目录、
抓取/PDF 实现或基准论文标题发生变化，审计失败、日期变化或 JSON 损坏时会自动失效；
需要主动重新检查来源时使用 `update --refresh`。复用不跳过导入、主题同步和六道闸门。

### 中文总结审校

自动直译已停用，避免将逐句机器翻译直接展示在台账中。新增摘要先作为可核验草稿保存，
由当前执行的 Codex agent 对照原文亲自撰写中文六段式；不得上传到翻译服务，也不得调用本地翻译模型。无法由公开材料支撑的段落必须如实说明信息边界，
不能用流程性确认措辞或“当前公开材料未覆盖本节”式空段落代替内容。已有摘要时应按语义拆分
问题、方法、实验和贡献；只有题录时只能作明确标注的题目级推断，不得虚构模型、数据或结果。
`summary_quality_gate.py` 会阻止无信息占位、流程措辞、乱码和未解码 HTML 实体进入推进或发布流程。

每次 `fetch` 还会生成 `skill-runs/collection_audit.json`：逐刊列出 OpenAlex 与 Crossref 的结果数量、排除原因、来源错误以及仅单来源 DOI。默认会重查最近 7 天的发表记录，以覆盖元数据延迟；只要任一来源失败，命令会在写出审计后失败，`advance` 和 `publish` 也会拒绝继续。

发布和推进前有六道不可绕过的质量门：`scripts/summary_gate.py --check` 要求每份总结具备六段式结构、且「一句话概括」是中文；`scripts/summary_quality_gate.py --check` 禁止无信息占位、流程性确认措辞、乱码和未解码实体；`scripts/theme_gate.py --check` 要求每篇都至少有一个主题；`scripts/pdf_gate.py --check` 要求每篇无本地 PDF 的论文都有可追溯的 `blocked`、`not-oa`、`no-file` 或 `non_research_document` 证据；`scripts/workflow_gate.py --check` 进一步核对 DOI、总结、状态、主题、PDF 链接和跳过证据的一致性；真实 Edge 回归同时检查展开卡片不会横向溢出，以及“查看全部”后滚动到列表中部仍有可见的悬浮收起按钮。网络错误不会自动标作跳过。

## 防“读不到摘要”速查

读不到摘要不是“换个请求头”的小修，按下面顺序走，保证缺口可见、可重试、可补全：

0. **开代理了先自检**：`python scripts/run_update.py route-check`
   - 若判定代理会把出版社域名带走 → 按 `proxy-rules/README.md` 加直连规则（Clash/系统代理两版），
     或跑 instsci 时关代理；做不到就切机构 SSO
1. **多渠道自动重试**：`python scripts/run_update.py abstracts`
   - 渠道顺序：OpenAlex → Semantic Scholar → Crossref → arXiv 标题精确匹配 → 出版社落地页
   - 结果分 `ok / absent / blocked / rate-limited / not-found / error`，记入
     `skill-runs/content_attempts.json`；“被墙”不会伪装成“试过”
2. **判定出路**：`absent` = 聚合器与公开页确实无摘要 → 走全文补全；
   `blocked` = 出版社 WAF/Cloudflare → 走可见浏览器或机构通道，不硬刷
3. **机构/IP 通道**：`python scripts/run_update.py instsci` 生成队列后，
   运行输出的 `instsci_batch_local_ip.ps1` 命令（或用 `instsci papers <dois.txt>`）
   - 校园网内优先 **IP 直连**：可见 CloakBrowser 里完成人机验证即直接放行，无需 SSO
   - 本项目包装器会先运行 `route_check.py --require-direct`；检测到代理/PAC 出口即拒绝启动，
     确保出版社看到的是本机网络出口，而不是普通代理 IP
   - 不在校内则走 **机构 SSO**（学校统一认证/CARSI），由你手动完成一次登录
   - **环境修复**：broker 联网下载 CloakBrowser 超时（ConnectTimeout）时，先设置
     ```powershell
     $env:CLOAKBROWSER_CACHE_DIR = 'C:\Users\Administrator\Documents\Codex\tools\instsci-venv\Lib\site-packages\instsci\_browsers\cloakbrowser'
     ```
4. **取回后闭环**：更新对应 `summaries/*.md`（内容改为真实摘要/全文信息），
   把「内容状态」从「待补全」改为「完整」，`node scripts/sync-papers.js` 后发布；
   卡片上的「待补全」徽标随之消失

## 目录结构

```
index.html / styles.css / app.js / tokens.css / fonts.css   # 网站本体
data/papers.js         # 网站数据（浏览器加载，脚本自动生成）
data/theme-tags.json   # 主题标签映射（DOI → 研究主题，人工维护）
summaries/             # 六段式总结（每篇一个 Markdown）
papers/                # 已下载的 PDF
scripts/               # 抓取 / 摘要收口(fetch_content) / PDF / 同步 / 发布脚本
shared/                # 浏览器与 Node 共用的解析 / 存储 / 统计模块
skill-runs/            # 更新基准、可恢复更新批次与抓取记录
proxy-rules/           # 代理分流规则与说明（保住 IP 直连路线）
CONTEXT.md             # 领域词汇表（研究方向 / 主题 / 内容状态 / 热点与趋势）
更新工作流.md          # 「更新」完整流程说明
部署指南.md            # 部署到 GitHub Pages 等平台的说明
```
