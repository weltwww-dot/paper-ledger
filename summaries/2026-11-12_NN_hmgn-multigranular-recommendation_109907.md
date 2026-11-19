# HMGN: A multigranular GNN for heterogeneous preference modeling in knowledge-aware recommender systems 总结

## 基本信息
- **标题**: HMGN: A multigranular GNN for heterogeneous preference modeling in knowledge-aware recommender systems
- **作者**: Ran Chen、Ruili Sun、Huaguang Zhu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109907
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109907

## 一句话概括
HMGN 用异质感知多尺度卷积和多粒度知识传播，适配不同活跃度用户并区分知识图谱邻居的贡献。

## 问题与动机
知识图谱推荐常偏重物品侧传播，对用户交互所体现的偏好结构差异关注不足；不同关系、实体及高阶邻居贡献也难区分，深层传播还会过平滑。

## 方法
异质感知多尺度卷积通过可微稀疏核选择与 Sparsemax 自适应选取感受野，建模局部到全局偏好；多粒度知识感知传播结合多头交互注意力、深层语义扩散与逐层融合，按用户条件加权多跳实体关系。

## 实验与结果
在电影、餐饮和音乐等数据集上与知识图谱推荐基线比较，报告 AUC、F1、命中率，并分析传播深度和邻居采样数。论文称多数设置优于对照；电影数据的 Hit@5 表中 HMGN 为 87.9%，高于表列 CKAN 的 81.3%，且深度增加时性能退化较缓。

## 贡献与局限
将用户偏好异质性与知识图谱多跳语义贡献放进统一推荐模型，并通过稀疏核选择适应活动水平。证据限于文中三类数据及离线排序指标；从报告实验看，跨平台真实部署、在线反馈和冷启动效果尚未得到验证。

---
DOI: 10.1016/j.neunet.2026.109907
