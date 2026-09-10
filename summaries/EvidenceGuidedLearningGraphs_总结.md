# Evidence-guided Learning against Noisy and Sparse Labels on Graphs 总结

## 基本信息

- **标题**: Evidence-guided Learning against Noisy and Sparse Labels on Graphs
- **作者**: Siyu Yi, Wei Zhang, Zhengyang Mao, Yongdao Zhou, Ziyue Qiao, Li Shen, Dacheng Tao, Jiancheng Lv, Wei Ju
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104608
- **arXiv**: 无
- **PDF**: [AIJ_2026_EvidenceGuidedLearningGraphs.pdf](papers/AIJ_2026_EvidenceGuidedLearningGraphs.pdf)

## 一句话概括

EvGNN 用主观逻辑和 Dempster–Shafer 证据理论量化多专家的不确定性，并通过一致性学习和伪标签利用图中的稀疏、噪声标签。

## 问题与动机

真实图数据的节点标签可能错误且昂贵，直接训练 GNN 容易过拟合并泛化不佳。相比视觉领域，图上的噪声标签与稀疏监督问题研究不足，尤其需要同时抵抗噪声并利用未标注节点。

## 方法

EvGNN 采用多专家框架，用主观逻辑和 Dempster–Shafer 证据理论为每个专家提供证据并量化不确定性。作者设计冲突条件下的融合策略，并加入一致性学习和伪标签正则化，将未标注节点转化为辅助监督。

## 实验与结果

论文在真实世界数据集上进行广泛实验，结果支持 EvGNN 在稀疏、噪声标签条件下的有效性。全文重点比较多专家证据融合、未标注节点利用和各正则项的作用，未在摘要中给出统一数字。

## 贡献与局限

贡献是把证据不确定性建模与图半监督学习结合，并专门处理专家冲突。局限是伪标签和证据融合仍依赖模型校准及图同质性假设，标签噪声机制变化或严重异质图上的表现需继续评估。

---
DOI: 10.1016/j.artint.2026.104608
