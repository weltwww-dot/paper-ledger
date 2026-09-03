# Plan of Knowledge 总结

## 基本信息

- **标题**: Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering
- **作者**: Ying Zhang, Xinying Qian, Yu Zhao, Baohang Zhou
- **期刊 / 会议**: IEEE TKDE 2026
- **发表**: 2026-08-14
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3718295
- **arXiv**: 2511.04072
- **PDF**: [TKDE_2026_PlanOfKnowledge.pdf](papers/TKDE_2026_PlanOfKnowledge.pdf)

## 一句话概括

提出 Plan of Knowledge (PoK)：把复杂时序问题分解为子目标序列并配合对比时序检索器，提升 LLM 在时间知识图谱问答（TKGQA）中的时序推理准确性与可解释性。

## 问题与动机

TKGQA 需利用时间知识图谱回答对时间敏感的问题。已有方法用预训练 TKG 嵌入或图神经网络注入时序知识，但难以理解时间约束的复杂语义；LLM 语义理解强但时序推理弱，且存在幻觉与知识缺失。

## 方法

PoK 框架：Plan of Knowledge 模块把复杂时序问题按预定义工具分解为子目标序列，作为推理探索的中间指引；并行构建带对比检索框架的时间知识库（TKS），让模型选择性检索语义与时间对齐的事实；结构化规划 + 时序知识检索结合，增强可解释性与事实一致性。

## 实验与结果

在四个 TKGQA 基准数据集上实验：显著提升检索精度与推理准确率，最高超过现有 SOTA 方法 56.0%（数字来自原文摘要）。

## 贡献与局限

- 贡献一：面向 TKGQA 的「规划 + 对比时序检索」框架，缓解 LLM 时序推理的幻觉与知识缺失。
- 贡献二：时间知识库（TKS）对比检索与子目标分解结合，四个基准上大幅领先 SOTA。
- 局限：评测集中于 TKGQA 基准；更复杂开放域时序问答的泛化待验证。

---

DOI: 10.1109/tkde.2026.3718295
