# 599 篇论文 PDF 全量复核规格

## 目标

对当前 599 条台账逐条复核 PDF 状态，找出“台账没有 PDF、PDF 字段存在但本地文件缺失/损坏、PDF 与 DOI/标题不匹配、已有 PDF 但未记录证据”等漏网项；对新确认获取的 PDF 按现有项目规则完成归档、中文六段式总结、主题同步和门禁验收。

## 当前基线

- 台账来源：`data/papers.js`，当前 599 条。
- 内容状态：`complete 238 / partial 300 / pending 61`，无空状态。
- PDF 字段：285 条；`papers/` 顶层有效 PDF：290 个。
- PDF 尝试证据：`skill-runs/pdf_attempts.json` 当前 501 条；既有记录不能替代新的身份复核。
- 远端功能代码：`origin/main` 与本地 HEAD 均为 `86d2473`；当前未提交变更仅为 `index.html` 的缓存版本 `tl2se4`。

## 必须满足的行为

1. 先审计，后下载；不因“重新跑一遍”覆盖或删除现有有效 PDF。
2. 每条成功 PDF 必须同时具备 `%PDF` 文件头、`%%EOF` 尾标记、可读页数和 DOI/标题身份依据；仅 HTTP 200 或文件名相似不算成功。
3. 所有下载先进入 `skill-runs/pdf_full_audit_YYYY-MM-DD/` 临时目录；只有身份校验通过后才复制到 `papers/` 顶层并更新总结链接。
4. 机构路线使用本机直连/校园机构通道；`route_check.py --require-direct` 失败时不得启动 InstSci，不得把通用代理出口当机构 IP。
5. InstSci 按出版社串行、单批不超过 25 篇、并发 1；遇到 WAF、验证码、SSO 或人工验证只记录状态并停止当前批次，不能绕过。
6. 新获得全文后，由当前主 agent 亲自阅读并撰写中文六段式；不得调用本地翻译模型、在线翻译服务或把最终翻译交给子代理。
7. handoff 只更新本地，不上传；GitHub 提交/Pages 发布必须等待用户明确授权。

## 完成判据

- 599 条均有 `audit_status`：`verified_local`、`verified_oa`、`verified_institution`、`missing_with_evidence`、`non_research_document` 或 `needs_manual_review` 之一。
- 所有新获取 PDF 已完成身份校验、规范命名、总结链接和 `data/papers.js` 同步。
- 新全文对应的 `pending`/`partial` 状态已按证据升级或保留明确原因；不得增加“有 PDF 但 partial”的历史技术债数量。
- `summary_gate`、`summary_quality_gate`、`theme_gate`、`pdf_gate`、`workflow_gate`、三项 Edge 回归、全量 Python 测试和 `git diff --check` 全部通过。
- 生成审计清单、出版社队列、失败/跳过证据和本地 handoff 更新；未获用户授权时不 commit/push。
