# A Multimodal Feature Distillation With Mamba-Transformer Network for Brain Tumor Segmentation With Incomplete Modalities 总结

## 基本信息

- **标题**: A Multimodal Feature Distillation With Mamba-Transformer Network for Brain Tumor Segmentation With Incomplete Modalities
- **作者**: Ming Kang, Fung Fung Ting, Shier Nee Saw, Raphaël C.-W. Phan, Zongyuan Ge, Chee-Ming Ting
- **期刊 / 年份**: IEEE Transactions on Artificial Intelligence, 2026
- **研究方向**: 医学图像分割、多模态 MRI、不完整模态学习、Mamba-Transformer
- **DOI**: 10.1109/TAI.2026.3678550
- **PDF**: [TAI_2026_MultimodalFeatureDistillationMamba.pdf](papers/TAI_2026_MultimodalFeatureDistillationMamba.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 MMTSeg，用多模态特征蒸馏、单模态特征增强和跨模态融合，把完整 MRI 的互补知识迁移到各单模态编码器，并用 Mamba-Transformer 建模长程空间关系，从而在脑瘤 MRI 模态缺失时保持分割性能。

## 问题与动机

脑瘤分割通常依赖 FLAIR、T1、T1ce 和 T2 四种 MRI 模态的互补信息，但临床中可能因成像协议、伪影、对比剂过敏、时间或成本限制而缺失部分模态。依赖完整输入的方法在模态缺失时性能显著下降；现有补全、融合或知识蒸馏方法还可能需要为每一种缺失组合训练专门模型，或在只有一两个模态时产生不可靠特征。论文因此关注无需完整模态、能够从可用模态恢复任务相关信息并精确描绘边界的脑瘤分割。

## 方法

MMTSeg 基于 3D U-Net，包含完整多模态教师编码器、四个单模态学生编码器及相应解码器。多模态特征蒸馏（MFD）用完整模态特征指导各单模态特征，采用中间第 3、4、5 层的 L1 特征差异进行蒸馏，以保留低层模态特有的局部信息。单模态特征增强（UFE）在 Transformer 自注意力模块前后结合 Mamba 状态空间模块和 MLP，在每种模态内部同时建模局部空间信息与全局长程依赖。

跨模态融合（CMF）将四个模态的特征乘以二值模态可用性变量，训练时随机丢弃模态以模拟缺失；一条分支用跨模态 Transformer 建立模态间关系，另一条分支用 Mamba 处理拼接特征，再融合为模态鲁棒表示。所有解码器使用广义表面损失（GSL），并对最终解码器采用深度监督，以减小预测边界与真实边界的距离。输入经过 Z-score 归一化、随机裁剪到 128×128×128，并进行旋转、强度偏移和镜像增强；网络训练 1000 个 epoch、batch size 为 1，初始学习率为 1e-4。

## 实验与结果

实验使用 BraTS 2018（285 名患者）和 BraTS 2020（369 名患者），每例含 FLAIR、T1ce、T1、T2，评估增强肿瘤（ET）、肿瘤核心（TC）和全肿瘤（WT），并测试 14 种缺失组合及完整输入。以平均平衡 Hausdorff 距离（bAHD）评价时，BraTS 2018 在“基线改用 GSL”的表 II 中平均 WT/TC/ET 分别为 4.14/6.24/3.75 mm；同一论文表 I 的 MMTSeg 主结果中，WT 为 4.41 mm。BraTS 2020 在表 II 中的平均 WT/TC/ET 分别为 3.65/5.55/3.12 mm；BraTS 2018 的平均 Dice WT/TC/ET 分别为 87.50%/72.58%/64.63%。在参数与计算量比较中，MMTSeg 为 48.24M 参数和 257.41G FLOPs。

消融结果显示，移除 MFD、UFE 或 CMF 后，三类肿瘤区域的平均性能相对下降分别为 23.32%、36.79% 和 43.56%；去除 UFE 或 CMF 中的 Mamba 后，平均性能相对下降分别为 13.53% 和 24.80%。定性分析显示，T1ce 对预测较有帮助，缺失 FLAIR 时瘤周水肿分割下降，缺失 T1ce 时坏死及非增强区域边界更差；仅有一个模态时仍可输出结果，但总体上可用模态越多越接近真实标注。

## 贡献与局限

论文将多模态到单模态的特征级自蒸馏、模态内 UFE 和跨模态 CMF 组合为 MMTSeg，并在不完整 MRI 分割中引入边界感知损失；实验和消融均支持 Mamba-Transformer 混合结构、模态特征蒸馏及跨模态对齐的作用。作者指出，当前方法只在脑瘤 MRI 分割和一种混合架构上验证，Mamba 在视觉任务中的架构选择仍有限，尚未完成跨架构的系统后分析；对肝脏 CT 或 MRI-CT 等其他器官和模态的泛化仍需进一步实验。
