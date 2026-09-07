# Dataset Distillation via a Noise-Unconstrained Generative Model 总结

## 基本信息

- **标题**: Dataset Distillation via a Noise-Unconstrained Generative Model
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3690778
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

Dataset distillation (DD) aims to synthesize a more compact dataset than the original one and models trained on it are expected to have the same generalization capabilities as on the original dataset. Previous work via a generative model (GM) faces several limitations. First, GM struggles to generate representative samples due to a lack of constraints. Second, it overlooks the relationships between generated samples, limiting its effectiveness. In this paper, a new noise-unconstrained GM-based DD framework is proposed. In the distillation stage, an adaptive matching coefficient is introduced to align generated images with representative class elements and the MiniMax loss function is extended to reduce the optimization difficulty. In the deployment stage, features among each generative image are ensembled by gradient-matching based DD. Theoretical analysis based on McDiarmid's inequality demonstrates that the proposed components can reduce the generalization error of the original baseline method. We also provide insights into the potential of generated images as an effective proxy dataset for DD. For example, on the ImageWoof dataset with 50 distilled images per class using a 6-layer ConvNet for evaluation, generated images outperform 25%, 50%, and 75% original images by 8.4%, 6.3%, and 8.3% in distillation performance. Our method effectively handles both low- and high-resolution datasets, with experiments on 11 benchmarks demonstrating its efficacy.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tpami.2026.3690778
