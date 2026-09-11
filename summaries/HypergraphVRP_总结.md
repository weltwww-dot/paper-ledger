# Learning Constraints-Based adaptive hypergraph neural networks for solving vehicle routing problems

## 基本信息

- 标题: Learning Constraints-Based Adaptive Hypergraph Neural Networks for Solving Vehicle Routing Problems
- 作者: Zhenwei Wang, Tiehua Zhang, Jing Liu, Heng Yu
- 期刊 / 会议: Neural Networks 2027
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1016/j.neunet.2026.109565
- PDF: [NN_2026_HypergraphVRP.pdf](papers/NN_2026_HypergraphVRP.pdf)

- 标题: Learning Constraints-Based Adaptive Hypergraph Neural Networks for Solving Vehicle Routing Problems
- 作者: Zhenwei Wang, Tiehua Zhang, Jing Liu, Heng Yu
- 期刊 / 会议: Neural Networks 2027
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

作者为 Zhenwei Wang、Tiehua Zhang、Jing Liu、Heng Yu、Kaizhu Huang、Ruibin Bai；发表于 *Neural Networks* 205 (2027) 109565。论文研究车辆路径问题及其容量、时间窗等复杂约束，提出约束导向的自适应超图神经网络与强化学习联合求解框架。DOI: 10.1016/j.neunet.2026.109565
## 一句话概括

该工作首次将超图学习引入路由求解，用动态超边保留客户组和部分路线的高阶约束语义，再由双指针解码器和强化学习生成满足约束的路线。

## 问题与动机

VRP 的组合解空间巨大，精确模型难以扩展，传统启发式又依赖问题参数和人工算子。多数神经路由方法以成对节点关系为主，但车辆容量、时间窗、路线时长和优先关系是由节点集合及已构造的部分路线共同决定的；把它们拆成独立边会丢失约束群组身份，并可能造成局部最优或不可行解。论文因此把约束诱导的高阶客户群视为一等结构对象。

## 方法

编码器根据节点表示和约束信息动态重建超边，对超边节点做稀疏/平滑正则化，并以重建损失增强约束感知表示；还通过数据增强加入约束相关特征。解码器用双指针注意力同时读取当前节点和 route recorder 中的部分解状态，逐步自回归生成路线，并进行可行性掩码。训练采用异步参数更新和双损失：超图/约束损失与策略梯度损失共同优化，使超图负责表示高阶约束、强化学习负责路线级决策。

## 实验与结果

作者在 CVRP、带时间窗的 CVRPTW 及 CVRPLIB 等基准上评估，并进行分布泛化、消融和敏感性分析。摘要报告相对方法改进最高达 7.38%；消融中 CVRP20 的 gap 为 0.65%，移除动态超图、数据增强、双指针记录器后分别升至 2.95%、1.80%、2.79%；CVRP50 中对应为 2.60%、7.42%、2.79%、6.64%。在大规模分布测试中，100 节点 Clustered/Mixed 的 gap 约为 10.11%/8.41%，优于 POMO 的 10.59%/8.75%，加入增强分布时也保持优势。敏感性分析显示 δ=0、λ=0.2 较佳；阈值过大或过小都会使超边过稀或过密。论文同时承认固定规模编码器结合贪心解码时大规模迁移仍困难。

## 贡献与局限

贡献是引入约束导向动态超边、双指针路线记录器和无标签强化学习的一体化路由框架，在小中规模和复杂约束任务上取得竞争力。局限是超图编码器与贪心解码的固定尺度限制了大规模泛化，超参数与约束构造也可能影响稳定性；相较带局部搜索/强解码的先进方法仍需更广泛规模、真实物流分布和更强搜索策略验证。作者建议研究层次化超图和改进解码/搜索。

DOI: 10.1016/j.neunet.2026.109565
