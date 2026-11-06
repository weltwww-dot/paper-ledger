# NeuroGraph: an AI graph-driven neuro-symbolic framework for explainable threat reasoning in advanced manufacturing 总结

## 基本信息
- **标题**: NeuroGraph: an AI graph-driven neuro-symbolic framework for explainable threat reasoning in advanced manufacturing
- **作者**: Padmeswari Nandiya、Ahmad Mohsin、Iqbal H. Sarker 等
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25，文章号185
- **发表**: 2026-11-05
- **日期来源**: Springer出版社文章网页的Published和citation_online_date
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01345-8
- **PDF**: [IJIS_2026_NeuroGraph.pdf](papers/IJIS_2026_NeuroGraph.pdf)

## 一句话概括
让大模型借助制造业威胁知识图谱检索和解释证据，支持对工业控制场景的安全推理。

## 问题与动机
先进制造同时涉及IT和OT，资产、漏洞与攻击技术间的联系分散在多种情报中。文本检索能找到相关段落，却难以保证多跳关联和最终回答具有可追溯依据。

## 方法
实现系统GRICS以BRIDG-ICS本体组织知识图谱，由一个模型把问题转为Cypher，另一个模型依据查询结果写答案。系统检查查询的语法、模式和可执行性；查询失败时先用向量检索找图谱锚点，再生成并执行查询。

## 实验与结果
作者在CTI-RCM和CTI-ATE上比较检索与问答配置，并考察多跳推理、扰动下的表现和时延。微调与图检索结合的配置在论文的对比中表现较好（PDF第13、29页）。

## 贡献与局限
将查询验证和证据约束接入工业威胁问答，有助于审查答案来源。效果依赖本体与图谱的覆盖和更新质量，测试也无法排除幻觉或证明系统适用于所有生产现场。

---
DOI: 10.1007/s10207-026-01345-8 | PDF: [IJIS_2026_NeuroGraph.pdf](papers/IJIS_2026_NeuroGraph.pdf)
