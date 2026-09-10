# Utility-Preserving Federated Graph Learning With Dual-Perspective Fairness 总结

## 基本信息

- **标题**: Utility-Preserving Federated Graph Learning With Dual-Perspective Fairness
- **作者**: Renqiang Luo, Huafei Huang, Shuo Yu, Fengqi Yu, Feng Xia, Sajal K. Das, Chengqi Zhang
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 联邦图学习、算法公平性
- **DOI**: 10.1109/TPAMI.2026.3689213
- **PDF**: [TPAMI_2026_UtilityPreservingFederatedGraph.pdf](papers/TPAMI_2026_UtilityPreservingFederatedGraph.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 F3GL，通过选择图邻接矩阵的主导特征值/特征向量并加入可学习 Fourier positional encoding，在 FedGNN 中同时改善客户端 local fairness 与服务器 global fairness，同时尽量保持节点分类效用。

## 问题与动机

联邦图神经网络中的非 IID 敏感属性分布会使偏差同时出现在客户端聚合前和服务器聚合后；local fairness 与 global fairness 不能相互线性替代，因此只优化一侧并不能保证整体公平。已有公平 GNN 方法通常会牺牲预测准确率，而分布式图结构与缺少全局邻居信息又会放大这种效用损失。本文据此研究敏感特征与图谱卷积之间的关系，试图在双视角公平与 utility 之间取得更好的平衡。

## 方法

F3GL 采用 FedAvg，并在每个客户端的邻接矩阵上用 Arnoldi 方法选取幅值最大的 e 个特征值及对应特征向量，抑制非主导谱分量对敏感特征相关性的重新引入。理论分析证明，卷积后敏感特征相似度的渐近行为主要由最大幅值特征值控制，收敛速率由前两个特征值的比值决定；客户端公平性与这些客户端主特征向量相关，服务器 global fairness 则可由各客户端主谱相似度给出下界。随后，方法以 learnable Fourier feature positional encoding 和 MLP 调整选定谱的表示，再将其用于图卷积以保留图结构 utility。

## 实验与结果

作者在 Credit、Pokec-z、Pokec-n 和 AMiner-L 四个真实数据集上进行节点分类实验，以 ACC/AUC 衡量 utility，以 ΔSP/ΔEO 衡量 fairness，并与 GCN、SAGE、APPNP、GAT、NIFTY、FairVGNN、FairGNN、FairSIN、FED-PUB、FedGCN、FairFed 和 F²GNN 等比较。实验采用 FedAvg，训练 200 个全局轮次、每轮 10 个本地步骤，并在 Pokec 数据上同时考察 region 与 gender 敏感属性。结果显示，F3GL 在绝大多数设置中取得更低的 local/global ΔSP 与 ΔEO，同时保持公平方法中最高或接近最高的 ACC/AUC；消融实验表明，fairness-aware eigenvalue selection 与 Fourier encoding 均能同时改善公平和效用。e 增大到纳入更多非主导特征向量后公平性下降；谱选择的特征分解复杂度为 O(ne²)，相较完整分解的 O(n³) 可减少运行时间和存储。

## 贡献与局限

贡献包括：建立 FedGNN 双视角公平的谱理论分析；提出只保留主导谱并以 Fourier encoding 修正其表示的 F3GL；在多敏感属性和四个真实数据集上验证公平—效用折中。局限是结论和评估依赖可获得的敏感特征、客户端图分区及所选谱卷积设置，论文未来还计划进一步提高计算效率并扩展到敏感特征受限的场景。

---
DOI: 10.1109/TPAMI.2026.3689213
