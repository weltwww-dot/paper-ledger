# Deterministic Learning-Based Fault Identification for Nonlinear Sampled-Data Systems: Learning Accuracy Analysis 总结

## 基本信息

- **标题**: Deterministic Learning-Based Fault Identification for Nonlinear Sampled-Data Systems: Learning Accuracy Analysis
- **作者**: Tianrui Chen, Jiajue He, Jingtao Hu, Cong Wang
- **期刊 / 年份**: IEEE Transactions on Neural Networks and Learning Systems, 2026
- **研究方向**: 机器学习方法；确定性学习、故障辨识与非线性控制系统
- **DOI**: 10.1109/tnnls.2026.3671326
- **PDF**: [NN_2026_DeterministicFaultIdentificationNonlinear.pdf](papers/NN_2026_DeterministicFaultIdentificationNonlinear.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文为非线性采样数据系统提出基于 deterministic learning 的故障辨识方案，把估计器与局部 RBF 神经网络权重写成采样线性时变系统，并推导可由可测信号计算的学习精度和收敛速度公式。

## 问题与动机

工业故障辨识既要处理未建模动力学、故障项和噪声，又要给出可验证的学习精度；现有工作更多关注诊断或控制性能，对神经网络权重和故障近似误差的定量分析较少。全局 persistent excitation 条件严格且难满足，已有收敛分析还因估计与自适应耦合而复杂，难以直接用于实际性能评估。

## 方法

作者用沿系统轨迹选取的 localized RBF 网络近似未知动力学，设计状态预测估计器和基于下一时刻预测误差的权重自适应律，将状态误差与权重误差组成 sampled-data LTV 学习误差系统。为处理耦合，作者从权重子系统的状态转移矩阵构造 time-varying symmetric positive definite matrix，并据此建立 Lyapunov 函数；在局部 PE、采样和增益条件下，Theorem 1 给出权重收敛邻域及 NN 逼近误差上界，Theorem 2 给出收敛速度，公式中的 PE、网络和扰动参数均可由轨迹、回归向量和可测信号计算。

## 实验与结果

机器人操纵器仿真使用采样周期 0.005 s、10 个 RBF 节点和噪声幅值 0.05，理论收敛误差上界计算为 2，实验实际误差验证了该上界可由可测信号估计。在噪声幅值 4 的比较中，所提 DLFI 的收敛速度与 FTCL、FxTCL 相当，但收敛精度明显更高。Mansoux 压气机旋转失速模型使用 22 个 RBF 节点和采样周期 0.01 s，公式给出的误差上界为 0.025；学习增益允许范围为 (0, 82.64]，兼顾速度与精度的实验区间约为 [1.5, 21]。

## 贡献与局限

贡献包括：提出适用于非线性 sampled-data 系统的确定性学习故障辨识器；用专门构造的时变正定矩阵完成耦合 LTV 系统的指数收敛分析；给出不依赖未知参数、可实际计算的学习精度与速度公式，并用操纵器和压气机仿真验证。局限是结果依赖 RBF 回归向量的局部 PE，只保证沿轨迹的局部辨识精度；采样周期需在离散化误差与计算负担间折中。作者将进一步研究其他网络的 PE 条件及随机非线性故障。

---
DOI: 10.1109/tnnls.2026.3671326
