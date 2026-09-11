# Generalized context in cross attention for transfer learning of disjoint tabular data

## 基本信息

- 标题: Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data
- 作者: Kazi F. Akhter, Ibna Kowsar, Manar D. Samad
- 期刊 / 会议: Neural Networks 2027
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1016/j.neunet.2026.109568
- PDF: [NN_2026_GeneralizedContext.pdf](papers/NN_2026_GeneralizedContext.pdf)

- 标题: Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data
- 作者: Kazi F. Akhter, Ibna Kowsar, Manar D. Samad
- 期刊 / 会议: Neural Networks 2027
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

作者为 Kazi F. Akhter、Ibna Kowsar、Manar D. Samad；发表于 *Neural Networks* 205 (2027) 109568。论文研究没有共享特征的异构表格数据跨域迁移，提出 generalized context learning 和 Cross-domain Attention Transfer Learning（CATTLE）。DOI: 10.1016/j.neunet.2026.109568
## 一句话概括

CATTLE 不再把源域与目标域共享特征作为迁移前提，而是从 Transformer 的 key/value/query 投影权重提取数据无关的广义上下文，并把它迁移到不相交表格的目标分类任务。

## 问题与动机

表格数据同时包含数值、类别、序数和文本特征，不同领域的列结构与语义往往完全不同；银行交易表与电子病历就很难共享可解释的列。现有 TransTab、XTab 等跨表迁移方法通常依赖特征重叠或多源预训练，通用视觉/语言迁移的共享表示假设也不适用。作者希望只用一个源表学习可迁移规则，并避免源域表示在目标域微调时被覆盖或产生知识冲突。

## 方法

以每个表格特征为 token 的 Transformer 将其投影为 query、key 和 value。不同于从数据激活得到领域特定上下文，CATTLE 直接利用预训练 Transformer 的投影矩阵学习 generalized context：源域 key/value 投影权重与目标域 query 投影权重进行跨注意力交互，选择预训练 gFTT 的高层权重并在目标域冻结，再仅用目标数据训练下游模型。作者比较监督和自监督源域预训练，并通过不同活动层数、随机权重、继续训练权重和直接微调进行消融。

## 实验与结果

实验使用 10 对没有共享特征的源—目标表格数据，比较 9 个机器学习、深度学习和迁移学习基线，包括大规模预训练模型。摘要报告 CATTLE 平均排名 2.9，平均 AUROC 比基线高 3.7%，并在排名和统计检验上优于基线。表格结果显示，CATTLE 在多组任务上超过 XGBoost、TransTab、XTab、CM2 等方法；例如 optdigits→vehicle 的 AUROC 为 0.942，seismic-bumps→cylinder-bands 为 0.856。自监督源预训练通常优于监督版本，且在样本较少的 Cylinder Bands 上超过 XGBoost；消融表明选择合适的高层 key/value 权重、而非随机权重或直接微调，是效果的重要因素。

## 贡献与局限

贡献是提出无需共享特征、可由单一源表获得的表格跨域迁移范式，并把跨注意力从数据激活层面推进到投影权重层面。局限是注意力层选择主要依据经验，缺少关于深层权重知识分布的理论解释；数据集规模与任务类型仍有限，方法对特征编码、源域选择和目标分类设置可能敏感。未来需要系统学习层选择策略，并在更多真实跨行业表格、回归和更强分布偏移上验证。

DOI: 10.1016/j.neunet.2026.109568
