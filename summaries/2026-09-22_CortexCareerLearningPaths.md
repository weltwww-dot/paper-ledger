# Cortex: A Retrieval-Augmented Framework for Career-Aligned Learning Paths 总结

## 基本信息
- **标题**: Cortex: A Retrieval-Augmented Framework for Career-Aligned Learning Paths
- **作者**: Vatsala Ramachandran、Manasvi Vedanta、Sonia Khetarpaul
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-22
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07160-5
- **PDF**: [ML_2026_CortexCareerLearningPaths.pdf](papers/ML_2026_CortexCareerLearningPaths.pdf)

## 一句话概括
Cortex 将检索增强生成、语义职业匹配与 ESCO 技能知识图谱结合，把兴趣和目标职业转化为受先修关系约束的学习路径。

## 问题与动机
关键词式职业推荐会遗漏语义相近但措辞不同的兴趣表达；通用生成模型也可能给出不符合职业技能体系或先修顺序的建议。作者希望改善语义匹配并增强技能路径的可追溯性。

## 方法
系统以句向量检索学习者兴趣与职业描述，结合检索增强生成和 ESCO 职业—技能图谱生成技能序列；生成受分类体系及先修关系约束。评估比较 BM25 与语义嵌入匹配，并检查约束对技能覆盖的影响。

## 实验与结果
论文报告语义嵌入的职业匹配优于 BM25；TF-IDF 的差异方向为正但未达到统计显著。ESCO 约束使生成技能保持在体系定义范围内，无约束生成的有效技能覆盖接近于零。语义错误率未被量化，社区反馈只模拟一轮。

## 贡献与局限
- 组合职业语义匹配、技能知识图谱与检索增强生成，构造学习路径框架。
- 通过知识体系约束减少无效技能项。
- 尚未在真实学习者长期使用中验证；反馈轮次有限，且结构合规不代表建议必然适合个人。

---
DOI: 10.1007/s10994-026-07160-5
