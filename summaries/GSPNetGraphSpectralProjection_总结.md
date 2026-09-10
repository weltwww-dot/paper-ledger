# GSPNet: Graph Spectral Projection Network Using Learnable Spectral Transformation 总结

## 基本信息

- **标题**：GSPNet: Graph Spectral Projection Network Using Learnable Spectral Transformation
- **作者**：Yangli-ao Geng、Yuxiao Dong、Wenzheng Feng、Qingyong Li、Jie Tang
- **期刊 / 年份**：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **研究方向**：人工智能
- **DOI**:10.1109/TPAMI.2026.3685759
- **PDF**：[TPAMI_2026_GSPNetGraphSpectralProjection.pdf](papers/TPAMI_2026_GSPNetGraphSpectralProjection.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文从理论上揭示固定图谱变换下 SGCN 多项式传播存在不可忽略的传播误差，并提出学习谱变换子空间的 GSPNet，使节点传播矩阵能够更接近由类别划分定义的理想结构。

## 问题与动机

经典 SGCN 固定输入图的特征向量矩阵 (P)，只学习谱滤波器，因此传播矩阵属于由归一化邻接矩阵多项式生成的受限集合。实际图中常含与类别无关的噪声或结构信息；论文证明在温和条件下，即使选取该集合中的理论最优矩阵，也与理想类别块结构保持非零距离，堆叠多层后误差还可能累积。作者据此把学习对象从固定谱域中的滤波器扩展到谱变换本身。

## 方法

GSPNet 用列正交矩阵 $U \in \mathbb{R}^{N\times C}$ 表示低秩谱子空间，以 $UU^T XW$ 作为传播特征，并加入图正则项 $-\alpha\,\mathrm{tr}(U^T\hat{A}U)$，使学习到的投影仍利用原图结构。正交约束在 Grassmann 流形上用黎曼梯度下降和 SVD 投影优化；多层版本共享同一 $U$ 以降低参数与存储。为控制其强表达能力导致的过拟合，作者在图视图和特征视图间采用非对称协同训练：传递特征变换矩阵 $W$，并反向传递高置信伪标签。

## 实验与结果

实验覆盖 Cora、Citeseer、Pubmed、Coauthor-Physics、Coauthor-CS、Amazon-Computers、Amazon-Photo、Actor 八个真实数据集，并在 Spiral 上注入 0%–70% 邻接噪声，所有自实现结果进行 50 次随机试验。GSPNet 在八个真实数据集中的多数任务优于通用和谱 GNN；UniFilter 在 Coauthor-CS、Amazon-Computers 最好，TFEGNN 与 GSPNet 在 Pubmed 并列，GSPNet 在其余五个数据集领先。Spiral 的 10%–70% 噪声下 GSPNet 均优于基线，70% 噪声时领先第二名 SSGC 约 9 个百分点；四层模型在约一百万节点图上的训练时间约 32 s。

## 贡献与局限

主要贡献是给出固定谱变换传播误差的表达式与下界，并以可学习的低秩正交投影突破多项式传播限制；Grassmann 优化、图正则和协同训练共同使模型在噪声图与异质结构上保持较强表现。局限是当前谱表示与单个图一一对应，因而不适合直接处理节点数和结构各异的图级分类；极大规模图（如 (10^8) 节点、(10^4) 类）仍具挑战，且高表达能力带来的过拟合控制和协同训练机理尚未完全解释。
