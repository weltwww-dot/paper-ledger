# Silent Poisoning: A Stealthy and Unified Dual-Space Framework for VFL Backdoor Attacks 总结

## 基本信息

- **标题**: Silent Poisoning: A Stealthy and Unified Dual-Space Framework for VFL Backdoor Attacks
- **作者**: Qiao Li, Xiaoya Ma, Zijun Zhang, Jing Chen, Kun He, Ruiying Du, Zijian Zhang, Cong Wu, Yang Liu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3705642
- **arXiv**: 无
- **PDF**: [TDSC_2026_SilentPoisoningStealthyUnified.pdf](papers/TDSC_2026_SilentPoisoningStealthyUnified.pdf)

## 一句话概括

论文系统分析纵向联邦学习中的干净标签后门风险，在输入空间和潜空间分别设计攻击，并用 VFL 特有的隐蔽性指标与正则约束提高攻击效果和难检测性。

## 问题与动机

纵向联邦学习的参与方只持有同一批样本的不同特征，通常无法看到标签，也只能控制本地输入或上传表示，因此水平联邦学习中的许多后门方法不能直接迁移。攻击者仍可能通过训练梯度影响输入—标签关系或把局部嵌入推向目标类别表示。作者希望回答在不改标签、不依赖代理模型的情况下，VFL 是否仍存在高效且隐蔽的干净标签后门，并建立可量化的检测风险指标。

## 方法

框架包含输入空间攻击 IASR 和潜空间攻击 LAEO。IASR 利用标准 VFL 训练中可获得的梯度信息，在线替换或微调少量本地输入，重塑输入与目标标签的关联；LAEO 直接优化被动方上传的局部嵌入，使其靠近目标类表示。两者都加入统一的隐蔽性正则项，约束恶意表示与正常表示的统计差异，并定义攻击隐蔽性 AS 指标衡量攻击效果与可检测性的权衡。论文在不同聚合方式、参与方数量、噪声标签和常见服务器侧检测下进行评估。

## 实验与结果

在 CIFAR-10、CIFAR-100、CINIC-10 以及 BHI、BM 等图像和表格数据上，IASR 与 LAEO 在保持较高干净准确率的同时取得高攻击成功率；潜空间 LAEO 通常比输入空间方法更隐蔽。在投毒率仅 0.5% 或 0.05% 时，IASR 的 ASR 超过 84%，LAEO 超过 95%；即使只有 1 个目标类样本，LAEO 在 CIFAR-10 上仍达到 68.25% ASR，5 个样本时升至 88.50%。在 4 或 8 个被动参与方以及拼接、逐元素求和、平均等聚合方式下，LAEO 仍保持较强稳定性；但推理时嵌入扰动系数达到 1 时，CIFAR-10 ASR 会降至 25% 以下。

## 贡献与局限

贡献在于把 VFL 后门攻击的输入空间和潜空间统一起来，并提出面向分裂模型结构的隐蔽性度量与正则化，揭示了无标签访问条件下的供应链风险。局限是攻击假设对方能获得少量目标类干净样本，参与方数量、模型异质性和聚合方式变化会影响效果；论文结果应仅用于获授权的安全评估与防御研究，不应转化为未授权投毒。后续可研究更强的表示异常检测、鲁棒聚合和面向多方异质架构的防御方法。

---
DOI: 10.1109/tdsc.2026.3705642
