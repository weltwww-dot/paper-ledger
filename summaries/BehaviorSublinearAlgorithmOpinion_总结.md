# Behavior and Sublinear Algorithm for Opinion Disagreement on Noisy Social Networks 总结

## 基本信息

- **标题**: Behavior and Sublinear Algorithm for Opinion Disagreement on Noisy Social Networks
- **作者**: Wanyue Xu、Yubo Sun、Mingzhe Zhu、Zuobai Zhang、Zhongzhi Zhang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/tkde.2026.3680940
- **arXiv**: 无
- **PDF**: [TKDE_2026_BehaviorSublinearAlgorithmOpinion.pdf](papers/TKDE_2026_BehaviorSublinearAlgorithmOpinion.pdf)

## 一句话概括

该文研究稀疏无标度社交网络上受白噪声扰动的 DeGroot 意见动力学，发现意见分歧度趋于常数、即幂律拓扑对噪声具有抗性，并提出带误差保证的亚线性时间近似算法以支撑大规模网络计算。

## 问题与动机

意见分歧现象在文献中已有实证报道，其受社交网络结构等多种因素影响。网络科学的一项重要发现是：包括社交网络在内的大多数真实网络都是稀疏且无标度的。然而，幂律拓扑究竟如何影响噪声环境下的意见分歧，此前并不清楚；同时，既有估计意见分歧度的算法计算复杂度过高，在大规模网络上不具备可行性。作者希望同时回答"行为规律"与"可计算性"两个问题。

## 方法

作者采用图上离散时间的 DeGroot 意见动力学模型，令节点意见受白噪声扰动，在稀疏无标度网络上展开分析。在行为层面，作者先在大量真实网络与模型网络上考察意见分歧度的表现；在算法层面，针对既有方法复杂度过高的问题，提出一种亚线性时间算法：它从部分节点出发高效模拟截断随机游走，在保留精度的同时把估计代价压到亚线性，并给出理论保证的误差界。文中还用到 Kemeny 常数等量与 APPROXDELTA、SAMPLEDELTA 两个算法做估计与对比。

## 实验与结果

真实网络实验覆盖 Protein、web-EPA、Brightkite、soc-delicious、soc-hyves、delaunay-n24 等规模各异的图，误差参数 ε 在 [0.25, 0.4] 范围内系统调整。结果显示两种算法的运行时间均符合其理论复杂度中 ε^-2 的规律，但规模表现不同：在 Protein、web-EPA 等较小网络上，APPROXDELTA 凭借优化过的矩阵运算更快；而在 soc-hyves、delaunay-n24 等大规模网络上，SAMPLEDELTA 的亚线性采样策略带来显著效率优势，其收益随网络规模 √n 增长，只有当规模超过一定阈值后采样开销才被摊薄。在模型网络 F^12、F^13、F^14、F^15 上估计 Kemeny 常数（其中 F^15 含 21,523,362 个节点）时，两种算法在 F^12、F^13 上均表现良好，SAMPLEDELTA 更为高效；对 F^15，APPROXDELTA 在时间与内存上均耗尽，而 SAMPLEDELTA 在 920 秒内返回结果，相对误差小于 0.3%。行为层面的实验表明，无标度网络上的意见分歧度趋近于一个常数，说明幂律结构对意见动力学中的噪声具有抗性。

## 贡献与局限

- 揭示稀疏无标度拓扑对噪声意见动力学的抗性：意见分歧度收敛到常数，给出幂律结构影响意见分歧的清晰结论。
- 提出带理论误差保证的亚线性时间近似算法，通过截断随机游走把大规模网络上的意见分歧估计变为可行。
- 在六个真实网络与四个大规模模型网络上验证：SAMPLEDELTA 在 2152 万节点图上 920 秒内完成估计且相对误差小于 0.3%，而传统方法已不可行。
- 局限：效率优势依赖网络规模，小规模网络上采样开销未必划算；结论建立在 DeGroot 模型与白噪声假设之上，向其他意见动力学模型与非无标度拓扑的推广仍需检验。

---
DOI: 10.1109/tkde.2026.3680940
