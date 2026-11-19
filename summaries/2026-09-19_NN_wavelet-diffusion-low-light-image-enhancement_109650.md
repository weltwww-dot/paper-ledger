# Bidirectional cross-frequency guided wavelet diffusion for detail-preserving low-light image enhancement 总结

## 基本信息
- **标题**: Bidirectional cross-frequency guided wavelet diffusion for detail-preserving low-light image enhancement
- **作者**: Pingping Liu、Jiahao Liu、Shihui Pei 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109650
- **发表**: 2026-09-19
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109650

## 一句话概括
BCF-Diff 在小波频域分离结构与细节，只对低频结构执行扩散恢复，再以恢复结构引导高频细节增强和去噪，改善低照图像的亮度与纹理保真。

## 问题与动机
直接在像素域使用扩散模型时，全局照明校正与局部细节保留难以兼顾，噪声还可能被放大或生成不自然纹理。作者探索能否利用图像频率分解，让扩散负责紧凑的结构成分，再以跨频引导恢复边缘和纹理。

## 方法
BCF-Diff 先用 K 级离散小波变换分解低、高频分量。扩散网络仅恢复低频近似分量，训练损失按高频细节能量加权，使结构学习关注细节丰富区域；随后跨频门控细化模块 CFGR 用恢复后的低频引导高频子带增强，空间门控模块再抑制噪声、锐化纹理，并经逆小波变换重建图像。高频真值仅用于训练损失加权，推理只需低照输入。

## 实验与结果
在 LOL-v1、LOL-v2-Real 和 LOL-v2-Synthetic 配对数据上与多种增强及扩散方法比较，作者报告 BCF-Diff 在三个数据集的 SSIM 均为最高。非配对 Dark Face 测试中，NIQE 与 BRISQUE 均优于对照；下游行人检测也优于未增强输入。消融显示 K=2 是细节与结构平衡较好的小波分解层数。

## 贡献与局限
方法的关键是双向频率协作：高频能量训练时反向指导低频结构恢复，恢复出的低频又在推理时正向引导高频细节生成。多组图像质量、视觉比较和检测评估支持其有效性；作者仍指出对不同区域照明变化的处理有待改进，且主观纹理质量与下游任务表现不能替代更广泛真实场景验证。

---
DOI: 10.1016/j.neunet.2026.109650
