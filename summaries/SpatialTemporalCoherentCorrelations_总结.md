# Learning Spatial-Temporal Coherent Correlations for Speech-Preserving Facial Expression Manipulation 总结

## 基本信息

- **标题**：Learning Spatial-Temporal Coherent Correlations for Speech-Preserving Facial Expression Manipulation
- **作者**：Tianshui Chen, Jianman Lin, Zhijing Yang, Chunmei Qing, Guangrun Wang, Liang Lin
- **期刊 / 年份**：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **研究方向**：计算机视觉与情感人脸视频生成
- **DOI**:10.1109/TPAMI.2026.3687518
- **PDF**：[TPAMI_2026_SpatialTemporalCoherentCorrelations.pdf](papers/TPAMI_2026_SpatialTemporalCoherentCorrelations.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文发现同一说话者在表达相同语音内容但情绪不同的情况下，局部面部动画在空间和时间上仍具有高度相关性，并提出 STCCL 将这种相关性作为可插拔监督，以提升表情操控的情绪表达和口型—语音保持能力。

## 问题与动机

Speech-Preserving Facial Expression Manipulation（SPFEM）要改变面部情绪，同时严格保留与语音内容对应的口部运动。现有方法依赖难以获得的同一人物、同一内容、不同情绪的配对样本，或使用全局循环一致性/隐式解耦，容易在大幅表情变形时破坏细粒度口型同步；扩散模型的随机去噪也会增加精确口型控制的困难。作者通过对应与非对应局部区域的统计比较发现，保持语音内容时对应区域的空间、跨帧时间相关性明显更强，可作为伪配对监督信号。

## 方法

STCCL 先用 ArcFace 的四个卷积层提取多尺度特征，并以 visual disparity 或 correlation matrix 两种方式表示局部相关性；通过带温度系数 0.07 的对比学习，分别预训练 Spatial Coherent Correlation（SCC）和 Temporal Coherent Correlation（TCC）度量。训练 SPFEM 时，将输入与生成输出的对应局部区域及相邻帧相关性加入辅助损失，使空间结构和运动轨迹保持一致。相关性感知自适应策略 CAAS 对更难学习的区域赋予更高权重，默认 λ 与 r 均为 2。该损失可接入中间 3DMM 表示或最终渲染图像，并应用于 ICface、NED、EAT 和 DICE-Talk 等不同生成架构。

## 实验与结果

在 MEAD 上用 36 位说话者的 7,560 个视频训练 STCCL，用 6 位未重叠说话者的 1,260 个视频评估；另在未重新训练的 RAVDESS（6 位演员、168 个视频）上测试，指标为 FAD、CSIM 和 LSE-D，并分别报告 Intra-ID 与 Cross-ID。MEAD Cross-ID 中，加入 visual-disparity STCCL 的 NED 将 FAD 从 4.448 降至 4.169、LSE-D 从 9.906 降至 9.216；EAT 的 LSE-D 从 10.023 降至 9.381，DICE-Talk 的 FAD/LSE-D 从 2.666/9.082 降至 2.470/8.872。25 人、140 个视频的用户研究中，STCCL 相比 NED 基线的真实感、情绪相似度和口型相似度平均评分分别提高 40%、38% 和 46%。

## 贡献与局限

贡献包括：揭示并显式学习跨情绪的空间—时间局部相关性；提出可适配不同区域难度的 CAAS；比较 visual disparity 与 correlation matrix 两种互补建模方式；证明 STCCL 能以架构无关的辅助监督提升 GAN/Transformer/扩散式生成器，并可跨数据域泛化。局限是方法优先保证语音驱动结构，对极端情绪强度或复杂跨身份迁移中的显式情绪语义约束不足，效果还受骨干生成模型能力与域偏差限制；作者计划加入情绪感知相关性。
