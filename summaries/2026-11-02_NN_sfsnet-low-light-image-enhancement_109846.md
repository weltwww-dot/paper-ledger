# SFSNet: A spatial-frequency-semantic tri-domain fusion network for low-light image enhancement 总结

## 基本信息
- **标题**: SFSNet: A spatial-frequency-semantic tri-domain fusion network for low-light image enhancement
- **作者**: Mingtong Chen、Zhida Ren、Xiaowen Shi 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109846
- **发表**: 2026-11-02
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109846

## 一句话概括
SFSNet串联自适应照明估计、空间与频率联合去噪、CLIP语义引导，在低照度图像增强中兼顾亮度、细节和语义。

## 问题与动机
低照度增强常因照明估计不准而出现整体曝光失衡；增强同时放大噪声，单靠像素级恢复又可能损伤物体细节和语义外观。作者提出在空间、频率与语义表征间传递互补信息，缓解亮度、噪声和语义一致性之间的冲突。

## 方法
SFSNet分三阶段处理输入。AIENet以可学习照明参数自适应估计全局曝光；DNRNet在空间域去噪，并用Haar小波分解高频子带、分别处理后融合，以抑制增强放大的噪声并保留细节；SGNet利用预训练CLIP视觉嵌入作为语义查询，与空间特征交叉注意力融合，校正增强结果的语义表达和颜色。

## 实验与结果
在LOLv1、LOLv2-real、LOLv2-synthetic及其他低照度基准上比较。表1中SFSNet在三项数据集的PSNR/SSIM分别为24.97 dB/0.866、23.13 dB/0.875、27.12 dB/0.950，参数量10.559 M。对比CIDNet，LOLv2-real的PSNR仅高0.04 dB；消融和语义编码器替换实验支持三阶段设计及CLIP先验的作用。

## 贡献与局限
方法把照明估计、小波域降噪和预训练视觉语义引导组合为统一增强流程，并在三个LOL测试集取得表内领先指标。语义编码器和三阶段网络增加模型复杂度；像素指标不能完全代表真实场景偏好或下游视觉性能，论文以LOE和定性结果补充评估。跨设备及真实照明分布的泛化仍需检验。

---
DOI: 10.1016/j.neunet.2026.109846
