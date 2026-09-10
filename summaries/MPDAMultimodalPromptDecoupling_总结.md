# MPDA: Multimodal Prompt Decoupling Attack on the Safety Filters in Text-to-Image Models 总结

## 基本信息

- **标题**: MPDA: Multimodal Prompt Decoupling Attack on the Safety Filters in Text-to-Image Models
- **作者**: Xingkai Peng, Jun Jiang, Meng Tong, Shuai Li, Weiming Zhang, Nenghai Yu, Kejiang Chen
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-06-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3696145
- **arXiv**: 无
- **PDF**: [TDSC_2026_MPDAMultimodalPromptDecoupling.pdf](papers/TDSC_2026_MPDAMultimodalPromptDecoupling.pdf)

## 一句话概括

论文提出 MPDA，一种黑盒多模态提示解耦攻击，通过把有害语义拆分到文本与图像两种输入中，研究文本到图像模型安全过滤器在跨模态语义分散下的脆弱性。

## 问题与动机

现有越狱方法多只改写文本，面对更强的语义审核机制时容易被拦截，而且改写后常与原始意图产生语义偏差。已有多模态方法 MMA-Diffusion 还依赖固定提示空间搜索或适合白盒模型的图像扰动，对黑盒商用模型的适用性有限。论文以此评估 T2I 模型同时接收文本和图像时的安全边界，并为防御设计提供攻击面分析。

## 方法

MPDA 先利用大语言模型把不安全提示解耦为看似安全的子提示和保留有害语义的子提示，再将后者改写成自然的对抗提示。该提示与基础图像共同输入 T2I 模型，使有害语义分散到两个模态中；随后视觉语言模型为生成图像生成描述，反馈给语言模型进行迭代改写和细化，以提高图像与原始提示的语义一致性。论文还提出基于重构提示的安全检查（RPSC）分析跨模态信息重新合并后的防御效果。

## 实验与结果

实验覆盖 Stable Diffusion 3.5、CogView、Tongyiwanxiang 和 Midjourney，使用 I2P、JADE-T2I 与 MMA-Dataset，设置暴力和色情两类提示，并与 SneakyPrompt、PGJ、MMA-Diffusion 比较。在 Midjourney 上，MPDA 的暴力内容绕过率达到 92%（对比方法为 47%），色情场景达到 83%，论文摘要报告后者较此前方法高 29%。在显式图像过滤实验中，暴力和色情绕过率分别为 96% 和 91%，比基线高 12%–38%；RPSC 重构后，Midjourney 的两类绕过率分别降至 58% 和 32%，说明跨模态语义重组有助于检测。

## 贡献与局限

论文揭示了文本—图像联合输入中“分散有害语义”这一黑盒攻击面，并用多平台、多场景实验量化了绕过率、危害性和语义一致性的权衡；同时给出 RPSC 这一防御分析方向。局限是需要先生成基础图像，商用平台成本较高，且性能依赖文本与图像权重的精细平衡；作者未公开 REF-I2P 数据集以减少滥用风险。结果应主要用于完善多模态安全审核，而非面向实际滥用。

---
DOI: 10.1109/tdsc.2026.3696145
