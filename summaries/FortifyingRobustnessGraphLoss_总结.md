# Fortifying Robustness in Graph Neural Networks: A Loss Correction Approach to Mitigate Label Noise 总结

## 基本信息

- **标题**: Fortifying Robustness in Graph Neural Networks: A Loss Correction Approach to Mitigate Label Noise
- **作者**: I-Chung Hsieh、Cheng-Te Li
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3661886
- **arXiv**: 无
- **PDF**: [NN_2026_FortifyingRobustnessGraphLoss.pdf](papers/NN_2026_FortifyingRobustnessGraphLoss.pdf)

## 一句话概括

本文提出抗噪图神经网络 NomiGNN，通过估计节点与边标签噪声、修正损失并引入伪边标签学习，提升 GNN 节点分类在标签和边同时受污染时的鲁棒性。

## 问题与动机

图神经网络同时聚合节点特征与邻接关系，标签噪声不仅会误导节点分类损失，还可能通过消息传递沿错误边扩散。已有鲁棒 GNN 多聚焦节点标签，较少处理边关系被噪声破坏以及两类噪声之间的耦合。作者因此希望在不依赖干净标签的前提下，同时估计噪声分布并抑制错误聚合。

## 方法

NomiGNN 采用“噪声估计—鲁棒微调”的迭代框架。模型先利用预测置信度估计节点标签转移矩阵，并由节点标签概率推导边一致性标签的噪声转移矩阵；随后在节点分类之外增加边标签预测任务，用经逆转移矩阵修正的损失联合训练。方法还利用高置信度预测生成伪边标签，并在每轮微调后重新估计噪声，使估计误差逐步降低。理论分析表明，边标签损失可以对节点标签损失形成上界，为联合任务设计提供依据。

## 实验与结果

实验覆盖 Cora、Citeseer、Polblogs、ACM、DBLP、Pubmed、Ogbn-arxiv，以及低同质性的 Wisconsin、Chameleon 和 Squirrel 等图数据集。作者把 NomiGNN 嵌入 GCN、GraphSAGE、GIN、GAT、GCNII、LafAK-D、NRGNN、ProGNN 等八类基线进行节点分类比较，并构造节点标签、边标签、联合标签、对抗边和非均匀标签等噪声。结果显示，NomiGNN 在多种真实图和异质图上都比对应基线更能保持分类性能；Cora 上的对比还表明，伪边标签和损失修正共同改善了噪声边场景下的表现。

## 贡献与局限

- 提出同时面向节点标签噪声与边关系噪声的 NomiGNN 框架。
- 将边一致性预测、损失修正、伪边标签和迭代噪声估计结合起来，并给出边损失约束节点损失的理论解释。
- 在同质与异质图、不同噪声类型及多个 GNN 骨干上验证了鲁棒性。
- 局限：方法需要估计噪声转移矩阵和设置伪边标签阈值；当图结构极度异质、类别极不平衡或噪声并非近似可建模的标签转移时，估计误差及计算开销仍可能限制效果。

---
DOI: 10.1109/tnnls.2026.3661886
