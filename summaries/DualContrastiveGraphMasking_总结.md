# Dual contrastive learning with graph masking: A self-supervised framework for multi-view clustering 总结

## 基本信息

- **标题**: Dual contrastive learning with graph masking: A self-supervised framework for multi-view clustering
- **作者**: Jian-Sheng Wu, Wen-Ting Li, Jun-Yun Wu, Weidong Min
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108894
- **arXiv**: 无
- **PDF**: [NN_2026_DualContrastiveGraphMasking.pdf](papers/NN_2026_DualContrastiveGraphMasking.pdf)

## 一句话概括

论文提出 DCMGAL，通过随机边遮蔽、全局融合和双重对比学习，缓解多视图聚类中的噪声、冗余和跨视图表示同质化问题。

## 问题与动机

图式多视图聚类能够建模非线性关系，但图构建容易受噪声和冗余干扰。过度追求跨视图对齐又会抹平视图间的固有差异，导致表示缺乏区分性。

## 方法

DCMGAL 采用 masked aggregation，以随机边遮蔽放大视图差异并抑制噪声。全局特征融合机制结合双重注意力网络和 self-expression 网络，双重对比模块分别保持跨视图簇一致性和局部拓扑结构；图自编码器负责重构必要的邻接信息。

## 实验与结果

论文在多视图聚类基准数据集上开展广泛实验，并报告 DCMGAL 整体优于现有先进聚类方法。全文重点考察聚类效果、表示分离性及消融组件作用，未在摘要中给出统一的单一数字结果。

## 贡献与局限

贡献是把 masked graph autoencoder 与两类对比目标结合，并同时保留跨视图一致性和视图特异性。局限是效果依赖视图构造、遮蔽策略及超参数，面对更强噪声或视图缺失时的稳健性仍需验证。

---
DOI: 10.1016/j.neunet.2026.108894
