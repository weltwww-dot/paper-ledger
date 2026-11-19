# RV-mixer: Random Fourier and variance-guided global feature learning for medical image segmentation 总结

## 基本信息
- **标题**: RV-mixer: Random Fourier and variance-guided global feature learning for medical image segmentation
- **作者**: Xiao Feng Dong、Guangju Li、Qinghua Huang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109540
- **发表**: 2026-08-21
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109540

## 一句话概括
RV-Mixer以随机傅里叶特征建模空间全局关系、以方差引导通道重校准，在轻量分割网络中补充全局上下文，提升多种医学图像分割效果。

## 问题与动机
卷积网络擅长局部结构但感受野有限，Transformer可捕获长程关系却计算和参数开销较大，且在标注少、噪声较强的医学影像中未必稳定。论文希望以较低成本引入空间和通道两类全局信息。

## 方法
网络由随机傅里叶特征（RFF）分支和方差引导通道重校准（VGCR）分支组成：RFF将空间位置映射后高效近似全局关系，VGCR根据特征通道统计量强化信息通道、抑制冗余响应。两路全局表征与U-Net式局部特征结合，形成轻量分割架构。

## 实验与结果
在ISIC 2017/2018皮肤病灶、BUSI乳腺超声、Kvasir内镜及前列腺分区等数据集与Transformer、MLP、Mamba及卷积基线比较。ISIC 2017和2018的F1分别为90.90%和90.04%；模型参数量为0.98M，推理时间3.54 ms。作者报告其在多项分割指标上超过更大模型，例如TransUNet参数量62.61M、推理时间99.05 ms。

## 贡献与局限
贡献是用随机特征近似与方差门控组成低成本双路全局模块，并在多类医学图像任务上验证。结果依赖特定数据集、图像尺寸和硬件实现；从所报告实验看，尚不能据此推断在临床流程、跨设备或外部医院数据上具有同等性能。

---
DOI: 10.1016/j.neunet.2026.109540
