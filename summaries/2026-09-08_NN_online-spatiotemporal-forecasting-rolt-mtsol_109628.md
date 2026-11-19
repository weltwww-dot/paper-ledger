# Online spatio-temporal forecasting with retrieval-augmented orthogonal landmark transformer and masked teacher–student learning 总结

## 基本信息
- **标题**: Online spatio-temporal forecasting with retrieval-augmented orthogonal landmark transformer and masked teacher–student learning
- **作者**: Jinhao Ding、Liang Xie
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109628
- **发表**: 2026-09-08
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109628

## 一句话概括
ROLT-MTSOL 将历史检索、正交地标注意力和掩码教师—学生在线学习结合，以有界缓存兼顾时空预测效率、适应与记忆保持。

## 问题与动机
离线训练的时空预测器难以应对持续到来的数据、分布漂移和有限更新预算；一般在线时序方法又未充分建模变量间关系。作者关注如何在流数据上同时利用长历史上下文、降低注意力计算成本，并避免更新新模式时遗忘已学规律。

## 方法
ROLT 将当前窗口切成变量—时间片段作为查询，并从有界 FIFO 回放缓存检索相似的已标注历史片段，只把检索记忆附加到注意力的键和值上下文。LOLA 用共享可学习地标压缩上下文，并通过 Newton–Schulz 正交化稳定地标。MTSOL 联合近期未完全标注窗口的掩码监督、历史样本回放监督和教师蒸馏；教师周期性由学生刷新，在线缓存分为待标签区和已监督回放区。

## 实验与结果
评估覆盖交通、天气、能源、金融、空气质量和风场；交通含 PEMS03/04/07/08，ETT预测步长为96、192、336、720。论文报告交通基准各跨度总体最佳；ETT配对比较多数 p<0.05，少数差距较小者为0.05<p<0.1。

## 贡献与局限
检索旧经验扩展当前上下文，正交地标压缩长序列，三类监督平衡适应和记忆。多领域基准支持其效果；真实部署中的缓存规模、漂移和延迟仍需评估。

---
DOI: 10.1016/j.neunet.2026.109628
