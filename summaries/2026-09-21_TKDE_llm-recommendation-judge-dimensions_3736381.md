# What Do LLM Judges Evaluate in Recommendation Assessment? Disentangling Relevance, Local Diversity, and System-Level Diversity 总结

## 基本信息
- **标题**: What Do LLM Judges Evaluate in Recommendation Assessment? Disentangling Relevance, Local Diversity, and System-Level Diversity
- **作者**: Yunan Zhang、Jingjing Fan、Yanxiao Liu
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8591-8603
- **发表**: 2026-09-21
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3736381

## 一句话概括
大语言模型正被用来评判推荐列表，但单个用户看到的局部列表多样性与全系统覆盖率并非同一概念。本文系统检验评判模型的偏好对应哪些推荐质量维度，指出提示中的局部线索无法替代需要全体用户曝光数据的全局指标。

## 问题与动机
LLM 评判者在准确率与多样性冲突时偏向哪一方？仅看两份用户列表，能否可靠评估覆盖率等系统级多样性？

## 方法
作者构造准确率与多样性指标意见相反的推荐模型对，比较四种提示、多个数据集和不同规模及家族的评判模型；以指标胜者对齐率衡量偏好，并通过人类小规模核验及跨模型复现检验结论。

## 实验与结果
研究覆盖 19,240 次模型调用、四个数据集和 16 组模型对。标准提示在冲突样本中有 86.7% 与 NDCG 胜者一致；多样性提示与系统 Coverage 胜者仅 38.0% 一致，却与提示可见的类别数、类别熵和文本差异分别有 83.7%、80.5%、63.2% 一致（PDF 第 1 页）。局限是评判输入仅包含局部列表，且人类核验规模较小。

## 贡献与局限
贡献是实证区分 LLM 可判断的局部文本多样性与需全局数据计算的曝光覆盖，并给出适用边界。局限在于对齐率是统计关联，不代表模型实际计算了相应指标；涉及系统级公平或覆盖时仍须报告直接量化指标。

---
DOI: 10.1109/tkde.2026.3736381
