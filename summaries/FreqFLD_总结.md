# FreqFLD: Towards All-in-One Facial Landmark Detection via Frequency Modulation 总结

## 基本信息

- **标题**: FreqFLD: Towards All-in-One Facial Landmark Detection via Frequency Modulation
- **作者**: Shun Ren、Kaijie Jin、Shengkai Hu et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109604
- **arXiv**: 无
- **PDF**: [NN_2026_FreqFLD.pdf](papers/NN_2026_FreqFLD.pdf)

## 一句话概括

FreqFLD 通过高低频解耦、频率条件化专家路由和一致性约束，在一个模型中联合学习标注方案不同的多个人脸关键点数据集，并增强复杂场景下的跨数据集泛化。

## 问题与动机

现有人脸关键点检测通常针对单一数据集训练，重复学习相同面部几何结构，维护成本高且跨域泛化有限。多数据集联合训练又会因关键点数量、姿态、表情和遮挡差异产生特征冲突；纯空间域建模也未充分利用面部结构对频率变化的敏感性。

## 方法

Frequency Modulation Module 将特征分解并调制为低频全局结构和高频局部关键点细节，形成频率先验。Frequency-Modulated Mixture-of-Experts 据此前验自适应选择专家；FreqCR 损失约束路由与频率结构保持一致，促进专家均衡利用和稳定专门化。

## 实验与结果

作者在 300W、AFLW、COFW、WFLW 等具有不同关键点标注方案的数据集上进行联合评估。全文报告该统一模型在常用基准上达到具有竞争力的表现，并改善跨场景稳健性；公开代码可用于复现。论文摘要未给出可统一比较的单一提升数字。

## 贡献与局限

贡献是以频率先验协调多数据集共享几何与异质面部模式，形成 All-in-One 关键点检测框架。局限在于专家路由增加结构复杂度，且不同人群、极端遮挡、低分辨率和新标注体系下的公平性与迁移能力仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.109604
