# Neural network pruning and simultaneous feature and structure selection 总结

## 基本信息

- **标题**: Neural network pruning and simultaneous feature and structure selection
- **作者**: Xinyue Zhang, Hong Gu, Toby Kenney
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108977
- **arXiv**: 无
- **PDF**: [NN_2026_NeuralNetworkPruningSelection.pdf](papers/NN_2026_NeuralNetworkPruningSelection.pdf)

## 一句话概括

本文将神经网络LASSO剪枝重写为加权回归/分类问题，同时选择输入特征和网络结构，以减少冗余并提升可解释性。

## 问题与动机

大型网络便于拟合复杂关系，却带来部署成本和解释困难；简单删权重又可能损失预测能力。理想的剪枝方法应同时处理输入特征选择、连接结构选择和模型拟合质量。

## 方法

作者从包含所有可能前馈子网络的致密结构出发，将神经网络LASSO问题重构为带LASSO惩罚的标准加权回归或分类问题。第一步去除大量冗余，第二步逐条循环剩余连接，删除不能充分改善模型拟合的连接。

## 实验与结果

四项模拟研究显示方法在回归和分类中有效且稳定；十个真实数据示例（五个回归、五个分类）中，方法相对原始致密网络和最新剪枝方法取得更好的预测与解释表现。

## 贡献与局限

贡献是把特征与结构选择统一到可解释的稀疏惩罚流程。局限是逐连接循环可能在超大网络上增加计算量，LASSO惩罚和加权拟合对特征尺度、相关性及初始化的敏感性仍需系统分析。

---
DOI: 10.1016/j.neunet.2026.108977
