# Joint optimization transposed projection envelope linear discriminant analysis mode 总结

## 基本信息
- **标题**: Joint optimization transposed projection envelope linear discriminant analysis mode
- **作者**: Yongming Li、Wenqiang Zhao、Fan Li 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109475
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109475

## 一句话概括
TPELDA 以同类近邻构成样本包络并联合优化判别投影与分布差异，在多类结构化及图像数据上改善分类表现，但收益会随数据集和训练样本量变化。

## 问题与动机
如何让线性判别分析利用同类相似样本间的相关信息，同时避免投影后包络样本偏离原始样本分布？

## 方法
将样本与其同类近邻加权融合为包络样本，在包络空间最大化 Fisher 类间与类内判别性，并加入包络和原样本投影分布差异项；通过迭代算法联合求解投影和融合权重。

## 实验与结果
在结构化数据集及 Jaffe、Coil20、UMIST 等图像数据上与多种 LDA 变体和学习方法比较；TPELDA 在 11 个数据集中的 7 个取得最佳、2 个取得次佳表现，Jaffe 的优势随每类训练样本数改变，论文另报告噪声鲁棒性与迭代收敛分析（PDF 第11–17页）。

## 贡献与局限
把同类局部相关信息、判别投影和分布保持纳入统一 LDA 优化，并分析各损失项的贡献；近邻构造依赖标签与参数选择，性能优势并非对所有数据集一致。

---
DOI: 10.1016/j.neunet.2026.109475
