# Differentially Private Accelerated Distributed Algorithm for Aggregative Optimization 总结

## 基本信息

- **标题**: Differentially Private Accelerated Distributed Algorithm for Aggregative Optimization
- **作者**: Bing Liu, Dongxing Li, Li Chai
- **期刊 / 年份**: IEEE Transactions on Neural Networks and Learning Systems, 2026
- **研究方向**: 差分隐私、分布式聚合优化与梯度跟踪
- **DOI**: 10.1109/TNNLS.2026.3674758
- **PDF**: [NN_2026_DifferentiallyPrivateAcceleratedDistributed.pdf](papers/NN_2026_DifferentiallyPrivateAcceleratedDistributed.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出隐私保护的 heavy-ball DAGT 算法 PP-HB-DAGT，在分布式 aggregative optimization 中结合梯度跟踪、动量加速和 Laplace 噪声，实现可证明的差分隐私与线性均方误差收敛。

## 问题与动机

在 DAO 中，每个 agent 的目标不仅依赖自身决策，还依赖所有 agent 决策形成的 aggregate。频繁交换 aggregate 估计和梯度跟踪量会暴露局部决策或目标函数参数，普通加密或非隐私算法无法直接给出迭代输出的严格隐私保证。已有 DAO 研究较少同时处理差分隐私和 momentum acceleration，且重复加噪可能使估计误差不断累积。

## 方法

PP-HB-DAGT 用 heavy-ball 项加速局部决策更新，用 distributed dynamic average consensus 跟踪 aggregate，用 gradient tracking 估计全局梯度。每个 agent 在发送 aggregate 与梯度跟踪状态前加入独立 Laplace 噪声，并在对应动态更新中扣除同一噪声，使全局平均状态不保留历次噪声的累积项。作者在全局目标强凸且梯度 Lipschitz 连续、通信图连通且双随机的条件下，建立误差递推矩阵，给出线性收敛到最优解邻域的条件、稳态次优界以及有限迭代下的 ε-DP 证明。

## 实验与结果

数值实验包含 R² 中的最优设施布置和带 consensus regularization 的分布式 logistic regression。设施布置案例使用 5 个固定实体和 5 个自由实体，设 α=0.02、β=0.3、δ=1.0、K=100、噪声尺度 θi=0.01，并对 50 次模拟取平均。PP-HB-DAGT 能使局部决策和 aggregate 估计收敛；在相同噪声下，它比无 momentum 的 PP-DAGT 瞬态收敛更快，但稳态误差略大，且优于不稳定的带噪 DAGT。改变 α 和 ε 的实验验证了步长带来的速度—精度权衡及隐私预算越小、稳态误差越大的趋势；logistic regression 案例得到相同的 momentum 效应。

## 贡献与局限

贡献包括：面向 DAO 设计带 heavy-ball acceleration 的 DP 梯度跟踪算法；用 noise deduction 同时缓解隐私噪声累积并保持聚合估计准确；统一给出收敛、次优性和 ε-DP 分析。局限是强凸、平滑目标和固定步长假设限制了适用范围，常数噪声下只能收敛到最优解邻域，且更强隐私会牺牲优化精度；未来将改善准确性并处理带约束的 distributed aggregative optimization。DOI: 10.1109/TNNLS.2026.3674758
