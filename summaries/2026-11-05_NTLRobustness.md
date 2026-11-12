# Evaluating Parameter-Efficient Fine-Tuning Attacks Against Non-Transferable Learning Defenses 总结

## 基本信息
- **标题**: Evaluating Parameter-Efficient Fine-Tuning Attacks Against Non-Transferable Learning Defenses
- **作者**: Ammara Zamir、Paolo Falcarin、Salvatore Orlando 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105228
- **发表**: 2026-11-05
- **日期来源**: 出版社正式 PDF 首页 Available online，2027 为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105228
- **PDF**: [COSE_2026_NTLRobustness.pdf](papers/COSE_2026_NTLRobustness.pdf)

## 一句话概括
评估非迁移学习防护在参数高效适配下能否持续限制预训练视觉模型的任务迁移。

## 问题与动机
模型发布方有时希望保留模型在原任务上的精度，同时限制它被迁移到指定的新任务。只用常规全量微调检验这种防护，可能高估模型权重的保护效果。

## 方法
作者在统一评估框架下比较不同防护、骨干网络与适配预算，分别记录原任务和目标任务的表现。论文还把稀疏更新作为一类额外的压力测试。

## 实验与结果
实验覆盖 Imagenette、CIFAR10、CINIC10 和 STL10 等数据。多种防护确实压低了常规微调的目标域精度，但较小规模的参数更新在多项对照中恢复了目标域表现（PDF 第 6–8 页）。

## 贡献与局限
结果说明防护评估需要覆盖多种适配预算与策略。实验证据来自选定的视觉数据、网络和白盒权重访问设定，不能直接外推至闭源 API 或其他模态。

---
DOI: 10.1016/j.cose.2026.105228 | PDF: [COSE_2026_NTLRobustness.pdf](papers/COSE_2026_NTLRobustness.pdf)
