# Fine-Grained Detection and Analysis of Unknown Encrypted Malicious Traffic From Mixed Noisy Labels 总结

## 基本信息

- **标题**: Fine-Grained Detection and Analysis of Unknown Encrypted Malicious Traffic From Mixed Noisy Labels
- **作者**: Qianwei Meng, Qingjun Yuan, Meng Shen, Siqi Lu, Guangsong Li, Jing Tao, Yong Yu, Yongjuan Wang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3697849
- **arXiv**: 无
- **PDF**: [TDSC_2026_FineGrainedDetectionAnalysis.pdf](papers/TDSC_2026_FineGrainedDetectionAnalysis.pdf)

## 一句话概括

Sieve 面向混合标签噪声下的加密恶意流量，先校正闭集与开放集噪声，再用紧凑特征空间中的 Mahalanobis 距离发现未知威胁，并通过半监督聚类更新流量类别。

## 问题与动机

网络入侵检测依赖高质量标签，但真实流量数据既可能把已知类别错误标注，也可能把未知攻击误当作已知类别，混合噪声会扭曲决策边界并造成安全漏报。加密流量又缺少可直接检查的载荷内容，使传统基于规则或明文特征的方法难以工作。作者希望在标签不可靠的情况下，同时保持已知流量分类能力、发现未知威胁，并形成可持续更新的数据闭环。

## 方法

Sieve 包含三个协同模块。噪声标签校正模块利用邻域一致性和预测置信度，筛除混合噪声并逐步扩展可信样本子集；未知流量检测模块在净化后的紧凑特征空间中计算 Mahalanobis 距离，以区分已知分布和开放集流量；未知流量标注模块使用半监督聚类估计未知类别数量、形成新簇并辅助数据集更新。训练中还结合对比学习，强化抗噪特征表示，避免错误标签继续把不同攻击类型拉到一起。

## 实验与结果

在四个公开数据集上的评估显示，Sieve 在已知类别分类和未知威胁检测上均优于对比方法。Mal_TLS2023 在 50% 噪声条件下准确率和 F1 均超过 94%；在 Mal_TLS2023 与 DDoS2019 的高噪声开放集实验中，F1 分别保持在 97% 和 98% 以上。消融实验表明，去除标签校正、子集扩展或对比损失都会造成性能下降；未知流量聚类能够较好恢复攻击类别结构，但在某些数据上仍会把一个真实攻击类别拆成多个簇。

## 贡献与局限

贡献在于把混合噪声校正、开放集检测和未知类别聚类串成完整的加密流量分析流程，并用理论分析和多数据集实验验证其抗噪性。局限是未知流量由外部数据集类别模拟，未完全复现真实世界中分散、渐变和协议交织的未知攻击；聚类过度分割时仍需额外合并，概念漂移下的持续更新也未充分评估。后续应研究基于簇间距离的自动合并、渐进式漂移适应及更复杂的混合噪声生成机制。

---
DOI: 10.1109/tdsc.2026.3697849
