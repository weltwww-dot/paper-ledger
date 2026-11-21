# AdaFGNN: An adaptive filtering graph neural network for protein–protein interaction site prediction 总结

## 基本信息
- **标题**: AdaFGNN: An adaptive filtering graph neural network for protein–protein interaction site prediction
- **作者**: Qi Zhang、Mengmeng Si、Xinming Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109941
- **发表**: 2026-11-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109941

## 一句话概括
AdaFGNN通过多频段图滤波和残基自适应融合，提升蛋白质相互作用位点的机器学习预测与独立基准表现。

## 问题与动机
常规图神经网络的邻域聚合偏向低通平滑，容易削弱局部差异。对于类别高度不平衡的残基二分类，研究关注能否保留中高频特征，并在独立数据集上改善预测，而非仅提高总体准确率。

## 方法
模型在残基图上以固定、无可学习参数的低、中、高通多阶滤波提取表示，再将原始和滤波特征编码为谱token。Transformer学习跨频段和阶数的关系，门控注意力为每个残基融合信息；训练使用类别加权二分类与边界感知辅助监督，推理仅用二分类头。

## 实验与结果
实际训练集为Train_334，评测包含Test_60及另外三个整理后的测试集。Test_60上MCC为0.526、AUPRC为0.635，高于GTE-PPIS的0.500与0.611；UBtest_25上分别为0.342与0.371。移除高通分支后，Test_60的MCC、AUPRC绝对下降0.036、0.042，支持多频段互补。

## 贡献与局限
贡献在于显式保留多频段信号并按残基学习融合权重，以不平衡指标检验效果。局限是结果依赖结构图和有限基准；未结合状态的预测仍明显较弱。正文虽称十次重复并报告标准差，主比较表却未列方差，不能据此认定差异已获显著性验证。

---
DOI: 10.1016/j.neunet.2026.109941
