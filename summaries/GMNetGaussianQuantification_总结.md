# Quantification via gaussian latent space representations 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Quantification via gaussian latent space representations
- 作者：Olaya Pérez-Mon, Juan José del Coz, Pablo González
- 期刊 / 年份：Neural Networks / 2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108886
- PDF：[GMNetGaussianQuantification.pdf](papers/GMNetGaussianQuantification.pdf)

## 一句话概括

GMNet在潜在空间中用多元 Gaussian 表示样本 bag 的联合分布，并直接针对 quantification 任务损失进行训练，以估计未知样本集中的类别比例。

## 问题与动机

Quantification 需要估计未标注样本集合中各类别的 prevalence，传统方法通常依赖分类器输出或 prior probability shift 假设。独立逐特征的直方图难以表达特征间关系，论文因此寻求一种对样本顺序不敏感、能保留潜在空间联合结构、并可直接优化任务损失的 bag 表示。

## 方法

GMNet包含 bag representation module（BRM），把输入 bag 投影到多个 latent spaces，并在每个空间用 multivariate Gaussian 建模特征联合分布，再融合这些分布表示完成 prevalence 预测。模型端到端按任务训练，可分别优化 T1B/T2 的 RAE 或有序 quantification 任务 T3 的 NMD；文中还使用 CKA 正则化鼓励潜在空间提供互补信息。

## 实验与结果

论文在 LeQua 的 T1B、T2、T3 基准以及 CIFAR-10 和 CIFAR-100 coarse 上评估。GMNet在 T1B、T2 上取得文中报告的 state-of-the-art，并在 T3 的 NMD 目标上有效；在 CIFAR-10/CIFAR-100 上 RAE 分别为 0.1684±0.123 和 0.3884±0.2331，优于表中其他方法。代价是训练时间较长，但推理时间与其他深度 quantifier 差异不大；K、L 扫描显示模型对多种配置较稳健。

## 贡献与局限

论文提出以多元 Gaussian 捕获潜在特征依赖的 BRM，支持直接损失优化、有限数据训练和无 example-labeled data 场景，并验证了其在多类 quantification 中的优势。局限包括训练成本较高、对数据生成协议和特征提取器仍敏感，且对非 prior probability shift、其他集合任务及更大规模数据的适用性尚待验证。

DOI: 10.1016/j.neunet.2026.108886
