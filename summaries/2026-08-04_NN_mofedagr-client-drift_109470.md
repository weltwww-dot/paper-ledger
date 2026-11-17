# MoFedAGR: Mitigating client drift with adaptive gradient regularization and global momentum in federated learning 总结

## 基本信息
- **标题**: MoFedAGR: Mitigating client drift with adaptive gradient regularization and global momentum in federated learning
- **作者**: Xiang Wang、Lei Tian、Jiahao Gan 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109470
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109470

## 一句话概括
MoFedAGR 以自适应梯度正则和全局动量缓解异质数据下的联邦客户端漂移，在图像基准上更快达到目标精度，但单轮计算成本高于简单聚合方法。

## 问题与动机
如何在客户端数据异质时减小本地更新与全局优化方向的偏差，并改善联邦训练的收敛与泛化？

## 方法
根据本地与全局模型参数差异自适应调整梯度正则强度，并利用全局动量修正方差估计和本地模型更新；论文给出收敛分析。

## 实验与结果
在 CIFAR-10、CIFAR-100 与 TinyImageNet 的不同数据异质划分下，与 FedAvg、FedProx、SCAFFOLD、FedSAM 等比较；CIFAR-10 的 dir-0.1 设定中达到 74% 准确率，MoFedAGR 用 248 轮、总计 7881.44 秒，快于 FedAvg 的 731 轮和 12843.67 秒，但每轮耗时更长（PDF 第5–8页）。

## 贡献与局限
把客户端漂移显式纳入正则与动量校正，并在多个图像分类基准上验证其收敛效率；每轮计算开销以及对具体数据异质模式的依赖仍需考虑。

---
DOI: 10.1016/j.neunet.2026.109470
