# Proven advantage of multiobjective evolutionary algorithms for problems with different degrees of conflict

## 基本信息

- 标题: Proven advantage of multiobjective evolutionary algorithms for problems with different degrees of conflict
- 作者: Weijie Zheng
- 期刊 / 会议: Artificial Intelligence 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1016/j.artint.2026.104573
- PDF: [AIJ_2026_ProvenAdvantageMOEA.pdf](papers/AIJ_2026_ProvenAdvantageMOEA.pdf)

- 标题: Proven advantage of multiobjective evolutionary algorithms for problems with different degrees of conflict
- 作者: Weijie Zheng
- 期刊 / 会议: Artificial Intelligence 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

作者为 Weijie Zheng；发表于 *Artificial Intelligence* 358 (2026) 104573。论文是关于多目标进化算法在不同目标冲突程度下运行时间与 Pareto 覆盖能力的理论分析，核心测试族为 OneMaxMin_k 及其 LOTZ_k 变体。DOI: 10.1016/j.artint.2026.104573
## 一句话概括

作者证明在冲突程度参数 k 变化时，多目标进化算法在特定伪布尔基准上仍可达到 O(max{k,1} n ln n) 或 O(max{k,1} n²) 的期望时间，并说明标量化和惩罚法何时无法完整恢复 Pareto 集。

## 问题与动机

多目标优化中目标之间的冲突程度会直接影响 Pareto 前沿的形状和算法搜索难度，但许多理论结论只针对完全冲突或固定的二目标设置。论文希望在可控的冲突参数 k 下比较标量化、ε-约束、外部惩罚和多种进化算法，解释何时“多目标”方法相对单目标标量化具有理论优势。

## 方法

OneMaxMin_k 用 k 个冲突位刻画冲突程度，包含 k=n/2 的 COCZ、k=n 的 OneMinMax 和 k=0 的无冲突情形。作者先证明任意权重标量化在 k>2 时不能覆盖完整 Pareto 集；ε-约束在选取 k+1 个合适阈值时可以覆盖完整前沿，外部惩罚则需要满足 `r > 1/(ε+1−ceil ε)` 等条件。随后对 RLS、(G)SEMO、MOEA/D、NSGA-II、SMS-EMOA 进行漂移/势函数式期望运行时间分析，并将结果扩展到 LOTZ_k。

## 实验与结果

论文没有数据集、实证仿真或实验基线，结果全部是理论期望界。在 OneMaxMin_k 上，RLS、(G)SEMO、MOEA/D、NSGA-II 和 SMS-EMOA 在各自自然参数条件下达到 O(max{k,1} n ln n)；例如 NSGA-II 需要种群规模 N≥4(k+1)，SMS-EMOA 需要 μ≥k+1 及合适参考点，MOEA/D 使用 k+1 个子问题。对 LOTZ_k，相关算法达到 O(max{k,1} n²)。这些界说明随着冲突程度增加，搜索代价以 k 线性放大，同时标量化仍可能遗漏前沿。

## 贡献与局限

贡献是把“目标冲突程度”显式参数化，并给出从标量化失败、约束法覆盖到多个 MOEA 运行时间的统一理论图景。局限是分析集中于二目标伪布尔函数和结构高度规则的基准族，依赖自然参数条件；不能直接推出一般多目标、连续问题或实际复杂前沿上的经验优势，也没有实验验证。后续应研究更多目标、不同冲突结构和与真实应用的联系。

DOI: 10.1016/j.artint.2026.104573
