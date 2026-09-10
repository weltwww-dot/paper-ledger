# Resilient Secure Control of Networked Industrial Control Systems Under AI-Driven Feedback Poisoning via ACK Bundling 总结

## 基本信息

- **标题**: Resilient Secure Control of Networked Industrial Control Systems Under AI-Driven Feedback Poisoning via ACK Bundling
- **作者**: Xiao Cai, Yanbin Sun, Yanli Chen, Jinglei Tan, Kaibo Shi, Jun Cheng, Shiping Wen, Zhihong Tian
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3698054
- **arXiv**: 无
- **PDF**: [TDSC_2026_ResilientSecureControlNetworked.pdf](papers/TDSC_2026_ResilientSecureControlNetworked.pdf)

## 一句话概括

本文针对工业控制网络中的 AI 驱动反馈投毒攻击，提出由自适应 ACK 捆绑、梯度下降窗口调节和 Lyapunov–Krasovskii 稳定性分析组成的韧性控制框架，以降低通信开销并保持闭环跟踪稳定。

## 问题与动机

网络化工业控制系统的反馈通道同时受到通信延迟、异步更新和数据投毒的影响，攻击者还可以利用 ACK 的时间规律隐蔽地干扰闭环控制。仅靠固定频率反馈会增加通信负荷，也会暴露可被推断和利用的时间模式。已有控制分析往往使用理想化攻击或随机扰动，难以反映真实工业网络中攻击持续时间和间隔的时序特征，因此作者使用 SWaT 水处理系统攻击轨迹构造数据驱动的反馈投毒模型。

## 方法

系统采用含当前状态和延迟状态的离散采样反馈控制模型，并用 SWaT 数据集中 41 个带标签攻击场景的时间信息生成二值攻击激活信号。ACK 捆绑机制在可调窗口 (T_b) 内聚合多个确认，仅在窗口达到条件时发送 ACK，从通信层降低反馈频率并打破攻击者对时间规律的利用。作者定义同时考虑跟踪误差和通信频率的代价函数，用前向有限差分估计状态对 (T_b) 的影响，再以梯度下降在线更新窗口。为证明延迟和投毒反馈下的闭环稳定性，论文构造轻量级 Lyapunov–Krasovskii 泛函，并将稳定性条件转化为含反馈增益的线性矩阵不等式。

## 实验与结果

作者在基于 Simulink 的网络化无人水面艇（USV）平台上进行仿真，把 SWaT 的攻击轨迹对齐到采样时刻后注入反馈通道。实验考察了学习率、通信延迟和 AI 驱动反馈投毒三类因素；采样周期取 0.01、0.05 和 0.1，通信延迟最高测试到 2.319 s，梯度下降学习率取 0.001、0.005、0.1 和 0.5。结果显示，延迟不超过 2.319 s 时系统仍能保持稳定运行，但收敛变慢、振荡增强；超过该临界范围后轨迹发散。适中的学习率使 ACK 窗口变化更平滑，在投毒反馈下保持较平稳的控制输入和较小的跟踪偏差；与无自适应监督的固定调节相比，自适应 ACK 捆绑通常产生更少或相当的通信传输，并能缓解攻击造成的控制输入振荡。论文同时指出，过大的学习率会放大窗口振荡，过小则降低对时变网络的响应速度。

## 贡献与局限

本文把真实攻击轨迹、通信层 ACK 调节、在线参数优化和闭环稳定性证明整合到同一控制回路中，兼顾了反馈投毒下的跟踪韧性、通信效率和时延稳定性。局限在于验证主要是 USV 代表性仿真，SWaT 轨迹来自水处理系统，与具体工业对象的物理过程并不完全相同；当前范围集中在反馈投毒和通信延迟，传感器退化、执行器故障以及真实工业硬件上的部署仍未覆盖。学习率和初始窗口的选择也会显著影响瞬态性能与稳定裕度。

---
DOI: 10.1109/TDSC.2026.3698054
