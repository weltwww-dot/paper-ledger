# Refining Bayesian neural networks via Stein variational gradient descent for uncertainty-aware cardiac registration 总结

## 基本信息
- **标题**: Refining Bayesian neural networks via Stein variational gradient descent for uncertainty-aware cardiac registration
- **作者**: Zefeng He、Yong Hua、Xuan Yang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109450
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109450

## 一句话概括
BVAE针对心脏配准的不确定性估计，以可学习先验和SVGD细化权重后验，在多数据集部分指标改善，但提升随数据集和指标变化。

## 问题与动机
如何在心脏配准中表达模型不确定性并改善权重后验？

## 方法
贝叶斯变分自编码器估计形变及权重不确定性，学习先验，再以形变感知似然驱动SVGD细化，并评估CNN/Mamba骨干。

## 实验与结果
在ACDC、YORK、MICCAI、M&Ms测Dice、边界误差、Hausdorff及Jacobian；MambaGI在ACDC的SVGD-C Dice为0.8186，基线0.8154，其他数据集和层表现不一（PDF第8–10页）。

## 贡献与局限
把贝叶斯估计和SVGD用于心脏配准；增益依场景且计算成本增加。

---
DOI: 10.1016/j.neunet.2026.109450
