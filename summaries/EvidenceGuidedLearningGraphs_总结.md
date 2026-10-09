# Evidence-guided Learning against Noisy and Sparse Labels on Graphs 总结

## 基本信息

- **标题**: Evidence-guided Learning against Noisy and Sparse Labels on Graphs
- **作者**: Siyu Yi, Wei Zhang, Zhengyang Mao, Yongdao Zhou, Ziyue Qiao, Li Shen, Dacheng Tao, Jiancheng Lv, Wei Ju
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-02
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104608
- **arXiv**: 无
- **PDF**: [AIJ_2026_EvidenceGuidedLearningGraphs.pdf](papers/AIJ_2026_EvidenceGuidedLearningGraphs.pdf)

## 一句话概括

EvGNN 将多专家证据融合、不确定性建模和未标注节点利用结合起来，使图神经网络能在标签稀少且含有错误标注时进行更可靠的节点分类。

## 问题与动机

现实图数据的人工标注成本高、错误难以避免，而标准 GNN 往往假设标签充足且可靠，容易把噪声监督记入模型。直接借用视觉任务中的样本筛选或标签修正方法，又不能充分利用节点间的结构关系。本文同时处理标签噪声与标签稀疏，并关注多个专家意见相互冲突时，普通证据融合可能产生错误的高置信预测这一问题。

## 方法

各专家以 Dirichlet 分布表达类别证据，分别估计信念与不确定性；融合前结合 Jensen–Shannon 散度和质量熵评估专家之间的一致性与信息量，先计算加权意见，再应用 Dempster 组合规则，减弱直接合并冲突证据的问题。框架同时进行表征层和决策层融合，通过一致性正则与高置信伪标签利用未标注节点。对真实标签采用证据监督，对筛选后的伪标签采用交叉熵，使抵抗错误标注与补充监督发挥互补作用。理论结果给出了特定条件下的信念、不确定性及错误融合概率界，而非无条件的正确分类保证。

## 实验与结果

主实验覆盖 Coauthor CS、Amazon Photo、Amazon Computers、Pubmed、DBLP 和 Citeseer 六个节点分类基准，注入均匀噪声和成对噪声，与 GCN、NRGNN、RTGNN、CR-GNN 等方法比较；默认噪声率为 20%，标注节点约占全图 1% 或 5%，各设置重复五次。EvGNN 在多数设置取得最佳结果，并非所有设置均排名第一。消融表中，完整模型在 Pubmed 的两类噪声下均达到 81.2% 准确率；在 Citeseer 的均匀噪声下达到 72.7%。移除融合、一致性学习或伪标签后性能下降，支持这些组件的作用；另外评估了异配图、校准误差和加入高斯扰动的分布外节点。

## 贡献与局限

主要贡献是面向稀疏、含噪标签的图学习整合多专家证据建模，并为冲突意见融合提供机制与条件性理论分析，同时利用未标注节点补充监督。作者明确指出：专家数量仍需经验设定，缺少自适应选择机制；专家表征之间的交互还可以更灵活，高置信错误伪标签也未被根除。实验包含异配图，因此不能简单把局限概括为“只适用于同质图”；更准确的边界是现有图基准、模拟噪声和特定专家配置下的验证尚不足以覆盖所有现实标注机制。

---
DOI: 10.1016/j.artint.2026.104608
