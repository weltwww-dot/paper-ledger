# Beyond temporal encoding: Efficient and hierarchical model-level online adaptation for tabular distribution shift 总结

## 基本信息
- **标题**: Beyond temporal encoding: Efficient and hierarchical model-level online adaptation for tabular distribution shift
- **作者**: Tianyu Wang、Mian Li、Xi Vincent Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109802
- **发表**: 2026-10-26
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109802
- **PDF**: [NN_2026_HierarchicalOnlineAdaptation.pdf](papers/NN_2026_HierarchicalOnlineAdaptation.pdf)

## 一句话概括
在冻结的表格预测先验上叠加分层集成与双缓冲近邻误差修正，以适应时间分布变化。

## 问题与动机
表格预测在部署后会遇到随时间变化的数据分布，固定模型或昂贵重训难以及时应对。快速追踪近期变化与保留长期稳定性之间也存在取舍。

## 方法
设置冻结先验、固定权重集成和快尺度修正三层，在嵌入空间维护短期与长期误差缓冲，以漂移信号混合近邻残差，辅以稳健裁剪和级联修正。按先预测、再获标签、再更新状态的顺序评价。

## 实验与结果
在8个TabReD基准及额外13个时间/领域偏移数据上测试，报告多项回归RMSE和分类AUC改进，并获得相当覆盖率下更窄的区间。超参数在时间验证流选定；测试标签在预测后才揭示，不用于调参（PDF第11页）。

## 贡献与局限
以模型级记忆修正减少反复重训先验的成本。方法依赖后续真实标签和缓冲维护，不能说无需任何更新或无需标注；标签长期延迟、长期无反馈、存储和近邻检索开销仍限制部署，脑启发类比不等于生物机制验证。

---
DOI: 10.1016/j.neunet.2026.109802 | PDF: [NN_2026_HierarchicalOnlineAdaptation.pdf](papers/NN_2026_HierarchicalOnlineAdaptation.pdf)
