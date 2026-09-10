# Multi-modal contrastive learning based on molecular and textual data for drug response prediction 总结

## 基本信息

- **标题**: Multi-modal contrastive learning based on molecular and textual data for drug response prediction
- **作者**: Meiyu Duan, Xiaobo Li, Xiaodi Hou, Yanchen Qu, Hai Cui, Yijia Zhang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108882
- **arXiv**: 无
- **PDF**: [NN_2026_MultiModalContrastiveDrugResponse.pdf](papers/NN_2026_MultiModalContrastiveDrugResponse.pdf)

## 一句话概括

论文提出多模态对比学习方法，将生物医学文本、分子属性和药物—细胞结构关系统一用于药物反应预测。

## 问题与动机

现有方法多依赖分子特征，忽略文本语料中的生物学知识，也没有充分融合属性表示与结构表示。作者希望把互补知识纳入同一语义空间，以提高精准用药相关预测。

## 方法

模型从权威数据库获取生物通路和分子机制文本，从多组学特征与药物分子图获得属性表示，并用异构图神经网络编码药物—细胞系交互结构。跨模态和模态内对比学习分别对齐文本—属性、属性—结构表示。

## 实验与结果

在 GDSC 和 CCLE 数据集上的实验表明，所提模型优于文中比较的现有先进药物反应预测方法。论文同时提供了代码和数据链接，摘要未给出具体指标数值。

## 贡献与局限

贡献是把权威生物医学文本与双视图分子/交互表示结合，并用对比目标完成协同学习。局限是结果受数据库覆盖、分子图质量和细胞系分布影响，向真实患者反应外推仍不能由这些数据直接保证。

---
DOI: 10.1016/j.neunet.2026.108882
