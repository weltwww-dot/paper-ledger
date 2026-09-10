# TCPFMC: Trustworthy Cyclic Progressive Fusion for Multimodal Classification 总结

## 基本信息

- **标题**: TCPFMC: Trustworthy Cyclic Progressive Fusion for Multimodal Classification
- **作者**: Ao Li, Dehua Miao, Tianyu Gao, Sanlin Mei, Fengwei Gu, Chen Chen, Aichen Wang, Haoyi Fan, Xinwang Liu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3661974
- **arXiv**: 无
- **PDF**: [NN_2026_TCPFMCTrustworthyCyclicProgressive.pdf](papers/NN_2026_TCPFMCTrustworthyCyclicProgressive.pdf)

## 一句话概括

TCPFMC 先用模态能量分数评估每个模态的可靠性，再以循环渐进方式逐对融合模态信息，从而减少噪声模态和简单拼接造成的模态偏置与特征丢失。

## 问题与动机

多模态分类通常把不同来源的特征直接拼接或映射到统一空间，但现实数据中的模态质量不均衡，噪声或冗余模态可能主导融合结果；过早压缩也会丢失具有判别力的模态特有信息。已有动态融合方法能够估计置信度，却常在决策层操作，难以保留细粒度模态关系。作者希望在不依赖真实类别概率的情况下估计模态信息量，并在渐进融合中维持每种模态的独特结构。

## 方法

TCPFMC 为每个模态设置独立编码器、分类器和模态记忆库，利用样本表示与模态中心及记忆模式的关系计算能量分数，把它作为当前模态的置信权重。融合阶段采用循环渐进策略，按模态对逐步组合表示，而不是一次性拼接全部特征；模态特定映射和对抗对齐帮助把源模态信息映射到目标模态，同时减少模态差异带来的偏移。总目标联合分类、置信度与融合相关损失，并通过后续阶段继续利用前面已经融合的表示。

## 实验与结果

作者在 BRCA、ROSMAP、LGG、KIPAN、MVSA 和 FOOD101 六个多模态数据集上进行实验。TCPFMC 在四个生物医学数据集上总体取得最佳表现；以 BRCA 多分类任务为例，相比最佳单模态方法，ACC、Weighted-F1 和 Macro-F1 分别提升 12.9、14.8 和 17.6 个百分点，在 LGG 与 ROSMAP 的二分类任务上也保持领先。在 MVSA 和 FOOD101 等通用多模态基准上表现同样具有竞争力。消融实验显示，单独加入能量置信度或渐进融合都能提升结果，完整模型在六个数据集上最优；MVSA 中能量模块带来约 7.2% ACC 和 6.3% Weighted-F1 的提升。

## 贡献与局限

贡献在于提出无需真实类别概率的模态能量评估，以及保留模态特有信息的循环渐进融合，并在生物医学与通用多模态任务中验证鲁棒性。局限是当前方法仍假设各模态可用，模态缺失、严重错位和样本量很小的场景可能影响记忆中心与能量估计；多阶段映射和对抗训练也会增加优化复杂度。未来需要扩展到不完整模态、在线模态到达和更大规模多模态数据。

---
DOI: 10.1109/tnnls.2026.3661974
