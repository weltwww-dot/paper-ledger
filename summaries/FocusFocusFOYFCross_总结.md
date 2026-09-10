## 基本信息

- **标题**：Focus on Your Focus (FOYF): Cross-Domain Few-Shot Semantic Segmentation by Attention Specialization
- **研究方向**：跨域 few-shot semantic segmentation、Transformer attention
- **作者**：Jiaming Xu、Zegeng Wei、Zhifu Huang、Ge Ma、Yu Liu
- **期刊 / 年份**：IEEE Transactions on Neural Networks and Learning Systems，2026
- **DOI**:10.1109/TNNLS.2026.3669921
- **PDF**：[NN_2026_FocusFocusFOYFCross.pdf](papers/NN_2026_FocusFocusFOYFCross.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

FOYF 用基于 Swin Transformer 的多重 attention specialization 同时建模目标内部属性、场景级对象关系和跨场景对应，从而提升跨域 few-shot 语义分割对 domain shift 的适应能力。

## 问题与动机

CD-FSS 要求模型只凭少量目标域标注，在未见域分割新类别；源域与目标域的显著分布差异使传统 FSS 性能下降。现有卷积方法偏重局部前景特征，难以捕获场景级上下文、前景—背景关系和长程依赖；单一 attention 也不足以处理复杂跨场景交互，因此需要能兼顾细节、关系和层级上下文的结构。

## 方法

FOYF 是 Siamese meta-learning 网络，包含 self-attention pattern learning module（SAPLM）、guide-attention pattern learning module（GAPLM）、attention-based soft-fusion module（ASFM）和 multiscale attention perception classification module。SAPLM 用 Swin 的层级移位窗口学习 support/query 的自相关模式，GAPLM 以 support 模式引导 query 的跨场景关系，ASFM 以归一化和 skip-attention 融合不同层级，MAP 通过 3、5、7 窗口的多尺度注意力恢复细节并输出像素掩码。

## 实验与结果

模型在 PASCAL VOC 2012（含 SBD augmentation）上训练，在 FSS-1000、Chest X-ray、ISIC2018 和 DeepGlobe 上进行跨域测试；五-shot 评估平均五次，每次通常 200 个 episode，FSS-1000 每次 1000 个。FOYF 平均 mIoU 为 61.91%、平均 FB-IoU 为 69.08%；在 Chest X-ray 上为 68.25% mIoU、77.23% FB-IoU。相较 PFENet/HSNet，Chest X-ray 的 mIoU 提升 31.22/12.64 个百分点，ISIC2018 提升 24.90/9.89，DeepGlobe 提升 11.42/6.57；消融显示 SAPLM、GAPLM、ASFM、DSFP 和 MAP 均有作用。

## 贡献与局限

贡献包括：提出首个完全基于 Transformer 的 CD-FSS 框架；以四类协同 attention specialization 联合学习目标属性、场景关系和层级特征；在多个跨域 benchmark 上取得稳定提升。局限是 patch merging 仍会损失边界细节，医学图像阴影和遥感图像外观差异会造成误分或漏分；复杂/长域差距场景仍明显低于普通数据集，作者将 edge-aware loss、多尺度融合和更强 backbone 留作后续方向。
