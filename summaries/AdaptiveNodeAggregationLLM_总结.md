# Towards context-aware graph representation learning: Adaptive node aggregation with LLMs 总结

## 基本信息

- **标题**: Towards context-aware graph representation learning: Adaptive node aggregation with LLMs
- **作者**: Songwei Zhao, Yuan Jiang, Sinuo Zhang, Jifeng Hu, Philip S. Yu, Hechang Chen
- **期刊 / 会议**: Artificial Intelligence 358 (2026) 104584
- **发表**: 2026-06-14（2025-06-23 投稿，2026-04-23 修回，2026-06-06 录用）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104584
- **arXiv**: 无
- **PDF**: [AIJ_2026_AdaptiveNodeAggregationLLM.pdf](papers/AIJ_2026_AdaptiveNodeAggregationLLM.pdf)

## 一句话概括

本文提出 LTNA：利用大模型上下文推理能力为文本属性图的每个节点定制语义驱动的聚合策略，使 GNN 消息传递从固定数值聚合变为上下文敏感的语义操作。

## 问题与动机

文本属性图（TAG）上节点同时携带图结构与文本属性，表示学习对节点分类等任务至关重要。传统 GNN 用固定的 sum/mean/max 等聚合函数在浅层文本特征上做消息传递，难以建模节点间复杂语义关系，容易信息丢失或过度平滑；最近工作引入 LLM 增强节点特征，但大多把 LLM 当作静态编码器，忽视其推理能力，聚合器仍未针对节点上下文设计。例如引文网络中一篇论文引用他人可能是背景支撑、批判反驳或工作延伸，固定聚合无法区分这些微妙语义；电影评论与粉丝周边消费场景也表明单一聚合器无法适应多样化需求。作者因此提出核心问题：如何设计上下文感知、语义驱动的聚合策略，让每个节点根据邻居的关系语义选择性整合邻居信息。

## 方法

作者提出 LLM-based Tailored Node Aggregation（LTNA）框架。整体流程是：将节点的文本属性（如引文网络的标题、摘要）与其邻居文本组织成结构化提示 p(v)，输入冻结的 LLM（默认 LLaMa3-8B），由 LLM 依次完成 Select–Explain–Act 三阶段：先依据语义相似度、上下文等推理策略挑选至多 k 个有价值的邻居（SelectLLM）；再解释目标节点与各邻居的语义关系（如 supportive/critical/background/irrelevant，ExplainLLM）；最后据此输出可执行的自适应聚合策略 gv（ActLLM），即"谁聚合、如何聚合"由 LLM 统一决策，得到节点嵌入 hv=gv({hu})。生成的聚合器不是固定的解析函数，而是可分配邻居权重、选择聚合模式乃至构造非线性规则的语义策略，全程单次前向推理、无需微调或反向传播；训练时仅更新下游分类器参数（交叉熵 + L2 正则），LLM 保持冻结，属于即插即用与上下文元学习范式。论文还以 Borsuk-Ulam 定理证明：要使 N 个节点表示完全可区分至少需要 N 个不同聚合器（定理 1），以此说明逐节点定制聚合器的必要性。

## 实验与结果

作者在五个基准数据集（CORA 2708 节点、CITESEER 3186、PUBMED 19717、OGBN-ARXIV 169343、OGBN-PRODUCTS 约 54K 节点子图）上以 Accuracy 与 Macro-F1 为指标，与 13 个基线（MLP、GCN、GAT、GraphSAGE、MixHop、APPNP、GPR-GNN、RNCGLN、GCN+ReP、IDGL、GraphNAS 以及 TAPE、GLEM、GraphEdit、OFA 等 LLM 增强模型）比较。LTNA（LLaMa3-8B）在五个数据集全面领先：Accuracy 相对最优基线平均提升 7.95%、Macro-F1 平均提升 9.90%，单数据集 Accuracy 相对提升分别为 4.55%/10.44%/3.38%/6.69%/14.70%，例如 CORA 达 91.04（最优基线 87.08）、CITESEER 达 85.24（最优基线 77.18）、PRODUCTS 达 81.71（最优基线 71.24）。与同类 LLM 方法比，LLaMa3-8B 版 LTNA 在 CORA/PUBMED/ARXIV 上均优于 TAPE、GLEM、GraphEdit、OFA、GraphAlign、GRADMLP；换用 Qwen3-32B 略升（CORA 92.70）但成本大幅上升，故以 LLaMa3-8B 为主干。消融显示 LLM+MLP（无聚合）与 LLM+GCN（固定聚合）在全部数据集上明显差于带自适应聚合器的 LTNA；t-SNE 可视化显示其嵌入类别簇清晰分离；敏感性分析表明采样邻居数 k 的最优值接近平均节点度（PUBMED 4.50、ARXIV 13.67），超过后易过度平滑，实验中 ARXIV 取 k=10、PUBMED 先升后降。资源分析（4×L40 GPU 上批量推理）显示各数据集延迟 0.10–0.31 秒、吞吐 3.16–10.17 节点/秒，主要开销来自 LLM 前向推理而非训练。

## 贡献与局限

主要贡献：提出 LTNA，首次将 LLM 的上下文推理能力嵌入 GNN 的消息传递阶段，为每个节点生成语义感知的定制聚合器，突破固定统一聚合范式，实现"从参数加权聚合到语义驱动推理"的范式转变；通过统一 Select–Explain–Act 的单提示设计，让聚合器自适应采样高相关邻居并抑制噪声，缓解过度平滑与信息损失，且无需对 LLM 做任何训练或微调；在五个公开基准上相对最优基线平均提升 Accuracy 7.95%、Macro-F1 9.90%，全面验证逐节点定制聚合的必要性与广泛适用性。局限方面：聚合目前只考虑一跳邻居，难以捕捉全局图信息；提示设计仍依赖人工，有待让模型自我提示优化提示词；引入 LLM 使大规模数据集上的计算开销偏高，未来将探索多跳聚合、LLM 自适应提示设计与效率优化。

---
DOI: 10.1016/j.artint.2026.104584
