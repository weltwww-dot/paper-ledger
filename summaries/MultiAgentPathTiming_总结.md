# Robust and effective multi-agent path execution with timing uncertainty 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Robust and effective multi-agent path execution with timing uncertainty
- 作者：Yihao Liu, Xueyan Tang, Wentong Cai, Jingning Li
- 期刊 / 年份：Artificial Intelligence，2026
- 研究方向：人工智能
- DOI：10.1016/j.artint.2026.104586
- PDF：[MultiAgentPathTiming.pdf](papers/MultiAgentPathTiming.pdf)

## 一句话概括

论文提出一个面向任意执行延迟的多智能体路径在线执行框架：在不必反复重规划路径的情况下，动态选择可并行移动的最大智能体集合，并通过可行性检验保证无冲突、无死锁且最终可达。

## 问题与动机

机器人和自动导引车的预先规划路径通常假设移动按时完成，但硬件故障、打滑、通信延迟或人为干预都会造成 timing uncertainty。静态依赖关系会使其他智能体不必要地等待，而每次延迟都重规划又计算昂贵；因此需要在安全性、执行效果和在线计算开销之间取得平衡。

## 方法

论文用 Location Dependency Graph（LDG）表示智能体路径之间的时空依赖，将“剩余路径能否在延迟下完整执行”形式化为 feasibility problem，并证明该问题为 NP-complete。作者设计了 sound and complete 的可行性检验、启发式和两级检验，再基于检验结果在线切换即将占用共享节点的先后关系，尽可能让更多智能体并行移动；同时加入多项优化以提升检验效率和可扩展性。

## 实验与结果

实验使用 Moving AI MAPF benchmark 的 room-32-32-4、warehouse-10-20-10-2-1、random-32-32-20，以及作者生成的 random-32-32-30 四类地图；每张地图有 25 个场景、10 种延迟模拟，共 250 组设置，并与 MCP、重规划、Causal-PIBT+、BTPG-optimized 和 GSES 比较。所提方法在每张地图的 250 组设置中均达到 100% 成功率；在存在暂停时通常显著降低 sum-of-costs，相比 BTPG 允许更多依赖切换，同时保持低于重规划方法的计算开销。

## 贡献与局限

贡献包括：提出适用于预定义路径的 LDG 和可行性判定框架；给出 NP-completeness 结果及相应检验算法；构建在线协调策略并以多地图实验验证其安全性和执行效果。局限是可行性检验本身为 NP-complete，复杂地图、更多智能体及更频繁或更大的延迟会影响可扩展性；未来仍需研究窗口化、并行/分布式检验，并在真实机器人通信和动力学约束下验证。

---
DOI: 10.1016/j.artint.2026.104586
