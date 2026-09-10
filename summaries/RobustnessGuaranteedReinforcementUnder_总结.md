# Robustness-Guaranteed Reinforcement Learning Under Uncertainties in Dynamics Modeling and State Estimates 总结

## 基本信息

- **标题**: Robustness-Guaranteed Reinforcement Learning Under Uncertainties in Dynamics Modeling and State Estimates
- **作者**: Duofeng Pan, Yongquan Huang, Rong Chen, Wenjie Lu, Manman Hu
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026年3月20日
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TAI.2026.3675539
- **arXiv**: 无
- **PDF**: [TAI_2026_RobustnessGuaranteedReinforcementUnder.pdf](papers/TAI_2026_RobustnessGuaranteedReinforcementUnder.pdf)

## 一句话概括

论文提出鲁棒性保证强化学习（RGRL），通过显式建模动力学和状态估计不确定性、联合学习控制器与Lyapunov函数，为不确定系统的闭环控制提供可验证的鲁棒性约束。

## 问题与动机

传统鲁棒强化学习通常依靠双层或极小极大优化提升平均或最坏情形性能，但难以严格保证闭环稳定性。已有方法还可能预先假定未经验证的吸引域，使强化学习问题本身不可解，导致训练损失被无法满足的状态主导。对于机器人和安全关键系统，动力学建模误差与状态估计误差必须同时纳入控制器设计。

## 方法

作者用ReLU神经网络表示系统动力学和不确定性，并将其转化为高层分段线性表示，以精确寻找最违反鲁棒条件的状态。RGRL在双层优化中同时学习控制器和Lyapunov函数，优先处理违反条件的状态，并设计鲁棒性损失约束不确定状态下的稳定性。论文进一步推导鲁棒控制器与Lyapunov函数存在的必要条件，用于预验证或缩小吸引域；结合控制饱和的几何分析，还给出可放大的最大鲁棒性范围。

## 实验与结果

实验覆盖倒立摆、二维四旋翼和12维三维四旋翼，并将鲁棒神经控制器（RNC）与Lyapunov神经网络控制、鲁棒迭代LQR及域随机化强化学习比较。倒立摆中，RGRL相对DRRL的平均收敛角误差为0.1270，对比DRRL的0.2215，降低57.3%；在20秒时平均角误差降低88.6%。三维四旋翼轨迹跟踪中，RNC的RMSE为0.08±0.015、MAE为0.06±0.035，均比RiLQR低33.3%，控制方差为0.018±0.03，对比RiLQR的0.276±0.04。实际动力学测试中，RNC使Lyapunov值总体趋于零，但神经网络近似误差约为10^-4，仍有4.75%的状态样本违反鲁棒条件。

## 贡献与局限

主要贡献是把鲁棒条件识别、吸引域可解性分析和Lyapunov约束纳入强化学习训练，并以必要条件和最大鲁棒性分析增强可验证性。局限是高维实际动力学的神经网络近似仍会产生反例，导致Lyapunov值短时上升；控制器通常比局部优化方法更保守、收敛更慢，且实验主要集中在仿真与四旋翼验证。

---
DOI: 10.1109/TAI.2026.3675539
