# An efficient algorithm for learning-based visual localization 总结

## 基本信息
- **标题**: An efficient algorithm for learning-based visual localization
- **作者**: Jindi Zhong、Ziyuan Guo、Hongxia Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109456
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109456

## 一句话概括
OCP-LS将曲率预条件纳入学习式视觉定位优化，在 Cambridge Landmarks 上改善多项位姿误差并在图像分类中显示收敛与泛化优势，但理论保证依赖光滑性等条件且计算和显存开销较高。

## 问题与动机
一阶优化在位置与方向等不同尺度参数上可能收敛缓慢，二阶方法则常因 Hessian 计算成本过高而难用于学习式视觉定位，能否兼顾曲率校正与可计算性？

## 方法
作者基于 OCP 构造二阶优化器，以 Hutchinson 方法近似对角 Hessian 信息，并使用预条件梯度更新；算法收敛率在给定假设下分析，再通过定位和分类任务检验实际表现。

## 实验与结果
在 Cambridge Landmarks 与 CIFAR 图像分类任务上对比 Adam、AdamW、AdaHessian 等方法；定位表中 OCP-LS 在 King’s College 的 ATE RMSE 为 1.43 m、Adam 为 1.57 m，在 Old Hospital 分别为 3.75 m 与 3.79 m，同时单轮时间约 0.05–0.06 秒、显存约 2 GB，高于 Adam 类基线（PDF 第 8、12 页）。

## 贡献与局限
将可估计的对角曲率信息用于 OCP 式学习优化，并提供收敛分析及跨任务实证；优势幅度随场景变化，理论保证仅在所列假设成立时适用，且资源成本限制其效益判断。

---
DOI: 10.1016/j.neunet.2026.109456
