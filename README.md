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
- **手动录入**：六段式表单直接录入，论文即时置顶
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
读基准 → 增量抓取（上次更新以来的全部期刊论文，DOI + 标题双重去重）→ OA 检查 → 多渠道抓摘要
→ 六段式总结（带发表时间与内容状态）→ 打主题标签 → PDF 智能探测并下载 → 同步进 data/papers.js
→ 推进基准 → QA → publish 发布并验证
```

一键命令：

```bash
python scripts/run_update.py fetch     # 抓取 + OA + 摘要
python scripts/run_update.py pdf       # 探测新增论文的 PDF 可下载性
python scripts/run_update.py abstracts # 对「待补全」论文重试多渠道摘要（typed 结果 + attempts 缓存）
python scripts/run_update.py instsci   # 生成机构全文补全队列（HITL，需一次机构登录）
node scripts/sync-papers.js            # 总结同步进网站数据
python scripts/run_update.py advance   # 推进更新基准
python scripts/run_update.py publish   # 推送 + 等待 Pages 构建 + 验证线上一致
```

## 防“读不到摘要”速查

读不到摘要不是“换个请求头”的小修，按下面顺序走，保证缺口可见、可重试、可补全：

1. **多渠道自动重试**：`python scripts/run_update.py abstracts`
   - 渠道顺序：OpenAlex → Semantic Scholar → Crossref → arXiv 标题精确匹配 → 出版社落地页
   - 结果分 `ok / absent / blocked / rate-limited / not-found / error`，记入
     `skill-runs/content_attempts.json`；“被墙”不会伪装成“试过”
2. **判定出路**：`absent` = 聚合器与公开页确实无摘要 → 走全文补全；
   `blocked` = 出版社 WAF/Cloudflare → 走可见浏览器或机构通道，不硬刷
3. **机构/IP 通道**：`python scripts/run_update.py instsci` 生成队列后，
   运行输出的 `instsci_batch.ps1` 命令（或用 `instsci papers <dois.txt>`）
   - 校园网内优先 **IP 直连**：可见 CloakBrowser 里完成人机验证即直接放行，无需 SSO
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
skill-runs/            # 更新基准与抓取记录
CONTEXT.md             # 领域词汇表（研究方向 / 主题 / 内容状态 / 热点与趋势）
更新工作流.md          # 「更新」完整流程说明
部署指南.md            # 部署到 GitHub Pages 等平台的说明
```
