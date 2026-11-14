# Friedkin–Johnsen Opinion Dynamics on Hypergraphs 总结

## 基本信息
- **标题**: Friedkin–Johnsen Opinion Dynamics on Hypergraphs
- **作者**: Runze Zhang、Gengyu Wang、Ahad N. Zehmakan 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8224-8236
- **发表**: 2026-10-02
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3740172

## 一句话概括
论文将Friedkin–Johnsen观点动力学扩展至超图，在显式保留群组高阶交互的同时，设计算法近似计算个体观点的平衡状态。

## 问题与动机
简单图只表达两两关系；将超图直接投影为稠密矩阵会增加计算和存储负担，也可能扭曲高阶群组影响。

## 方法
作者提出同步、异步、Chebyshev加速和共轭梯度四种迭代算法，并给出收敛及误差保证，避免显式构造高阶转移矩阵。

## 实验与结果
在10个真实超图上评估，四种算法均达到无穷范数误差低于10⁻⁸；共轭梯度在大规模实例上兼顾运行时间与误差，且与团投影模型给出不同的意见分歧指标（PDF第10–12页）。

## 贡献与局限
研究提供超图FJ平衡意见的可计算方案；模型假定超边内所有节点影响同质，作者指出现实群组中角色影响异质，尚未纳入建模（PDF第12页）。

---
DOI: 10.1109/tkde.2026.3740172
