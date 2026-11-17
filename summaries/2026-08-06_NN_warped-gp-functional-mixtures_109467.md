# Mixture of warped Gaussian process functional regressions and its classification EM algorithm 总结

## 基本信息
- **标题**: Mixture of warped Gaussian process functional regressions and its classification EM algorithm
- **作者**: Yurong Xie、Di Wu、Zhe Qiang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109467
- **发表**: 2026-08-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109467

## 一句话概括
MWGPFR 将变换高斯过程功能回归组合为混合专家并以分类 EM 学习，在多模态模拟与实测数据上改善预测，但更复杂的模型计算代价更高。

## 问题与动机
如何在含函数型协变量的多模态数据中同时刻画非平稳变化、非线性输出变换和共享函数趋势？

## 方法
每个混合成分采用带函数型均值结构的变换高斯过程回归，并通过分类期望最大化估计参数；为减轻初始化敏感和局部最优，进一步提出分裂合并 CEM。

## 实验与结果
在 16 组模拟数据及电力等真实数据上与高斯过程回归、变换 GP 和混合回归等比较；合成实验中 MWGPFR II 在多成分场景取得较低预测误差，电力数据五折评估的平均 RMSE 为 0.3035 kW，作者同时指出该模型计算较昂贵（PDF 第7–13页）。

## 贡献与局限
统一处理多模态结构、非线性输出与函数型协变量，并提供改进初始化收敛的 SMCEM；高复杂度模型的运行成本较高，且结论主要建立在文中所测数据上。

---
DOI: 10.1016/j.neunet.2026.109467
