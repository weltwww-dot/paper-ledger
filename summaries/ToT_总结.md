# Tree of Thoughts 总结

## 基本信息

- **标题**: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- **研究方向**: 人工智能
- **作者**: Shunyu Yao, Dian Yu, Jeffrey Zhao 等 7 人 (et al.)
- **期刊 / 会议**: NeurIPS 2023
- **arXiv**: 2305.10601（DOI: 10.48550/arXiv.2305.10601）
- **PDF**: [NeurIPS_2023_ToT.pdf](papers/NeurIPS_2023_ToT.pdf)

## 一句话概括

提出 Tree of Thoughts (ToT) 推理框架，让大语言模型在推理时显式探索多条思维路径、对部分解自我评估，并在必要时前瞻或回溯，把 Chain-of-Thought 推广为树状搜索式推理。

## 问题与动机

语言模型推理被限制在 token 级、从左到右的逐字生成，遇到需要探索、策略性前瞻或初始决策起关键作用的任务时容易局部最优而失败。Chain-of-Thought 只沿单一路径生成，缺少备选路径、自我评估与回溯机制，无法应对需要全局规划的复杂问题。

## 方法

以「思维」(thoughts)——连贯的文本单元——作为中间步骤构建搜索树：模型先生成多条候选思维，再用 self-evaluation 为部分解打分，依据分数决定继续、前瞻或回溯。该方法把推理从「单路径采样」变成「带评估的树搜索」，在 Game of 24、Creative Writing、Mini Crosswords 三个需要非平凡规划或搜索的新任务上评测。

## 实验与结果

在三个任务上 ToT 显著提升了大语言模型的解题能力。以 Game of 24 为例：GPT-4 配合 chain-of-thought prompting 只解出 4% 的任务，ToT 达到 74% 的成功率（数字来自原文摘要）。Creative Writing 与 Mini Crosswords 的详细指标原文摘要未提供。

## 贡献与局限

- 贡献一：提出 ToT 框架，首次把「探索 + 自我评估 + 前瞻/回溯」的树搜索机制系统性地用于语言模型推理。
- 贡献二：ToT 通用化 Chain-of-Thought，证明了在复杂规划类任务上「想得多」比「想得快」更有效。
- 局限：推理代价高于单路径采样（需要多次生成与评估）；评测集中在三个人工设计的任务，广泛性与成本分析原文未提供。

---

DOI: 10.48550/arXiv.2305.10601
