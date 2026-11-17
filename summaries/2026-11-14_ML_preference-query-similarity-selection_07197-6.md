# Query Selection with Proper Latent-Representation Similarity in Preference-Based Reinforcement Learning 总结

## 基本信息
- **标题**: Query Selection with Proper Latent-Representation Similarity in Preference-Based Reinforcement Learning
- **作者**: Chunru Dong、Aoxiang Wang、Yang Wang 等
- **期刊 / 会议**: Machine Learning 2026
- **卷期 / 文章号**: 115，文章号256
- **发表**: 2026-11-14
- **日期来源**: Springer 官网 citation_online_date
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07197-6

## 一句话概括
QSPLS 先按奖励引导的相邻聚类选取候选轨迹对，再以熵和潜在相似度过滤冗余查询，在 DMControl 与 MetaWorld 任务中通常提高偏好强化学习表现，但收益伴随额外训练时间且部分比较不显著。

## 问题与动机
偏好强化学习中，如何选择既有信息量又不过度相似的轨迹对，以减少人工偏好标注需求？

## 方法
QSPLS 分两阶段选查询：奖励引导的相邻聚类提供具有结构差异与较高不确定性的候选对，随后依据熵和潜在表示相似度剔除过度相似样本；最终将偏好用于奖励模型学习并接入现有强化学习算法。

## 实验与结果
作者在 DMControl 连续控制和 MetaWorld 操作任务中以 QPA 为基础，与随机、分歧及熵采样方案比较；五个运动任务中 QSPLS 相比 QPA 的最终表现均提高，Walker_walk 增益为 6.3%，Cheetah_run 与 Quadruped_run 分别为 13.8% 与 22.1%；训练耗时高于 QPA（PDF 第 11–21 页）。部分预算下显著性检验未显示明确差异，效果依任务和查询量变化。

## 贡献与局限
研究明确讨论轨迹对潜在相似度对偏好反馈效率的影响，并提出兼顾不确定性与冗余的采样策略；额外筛选和训练开销、任务迁移能力及偏好噪声仍需考虑。

---
DOI: 10.1007/s10994-026-07197-6
