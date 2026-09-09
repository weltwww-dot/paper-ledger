# Causality-Preserving Domain Generalization via Adaptive Fourier Mixup for RUL Prediction 总结

## 基本信息

- **标题**: Causality-Preserving Domain Generalization via Adaptive Fourier Mixup for RUL Prediction
- **作者**: Yifan Zhu、Wenyu Chen、Zhe Cheng、Fode Zhang、Zhisheng Ye
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3688520
- **arXiv**: 无
- **PDF**: [TPAMI_2026_CausalityPreservingDomainGeneralization.pdf](papers/TPAMI_2026_CausalityPreservingDomainGeneralization.pdf)

## 一句话概括

本文提出 AFM-CIR，将语义相似度引导的自适应傅里叶混合与因果启发回归结合，在没有目标域训练数据的严格域泛化设置下提升剩余寿命预测的跨域可靠性。

## 问题与动机

工业时间序列通常存在传感器、工况和设备环境造成的域偏移，严格域泛化又要求训练阶段完全看不到目标域。普通 ERM 或随机增强可能破坏时间序列的语义和因果关系，导致生成样本标签不一致、跨域性能下降。作者希望在增加频域变化多样性的同时，控制增强对语义和因果结构的破坏。

## 方法

AFM 根据域不变且保持顺序的指导嵌入，按语义相似度自适应选择样本进行傅里叶幅度混合，并使用有界的最短角相位扰动模拟可控的域变化。CIR 通过相关性分解约束表示的不变性和维度间独立性，再用对抗掩码迫使模型依赖具有因果充分性的维度。作者还从互信息和 Lipschitz—谱范数界出发，分析相位干预的可控性和预测一致性。

## 实验与结果

实验覆盖四个常用工业剩余寿命预测数据集，并与 ERM、通用域泛化方法和任务专用域泛化基线比较。AFM-CIR 在四个数据集上均取得具有竞争力的最优或近最优表现，整体优于强基线。消融结果显示，随机配对、仅做幅度增强或不加入因果约束的回归都会削弱性能；超参数分析表明，在该实验中相位控制参数 τ=2、因果权重 κ=0.8、邻居池阈值 η=0.8 时 RMSE 最低，过大的邻居阈值会降低增强多样性，过小则可能引入语义不匹配的相位噪声。

## 贡献与局限

- 将语义保持的频域增强与因果约束统一到严格时间序列域泛化框架中。
- 通过自适应幅度混合和有界相位干预生成更可控的跨域样本。
- 以相关性分解和对抗掩码增强表示不变性、维度独立性与因果充分性。
- 局限：方法包含多个增强和正则化超参数，对参数尺度和邻居质量较敏感；当前验证集中于 RUL 回归，向分类、预测等其他时间序列任务的迁移仍待研究。

---
DOI: 10.1109/tpami.2026.3688520
