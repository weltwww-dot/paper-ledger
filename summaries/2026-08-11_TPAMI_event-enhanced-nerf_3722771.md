# E3NeRF: Efficient Event-Enhanced Neural Radiance Fields From Blurry Images 总结

## 基本信息
- **标题**: E3NeRF: Efficient Event-Enhanced Neural Radiance Fields From Blurry Images
- **作者**: Yunshan Qi、Jia Li、Yifan Zhao 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15382-15399
- **发表**: 2026-08-11
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3722771

## 一句话概括
本文提出 E3NeRF，将模糊图像与同步事件流结合来重建清晰的新视角场景，面向高速或低照度下常见的运动模糊。

## 问题与动机
基于普通图像的 NeRF 在输入存在运动模糊时难以恢复清晰几何与纹理；事件流提供高时间分辨率变化信息，但如何将其与图像的模糊形成过程共同用于重建仍是挑战。

## 方法
E3NeRF 分别建立模糊图像渲染损失与事件渲染损失，以约束相机运动造成的曝光积分和事件生成过程。训练时利用事件流中的时空模糊线索，在时间模糊与空间模糊相关部分之间分配计算；作者还构建事件引导的真实场景相机位姿估计流程。

## 实验与结果
作者在合成场景、两组自建真实模糊场景、TUM-VIE 与 Ev-DeblurCDAVIS 上比较 E3NeRF 与图像去模糊、事件式及融合式 NeRF。合成场景的七场景平均定量结果列于正文表 III，真实场景的五场景平均结果列于表 IV；论文报告 E3NeRF 在严重抖动和低照度挑战场景中重建质量更稳定（PDF 第10–12页）。在 Ev-DeblurCDAVIS 的全视图设置下，E3NeRF 优于 Ev-DeblurNeRF（PDF 第13页）；具体数值依数据集和视图设置而异。

## 贡献与局限
方法将图像模糊物理过程与事件生成机制纳入同一 NeRF 优化，并把事件线索用于训练分配和真实相机位姿估计。效果依赖事件传感器与同步数据质量；真实场景范围和跨设备泛化仍需更广泛验证。

---
DOI: 10.1109/tpami.2026.3722771
