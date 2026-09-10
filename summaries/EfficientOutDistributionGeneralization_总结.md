# Efficient Out-of-Distribution Generalization for Pretrained GNNs via Prompt Learning 总结

## 基本信息

- **标题**: Efficient Out-of-Distribution Generalization for Pretrained GNNs via Prompt Learning
- **作者**: Zhenmeng Zuo, Changsheng Li, Mingkui Tan, Xing Gong, Ye Yuan, Guoren Wang
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3666523
- **arXiv**: 无
- **PDF**: [TAI_2026_EfficientOutDistributionGeneralization.pdf](papers/TAI_2026_EfficientOutDistributionGeneralization.pdf)

## 一句话概括

EGOG 通过提示学习复用预训练 GNN，从节点特征和图结构两方面提取因果子图、抑制伪相关信息，以较少可训练参数提升图数据的分布外泛化能力。

## 问题与动机

图 OOD 泛化要求模型面对训练环境之外的新图分布仍保持可靠预测。已有方法往往从头训练复杂因果推理模型，计算成本高且忽视成熟预训练 GNN 的表示能力；同时，分布偏移不仅影响节点特征，也会改变图结构，单独处理某一方面容易把结构伪相关留在解释中。作者希望在冻结或基本复用预训练 GNN 的前提下，通过轻量提示模块分离节点和结构层面的因果信息与伪信息。

## 方法

EGOG 的图因果提示模块由因果特征生成器（CFG）和因果结构生成器（CSG）组成。CFG 利用图提示学习引导预训练 GNN 从节点表示中解耦因果特征与伪特征；CSG 复用预训练 GNN 分析图结构，提取因果子结构并抑制结构伪相关。模型加入梯度反转层，使表示对环境相关伪信息不敏感，并用信息瓶颈限制无关信息通过。由于主要训练提示和生成模块而非完整 GNN，方法在保持预训练知识的同时降低了训练参数量与计算开销。

## 实验与结果

作者在 GOODMotif、GOODCMNIST 等合成 OOD 数据集上进行环境变化和无环境标签实验。与最先进基线相比，EGOG 在两个合成数据集上的平均相对性能提升 2.73%，可训练参数量平均仅为基线的 4.38%。在 GOODCMNIST、批大小 64、NVIDIA RTX 2080 Ti 环境中，EGOG 的训练/推理延迟为 `54.37/22.74 ms`，低于全量微调的 `60.84/23.49 ms` 和 LECI 的 `195.13/96.09 ms`。消融与超参数实验验证信息瓶颈、梯度反转以及节点/结构两个生成器都对 OOD 泛化有贡献；无环境标签时，EGOG 仍能利用因果提示取得稳定表现。

## 贡献与局限

贡献在于把预训练 GNN、提示学习和因果子图解耦结合起来，以较小训练开销同时处理节点和结构分布偏移，并通过轻量模块提高 OOD 泛化。局限是因果/伪相关分离依赖环境变化与预训练表示是否包含足够信息，合成数据上的收益不一定直接迁移到大规模真实图；梯度反转和信息瓶颈的权重也需要调节。更复杂的异构图、动态图、标签分布偏移和预训练模型架构变化仍需进一步评估。

---
DOI: 10.1109/tai.2026.3666523
