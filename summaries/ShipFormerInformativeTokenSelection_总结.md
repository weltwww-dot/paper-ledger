# ITS-ShipFormer: An Informative Token Selection Former for SAR Ship Recognition 总结

## 基本信息

- **标题**: ITS-ShipFormer: An Informative Token Selection Former for SAR Ship Recognition
- **作者**: Yuanzhe Shang、Wei Pu、Congwen Wu、Yulin Huang、Yin Zhang、Junjie Wu、Jianyu Yang、Jianqi Wu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3661083
- **arXiv**: 无
- **PDF**: [NN_2026_ShipFormerInformativeTokenSelection.pdf](papers/NN_2026_ShipFormerInformativeTokenSelection.pdf)

## 一句话概括

本文提出 ITS-ShipFormer，通过动态局部卷积、海杂波抑制模块和判别式混合损失筛选有信息量的船舶 token，提升合成孔径雷达船舶识别的准确率与可解释性。

## 问题与动机

SAR 船舶图像中的海杂波会使模型把注意力分配到与目标无关的区域，而船舶类别之间又存在类内差异大、类间相似度高的问题。现有方法通常把整幅图像作为输入，缺少对“哪些 token 真正来自船舶目标”的显式约束。作者希望让 Transformer 主动抑制海杂波、集中计算资源到目标区域，同时增强同类紧凑性和异类可分性。

## 方法

ITS-ShipFormer 在早期阶段使用多头动态局部卷积（MHDLC）增强局部特征提取，在后续 Transformer 阶段加入海杂波抑制模块（SCSM）。SCSM 通过 token 分数和双流 token 更新策略区分有信息的船舶 token 与无用海杂波 token，只保留约 10% 的关键 token 参与后续计算。模型还设计判别式混合损失，同时约束 CLS token 和筛选出的信息 token，以提高类内紧凑性与类间分离度。

## 实验与结果

实验在 OpenSARShip 三类别任务和 FUSAR-Ship 七类别任务上进行，输入统一为 224×224，并与 CNN、ViT 及其他 SAR 船舶识别方法比较。ITS-ShipFormer 在 OpenSARShip 上达到 84.09% 识别准确率，比次优 HDSS-Net 的 83.23% 高 0.86 个百分点；在 FUSAR-Ship 上达到 90.84%，比次优方法高 0.76 个百分点。消融实验显示，MHDLC、SCSM 和判别式混合损失逐步加入后准确率从 78.86%/86.80% 提升到 84.09%/90.84%；模型规模为 9.35M 参数、0.907G FLOPs，兼顾了识别效果和计算效率。

## 贡献与局限

- 将动态卷积、信息 token 选择和判别式损失统一用于 SAR 船舶识别，显式处理海杂波干扰与类间相似问题。
- SCSM 通过双流更新集中计算到目标区域，并提供可视化热图，增强了模型决策的可解释性。
- 在 OpenSARShip 和 FUSAR-Ship 上取得最高识别准确率，同时保持相对可控的参数量和 FLOPs。
- 局限：当前公开实验主要依赖两个数据集，近岸建筑、集装箱和车辆等复杂背景下的检测仍可能不稳定；作者计划使用更多样本和更丰富场景进一步验证，并扩展到船舶检测。

---
DOI: 10.1109/tnnls.2026.3661083
