# Beyond Sparsity: Receptive Field Expansion and Cross-Task Fusion for LiDAR Multi-Task Perception 总结

## 基本信息

- **标题**: Beyond Sparsity: Receptive Field Expansion and Cross-Task Fusion for LiDAR Multi-Task Perception
- **作者**: Shengjie Huang, Runbang Zhang, Shuo Liu, Yougang Bian, Xiaohui Qin
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 机器学习方法；LiDAR 三维感知、多任务学习与自动驾驶
- **DOI**: 10.1109/tpami.2026.3688337
- **PDF**: [TPAMI_2026_BeyondSparsityReceptiveField.pdf](papers/TPAMI_2026_BeyondSparsityReceptiveField.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出统一的 LiDAR 多任务感知网络，通过 SDIMI 在保持稀疏性的同时扩大空间感受野，并用 SIDMF 以检测实例先验增强语义分割，从而联合提升 3D 目标检测和点级语义分割。

## 问题与动机

Submanifold sparse convolution 只在非空位置激活，计算高效却限制了有效感受野和长程上下文；额外下采样或转为稠密 BEV 又会改变稀疏模式、增加内存与计算。已有多任务方法通常只共享浅层特征，或通过全局交互引入无关区域噪声，未充分利用检测实例结构对分割边界和语义判断的帮助。

## 方法

网络采用 voxel-based sparse encoder–decoder，并设置检测与分割分支。SDIMI 将多尺度特征对齐到非空的高分辨率体素位置，仅对这些位置做三线性插值，再由空间注意力自适应融合，扩大感受野而保持双分支稀疏性。SIDMF 根据预测 3D box 构造点—实例映射 mask，对落入 box 的检测实例特征做平均，经可学习 MLP 对齐通道后以残差方式加入点级分割特征；训练同时使用检测、点级分割和辅助 BEV 分割损失，并采用任务不确定性加权。

## 实验与结果

在 nuScenes（700/150/150 个场景用于训练/验证/测试）和 Waymo Open Dataset（798/202/150 个序列）上，nuScenes 验证集达到 67.1% mAP、72.0% NDS 和 84.4% mIoU，测试集达到 69.9% mAP、73.5% NDS；Waymo 验证集达到 79.8% mAPH-L2 和 72.3% mIoU。消融中，多任务基线为 79.6% mIoU/64.4% mAP/69.9% NDS，加入 SDIMI 后为 80.7%/65.1%/70.7%，再加入 BEV 一致性损失和 SIDMF 后达到 84.4%/67.1%/72.0%；最终 nuScenes 推理延迟为 107 ms、FLOPs 为 156.1G。用真值 box 替代预测 box 时 mIoU 为 85.1%，box 中心扰动 8% 时仅下降 0.9%。

## 贡献与局限

贡献包括：提出保持特征密度的多尺度感受野扩展 SDIMI；提出利用 box mask 精确传递实例级检测特征的 SIDMF；在两个大规模 LiDAR 基准上以统一模型取得检测、分割和效率的综合改进。局限方面，全文验证范围集中在 nuScenes 与 Waymo 两个数据集，且跨任务融合仍依赖检测候选框质量；虽然实验显示对定位扰动具有鲁棒性，但原文未报告更多传感器配置、跨域迁移或极端检测失效场景的结果。

---
DOI: 10.1109/tpami.2026.3688337
