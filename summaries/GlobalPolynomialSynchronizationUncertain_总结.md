# Global Polynomial Synchronization of Uncertain Complex-Valued Reaction–Diffusion T–S Fuzzy Memristive Neural Networks With Proportional Delays Under Adaptive Event-Triggered Control 总结

## 基本信息

- **标题**: Global Polynomial Synchronization of Uncertain Complex-Valued Reaction–Diffusion T–S Fuzzy Memristive Neural Networks With Proportional Delays Under Adaptive Event-Triggered Control
- **作者**: Yuxian Guo, Liqun Zhou
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-03-06
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3668287
- **arXiv**: 无
- **PDF**: [NN_2026_GlobalPolynomialSynchronizationUncertain.pdf](papers/NN_2026_GlobalPolynomialSynchronizationUncertain.pdf)

## 一句话概括

本文研究带比例时延和参数不确定性的复值反应–扩散 T–S 模糊忆阻神经网络，利用自适应事件触发控制建立全局多项式同步条件，并在退化情形讨论全局渐近同步。

## 问题与动机

复杂值忆阻神经网络同时包含复值状态、反应–扩散空间项、模糊规则、忆阻切换、不确定参数和比例时延，直接拆成实部与虚部会增加分析复杂度。周期触发控制可能带来不必要通信，且已有结果对比例时延或复域忆阻器的处理不足。作者希望在较弱且可验证的条件下实现同步并避免 Zeno 行为。

## 方法

作者将区间矩阵理论扩展到复域忆阻器，用共轭转置性质构造 Lyapunov 泛函，因而无需把复值状态拆成实部和虚部。基于误差系统建立 GPS 判据，并设计自适应事件触发控制器，使触发参数随系统状态调节；另给出常规事件触发控制器及 δ=0 时 GPS 退化为 GAS 的条件。理论条件只依赖有界激活函数等假设，并通过不等式和矩阵条件排除 Zeno 现象。

## 实验与结果

论文给出两个数值同步例子和一个图像加密/解密应用。二维系统例子取空间域 [-2,2]、比例延迟因子 q1=0.85、q2=0.75，Case I 用自适应事件触发控制实现 GPS，Case II 在 δ=0 时实现 GAS；无控制时误差状态不同步。第二个例子的判据量给出 ⊐1=−9.95、⊐2=−0.76，满足推论条件；与常规事件触发控制器相比，自适应控制器表现出更好的同步效果。图像实验中密文熵为 7.9912，原图和解密图熵分别为 7.6161 和 7.6212，密文直方图近似均匀且邻像素相关性降至接近零。

## 贡献与局限

贡献是：首次将区间矩阵理论用于复域忆阻器刻画，并以不拆分复状态的 Lyapunov 分析得到比例时延下 GPS 条件；自适应事件触发器兼顾同步性能、通信资源与 Zeno 排除，并以数值和图像应用验证。局限是激活函数须有界，反应–扩散空间域仍限于一维建模设定，实际二维/三维过程的适用性受限；未来将研究无界激活函数、高维空间和其他无界时延。

---
DOI: 10.1109/TNNLS.2026.3668287
