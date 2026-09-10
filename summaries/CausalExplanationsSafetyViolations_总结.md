# Causal explanations of safety property violations in discrete event systems 总结

## 基本信息
- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: Causal explanations of safety property violations in discrete event systems
- **作者**: Gregor Gössler, Thomas Mari, Yannick Pencolé, Louise Travé-Massuyès
- **期刊 / 会议**: Artificial Intelligence 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104588
- **PDF**: [CausalExplanationsSafetyViolations.pdf](papers/CausalExplanationsSafetyViolations.pdf)

## 一句话概括
论文为离散事件系统中的安全性质违例建立因果解释理论，在部分可观测、含事件和变量的动态系统中说明“为什么”观测轨迹导致失败。

## 问题与动机
传统故障诊断通常回答发生了什么，却未必说明为何观测轨迹违反安全性质。嵌入式系统具有并发、部分观测、变量约束和复杂事件序列，简单截取日志会保留大量无关行为，因此需要同时表达相关事件、变量状态、因果顺序以及相对于预期行为的对比信息。

## 方法
作者用带隐式状态和变量的自动机表示离散事件系统，先定义 soundness、completeness、causality 等解释要求，再研究基于轨迹最小子序列的解释。核心是 choice explanation：按系统逐层作出的选择构造解释，突出把系统推向违例的关键选择，并保留可避免该结果的替代事件；框架也支持 contrastive explanation。

## 实验与结果
论文以形式化定义、定理和示例验证框架性质，而非数据集统计实验。示例中，包含 7 个转换的 choice explanation 可用含 246 个状态和 415 个转换的自动机表达，展示在压缩完整行为的同时保留因果信息；作者还给出了可计算 choice explanation 的高效算法及实现。

## 贡献与局限
贡献是形式化安全违例解释语义与期望性质，统一事件和变量状态信息，并提出兼顾轨迹压缩和关键选择识别的 choice explanation 算法。局限是目前主要针对已有行为模型，在线构造、抽象模型、日志观测选择以及如何利用解释预防后续违例仍是开放问题。

---
DOI: 10.1016/j.artint.2026.104588

