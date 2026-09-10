# VGM-UNet: A hybrid visual graph deformable mamba with fourier neural operator U-Net for medical image segmentation 总结
## 基本信息
- **标题**: VGM-UNet: A hybrid visual graph deformable mamba with fourier neural operator U-Net for medical image segmentation
- **作者**: Hang Li, Jianan Fan, Weidong Cai
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108890
- **PDF**: [NN_2026_VGMUNet.pdf](papers/NN_2026_VGMUNet.pdf)
## 一句话概括
VGM-UNet把视觉图结构、可变形注意、Mamba-2和Fourier神经算子融入U形网络，增强医学图像分割表达。
## 问题与动机
医学图像目标尺度、形状和边界变化明显，传统U-Net难以同时建模长程依赖与细粒度结构，需要兼顾精度和复杂度。
## 方法
作者以二维状态空间模型和八向扫描构建Vision Mamba-2骨干，并建立层次视觉图结构；FFT前馈模块补充通道建模，图网络、可变形注意和U形跳连共同完成分割。
## 实验与结果
在Synapse和ACDC基准上，VGM-UNet分割精度优于对比的最新方法；摘要未给出统一可复述指标。
## 贡献与局限
贡献是组合图结构、状态空间建模和Fourier算子。局限是多模块带来实现和调参负担，跨器官泛化与计算开销仍需评估。
---
DOI: 10.1016/j.neunet.2026.108890
