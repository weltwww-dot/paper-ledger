# Weighted UnLearning from Experience for Improved Spurious Correlation Robustness 总结

## 基本信息
- **标题**: Weighted UnLearning from Experience for Improved Spurious Correlation Robustness
- **作者**: Jeff Mitchell、Jesus Martinez-del-Rincon、Niall McLaughlin
- **期刊 / 会议**: Machine Learning 2026
- **卷期 / 文章号**: 115:251
- **发表**: 2026-10-20
- **日期来源**: Crossref published-online；不以PDF收稿、修回或录用日期替代
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07164-1
- **PDF**: [ML_2026_WeightedUnlearningSpuriousCorrelations.pdf](papers/ML_2026_WeightedUnlearningSpuriousCorrelations.pdf)

## 一句话概括
wULE按样本是否可能含有伪相关，分别加权分类和显著性约束，避免去偏模型对所有样本都被迫偏离偏置模型。

## 问题与动机
模型可能利用背景等偶然线索完成训练任务，却在相关性失效的群体上表现较差。原ULE对所有样本施加相同的去偏要求，也可能妨碍对不含伪相关样本的正常学习。

## 方法
并行训练偏置模型和去偏模型，用输入梯度显著性约束引导后者避免依赖前者关注的特征。通过JTT式早期分类表现或SPARE式聚类估计伪相关样本集合，再按集合分别调整分类项与显著性项；早期训练后冻结偏置模型，推理只使用去偏模型。

## 实验与结果
在Waterbirds、CelebA、UrbanCars和MultiNLI上评估。表7中，UrbanCars最差群体准确率由ULE的71.6%升至76.2%，但平均准确率由98.2%降至96.6%；Waterbirds最差群体准确率为89.8%，仍低于SPARE的91.6%（PDF第22页）。因此最弱群体改善不等于平均性能或所有基准均最优。

## 贡献与局限
将逐样本加权引入ULE，明确区分可能含伪相关与不含伪相关的训练样本。常规训练估计群体而不依赖真实训练群体标签，但验证集群体标签仍用于调参和早停，不能称完全无群体标注。效果依赖早期偏置及群体估计，错误识别伪相关时可能失效；Oracle结果还额外假设真实群体信息已知（PDF第6—8、11、21—23页）。

---
DOI: 10.1007/s10994-026-07164-1 | PDF: [ML_2026_WeightedUnlearningSpuriousCorrelations.pdf](papers/ML_2026_WeightedUnlearningSpuriousCorrelations.pdf)
