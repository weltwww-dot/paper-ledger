# PerC-SimAM-BLSTM: Position Perception Circular Convolution With Simple Attention Mechanism Based on BLSTM for Bundle Branch Block Detection

## 基本信息

- **标题**: PerC-SimAM-BLSTM: Position Perception Circular Convolution With Simple Attention Mechanism Based on BLSTM for Bundle Branch Block Detection
- **作者**：Jibin Wang、Bo Shi
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3665367
- **arXiv**：无
- **PDF**：[NN_2026_PerCSimAMBLSTMPosition.pdf](papers/NN_2026_PerCSimAMBLSTMPosition.pdf)

## 一句话概括

本文提出 PerC-SimAM-BLSTM 心电分类模块，把具有全局感受野的位置感知循环卷积与三维能量注意力双向长短期记忆结合，用于轻量而准确地区分左、右束支传导阻滞和正常心律。

## 问题与动机

左束支传导阻滞和右束支传导阻滞在心电图上的形态相近，单纯依靠人工目测或固定局部卷积窗口容易漏检；而 Transformer 类模型虽然能捕获长程关系，却可能带来较高的时间和空间开销。论文希望在保留全局依赖建模能力的同时，增强对心电局部结构和位置差异的感知，并降低模型面向移动或边缘设备部署时的复杂度。

## 方法

PerC 模块沿垂直和水平方向分别执行循环卷积，将输入维度视为首尾相接的环形缓冲区，并通过双线性插值生成可学习的位置嵌入，使每个位置能够获得全局且具有位置区分能力的特征。SimAM-BLSTM 先用双向 LSTM 建模时序，再根据神经元能量函数计算三维重要性权重，对前向和后向隐藏状态进行重标定。作者将该模块嵌入 ResNet50，形成 PSB-ResNet50；心电信号先下采样到 250 Hz、切分为 2 秒片段，经小波滤波和 Z-score 标准化后完成三分类，并使用 Adam 优化交叉熵损失。

## 实验与结果

实验使用 CPSCDB 和 MIT-BIH 心律失常数据库，分别包含 22,770 和 15,299 个涉及正常心律、左束支和右束支传导阻滞的心电片段。PSB-ResNet50 在 CPSCDB 上对正常心律和左束支样本的准确识别率分别达到 99.1% 和 98.9%，右束支样本误分率约为 1.0%；在 MADB 上对应正常心律、左束支识别率为 98.7% 和 98.8%，右束支误分率约为 1.3%。相较替换模块的 MLP-Mixer、ViT、Swin Transformer 和单向 LSTM 版本，整体指标提高约 0.1–0.7%，并在 CPSCDB 上约 22–23 个 epoch、MADB 上约 20–21 个 epoch 收敛。与 CNN-Transformer 结构相比，时间复杂度和空间复杂度分别降低 43.5% 和 36.8%。

## 贡献与局限

论文以循环卷积补足全局—局部心电特征提取，以 SimAM-BLSTM 提供更细粒度的时空通道重标定，并通过理论分析和跨数据库实验验证了收敛性、精度与复杂度之间的平衡。局限在于验证类别主要限于左束支、右束支和正常心律，尚未覆盖房颤、室速等更多临床心律失常；数据集也较为规整，现实中的运动伪影、电极噪声和基线漂移可能降低表现。此外，模型的临床可解释性仍不足，后续需要扩展真实动态心电数据并提供可视化诊断依据。

---
DOI: 10.1109/tnnls.2026.3665367
