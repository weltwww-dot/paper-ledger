# Adaptive Graph Convolution With Diffusion Models for Multimodal Recommendation 总结

## 基本信息

- **标题**: Adaptive Graph Convolution With Diffusion Models for Multimodal Recommendation
- **作者**: Jie Guo, Ziyuan Guo, Bin Song, Peidong Zhang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3706381
- **arXiv**: 无
- **PDF**: [TKDE_2026_AdaptiveGraphConvDiffusion.pdf](papers/TKDE_2026_AdaptiveGraphConvDiffusion.pdf)

## 一句话概括

本文提出 DiffGCN，首次用条件扩散模型替代固定传播规则实现自适应图卷积，通过融合语义与行为双源邻域并迭代去噪精化物品表征，在三个真实数据集上全面超越多模态推荐基线。

## 问题与动机

多模态推荐系统（MRSs）通过引入物品的图像、文本等内容缓解协同过滤中的数据稀疏与冷启动问题。近年基于结构的 MRSs 依据模态特征相似度显式构建 item–item 图并用图卷积网络（GCN）传播信息，但存在两大挑战：C1 单一来源邻域——仅由单一模态相似度建图会引入模态噪声（如无关图像背景、冗余文本），并忽略如"物品–用户–物品"的行为关系；C2 固定传播规则——多数方法沿用 LightGCN 式对所有节点统一聚合的规则，在语义相近物品邻域高度重叠时模糊细粒度语义区分，降低表征质量与推荐性能。

## 方法

DiffGCN 由三大组件构成：a) 自适应多源邻域融合：分别基于模态特征余弦相似度经 kNN 稀疏化（top-k）构建语义邻域图，基于用户交互中的物品共现（top-k 且阈值 ε 剪枝）构建行为邻域图，再用逐物品可学习权重向量 α 加权融合为最终邻域图（C^m = diag(α)·S^m + (I − diag(α))·S^b），实现个性化取舍；b) 扩散感知表征学习：将模态特征经 MLP 与 ℓ2 归一化映射到隐空间，以邻域表征为条件，用基于 DDPM 的条件扩散模型逐步加噪、并由引导去噪网络（GD-Net，MLP）多步迭代去噪精化物品表征，推理时引入 classifier-free guidance（强度参数 ω）控制邻域信息影响；c) 交互偏好增强：以 LightGCN 为基础推荐器在 user–item 图上按模态传播（L 层、残差连接、跨层求和、跨模态拼接），联合 BPR 损失与扩散 MSE 损失训练。另提出高效变体 DiffGCN-IM，基于 DDIM 将反向去噪步数从 T 压缩到 S，把扩散表征学习复杂度由 O(T|I|h²) 降至 O(S|I|h²)。

## 实验与结果

在 Amazon 的 Baby、Sports、Electronics 三个 5-core 数据集上（4096 维 CNN 视觉特征、384 维 sentence-transformers 文本特征），以 Recall@K 与 NDCG@K（K=10,20）为指标，对比 BPR-MF、LightGCN、VBPR、MMGCN、SLMRec、BM3、LATTICE、FREEDOM、MGCN、LGMRec、DiffMM 等基线。结果显示 DiffGCN 在所有数据集上一致超越全部基线（含最新扩散方法 DiffMM）。消融实验表明：去掉扩散学习模块（DiffGCN-DL）性能下降最明显，替换为 LightGCN（DiffGCN-LG）同样明显下降，去掉行为邻域图（DiffGCN-BG）在各数据集均有下降且在 Sports、Electronics 上更显著；仅文本模态优于仅图像模态，双模态全量最优。参数敏感性：ω=0 时性能大幅下降，过大的 ω（如 8）导致过拟合退化（Electronics 最优 ω=6）；噪声尺度 s=0.01 对 Sports、Electronics 最优，小数据集 Baby 上 s=0.001 更佳。效率上，DiffGCN 内存占用最低；DiffGCN-IM（S 取 2/5/8）在 Baby 上 R@20 与 N@20 仅降 1.8% 与 2.5%，Sports/Electronics 损失在 1% 以内甚至略升，Electronics 上训练时间最高缩减 45.4%，Baby 与 Sports 总训练时间分别缩减 45.4% 与 58.9%，推理时间在三个数据集分别缩减 10.0%、5.8%、47.4%。可视化与案例分析显示 DiffGCN 的表征分布更均匀分散，且能检索到语义更一致的结果（如婴儿玩具、腕带手套），减少语义漂移。

## 贡献与局限

贡献：提出 DiffGCN，首个利用条件扩散模型实现自适应图卷积的多模态推荐框架，克服单源邻域与固定传播规则两大局限；提出基于可学习逐物品权重的语义—行为多源邻域自适应融合，并以多步去噪过程迭代精化表征；提出 DDIM 加速变体 DiffGCN-IM，在极小精度损失下显著提升训练与推理效率；代码已开源（https://github.com/ZyGuo-0708/DiffGCN）。局限与展望：扩散过程的多步去噪带来额外训练与推理开销（需 DiffGCN-IM 缓解）；引导强度等超参数对性能敏感，需仔细调参；本文实验场景限于同构 item–item 图，作者计划未来将自适应去噪范式推广到关系类型与图结构更复杂的异构图。

---
DOI: 10.1109/tkde.2026.3706381
