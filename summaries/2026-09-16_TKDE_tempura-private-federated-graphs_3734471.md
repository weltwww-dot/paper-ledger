# TEMPURA: Privacy-Preserving Federated Learning on Temporal Transaction Graphs 总结

## 基本信息
- **标题**: TEMPURA: Privacy-Preserving Federated Learning on Temporal Transaction Graphs
- **作者**: Jianbin Gao、Kombou Victor、Qi Xia 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8515-8527
- **发表**: 2026-09-16
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3734471

## 一句话概括
TEMPURA面向跨机构加密货币交易图欺诈检测，结合时序图学习、联邦协作与差分隐私，尝试在减少数据集中暴露的同时保留检测能力。

## 问题与动机
单机构难以观察跨组织交易模式，而集中共享交易记录有隐私代价；已有研究较少在统一保证下同时处理时序建模、联邦鲁棒性与隐私噪声。

## 方法
框架引入时间邻域隐私噪声校准、稳健联邦图聚合及多时间尺度差异学习；摘要给出相同隐私参数下噪声标准差降低 79%，并报告对拜占庭参与者的稳健性。

## 实验与结果
四个交易数据集（最大 2.03 亿边）上，无隐私 F1 为 0.9012，ε=1.0 时 F1 为 0.8654；30% 拜占庭参与下 F1 为 0.82，论文还报告其隐私机制相对标准高斯机制的噪声优势（PDF 第 1 页）。

## 贡献与局限
工作把图时序检测、隐私机制和稳健聚合纳入一个框架，并给出理论与实测证据。数据集及攻击评估范围有限，指标不保证真实机构部署效果。

---
DOI: 10.1109/tkde.2026.3734471
