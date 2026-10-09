# SURGE: Structural Perturbation Response Field Guided Residual Distillation for Graph Unlearning 总结
## 基本信息
- **标题**: SURGE: Structural Perturbation Response Field Guided Residual Distillation for Graph Unlearning
- **作者**: Chaofan Shen、Mingyu Wang、Jing Zhang
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-07
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07176-x
- **PDF**: [ML_2026_SURGE.pdf](papers/ML_2026_SURGE.pdf)

## 一句话概括
SURGE 用删除请求前后的节点预测变化构造结构响应场，再以此引导输出层修正和知识蒸馏，完成图神经网络中的节点、边或特征遗忘，同时尽量保持保留数据上的效用。

## 问题与动机
图神经网络通过邻居聚合传播信息，删除一个节点或边的影响可能扩散到多跳邻域。已有分区法可能破坏跨分区连边，影响函数法估计参数变化，学习式方法常用固定邻域近似受影响范围；作者认为这些方法缺少依请求而变、直接反映预测变化的连续信号（第2–4页）。

## 方法
Sense 阶段比较缓存的原始 logits 与删除后图上的预测分布，以对称 KL 构造逐节点响应分数；Repair 阶段在输出空间求解带响应权重、保留标签引导和图平滑项的残差修正，采用无反向传播的 Jacobi 迭代生成校正教师 logits；Distill 阶段按修正幅度加权蒸馏，并用保留节点标签维持分类效用。Sense 与 Repair 不需反向传播，但响应场只是预测级修正路由信号：理论命题对线性 GNN 给出单向关系，不能把它解释为精确影响区域或训练影响排序（第8–14页、32–33页）。

## 实验与结果
实验覆盖七个常规基准及 ogbn-arxiv 扩展，主要使用 GCN/GAT；节点、边、特征删除默认比例为10%，与全量重训及多类图遗忘方法比较。跨 Cora、PubMed、Amazon Computers，三类删除、两种骨干组成的18格、每格10个种子评估中，SURGE 平均 micro-F1 为0.8632，测试集相对重训模型的平均 JSD 为0.0243，在 SURGE、ETR、MEGU、IDEA 中最佳；单项结果仍有差异。GCN/GAT 上报告的平均重训加速比分别为2.89倍和2.98倍（第16、18–26、28页）。

## 贡献与局限
贡献是把请求引发的预测变化转成连续、拓扑相关的修正信号，并串联无梯度教师修正与响应自适应蒸馏；多种删除类型的匹配实验显示其整体效用与重训一致性有竞争力。局限是响应分数可能因模型输出抵消而漏掉结构变化，作者也明确其不是精确定位器；隐私评估仅用单一 loss-based membership inference，且缓存原始 logits 仍需保护。现有强比较集中于18格子集，长期连续遗忘还只覆盖短序列情形（第23–26、32–33页）。

---
DOI: 10.1007/s10994-026-07176-x
