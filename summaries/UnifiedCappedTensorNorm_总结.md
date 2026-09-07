# A Unified Framework With Capped Tensor Norm Minimization for Multiview Subspace Learning 总结

## 基本信息

- **标题**: A Unified Framework With Capped Tensor Norm Minimization for Multiview Subspace Learning
- **作者**: Yao Fu, Zhi Wang, Dong Hu, Tao Jia, Chao Gao, Zhen Wang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3694749
- **arXiv**: 无
- **PDF**: [TKDE_2026_UnifiedCappedTensorNorm.pdf](papers/TKDE_2026_UnifiedCappedTensorNorm.pdf)

## 一句话概括

提出统一框架 UFCTNM，以截断张量核范数联合超图拉普拉斯正则与谱嵌入学习多视图子空间表示，兼顾全局低秩、局部几何与离群点鲁棒性。

## 问题与动机

多视图子空间聚类（MVSC）能利用多个特征空间的互补信息，但现有方法仍有两类不足：一是普遍采用凸低秩近似（如张量核范数 TNN），对所有奇异值施加相同惩罚，会过度收缩主导成分，难以充分挖掘互补子空间信息；二是多数模型忽略视图内在的几何关系，并把谱聚类作为独立步骤执行，容易得到次优解。此外，用 ℓ2,1 或 ℓ1 范数建模稀疏误差对不同样本施加均匀约束，忽略噪声分布的差异，使模型对极端离群点敏感。因此需要设计统一框架，同时解决低秩表示不精确、几何信息与全局一致性被割裂以及鲁棒性不足的问题。

## 方法

论文提出名为 UFCTNM（capped tensor norm minimization 的统一框架）的 MVSC 模型：将各视图自表示矩阵堆叠为三阶张量，用截断张量核范数（CTNN）刻画全局低秩结构——其截断阈值随迭代自适应变化，比固定截断参数更灵活；用截断 ℓ2,1 范数（capped ℓ2,1-norm）对误差建模，超过阈值的列范数不再增长，从而抑制极端离群点的影响。同时该模型把超图拉普拉斯正则化（保留各视图局部几何/非线性流形结构）与谱嵌入（联合优化簇指示矩阵 F 以避免分步执行带来的次优性）集成进同一目标函数。求解上，基于 ADMM 框架引入辅助变量 G 与 Q(v)，交替更新 Z(v)、E、Q(v)、G、F 及各乘子；文中证明 CTNN 正则化最小二乘子问题存在可由 t-SVD 加阈值算子直接给出的闭式全局最优解，并进一步证明算法产生的解序列收敛到满足一阶最优性条件的 KKT 点。整体时间复杂度约为 O(T(n³ + n²V log n + n²d_v))（T 次迭代）。

## 实验与结果

在九个真实基准数据集（20Newsgroups、Yale、ORL、Notting-Hill、UCI-Digits、MITIndoor、ALOI、COIL20、100leaves，覆盖文本、人脸、数字、场景、物体、植物六类）上与 14 个多视图聚类方法对比，包括矩阵式（DiMSC、MLRR、LSGMC、FAMvC）和张量式（LT-MSC、ETLMSC、HLR-M2VS、GNLTA、WTSNM、t-SVD-MSC、EMKIC、L1SL-ℓ2,p-TAF-MSC、T-UMC、Orth-NTF），采用 ACC、NMI、AR、F-score、Precision、Recall 六种指标。总体上该方法在多数数据集与指标上全面领先：在 Yale、ORL、20Newsgroups、COIL20、UCI-Digits 五个数据集取得理想结果，其中 Yale 上所有指标均达 100%，较第二名在六项指标上分别提升约 1.5%、1.1%、2.7%、2.5%、3%、1.5%；在 MITIndoor 上相对次优的 L1SL-ℓ2,p-TAF-MSC 六项指标提升约 1.4%、0.1%、1.2%、1.1%、2.1%、0.1%，ACC 相对非凸方法 L1SL-ℓ2,p-TAF-MSC、GNLTA、WTSNM 分别提升 2.4%、16.8%、21.7%。混淆矩阵（Yale）与相似度矩阵（ORL、COIL20）可视化显示其对角块更清晰、块对角结构更明显。消融实验表明超图拉普拉斯正则（ALOI 上 ACC 较基础模型提升超 2%）与谱嵌入（100leaves 提升约 0.6%、ALOI 约 2%）各自有效且完整模型最佳；τ 在 [0.1, 1] 时六数据集均达最优。数值上算法约 10 次迭代内 ACC/NMI 趋于稳定，目标函数约 25 次迭代收敛到平稳值。实验环境为 MATLAB R2020b，Intel Xeon Gold 6230 CPU、256 GB RAM。

## 贡献与局限

主要贡献：提出统一框架 UFCTNM，据作者所知首次将超图拉普拉斯正则化与谱嵌入整合进单一 MVSC 模型，使表示学习、局部几何保持与判别信息编码相互促进；引入 CTNN 与截断 ℓ2,1 范数，既能更准确刻画全局低秩结构又抑制极端离群点；CTNN 子问题具有闭式解使算法高效精确，并给出非凸多块问题收敛到 KKT 点的理论保证；九数据集上的大量实验全面验证其有效性，MATLAB 代码公开在 GitHub（wangzhi-swu/UFCTNM）。局限：傅里叶变换、t-SVD 与矩阵求逆带来较高的时间复杂度；未来工作将考虑加速算法，并引入自适应视图加权或视图选择以处理视图间明显矛盾的情形，以及扩展到不完整多视图（incomplete multi-view）设定。

---
DOI: 10.1109/tkde.2026.3694749
