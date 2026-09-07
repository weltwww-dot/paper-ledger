# Retrieval-augmented and feedback-optimized large language model for recommendation 总结

## 基本信息

- **标题**: Retrieval-augmented and feedback-optimized large language model for recommendation
- **作者**: Zhisheng Yang, Li Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108954
- **arXiv**: 无
- **PDF**: [NN_2026_RetrievalAugmentedFeedbackLLM.pdf](papers/NN_2026_RetrievalAugmentedFeedbackLLM.pdf)

## 一句话概括

提出一种无需微调大模型的检索增强与反馈优化闭环推荐框架 KDRAG-Critic-LLM-RS，从用户与物品两侧挖掘协同信号，显著提升推荐的准确性、个性化与鲁棒性。

## 问题与动机

"LLM-as-Recommender" 范式虽具备强大生成能力，但面临四方面挑战：缺乏对协同过滤信号的有效整合、输入长度受限难以编码完整用户历史、预训练 LLM 静态且重训/微调成本高、真实行为数据含噪声且缺少结构化反馈机制。现有 LLM 推荐方法多依赖静态预训练检索器或固定图先验，难以适应行为漂移、数据噪声与冷启动，也极少利用生成反馈在线优化检索。为此本文提出 KDRAG-Critic-LLM-RS，以检索—生成—反馈闭环同时利用用户侧与物品侧协同信息，无需修改底层 LLM 参数即可持续优化推荐质量。

## 方法

框架由三部分构成：预训练大语言模型（实验用 Vicuna-1.5 7B，并扩展到黑盒 GPT4o_mini）、KDTreeRAG 检索模块和 R-Critic 评分反馈模块。KDTreeRAG 基于用户协同过滤：用预训练检索器（如 Contriever）把用户交互序列编码为稠密嵌入，建立 KDTree 空间索引，检索 top-10 行为相似用户的历史（标题+评分）构建分布式 prompt，LLM 对每个相似用户生成 10 条候选、按出现频率排序选出 Top-10；检索器通过最小化与基于 R-Critic 聚合分数的 softmax 目标分布间的 KL 散度训练（Adam 优化、周期重建索引），实现无需更新 LLM 的在线检索优化。R-Critic 基于物品协同过滤：用 BERT 编码用户历史物品与待评物品，历史长度截断/补零至固定上限后送入含 ReLU 的多层全连接网络，将评分离散为 10 个宽度 0.5 的区间标签做交叉熵分类训练；对预测评分低于 4 的候选生成自然语言负面反馈，约束下一轮 prompt 并重新检索生成，形成 retrieve→generate→feedback 闭环。每用户默认 k=10 次生成调用加 1 次 critic 评估（时延约 k·T_LLM + r·T_Critic），并有 3-retrieve/3-critic 变体做开销权衡分析。

## 实验与结果

在 Movie 与 Book 两个真实数据集上评测：Movie 源自 MovieLens（247,383 用户、84,661 部电影，评分 0.5–5、步长 0.5），Book 源自 Book-Crossing（350,332 用户、9,374 本书，评分 1–5、步长 1）。实验在 8 核 CPU、64GB 内存、RTX 3090 集群上进行：各用 3k 用户完整历史输入 KDTreeRAG，10k 用户按 8:1:1 划分训练 R-Critic（每用户 20 个已评分物品+1 候选），另选 1000 个未参与训练的用户（各 20 条已评分历史）测试，指标为 Precision、HR、NDCG@3/5/10，偏好物品定义为评分≥4；对无真实评分的自由生成采用 30k 用户训练的 Oracle 模型估分（Movie 上 micro-P/micro-R 达 0.7720/0.6913，Book 上为 0.7765/0.6952）。完整模型 KCLLM-RS 在 Oracle 设置下：Book PR@10=0.5786、HR@10=0.7950、NDCG@10=0.6865；Movie PR@10=0.3792、HR@10=0.7660、NDCG@10=0.6088，全面优于 GPTRec、GENREC、InteraRec、Llama4Rec、LLM-FT、LLM-KM、LLM-BTE、ARAG-RS、RRAG-RS 等 13 个基线；候选集设置下 Book PR@10=0.5715、HR@10=0.9260、NDCG@10=0.8065，Movie PR@10=0.4050、HR@10=0.8520、NDCG@10=0.7447。RQ3 显示黑盒 GPT4o_mini 加入检索与反馈后各指标随反馈轮数（R1–R3）持续提升；RQ4 表明性能在第一轮反馈后即收敛，单轮即可达到高质量；RQ5 中 R-Critic 作批评者显著优于 LLM 作批评者；RQ6 中 KDTreeRAG 优于标准 RAG 检索；RQ7 消融（仅 LLM、静态 top-K、仅检索、仅反馈、完整模型）显示所有部分增强变体均优于仅用 LLM 的基线，完整模型最优；RQ8 电影案例分析显示推荐列表真实评分更高、排序更准；RQ9 表明端到端时延随反馈轮数近似线性累积，无额外系统性开销。

## 贡献与局限

贡献：(1) 提出即插即用、无需微调或改动参数（可挂接黑盒大模型）的 KDRAG-Critic-LLM-RS 闭环框架，统一用户侧协同检索与物品侧协同反馈；(2) 设计基于 KDTree 近邻搜索的快速用户检索模块 KDTreeRAG 与把连续预测评分转化为简洁文本指导、迭代修正候选的轻量评分回归器 R-Critic；(3) 提供利用生成反馈在线优化检索器而不更新 LLM 的端到端训练/评测方案，避免高频 LLM 重训练成本，缓解噪声数据影响并突破输入长度限制，增强对偏好漂移与冷启动的适应性；(4) 电影与图书基准上 Precision/HR/NDCG 一致领先，且保持实际推理效率。局限：R-Critic 仅以显式评分作为监督，未纳入隐式反馈；未来工作拟通过把交互事件映射为置信度加权目标，或采用带曝光校正的 BPR 式成对/列表式目标来支持纯隐式反馈场景。研究受国家自然科学基金（61877051）资助。

---
DOI: 10.1016/j.neunet.2026.108954
