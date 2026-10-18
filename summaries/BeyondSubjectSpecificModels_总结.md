# Beyond Subject-Specific Models in Dynamical Human--Machine Interaction: Benchmarking and Optimization Strategies 总结

## 基本信息

- **标题**: Beyond Subject-Specific Models in Dynamical Human--Machine Interaction: Benchmarking and Optimization Strategies
- **作者**: Luca Manneschi, Matthew O. A. Ellis, Elisa Donati
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems · 2026
- **发表**: 2026-09
- **日期来源**: crossref-published，保留来源精度；预印本日期不替代期刊发表时间
- **内容状态**: 完整 · 已对照现有PDF审校中文六段式；版本按本条记录
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3662308
- **版本**: 出版社正式正文（含内容已定稿的Early Access）
- **PDF**: [NN_2026_BeyondSubjectSpecificModels.pdf](papers/NN_2026_BeyondSubjectSpecificModels.pdf)

## 一句话概括

论文以连续肌电到手指位置的回归任务为基础，比较时序模型及跨受试者适配策略，减少逐人训练的依赖。

## 问题与动机

连续控制比离散手势分类更接近自然运动，但必须兼顾时间建模、个体差异和实时性。只为单个受试者训练模型会增加校准与部署成本。

## 方法

在Ninapro DB8上比较RNN、TCN、Transformer和神经常微分方程模型，依据肌电自相关调节感受野。再比较多任务、迁移及元学习，并引入LoRA和适配器等轻量微调。

## 实验与结果

正文报告受试者专属TCN的MAE为5.45±1.06，多任务加LoRA的最低MAE为5.33。这两项来自不同训练配置，不能把它们当作同一基线上的提升；作者还比较适配数据量及资源开销。

## 贡献与局限

贡献是把架构选择、跨受试者训练和轻量适配纳入统一评测。数据集和真实用户覆盖仍有限，尤其不能直接把结果外推为截肢者、长期佩戴或临床部署效果。

---
DOI: 10.1109/tnnls.2026.3662308 | PDF: [NN_2026_BeyondSubjectSpecificModels.pdf](papers/NN_2026_BeyondSubjectSpecificModels.pdf)
