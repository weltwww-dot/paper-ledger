# Handling Learnwares From Heterogeneous Feature and Label Spaces With Explicit Label Exploitation 总结

## 基本信息
- **标题**: Handling Learnwares From Heterogeneous Feature and Label Spaces With Explicit Label Exploitation
- **作者**: Peng Tan、Zhi-Hao Tan、Hai-Tian Liu 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15312-15329
- **发表**: 2026-08-12
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3723272

## 一句话概括
本文扩展 learnware 规格以显式编码模型输出，并用统一子空间中的条件分布匹配，从异构特征或标签空间中检索可复用模型。

## 问题与动机
模型仓库中的候选模型往往与用户任务具有不同的输入特征，甚至标签空间也不同；仅比较特征边际分布难以识别模型是否适合目标任务，而直接获取开发者原始数据又不利于隐私保护。

## 方法
方法将模型输出及其伪标签信息写入 learnware 规格，通过共享子空间对齐异构任务，并使用 MMD 比较边际与标签条件分布，以保留预测行为信息。系统据此选择候选模型，并可将其与用户侧模型动态集成；规格匹配不要求取得开发者原始训练数据。

## 实验与结果
作者在合成任务及真实表格任务上比较异构特征、异构特征与标签的组合情形，并纳入 PFS 销售预测和 MIMIC-III。结果显示，所提方法在多数分类与回归任务上优于从头训练、特征对齐和预训练表格模型等比较方法；在同时异构特征与标签的设置中，实验涵盖多类用户任务，所提方法在各情形均取得最高表现（PDF 第12页、13页、16页）。

## 贡献与局限
论文将模型输出的条件分布纳入 learnware 规格，使模型复用可以跨越特征和标签空间差异，并在低标注用户任务中提供推荐与集成。结果依赖共享子空间和可用用户标注；作者也指出仅靠子空间系统预测器会因映射信息损失而受限（PDF 第15页），因此并非无需适配即可普遍迁移。

---
DOI: 10.1109/tpami.2026.3723272
