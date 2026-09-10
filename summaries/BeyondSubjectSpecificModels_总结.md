# Beyond Subject-Specific Models in Dynamical Human--Machine Interaction: Benchmarking and Optimization Strategies

## 基本信息

- **标题**: Beyond Subject-Specific Models in Dynamical Human--Machine Interaction: Benchmarking and Optimization Strategies
- **作者**：Luca Manneschi、Matthew O. A. Ellis、Elisa Donati
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3662308
- **arXiv**：无
- **PDF**：[NN_2026_BeyondSubjectSpecificModels.pdf](papers/NN_2026_BeyondSubjectSpecificModels.pdf)

## 一句话概括

本文围绕表面肌电驱动的动态人机交互，系统比较时序模型及跨受试者适应策略，说明 TCN、迁移学习、LoRA/适配器和元学习能够降低对逐人训练的依赖。

## 问题与动机

利用表面肌电信号连续预测手指位置，可用于假肢和其他人机接口，但不同受试者的肌肉结构、信号幅值和动作习惯差异很大，导致只在单个受试者上训练的模型难以迁移。论文希望回答三个问题：不同时间建模架构在动态肌电回归中的表现如何，如何依据肌电的时间相关性选择感受野，以及多任务学习、迁移学习和少样本元学习能否在减少校准数据的同时保持精度和轻量化部署能力。

## 方法

论文在 Ninapro DB8 上比较 RNN、LSTM、TCN、Transformer 和神经常微分方程模型，并通过肌电自相关估计合适的时间感受野。针对跨受试者泛化，分别评估多任务学习、迁移学习、FOMAML/Reptile 等一阶元学习，以及只更新少量参数的 LoRA/适配器方案。连续手指位置预测采用 MAE 等指标评价；模型还从参数量、乘加运算量、感受野和存储占用角度分析嵌入式部署代价。

## 实验与结果

基准结果显示，TCN 在动态回归中表现稳定；摘要报告多任务/迁移设置的 MAE 可低于 5.4，少样本元学习约为 6.47。全文实验中，受试者专属优化 TCN 的 MAE 为 5.45±1.06，跨受试者 TCN、LSTM 和 NODE 分别约为 5.70、5.57 和 6.86；结合 LoRA 的多任务方案最低约为 5.33，二次样本元学习约为 6.55，一次样本元学习约为 8.50。TCN 约含 5.8 万参数、1.8–2.0 MMAC、感受野约 475 个时间步，存储约 240 KB；NODE 约 4.9 万参数、约 200 KB，说明轻量模型可以在较低部署成本下获得跨受试者能力。

## 贡献与局限

论文提供了动态肌电人机交互的统一架构基准，并把时间感受野选择、跨受试者训练和轻量化适配放在同一实验框架中，给出了从精度到资源占用的可复现实证。局限在于 Ninapro DB8 的受试者多样性和截肢者覆盖仍有限，实验可能受到会话时间特征和数据分布的影响；真实设备中的电极移动、噪声和长期漂移尚未充分验证。后续需要扩大真实用户和场景测试，并研究更稳健的在线校准与持续适配机制。

---
DOI: 10.1109/tnnls.2026.3662308
