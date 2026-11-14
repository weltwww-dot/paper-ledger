# Are We Really Making Much Progress in Text Classification? A Comparative Review 总结

## 基本信息
- **标题**: Are We Really Making Much Progress in Text Classification? A Comparative Review
- **作者**: Ansgar Scherp、Andor Diera、Fabian Karl 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，7959-7978
- **发表**: 2026-09-21
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3735248
- **PDF**: [TKDE_2026_text-classification-comparative-review_3735248.pdf](papers/TKDE_2026_text-classification-comparative-review_3735248.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
文本分类方法不断增加，但论文报告的数字常因数据处理、超参数和实现差异而不可直接比较。本文综述单标签、多标签与层次文本分类，并对词袋、序列、图及层次方法作定量比较，重点检视图方法和生成式语言模型是否带来可复现的进步。

## 问题与动机
在统一的比较视角下，近年文本分类方法相对强基线究竟进步多少，训练式模型与少样本生成模型各适用于什么条件？

## 方法
作者系统梳理不同任务和方法谱系，并在多个公开数据集上复现实验比较；同时分析文献中同模型同数据集结果的离散度及微调学习率等因素的影响。综述据此归纳数据量、微调与上下文少样本学习对性能的关系。

## 实验与结果
定量比较发现，图方法在多数评测数据集上未超过微调 Transformer；有足够训练数据时，微调语言模型通常胜过 decoder-only 生成模型的少样本上下文学习，而所需数据量依任务而异。文献中同一 BERT 及相同数据划分的准确率差异最高约 13 个百分点，学习率等设置会影响结论（PDF 第 3 页）。综述覆盖范围、语言及生成模型训练数据泄漏均限制外推。

## 贡献与局限
贡献是把多个分类任务和方法类别放入共同评测，并强调强基线与调参规范对判断真实进步的重要性。作者建议数据充足时微调语言模型，数据有限时考虑冻结生成模型的少样本方案；结果不应被视为对未覆盖语言和数据集的普遍定论。

---
DOI: 10.1109/tkde.2026.3735248 | PDF: [TKDE_2026_text-classification-comparative-review_3735248.pdf](papers/TKDE_2026_text-classification-comparative-review_3735248.pdf)
