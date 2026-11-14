# Non-Negative Tensor Factorization Based Bi-Clustering on Anchor Graphs 总结

## 基本信息
- **标题**: Non-Negative Tensor Factorization Based Bi-Clustering on Anchor Graphs
- **作者**: Quanxue Gao、Rui Wang、Jing Li 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15252-15266
- **发表**: 2026-08-14
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3724177

## 一句话概括
该方法对多视图锚图进行非负张量分解，同时学习样本与锚点簇结构，以实现数据层和决策层融合。

## 问题与动机
如何在多视图聚类中显式利用不同视图锚图间的数据层关系，并让样本标签和锚点标签都具有可解释的分解含义？

## 方法
方法将各视图锚图张量化，以正交非负张量分解得到锚点指示张量与样本指示张量，并在两者上加入低秩张量 Schatten-p 正则项；模型还可结合去噪锚图，联合利用跨视图互补结构和决策层标签信息。

## 实验与结果
研究在十个多视图基准数据集上与矩阵分解及其他聚类方法比较。相对另一种张量分解方法 Orth-NTF，ACC 在 Scene15、Reuters、NUS、AWA 和 NoisyMNIST 分别提高 0.167、0.132、0.152、0.430 和 0.137（PDF 第 9 页）；打乱数据顺序的诊断实验显示方法仍具竞争力，但张量运算使其比简单矩阵分解基线更耗时（PDF 第 11–12 页）。

## 贡献与局限
贡献是将样本和锚点的聚类结构一并纳入跨视图非负张量分解，并赋予分解结果概率解释。局限是 FFT 和 Schatten-p 正则带来额外计算成本；旋转张量构造对样本顺序可能敏感，打乱顺序的结果因此需要谨慎解释（PDF 第 12 页）。

---
DOI: 10.1109/tpami.2026.3724177
