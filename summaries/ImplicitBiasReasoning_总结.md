# Implicit-bias-like patterns in reasoning models 总结

## 基本信息

- **标题**: Implicit-bias-like patterns in reasoning models
- **作者**: Messi H. J. Lee, Calvin K. Lai 等 (et al.)
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01300-1
- **arXiv**: 2503.11572
- **PDF**: [NMI_2026_ImplicitBias.pdf](papers/NMI_2026_ImplicitBias.pdf)

## 一句话概括

提出推理模型内隐关联测验（RM-IAT）研究推理模型中的类隐式偏见处理：通过逐步推理完成任务的模型对「与刻板印象不一致」的关联任务消耗显著更多的推理 token，表明其存在类隐式偏见模式。

## 问题与动机

隐式偏见指影响知觉、判断与行为的自动心理过程。此前对 LLM「隐式偏见」的研究大多聚焦输出而非产生输出的过程；推理模型用逐步推理解决复杂任务，其内部处理是否呈现类隐式偏见模式尚不清楚。

## 方法

设计 RM-IAT（Reasoning Model Implicit Association Test）：对比模型在关联相容（association-compatible）与关联不相容任务上的推理 token 消耗，量化处理反刻板印象信息时的计算努力；并配合主题分析考察模型内部关于偏见与刻板印象的推理内容。

## 实验与结果

o3-mini、DeepSeek-R1、gpt-oss-20b 与 Qwen-3 8B 等推理模型在不相容任务上一致消耗更多推理 token，提示处理反刻板印象信息需要更大计算努力；Claude 3.7 Sonnet 呈现反转模式，其主题分析与对偏见/刻板印象的独特内部推理关注相关（论文未报告具体数值指标）。

## 贡献与局限

- 贡献一：首个关注推理模型内部处理过程的隐式偏见测试范式（RM-IAT），而非仅输出层。
- 贡献二：跨多个推理模型发现一致的类隐式偏见模式，并揭示模型间因内部推理内容而显著不同。
- 局限：论文未报告具体数值指标；token 消耗作为偏见代理的效度与更广模型覆盖待后续研究。

---

DOI: 10.1038/s42256-026-01300-1
