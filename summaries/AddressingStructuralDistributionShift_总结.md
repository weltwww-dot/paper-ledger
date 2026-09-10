# Addressing Structural Distribution Shift in Explanations for Graph Neural Networks 总结

## 基本信息

- **标题**: Addressing Structural Distribution Shift in Explanations for Graph Neural Networks
- **作者**: Zhuomin Chen, Hojat Allah Salehi, Esteban Schafir, Xu Zheng, Jiaxing Zhang, Hua Wei, Jingchao Ni, Farhad Shirani, Dongsheng Luo
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3690304
- **arXiv**: 无
- **PDF**: [TPAMI_2026_AddressingStructuralDistributionShift.pdf](papers/TPAMI_2026_AddressingStructuralDistributionShift.pdf)

## 一句话概括

本文指出 GNN 解释子图与模型训练图之间存在被忽视的结构分布偏移，并提出 EdgeDropExplainer 与 ProxyExplainer，用保持解释信息且贴近原始分布的代理图改善解释可靠性。

## 问题与动机

GNN 解释方法通常从原图中抽取少量节点或边作为解释，但 GNN 实际训练时看到的是完整图，抽取后的解释子图在节点数、度分布、聚类系数或谱结构上可能与训练分布明显不同。即使一个子图在语义上是真实解释，模型也可能因为 OOD 输入而无法正确预测，导致传统 fidelity 指标和解释结论失真。作者因此希望同时满足解释的充分性、最小性与分布内性质，避免解释方法只追求“更小”而牺牲模型可解释行为的可信度。

## 方法

论文先从信息论角度形式化解释子图的充分性和最小性，并提出代理图概念：代理图保留关键解释信息，同时让结构统计接近原始训练图。EdgeDropExplainer 通过边删除生成轻量代理图；ProxyExplainer 进一步采用双层优化，把解释器与非解释子图生成器结合起来，利用变分自编码器生成补充结构，并使用 KL 项和分布约束减少结构偏移。作者以图统计量之间的最大均值差异（MMD）衡量分布接近程度，同时用 AUC、正/负 fidelity 和节点分类任务评估解释质量。

## 实验与结果

实验覆盖分子、生物、社交网络和合成图数据集，包括 MUTAG、Benzene、Alkane-Carbonyl、Fluoride-Carbonyl、BA-2motifs、BA-3motifs、D&D、OGBG-MolHIV、IMDB-BINARY 和 REDDIT-BINARY，并额外测试 Tree-Cycles/Tree-Grid 节点分类。每组实验运行 10 次取平均和标准差。ProxyExplainer 在除 Alkane-Carbonyl 外的真实数据集上平均 AUC 比领先基线高 6.9%，在合成数据集上平均高 7.5%，并在大规模 D&D、OGBG-MolHIV 与 IMDB-BINARY 上保持有效。MMD 分析显示，真实解释子图和 PGExplainer 结果常与原图有明显偏移，而代理图通常比 MixupExplainer 更接近原始分布；去掉非解释子图生成器、规模约束或分布约束都会使性能下降。参数分析表明在所测范围内 `λ∈[0.25,1.0]` 表现稳定，节点潜变量维度 512 时效果最好。

## 贡献与局限

贡献包括：明确揭示 GNN 解释中的结构分布偏移问题；建立同时考虑解释充分性、最小性与分布内约束的理论框架；提出边删除和代理图两种实现，并在多类型图任务上验证了可靠性。局限是代理图生成增加了训练与调参成本，性能依赖潜变量维度、KL 权重和分布约束；实验主要针对图分类及部分节点分类，真实动态图、异构图和更复杂消息传递架构仍需验证。方法还默认待解释 GNN 已训练良好，若原模型本身存在偏差，解释质量不能单靠代理图生成完全修复。

---
DOI: 10.1109/tpami.2026.3690304
