# FUGEA: Fused unified gradient ensemble for cross-architecture transferable attacks 总结

## 基本信息

- **标题**: FUGEA: Fused unified gradient ensemble for cross-architecture transferable attacks
- **作者**: Guangliang Huang、Feng Ye、Tianqiang Huang、Chenhao Lu、Runze Chen、Quan Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108926
- **arXiv**: 无
- **PDF**: [NN_2026_Paper.pdf](papers/NN_2026_FUGEA_FusedUnifiedGradientEnsemble.pdf)

## 一句话概括

FUGEA 用两阶段梯度集成提高对抗样本跨 CNN 与 ViT 的迁移攻击成功率。

## 问题与动机

黑盒攻击依赖对抗样本的迁移性，但在 CNN 与 Vision Transformer 等不同架构之间迁移时，攻击成功率常明显下降。已有集成攻击还存在固定权重、梯度方向不稳定和缺少细粒度优化等问题。研究目标是同时改善攻击成功率、跨架构迁移性和面对防御方法时的稳健性。

## 方法

FUGEA 将扰动优化拆成 Rapid Convergence Engine（RCE）和 Precision Refinement Gradient（PRG）两个阶段。RCE 用 Uncertainty Weight 动态分配不同代理模型的梯度权重，并用 Gradient Agreement Mapping 过滤方向冲突。PRG 通过 Sampled Neighbor Predictive Gradient 对当前样本邻域采样并预测下一步梯度，进行细粒度扰动优化。

## 实验与结果

作者在 CNN 和 ViT 架构间开展迁移攻击实验，并与现有方法比较攻击成功率和迁移性。全文报告 FUGEA 在两类架构上持续优于基线，并对先进对抗防御保持较强攻击效果；文中图示的集成模型包括 ResNet18、Inception_v3、BiT-M-R50×1 和 Inception_v4。

## 贡献与局限

贡献是提出 RCE–PRG 两阶段框架，并将动态权重、方向稳定和邻域预测组合到跨架构攻击中。局限是结论主要来自图像分类代理模型与设定的扰动约束，真实系统中的物理攻击成本、迁移到更多任务的表现仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.108926

