# Autonomous Causal Discovery: Evaluating LLMs’ Priors and Constraint Strategies for Reliability 总结

## 基本信息

- **标题**: Autonomous Causal Discovery: Evaluating LLMs’ Priors and Constraint Strategies for Reliability
- **作者**: Lyuzhou Chen, Xiangyu Wang, Taiyu Ban, Derui Lyu, Qinrui Zhu, Xin Wang, Huanhuan Chen
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 机器学习方法；因果结构学习与大语言模型
- **DOI**: 10.1109/tpami.2026.3689960
- **PDF**: [TPAMI_2026_AutonomousCausalDiscoveryEvaluating.pdf](papers/TPAMI_2026_AutonomousCausalDiscoveryEvaluating.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文建立结构约束强度与约束质量的分析框架，系统评估 LLM 生成的边、路径和顺序先验，并提出按节点顺序分层搜索、再用路径约束细化 DAG 的因果结构学习框架，以在先验含噪时兼顾搜索效率与可靠性。

## 问题与动机

专家引导的因果结构学习依赖昂贵且难以扩展的专家知识，而 LLM 可低成本提供先验，却可能因幻觉和语境误解给出错误因果关系。过强的边存在约束会把真实 DAG 直接排除，过弱的约束又难以有效缩小搜索空间；现有工作较少从约束类型本身系统刻画这种可靠性—剪枝效率权衡。

## 方法

作者将约束强度定义为约束导致 DAG 不确定性的减少，将约束质量定义为 LLM 肯定断言与真实结构一致的精确率，并比较 Edge Existence、Edge Forbidden、Path Existence、Path Forbidden 和 Order Constraints 五类约束。理论上得到约束强度排序 EEC > PEC > OC > PFC > EFC，并给出质量下界排序 EEC < PEC < OC < PFC < EFC；其中单个 PFC 与相反方向的 OC 等价，多条约束下 OC 可能更严格。所提两级贪心优化先按 OC（并将 PEC 转为顺序约束）划分搜索空间，再在每个顺序子空间内通过 EFC、PFC、PEC 和评分共同搜索 DAG，并对冲突顺序采用取消或软约束处理。

## 实验与结果

实验使用 ASIA、LUCAS、CHILD、NEURO、INSURANCE、WATER、MILDEW 和 ALARM 八个因果网络，以 SHD 和 F1 评价，并与 Hill Climbing、MMHC 和 Astar 比较。用 GPT-4o 获取约束时，EFC、OC、PFC 的平均精确率分别为 0.97、0.90、0.87，而 EEC 虽召回较高但精确率常低于 0.5；跨 Gemini 2.5、GPT-4.1、Claude 4.5 Haiku Thinking 和 DeepSeek v3.2 的实验保持了大体相同的类型排序。增加 PFC 通常使 F1 上升、SHD 下降，但在 WATER 和 MILDEW 等网络上存在改进上限；基于多模型共识的自动筛选流程相较仅用数据的基线仍具竞争力。

## 贡献与局限

贡献包括：提出同时刻画先验可靠性和搜索剪枝能力的结构约束度量；揭示不同约束类型与 LLM 获取方式的适配关系，尤其指出 PFC 和 OC 的实用价值；构造可联合处理全局与局部约束的可靠性导向 CSL 框架。局限是实验主要依赖八个受控网络和当前 LLM，模拟数据不能完全覆盖真实领域的语义歧义与分布偏移；PFC 擅长排除冗余关系，却不能直接发现遗漏的因果连接，作者将进一步研究 LLM 输出精度和跨领域应用。

---
DOI: 10.1109/tpami.2026.3689960
