# Boosting cross-architecture adversarial transferability by enhanced deformation attack 总结

## 基本信息

- **标题**: Boosting cross-architecture adversarial transferability by enhanced deformation attack
- **作者**: Jiachen Wang、Hegui Zhu、Yifan Zhang et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-14
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109637
- **arXiv**: 无
- **PDF**: [NN_2026_BoostingCrossArchitectureAdversarial.pdf](papers/NN_2026_BoostingCrossArchitectureAdversarial.pdf)

## 一句话概括

本文提出 Enhanced Deformation Attack（EDA），在代理模型梯度估计阶段随机施加几何形变与外观扰动，以提升 CNN 生成的对抗样本向 ViT 目标模型的黑盒迁移率。

## 问题与动机

迁移攻击常以 CNN 代理模型生成样本，但攻击跨到视觉 Transformer 时成功率明显下降。现有输入变换虽然增加梯度视图多样性，却未充分改变控制点几何与边界支撑，因而难以缩小 CNN—ViT 的架构鸿沟。

## 方法

EDA 对当前对抗图像采样两类控制点网格：允许边界点移动的全网格和仅取内部点的中心网格。控制点在反射填充画布上位移后用 thin-plate spline 重采样，并辅以高斯噪声或亮度变化；这些变换只参与梯度平均，最终样本仍回到原坐标系并遵守既定的 l∞ 扰动预算。

## 实验与结果

在 ImageNet-Compatible 数据集上，EDA 面向四种 CNN 源模型攻击 ViT 的平均 ASR 均为最高，较对应最强基线分别提高 5.8、11.2、8.7 和 8.0 个百分点。完整 ImageNet、ImageNet-V2、不同预算、目标攻击、五个随机种子及鲁棒模型评测也维持增益；例如 IncRes-v2 到 ViT 的五种子均值为 73.01%，高于 SID 的 65.02%。

## 贡献与局限

- 提出同时扰动控制点布局与边界支撑的梯度估计变换，针对 CNN 到 ViT 的迁移短板。
- 在不扩大最终扰动约束的前提下，以多视图梯度提高攻击稳定性。
- 局限：评测主要覆盖 ImageNet 类分类模型；对实际物理场景、检测任务和未知防御策略的迁移仍需谨慎验证。

---
DOI: 10.1016/j.neunet.2026.109637
