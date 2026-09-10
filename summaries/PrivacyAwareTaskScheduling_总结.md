# Privacy-Aware Task Scheduling in Satellite Edge Computing: A Game-Theoretic Framework 总结

## 基本信息

- **标题**: Privacy-Aware Task Scheduling in Satellite Edge Computing: A Game-Theoretic Framework
- **作者**: Ruizhi Wang, Xiaolong Xu, Guangming Cui, Haipeng Dai, Lianyong Qi, Xuyun Zhang, Wanchun Dou
- **期刊 / 年份**: IEEE Transactions on Dependable and Secure Computing, 2026
- **研究方向**: 卫星边缘计算、隐私保护、任务调度
- **DOI**: 10.1109/TDSC.2026.3696118
- **PDF**: [TDSC_2026_PrivacyAwareTaskScheduling.pdf](papers/TDSC_2026_PrivacyAwareTaskScheduling.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文把任务共址、路径跳数、加密状态和执行节点信任差异纳入卫星边缘计算的统一调度目标，并提出集中式 TS-OPT 与可扩展的精确潜在博弈调度器 PAPGS，以联合优化延迟、能耗和隐私暴露。

## 问题与动机

LEO 卫星边缘计算中的任务需要在本地卫星、经 ISL 多跳转发的远端卫星或地面云之间选择执行位置；异构算力、带宽限制、队列竞争和移动链路使放置与路由紧密耦合。现有调度器多关注时延、能耗和吞吐，较少刻画多跳中继、同一用户任务共址、明文传输及低信任执行节点带来的隐私风险。集中式混合整数优化难以扩展到大星座，而简化的分布式方法又可能牺牲稳定性或隐私。

## 方法

作者定义任务级隐私风险分数，将 server-level co-location、path-induced exposure、encryption-dependent risk 和 execution-location trust 四项相加，并与传输/执行时延和能耗组成统一目标。TS-OPT 将该模型改写为集中式混合整数规划，为小规模实例提供全局最优参照。PAPGS 把每个任务视为玩家，将目标分解为链路拥塞、目的地拥塞、任务个体项和同用户共址项，构造 exact potential；任务通过严格 best response 在可行本地、地面云和远程卫星路径间更新。势函数单调改进，因此存在纯策略 Nash equilibrium，严格最佳响应在有限步内终止。

## 实验与结果

作者以 Python 3.9、50 次独立 Monte Carlo 试验评估 TS-OPT、PAPGS、MFGLB、GDCO、SAC、Local 和 Random；PAPGS 的 ISL 跳数上限为 2，默认权重为 α=100、β=1.0×10⁻⁴、γprivacy=10。小规模实验中，摘要报告 PAPGS 相对 TS-OPT 的 optimality gap 为 0.18%。大规模星座 N∈{15,21,27}、负载 1.0–3.0 MB 的汇总结果中，PAPGS 平均时延 0.947 s、完成率 98.094%、隐私分数 1.789、运行时间 0.284 s；相较 MFGLB 的 2.164 s/87.797%/1.628/1.776 s 和 GDCO 的 2.244 s/86.902%/1.552/11.547 s，PAPGS 在统一目标下提供了更均衡的折中。论文也指出，MFGLB/GDCO 更低的隐私分数伴随更高时延和更低完成率。

## 贡献与局限

贡献包括：面向 post-uplink SEC 的四因素隐私暴露模型；具有有限步收敛保证的 PAPGS 精确潜在博弈；以 TS-OPT 和多种基线验证小规模近最优性及大规模负载鲁棒性。局限是隐私泄漏是用于调度比较的 composite risk score，而非信息论泄漏量；信任、拓扑和攻击面主要按静态或简化设置建模，实验为仿真，未来需纳入时变信任、预测接触动态和更真实的对手模型。

---
DOI: 10.1109/TDSC.2026.3696118
