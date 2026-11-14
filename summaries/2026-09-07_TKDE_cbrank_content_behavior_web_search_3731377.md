# Multi-Faceted Learning to Rank With Content-Behavior Fusion for Satisfaction-Diverse Web Search 总结

## 基本信息
- **标题**: Multi-Faceted Learning to Rank With Content-Behavior Fusion for Satisfaction-Diverse Web Search
- **作者**: Yuchen Li、Hao Zhang、Yongqi Zhang 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8337-8353
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3731377

## 一句话概括
搜索排序需要兼顾相关性、质量、时效与用户行为，但行为反馈稀疏且与内容信号不成对。CBRank 用预训练语言模型、多个专家头和动态融合共同学习内容及行为信号，面向多维用户满意度排序。

## 问题与动机
在行为反馈稀少且分布不均时，如何把点击、浏览等信号与内容质量共同用于排序？

## 方法
内容侧和行为侧分别通过多专家模块建模，再以动态融合模块组合；作者使用离线满意度标注数据、交错比较、人工评价和线上 A/B 测试验证排序效果。

## 实验与结果
离线指标 NDCG@4、NDCG@10 的 95% 置信区间分别为 [0.6506,0.6540]、[0.7171,0.7241]，高于对比模型区间；线上交错比较较旧系统提升 0.69%，额外特征查询延迟约 0.53 ms（PDF 第 11、14–15 页）。结果来自特定搜索平台，行为反馈和线上流量分布限制外推。

## 贡献与局限
将稀疏行为监督与内容信号分支建模再动态融合，并以线上评估补充离线排序指标。收益及延迟数据依赖该平台的缓存、特征和流量环境，不能直接推断其他搜索场景效果。

---
DOI: 10.1109/tkde.2026.3731377
