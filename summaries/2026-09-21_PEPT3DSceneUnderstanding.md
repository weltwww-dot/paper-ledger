# Parameter-efficient prompt tuning based on adaptive fused pre-trained models for 3D scene understanding 总结

## 基本信息
- **标题**: Parameter-efficient prompt tuning based on adaptive fused pre-trained models for 3D scene understanding
- **作者**: Xinyan Huang、Fang Liu、Licheng Jiao et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-21
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109662
- **PDF**: [NN_2026_PEPT3DSceneUnderstanding.pdf](papers/NN_2026_PEPT3DSceneUnderstanding.pdf)

## 一句话概括
本文以多层提示生成和自适应特征融合适配预训练点云模型，在减少可训练参数的同时完成三维场景理解任务。

## 问题与动机
针对点云任务微调整个预训练模型成本较高、不同模型表征互补难以利用的问题，作者研究如何以参数高效方式融合预训练知识并适配下游任务。

## 方法
PEPT 以多层提示生成模块向预训练点云网络注入任务信息，并用轻量自适应融合头整合不同模型特征。在 ScanObjectNN、ModelNet40 和 ShapeNetPart 上评估分类、少样本识别及部件分割，并与全量微调等方法比较。

## 实验与结果
论文报告多个三维任务上具有竞争力；大多数任务中可训练参数约为全量微调的 2%。实验涵盖不同数据集与任务，说明提示学习和多模型融合具有互补性，但具体收益随基准而变化。

## 贡献与局限
- 结合多层提示学习与预训练点云模型自适应融合，避免更新全部参数。
- 在分类、少样本识别和部件分割中进行评估。
- 证据集中于论文选取的模型与数据；参数量下降并不意味着训练时长或推理成本同比下降。

---
DOI: 10.1016/j.neunet.2026.109662
