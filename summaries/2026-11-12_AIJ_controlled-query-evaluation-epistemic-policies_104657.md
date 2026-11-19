# Controlled query evaluation under epistemic policies 总结

## 基本信息
- **标题**: Controlled query evaluation under epistemic policies
- **作者**: Gianluca Cima、Domenico Lembo、Lorenzo Marconi 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **卷期 / 文章号**: 362，文章号104657
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.artint.2026.104657 | 📄 [AIJ_2026_controlled-query-evaluation-epistemic-policies_104657.pdf](papers/AIJ_2026_controlled-query-evaluation-epistemic-policies_104657.pdf)
- **PDF许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 一句话概括
论文把认知依赖规则引入本体查询控制，使数据策略能约束用户可推知的信息，并分析其保密性与数据复杂度。

## 问题与动机
查询控制评估（CQE）通过过滤答案避免用户从数据库或本体推知敏感事实。传统否定式策略表达力有限，隐藏患者身份时甚至可能连患者存在与否也一并遮蔽；因此需要表达“若用户知道某事实，就必须同时知道某条件”等细粒度规则。论文研究这种策略下的可靠查询回答及计算代价。

## 方法
作者用认知算子K书写epistemic dependencies（ED），结合描述逻辑TBox、数据ABox和censor语义定义CQE。分析对所有最优censor取交集的SC-entailment及其保守近似IC-entailment，考察布尔合取查询（BCQ）及其并（BUCQ）的保密性和DL-Lite_R下复杂度，并给出无环ED策略的查询改写算法。

## 实验与结果
这是形式化理论研究，证据来自复杂度归约、保密性反例与定理证明，不是数据集实验。DL-Lite_R中，任意ED策略下BCQ和BUCQ的SC、IC回答问题均为coNP-complete；策略限为无环ED后，改写算法使数据复杂度降至AC0，可用一阶查询或SQL执行。对BUCQ，SC不保证保密性而IC保持；IC是满足性质的SC可靠近似中信息损失最小者。

## 贡献与局限
ED可表示开放查询答案隐藏和带条件披露约束，较闭式禁令更有表达力。论文明确任意策略的计算困难，并给出无环策略下的可处理边界及SQL改写路径。结论针对文中CQE语义、DL-Lite_R及数据复杂度；AC0是渐近类别，不代表实际系统的运行时间。

---
DOI: 10.1016/j.artint.2026.104657 | 📄 [AIJ_2026_controlled-query-evaluation-epistemic-policies_104657.pdf](papers/AIJ_2026_controlled-query-evaluation-epistemic-policies_104657.pdf)
