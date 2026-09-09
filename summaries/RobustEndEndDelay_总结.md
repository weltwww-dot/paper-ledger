# Toward Robust End-to-End Delay Prediction: A GNN Approach With Routing-Aware Attention and Masked Subgraph Sampling 总结

## 基本信息

- **标题**: Toward Robust End-to-End Delay Prediction: A GNN Approach With Routing-Aware Attention and Masked Subgraph Sampling
- **作者**: Zichen Wang、Yiqi Chen、Dongwei Liu、Huile Wang、Yusong Zhou、Weiping Zheng
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3670186
- **arXiv**: 无
- **PDF**: [NN_2026_RobustEndEndDelay.pdf](papers/NN_2026_RobustEndEndDelay.pdf)

## 一句话概括

该文提出一种面向端到端时延预测的图神经网络，用统一的拓扑—路由图与路由感知注意力替代路由路径的顺序编码，并以掩码子图采样推断全局路由相关性，从而显著改善对未见路由方案的泛化能力。

## 问题与动机

端到端时延预测对智能网络管理至关重要，尤其是在时延敏感与动态变化的环境中。已有深度学习方法虽取得不错效果，但大多依赖对路由路径做顺序编码（如 RouteNet、FI-Graphormer 沿路径迭代更新状态），这种建模方式把模型与训练时见过的路由序列绑定，一旦测试中出现未见过的路由配置，泛化能力便明显下降。

## 方法

作者提出基于 GNN 的时延预测模型，包含三项设计：其一，构建统一的拓扑—路由图作为全局路由表示，模型直接从该图中查询与流相关的特征，而不再依赖路由序列编码；其二，设计路由感知注意力机制，使模型无需顺序处理即可从拓扑与路由信息中检索路由相关特征、学习全局路由相关性；其三，提出基于掩码的子图采样策略，让模型仅从部分流的交互中推断全局路由相关性，进一步增强对动态路由场景的适应性。训练以均方误差为损失，使用 Adam 优化器。

## 实验与结果

实验在四个公开数据集上展开——TnCwD、NSFNET、GBN 与 GEANT2，对比九种基线（含当前最优方法、常用 GNN 与时空预测模型），评价指标为 RMSE、R²、PCC 与 MAE，实验环境为 CentOS 7.9、PyTorch 2.3.1、CUDA 11.8 与两块 80GB NVIDIA A100。完整数据下的结果为：在难度最高的 TnCwD（模拟 TCP 与 UDP 混合流量）上，本模型 RMSE 0.0206、R² 0.9314、PCC 0.9662、MAE 0.0103，相比最优基线 FI-Graphormer 分别提升 9.25%、1.56%、0.64% 与 12.71%；在 NSFNET（GBN）上，四项指标为 0.2001（0.1496）、0.9584（0.9876）、0.9806（0.9945）、0.0921（0.0773），相较最优基线的提升分别为 1.48%（39.08%）、0.13%（2.15%）、0.22%（0.40%）与 −6.22%（33.42%），其中 NSFNET 上 MAE 0.0921 略高于 PLNet。在含未见路由路径的测试划分（Unseen-A/Unseen-B）上，所有模型表现均低于替换类划分（Substitution-A/B），说明未见路由路径确实更考验泛化；而本模型在四类测试集上均取得最优，两个消融变体（去掉路由感知注意力、去掉随机采样）性能均下降，验证了两个组件的有效性。

## 贡献与局限

- 用统一拓扑—路由图与路由感知注意力取代路由序列编码，从建模层面缓解对未见路由方案的泛化瓶颈。
- 提出掩码子图采样，使模型能从部分流交互推断全局路由相关性，兼顾精度与对动态路由的适应性。
- 在四个公开数据集、九种基线上全面取得最优或具竞争力的结果，并通过消融验证了关键组件。
- 局限：在 NSFNET 上 MAE 指标仍略逊于 PLNet；作者也指出未来需在更复杂、更动态的路由场景中进一步验证模型。

---
DOI: 10.1109/tnnls.2026.3670186
