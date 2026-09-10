## 基本信息

- **标题**：Recent Advances of Multimodal Continual Learning: A Comprehensive Survey
- **研究方向**：多模态持续学习（MMCL）
- **作者**：Dianzhi Yu、Xinni Zhang、Yankai Chen、Aiwei Liu、Yifei Zhang、Philip S. Yu、Irwin King
- **期刊 / 年份**：IEEE Transactions on Neural Networks and Learning Systems，2026
- **DOI**:10.1109/TNNLS.2026.3658485
- **PDF**：[NN_2026_RecentAdvancesMultimodalContinual.pdf](papers/NN_2026_RecentAdvancesMultimodalContinual.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文系统综述多模态持续学习，解释多模态灾难性遗忘、模态不平衡、复杂交互、高计算成本和预训练 zero-shot 能力退化等问题，并整理方法、基准与未来方向。

## 问题与动机

传统持续学习要求模型在连续接收新任务时保留旧知识，而多模态数据会使不同模态以不同速度学习和遗忘，并带来对齐、融合和缺失模态等额外困难。直接叠加单模态持续学习方法常造成严重遗忘；在预训练多模态 backbone 上持续微调还可能损失原有 zero-shot 能力，因此需要专门的 MMCL 设定、指标和方法体系。

## 方法

论文先形式化任务序列、模态静态/动态设置和五种场景：CIL、DIL、TIL、XDIL 与 MDTIL，并介绍平均性能、遗忘、BWT、FWT、zero-shot transfer、模态平均性能、平均差异和平均融合效果等指标。随后将方法归纳为 regularization-based、architecture-based、replay-based 和 prompt-based 四类，分别讨论模态一致性/关系约束、任务或模态驱动结构、自然或交互式回放、多模态或 universal prompt，并汇总数据集与 benchmark。

## 实验与结果

这是综述论文，原文未报告新的统一对比实验；其结果是对现有研究的结构化整理。文中汇总了 P9D（超过一百万图文对、九个工业类别任务）、LILAC、UESTC-MMEA-CL、CLiMB、CLOVE、MTIL、IMNER、IMRE 和 MMCL 等基准，并指出已有结果中 replay 往往比 EWC/LwF 更能缓解遗忘，而多模态输入在持续学习中仍可能不如单模态。综述还观察到研究重心已从从头训练转向 CLIP、BLIP2 等 foundation model 的参数高效适配。

## 贡献与局限

贡献包括：给出首个综合 MMCL 方法 taxonomy；统一整理五种场景、评估指标、数据集和 benchmark；围绕缺失模态、更多模态、PEFT、预训练知识维护、prompt 方法及可信 MMCL 提出研究方向，并维护 Awesome-Multimodal-Continual-Learning 资源仓库。局限是该领域仍处于早期，除 vision-language 外的模态和大规模真实世界 benchmark 较少，现有数据常由已有数据集拼接或切分得到；文中未提供新的统一复现实验。
