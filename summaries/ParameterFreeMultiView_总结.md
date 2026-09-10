# A Parameter-Free Multi-View Clustering Framework With Adaptive Anchors for Large-Scale Data 总结

## 基本信息

- **标题**: A Parameter-Free Multi-View Clustering Framework With Adaptive Anchors for Large-Scale Data
- **作者**: Xu Chen, Zhiwen Yu, Kaixiang Yang, C. L. Philip Chen
- **期刊 / 年份**: IEEE Transactions on Knowledge and Data Engineering, 2026
- **研究方向**: 多视图聚类与大规模数据挖掘
- **DOI**: 10.1109/TKDE.2026.3700824
- **PDF**: [TKDE_2026_ParameterFreeMultiView.pdf](papers/TKDE_2026_ParameterFreeMultiView.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 FPMCAA，将 view-specific adaptive anchors、anchor graphs 和跨视图共识对齐统一到一个无需手动权衡参数的优化框架中，以提升异构大规模多视图数据的聚类质量与可扩展性。

## 问题与动机

传统多视图聚类常操作 n×n 相似矩阵，计算和存储开销随样本规模快速增长。已有 anchor 方法虽更高效，却常在初始化后固定 anchors、强制所有视图共享 anchors，或用启发式/自加权融合替代显式对齐，因而难以同时保留视图特有结构、利用互补信息并适应异构分布。论文希望减少人工调参，同时让 anchors、图和共识表示相互修正。

## 方法

FPMCAA 为每个视图联合学习 anchor basis Av 和 anchor graph Zv，并用重构误差、Frobenius 正则、非负归一化及正交约束保持稳定和可解释的表示。它引入 view-specific projection Hv 与正交共识指示矩阵 Y，通过 ||Zv−HvY||² 将各视图图结构对齐到共同潜空间，同时保留互补性；view weight α 根据重构误差自适应确定。算法交替用 SVD、simplex projection 和闭式更新求解各变量，作者给出单次迭代关于样本数近似线性的复杂度与单调下降收敛分析。

## 实验与结果

作者在 ORL、BDGP、Cifar-100、MNIST 以及 YTF-10/20/50/100/200 九个多视图数据集上，以 ACC、NMI、Purity、F-score、ARI 和 Precision 评价，并与 14 个方法比较；k-means 在 50 个随机种子下重复。FPMCAA 在小规模到十万级样本上均达到最好或接近最好结果：相对 FSMSC，在 YTF-10 和 MNIST 的 ACC 分别提高 9.41% 和 9.58%；在 Cifar-100 上较 OMVCDR 提高 10.45%，在 YTF-50 达到 74.81% ACC。Cifar-100 和 MNIST 的运行时间分别为 334.69 s 和 167.74 s；消融、可视化与收敛实验支持 view-specific anchors 和图对齐的作用，目标值通常在少于 10 次迭代内明显稳定。

## 贡献与局限

贡献包括：把 adaptive anchor learning、anchor graph construction 和 consensus alignment 统一起来；通过逐视图 anchors 保留局部几何与互补性，再以共识空间融合；在无需外部权衡参数的条件下兼顾聚类性能和线性规模特征。局限是聚类数 k 仍需作为任务输入，anchor 数增大虽只带来小幅精度波动却明显增加运行时间；未来将处理 incomplete views，并引入 semantic priors。DOI: 10.1109/TKDE.2026.3700824
