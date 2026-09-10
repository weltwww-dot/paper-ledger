# SRFormerV2: Taking a Closer Look at Permuted Self-Attention for Image Super-Resolution

## 基本信息

- **标题**: SRFormerV2: Taking a Closer Look at Permuted Self-Attention for Image Super-Resolution
- **作者**：Yupeng Zhou、Zhen Li、Chun-Le Guo、Li Liu、Ming-Ming Cheng、Qibin Hou
- **期刊 / 会议**：IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tpami.2026.3685679
- **arXiv**：无
- **PDF**：[TPAMI_2026_SRFormerV2TakingCloserLook.pdf](papers/TPAMI_2026_SRFormerV2TakingCloserLook.pdf)

## 一句话概括

本文提出置换自注意力 PSA，使图像超分辨率 Transformer 能在较大窗口中建模更广泛的像素关系，并通过扩大窗口、增加通道和融合局部块构造性能更强的 SRFormerV2。

## 问题与动机

扩大窗口通常能提升 Transformer 超分辨率模型的重建质量，但标准窗口自注意力的计算开销会快速增加；简单下采样或随机采样键和值又可能损失空间结构。论文希望在让更多像素参与注意力的同时控制参数量和乘加量，并进一步研究大窗口、通道信息和局部细节之间的平衡。

## 方法

SRFormer 由像素嵌入、分层特征编码器和高分辨率重建头组成。核心 PSA 先在非重叠窗口中生成 Q、K、V，再压缩 K/V 的通道维并把空间 token 置换到通道维，从而减少注意力矩阵中的 token 数，却不直接平均或丢弃像素；配合相对位置编码完成大窗口注意力。PAB 还加入深度卷积 ConvFFN，补偿自注意力偏向低频而损失局部高频细节的问题。SRFormerV2 进一步采用 36×36 大窗口、更多通道，并在每两个 PSA 组前插入小窗口局部块，以同时聚合全局和局部信息；另提供资源更低的 SRFormerV2-S。

## 实验与结果

实验在 DIV2K、DF2K 和 OST 上训练，在 Set5、Set14、BSD100、Urban100、Manga109 以及生物医学和天文图像上测试，使用 Y 通道 PSNR 和 SSIM 评价。基础 SRFormer 在 Urban100 上达到 33.86 dB，比 SwinIR 高 0.46 dB，同时参数和计算量更少；消融表明增大窗口持续改善性能，5×5 深度卷积的 ConvFFN 比 3×3 更有效。SRFormerV2 在 Urban100、Manga109 等高分辨率数据上继续提升，并在生物医学图像上达到 45.09 dB/0.9812 SSIM，在天文图像上达到 40.53 dB/0.9664 SSIM，均优于 SwinIR 和 HAT。模型规模实验还显示，SRFormerV2-S 以更低资源取得了与 HAT 有竞争力的结果。

## 贡献与局限

论文展示了通过空间—通道置换实现高效大窗口注意力的设计路径，并从窗口、通道、高频局部信息和模型规模四个方面系统扩展 SRFormer，在经典、轻量、真实场景和分布外图像超分辨率上获得稳定收益。局限在于更大窗口和更宽通道仍会增加训练显存与推理成本，模型主要针对单图像超分辨率和特定退化设置，真实复杂退化、视频时序一致性及极端资源设备上的表现仍需验证。后续可研究自适应窗口、面向真实退化的训练和视频/多模态恢复任务。

---
DOI: 10.1109/tpami.2026.3685679
