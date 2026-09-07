# Backdoor-Based Watermarking in Multi-Client Split Learning 总结

## 基本信息

- **标题**: Backdoor-Based Watermarking in Multi-Client Split Learning
- **作者**: Yao Zhao, Juan Zhao, Zahir Tari, Nasrin Sohrabi, Fu Xiao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3712080
- **arXiv**: 无
- **PDF**: [TDSC_2026_BackdoorWatermarkSplitLearning.pdf](papers/TDSC_2026_BackdoorWatermarkSplitLearning.pdf)

## 一句话概括

本文提出 MarkSplit 与 MarkSplit+，首次为多客户端分割学习中的后门式模型水印提供可行方案，实现约 98% 水印检测率且主任务精度仅下降约 3%。

## 问题与动机

分割学习（Split Learning, SL）将深度神经网络划分为客户端模型与服务器端模型，客户端轮流训练客户端侧部分以降低本地计算开销，其在医疗、车联网边缘智能等场景日益普及，随之而来的是模型知识产权（IP）保护问题。已有模型水印方法主要面向集中式训练或联邦学习，因 SL 的顺序训练特性而无法直接适用；仅有的 SL 水印研究也局限于单客户端。多客户端 SL 中存在三大独特挑战：C1 服务器端训练可能擦除客户端嵌入的水印；C2 共享客户端模型使后序客户端覆盖先前客户端的水印；C3 恶意客户端可通过水印洪泛（watermark flooding）故意抹除他人水印。为在争议中证明多客户端的联合所有权，需要专门面向多客户端 SL 的后门式水印方法。

## 方法

作者提出两种方案：面向良性环境的 MarkSplit 与面向含恶意客户端对抗场景的 MarkSplit+，并设计新型水印样本生成机制 Color-Shape-ID（CSI）。CSI 将每个客户端的水印编码为颜色、形状与客户端 ID 的三元组（c, s, i），经渲染与噪声增强生成水印样本，兼具可识别性、难度、可扩展性、鲁棒性与隐蔽性。MarkSplit 通过 mini-local、local、global 三层训练结构，在主任务与个性化水印样本的联合批次中训练，使模型反复接触所有客户端水印以防被后续训练覆盖；MarkSplit+ 由服务器依据各客户端当前水印检测精度 acci(m) 动态调整下一轮分配的水印样本数 ki(m+1)（实验中阈值 Acc=90%、缩放因子 h=0.2），以应对水印洪泛。两类方法均支持同质与非同质（Dirichlet 非 IID）数据分布，并给出通信复杂度（MarkSplit 为 T×M×n×δ）与收敛性的理论分析（Theorem 1）。

## 实验与结果

实验采用 Ubuntu 22.04 与 2×24GB RTX 4090，覆盖 MNIST、CIFAR10、CIFAR100、FMNIST、GTSRB 五个数据集及 LeNet、AlexNet、ResNet-18、SqueezeNet、VGG13 五种模型，客户端数在 5/10/20/30 间变化，对抗场景默认随机选取 20% 恶意客户端。平均而言两种方法达到约 98% 的水印检测率，主任务精度仅下降约 3%。基线对比中，直接扩展集中式（CenB）、联邦（FLB）及单客户端 SL（SLB）基线到多客户端均失效：CenB 精度低于 23%，FLB 低于 38%，n=20 时 SLB 低于 11.25%，而 MarkSplit 均接近 100%。非同质数据下两者在全部数据集达到 100% 水印检测率；n 增至 20 时精度略有下降（如 MarkSplit+SqueezeNet 最低 86.66%）。保真度方面以 LeNet 为例，MNIST 主任务精度由 98.19% 降至 97.02%（MarkSplit）与 97.12%（MarkSplit+）。抗攻击测试（微调、剪枝、量化、后门、投毒）中 MarkSplit+ 更稳健，如 MNIST 投毒 20000 样本时仍保持 100% 水印检测率，而 MarkSplit 由 100% 降至 97.4%；洁净模型上误报率恒为 0.00%，归因于主任务与水印标签空间的显式分离。

## 贡献与局限

- 首次系统研究多客户端 SL 中的 DNN 水印问题，厘清服务器端训练擦除、客户端相互覆盖与恶意水印洪泛三类挑战。
- 提出后门式中期嵌入方法 MarkSplit（良性场景）与 MarkSplit+（对抗场景，通过动态水印分配增强鲁棒性但资源开销更高），并配套新型水印样本生成机制 CSI。
- 在五数据集、五模型、同质/非同质与多客户端规模下全面验证有效性、保真度与对五类攻击的鲁棒性，并提供通信复杂度与收敛性理论分析。
- 局限：目前仅针对图像 DNN 模型，扩展至文本、音频、视频等模态或更复杂架构仍是开放问题；MarkSplit+ 依赖经验选择的参数（阈值 Acc 与缩放因子 h），未来可结合置信度与梯度统计实现自适应微调，并给出鲁棒性与动态分配对收敛影响的更严格理论分析。

---
DOI: 10.1109/tdsc.2026.3712080
