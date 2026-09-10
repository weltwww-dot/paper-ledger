# Multi-modal Interaction Enhanced Segment Anything Model (MIE-SAM) for RGB-T Salient Object Detection 总结

## 基本信息

- **标题**: Multi-modal Interaction Enhanced Segment Anything Model (MIE-SAM) for RGB-T Salient Object Detection
- **作者**: Ze Li, Ying Ying Zhang, Shuai Zhang, Zhi Peng Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109586
- **arXiv**: 无
- **PDF**: [NN_2026_MIESAM_RGBT.pdf](papers/NN_2026_MIESAM_RGBT.pdf)

## 一句话概括

MIE-SAM 将 SAM 改造成 RGB-T 双分支、动态融合且无需人工提示的显著目标检测模型，以适应低照度、雨雾和复杂背景。

## 问题与动机

RGB 和热红外图像具有互补信息，但固定融合策略难以应对环境变化，像素级标注稀缺又容易过拟合。SAM 的 RGB 预训练、缺乏显著性语义和手工 prompt 依赖限制了其直接迁移。

## 方法

模型把 SAM 图像编码器重构为权重共享的双分支，并在冻结编码器中加入 Multi-modal LoRA，以参数高效地注入显著性语义和跨模态交互。Dynamic Fusion Module 按环境可靠性学习融合权重，Progressive Decoder Module 直接输出细粒度显著图。

## 实验与结果

在多个公开 RGB-T 显著目标检测数据集上，MIE-SAM 达到文中报告的 state-of-the-art，并显示出复杂场景下的鲁棒性和泛化能力。论文还提供了代码链接；摘要未给出具体指标数值。

## 贡献与局限

贡献是将 SAM 的先验知识、低秩适配和动态多模态融合结合，并实现 prompt-free 端到端预测。局限是性能仍依赖 RGB-T 配准和公开数据分布，极端传感器失效及更少标注条件需进一步验证。

---
DOI: 10.1016/j.neunet.2026.109586
