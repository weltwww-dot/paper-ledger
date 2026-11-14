# Efficient Approximation Algorithms for Resolvent Subgraph Centrality on Signed Graphs 总结

## 基本信息
- **标题**: Efficient Approximation Algorithms for Resolvent Subgraph Centrality on Signed Graphs
- **作者**: Yubo Sun、Haoxin Sun、Ahad N. Zehmakan 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(11)，7416-7429
- **发表**: 2026-09-02
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3730450

## 一句话概括
有符号网络中正负边共同影响节点中心性，传统无符号定义难以表达这种作用。论文推广 resolvent 子图中心性，并提出求解器法与根森林采样法，在计算成本和估计精度之间提供不同取舍。

## 问题与动机
如何在保留有符号边影响的同时，避免大图上精确计算 resolvent 中心性的高昂成本？

## 方法
定义有符号图的 resolvent 中心性；SOLVERRSC 用线性方程求解，SIMPLERSC 采用根森林抽样，GROUPRSC 与 NEIGHBORRSC 则从抽样森林提取更多信息以改善估计。

## 实验与结果
在八个真实网络上评估误差、方差和运行时间；GROUPRSC、NEIGHBORRSC 的平均相对误差低于 0.01，森林采样法在合成网络上的运行时间随网络规模近线性增长（PDF 第 11–12 页）。求解器精度较高但内存开销大，采样法则存在估计误差；衰减参数选择也会影响中心性排序（PDF 第 13 页）。

## 贡献与局限
给出有符号图中心性的自然推广，并提供数种可扩展近似算法及理论复杂度分析。实验覆盖的网络与参数范围有限；参数 α 没有统一选取准则，具体排序仍需结合应用解释。

---
DOI: 10.1109/tkde.2026.3730450
