# Multi-View Multi-Label Feature Selection Based on View-Specific Implicit Label and Adaptive View-Driven Unified Feature Learning 总结

## 基本信息
- **标题**: Multi-View Multi-Label Feature Selection Based on View-Specific Implicit Label and Adaptive View-Driven Unified Feature Learning
- **作者**: Jianhua Dai、Shiyu Wei、Xinwang Liu
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8354-8366
- **发表**: 2026-09-22
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3736667

## 一句话概括
VIL-AVUFL针对多视图多标签特征选择，联合学习增强的共享视图与各视图隐式标签，以减少噪声冗余并保留视图差异。

## 问题与动机
既有方法难以在提取视图专属语义时保持共享标签完整，也不易在各视图质量不均、特征含噪时可靠融合信息。

## 方法
模型从各视图特征学习隐式标签，以HSIC抑制跨视图冗余；同时构造统一增强特征空间、自适应学习视图表示，并用稀疏约束排序选出的特征。

## 实验与结果
在七个多视图多标签数据集、四项指标上比较后，方法取得最佳平均排名；Emotions的随机特征噪声实验中，20组比较有超过半数排名第一，系统偏移实验中12/20次进入前二（PDF第7–11页）。

## 贡献与局限
消融结果显示隐式标签和统一视图等模块均有贡献；参数最优值随数据集而变，噪声鲁棒性结果主要来自Emotions等受控扰动设置，尚不能代表所有真实噪声（PDF第9–11页）。

---
DOI: 10.1109/tkde.2026.3736667
