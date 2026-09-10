# Quantum-enhanced learning: Leveraging von Neumann entropy for enhanced graph neural network performance 总结

## 基本信息

- **标题**: Quantum-enhanced learning: Leveraging von Neumann entropy for enhanced graph neural network performance
- **作者**: Muhammad Awais, Octavian Adrian Postolache, Sancho Moura Oliveira
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108958
- **arXiv**: 无
- **PDF**: [NN_2026_QuantumEnhancedGNN.pdf](papers/NN_2026_QuantumEnhancedGNN.pdf)

## 一句话概括

论文提出带 Quantum Entanglement Loss 的 QGNN，以 von Neumann 熵正则化缓解图神经网络的 over-squashing 和长程依赖瓶颈。

## 问题与动机

GNN 的局部消息传递会把指数增长的邻域信息压缩到固定维度，导致远距离节点间信息丢失。现有平滑或最大熵正则化并不直接提供跨多跳的信息通路，因此作者寻找另一种结构约束。

## 方法

QEL 最小化节点嵌入相关矩阵的 von Neumann 熵，使特征值集中于保留全局结构模式的主导模态。该机制在功能相关但相距较远的节点间形成更直接的信息路径，作为 QGNN 的训练正则项。

## 实验与结果

实验覆盖 Cora、Citeseer、PPI、Electronic Circuits 和 LRGB。Peptides-struct 上相对 GCN 的 MAE 降幅为 37.6%，较 GraphGPS 提升 4.0%，7 跳以上节点对上较 GCN 提升 97%；额外计算开销约 20%–30%，速度约为 Graph Transformer 的 5–6 倍。

## 贡献与局限

贡献是把量子信息论中的熵量引入 GNN 长程建模，并兼顾效果与效率。局限是“量子”机制仍是启发式正则化，收益依赖相关矩阵和任务设置，在更多图类型及更大规模图上的稳定性需继续验证。

---
DOI: 10.1016/j.neunet.2026.108958
