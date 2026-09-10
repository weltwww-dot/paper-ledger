# Randomized forward mode gradient for spiking neural networks in scientific machine learning 总结

## 基本信息

- **标题**: Randomized forward mode gradient for spiking neural networks in scientific machine learning
- **作者**: Ruyin Wan, Qian Zhang, George Em Karniadakis
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108978
- **arXiv**: 无
- **PDF**: [NN_2026_RandomizedForwardModeGradient.pdf](papers/NN_2026_RandomizedForwardModeGradient.pdf)

## 一句话概括

本文用权重扰动和随机前向模式梯度训练脉冲神经网络，在不依赖反向传播的情况下完成科学机器学习回归任务。

## 问题与动机

SNN以稀疏脉冲事件工作，具有节能和神经形态硬件适配潜力，但传统反向传播的生物合理性有限，且不一定适合硬件实现。脉冲操作的非可微性也使直接训练困难，因此需要只依靠前向计算的替代梯度机制。

## 方法

作者在前向模式梯度框架中对权重矩阵加入小噪声，通过观察网络输出变化估计方向梯度。论文比较了两种替代梯度与扰动实现方式，并将其用于基于LIF神经元的脉冲多层感知器。该流程避免沿计算图反向传递梯度，因而更接近局部、并行的突触更新。

## 实验与结果

实验覆盖函数回归和多个偏微分方程求解任务。结果显示，随机前向模式训练取得了具有竞争力的预测精度，说明该方法能够学习科学计算中的连续映射；论文未将其表述为在所有任务上优于反向传播。

## 贡献与局限

贡献是把随机权重扰动前向梯度引入SNN科学机器学习，并以PDE回归验证其可行性和神经形态硬件潜力。局限在于实验主要集中于回归任务和软件仿真，扰动尺度、计算开销及真实Loihi等硬件上的收益仍需进一步评估。

---
DOI: 10.1016/j.neunet.2026.108978
