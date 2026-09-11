# CTISum: A new benchmark dataset for Cyber Threat Intelligence summarization

## 基本信息

- 标题: CTISum: A new benchmark dataset for Cyber Threat Intelligence summarization
- 作者: Wei Peng, Junmei Ding, Wei Wang, Lei Cui, Wei Cai, Zhiyu Hao, Xiaochun Yun
- 期刊 / 会议: Computers & Security 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1016/j.cose.2026.104928
- PDF: [COSE_2026_CTISumBenchmark.pdf](papers/COSE_2026_CTISumBenchmark.pdf)

- 标题: CTISum: A new benchmark dataset for Cyber Threat Intelligence summarization
- 作者: Wei Peng, Junmei Ding, Wei Wang, Lei Cui, Wei Cai, Zhiyu Hao, Xiaochun Yun
- 期刊 / 会议: Computers & Security 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

作者为 Wei Peng、Junmei Ding、Wei Wang、Lei Cui、Wei Cai、Zhiyu Hao、Xiaochun Yun；发表于 *Computers & Security* 168 (2026) 104928。论文发布 CTISum 网络威胁情报摘要基准，包含常规 CTI 摘要（CTIS）和新增攻击过程摘要（APS）子任务。DOI: 10.1016/j.cose.2026.104928
## 一句话概括

CTISum 以多来源 CTI 文档、人工—大模型协同标注和攻击过程专门摘要任务，为评估长文本威胁情报摘要的事实性、完整性和安全语气提供基准。

## 问题与动机

CTI 文档长、术语密集、包含实体与时间线，普通新闻摘要指标难以反映攻击链是否完整、关键 IOC 是否保留以及是否出现安全语义错误。既有公开数据集也缺少面向攻击过程的独立任务。论文的目标是建立可复现的数据和标注方案，并用代表性摘要模型验证任务难度和数据质量。

## 方法

数据来自 APTnotes、Trend Micro、Symantec、CTI 团队及 2016–2025 年相关资料，经过 PDF 解析、清洗和结构化。对每篇文档设计 CTIS 与 APS 提示模板，使用 GPT-4o、Claude、ChatGLM3 等生成候选摘要，再由 3 名专家按事实/幻觉、完整性、冗余和安全语气评价；约 15% 样本双重标注并进行校准。最终从 1463 篇候选文档中剔除 92 篇，保留 1371 篇，按 8:1:1 划分训练、验证和测试集，比较 MatchSum、Transformer、T5、BART、Longformer、LLaMA2 和 GPT-4o 等模型。

## 实验与结果

文档平均约 2865.60 词，CTIS 摘要平均 200.04 词，APS 摘要平均 118.27 词，压缩比分别约 14.32 和 22.23。监督模型中 BART-large 的基线表现最好；CTIS 测试集上 BERTScore、ROUGE-1/2/L 为 70.41、45.76、16.88、29.03，Longformer 为 70.31、45.39、15.66、27.09；GPT-4o 零样本为 64.31、38.70、12.71、22.98，LLaMA2 更弱。人工比较中 BART 多数情况下优于 Longformer；原始 Fleiss κ 为 0.37，合并等级后为 0.613，96.4% 评分不低于 3。错误主要包括实体/时间幻觉、遗漏或重排攻击步骤；APS 比 CTIS 更难。

## 贡献与局限

贡献是提供首个同时覆盖 CTI 摘要和攻击过程摘要的基准，并将专家规则、LLM 候选生成和质量控制结合起来。局限是数据主要为英文和公开来源，专家一致性仍有限，样本与来源分布可能影响泛化，当前基线也不代表所有最新模型；摘要质量还受长文解析、实体时间线和幻觉控制约束。后续需扩大来源、提供更丰富标注并完善事实级评价。

DOI: 10.1016/j.cose.2026.104928
