# DRE: An effective dual-refined method for integrating small and large language models in open-domain dialogue evaluation 总结

## 基本信息
- **标题**: DRE: An effective dual-refined method for integrating small and large language models in open-domain dialogue evaluation
- **作者**: Kun Zhao、Bohao Yang、Chen Tang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109574
- **发表**: 2026-08-31
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109574

## 一句话概括
DRE先让小模型提供对话响应线索以引导大模型初评，再用小模型信息校正评分，提升自动评价与人类判断的一致性。

## 问题与动机
开放域对话常有多个合理回答，单一大模型评估容易在含糊样本上不稳定，小模型虽能区分正向响应，却易受误导性输入影响。传统词面指标与人类判断相关性有限，且数据稀缺和话题覆盖不足妨碍专用评估器训练。

## 方法
作者先以对比学习训练小语言模型，使上下文、正向响应及对抗负例形成可区分表征，并从稳健子空间计算响应概率和余弦距离。SLIDE把这些分数与大模型评分自适应整合；DRE进一步分两阶段使用小模型线索：先写入结构化提示辅助大模型初评，再估计影响系数，对评分二次修正。论文还扩充多个正向和对抗负向响应样本。

## 实验与结果
在DailyDialog++、TopicalChat和PersonaChat三个开放域数据集上，用Pearson/Spearman相关系数比较自动分数与人工判断，并测试GPT-3.5、Claude、Gemini。表5中GPT-3.5版DRE的Pearson相关分别为0.744、0.729、0.742，Spearman为0.688、0.748、0.755；相较非DRE GPT-3.5，各数据集相关性均提高。SLIDE合并小模型距离与概率在TopicalChat Pearson相关为0.741，优于单独小模型分数。

## 贡献与局限
DRE利用小模型与大模型在正负响应识别上的互补性，以提示引导和评分再校正双阶段组合，三个数据集上与人工判断的相关性均改善。人工评估质量受数据集构造、标注者和LLM裁判影响；实验基于特定模型版本与有限对话语料，跨语言、长对话和在线评估成本仍需验证。

---
DOI: 10.1016/j.neunet.2026.109574
