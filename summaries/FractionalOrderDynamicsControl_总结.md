# Fractional-Order Dynamics Learning and Control via Data-Driven Approaches: Taking Soft Manipulator as an Example 总结

## 基本信息

- **标题**: Fractional-Order Dynamics Learning and Control via Data-Driven Approaches: Taking Soft Manipulator as an Example
- **作者**: Xiangyu Shao、Linke Xu、Shaojie Zhang、Guanghui Sun、Chengwei Wu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3665811
- **arXiv**: 无
- **PDF**: [NN_2026_FractionalOrderDynamicsControl.pdf](papers/NN_2026_FractionalOrderDynamicsControl.pdf)

## 一句话概括

本文面向具有记忆和非局部效应的软体机械臂，提出从分数阶动力学学习到鲁棒控制的一体化数据驱动框架，在较低建模误差和有限时间稳定控制之间建立协同设计。

## 问题与动机

分数阶微积分能够表达复杂系统的记忆效应，但也使动力学辨识和控制更加困难。软体机械臂还存在模型不确定性、外部扰动和执行器饱和，传统整数阶模型或只针对单一误差来源的控制器难以同时处理这些因素。作者希望直接从均匀采样数据学习分数阶动力学，并将模型、扰动观测和控制器联合起来。

## 方法

框架包含三个核心组件。fPLCS-DeLaN 是带物理先验的分数阶深度拉格朗日网络，以 Transformer 式结构和长短期卷积自注意力捕捉记忆效应；T2F-CRNN 结合 CNN 的时间特征、层次循环结构与区间模糊推理，估计未知且非均匀有界的综合扰动；最终的全分数阶控制器加入输入饱和补偿和滑模约束，并给出实际有限时间收敛性质，从而把动力学学习误差和控制不确定性纳入同一流程。

## 实验与结果

仿真与软体机械臂实验共同评估建模和轨迹跟踪性能。fPLCS-DeLaN 的建模误差比对比模型至少低一个数量级，而计算时间增加不到 15%；在结论汇总的实验证据中，相比先进控制器，所提出控制器使瞬态跟踪误差降低 23.1%，稳态跟踪误差降低 87.6%。真实软体机械臂实验还验证了在执行器饱和和模型失配条件下的跟踪效果，说明该框架不仅在仿真中有效，也具有实际控制可行性。

## 贡献与局限

- 将分数阶动力学学习、扰动观测和有限时间控制整合为统一数据驱动框架。
- 在 DeLaN 中嵌入分数阶结构和记忆建模能力，降低软体系统动力学学习误差。
- 通过 T2F-CRNN、饱和补偿和滑模约束提高实际跟踪鲁棒性。
- 局限：当前示例依赖软体机械臂和均匀采样数据；更高保真 Cosserat 杆模型、迟滞、自激振动以及传感器/执行器故障仍未完全纳入，控制器的复杂度也会增加部署成本。

---
DOI: 10.1109/tnnls.2026.3665811
