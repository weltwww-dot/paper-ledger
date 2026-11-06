# STMH-Xception: Sequential multi-head residual learning for robust underwater acoustic target recognition 总结

## 基本信息
- **标题**: STMH-Xception: Sequential multi-head residual learning for robust underwater acoustic target recognition
- **作者**: Chenhong Yan、Shefeng Yan、Ruobin Gao 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109831
- **发表**: 2026-11-02
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109831
- **PDF**: [NN_2026_STMHXception.pdf](papers/NN_2026_STMHXception.pdf)

## 一句话概括
用逐步冻结和多头监督训练轻量卷积网络，改善被动声呐中的船舶辐射噪声分类。

## 问题与动机
水下声学信号受背景噪声与传播条件影响，区分类似船型需要同时利用不同深度的特征。增加复杂分支又可能抬高计算成本。

## 方法
以深度可分离卷积网络为骨干，逐步冻结已训练阶段，为后续阶段引入残差式多头监督，并累计各头的分类输出。

## 实验与结果
与论文中的骨干基线相比，所报准确率在ShipsEar上从68.72%升到73.10%，在DeepShip上从72.89%升到76.14%。方法增加的参数量有限。

## 贡献与局限
展示了用训练和输出融合改进现有骨干的方法。评估集中在两个公开数据集与指定划分，跨海域、跨设备和背景噪声变化下的收益仍需检验。

---
DOI: 10.1016/j.neunet.2026.109831 | PDF: [NN_2026_STMHXception.pdf](papers/NN_2026_STMHXception.pdf)
