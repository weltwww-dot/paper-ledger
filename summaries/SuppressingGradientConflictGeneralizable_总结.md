# Suppressing Gradient Conflict for Generalizable Deepfake Detection 总结

## 基本信息

- **标题**: Suppressing Gradient Conflict for Generalizable Deepfake Detection
- **作者**: Ming-Hui Liu、Harry Cheng、Xin Luo、Xin-Shun Xu
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3687009
- **arXiv**: 无
- **PDF**: [TPAMI_2026_SuppressingGradientConflictGeneralizable.pdf](papers/TPAMI_2026_SuppressingGradientConflictGeneralizable.pdf)

## 一句话概括

本文提出 CS-DFD 深度伪造检测框架，通过搜索兼顾两类伪造数据的更新向量并约束特征层梯度冲突，改善检测器在源域和未知目标域之间的性能折中。

## 问题与动机

将原始伪造视频与在线合成伪造视频同时用于训练，理论上可以增加数据多样性，但实验中却经常出现“1+1<2”：源域精度和跨域泛化能力同时下降。作者分析认为，原始伪造数据包含特定生成方法的低层痕迹，而在线合成数据更强调可迁移的高层伪造线索，两者在反向传播时产生相互冲突的梯度，导致优化过程振荡，检测器难以学习兼顾两类数据的表示。

## 方法

CS-DFD 包含更新向量搜索（UVS）和冲突梯度约简（CGR）两个协同模块。UVS 分别计算原始伪造与在线合成伪造的梯度，在靠近初始梯度的范围内搜索一个能同时降低两类损失的更新向量，以避免某一数据源的优化破坏另一数据源。CGR 在特征空间加入冲突下降损失，利用投影层和 Hessian 对角近似惩罚不一致的梯度方向，使不同伪造来源形成低冲突表示。两个模块共同作用于参数更新和表示学习。

## 实验与结果

模型在 FaceForensics++（FF++）上训练，并在 FF++、Celeb-DF、DFDC、DFDCp 和 UADFV 上进行源域与跨域测试，同时使用 DiFF 评估对扩散模型伪造的泛化能力。CS-DFD 在 FF++ 上取得约 99% AUC，在四个目标域上的平均 AUC 达约 88%，优于仅使用原始伪造、仅使用在线合成伪造以及通用梯度手术方法的基线；在 DiFF 上取得 89.93% AUC。消融实验显示 UVS 和 CGR 分别带来增益，组合后效果最好；在 Celeb-DF 的性别和种族分组公平性分析中，CS-DFD 的 Skew 最低，训练时间仅比原骨干增加约 2%。

## 贡献与局限

- 通过实证分析揭示异质伪造数据之间的梯度冲突是“1+1<2”现象的重要原因。
- 提出 UVS 与 CGR 协同的 CS-DFD，在参数优化和特征表示两个层面抑制冲突。
- 在跨数据集、扩散伪造和公平性评估中同时改善检测性能与稳定性，并保持较低额外计算开销。
- 局限：论文指出的冲突主要针对原始伪造与在线合成伪造这类异质数据；同质伪造之间未必存在同样问题，方法效果仍可能受伪造类型、数据分布、骨干网络和超参数选择影响。

---
DOI: 10.1109/tpami.2026.3687009
