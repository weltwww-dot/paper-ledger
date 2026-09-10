# Learned Optimal Visual Time-of-Flight Imaging With Fisher Information Guidance 总结

## 基本信息

- **标题**: Learned Optimal Visual Time-of-Flight Imaging With Fisher Information Guidance
- **作者**: Kanghui Wang, Jiaqu Li, Zhangnan Li, Kai Wang, Xiangshun Kong, Feng Yan, Tao Yue, Xuemei Hu
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-04-29
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3688946
- **arXiv**: 无
- **PDF**: [TPAMI_2026_LearnedOptimalVisualTime.pdf](papers/TPAMI_2026_LearnedOptimalVisualTime.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出由 RGB 视觉信息辅助的 learned visual ToF 成像方案，以 Fisher information 指导 iToF 编码函数和深度重建网络的端到端优化，改善低信噪比条件下的深度精度和边缘细节。

## 问题与动机

iToF 通过调制—解调相关测量编码光程延迟，但强环境光会降低 SNR，导致信号衰减、相位误差和深度边界伪影。传统 sinusoidal、square-wave 或固定 Hamilton coding 难以适应低 SNR 场景；单纯后处理也没有同时优化测量编码和重建过程，因此需要把物理可实现的编码设计与视觉先验联合起来。

## 方法

作者建立可微 iToF 物理模型，用受带宽、能量、非负性和解调幅度约束的谐波调制/解调函数模拟成像过程，并最大化关于深度的 Fisher information。重建端采用双分支结构：iToF 分支包含多尺度 Spatial-Structure Extraction Branch 和 Pixel-wise Depth Regression Branch，RGB 分支通过 DACMM、Hierarchical Edge Gating Module 与 iToF 特征融合，再由 TEM 提取深度不连续边缘并进行残差增强。整体损失联合深度 fidelity、Fisher guidance、多测量差异和 hybrid edge guidance。

## 实验与结果

训练使用 NYU-V2 的 1,449 对 RGB-D 图像，其中 1,000 对训练、449 对测试；另在 SUN RGB-D 选 200 对、4D Light Field 选 14 对验证泛化。模拟噪声覆盖 22、19 和 16 dB，评价 MAE、RMSE、Abs. Rel 和 Sq. Rel；方法在 NYU-V2 的不同噪声水平下均取得最低 MAE，并相对 Base 方法降低 3–8 mm MAE。低 SNR 下去除 DACMM 会使 MAE 和 RMSE 分别增加 17.65 mm 和 18.76 mm；用标准 transformer 注意力替代 DACMM 时，MAE 和 Abs. Rel 分别高出 28.3% 和 15.1%。

## 贡献与局限

论文把 Fisher-information-guided coding、RGB 边缘先验和双分支 iToF 重建统一为端到端 visual ToF 框架，实验证明视觉信息能提高编码函数收敛和深度边界恢复。当前工作主要聚焦噪声鲁棒的深度重建，尚未解决 multipath interference、遮挡和远距离阵列 ToF 传感等问题；这些场景以及更广泛的计算成像应用是后续方向。

---
DOI: 10.1109/tpami.2026.3688946
