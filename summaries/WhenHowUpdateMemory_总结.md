## 基本信息

- **标题**：Learning When and How to Update Memory for Video Object Segmentation
- **研究方向**：半监督视频目标分割、变化感知记忆更新
- **作者**：Shengye Qiao、Changqun Xia、Yanjie Liang、Xiaowu Chen、Jia Li
- **期刊 / 年份**：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **DOI**:10.1109/TPAMI.2026.3684742
- **PDF**：[TPAMI_2026_WhenHowUpdateMemory.pdf](papers/TPAMI_2026_WhenHowUpdateMemory.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 Change-Sensitive Network（CSNet），根据视频目标的语义变换和空间形变自适应决定记忆何时更新，并分别在片内和跨片段强化目标原型与变化。

## 问题与动机

现有 memory-based 半监督视频目标分割方法常按固定帧间隔更新记忆，在对象发生语义突变、遮挡、消失重现或剧烈形变时容易错过关键帧；被动抽取原型还不能突出变化前后的差异。复杂数据集 VOST、MOSE 和长视频场景因此显著暴露固定更新机制的不足，需要同时学习“何时更新”和“如何更新”。

## 方法

CSNet 的 Adaptive Perception-Capture（APC）模块用空间放大、语义放大及 frame/object/pixel 三级 hierarchical contrastive learning，比较概率分布的 Jensen–Shannon divergence 与全局向量余弦相似度，将视频划分为 object-change clips。进入同一片段时，Short-term Memory Modulation（SMM）按相似度加权并传播片内原型；跨片段时，Long-term Memory Augmentation（LMA）感知当前与片段首帧差异、维护一致性并保存 variation-enhanced prototype。模型还以 plug-in 方式替换其他方法的固定更新机制。

## 实验与结果

实验覆盖 DAVIS 2016/2017、YouTube-VOS 2018/2019、VOST、MOSE、LVOS 和 BURST 八个数据集。相较同为 ResNet-50 的 Cutie，CSNet 在 DAVIS 2017 test/val 的 J&F 分别提升 3.2%/1.8%，在 YouTube-VOS 2019/2018 val 的 G 分别提升 1.1%/0.9%；在复杂数据集上，VOST val 的 J 比 RMem 高 2.5%，MOSE val 的 J&F 比 Cutie 高 4.9%，LVOS test 比 STMA 高 1.5%，BURST test 的 HOTA 比 Cutie 高 2.8%。模型达到 31 FPS；APC 的采样帧数 K 从 4 增至 12 时，VOST val 的 J 从 48.5% 增至 54.3%。

## 贡献与局限

贡献包括：用 APC 显式感知目标语义—空间变化；以 SMM/LMA 处理片内平滑变化和跨片段差异；在普通、复杂、长视频数据集及视觉跟踪任务中验证了自适应记忆更新的有效性和可插拔性。局限是 VOST/LVOS 等复杂长视频精度仍低于普通数据集（文中示例为 54.3%/58.9% 对 YouTube-VOS 2019 val 的 87.2%），更强 backbone 会牺牲效率；目标初始标注严重缺失或目标空间重叠时仍会失败，后续需兼顾实时性、能耗与精度。
