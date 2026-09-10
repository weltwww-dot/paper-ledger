# Towards robust deep reinforcement learning-based quantitative trading with neuro-symbolic trend analysis 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Towards robust deep reinforcement learning-based quantitative trading with neuro-symbolic trend analysis
- 作者：Junzhe Jiang, Zhiming Li, Aixin Cui, Xiao Zhou, Bo Li, Dongning Sun
- 期刊 / 年份：Neural Networks，2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108924
- PDF：[LogicQQuantTrading.pdf](papers/LogicQQuantTrading.pdf)

## 一句话概括

论文提出 Logic-Q：把可表达的人类市场趋势知识与深度强化学习结合，通过 neuro-symbolic trend analysis 动态识别市场状态，并调节单模型或多模型交易策略的动作分布，从而提升量化交易在市场变化和崩盘场景下的稳健性。

## 问题与动机

现有深度强化学习量化交易方法容易过拟合历史序列中的噪声，且对市场趋势识别不足，可能错过交易机会或在市场崩盘时产生较大回撤。技术指标和专家规则有助于识别趋势，但规则中的阈值等数值随市场变化而变，难以人工固定。因此需要一种既能利用抽象专家知识、又能由数据细化参数的机制。

## 方法

Logic-Q采用 program synthesis by sketching 范式，构建 neuro-symbolic trend analysis（NeSy-TA）。其中 Symbolic-TA 将抽象趋势知识写成程序草图，根据当前市场信息给出粗粒度市场标签和调节参数；Neural-TA再依据该标签学习更细粒度的趋势和参数。两者合成为 combo tuning parameter，用于调整下游 DRL 策略的动作概率分布。框架同时支持单智能体和包含不同模态策略的 ensemble reinforcement learning。

## 实验与结果

论文在 order execution 和 stock trading 两类量化交易任务上进行实验，并比较单模型、集成模型及多模态实现。结果表明，NeSy-TA能够进行更精确的市场分类并相应组合或修正 backbone 策略；Logic-Q在累计收益和最大回撤方面均大幅优于已有 state-of-the-art 基线，包括多模态 LLM 交易策略。论文还通过消融和扩展实验验证了神经趋势分析、多模态组合及相关设计的作用；原文未在摘要和结论中给出可直接统一引用的具体汇总数值。

## 贡献与局限

主要贡献是：将原有硬编码趋势分析扩展为 neuro-symbolic 机制；把 Logic-Q 扩展到不同模态和网络架构的策略集成；通过系统消融和结果分析验证 NeSy-TA 的有效性。局限在于性能依赖趋势规则草图、指标和下游策略的配置，神经符号模块还会带来额外计算开销；论文对更广泛资产、市场制度和极端交易条件的外推仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.108924
