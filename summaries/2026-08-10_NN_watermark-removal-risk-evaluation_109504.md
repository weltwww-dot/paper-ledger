# CRFormer: Multi-scale contrastive regularization transformer for visible watermark removal 总结

## 基本信息
- **标题**: CRFormer: Multi-scale contrastive regularization transformer for visible watermark removal
- **作者**: Yun Hao、Jiaju Wu、Ruizhou Sun 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109504
- **发表**: 2026-08-10
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109504

## 一句话概括
以受控图像复原实验评估可见水印保护的边界，展示版权标识可能因图像处理而失效。

## 问题与动机
水印在颜色、尺度、透明度和位置上差异较大，局部卷积建模及中间特征对比约束可能不足以恢复被遮挡背景；与此同时，去除能力也可能被用于规避内容来源标识。

## 方法
研究以包含不同水印外观的基准评估复原质量，并用对照及消融比较区域定位和背景恢复能力。

## 实验与结果
在 LOGO-H、LOGO-L、LOGO-Gray 和 LOGO-30k 上比较复原质量；LOGO-30k 上报告 PSNR 为 47.72 dB，较此前方法高 5.15 dB。跨数据集评测也显示训练数据变化会影响质量；结果说明水印移除能力较强，同时凸显版权标记可能被削弱的风险（PDF 第 6–8 页）。

## 贡献与局限
论文为评估可见版权标识对图像处理的抵抗力提供了对照。真实传播中的混合退化与不同标识标准仍需单独验证。

---
DOI: 10.1016/j.neunet.2026.109504
