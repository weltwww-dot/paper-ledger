# An Enhanced Low-Computational-Complexity Predefined-Time Convergent Zeroing Neural Network for Constrained Time-Varying Quadratic Programming With Kinematic Control of Robotic Manipulator 总结

## 基本信息

- **标题**: An Enhanced Low-Computational-Complexity Predefined-Time Convergent Zeroing Neural Network for Constrained Time-Varying Quadratic Programming With Kinematic Control of Robotic Manipulator
- **作者**: Junpei Yang, Zhan Li, Weibing Li
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3672118
- **arXiv**: 无
- **PDF**: [NN_2026_EnhancedLowComputationalComplexity.pdf](papers/NN_2026_EnhancedLowComputationalComplexity.pdf)

## 一句话概括

本文提出 ELNCP-LCCZNN，通过降维非线性互补函数、无矩阵求逆的低复杂度零化神经网络和预定义时间激活函数，高效求解带等式、不等式及边界约束的时变二次规划，并用于机械臂运动控制。

## 问题与动机

带时变等式、约束和变量边界的二次规划广泛出现在机械臂实时运动规划中，但传统 ZNN 方案存在三类问题：完整处理约束的非线性互补问题会扩大矩阵和状态变量维度；常规 ZNN 每步需要矩阵求逆，不利于实时计算；噪声会使解的精度和轨迹稳定性下降。作者希望在保持约束可行性、预定义时间收敛和噪声鲁棒性的同时，降低模型维度与单步计算成本。

## 方法

作者设计低维 ELNCP 函数，将等式、不等式和边界约束编码到更小的互补问题中；在此基础上构造 LCCZNN 动力学，避免实时求解中的矩阵求逆。模型配合带指数/幂项的平滑过渡预定义时间激活函数（STPEAF），使收敛时间可以由参数预先设定，并提升对噪声的抑制能力。论文先证明模型的收敛、可行性和鲁棒性，再把时变二次规划转化为 6 自由度 UR3/UR3e 机械臂的速度级运动控制问题进行仿真和实体实验。

## 实验与结果

在 MATLAB R2024a 仿真中，ELNCP-LCCZNN 的无噪声残差保持在约 `10^-14` 量级，求解约在 `0.001 s` 内收敛，精度约为 `10^-12`；与 NCP-LCCZNN、LNCP-LCCZNN 及多种 RNN 基线相比，满足同样边界约束且计算时间更短。在常数、线性时变和二次时变三种噪声下，所提方法的计算精度稳定在约 `10^-10`，而部分传统方法误差会随时间积累。UR3 圆轨迹跟踪对比中，ELNCP-LCCZNN 的收敛时间为 `0.08 s`、位置 MSE 为 `1.29×10^-4`；其 CPU 时间约 `2.38 s`，虽然高于最简单 CZNN 的 `1.1 s`，但在采用非线性激活函数的改进方法中更具综合效率。线性时变噪声下，轨迹误差保持在 `10^-4` 量级；UR3e 实体实验中，关节速度始终满足约束，末端轨迹误差不超过 `1.5×10^-4 m`。

## 贡献与局限

贡献包括：用低维互补函数减少约束建模规模；消除实时矩阵求逆；在可预定义收敛时间的同时提高噪声下的解精度，并通过 UR3/UR3e 仿真和实体实验验证工程可行性。局限是 STPEAF 的指数和幂运算会带来额外 CPU 开销，参数选择需要在理论收敛时间与单步计算量之间折中；实验集中在特定 TVQP 和 6 自由度机械臂，尚未覆盖更高维、多目标或更复杂约束系统。对更强噪声、模型不确定性以及低算力控制器的实际部署仍需进一步评估。

---
DOI: 10.1109/tnnls.2026.3672118
