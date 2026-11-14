# Digging Into Monocular Texture-Scale Feature Fusion for Optical Flow and Optical Expansion Estimation 总结

## 基本信息
- **标题**: Digging Into Monocular Texture-Scale Feature Fusion for Optical Flow and Optical Expansion Estimation
- **作者**: Changlin Li、Yeqiang Qian、Chunxiang Wang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15427-15439
- **发表**: 2026-08-18
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3725402

## 一句话概括
MonoFusion 将图像纹理与局部尺度变化显式交互，用单目图像联合估计光流、光学扩张及相关运动量。

## 问题与动机
单目光流方法已较成熟，但光学扩张常被当作光流的派生量，缺少针对尺度变化的独立建模；纹理与局部尺度线索若不能互补，也会限制动态场景下的运动估计。本文关注如何让两类线索共同支持像素级运动感知。

## 方法
MonoFusion 分别编码纹理和尺度特征，通过融合模块交互更新光流与光学扩张；MonoFusion-R 在此基础上加入循环迭代融合。预测的光学扩张还用于推导碰撞时间和场景流。

## 实验与结果
作者在 KITTI 上评估光流、光学扩张、碰撞时间和场景流，并在 FlyingThings3D 检验光流泛化。论文报告其在四项 KITTI 单目任务达到或超过当时最佳结果，且在 FlyingThings3D 光流上表现有竞争力；消融显示去掉纹理—尺度融合会降低两项估计精度，循环更新可用较少迭代改善场景流（PDF 第7–11页）。

## 贡献与局限
核心贡献是把光学扩张作为具有独立尺度特征流的稠密预测目标，并设计纹理—尺度交互与循环细化。局部标量尺度不能完整表示旋转、剪切、各向异性形变或遮挡导致的局部映射变化；作者也指出特征融合带来计算负担（PDF 第11页）。

---
DOI: 10.1109/tpami.2026.3725402
