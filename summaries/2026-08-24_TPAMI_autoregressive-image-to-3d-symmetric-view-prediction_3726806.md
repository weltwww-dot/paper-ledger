# Autoregressive Image to 3D Generation via Next Symmetric View Prediction 总结

## 基本信息
- **标题**: Autoregressive Image to 3D Generation via Next Symmetric View Prediction
- **作者**: Haibo Yang、Yang Chen、Yingwei Pan 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15703-15715
- **发表**: 2026-08-24
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3726806

## 一句话概括
AR3D 以近到远的对称视角自回归生成多视图，再从单张图像重建具有一致外观和几何结构的三维物体。

## 问题与动机
单张图像无法直接呈现物体背面，独立生成各视角容易产生几何和外观不一致；普通循环视角顺序还会把最困难的背面放在生成链中段，使后续误差累积。本文研究如何利用视角序列的对称关系稳定图像到三维生成。

## 方法
AR3D 将预训练视频扩散模型改造成因果式自回归生成器，并在每一步同时预测相对于输入视角对称的两幅视图，按近到远顺序推进；随后使用基于 instant-NGP 的 SDF 重建器从合成视图恢复三维形状。训练噪声策略也按自回归推理时的上下文设计。

## 实验与结果
模型在约 30 万组 Objaverse 多视图图像上训练，并在 GSO、OmniObject3D 测试。AR3D 在 GSO 与 OmniObject3D 新视图合成中取得最低 Ewarp，在 GSO 单视图重建的两项指标上超过对比方法；消融显示对称近远顺序优于普通循环及仅缩短递归链的方案（PDF 第6–9页）。

## 贡献与局限
方法把视角顺序对称性转化为成对预测机制，降低递归深度并改善背面视图一致性。单图输入仍无法恢复被遮挡且缺乏语义/几何线索的细节，背面输入时性能会明显下降；自回归生成也比并行视图生成更慢，文中运行时间比较并非严格同硬件对照（PDF 第10–11页）。

---
DOI: 10.1109/tpami.2026.3726806
