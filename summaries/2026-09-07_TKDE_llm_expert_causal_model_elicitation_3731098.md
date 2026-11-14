# Augmenting Expert Elicitation With LLMs for Building Causal Models to Aid Decision Making 总结

## 基本信息
- **标题**: Augmenting Expert Elicitation With LLMs for Building Causal Models to Aid Decision Making
- **作者**: Olha Shaposhnyk、Svetlana Yanushkevich
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，7979-7990
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3731098
- **PDF**: [TKDE_2026_llm_expert_causal_model_elicitation_3731098.pdf](papers/TKDE_2026_llm_expert_causal_model_elicitation_3731098.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
研究考察大语言模型能否补充专家，为医学决策支持整理因果结构。作者针对措辞敏感性，对变量对使用七种因果连接词分别询问并投票；结果显示多提示聚合能降低单一措辞偏差，但复杂网络仍会失真。

## 问题与动机
多种提示措辞的共识，能否让模型生成的医学因果图更接近基准结构？

## 方法
将模型生成图与五类医学诊断基准比较，以结构汉明距离和边召回误差评估；每对变量用七种连接词询问，再通过多数票决定边是否保留，并分析投票阈值。

## 实验与结果
阈值敏感性实验发现七种措辞中至少四种同意时，结构汉明距离总体较低；阈值过宽易纳入语言噪声，过严又可能漏边。COVID-19 与医学诊断等复杂数据仍出现明显结构扭曲（PDF 第 8、10 页）。研究是基准图对照，不能证明模型发现了真实临床因果关系，且结论受提示词、模型和基准质量影响。

## 贡献与局限
以多提示投票缓和因果关系抽取对措辞的敏感性，并用结构指标检验其边界。结果支持将模型作为专家稀缺时的辅助来源，而非替代领域验证；复杂诊断网络上的失真是明确限制。

---
DOI: 10.1109/tkde.2026.3731098 | PDF: [TKDE_2026_llm_expert_causal_model_elicitation_3731098.pdf](papers/TKDE_2026_llm_expert_causal_model_elicitation_3731098.pdf)
