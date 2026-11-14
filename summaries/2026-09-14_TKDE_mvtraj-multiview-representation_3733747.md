# Context-Enhanced Multi-View Trajectory Representation Learning: Bridging the Gap Through Self-Supervised Models 总结

## 基本信息
- **标题**: Context-Enhanced Multi-View Trajectory Representation Learning: Bridging the Gap Through Self-Supervised Models
- **作者**: Tangwen Qian、Junhe Li、Yile Chen 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8042-8053
- **发表**: 2026-09-14
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3733747

## 一句话概括
MVTraj融合 GPS、道路路线和网格/兴趣点上下文，学习可迁移的轨迹表示，以弥补单一空间视图难以同时表达运动细节、道路拓扑与地点语义的问题。

## 问题与动机
不同空间视图结构不一致，单视图编码又会遗漏互补信息；如何对齐同一移动过程并有效融合多源上下文？

## 方法
模型以 GPS 轨迹作为桥梁，通过自监督对比任务对齐 GPS、路线和网格视图，再用分层跨模态交互及共享 Transformer 融合表示。

## 实验与结果
在西安与成都真实数据上评估轨迹及路段任务；成都行程时间估计相较 MM-Path 的 MAE 降低 41.37%、RMSE 降低 33.68%，网格目的地预测也优于所比较基线（PDF 第 8 页）。

## 贡献与局限
多视图表示在多类下游任务展现收益，并增强跨城市任务适用性。作者指出仍需改进空间划分、外部 POI 知识、推理压缩，以及稀疏或超长轨迹处理，当前结论限于两个城市数据。

---
DOI: 10.1109/tkde.2026.3733747
