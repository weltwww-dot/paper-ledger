# When Optimal Transport Meets Photo-Realistic Image Dehazing With Unpaired Training 总结

## 基本信息

- **标题**: When Optimal Transport Meets Photo-Realistic Image Dehazing With Unpaired Training
- **作者**: Yuanbo Wen, Tao Gao, Shan Liang, Dena Zhang, Ziqi Li, Jing Qin, Ting Chen
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-04-09
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3673760
- **arXiv**: 无
- **PDF**: [NN_2026_WhenOptimalTransportMeets.pdf](papers/NN_2026_WhenOptimalTransportMeets.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出 OBCOT，将无配对图像去雾建模为带结构保持运输代价和频域 Bayesian 正则的 optimal transport，并借助单步 Stable Diffusion 在不需要配对样本的情况下恢复兼顾保真度与自然度的图像。

## 问题与动机

真实场景中的成对雾图和清晰图难以采集，依赖 paired training 的方法在真实雾特征上泛化有限。无配对域转换虽能避免配对数据，却容易出现结构错位、残余雾、颜色失真和高频细节缺失。作者利用 OT 的几何分布对齐能力，同时显式约束空间结构和频谱，避免仅靠空间域对抗学习造成的失真。

## 方法

OBCOT 以 hazy 与 clean 图像分布为 OT 两端，设计由 L1 fidelity 和负 SSIM 组成的 structure-preserving transport cost，以兼顾像素差异与局部结构。恢复网络采用预训练 one-step Stable Diffusion，使用 LoRA 和 zero-convolution 层适配输入图像，并用 hazy image/clean image 等域提示引导生成；双向 identity 约束保留内容。另提出 Bayesian frequency-domain regularization（BFR），用频谱似然吸引输出接近清晰参考频谱，并用 contrastive prior 排斥雾图频谱模式。

## 实验与结果

去雾实验使用 Dense-Haze、NH-Haze、I-HAZE 和 O-HAZY，指标包括 PSNR、SSIM、LPIPS、LIQE、NIMA、MUSIQ 和 ManIQA；相对第二好的无配对方法，四个数据集的 PSNR 分别提高 0.820、2.780、1.948 和 2.226 dB。无配对 deraining/desnowing 在 RealRain1K-H、LHP-Rain、RainD-real 和 WeatherBench-Snow 上相对第二好方法分别提高 0.845、0.575、1.372 和 1.234 dB；BFR 消融带来 1.204 dB PSNR 和 22.15% NIMA 增益。效率上，模型相对 UNSB/DehazeSB 的计算负担降低 33.238%，相对 NSB-CLIP 和 DehazeSB 的推理时间分别降低 55.024% 和 10.384%。

## 贡献与局限

论文把 OT 的结构感知运输、Stable Diffusion 的生成先验和显式频域正则结合起来，在无配对训练下同时提升 fidelity 与 photo-realism，并显示该框架可迁移到无配对去雨和去雪。局限是跨不同天气条件的泛化仍有限，极端大气干扰或复杂光照下可能出现颜色偏移和残余退化；后续需解耦退化与内容，并研究 prompt-invariant 的运输机制。

---
DOI: 10.1109/tnnls.2026.3673760
