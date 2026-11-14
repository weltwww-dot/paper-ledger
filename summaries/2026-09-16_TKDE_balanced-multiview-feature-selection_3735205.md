# Balanced Multi-View Feature Selection via Differential Information Loss and ℓ²(ln,2)-Norm Regularization 总结

## 基本信息
- **标题**: Balanced Multi-View Feature Selection via Differential Information Loss and ℓ²(ln,2)-Norm Regularization
- **作者**: Jiaye Li、Zhongle Xie、Ke Chen 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，7991-8008
- **发表**: 2026-09-16
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3735205

## 一句话概括
多视图数据能提供互补信息，但类别不平衡会让特征选择偏向多数类，使少数类表示不足。本文提出面向不平衡多视图数据的特征选择框架，通过度量各类别的信息损失并适配视图权重，力求同时保留判别性和稀疏性。

## 问题与动机
如何在多视图特征冗余和类别比例失衡并存时，选择对各类别都有效且紧凑的特征？

## 方法
框架以差异化信息损失刻画各类别的信息差距，减轻多数类对目标函数的支配；引入视图专属权重，自适应反映不同视图的重要性，并提出 ℓ₂ln,₂ 范数稀疏正则项约束关系矩阵。通过联合优化获得用于下游分类的特征子集。

## 实验与结果
对照实验覆盖类别均衡和失衡的公开多视图数据。均衡数据上的优势较小，在失衡的 Caltech-256 和 iNaturalist 上，作者报告准确率、精确率、召回率和 F1 的综合优势更为明显（PDF 第 11–13 页）。

## 贡献与局限
论文把类别间信息损失、视图加权和稀疏约束纳入一个目标，在类别失衡时同时关注少数类和总体分类表现。高维视图上的计算成本和更复杂失衡分布下的稳定性仍需验证。

---
DOI: 10.1109/tkde.2026.3735205
