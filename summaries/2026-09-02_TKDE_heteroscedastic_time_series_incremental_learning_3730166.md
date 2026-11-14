# HADA: Heteroscedastic-Aware Analytical Dynamic Adaptation for Time Series Class-Incremental Learning 总结

## 基本信息
- **标题**: HADA: Heteroscedastic-Aware Analytical Dynamic Adaptation for Time Series Class-Incremental Learning
- **作者**: Han Liu、Fengbin Zhang、Sizhe Huang 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8237-8249
- **发表**: 2026-09-02
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3730166

## 一句话概括
时间序列类别增量学习需不断吸收新类别而不遗忘旧类。论文将遗忘归因于新任务梯度干扰、特征异方差及表示漂移，提出 HADA：预训练阶段稳定时序表示，增量阶段冻结编码器并解析更新分类器。

## 问题与动机
不保存旧样本时，能否利用特征方差差异和无梯度更新减轻连续学习中的灾难性遗忘？

## 方法
以层级扰动一致性正则化预训练编码器；每来一个任务，估计特征统计量并降低不稳定维度权重，再用递归闭式岭回归更新分类头。

## 实验与结果
作者在多个时间序列增量基准上报告准确率、稳定性和耗时；五个数据集上的运行时间比较显示 HADA 比回放类方法更快，且总体准确率优于若干无样本回放基线（PDF 第 8 页）。但过强扰动会使复杂数据集性能下降，且冻结编码器依赖首任务数据质量；UWave 边界实验专门显示这种依赖（PDF 第 10–11 页）。

## 贡献与局限
将异方差感知加权与冻结表示后的递归解析更新结合，减少梯度冲突及存储旧样本的需要。性能受首任务代表性和扰动强度制约，证据来自有限基准，不能直接外推到任意流式分布漂移。

---
DOI: 10.1109/tkde.2026.3730166
