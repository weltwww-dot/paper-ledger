# Authorization assurance for tool-using LLM agents: a structured review of enforcement semantics and effect-level security evidence 总结

## 基本信息
- **标题**: Authorization assurance for tool-using LLM agents: a structured review of enforcement semantics and effect-level security evidence
- **作者**: Mohamed Abbas Elmasry
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25（2026），文章号186
- **发表**: 2026-11-10
- **日期来源**: Springer 官网 citation_online_date，与正式 PDF 的 DOI 和文章号一致
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01343-w
- **PDF**: [IJIS_2026_AgentAuthorizationAssurance.pdf](papers/IJIS_2026_AgentAuthorizationAssurance.pdf)

## 一句话概括
用结构化综述检查工具型语言模型智能体的授权声明，梳理这些声明需要什么证据。

## 问题与动机
智能体通过 API、工具和凭据改变外部状态。一次任务最终执行正确，仍无法说明每个中间步骤都遵守了权限边界。

## 方法
作者从 75 条来源筛选出 30 条纳入分析，按声明范围、执行约束、观察证据、受保护操作与前提编码，形成 92 条来源与声明的对应记录。

## 实验与结果
三个可评价的最小权限研究都缩小了可用权限，但未测量整个执行轨迹的实际权限。21 条智能体来源中没有可评价的撤权声明，30 条分析来源中没有委托权限约束声明（PDF 第 17 页）。

## 贡献与局限
论文提出 MAAP 最低报告框架，帮助读者核对授权声明与证据。缺口只反映所纳入的样本，框架仍需独立验证后才能用于评估。

---
DOI: 10.1007/s10207-026-01343-w | PDF: [IJIS_2026_AgentAuthorizationAssurance.pdf](papers/IJIS_2026_AgentAuthorizationAssurance.pdf)
