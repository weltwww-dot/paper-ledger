# Continual Test-Time Training on Graphs via Adaptive Prompts Integration 总结

## 基本信息

- **标题**：Continual Test-Time Training on Graphs via Adaptive Prompts Integration
- **作者**：Qianyi Cai, Ziyue Qiao, Rui Cai, Huijie Liu, Junyi Li, Xiao Luo, Hui Xiong
- **期刊 / 会议**：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **发表**：2026-04-27
- **研究方向**：图机器学习、持续学习、无监督图域适应
- **DOI**:10.1109/tpami.2026.3687933 · **PDF**：[TPAMI_2026_ContinualTestTimeTraining.pdf](papers/TPAMI_2026_ContinualTestTimeTraining.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 DPCGL（Dynamic Prompts-based Continual Graph Learning），在冻结预训练 GNN 的前提下，用可动态选择和更新的图提示池持续适应无标签、不断变化的 OOD 图域，并以多目标优化缓解长期适应中的灾难性遗忘。

## 问题与动机

传统 graph test-time training 多针对单步适应，连续处理多个 OOD 图时会遗忘早期域；直接为每个新图训练独立模型又带来参数、存储和模型选择成本。监督式 continual learning 依赖标签、明确任务边界或静态回放缓存，而测试时通常都不可用，因此需要一种无需源数据和标签、能累积知识且保持参数高效的图适应机制。

## 方法

DPCGL 冻结骨干参数，仅维护可训练的动态 prompt pool。每个新图先用骨干节点嵌入的均值与提示向量做余弦相似度，选取 top-k_p 提示，并通过可微投影作为附加节点注入输入图；提示之间按相似度阈值连边，提示与原节点连接 top-k_n 条边。训练以熵最小化实现无监督适应，同时加入 K-means 代表性相似度损失、提示多样性损失和基于 EMA 历史 logits 的 KL 正则；共享池在每个域结束后写回已选提示。作者还给出基于冻结编码器 Lipschitz 性质、提示子空间谱残差和图扰动的累计 RMSE 界，说明提示子空间与构造图质量共同影响持续适应误差。

## 实验与结果

实验覆盖 Facebook-100、Twitch-Explicit、OGB-Arxiv 和 Elliptic 四类跨域或时间变化图数据：分别先在指定源图/时间片预训练，再对剩余目标域在线、无标签适应；比较 Test、DANN、Tent、EERM、GTrans、GraphCTA、GraphATA、Matcha、CoTTA、EATA、EcoTTA、BECoTTA 等基线，使用 Accuracy、ROC-AUC 或 F1，并以 Average Performance 和 Average Forgetting 评估。正文报告 DPCGL 在四个数据集上均超过比较方法并达到新的 SOTA，且准确率矩阵显示其较 CoTTA 更能保持旧域性能。消融表明适应、代表性、KL 保留、多样性及共享提示池组合最好；top-k_n 在 OGB-Arxiv 取 6、其他数据集取 4，提示相似度阈值 0.05、0.10、0.20 下性能总体稳定；GCN、GraphSAGE、GAT、GIN 上均有增益。

## 贡献与局限

贡献包括：提出面向连续 OOD 图测试时训练的动态提示框架；以冻结骨干、提示选择/写回和代表性—保留—多样性联合目标实现参数高效的知识累积；用理论界与四类图数据实验验证适应性和抗遗忘性。局限方面，全文主要验证四个图数据集和节点分类场景，提示比例、连边阈值及损失权重仍需经验设定；理论分析依赖冻结编码器的 Lipschitz 与低秩提示子空间等假设，作者未报告在更大规模或更复杂任务上的结果。

---
DOI: 10.1109/tpami.2026.3687933
