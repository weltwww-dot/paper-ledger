# CTISum: A new benchmark dataset for Cyber Threat Intelligence summarization 总结

## 基本信息

- **标题**: CTISum: A new benchmark dataset for Cyber Threat Intelligence summarization
- **作者**: Wei Peng, Junmei Ding, Wei Wang, Lei Cui, Wei Cai, Zhiyu Hao, Xiaochun Yun
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104928
- **arXiv**: 2408.06576v2
- **PDF**: [COSE_2026_CTISumBenchmark.pdf](papers/COSE_2026_CTISumBenchmark.pdf)

## 一句话概括

本文构建了网络安全领域首个面向网络威胁情报（CTI）报告摘要的基准数据集 CTISum，除通用 CTI 摘要任务（CTIS）外还提出细粒度攻击过程摘要子任务（APS），实验表明现有抽取式、生成式乃至零样本大模型方法在该基准上仍面临显著挑战。

## 问题与动机

CTI 数据通常来自论坛、博客与开源仓库等多样化 web 来源，信息碎片化且体量大，分析师难以快速定位高价值情报，因此需要自动把长篇 CTI 报告压缩成简洁、准确、可支撑决策的摘要；但网络安全领域的 CTI 摘要研究长期受制于缺乏合适数据集。CTI 报告具有技术术语密集、威胁态势快速演变、篇幅长、信息分散等特点，使标注与评测都相当困难；而传统深度摘要模型通常无法处理超过 512/1024 token 的长输入，通用语料预训练的大语言模型在特定安全领域零样本任务上也表现欠佳。为填补这一空白，作者构建 CTISum，并在通用摘要之外提出关注攻击过程理解的细粒度 APS 子任务，以帮助防御者评估风险、识别安全缺口与漏洞。

## 方法

论文设计了四阶段多阶段标注流水线来构建数据集：数据收集阶段从三类来源（如 APTnotes 等开源报告、Trendmicro 等威胁百科、Symantec 等安全公司报告）采集覆盖 2016–2024 年的 CTI 报告并抽样 1,345 篇；解析与清洗阶段用 PDF 解析工具抽取文本，再以人工规则和正则表达式过滤噪音（连续 IP、哈希、非英文字符、目录省略号等）；提示词方案阶段由 CTI 专家针对 CTIS 与 APS 设计提示模板（关键事件高亮、连贯摘要、补充要点、判断是否存在攻击过程、列出/抽取攻击过程）；情报摘要阶段用 GPT-4o、Claude2/3.5、ChatGLM3 等 LLM 生成多个候选粗粒度摘要，再由三名领域专家评审、排名并合并出最终金标准摘要，质量不佳的样例被丢弃，LLM 与专家协作实现半自动标注。CTISum 是唯一带子任务的摘要数据集：平均文档长 2,865.60 词，CTI 摘要平均 200.04 词（压缩比 14.32），APS 摘要平均 118.27 词（压缩比 22.23）。

## 实验与结果

作者对数据集按 8:1:1 划分训练/验证/测试，用 ROUGE-1/2/L 与 BERTScore 对抽取式（BertSumExt、MatchSum）、生成式（Transformer、T5-base、BART-base、BART-large）及长文档/LLM（Longformer、LLAMA2-7B、GPT-4o 零样本）方法进行评测。结果表明：抽取式模型在两任务上几乎最差但 BERTScore 最高（因其基于 BERT）；BART-large（约 374M）最优，测试集 CTIS 上 ROUGE-L 达 29.03、APS 上达 25.06，相对 MatchSum 在 ROUGE-L 上分别提升约 10.12% 与 6.18%；Longformer（102M）与 BART-base（约 121M）表现相当；零样本的 LLAMA2-7B 与 GPT-4o 未带来进一步提升，且两任务中 APS 普遍更难。人工 A/B 评测（约 80 条随机样本、三名分析师多数投票，从事实正确性、相关性、覆盖度三方面）中 BART-large 优于 Longformer，例如 CTIS 覆盖度 BART 更优占 46.67%、Longformer 仅 20.00%，但相关性上优势不显著。Fleiss Kappa 一致性为 0.37（5 名专家、50 条摘要），评分≥3 的摘要占 96.4%（241/250），合并分箱后 Kappa 升至 0.61。输入长度分析显示 BART-base 在输入增长至 1024 token 内性能持续提升，Longformer 在 3500 token（长度分布 75 分位）时最优；少样本实验中 BART-base 随训练数据从 10% 增至 100% 性能持续上升，APS 在低资源设置下表现更差；案例分析还发现模型幻觉与事实不一致，如时间信息混淆及攻击链细节（OLE、Equation Editor）的虚构。

## 贡献与局限

- 贡献一：据作者所述首次在网络安全领域构建含 CTIS 任务与新颖 APS 子任务的 CTI 摘要基准 CTISum（1,345 篇文档，覆盖 2016–2024 的多样 web 来源）。
- 贡献二：设计了 LLM 辅助、人工质量把关的多阶段标注流水线（数据收集、解析清洗、提示词方案、智能摘要四阶段）。
- 贡献三：对抽取式、生成式、长文档与大模型方法做了全面基准评测，证明现有 SOTA 在该任务上仍有较大提升空间，自动摘要 CTI 报告仍是开放问题；代码与示例数据将公开于 GitHub（pengwei-iie/CTISum）。
- 局限：CTI 摘要（尤其 APS）因攻击行为多变、隐蔽、复杂而挑战大，模型易产生幻觉与事实不一致；人工一致性的 Fleiss Kappa 仅 0.37；零样本 LLM 表现不佳且 LLM 微调资源消耗大；未来可沿领域 LLM 微调、少样本学习、迁移学习、数据增强及面向攻击行为内在复杂性的摘要技术适配等方向推进。

---
DOI: 10.1016/j.cose.2026.104928
