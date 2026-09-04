# Event-triggered impulsive control for switched delay systems and its application in image encryption of switched neural networks 总结

## 基本信息

- **标题**: Event-triggered impulsive control for switched delay systems and its application in image encryption of switched neural networks
- **作者**: Zhifeng Lu, Haiying Wang, Yujuan Tian
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-08-26
- **内容状态**: 完整
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109525
- **PDF**: [NN_2026_EventTriggered.pdf](papers/NN_2026_EventTriggered.pdf)

## 一句话概括

研究带时滞的切换非线性系统的事件触发脉冲控制（ETIC）：提出模态依赖事件触发机制（MDETM），用 Lyapunov–Razumikhin 与平均驻留时间方法给出指数稳定判据并排除 Zeno 现象，再把结果用于切换神经网络的同步与图像加密。

## 问题与动机

切换与时滞并存时，延迟状态可能来自当前子系统不同的一段历史区间，切换也可能发生在下一次脉冲之前，使稳定性分析与控制综合变得困难；同时希望只在触发时刻施加脉冲输入，从而降低控制器到执行器的通信负担。

## 方法

构造模态依赖事件触发机制，把与初始历史信息相关的指数衰减项纳入触发条件，以处理时滞与切换耦合的影响；基于 Lyapunov–Razumikhin 方法与平均驻留时间技术建立充分判据，保证系统指数稳定并排除 Zeno 行为，同时给出事件间隔的显式下界。将该理论应用于切换神经网络（SNN）的指数同步，触发机制与脉冲控制增益的设计条件写成线性矩阵不等式（LMI）；随后用同步系统驱动图像加密。

## 实验与结果

两个数值算例验证有效性，其中图像加密算例中相邻像素相关系数由接近 0.97–0.99 降至约 ±0.004（RGB 三通道），信息熵从约 6.79–7.19 升至 7.999；NPCR 约 99.34%–99.50%、UACI 约 33.35%–33.42%，接近理论理想值（99.6094% / 33.4635%）。与需要置换步骤的同步加密算法相比，本方法无需置换仍能打散相邻像素相关性，计算与内存开销更低。

## 贡献与局限

- 贡献一：带指数衰减项的模态依赖事件触发机制，解决切换+时滞下稳定判据与 Zeno 排除问题，并给出事件间隔下界。
- 贡献二：把结果推广到 SNN 指数同步并以 LMI 表达设计条件，图像加密实验验证实用性。
- 局限：未考虑脉冲信号本身的采样/传输时延；未来拟发展事件触发延迟脉冲控制并纳入外部扰动。

---

DOI: 10.1016/j.neunet.2026.109525
