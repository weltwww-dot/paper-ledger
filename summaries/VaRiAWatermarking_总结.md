# VaRiA: Variable-Resolution Image Adaptive Robust Watermarking 总结

## 基本信息

- **标题**: VaRiA: Variable-Resolution Image Adaptive Robust Watermarking
- **作者**: Guanjie Wang, Zehua Ma, Han Fang, Chang Liu, Weiming Zhang, Nenghai Yu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-06-25
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3707132
- **arXiv**: 无
- **PDF**: [TDSC_2026_VaRiAWatermarking.pdf](papers/TDSC_2026_VaRiAWatermarking.pdf)

## 一句话概括

VaRiA 是面向不同分辨率和宽高比图像的 Transformer 鲁棒水印框架，通过 Message Attention Block 与两阶段训练，在保持图像质量的同时提升复杂失真下的水印提取能力。

## 问题与动机

现有深度水印方法通常在固定尺寸、方形图像上训练和测试，面对高分辨率、非等比例图像、裁剪、填充和社交平台处理时，鲁棒性和视觉质量会下降。简单的残差缩放或分块嵌入只能部分适配，还可能带来计算量、几何失配和提取失败。论文希望让同一水印模型覆盖从低分辨率到 8K 的多种输入，并兼顾不可见性与抗扰动能力。

## 方法

VaRiA 使用 Transformer 建模跨图像块的像素关系，并加入 Message Attention Block，使嵌入和提取更关注水印与图像内容的对应关系。训练分为两阶段：第一阶段在固定分辨率下学习基础鲁棒水印能力，第二阶段通过变量分辨率微调，使模型适配不同尺寸、宽高比及常见扰动。训练中还结合对抗和感知约束，并通过不同消息长度、补丁数量及模块移除实验分析设计取舍。

## 实验与结果

实验覆盖 MS COCO、DIV2K 和 Flickr2K 等数据，并比较 TrustMark、VideoSeal 等方法。VaRiA 在多种失真和分辨率下达到接近 100% 的提取准确率，图像质量约为 44 dB PSNR；在壁纸场景中，64 位水印示例的 PSNR 为 44.75/43.79 dB、提取准确率为 98.44%/100%，社交媒体示例的提取准确率为 98.44%。消融结果显示，Message Attention Block 使 PSNR 提升约 1 dB、鲁棒性提升约 6%，代价是约 0.0027 秒的嵌入和提取开销；在简单 VAE 去水印测试中，PSNR 降至 39.81、SSIM 为 0.9762 时，平均提取准确率仍为 96%。

## 贡献与局限

论文针对变量分辨率水印的实际缺口，提出统一的 Transformer 架构、Message Attention Block 和两阶段训练流程，并在真实壁纸和社交媒体情境中验证了可用性。局限在于模型参数量约 3718 万、Transformer 的内存带宽操作带来约 17% 推理时间增加，复杂度和部署成本仍需优化；对更强的水印移除、伪造和对抗攻击的鲁棒性也有待进一步研究。

---
DOI: 10.1109/TDSC.2026.3707132
