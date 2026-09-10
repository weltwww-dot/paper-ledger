# Enhancing knowledge tracing with multi-level individualized perception and teacher-student semantic distillation 总结

## 基本信息

- **标题**: Enhancing knowledge tracing with multi-level individualized perception and teacher-student semantic distillation
- **作者**: Zhenqiang Yu、Luyao Huang、Xingbing Li、Yuncheng Jiang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109576
- **arXiv**: 无
- **PDF**: [NN_2026_IndividualizedKnowledgeTracing.pdf](papers/NN_2026_IndividualizedKnowledgeTracing.pdf)

## 一句话概括

本文用多层个性化感知和教师–学生语义蒸馏改善知识追踪中的动态状态建模。

## 问题与动机

知识追踪需要根据学习交互模拟学生知识状态并预测未来表现。现有序列模型常忽略不同学生对同一问题的差异，轻量模型的语义建模能力也有限。研究希望同时建模个体差异、问题–知识关系和记忆衰减。

## 方法

模型包含个性化问题理解、个性化问题–知识关联和个性化知识状态遗忘三个模块。前两者分别捕捉学生理解差异与问题和知识概念的关系，遗忘模块模拟记忆衰减。作者以 LLM 为教师，把语义能力通过知识蒸馏迁移到 LSTM 学生模型。

## 实验与结果

作者在两个基准数据集上实验。结果显示，所提方法持续改善预测性能，说明个性化模块和语义蒸馏有助于动态知识状态建模；摘要未给出数据集名称和具体增益数字，故不补写。

## 贡献与局限

贡献是把个性化感知与 LLM–LSTM 语义蒸馏结合到知识追踪。局限是教师模型带来的训练成本和潜在偏差，以及不同教育平台、题型和学生群体上的泛化仍需验证。

---
DOI: 10.1016/j.neunet.2026.109576
