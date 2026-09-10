# Query Refinement for Radius-Bounded $k$-Core Queries 总结

## 基本信息

- **标题**: Query Refinement for Radius-Bounded $k$-Core Queries
- **作者**: Zefang Dong, Chuanyu Zong, Xiaochun Yang, Bin Wang, Boce Chu, Yaqi Wang, Huaijie Zhu
- **期刊 / 年份**: IEEE Transactions on Knowledge and Data Engineering, 2026
- **研究方向**: 空间图查询、查询处理与优化
- **DOI**: 10.1109/TKDE.2026.3702049
- **PDF**: [TKDE_2026_QueryRefinementRadiusBounded.pdf](papers/TKDE_2026_QueryRefinementRadiusBounded.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文为半径约束 k-core（RB-k-core）查询建立统一的 why-not/why 参数解释框架，同时调整 k 与 r，以高效找出能纳入期望顶点或排除意外顶点的最优查询参数。

## 问题与动机

RB-k-core 查询要求包含查询顶点 q 的连通子图满足 k-core 社交凝聚约束和半径 r 的空间约束，适用于团队组建与活动组织等地理社交场景。用户往往难以一次设定合适的 k、r，导致期望顶点缺失（EOPE）或意外顶点出现（EOPU）；只调整单一参数还不能覆盖所有缺失情形，也可能造成过多结果变化。因此需要在保留原查询结果质量的同时，联合优化两个参数并解释结果差异。

## 方法

EOPE 要求 k′≤k、r′≥r，并使期望顶点 ω 与 q 同处一个 RB-k′-core，同时最小化修订结果规模；EOPU 则要求 k′≥k、r′≤r，在排除意外顶点 ψ 的同时最大化原结果保留量。作者先提出 PriorityR、HybridR 两个基线，再利用 k′ 的有效界、参数对的支配关系和连续收缩界提出 PriorityK、HybridK；其中 HybridK 利用多个 k′ 共享同一最优半径的关系跳过被支配搜索。作者还提出 HCR-Tree，把层次 coreness 存入 R-Tree 节点以在构图前剪枝。EOPU 采用三顶点方法得到候选参数的基本方案 BS，并以分段搜索、剪枝和终止策略形成 SA；FA 直接累计结果规模，减少对 RotC+ 的重复验证。

## 实验与结果

实验在 Weeplace、Brightkite、Gowalla、Flickr 和 Foursquare 五个真实地理社交网络上进行；每个数据集默认随机生成 100 个查询，每个查询再生成 10 个期望或意外顶点，并测试 k、r 与数据规模变化。EOPE 中 HybridK 是最有效的方案：相较 PriorityK 平均提升约 1.05–1.2 倍，HCR-Tree 使 HybridK 相比 R-Tree 版本约提升 2 倍。EOPU 中 SA 平均约比 BS 快 5 倍，并优于或接近 EOPE 最优方案 HybridK；HCR-Tree 使 SA 相比 SA-R 平均提升约 1.26 倍。FA 相较 RotC+ 在 EOPE 与 EOPU 上平均分别提升 3.68 倍和 3.74 倍；结果质量实验也显示同时修订 k 与 r 通常比单参数修订得到更小的 EOPE 结果规模。

## 贡献与局限

本文贡献是统一处理 expected/unexpected 顶点的查询解释问题，提出 EOPE 的四类探索算法、EOPU 的 BS/SA 算法，以及可复用于两类任务的 HCR-Tree 与 FA 验证方法。局限是方法针对 RB-k-core 的单查询顶点和参数单调性设计，实验主要是离线、静态地理社交图；多期望/意外顶点的复杂情形只能在部分条件下判定可行性，动态图、流式查询和更广泛的查询约束仍需进一步研究。

---
DOI: 10.1109/TKDE.2026.3702049
