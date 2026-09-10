# A Neural-Network-Assisted Approach to Recursive State Estimation for Energy Harvesting Complex Networks With Unknown Nonlinearities 总结

## 基本信息

- **标题**: A Neural-Network-Assisted Approach to Recursive State Estimation for Energy Harvesting Complex Networks With Unknown Nonlinearities
- **作者**: Yuhan Zhang, Zidong Wang, Lei Zou, Junping Du, Shuang-Hua Yang
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026年3月10日
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3669864
- **arXiv**: 无
- **PDF**: [NN_2026_AssistedApproachRecursiveState.pdf](papers/NN_2026_AssistedApproachRecursiveState.pdf)

## 一句话概括

论文面向带未知非线性、能量采集传感器和部分节点可观测的复杂网络，提出同时递推估计网络状态与未知非线性的神经网络状态估计方法。

## 问题与动机

复杂网络中的传感器可能只能获得部分节点信息，且能量采集传感器只有在当前能量足以承担通信消耗时才发送测量值，使传统状态估计面临信息不完整和通信受限的双重困难。与此同时，网络动力学中的未知非线性会进一步扩大估计误差。论文因此希望在能量约束和部分节点观测下，仍能对系统状态及未知非线性进行有效递推估计。

## 方法

作者利用神经网络的通用逼近能力表示复杂网络中的未知非线性，并建立基于部分节点的递归状态估计器。能量采集机制由随机变量描述，传感器仅在能量水平满足传输成本时发送测量。方法在统一递推框架中同时计算状态估计器增益和神经网络权重调节参数，并通过充分条件最小化状态估计误差上界及神经网络权重估计误差迹的上界。该设计还保留了对能量采集、节点可用性和网络耦合影响的显式刻画。

## 实验与结果

论文采用一个复杂网络仿真例子验证方法，仿真长度为50，并绘制了多个节点状态及其估计轨迹、5个未知非线性函数的估计误差、能量采集与能量消耗以及不同参数设置下的误差范数。结果显示，即使部分节点没有测量信息，神经网络递归估计器仍能同时较好地估计系统状态和未知非线性；固定神经网络权重时性能变差，而递推计算权重调节参数能保持有效性。改变内耦合矩阵后，方法仍表现出良好的估计性能。

## 贡献与局限

主要贡献是把能量采集通信、部分节点观测和未知非线性逼近纳入同一递归估计框架，并给出可递推计算的增益与权重调节参数及误差上界条件。局限在于验证主要依赖单个仿真例子，尚未系统评估真实网络和更复杂通信异常；作者将含网络攻击、故障、丢包或时延的情形以及未知非线性复杂网络的钉扎控制列为后续方向。

---
DOI: 10.1109/TNNLS.2026.3669864
