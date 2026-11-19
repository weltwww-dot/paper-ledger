# BH-CDiff: Boundary-aware and heterogeneous feature synergy cold diffusion for medical image segmentation 总结

## 基本信息
- **标题**: BH-CDiff: Boundary-aware and heterogeneous feature synergy cold diffusion for medical image segmentation
- **作者**: Ke Sun、Yu Wang、Wenzheng Ma 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109908
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109908

## 一句话概括
BH-CDiff 将边界先验、空间与频域特征协同及双源条件融合引入冷扩散分割，以改善恢复过程中的边界质量。

## 问题与动机
传统扩散以随机高斯噪声扰动掩膜，增加不确定性；冷扩散改用任务相关扰动，但迭代恢复时仍可能丢失边界，并未充分利用随步骤变化的异质表征。

## 方法
边界感知特征调制（BAFM）用边界先验引导通道与空间注意；多域表征协同（MDRS）联合空间域、频域特征；双源特征融合（DSFF）交互融合分割特征和条件先验，构成冷扩散逐步恢复框架。

## 实验与结果
在三种医学影像分割数据集上与 CNN、Transformer 和扩散方法比较，报告 IoU、DSC、准确率、敏感度及特异度，并开展模块消融和扩散步数敏感性分析。论文报告各模块组合带来协同收益；复杂度还以 256×256 输入比较参数量、FLOPs，速度按 batch=1 测量。

## 贡献与局限
把显式边界建模和空间/频域协同融入确定性冷扩散，实验同时考察精度与推理代价。作者指出迭代恢复仍比常规判别式分割耗时；现有验证集中于二维任务，三维、弱监督及多模态场景仍待验证。

---
DOI: 10.1016/j.neunet.2026.109908
