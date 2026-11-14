# Learning to Transfer: Toward Sim-to-Real Spatial Task Assignment via Travel Time Alignment 总结

## 基本信息
- **标题**: Learning to Transfer: Toward Sim-to-Real Spatial Task Assignment via Travel Time Alignment
- **作者**: Qingshun Wu、Yafei Li、Shuo He 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8308-8321
- **发表**: 2026-10-06
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3741084

## 一句话概括
HATrans针对空间众包任务分配的仿真到现实落差，结合拥堵结构搜索、LLM辅助动作迁移和多目标人类偏好对齐。

## 问题与动机
模拟器中的行程时间与现实交通不一致，会使强化学习策略部署后错配任务；仅靠历史数据估计也难覆盖动态路况和个人偏好。

## 方法
MCGS-CI识别影响行程的拥堵子图，以DEGS平衡探索利用、SOMR扩大长期状态覆盖；GAT转换模拟动作，并用多目标偏好反馈校准LLM行程时间估计。

## 实验与结果
在CD与XA两个真实数据集上，HATrans相对较强基线的收入提升约6%–9%，推理延迟增加约2%–3%；扩大工作者规模时收入与完成率仍领先（PDF第10–12页）。

## 贡献与局限
结果显示交通感知搜索与复合偏好对齐有助于迁移任务分配策略；作者仍将大规模实时拥堵子图构造、噪声偏好下的鲁棒性及LLM推理效率列为后续问题（PDF第12–13页）。

---
DOI: 10.1109/tkde.2026.3741084
