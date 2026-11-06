# Flash SewerNet: A lightweight expert network with Gaussian-multimodal fusion for sewer defect recognition 总结

## 基本信息
- **标题**: Flash SewerNet: A lightweight expert network with Gaussian-multimodal fusion for sewer defect recognition
- **作者**: Songyi Dian、Xuke Zhong、Yuzhong Zhong 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109828
- **发表**: 2026-11-02
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109828
- **PDF**: [NN_2026_FlashSewerNet.pdf](papers/NN_2026_FlashSewerNet.pdf)

## 一句话概括
结合缺陷边缘、管材信息和专家分工，以较低开销识别下水管检测画面中的多种缺陷。

## 问题与动机
同一管道画面可同时出现多个缺陷，稀有标签又很少见。传感噪声、管材差异和现场算力进一步限制可用模型。

## 方法
以边缘感知模块保留细小缺陷轮廓，利用高斯多模态特征模块融合图像与管材文本，并用混合专家处理标签分布差异。

## 实验与结果
轻量版在Sewer-ML上以1211万参数达到64.65%的F2CIW。论文在QV-Pipe视频基准报告mAP 63.36和宏平均F1 65.87，并在Jetson Orin NX上测得28.2帧/秒（PDF第16页）。

## 贡献与局限
兼顾多标签效果和边缘设备效率。模型按帧处理，需要相应的管材信息；不同传感器、现场条件和帧间连续性上的效果仍需验证。

---
DOI: 10.1016/j.neunet.2026.109828 | PDF: [NN_2026_FlashSewerNet.pdf](papers/NN_2026_FlashSewerNet.pdf)
