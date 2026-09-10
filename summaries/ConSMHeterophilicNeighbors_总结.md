# Identifying heterophilic neighbors via confidence-based subgraph matching for graph neural networks 总结

## 基本信息

- **标题**: Identifying heterophilic neighbors via confidence-based subgraph matching for graph neural networks
- **作者**: Yoonhyuk Choi, Chong-Kwon Kim
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104575
- **arXiv**: 无
- **PDF**: [AIJ_2026_ConSMHeterophilicNeighbors.pdf](papers/AIJ_2026_ConSMHeterophilicNeighbors.pdf)

## 一句话概括

ConSM以2-hop子图结构和最优传输估计边置信度，再用符号感知标签传播选择性传递消息，以提升GNN在异配图上的鲁棒性。

## 问题与动机

许多GNN默认相邻节点同质，因而在邻居标签不同的异配图上错误聚合信息并产生过平滑。现实网络中的社交、物理和生物关系往往并不满足同质性假设，需要识别有用、误导或与任务无关的边。

## 方法

ConSM分为两阶段：先比较节点2-hop邻域的结构相似性，以最优传输计算边系数，并依据可调置信比率识别边作用；再将系数纳入符号感知标签传播，按置信度鼓励或抑制消息传递。论文还提出无需人工搜索的置信比率自适应策略。

## 实验与结果

新增实验覆盖近期异配导向基线以及更大、无数据泄漏的数据集。结果显示ConSM提升分类准确率、缓解过平滑，并在同配和异配两类设置中保持有效。

## 贡献与局限

贡献是用局部子图结构而非单条边属性判断邻居作用，并将置信度用于有符号传播。局限是最优传输与2-hop构图会增加成本，置信度假设在噪声边、动态图和极大规模图上的稳定性仍需评估。

---
DOI: 10.1016/j.artint.2026.104575
