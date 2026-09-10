# Unsupervised Motion Artifact Purification Guided by Joint Prior from Pixel and K-space Domains 总结

## 基本信息

- **标题**: Unsupervised Motion Artifact Purification Guided by Joint Prior from Pixel and K-space Domains
- **作者**: Jiahua Xu、Dawei Zhou、Lei Hu、Jianfeng Guo、Feng Yang、Zaiyi Liu、Nannan Wang、Xinbo Gao
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109573
- **arXiv**: 无
- **PDF**: [NN_2026_Paper15.pdf](papers/NN_2026_MotionArtifactPurification.pdf)

## 一句话概括

本文利用 MRI 图像的像素域与 k-space 频域联合先验，引导预训练扩散模型无监督去除运动伪影。

## 问题与动机

MRI 运动伪影会干扰临床诊断，现有方法多依赖成对的干净/伪影数据。运动扰动在 k-space 中的高频部分尤其值得利用，但现有研究关注不足。研究希望在没有配对数据的情况下恢复组织纹理和形状。

## 方法

方法用 noisy MRI 的 k-space 信息引导预训练扩散模型。低频成分提供组织纹理恢复线索，高频和像素域信息则用于细化形状与纹理。作者设计交替互补掩膜破坏伪影结构，并提出 prior meanbook 作为稳定去噪参考。

## 实验与结果

作者在来自不同身体部位的三个数据集上评估。结果显示，所提方法在多个定量指标和定性临床评估中优于对比方法；摘要未给出具体指标表数值，故不补写。

## 贡献与局限

贡献是将像素域、k-space 域和扩散先验结合到无监督伪影净化中。局限是方法依赖预训练扩散模型与伪影频域假设，极端运动、不同扫描协议和临床诊断收益仍需更大规模验证。

---
DOI: 10.1016/j.neunet.2026.109573

