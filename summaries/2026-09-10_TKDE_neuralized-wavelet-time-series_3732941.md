# Neuralized Multi-Wavelet Decomposition for Time Series Classification and Forecasting 总结

## 基本信息
- **标题**: Neuralized Multi-Wavelet Decomposition for Time Series Classification and Forecasting
- **作者**: Xiaohan Jiang、Jingyuan Wang、Jiahao Ji 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(11)，7638-7654
- **发表**: 2026-09-10
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3732941

## 一句话概括
本文提出神经化多小波分解框架，将可学习的频率分解与下游时序分类、预测结合，针对固定分解难以适应数据差异的问题提升表示能力。

## 问题与动机
传统时频分解依赖预设变换，面对异质序列时适配有限；作者探讨如何让分解过程随数据学习，同时兼顾分类与预测。

## 方法
模型以神经化多小波卷积网络为基础，构造分类模型 TFBC 与预测模型 FTB，并采用可学习分解及频率对比预训练；消融结果显示各组成均有贡献。

## 实验与结果
TFBC 在 64 个 UCR 数据集上平均分类表现较对照提升 19.97%；FTB 在七个公开预测集上 MSE 平均降低 24.45%、MAE 降低 15.38%，训练每轮约 63.76 秒（PDF 第 14 页）。

## 贡献与局限
工作把可学习多小波分解用于两类时序任务，并在多基准上报告较强结果。局限是分类仅选取 64 个代表数据集（虽补充材料报告 128 集结果），预测评估为七个公开集，跨域部署和计算成本仍需进一步检验。

---
DOI: 10.1109/tkde.2026.3732941
