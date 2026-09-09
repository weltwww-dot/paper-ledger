# DPIU: Dynamic Pedestrian Intention Understanding Through Cognitive Decision-Making 总结

## 基本信息

- **标题**: DPIU: Dynamic Pedestrian Intention Understanding Through Cognitive Decision-Making
- **作者**: Jiaheng Xiao、Zhihui Li、Mingxin Wang、Yu Xie、Qin Ma、Xin Wang、Yu Sun
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3665567
- **arXiv**: 无
- **PDF**: [NN_2026_DPIUDynamicPedestrianIntention.pdf](papers/NN_2026_DPIUDynamicPedestrianIntention.pdf)

## 一句话概括

本文提出基于认知决策机制的 DPIU 行人意图理解框架，通过多尺度轨迹特征、概率化目标意图和贝叶斯动态优化提升复杂交通场景下的多模态轨迹预测能力。

## 问题与动机

现有行人轨迹预测方法通常依赖速度连续性、社会力或姿态等时空特征，难以直接表达行人的潜在目标意图，也难以适应不同个体的行为差异。固定图结构或单一时间尺度还可能在路口等密集交互区域产生过度平滑，使预测轨迹偏离真实行为。作者希望利用历史经验和人的目标选择机制，在不依赖场景微调的情况下生成更准确、可解释的多模态预测。

## 方法

DPIU 由三个核心部分组成。多尺度细节特征模块按照时间尺度切分历史轨迹，保留突然转向、加减速等局部变化；目标意图预测模块使用概率模型估计行人对潜在空间目标的倾向，并通过当前场景与历史经验的相似度利用碎片化信息；动态优化模块将意图点概率叠加起来，再用基于贝叶斯的密度估计生成与真实行为更一致的多模态轨迹。整体流程把历史记忆、意图概率和动态交互结合起来，并通过消融实验分别检验各模块的作用。

## 实验与结果

实验覆盖 Stanford Drone Dataset（SDD）、ETH-UCY 和 ApolloScape，采用平均位移误差（ADE）与最终位移误差（FDE）评价预测质量。在 SDD 上，DPIU 相比 MemoNet 的 ADE/FDE 分别降低 3.25% 和 4.46%，在密集交互场景中相较 Trajectron++ 的 ADE 降低 43.79%；在 ETH-UCY 上取得最低平均 ADE，并较 SHENet 的 FDE 再降低 0.06 米；在 ApolloScape 上相较 TPnet 的 ADE 降低 45.3%，相较 TP-EGT 的 FDE 降低 40.7%。模型在统一配置下的推理时间为 6.5 毫秒，且在减少多模态候选数时仍保持较好的误差稳定性。

## 贡献与局限

- 提出把人类认知决策与历史经验引入行人轨迹预测的 DPIU 框架，显式建模目标意图及其概率。
- 通过多尺度轨迹分段与贝叶斯动态优化，同时增强局部运动变化捕捉能力和多模态预测的可解释性。
- 在 SDD、ETH-UCY 和 ApolloScape 上相较多种现有方法取得更低的 ADE/FDE，并兼顾预测速度。
- 局限：当前分析主要使用行人的历史轨迹和决策特征，没有充分建模道路、车辆等交通场景语义；作者计划在后续工作中加入场景语义及其对行为的影响。

---
DOI: 10.1109/tnnls.2026.3665567
