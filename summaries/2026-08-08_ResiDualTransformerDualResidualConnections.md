# ResiDual: Transformer with dual residual connections 总结

## 基本信息
- **标题**: ResiDual: Transformer with dual residual connections
- **作者**: Shufang Xie、Huishuai Zhang、Junliang Guo 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-08-08
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104602
- **PDF**: [AIJ_2026_ResiDualTransformerDualResidualConnections.pdf](papers/AIJ_2026_ResiDualTransformerDualResidualConnections.pdf)

## 一句话概括
ResiDual 将 Pre-LN 与 Post-LN 的残差路径并行结合，试图同时缓解深层 Transformer 的梯度消失与表示坍缩。

## 问题与动机
Post-LN 在深层网络中可能使浅层梯度快速衰减；Pre-LN 虽改善梯度传播，却可能让高层表示逐渐相似，削弱模型表达能力。作者指出，既有改进通常偏重其中一个问题，因此希望用同一结构兼顾优化稳定性与表示多样性。

## 方法
每个模块保留 Post-LN 式归一化残差支路，同时另设一条累积未归一化残差的 Pre-LN 式支路，最终将两路表示相加。理论分析给出梯度范数下界，并分析表示多样性随深度的变化；推导采用简化的注意力、初始化及归一化假设。

## 实验与结果
作者在机器翻译、语言建模和视觉分类任务上与多种残差及归一化基线比较，并报告多个深度下的结果。ResiDual 在所测任务中总体优于标准 Pre-LN/Post-LN，深层模型优势更明显；实验还扩展到 50 层，且相对基线额外计算开销较小。结果支持其理论分析，但结论范围仍受所用任务、模型配置及推导假设约束。

## 贡献与局限
- 用双残差结构统一应对梯度传播与表示多样性问题，并给出相应理论分析。
- 在多种任务和模型深度上验证方法，也评估了吞吐、内存与计算量。
- 理论证明依赖简化条件，实验覆盖的是论文所选基准；对不同架构、训练设置及更大规模模型的普适性仍需进一步检验。

---
DOI: 10.1016/j.artint.2026.104602
