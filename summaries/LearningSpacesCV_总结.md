# Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation 总结

## 基本信息

- 标题: Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation
- 作者: Diego Marcondes、Claudia Peixoto
- 期刊 / 会议: Machine Learning 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1007/s10994-026-07150-7
- PDF: [incremental_e816d2adf30b.pdf](papers/incremental_e816d2adf30b.pdf)

- 标题: Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation
- 作者: Diego Marcondes、Claudia Peixoto
- 期刊 / 会议: Machine Learning 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**: Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation
- **作者**: Diego Marcondes、Claudia Peixoto
- **期刊 / 卷号文章号**: Machine Learning, 115:217 (2026)
- **正式版 PDF**: [incremental_e816d2adf30b.pdf](papers/incremental_e816d2adf30b.pdf)
## 一句话概括

论文为“先用交叉验证选择模型、再在所选模型中学习”的完整流程建立分布无关偏差界，并提出 Learning Spaces 来把领域知识编码进候选模型的偏序结构，从而在候选族与真实目标匹配时改善泛化。

## 问题与动机

交叉验证广泛用于风险估计和模型选择，但把训练、选择和最终学习视为一个整体时，理论性质仍不充分，尤其缺少对候选模型集合如何影响泛化的系统分析。已有候选族往往按复杂度启发式设置，未充分利用“哪些变量可共享效应”或“目标应当稀疏”等先验知识；错误或过弱的候选结构也可能让模型选择失去收益。

## 方法

作者在统计学习理论中定义 target model、交叉验证风险和类型 I–IV estimation errors，并用 VC dimension 推导有界损失下的 deviation bounds；对无界损失，进一步在尾部矩条件下扩展既有结果，得到相对估计误差界。Learning Space 是按模型包含关系反映复杂度的偏序集合，重点研究具有 lattice 结构的候选族；变量选择 Learning Space（VSLS）和 partition lattice Learning Space（PLLS）分别编码稀疏性与变量同效关系。

## 实验与结果

有限域分类实验在 partition lattice 上进行 1,000 次模拟，比较 ERM、独立样本模型选择和复用样本模型选择；模型选择在样本较小、最大判别误差较小的情形更有利，复用方案总体略优于独立样本方案。高维线性回归以稀疏/稠密和系数不等/分组构成四种场景，在 96 次重复、120 秒搜索预算下比较 ERM、LASSO、ridge、VSLS 和 PLLS。与先验结构匹配时，PLLS 或 VSLS 的 type IV error 可比标准方法低多个数量级；例如分组稀疏场景中 PLLS 约比 LASSO 好 15 倍、比 ERM 好 16 倍。先验完全错配时，ERM 在所有组合中占优。

## 贡献与局限

贡献在于把交叉验证模型选择作为统一学习流程给出有界/无界损失理论，并说明候选模型族本身可以成为利用领域知识改善泛化的关键设计对象。局限是分布无关界通常不够紧，未利用不同交叉验证折之间的依赖，不能据此确定最佳折数；搜索算法的计算预算会产生显著 type III error，理论收益在模型族错配或优化失败时不会兑现，且主要假设独立同分布数据，真实任务验证仍需开展。

---
DOI: 10.1007/s10994-026-07150-7
