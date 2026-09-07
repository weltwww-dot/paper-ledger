# Lightweight attention-aware fusion network based on state-space model for V-D-T salient object detection 总结

## 基本信息

- **标题**: Lightweight attention-aware fusion network based on state-space model for V-D-T salient object detection
- **作者**: Anzhi Wang, Jintao Wu, Yun Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-08-31
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109578
- **arXiv**: 无
- **PDF**: [NN_2026_LightweightAttentionFusion.pdf](papers/NN_2026_LightweightAttentionFusion.pdf)

## 一句话概括

针对可见光-深度-热红外三模态显著目标检测，本文提出基于状态空间模型的轻量级注意力感知融合网络 LAANet，以远小于 SOTA 的 6.78M 参数与 5.23G FLOPs 取得接近最优的精度。

## 问题与动机

可见光-深度-热红外（V-D-T）三模态显著目标检测（SOD）通过融合三种模态提升复杂场景下的泛化能力，但多数现有方法依赖复杂网络结构，计算开销大，难以部署到边缘设备；同时，盲目融合三模态特征容易引入噪声，导致性能下降。作者提出两个挑战：一是如何设计在精度与效率间取得平衡、具备实时性的轻量 V-D-T SOD 架构；二是如何从三模态特征中提取有效信息并发挥多模态协同潜力。此外，现有 Mamba/SSM 类 SOD 方法大多只做单模态建模，未显式处理跨模态交互。

## 方法

本文提出轻量级注意力感知融合网络 LAANet，采用 MobileNetV2-B0 作为主干分别提取 RGB、深度、热红外特征，以 RGB 为主分支分别与深度、热红外配对融合后再做三模态聚合。针对浅层高分辨率特征，设计了基于 SSM 的 Cross Mamba Fusion Module（CMFM），受交叉注意力启发，通过提出的 Cross 2D Select Scan（CSS2D，交换 SS2D 的观测矩阵 C）以线性复杂度实现模态间注意感知；针对 SSM 固有的"遗忘记忆"缺陷，对低分辨率深层特征使用基于自注意力的 Attention Perception Fusion Module（APFM）挖掘完整语义关系。此外设计了仅 0.37M 参数的轻量解码器 LDB（由不同膨胀率的深度可分离卷积 DSConv 与线性操作构成，膨胀率 1/3/5/9），并结合边缘感知模块 EAM 与多级监督（wIoU+wBCE 混合损失加边缘 BCE）细化预测。

## 实验与结果

在 VDT2048 数据集（1048 训练、1000 测试图）上与 15 种 SOTA 方法（含 6 种 RGB-D、5 种 RGB-T、4 种 V-D-T 方法）对比，采用 Sα、MAE、Em、wFm、meanFm 五个指标。LAANet 在 384×384 输入下达到 Sα 0.8842、MAE 0.0029、Em 0.9630、wFm 0.8683、meanFm 0.8278，同时参数量仅 6.78M、FLOPs 5.23G、模型 33.8MB、推理 23.70 FPS；相对最优常规方法 QASFNet，FLOPs 降低约 53 倍、速度提升约 2 倍以上（FPS、模型大小、参数量、复杂度分别改善 89.60%、94.61%、95.92%、98.13%），相对最优轻量方法 MFDF 在 Sα/MAE/Em/wFm/meanFm 上分别提升 0.52%/6.4%/0.49%/0.45%/1.94%。消融显示融合模块仅增 1.08M 参数与 1.69G FLOPs 即带来显著增益（去掉后 Sα、wFm 下降 2.92%、5.69%），LDB 增 0.37M 参数使 Em、wFm 提升 6.44%、8.47%，CMFM 用于第 1-2 层、APFM 用于第 3-5 层的配置精度-效率综合最优。

## 贡献与局限

贡献：首次将 SSM 扩展到跨模态交互并以尺度自适应方式与自注意力结合，提出轻量融合网络 LAANet；设计了以线性复杂度实现注意力式模态感知的 CMFM 与补偿 SSM 遗忘性的 APFM；提出仅 0.37M 参数的轻量解码器 LDB；实验证明 LAANet 精度接近 SOTA 且在轻量多模态方法中性能与效率全面占优。局限：轻量主干对高分辨率细节提取能力有限；对低质量模态采用均衡融合策略、未按质量动态调整权重；VDT2048 数据规模小且场景单一（仅约 7 类家庭场景），制约复杂场景泛化。未来计划构建万级 RGB-D-T 数据集、建立基于清晰度/信噪比的质量评估与动态权重机制、设计动态分辨率自适应机制。

---
DOI: 10.1016/j.neunet.2026.109578
