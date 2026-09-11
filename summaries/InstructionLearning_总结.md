# Instruction Learning Paradigms: A Dual Perspective on White-Box and Black-Box LLMs 总结

## 基本信息

- 标题: Instruction Learning Paradigms: A Dual Perspective on White-Box and Black-Box LLMs
- 作者: Yanwei Ren、Liu Liu、Baosheng Yu et al.
- 期刊 / 会议: Machine Learning 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1007/s10994-026-07137-4
- PDF: [ML_2026_InstructionLearning.pdf](papers/ML_2026_InstructionLearning.pdf)

- 标题: Instruction Learning Paradigms: A Dual Perspective on White-Box and Black-Box LLMs
- 作者: Yanwei Ren、Liu Liu、Baosheng Yu et al.
- 期刊 / 会议: Machine Learning 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**: Instruction Learning Paradigms: A Dual Perspective on White-Box and Black-Box LLMs
- **作者**: Yanwei Ren、Liu Liu、Baosheng Yu et al.
- **期刊 / 卷号文章号**: Machine Learning, 115:200 (2026)
- **正式版 PDF**: [ML_2026_InstructionLearning.pdf](papers/ML_2026_InstructionLearning.pdf)
## 一句话概括

论文提出一种黑盒初始化、白盒表征 refinement 的 instruction learning 框架：黑盒 LLM 生成高质量且多样的候选指令，白盒模型的 hidden/output representations 与相似性正则化共同引导迭代搜索，以兼顾性能、可解释性和成本。

## 问题与动机

手工设计指令成本高且难扩展，纯黑盒 prompt search 需要大量调用、可能陷入次优解，纯白盒方法则受模型容量和计算资源限制，也可能在复杂任务上初始化失败。现有方法往往只用外部评分，忽略 LLM 内部隐藏表示，因此需要把 black-box feedback 与 white-box semantic signals 放进同一个迭代优化闭环，并改善跨任务、跨语言泛化。

## 方法

作者先用 ChatGPT-4o 根据五个示例生成 40 条初始指令，再用 Vicuna-13B 提取中间 hidden representation，并结合黑盒输出 representation 做融合与平均池化。随后训练带回归损失和 similarity regularization 的神经 surrogate，以动态调整相似性损失权重；每轮生成候选指令、抽取特征、用 ChatGPT-3.5-Turbo 评估，持续更新最佳指令，直到固定轮数或达到性能阈值。该设计让黑盒模型负责探索质量，白盒表示负责可解释的结构性 refinement。

## 实验与结果

在沿用 InstructZero 的 30 个任务上，与 APE、InstructZero、EvoPrompt 和 Instinct 比较，方法平均准确率为 0.6955，高于 0.6219、0.6639、0.6848 和 0.6113；在 GPT-4o-mini 目标模型上平均分为 0.7332，也高于 EvoPrompt 的 0.7118。消融显示去掉 similarity regularization 后均值降至 0.6840，去掉 output representation 后降至 0.6717。效率方面，运行时间 643.57 分钟、GPU 57.33 GB，低于 Instinct 的 818.46 分钟和 69.82 GB，但 API 成本为 3.24 美元，高于其 2.86 美元。

## 贡献与局限

贡献是系统融合黑盒初始化、白盒 hidden/output 特征和相似性约束，并通过跨 30 任务、目标模型替换及组件消融验证其作用。局限是 sentence_similarity 等细粒度语义任务收益有限，后续搜索仍依赖白盒表示质量；候选生成和 API 评估带来成本，实验规模与目标模型种类有限，黑盒初始化的外部依赖和更大模型上的成本—收益仍需进一步验证。

---
DOI: 10.1007/s10994-026-07137-4
