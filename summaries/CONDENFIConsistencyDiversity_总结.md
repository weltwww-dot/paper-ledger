# CONDEN-FI: Consistency and Diversity Learning-Based Multi-View Unsupervised Feature and Instance Co-Selection 总结

## 基本信息

- **标题**: CONDEN-FI: Consistency and Diversity Learning-Based Multi-View Unsupervised Feature and Instance Co-Selection
- **作者**: Yanyong Huang, Yuxin Cai, Dongjie Wang, Xiuwen Yi, Tianrui Li
- **期刊 / 年份**: IEEE Transactions on Knowledge and Data Engineering, 2026
- **研究方向**: 多视图无监督特征选择与实例选择
- **DOI**: 10.1109/TKDE.2026.3700726
- **PDF**: [TKDE_2026_CONDENFIConsistencyDiversity.pdf](papers/TKDE_2026_CONDENFIConsistencyDiversity.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 CONDEN-FI，在多视图无标签数据中联合选择重要特征和代表性实例，通过 shared/view-specific representations、consensus similarity graph 以及 diversity learning 同时利用跨视图一致性和视图互补性。

## 问题与动机

高维多视图数据常含冗余特征、噪声样本和不具代表性的实例，增加存储和训练成本。既有方法往往把特征选择与实例选择分开，忽略两个空间的相互影响；面向多视图时又常先拼接视图，无法利用共享结构，并且主要压制冗余而不保证所选实例的多样性。因此需要在无标签条件下联合保留跨视图一致信息、视图特有信息和局部流形结构。

## 方法

CONDEN-FI 在每个视图学习特征变换矩阵 W(v)，把高维数据投影到受正交约束的低维空间；同时用实例自表示矩阵 B 与 B(v) 分解 shared 和 view-specific 重构，并以 ℓ2,1 正则产生特征、实例重要性。方法自适应学习各视图权重和 consensus similarity graph S：相似样本的 view-specific 表示应接近，而不相似样本在 shared 表示中的贡献被拉近，从而鼓励多样实例。算法交替更新 W(v)、B、B(v)、S 及权重，主要子问题具有闭式或可求解更新，并给出收敛与复杂度分析。

## 实验与结果

作者在 MSRC_V1、YaleB、Usps、BBCSport、NGs、WebKB、Cora 和 Sensit Vehicle 八个公开多视图数据集上，用选出的特征训练 SVM，再预测未选实例，以 ACC 和 F1 评价；特征选取比例为 10%–50%、实例比例为 10%–50%，每组实验独立运行 5 次，并与 UFI、DFIS、sCOs2 及多种组合基线比较。在选取 30% 特征和 20% 实例的设置下，CONDEN-FI 在八个数据集上均优于对比方法；相对第二名，YaleB/BBCSport 的 ACC 和 F1 提升超过 10%，MSRC/NGs 超过 7%，Sensit 超过 5%，Cora 接近 5%，WebKB/Usps 的提升接近 2%。收敛曲线通常约在 20 次迭代附近稳定，去掉 consensus graph、shared representation 或局部流形项的三个变体均变差。

## 贡献与局限

贡献包括：首次在无标签多视图数据中统一利用 shared 与 view-specific 信息进行特征—实例共选择；以低维重构和自适应共识图同时促进信息性与多样性；给出交替优化算法并通过多数据集和消融实验验证其有效性。局限是每次迭代更新 B、B(v) 等 n×n 结构，主复杂度为 O(Vn³+c nΣv dv)，对超大规模数据仍不够友好；参数 θ、α、r 也会影响结果。未来将研究可扩展并行算法、极端视图异质性和更稳健的自适应视图加权。DOI: 10.1109/TKDE.2026.3700726
