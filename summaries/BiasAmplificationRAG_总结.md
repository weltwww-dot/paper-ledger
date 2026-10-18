# Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs 总结

## 基本信息

- **标题**: Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs
- **作者**: Linlin Wang, Tianqing Zhu, Laiqiao Qin et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing · 2026
- **发表**: 2026-07-02
- **日期来源**: 出版社正式PDF第1页Date of publication；卷期及current version不替代首次在线日期
- **内容状态**: 完整
- **内容说明**: 已对照18页正式版复核方法、实验及边界，主agent亲自审定中文
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3709319
- **版本**: 出版社正式版（Version of Record），18页，卷/期/页23/5/11033-11050
- **PDF**: [TDSC_2026_BiasAmplificationRAG.pdf](papers/TDSC_2026_BiasAmplificationRAG.pdf)

## 一句话概括

BRRA通过知识库投毒、检索排序操纵和输出反馈，研究RAG如何放大大模型的社会偏见，并探索检索与生成两阶段缓解。

## 问题与动机

现有RAG投毒研究偏重事实性错误，较少检验看似可信的检索文档如何改变群体偏见。论文将偏见放大视为独立风险，比较不同模型、群体维度和问题情境下的变化。

## 方法

以可信度、权威性、偏见诱导和检索效果等奖励优化投毒文档；分别用子空间投影与词频优化影响稠密、稀疏检索，再把回答反馈回知识库。防御结合多查询检索扰动与生成阶段公平性约束（PDF第5—9页）。

## 实验与结果

覆盖GPT-4o-mini、DeepSeek-R1、Qwen-2.5-32B、Llama-3-8B，使用BBQ、StereoSet和三种检索器。在BBQ性别任务、GPT-4o-mini与E5-base-v2这一组设置中，正负情境的偏见选择率均为80%，偏见放大因子分别为2.4、3；不能推广为所有设置的平均结果。双阶段防御减轻偏见，但未消除BRRA影响（PDF第10—15页）。

## 贡献与局限

贡献是把知识投毒、检索操纵与反馈累积纳入统一偏见评估。实验聚焦单轮检索，尚未充分覆盖混合检索、GraphRAG及多轮交互；防御仅是可行性验证和研究基线，不是可直接部署的完整方案（PDF第16—17页）。

---
DOI: 10.1109/tdsc.2026.3709319 | PDF: [TDSC_2026_BiasAmplificationRAG.pdf](papers/TDSC_2026_BiasAmplificationRAG.pdf)
