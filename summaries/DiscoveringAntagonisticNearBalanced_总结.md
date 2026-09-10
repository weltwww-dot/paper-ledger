# Discovering Antagonistic Near-Balanced Dense Subgraphs in Signed Networks 总结

## 基本信息

- **标题**：Discovering Antagonistic Near-Balanced Dense Subgraphs in Signed Networks
- **作者**：Xiaojia Xu、Haoyu Liu、Xiaowei Lv、Yongcai Wang、Deying Li
- **期刊 / 年份**：IEEE Transactions on Knowledge and Data Engineering，2026
- **研究方向**：数据工程
- **DOI**:10.1109/TKDE.2026.3703775
- **PDF**：[TKDE_2026_DiscoveringAntagonisticNearBalanced.pdf](papers/TKDE_2026_DiscoveringAntagonisticNearBalanced.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文定义同时衡量平衡性、内部凝聚力和跨群体冲突强度的 antagonism measure，并提出 IPPV-s，在带符号网络中发现互不重叠、局部紧致且具有高对抗性的近均衡稠密子图。

## 问题与动机

最大平衡子图往往稀疏，严格平衡团又容易退化为很小的结构；极化社区方法通常不严格遵循平衡理论，也难区分合作与冲突；传统稠密子图则把正负边一视同仁。作者希望在允许少量不平衡和缺失连接的同时，保留内部紧密性并显式刻画两个对立群体之间的负边密度，以服务社区搜索、冲突检测和国际关系分析。

## 方法

Antagonism measure 定义为 polarity、internal cohesion 和 external antagonistic normalized density 三项乘积，其中外部项用两群体规模几何均值的平方归一化以减小群体大小差异造成的偏置。算法以含负边的 antagonistic balanced (h_x)-pattern 为局部结构单元，先用 pattern core 初始化紧致数上下界，再通过凸规划近似紧致数、TentativeGD 和 stable pattern group 收紧候选范围，随后剪枝。IPPV-s 对候选执行局部最大流验证，并用较小的边界流网络加速；最后用 PASTA-toss 求左右群体，按 antagonism 排序输出 top-(k) 局部 (h_x)-PDS。

## 实验与结果

实验在信任、投票和冲突领域的真实带符号图上评估，并用 Amazon、DBLP 等无符号大图随机赋予负边比例测试效率；对比 BCE、BANSAL、EIGENSIGN 和 ELECTRON。负边比例约 60% 时 antagonistic balanced patterns 数量通常最多，运行时间随模式数和图密度增加而增加；IPPV-s 在多数数据集上比 BANSAL 更高效，只有 wikiconflict 例外。Correlates of War 1996–1999 网络含 151 个顶点、1100 条正边和 147 条负边，最高对抗性结果包含左侧 20 个北美/欧洲国家与右侧俄罗斯、伊拉克；在 wikiconflict 上，IPPV-s 的 antagonism 高于多数比较方法且规模显著大于严格平衡团结果。

## 贡献与局限

主要贡献是把结构平衡、内部密度和外部冲突统一成可排序的对抗性指标，并将凸优化边界、剪枝和局部最大流验证组合成可扩展的 IPPV-s 管道；实验表明它能发现同时反映合作与对抗关系的有意义子图。局限是最大流验证在十亿规模或极稠密网络上仍可能成为瓶颈，模式结构目前预先定义且主要面向静态图，因而对不断演化的冲突和动态带符号网络的适应性尚未解决；作者计划研究近似、并行和动态网络扩展。
