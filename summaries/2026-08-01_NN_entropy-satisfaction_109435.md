# Entropy-aware filtering and hierarchical attention: A hybrid neural framework for fine-grained user satisfaction modeling 总结

## 基本信息
- **标题**: Entropy-aware filtering and hierarchical attention: A hybrid neural framework for fine-grained user satisfaction modeling
- **作者**: Huiran Liu、Zheng Wang、Zhiming Fang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109435
- **发表**: 2026-08-01
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109435

## 一句话概括
MSA-DLFO针对评论冗余及满意度多维难量化，结合熵筛选、层次情感建模和模糊排序，在18,559条评论上超过12种基线，但领域迁移仍待验证。

## 问题与动机
如何从评论提取细粒度情绪并形成多属性满意度排序？

## 方法
单位熵筛选评论，领域适配和对比学习提取特征，BERT层次门控预测情感，再用置信度、模糊TOPSIS和OWA排序。

## 实验与结果
出行服务18,559条评论五折评估，准确率、F1、AUC较12基线提升1.4%–5.6%，标注κ=0.81；领域阈值AUC仅增0.002且小样本新城市可能不稳（PDF第9–11页）。

## 贡献与局限
整合评论筛选、情绪估计与模糊排序；证据来自单一服务领域。

---
DOI: 10.1016/j.neunet.2026.109435
