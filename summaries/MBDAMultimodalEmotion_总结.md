# MBDA: A modality-balanced framework with data augmentation and alignment for multimodal emotion recognition 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：MBDA: A modality-balanced framework with data augmentation and alignment for multimodal emotion recognition
- 作者：Cheng Cheng, Ruisi Shang, Zixu Wang, Huazhi Li, Ziyu Jia
- 期刊 / 年份：Neural Networks，2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108852
- PDF：[MBDAMultimodalEmotion.pdf](papers/MBDAMultimodalEmotion.pdf)

## 一句话概括

论文提出 MBDA，将 modality-aware data augmentation、多层特征 alignment 与 counterfactual knowledge distillation 组成统一的渐进式学习框架，以缓解多模态情感识别中的模态失衡、跨模态错位和数据多样性不足。

## 问题与动机

EEG、面部表情和眼动等模态具有互补信息，但数据质量、噪声敏感性和语义表达不同，训练时强模态可能压制弱模态。现有增强方法还可能造成语义漂移和跨模态不一致，而简单拼接或单层对齐难以保持不同增强强度下的表示一致性。因此需要同时处理样本多样性、模态内一致性和模态间语义对齐，并动态平衡各模态贡献。

## 方法

MBDA先用模态专属特征提取器处理输入，再施加弱、强等不同强度的模态感知增强，并以对比一致性约束保持原始语义。多层、多视角 alignment 同时约束同一模态不同增强视图的一致性，以及不同模态之间的语义一致性。counterfactual knowledge distillation 构造跨模态排序关系和反事实样本，根据教师–学生预测差异动态调整模态权重，增强弱模态并抑制强模态冗余，最后进行融合分类。

## 实验与结果

论文在 DEAP 和 SEED-IV 上评估，报告 DEAP-A、DEAP-V、DEAP-AV 和 SEED-IV 的准确率分别为 93.86%、95.11%、91.02% 和 92.66%，并持续优于 state-of-the-art 方法。实验和消融结果支持三类模块及其闭环协同：增强提升数据多样性，对齐保持语义一致性，反事实蒸馏改善模态贡献平衡。

## 贡献与局限

贡献包括：提出把增强、对齐和蒸馏互相耦合的模态平衡框架；提出兼顾模态内与模态间一致性的多层对齐机制；提出基于反事实样本和跨模态排序的动态蒸馏。局限在于实验主要覆盖论文所选的 EEG、面部和眼动模态组合及 DEAP/SEED-IV 数据分布；对缺失模态、更多真实环境噪声和更大规模跨被试部署的适应性仍需验证。

---
DOI: 10.1016/j.neunet.2026.108852
