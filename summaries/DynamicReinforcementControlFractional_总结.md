# Dynamic Reinforcement Learning Control for Fractional-Order Neural Networks With Higher Order Interactions and Multiple Time Delays 总结

## 基本信息

- **标题**：Dynamic Reinforcement Learning Control for Fractional-Order Neural Networks With Higher Order Interactions and Multiple Time Delays
- **作者**：Hua Li, Min Xiao, Chengdai Huang, Qingxiang Fang, Xia Huang, Wenwu Yu, Yi Yao, Tingwen Huang, Leszek Rutkowski
- **期刊 / 年份**：IEEE Transactions on Artificial Intelligence，2026
- **研究方向**：复杂神经动力学、分数阶系统与强化学习控制
- **DOI**:10.1109/TAI.2026.3673682
- **PDF**：[TAI_2026_DynamicReinforcementControlFractional.pdf](papers/TAI_2026_DynamicReinforcementControlFractional.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文构造带模块化高阶三元相互作用、分数阶导数和多重时延的大规模神经网络，推导稳定性与 Hopf 分岔条件，并用不依赖显式模型的强化学习在线调节高阶耦合系数，以抑制时延诱发的振荡。

## 问题与动机

仅含成对连接的常规神经网络难以表达生物神经系统中的模块化高阶相互作用；分数阶记忆效应和多重时延又使大规模网络的稳定性与分岔分析变得高维、非线性且难以解析。传统模型控制器通常需要显式的稳定边界、特征根或分岔阈值，而这些量在复杂时延网络中难以在线求解。作者因此希望同时给出可分析的理论条件和不依赖精确模型的自适应控制路径。

## 方法

模型包含 3n+1 个神经元：3n 个外围神经元按三元簇组织，并与中心神经元构成 star-ring 结构，采用 Caputo 分数阶导数、tanh 激活函数和统一时延假设。在线性化系统上，作者使用 Coates 流图分解特征方程，得到无时延稳定条件、存在纯虚根的条件、首个分岔阈值 τ0 及横截性条件，从而刻画分数阶 α、自反馈 μ、高阶耦合 c 和网络规模 n 的作用。控制器是带二次/交叉多项式特征的 TD 线性 Q 学习 agent，以 ϵ-greedy 平衡探索和利用，动作直接取 c；奖励由加权平衡点跟踪误差和 `tanh(c)^2` 控制幅度惩罚组成，部署时根据状态贪心调节 c。

## 实验与结果

数值实验以 n=3 的 10 神经元网络为例：μ=0.63 时在 τ=0.5 下收敛且理论上对所有时延稳定；μ=0.58、c=0 时得到 τ0=0.2107，τ=0.1 稳定而 τ=0.3 出现持续振荡。固定 α=0.98 时将 c 从 0 调为 −0.1，τ0 从 0.2107 提高到 0.5932，使 τ=0.3 恢复稳定；当 α 从 0.91 增至 1、c=0 时，τ0 从 1.0671 降至 0.0404。RL 在 τ=0.2 和 0.3、t=800 启动后均能压制原有振荡并将状态推回平衡；在相对训练时延 ±30% 的异质时延环境中无需重训练仍能稳定，且在临界 τ=0.3453 测试中使谱 abscissa 变为负值。

## 贡献与局限

贡献包括：提出结合高阶三元耦合、分数阶记忆和时延的网络模型；用流图方法给出局部稳定与 Hopf 分岔判据；设计直接调节高阶耦合系数的模型无关 TD-RL 控制器，并以均匀、异质时延和不同初始振幅实验验证其抑振能力。局限是理论闭式条件依赖统一时延和局部线性化，tanh 也只是生物机制的简化；多项式特征维度会随网络规模增长而成为瓶颈，极端或快速时变时延、深度 RL 和更大网络的泛化仍未验证。
