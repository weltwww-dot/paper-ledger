# Synergistic optimization of camera-aware disentanglement and consistency learning for unsupervised person re-identification 总结

## 基本信息
- **标题**: Synergistic optimization of camera-aware disentanglement and consistency learning for unsupervised person re-identification
- **作者**: Qing Tian、Long Chen、Binghui Zhang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109448
- **发表**: 2026-08-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109448

## 一句话概括
SCC针对无监督行人重识别的摄像机偏差与伪标签错误循环，联合学习去偏特征和一致性标签，在两基准改善检索，但依赖聚类质量。

## 问题与动机
如何减轻摄像机偏差对伪标签和表征的连锁影响？

## 方法
动量编码器和DBSCAN初始化，CaDRL学习摄像机稳健原型，NCCPO按簇与邻居一致性修正标签。

## 实验与结果
在Market-1501、MSMT17比较mAP、Rank-1和摄像机探测；Base至CaDRL再至SCC的mAP分别增加20.0/0.8及21.9/3.3个百分点（PDF第8–10页）。

## 贡献与局限
联合摄像机去偏与标签修正；真实部署和更广分布未评估。

---
DOI: 10.1016/j.neunet.2026.109448
