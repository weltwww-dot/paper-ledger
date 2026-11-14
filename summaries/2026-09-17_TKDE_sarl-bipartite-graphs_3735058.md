# SARL: A Scalable Attribute-Informed Representation Learning Framework for Bipartite Graphs 总结

## 基本信息
- **标题**: SARL: A Scalable Attribute-Informed Representation Learning Framework for Bipartite Graphs
- **作者**: Jianke Yu、Hanchen Wang、Chen Chen 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8485-8498
- **发表**: 2026-09-17
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3735058

## 一句话概括
大规模二部图同时包含两类顶点的结构与属性，但现有嵌入常假定两侧特征对齐，并依赖代价较高的注意力，难以兼顾表示质量和扩展性。论文提出 SARL，针对两类顶点差异化建模，并结合局部邻域与全局社区信号，为海量属性二部图学习表示。

## 问题与动机
如何在不要求两类顶点属性空间对齐的前提下，充分利用结构和属性信息，并把嵌入扩展到超大二部图？

## 方法
方法先以低秩 SVD 和局部、全局位置编码提取结构信息，再生成锚点以传播顶点信息；属性增强状态空间模型 ASSM 负责筛选和更新关键属性表示，以较低开销替代重注意力。最终以学习到的顶点嵌入支持链接预测和推荐。

## 实验与结果
在 Google、MovieLens、Amazon 和 Mag 四个真实数据集上进行链接预测、推荐与效率比较。相对次优方法，链接预测 Logloss 分别改善 3.57%、12.10%、3.23% 和 37.71%，AUC 相对提升 0.85%、0.70%、0.91% 和 0.91%；MovieLens 上训练速度提升至次快方法的三个数量级（PDF 第 8–9 页）。结果显示 Mag 的 GAUC 因三天时限未能计算，且实验覆盖的数据集有限。

## 贡献与局限
贡献是为异构二部图设计不对称的位置编码与属性增强状态空间嵌入，并展示大图上的精度和效率收益。局限在于最大数据集的部分指标因计算成本缺失，真实部署表现仍需更多领域和规模验证。

---
DOI: 10.1109/tkde.2026.3735058
