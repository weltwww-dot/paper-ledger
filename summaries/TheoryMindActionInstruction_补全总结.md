# Theory of Mind in Action: The Instruction Inference Task in Dynamic Human-Agent Collaboration 总结

## 基本信息
- **标题**: Theory of Mind in Action: The Instruction Inference Task in Dynamic Human-Agent Collaboration
- **作者**: Fardin Saada, Pradeep K. Murukannaiah, Munindar P. Singh
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104621
- **PDF**: [AIJ_2026_TheoryMindActionInstruction.pdf](papers/AIJ_2026_TheoryMindActionInstruction.pdf)

## 一句话概括
论文提出 Instruction Inference 任务和 Tomcat agent，测试 LLM 在动态协作环境中依据上下文推断含糊指令背后意图并行动的能力。

## 问题与动机
真实协作指令常不完整或有歧义，传统 agent 容易按字面执行。既有 ToM 评测多为静态问答，不能检验心智推理是否能支持连续目标导向协作。

## 方法
作者设计包含 20 个场景的 Instruction Inference，在 Doors, Keys, and Gems 环境中让 agent 协助 principal 获取目标。Tomcat 有 Fs-CoT 和 Commonsense Prompt 两种变体，并部署于 GPT-4o、DeepSeek-R1、Gemma-3-27B。

## 实验与结果
52 名人类参与者在与 CP 相同的信息条件下参与研究，以意图准确率、行动最优性和规划最优性比较模型。Fs-CoT，尤其在 GPT-4o 与 DeepSeek-R1 上，表现可与人类参与者相当。

## 贡献与局限
贡献是将 ToM 评测推进到动态人机协作的指令理解与行动选择。局限是环境为离散网格、主要考察一阶意图，结果不能直接外推到开放世界或高阶博弈。

---
DOI: 10.1016/j.artint.2026.104621
