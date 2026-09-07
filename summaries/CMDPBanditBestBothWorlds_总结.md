# Policy optimization for CMDPs with bandit feedback: Best-of-both-worlds and beyond 总结

## 基本信息

- **标题**: Policy optimization for CMDPs with bandit feedback: Best-of-both-worlds and beyond
- **作者**: Francesco Emanuele Stradi, Anna Lunghi, Matteo Castiglioni, Alberto Marchesi, Nicola Gatti
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01（2026-07-19 在线发布）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104589
- **arXiv**: 无
- **PDF**: [AIJ_2026_CMDPBanditBestBothWorlds.pdf](papers/AIJ_2026_CMDPBanditBestBothWorlds.pdf)

## 一句话概括

本文针对奖励与约束可随机或对抗的带约束马尔可夫决策过程（CMDP），提出首个基于策略优化的 bandit 反馈 best-of-both-worlds 算法 PDB-PS，在无需知道 Slater 参数的前提下取得最优遗憾与约束违反界。

## 问题与动机

在许多真实交互式决策场景（自动驾驶、广告竞价、推荐系统等）中，学习者在奖励最大化的同时还需满足成本约束，这类问题通常建模为 CMDP。在线序贯 CMDP 中，奖励与约束每回合既可能按固定分布随机生成，也可能由对手对抗选择，而学习者在实践中往往只能获得所走轨迹上的 bandit 反馈。此前 Stradi 等人提出的首个 best-of-both-worlds 算法虽然能统一处理随机与对抗约束，但只适用于全反馈，并且需要在占用测度空间上每回合求解凸优化，效率很低。作者的目标是在 bandit 反馈下获得能同时最优处理两类约束的算法，并采用更高效的策略优化方法。

## 方法

作者提出 primal-dual 元算法 PDB-PS：对偶侧采用在线梯度下降（OGD），将有界对偶空间约束在 [0,T^{1/4}]^m 上以处理退化情形；原问题侧采用策略优化式的 regret minimizer FS-PODB（带 dilated bonus 的 fixed-share policy optimization），它基于 OMD 与（非归一化）负熵正则化，并叠加 fixed-share 更新使策略远离决策边界，从而获得 no-interval-regret 性质——这是首个对 bandit 反馈对抗 MDP 建立的此类结果。算法用乐观估计的状态-动作价值函数与 dilated bonus 控制估计方差并激励探索，用随观测 Lagrange 乘子上界动态调整的回合相关学习率，使遗憾对乘子只呈线性依赖。借助原、对偶 minimizer 的 no-interval-regret 性质，可证明 Lagrange 乘子在学习过程中自动有界（Λ=112mH²/ρ²，概率至少 1−11δ），因此无需知道 Slater 参数 ρ 即可给出对任意 ρ 值的界。

## 实验与结果

理论保证：约束随机且 Condition 2 成立时，算法以至少 1−14δ（随机奖励）或 1−13δ（对抗奖励）概率达到 Õ(√T) 遗憾与 Õ(√T) 违反；ρ 任意小（Condition 2 不成立）时退化为 Õ(T^{3/4})。约束对抗时，其累计收益至少为最优可行收益的 ρ/(ρ+H) 分数且违反为 Õ(√T)，该折衷被证明紧。对有限对抗性（非平稳度 E）约束，遗憾为 Õ(Λ(√T+E))；对每回合须满足约束的更弱基线，Condition 2 成立时恢复 Õ(√T) 遗憾与违反。实验（附录 L）在单决策状态 CMDP 上进行：3 个随机实例（动作数 4/8/16）与 2 个对抗实例（switching/cyclic 奖励），对比均匀随机 greedy 基线，每条曲线为 30 次独立运行均值并附 95% 置信区间。结果显示 PDB-PS 在两种反馈制式下均能稳定控制累积约束违反；基线虽常因采样不可行高奖励动作而取得更低甚至负遗憾，但代价是线性级大幅违反。运行时对比（m=8 约束、4 次重复）显示，策略搜索更新耗时近乎恒定，而占用测度式更新随动作数增长迅速变贵。

## 贡献与局限

主要贡献：首次为 bandit 反馈的序贯 CMDP 提供 best-of-both-worlds 算法，且基于策略优化、无需逐回合求解凸规划，效率显著高于既有占用测度方法；无需 Slater 参数 ρ 的先验知识即可覆盖任意 ρ；首创 bandit 反馈对抗 MDP 的 no-interval-regret 结果；将分析推广到有限对抗性与更弱基线两种设置并证明相应界的紧性（与 Bernasconi 等人下界一致）。局限：依赖表格（tabular）假设与未知转移估计，bandit 下 ρ 任意小对应的 Õ(T^{3/4}) 档是否本质尚待研究；向函数近似、连续状态动作空间、延迟反馈等更一般模型与非平稳形式的扩展仍是开放问题，且实验仅在简单实例上验证。

---
DOI: 10.1016/j.artint.2026.104589
