# Policy-Adjustable Q-Learning for Data-Driven Nonlinear Optimal Tracking Control 总结

## 基本信息

- **标题**: Policy-Adjustable Q-Learning for Data-Driven Nonlinear Optimal Tracking Control
- **作者**: Jiaoyuan Chen, Dawei Gong, Yuyang Zhao, Shijie Song, Minglei Zhu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3672136
- **arXiv**: 无
- **PDF**: [NN_2026_PolicyAdjustableQData.pdf](papers/NN_2026_PolicyAdjustableQData.pdf)

## 一句话概括

论文提出可调策略 Q 学习（PA-QL），把代价函数中的控制权重直接作为神经网络输入，使一个离线训练得到的策略能够在运行时连续调整，而无需为每组权重重新训练。

## 问题与动机

数据驱动的 ADP/Q-learning 通常围绕固定代价函数离线训练，环境或控制目标变化后往往必须重新训练。预先训练多套策略再切换虽然可行，但训练成本高、切换是离散的，并可能引起稳定性和控制信号突变。作者希望保留离线策略的快速执行，同时获得 LQR/MPC 一类在线调节状态权重和控制权重的灵活性。

## 方法

PA-QL 针对输入仿射非线性离散时间系统，在增广神经网络输入中加入控制权重矩阵的对角向量，学习“状态、期望轨迹、权重→最优策略”的连续映射。模型 NN、逆动力学 NN、critic NN 和 actor NN 通过输入输出数据迭代训练，不需要显式机理模型；理论部分分析了该策略对权重调整的最优性、可行性和收敛性质。运行时可根据跟踪误差改变权重，例如采用 τ=1+4exp(-||xk-dk||2) 的误差驱动规则，从而连续改变控制激进程度。

## 实验与结果

实验一使用离散 RLC 电路，采样间隔 0.1 s，采集 1000 对训练数据；PA-QL 在改变输入权重后仍与代数 Riccati 方程给出的最优控制完全一致，并在 50 个随机初始状态上保持一致。实验二使用 Van der Pol 振荡器，采样间隔 0.1 s，采集 2000 对数据。较大的控制权重带来更保守、更慢的收敛，较小权重则产生更积极的控制。与多策略切换相比，PA-QL 达到相近跟踪效果但控制输入连续；与预测时域 N=10 的自适应 MPC 相比，单步平均计算时间为 8.024×10^-6 s，而 MPC 为 3.60×10^-3 s，约快近三个数量级。

## 贡献与局限

贡献包括：把控制权重参数化地嵌入 Q 学习网络，形成一次训练、多目标在线调节的策略；通过连续权重映射避免离散策略切换；在非线性跟踪仿真中展示了无需重训的最优性与低在线开销。局限是验证仍以两个仿真系统为主，且作者明确指出尚需研究神经网络逼近误差传播下的严格理论，并扩展到更广泛的真实实时系统。

---
DOI: 10.1109/TNNLS.2026.3672136
