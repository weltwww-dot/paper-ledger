# CoreKD: A Context-Aware Local Region Structural Contrastive Knowledge Distillation Framework for Object Detection 总结

## 基本信息

- **标题**: CoreKD: A Context-Aware Local Region Structural Contrastive Knowledge Distillation Framework for Object Detection
- **作者**: Junfei Yi, Jianxu Mao, Yaonan Wang, Tengfei Liu, Mingjie Li, Kai Zeng, Hui Zhang, Xiaojun Chang
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-03-17
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3672967
- **arXiv**: 无
- **PDF**: [NN_2026_CoreKDContextAwareLocal.pdf](papers/NN_2026_CoreKDContextAwareLocal.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 CoreKD，用 patch-based semantic structural distillation（PSD）传递局部语义与结构知识，并用 intra-region（Ita-RC）和 inter-region（Ite-RC）约束补充上下文关系，从而提升轻量学生检测器的性能。

## 问题与动机

现有目标检测知识蒸馏方法多在像素层面匹配教师和学生特征，容易把背景噪声和冗余信息传给学生，同时忽略局部结构和区域间上下文。重型教师模型的计算开销又限制了检测器在边缘设备上的部署。CoreKD 试图在更高粒度的局部区域中传递有区分力的知识，并保持对全局语义依赖的建模能力。

## 方法

CoreKD 将教师和学生的中间特征划分为不重叠 patch，对应 patch 组成正样本、非对应 patch 组成负样本；语义相似度用特征内积表示，正样本的结构相似度用 SSIM 表示，再构成语义结构对比蒸馏损失 Lpsd。Ita-RC 在每个区域内聚合 patch 特征并用 softmax 后的均方误差约束教师与学生，Ite-RC 聚合不同区域以传递区域间上下文，二者合成 Lrcc。最终损失为 Lall=Ldet+λ1Lpsd+λ2Lrcc；训练时教师参数冻结，测试时只使用训练后的学生检测器。

## 实验与结果

实验覆盖 MS COCO 2017（120K 训练图像、5K 验证图像）、PASCAL VOC（VOC 07+12 共 16,551 张训练图像、4,952 张测试图像）和 VisDrone（6,471/548 张训练/验证图像）。在 GFL 的 ResNet-101 教师与 ResNet-50 学生设置下，COCO mAP 为 43.6，较无蒸馏学生的 40.2 提升 3.4；AP50、AP75、APS、APM、APL 分别为 62.1、47.3、26.6、48.0、56.4。相同设置下，CoreKD 在 Faster R-CNN、RetinaNet 和 FCOS 上的 mAP 分别为 40.8、39.8、42.4，较学生基线提升 2.4、2.4 和 3.9；训练效率比较中显存为 6.25 对 6.71 GB、迭代时间为 0.5297 对 0.5991 s/iter，并取得 37.1 对 36.3 的 mAP。

## 贡献与局限

CoreKD 将局部 patch 语义结构对比学习与区域内/区域间上下文约束统一为可插拔的特征级蒸馏框架，并在 CNN、Transformer、两阶段、单阶段和 anchor-free 检测器上验证了适用性。消融实验显示完整 PSD+Ita-RC+Ite-RC 在 COCO 上达到 43.6 mAP，AP50/AP75 为 62.3/47.8。局限是 PSD 的区域选择依赖启发式先验和固定粒度，面对大尺度变化或复杂目标分布时灵活性可能受限；作者计划研究自适应区域选择和动态 patching。

---
DOI: 10.1109/tnnls.2026.3672967
