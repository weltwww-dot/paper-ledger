# Redundancy Removal and Knowledge Alignment-Based Personalized Federated Learning for Online Condition Monitoring

## 基本信息

- **标题**: Redundancy Removal and Knowledge Alignment-Based Personalized Federated Learning for Online Condition Monitoring
- **作者**：Jinsheng Ji、Hongqun Li、Kai Xian Lai、Yuanjin Zheng、Xudong Jiang
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3663653
- **arXiv**：无
- **PDF**：[NN_2026_RedundancyRemovalKnowledgeAlignment.pdf](papers/NN_2026_RedundancyRemovalKnowledgeAlignment.pdf)

## 一句话概括

本文提出 FedRRKA 个性化联邦学习框架，以最大化客户模型的信息量、最小化模型知识冗余，并通过空间—逻辑知识对齐和隐私隔离分支改善高压设备局部放电在线监测。

## 问题与动机

高压开关设备的局部放电监测需要持续采集和快速判断，但原始信号集中传输会引发隐私和数据安全问题，客户之间的非独立同分布数据又会使简单 FedAvg 聚合丢失个性化知识。仅按客户本地性能加权可能重复聚合相似信息，且全局模型与本地分类头之间存在表征不一致。论文希望在不共享原始数据的前提下，选择更有信息量且更互补的客户模型，并让全局模型保留本地结构知识，同时支持不宜参与共享更新的隐私隔离客户。

## 方法

框架采用叶客户—分支客户—中心服务器三级结构。叶客户使用六层 CNN，并把上一轮本地调优模型的特征与空间激活图作为知识对齐目标，通过特征方向和空间图差异约束当前全局模型。服务器端的冗余移除模块用 Fisher 信息迹估计客户模型的信息量，再以 512 维识别特征的核密度估计互信息量化客户间冗余，使用贪心选择同时追求高信息量和高多样性的模型权重。对于隐私隔离客户，分支模型以全局模型为教师，结合软标签和空间—逻辑知识蒸馏获得共享知识而不直接参与全局聚合；局放信号先经 STFT、KPCA、聚类和人工标注转为 32×32 PRPD 图像。

## 实验与结果

实验使用 23,175 个真实局部放电 PRPD 图像，并在 Fashion-MNIST、CIFAR-10 和 CIFAR-100 上验证泛化性；20 个客户每轮本地训练 5 个 epoch，共 40 轮通信。信号—噪声分离模块的 CIoU 达到 0.969；CIFAR-100 消融中，冗余移除相较只按评估分数聚合提升约 0.43 个百分点。空间—逻辑对齐在局放、CIFAR-10 和 CIFAR-100 的隐私隔离分支上分别带来约 2.5、1.3 和 1.8 个百分点的提升。FedRRKA 在局放数据的不同非独立同分布程度和客户在线率设置下均取得最高准确率，在 Fashion-MNIST 多数场景以及 CIFAR-10/100 各设置中也整体优于对比方法；客户端单次前向约 15.65 MFLOPs，适合边缘部署。

## 贡献与局限

论文将信息量—冗余联合聚合、空间—逻辑知识对齐和隐私隔离分支整合到个性化联邦监测框架中，既改善异质客户的个性化性能，也降低了不活跃客户和知识重复带来的影响。局限在于模型投毒、梯度泄露等高级攻击尚未被充分处理，服务器端互信息计算和贪心选择会随客户规模增加而产生额外开销；实验主要使用图像分类数据，未充分覆盖真实工业时间序列和多模态输入。后续需要加强隐私保护、扩大可扩展性并支持持续学习。

---
DOI: 10.1109/tnnls.2026.3663653
