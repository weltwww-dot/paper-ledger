# Deep Reinforcement Learning With Adaptive Enhanced Attention for CTSPs 总结

## 基本信息

- **标题**: Deep Reinforcement Learning With Adaptive Enhanced Attention for CTSPs
- **作者**: Renyi Zhang；Xiangping Xu；Xinli Shi；Jinde Cao；Jie Gui
- **期刊 / 年份**: IEEE Transactions on Artificial Intelligence，2026
- **研究方向**: 神经组合优化、彩色旅行商与约束路径规划
- **DOI**: 10.1109/tai.2026.3673681
- **PDF**: [TAI_2026_ReinforcementAdaptiveEnhancedAttention.pdf](papers/TAI_2026_ReinforcementAdaptiveEnhancedAttention.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出自适应增强注意力模型 AEA，用强化学习统一求解带颜色可达性约束的 CTSP 与带容量、累计成本目标的 C2-CTSP，并通过增强注意力、动态约束解码和自适应惩罚提高解的质量与生成速度。

## 问题与动机

CTSP 要求不同销售员只能访问匹配颜色的城市，C2-CTSP 进一步加入容量约束和以客户到达累计成本为目标的开放路径。传统启发式方法需要手工规则，神经求解器则容易在动态可行域与累计成本之间失衡，且现有工作缺少面向 C2-CTSP 的专用 NCO 求解器。

## 方法

AEA 在编码器中将坐标、颜色和需求分别映射并融合，使用带 SiLU 非线性门控与 Hadamard 交互的 EAU，并结合预归一化和 SwiGLU 改善特征传播。解码器通过可学习权重融合上一节点、剩余容量和颜色状态，用位运算动态筛除不可行城市；针对 C2-CTSP，损失由累计路径成本与违反子路径约束的自适应惩罚组成，惩罚权重取当前批次的违规比例，再进行损失标准化和 REINFORCE 训练。

## 实验与结果

CTSP 实验覆盖 20、50、70、100、150、200 个节点的随机实例；C2-CTSP 覆盖 3/4 名销售员和 20、30、50、70 个节点。AEA 在 CTSP 上达到与精确求解器相近的成本，并优于所比较的启发式和神经基线；在 C2-CTSP 小规模实例上相对 GVNS/PLS 的平均 gap 小于 0.75%，大规模实例平均比 POMO 改善 0.2%。在 VRPTW 的 50/100 节点测试中，AEA gap 为 1.21%/1.43%，POMO 为 1.63%/2.03%，相对改善 25.8%/29.6%；在 ELI101/ELI301 上，AEA+DVNS 将 gap 从 3.30%/8.47% 降至 2.83%/7.67%。

## 贡献与局限

论文贡献包括面向颜色约束的动态解码、用于稳定训练的全局颜色表征与奖励归一化，以及首个面向 C2-CTSP 的 NCO 求解器；EAU 还在 TSP、CVRP 和 VRPTW 上显示出跨问题的收敛收益。局限是与 LKH-3 等专家启发式相比仍有小幅最优性差距，不同销售员配置需要重新训练，标准注意力的二次复杂度限制了超大规模实例的扩展。

---
DOI: 10.1109/tai.2026.3673681
