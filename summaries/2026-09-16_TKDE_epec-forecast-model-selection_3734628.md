# Beyond Side-by-Side Comparison: A Unified Evaluation Framework for Model Selection in Time Series Forecasting 总结

## 基本信息
- **标题**: Beyond Side-by-Side Comparison: A Unified Evaluation Framework for Model Selection in Time Series Forecasting
- **作者**: Ruoping Yang、Zhongliang Guan、Xiang Xie
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8009-8023
- **发表**: 2026-09-16
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3734628

## 一句话概括
EPEC把预测误差与训练时间整合为可解释排序分数，为时间序列预测模型提供统一筛选依据，回应只并列报告精度和效率时难以权衡的问题。

## 问题与动机
模型可能精度高但训练慢，或速度快但误差较大；并列指标缺少明确取舍规则，也使模型选择难复现。

## 方法
框架先按各任务最优误差计算相对精度损失，再用指数权重映射，并按平均权重与训练时间形成分数；论文分析其尺度不变性、Pareto 一致性，并比较不同参数和决策规则。

## 实验与结果
在交通、能源、金融、气象和公共健康五个领域、十个模型及多个预测任务上评估，结果显示 EPEC 排序与 TOPSIS 和实用决策规则较一致；五个数据集层级的 Friedman 检验仍显著，多随机种子与任务抽样下排名总体稳定（PDF 第 8 页）。

## 贡献与局限
EPEC提供训练阶段的精度—效率筛选框架。实验使用单台笔记本，作者指出硬件差异会影响训练时长与效率判断；权重参数及任务基准选择也会影响排序，实际部署仍需按场景校准。

---
DOI: 10.1109/tkde.2026.3734628
