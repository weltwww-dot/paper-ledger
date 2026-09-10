# Anti-Inpainting: A Proactive Defense Approach Against Malicious Diffusion-Based Inpainters Under Unknown Conditions 总结

## 基本信息

- **标题**: Anti-Inpainting: A Proactive Defense Approach Against Malicious Diffusion-Based Inpainters Under Unknown Conditions
- **作者**: Yimao Guo, Zuomin Qu, Wei Lu, Xiangyang Luo
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3708852
- **arXiv**: 无
- **PDF**: [TDSC_2026_AntiInpaintingProactiveDefense.pdf](papers/TDSC_2026_AntiInpaintingProactiveDefense.pdf)

## 一句话概括

本文提出 Anti-Inpainting，通过多层扩散特征、保持语义的数据增强和基于分布偏差的选择性优化，生成能跨未知掩码、随机种子和扩散模型版本发挥作用的主动防护图像。

## 问题与动机

扩散模型可以根据用户指定的掩码和文字提示自然地擦除或替换图像内容，恶意图像修复会带来肖像、版权和内容完整性风险。现有主动防御方法通常在已知模型、已知掩码或单一随机种子上优化，对未知掩码的迁移性不足；攻击者还可以反复更换初始 latent 随机状态，筛选出能够绕过防护的结果。作者关注的核心问题是，如何让防护扰动不依赖攻击者将使用的具体掩码和随机种子，同时尽量保留原图的语义质量。

## 方法

Anti-Inpainting 包含三个相互配合的模块。多层深度特征提取器从扩散 U-Net 的下采样、中间和上采样阶段提取特征，避免只攻击末端噪声预测；多尺度语义保持数据增强在优化中随机改变掩码尺度和强度，使扰动覆盖未知掩码条件；选择性分布偏差优化先估计原始图像的特征分布，再筛选满足阈值的 latent 状态，并最大化保护图像与原始分布之间的特征偏差，从而抑制容易导致防护失效的随机种子。扰动受 `L∞=16/255` 约束，使用 800 次迭代生成保护图像。

## 实验与结果

实验在 InpaintGuardBench 和 CelebA-HQ 上进行，主攻击模型为 Runway v1.5，并用 Stability AI v2.0 检验跨模型迁移；评价指标包括 PSNR、SSIM、LPIPS、ImageReward 和 ArcFace 相似度。在 CelebA-HQ 未知掩码设置下，Anti-Inpainting 的 PSNR/SSIM 为 `14.704/0.468`，优于 PhotoGuard 的 `17.874/0.640`，ArcFace 相似度降至 `0.744`，而 PhotoGuard 为 `0.861`，说明未经授权的修复结果更难保持原始身份和视觉质量。面对多随机种子筛选，Anti-Inpainting 在 InpaintGuardBench 上保持最低 PSNR `17.665`、SSIM `0.618` 和 ImageReward `-1.012`。在 JPEG 压缩、位深压缩和缩放插值后仍保持较强防护，并能迁移到不同扩散模型版本；但 DiffPure、GridPure 等扩散式净化会显著洗掉包括本文方法在内的多种扰动。

## 贡献与局限

贡献在于把未知掩码迁移、随机 latent 规避和跨模型迁移纳入统一的主动防御流程，并通过扩散网络多层特征提高扰动的语义层鲁棒性。局限是防护仍需要为每张图像进行迭代优化，且对扩散式重建/净化尤其脆弱；实验主要针对两个数据集、特定扩散修复模型和有限扰动预算，跨领域图像、更新后的模型架构及更强净化器仍可能降低效果。防护扰动还需要在抗修复能力与原图可用性之间取得平衡。

---
DOI: 10.1109/tdsc.2026.3708852
