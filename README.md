# 论文台账 · Paper Ledger

课题组内部使用的**顶刊论文台账**：把读过的顶刊论文按「基本信息 → 一句话概括 → 问题与动机 → 方法 → 实验与结果 → 贡献与局限」六段式整理成可翻阅、可筛选、可追问的条目。

🔗 **在线访问**: https://weltwww-dot.github.io/paper-ledger/

---

## 功能

- **收录列表**：全部论文按收录时间倒序排列，点击卡片展开六段式详情，附原文与 PDF 链接
- **研究方向筛选**：按「信息安全 / 人工智能」两大方向快速过滤
- **研究问题清单**：自动汇总各论文的「问题与动机」
- **导入总结**：粘贴 `paper-summarize-fetch` 生成的六段式 Markdown 总结，一键解析入库
- **手动录入**：六段式表单直接录入，论文即时置顶
- **数据诚实**：所有数字均来自原文；原文未提供处标注「原文未提供」，绝不编造

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
  direction,    // 研究方向：信息安全 / 人工智能
  doi, arxiv, pdf, link,   // 出处链接
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
读基准 → 增量抓取（上次更新以来的全部期刊论文）→ 去重 → OA 检查 → 抓摘要
→ 六段式总结 → 下载 PDF → 同步进 data/papers.js → 推进基准 → QA → git push 发布
```

一键命令：

```bash
python scripts/run_update.py fetch     # 抓取 + OA + 摘要
node scripts/sync-papers.js            # 总结同步进网站数据
python scripts/run_update.py advance   # 推进更新基准
```

## 目录结构

```
index.html / styles.css / app.js / tokens.css / fonts.css   # 网站本体
data/papers.js         # 网站数据（浏览器加载，脚本自动生成）
summaries/             # 六段式总结（每篇一个 Markdown）
papers/                # 已下载的 PDF
scripts/               # 抓取 / 同步 / 一键更新脚本
skill-runs/            # 更新基准与抓取记录
更新工作流.md          # 「更新」完整流程说明
部署指南.md            # 部署到 GitHub Pages 等平台的说明
```
