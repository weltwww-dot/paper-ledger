# CASE: Contrastive Activation for Class-Sensitive Explanations 总结

## 基本信息
- **标题**: CASE: Contrastive Activation for Class-Sensitive Explanations
- **作者**: Dane Williamson、Yangfeng Ji、Matthew Dwyer
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-26
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07169-w
- **PDF**: [ML_2026_CASEClassSensitiveExplanations.pdf](papers/ML_2026_CASEClassSensitiveExplanations.pdf)

## 一句话概括
CASE 通过对比同一输入在不同候选类别下的激活，检验并增强显著性解释对类别差异的敏感程度。

## 问题与动机
显著性图看起来合理，不代表它解释了模型为何选择某类别；不同类别可能得到近乎相同的热图，使通用显著区域被误当成类别特定依据。作者因此提出类敏感性诊断。

## 方法
研究先在多个卷积架构和自然图像数据集上比较常见显著性方法在竞争类别下生成的解释，再提出 Contrastive Activation for Class-Sensitive Explanations（CASE），突出区分目标类与竞争类的输入特征，并用类别特异性和扰动保真度等指标评估。

## 实验与结果
作者发现多种显著性方法对同一图像的不同类别给出近似解释，该现象跨多个架构和数据集存在。CASE 提高了类别特异性，同时在论文采用的扰动保真度评估中保持竞争力。

## 贡献与局限
- 将类别敏感性作为显著性解释的显式诊断维度，区分视觉合理性与类别决策解释。
- 提出对比激活方法，并在图像分类中评估类别区分能力。
- 证据主要来自单标签自然图像和特定解释指标；不能直接推广到文本、多标签或临床场景，指标改善也不等于用户决策质量提升。

---
DOI: 10.1007/s10994-026-07169-w
