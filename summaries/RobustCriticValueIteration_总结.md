# Neural-network-based robust critic learning control with advanced value iteration for continuous-time dynamical systems 总结

## 基本信息

- **标题**: Neural-network-based robust critic learning control with advanced value iteration for continuous-time dynamical systems
- **作者**: Ao Liu、Ding Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108928
- **arXiv**: 无
- **PDF**: [NN_2026_Paper12.pdf](papers/NN_2026_RobustCriticLearningControl.pdf)

## 一句话概括

本文用神经网络 critic 学习和改进价值迭代，为连续时间非线性系统设计无需初始可行控制律的鲁棒控制器。

## 问题与动机

连续时间非线性系统的自适应动态规划控制通常需要初始可行控制律，限制了算法启动条件。函数逼近误差还会影响参数选择与闭环稳定性。研究目标是放宽初始化要求并加快价值迭代收敛。

## 方法

作者提出带 advanced value iteration 的神经网络 robust critic learning 方法。通过新方案消除初始 admissible control law，并分析逼近误差以指导参数选择。引入 relaxation factor 加速迭代，同时对算法收敛和系统稳定性给出证明。

## 实验与结果

全文设置三个数值例子验证方法有效性。摘要明确报告改进价值迭代的收敛过程比传统 VI 更快，但没有列出可安全复述的统一性能数字。

## 贡献与局限

贡献是降低价值迭代的起始条件并给出鲁棒 critic 控制的理论分析。局限是验证主要依赖三个数值例子，复杂约束、噪声观测和真实系统实时计算开销仍需测试。

---
DOI: 10.1016/j.neunet.2026.108928

