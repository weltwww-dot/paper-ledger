# TriP: A triple-prompt framework aligning pre-training and class-incremental objectives in continual graph learning 总结

## 基本信息
- **标题**: TriP: A triple-prompt framework aligning pre-training and class-incremental objectives in continual graph learning
- **作者**: Can-Ming Cui、Hui-Yu Zhou、Pei-Yuan Lai 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109447
- **发表**: 2026-08-02
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109447

## 一句话概括
TriP针对持续图学习目标不一致及历史回放成本，以三类提示协调预训练与类别增量任务，在四个基准降低训练开销，但推理增加查询成本。

## 问题与动机
如何冻结预训练GNN并持续学习新类别、减少历史数据存储？

## 方法
对比式自监督预训练GNN，后续只更新提示并维护类别原型，以统一模板把分类转为相似度目标。

## 实验与结果
在Arxiv、CoraFull、Products、Reddit增量设置比较准确率、遗忘和效率；可训练参数少且训练快于CaT、DeLoMe，但推理慢于部分回放基线（PDF第6–9页）。

## 贡献与局限
降低持续图学习的历史数据需求；仅评估四个数据集及既定任务序列。

---
DOI: 10.1016/j.neunet.2026.109447
