# VLDUS: Vision-language distillated unseen synthesizer for zero-shot object detection 总结

## 基本信息

- **标题**: VLDUS: Vision-language distillated unseen synthesizer for zero-shot object detection
- **作者**: Caixia Yan、Muyan Jiao、Nuohan Xue、Weizhan Zhang、Jiahao Wang、Xiaojun Chang、Feng Tian
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108899
- **arXiv**: 无
- **PDF**: [NN_2026_Paper16.pdf](papers/NN_2026_VLDUS_ZeroShotObjectDetection.pdf)

## 一句话概括

VLDUS 把 CLIP 的图文知识蒸馏到未见类特征生成器，以提升零样本检测的多样性和泛化。

## 问题与动机

零样本目标检测常从已见类语义嵌入合成未见类视觉特征，但训练样本有限会导致生成特征多样性不足、过拟合已见类。研究希望同时提升未见类特征的类内多样性和类间可分性。

## 方法

VLDUS 设计两种互补的生成蒸馏策略，将预训练 CLIP 的图像–文本知识传给特征合成器。feature-aligned generative distillation 在判别器嵌入空间对齐 CLIP，降低对已见类的过拟合；relation-aligned generative distillation 蒸馏多样化图文关系，增强类内多样性。

## 实验与结果

作者在 MS COCO 2014、PASCAL VOC 2007/2012 和 DIOR 上评测 ZSD 与 GZSD。结果显示，VLDUS 生成的未见类特征具有更高类内多样性和类间分离度，并在两类任务上大幅优于 state-of-the-art 方法。

## 贡献与局限

贡献是把视觉–语言蒸馏用于零样本特征生成，并分别约束特征空间和关系空间。局限是依赖 CLIP 表示及类别语义质量，检测类别、域迁移和长尾分布下的表现仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.108899

