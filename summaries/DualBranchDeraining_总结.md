# High-resolution image deraining via dual-branch features interaction and fusion 总结

## 基本信息

- **标题**: High-resolution image deraining via dual-branch features interaction and fusion
- **作者**: Weilong Huang, Jiaxue Mei, Tao Yan, Yinghui Wang, Xiaojun Chang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108936
- **arXiv**: 无
- **PDF**: [NN_2026_DualBranchDeraining.pdf](papers/NN_2026_DualBranchDeraining.pdf)

## 一句话概括

针对高分辨率图像去雨中计算开销大、高频细节易被过度平滑丢失的问题，本文提出双分支去雨网络 DDNet，通过频域特征交互与动态融合同时保留局部高频细节与全局上下文信息。

## 问题与动机

现有图像去雨方法主要面向低分辨率图像，直接迁移到高分辨率（如 4K）图像时存在固有局限：一方面，直接在原分辨率上做特征提取会使特征图尺寸二次增长，带来巨大的计算与显存开销；另一方面，高分辨率雨图中雨痕常与背景交织甚至严重遮挡，要求模型同时具备局部细节刻画与全局上下文建模能力，而多数现有模型主要提取空间域特征、忽略频域信息，导致去除雨痕时过度平滑高频细节，产生模糊与结构信息丢失。此外，训练与测试分辨率不一致还会降低模型的泛化能力。

## 方法

作者提出高效的双分支去雨网络 DDNet，采用非对称双编码器–解码器结构：高分辨率分支由多尺度 CNN（NAF Block）组成，处理原始高分辨率输入以提取局部与高频特征；低分辨率分支以 4 倍下采样图像为输入，由带转置注意力的多尺度 Transformer 层构成，借助 Transformer 固有的低通滤波特性提取全局上下文与低频信息。文中还提出三个关键模块：自适应频率互惠模块（AFRM）通过低/高通滤波器生成器自适应生成频谱滤波器，实现两支路间高频与低频信息的互惠增强；基于 DCT 的多光谱融合模块（MSFM）借鉴 JPEG 的 ZIGZAG 扫描选取预定的 DCT 频谱分量，动态融合两支路解码特征（n=16）；双差分交叉注意力模块（DDCAM）利用差分注意力策略缓解 CNN 与 Transformer 特征分布差异带来的噪声与失衡。损失为两支路 L1 损失与高分辨率输出 SSIM 损失的加权和（α=1、β=0.5、γ=0.2）。

## 实验与结果

实验在真实高分辨率数据集 LHP-Rain、RealRain-1K（含 H/L 两个子集）与合成数据集 RainDirection 上进行，与 PReNet、MPRNet、Restormer、DRSformer、HCT-FFN、GLGFN、UDRMixer、UHD-Processor、ERR 等主流方法比较。DDNet 在全部数据集上取得最佳指标：RealRain-1k-H 上 PSNR/SSIM 为 40.64/0.9848（比次优 GLGFN 高 0.56 dB），RealRain-1k-L 上为 41.87/0.9875（高 0.83 dB），LHP-Rain 上为 34.13/0.9450，RainDirection 上为 30.79/0.9128；在 256×256 输入下仅 12.5M 参数、18.55G FLOPs，推理约 174.77 ms。消融实验表明：去掉低分辨率分支解码器（hybrid 结构）PSNR 下降 0.7 dB；去除 AFRM 性能下降 0.46 dB；用求和/拼接替换 MSFM 下降 0.22 dB；将 DDCAM 换为标准交叉注意力下降 0.45 dB；MSFM 中 n=1 时退化为全局平均池化（GAP）性能最差，n=16 最优、n=32 略降。模型基于 PyTorch 在单张 RTX3090 上训练，采用 AdamW、余弦退火与渐进式分辨率训练策略，共 1000 个 epoch。

## 贡献与局限

贡献包括：提出面向高分辨率图像去雨的高效双分支网络 DDNet，整合频域特征交互与动态特征融合以增强 CNN 与 Transformer 两支路的表征能力；设计自适应频率互惠模块 AFRM，自适应生成频谱滤波器实现跨支路频率互补；提出 DCT 多光谱融合模块 MSFM 与双差分交叉注意力模块 DDCAM，分别实现多光谱信息聚合与跨分支特征差异消解；实验证明其在真实与合成高分辨率雨图上以低参数量、低计算量达到 SOTA 性能，代码与模型已开源（https://github.com/YT3DVision/HRDerain）。局限方面：当雨痕呈现大范围聚集、块状等极端形态时（如图 10 所示失败案例），模型仍无法完全去除所有雨痕，部分背景结构会出现模糊或畸变；作者未来计划进一步研究空间域与频域特征的提取与融合，构建更强且更轻量的高分辨率图像复原架构。

---
DOI: 10.1016/j.neunet.2026.108936
