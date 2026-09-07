# Toward In-Depth Root Cause Localization for Microservices With Multi-Agent Recursion-of-Thought 总结

## 基本信息

- **标题**: Toward In-Depth Root Cause Localization for Microservices With Multi-Agent Recursion-of-Thought
- **作者**: Lingzhe Zhang, Tong Jia, Kangjin Wang, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3706572
- **arXiv**: 无
- **PDF**: [TDSC_2026_MultiAgentRecursionOfThought.pdf](papers/TDSC_2026_MultiAgentRecursionOfThought.pdf)

## 一句话概括

本文提出 RCLAgent，一种基于多智能体"递归思维"并行推理的微服务系统根因定位框架，通过沿 trace 图分解诊断过程缓解上下文爆炸与串行推理问题，在多个公开基准上以更高效率取得领先的根因定位精度。

## 问题与动机

微服务系统因动态交互与演化环境而频繁发生故障，能否准确、及时地定位根因（root cause localization, RCL）直接影响系统可靠性。现有方法中，基于图/统计的可解释方法依赖特定结构或遥测假设，跨环境泛化弱；基于深度学习的方法缺乏可解释性且迁移性差。作者通过访谈 15 位来自北京大学与华为理论实验室的开发者/SRE，归纳出人工根因分析的三大特征：递归性、多维扩展与跨模态推理；并对 AIOPS 2022 上 100 个失败案例的 ReAct 基线进行事后分析，发现其失败主要源于两类问题：一是上下文爆炸导致的证据稀释（43 例，其中 8 例丢失根因证据、35 例根因被降级），二是串行推理导致的浅层推理（57 例，过早收敛于中间假设）。这促使作者设计沿 trace 结构分解、证据有界传播的 RCLAgent。

## 方法

RCLAgent 实现了多智能体递归思维（multi-agent recursion-of-thought）与并行推理。它把诊断过程沿 trace 图分解：为每个 span 指派一个专用智能体（Dedicated Agent），智能体按图拓扑递归组织，并从 Agents Pool（默认容量 K=100，约束并发活跃智能体数）实例化，支持独立分支并行推理。数据工具层包括 Trace Tool（仅用于构造 trace 图）、Metric Tool（以 n-sigma 准则在局部时间窗内筛选显著波动指标，n=3、δ=60s）和 Log Tool（按严重级别、错误码等启发式过滤日志）。每个专用智能体先做自状态验证（调用日志与指标工具判断自身 span 是否异常，输出结构化证据摘要），再通过证据整合（Evidence Consolidation）把子智能体的下游证据与自身证据递归合成局部根因假设（含原因与置信度）上传父级；顶层 Root Agent 生成根级诊断报告，同时各智能体的细粒度自状态证据汇成与 trace 图同构的全局证据图（Global Evidence Graph），最后由 Diagnosis Synthesizer 联合二者输出按似然排序的根因候选列表。

## 实验与结果

实验在三个公开基准上进行：AIOPS 2022（真实电商系统，7 个微服务、44 个 pod、6 个节点，含 400 项性能指标与 4 项业务指标）、Augmented-TrainTicket（41 个微服务的火车票系统）和 RCAEval 的 RE2-OB 子集（共 735 个故障案例），以 Recall@1/5/10 与 MRR 为指标，与 CRISP、MicroRank、TraceRank、BARO、Nezha 等非 LLM 方法及 mABC、RCAgent、GALA、ReAct 等 LLM 方法对比。默认骨干为 Claude-3.5-Sonnet。结果显示：AIOPS 2022 上 MRR 达 69.73%，比最强 LLM 基线 mABC 高 11.68%、比最佳非 LLM 方法 TraceRCA 高 27.54%；Augmented-TrainTicket 上 MRR 74.08%，超过 mABC 6.82%（仅 Recall@5 落后 mABC 2.02%）；RCAEval 上 MRR 62.97%，超过 GALA 4.04%。配对的 Wilcoxon 符号秩检验显示 MRR 的 p 值为 0.012，各指标差异显著。效率方面，相对 ReAct，平均推理时间在 AIOPS 2022、TrainTicket、RCAEval 上分别从 87.63s、89.73s、85.77s 降至 41.43s、59.55s、49.79s，加速约 1.49×–2.11×。骨干模型研究表明 RCLAgent 依赖骨干推理能力：Claude-3.5-Sonnet 平均 MRR 最佳，DeepSeek-R1-Qwen 在 Δ、Z 子集上分别以 65.13 与 59.33 小幅超过 Claude（61.03 与 54.88），而 HumanEval 达 87.1 的 GPT-4 在各子集 MRR 均低于 15。消融实验（AIOPS 2022）显示去除全局证据图降幅最大（69.73%→56.90%），去除根级诊断报告降至 64.19%，去除自状态验证降至 62.00%，去除递归证据整合降至 61.27%；超参数 δ 从 10s 增至 120s 时精度先升后稳而延迟单调上升。

## 贡献与局限

主要贡献包括：其一，通过访谈与失败案例分析系统研究了 SRE 的根因定位实践，提炼出递归、多维扩展、跨模态推理三大特性，并指出既有 LLM 方法的失败根源在于上下文爆炸与串行推理；其二，提出 RCLAgent，以"每 span 一智能体 + 并行递归推理 + 有界上下文 + 全局证据图"的方式实现深度根因定位；其三，在多个异构公开基准上验证了其跨数据集精度优势与相对既有 LLM 方法约 1.49×–2.11× 的推理加速，并通过统计检验、消融与骨干敏感性分析佐证结论。局限在于：效果强依赖底层 LLM 的推理能力与任务对齐，且推理成本高于轻量非 LLM 方法（如 BARO），部署时需权衡精度、延迟与成本；作者提出未来将以更小规模模型实现更准更省的定位，并把框架扩展到完整故障管理流程。

---
DOI: 10.1109/tdsc.2026.3706572
