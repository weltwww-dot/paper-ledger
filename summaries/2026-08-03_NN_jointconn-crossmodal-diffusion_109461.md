# JointConn-v2: Learning a joint vector field with diffusion transformers for cross-modal connectivity and dual-timestep modeling 总结

## 基本信息
- **标题**: JointConn-v2: Learning a joint vector field with diffusion transformers for cross-modal connectivity and dual-timestep modeling
- **作者**: Honggang Zhao、Yi-Jun Yang、Wei Zeng
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109461
- **发表**: 2026-08-03
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109461

## 一句话概括
JointConn-v2以双向跨模态注意力和双时间步扩散联合建模图像与深度，在所测生成任务中改善图像质量和几何一致性，但高分辨率注意力成本快速增长且冲突条件下空间语义仍易失效。

## 问题与动机
文本到图像扩散与深度条件生成通常分别处理外观和几何，如何联合建模图像—深度关系并协调两种模态的去噪进度？

## 方法
方法在扩散 Transformer 中加入图像与深度之间的双向交换查询交叉注意力，并使用自适应调制及双时间步配对建模联合生成；同时将深度信号作为条件用于图像生成评估。

## 实验与结果
在 512×512 设置下进行联合图像—深度生成和深度条件文本生图，五个随机种子的时间步消融中同步比例 0.50 的联合生成 FID 为 15.90、CLIPScore 为 0.325、RMSE 为 0.148；深度条件下文字与深度左右方向冲突时空间准确率均值降至 0.150，而匹配条件为 0.875，显示语义冲突仍是明显限制（PDF 第 11、14 页）。

## 贡献与局限
提供跨模态连接器和时间步协同的联合扩散设计，并以生成质量、几何指标和冲突压力测试评估效果；交叉注意力随 token 长度二次扩展，文中估计分辨率由 512 提至 1024 时注意力图约增至 16 倍，限制高分辨率应用。

---
DOI: 10.1016/j.neunet.2026.109461
