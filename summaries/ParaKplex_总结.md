# ParaKplex: A parallel local search algorithm for the maximum K-Plex problem 总结

## 基本信息

- **标题**: ParaKplex: A parallel local search algorithm for the maximum K-Plex problem
- **作者**: Jieyu Wu, Rui Sun, Yiyuan Wang, Minghao Yin
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-08-20
- **内容状态**: 完整
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104604
- **PDF**: [AIJ_2026_ParaKplex.pdf](papers/AIJ_2026_ParaKplex.pdf)

## 一句话概括

提出 ParaKplex，一个面向最大 k-plex 问题（MKPP）的并行局部搜索算法：用基于分组的初始化与主-从搜索把全局与局部搜索并行化，并配套三项新的顺序策略，显著超过现有最先进算法。

## 问题与动机

最大 k-plex 问题是最大团问题的松弛推广，具有大量实际应用。近年局部搜索算法在该问题上表现优异，但多数最先进方法仍是串行的，并行化研究有限；大规模图场景下串行算法的求解能力成为瓶颈。

## 方法

并行化设计：基于分组的初始化方法（group-based initialization）为各线程生成初始解；主-从搜索方法（primary-secondary search）整合全局与局部搜索过程。顺序侧新增三项策略：新的配置检查策略（relax 顶点的禁忌条件）、顶点选择策略（挑选高质量顶点）与扰动策略（帮助跳出局部最优）。

## 实验与结果

在包含经典实例与大图（SNAP）基准的大量测试集上实验：ParaKplex 显著优于 GPULS、U-MKP、KLS、DCCplex、DiseMKP、KpLeX-Gap、kPEX、KplexT、RelaxPUB-Maplex 等现有算法；相对其中多个基线平均解质量提升约 7.8%–9.8%。与 KLS 相比，3123 个实例中 2697 个结果相同，426 个结果不同里 ParaKplex 胜出 423 个。用 10 线程跑一次即超过多数启发式算法跑 10 次取最优的结果，验证了并行化的可扩展性。

## 贡献与局限

- 贡献一：首个面向 MKPP 的并行局部搜索算法（组初始化 + 主-从搜索集成全局与局部搜索）。
- 贡献二：配置检查、顶点选择与扰动三项新顺序策略，可迁移到其他搜索类算法。
- 贡献三：在经典与大规模图上验证并行可扩展性，并给出与最优方法的全面对比。
- 局限：参数 L（邻域搜索预算）对实例类型敏感，需按经典/大规模稀疏图分别设定；并行规模与理论加速比的分析仍可深化。

---

DOI: 10.1016/j.artint.2026.104604
