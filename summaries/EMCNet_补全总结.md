# Meta-path and context-aware learning for attribute completion in heterogeneous graphs 总结

## 基本信息
- **标题**: Meta-path and context-aware learning for attribute completion in heterogeneous graphs
- **作者**: Geng Chen, Yuan Feng, Lijun Zhang, Xiaoyu Bai, Qingyue Wang, Peng Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108895
- **PDF**: [NN_2026_EMCNet.pdf](papers/NN_2026_EMCNet.pdf)

## 一句话概括
EMC-Net 利用 meta-path 语义和上下文注意力补全异质图属性，并直接支持下游节点分类。

## 问题与动机
现有 HGAC 方法忽视 meta-path、过度依赖邻居，并在补全后再使用异质 GNN，造成语义损失和计算低效。异质图中的长程语义关系需要显式建模。

## 方法
框架采用 collaborative meta-path-driven embedding，在随机游走中注入 meta-path 先验；context-aware attention 动态调整节点和边权重，以利用非邻居信息；增强 graph attention network 直接处理下游任务。

## 实验与结果
三个真实世界数据集实验显示 EMC-Net 在属性补全准确性和计算效率上优于既有 HGAC 方法，并可作为基线模型的 plug-and-play 插件。

## 贡献与局限
贡献是统一元路径、上下文补全与下游任务。局限是元路径设计、图规模和缺失机制会影响效果，复杂动态图上的可扩展性仍需研究。

---
DOI: 10.1016/j.neunet.2026.108895
