# Learned nonlocal feature matching and filtering for RAW image denoising 总结

## 基本信息
- **标题**: Learned nonlocal feature matching and filtering for RAW image denoising
- **作者**: Marco Sánchez-Beeckman、Antoni Buades
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109833
- **发表**: 2026-11-04
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109833
- **PDF**: [NN_2026_NonlocalRAWDenoise.pdf](papers/NN_2026_NonlocalRAWDenoise.pdf)

## 一句话概括
把经典非局部去噪中的匹配、协同滤波和聚合移入可学习的多尺度特征空间，以较轻的模型处理RAW图像。

## 问题与动机
深层去噪网络虽能恢复细节，参数和计算成本可能限制终端部署。跨传感器的噪声分布也有差异，仅在训练设备上表现好不足以支持泛化。

## 方法
在U形骨干各尺度用非局部模块搜索特征近邻，对近邻特征组做可学习的协同滤波与聚合。以真实干净RAW配合多传感器噪声模型训练，并用噪声水平图调节滤波强度。

## 实验与结果
论文在DND、SIDD及实拍RAW图像上比较效果，并用未见传感器和扰动后的噪声水平图检查泛化。部分条件下，较小的模型即可接近较重的卷积和Transformer对照（PDF第10–14页）。

## 贡献与局限
将具有可解释结构的非局部滤波与端到端学习结合。效果仍取决于训练噪声模型及输入噪声图的质量，测得的速度受硬件和分辨率影响。

---
DOI: 10.1016/j.neunet.2026.109833 | PDF: [NN_2026_NonlocalRAWDenoise.pdf](papers/NN_2026_NonlocalRAWDenoise.pdf)
