# DR-EFT: Exploring and reloading domain-representative experts for the memory-constrained fine-tuning of MoE large models 总结

## 基本信息
- **标题**: DR-EFT: Exploring and reloading domain-representative experts for the memory-constrained fine-tuning of MoE large models
- **作者**: Zhaomeng Cheng、Zhong Ji、Yan Zhang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109469
- **发表**: 2026-08-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109469

## 一句话概括
DR-EFT 通过识别并选择领域代表性专家来降低 MoE 大模型微调的显存负担，实验显示其在若干语言任务上保持竞争力，但效果依赖领域专家选择与切换策略。

## 问题与动机
在显存受限时，能否不改变 MoE 架构而只加载领域相关专家完成有效微调？

## 方法
框架先在量化模型中探索领域代表性专家，再对选中专家微调并重新装载至原精度模型；同时设计专家动态与连续微调策略，以适配任务域变化。

## 实验与结果
在三类任务及多个数据集上评估，并报告生成任务 ROUGE、问答与分类指标及消融结果；文中结果显示选取领域专家可在降低训练资源需求的同时保持任务表现，但任务间及专家切换设置的指标有所波动（PDF 第6–11页）。

## 贡献与局限
提出无需改动 MoE 结构的领域专家探索、微调与重载流程，面向资源受限的大模型适配；实验范围集中于所选模型和任务，迁移效果仍取决于专家代表性及动态切换配置。

---
DOI: 10.1016/j.neunet.2026.109469
