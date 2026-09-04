# Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data 总结

## 基本信息

- **标题**: Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data
- **作者**: Kazi F. Akhter, Ibna Kowsar, Manar D. Samad
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109568
- **arXiv**: 2608.28209
- **PDF**: [NN_2026_GeneralizedContext.pdf](papers/NN_2026_GeneralizedContext.pdf)

## 一句话概括

提出广义上下文学习（generalized context learning），去掉表格数据跨域迁移需共享特征的前提，用 Transformer 投影权重实现跨域注意力迁移（CATTLE）。

## 问题与动机

与图像和文本不同，表格数据因特征类型、结构与语义在不同领域间异构，迁移学习困难。现有方法假设数据表间存在共享特征以支持知识迁移，这在实践中不现实；需要不依赖共享特征、数据无关的迁移机制。

## 方法

Transformer 的 key/value/query 投影权重捕获的广义上下文提供基于规则（rule-based）的泛化，而非传统从 Transformer 激活中学到的领域特定上下文；源域的 key 投影权重与目标域的 query 权重交互，实现跨域注意力迁移（Cross-domain Attention Transfer Learning, CATTLE），以数据无关（data-agnostic）方式完成迁移。

## 实验与结果

原文以方法提出为主，具体实验数据原文摘要未提供。

## 贡献与局限

- 贡献一：首次移除表格迁移学习对共享特征的依赖，提出广义上下文学习范式。
- 贡献二：基于投影权重的跨域注意力迁移（CATTLE），数据无关、无需共享特征。
- 局限：具体性能数字原文摘要未提供；更多异构表格域与真实场景验证待展开。

---

DOI: 10.1016/j.neunet.2026.109568
