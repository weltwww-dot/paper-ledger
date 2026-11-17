# Controlling representation evolution in deep graph neural networks 总结

## 基本信息
- **标题**: Controlling representation evolution in deep graph neural networks
- **作者**: Jiajun Lin、Yuxin Tian、Li Feng 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109464
- **发表**: 2026-08-03
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109464

## 一句话概括
该框架通过稳定反应扩散传播、输入空间残差一致性和秩衰减控制改善深层 GNN 的表示演化，在多个节点分类数据集上提升准确率，但输入特征维度较高时辅助模块成本不可忽略。

## 问题与动机
深层 GNN 的重复传播会导致表示过度平滑或维度过早塌缩，如何直接控制表示随层数演化的轨迹而不局限于更换传播算子？

## 方法
方法组合稳定反应扩散传播（SRD）、输入空间残差一致性（RDC）和秩衰减率控制（RRC）：SRD调节前向传播轨迹，RDC约束投影回输入空间的逐层表示，RRC控制有效维数衰减速度。

## 实验与结果
在 CiteSeer、PubMed、Actor、Texas 及 ogbn-arxiv 等节点分类数据集上比较基线和组件消融；完整方法在 CiteSeer、PubMed、Actor、Texas 的准确率分别为 79.28%、89.40%、36.12%、78.95%，消融显示去除 SRD 后前三类数据表现明显下降；高维输入下 RDC 的二次特征维度成本可能成为负担（PDF 第 15 页）。

## 贡献与局限
把深层图表示演化拆分为传播稳定性、输入空间一致性与秩变化三类可控目标，并以消融验证其互补性；计算复杂度及不同特征规模下的效率需要结合具体数据进一步评估。

---
DOI: 10.1016/j.neunet.2026.109464
