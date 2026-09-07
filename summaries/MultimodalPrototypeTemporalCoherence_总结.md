# Multimodal-guided prototype calibration and temporal coherence-aware hybrid matching for few-shot action recognition 总结

## 基本信息

- **标题**: Multimodal-guided prototype calibration and temporal coherence-aware hybrid matching for few-shot action recognition
- **作者**: Yiyuan An, Yingmin Yi, Yiwei Yuan, Rui Yu, Qiming Xue
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108930
- **arXiv**: 无
- **PDF**: [NN_2026_MultimodalPrototypeTemporalCoherence.pdf](papers/NN_2026_MultimodalPrototypeTemporalCoherence.pdf)

## 一句话概括

本文提出多模态引导的 MGTH 少样本动作识别框架，融合运动增强、文本引导原型校准与时间一致性混合匹配，在四个基准及跨域与零样本任务上均达到领先精度。

## 问题与动机

少样本动作识别方法在区分相似类别时面临三大挑战：(a) 时空特征与运动特征互补且关键，但运动特征常被忽视；(b) 过度依赖单模态视频数据，多模态信息未被充分利用，导致类别原型精度不足、对未见类别存在偏差；(c) 动作的时间分布存在类内时间偏移（同类别不同视频帧序错位）与类间局部相似（不同类别子序列运动模式相近），使现有严格有序的时间对齐与子序列匹配策略失效，例如 "Putting pen into cup" 与 "Taking pen out of cup"、"Pushing something" 与 "Tipping something over" 等难以区分。因此需要一种更通用的匹配策略与多模态表征，以少量标注样本准确识别相似动作。

## 方法

作者提出 MGTH（Multimodal-guided prototype calibration and temporal coherence-aware hybrid matching）框架，以 CLIP 为基线并冻结文本编码器、微调视觉编码器，包含四个核心组件。其一是运动增强时间聚合模块（MTAM）：用时间 Transformer 建模空间外观特征的全局时间关系得到时空特征，再用 1D 卷积（核 3、步长 1）处理后相邻帧特征之差作为特征级运动表示，二者加权求和，全程无需 3D 卷积或光流计算。其二是文本引导原型校准模块（TPCM）：以视觉原型为 Query、视觉原型与类文本特征拼接为 Key/Value 做多头交叉注意力，并配合残差与 FFN 精化视频原型。其三是视频-文本适配目标（VTA）：采用 Prefix、Cloze、Suffix 三类提示模板（如 "[CLS], a video of action"），通过双向 InfoNCE 式概率（pvideo-text 与 ptext-video）最大化视频特征与对应文本表征的相似度，将 CLIP 从图像-文本匹配迁移到视频-文本匹配。其四是时间一致性感知混合匹配（TCH）：联合帧级与元组级（含位置编码的有序帧对）双向 Mean Hausdorff Metric（Bi-MHM）缓解类内偏移与类间局部相似，并对输入视频施加时间一致性正则化——拉近相邻帧特征、推远非相邻帧特征（窗口 δ 与超参数 σ 按数据集设置），以捕捉长期时间顺序而不增参数。总损失为 L = Lhybrid + β·Ltemporal-regular + (1−β)/2·(Lvideo-text + Ltext-video)。该框架还扩展到跨域少样本与零样本动作识别任务。

## 实验与结果

在 Kinetics-100、UCF-101、HMDB-51、SSv2 四个基准上以 5-way 1-shot/5-shot 评估（每个视频均匀采样 8 帧并缩放至 256×256，CLIP-ResNet50 与 CLIP-ViT-B/16 骨干，20 轮、每轮 1000 个元任务，Adam 初始学习率 1e-4，在 10,000 个测试任务上取平均精度）。基于 CLIP-ViT-B/16 的 MGTH 取得 HMDB-51 80.5%/89.1%、UCF-101 97.5%/99.1%、Kinetics 92.1%/96.3%、SSv2 63.1%/73.9%（1-shot/5-shot）；基于 CLIP-ResNet50 时分别为 73.9%/82.7%、91.8%/97.6%、88.1%/92.2%、60.2%/63.7%。相比最佳单模态方法 MSVT，CLIP-ResNet50 版在 Kinetics 与 UCF-101 的 1-shot 上分别高出 10.9% 与 1.4%；SSv2 1-shot 较 HyRSM++ 由 55.0% 提至 60.2%。消融（5-way 1-shot，HMDB-51/SSv2）：CLIP-OTAM 为 63.0%/44.1%，换成 TCH 基线提升至 66.1%/47.5%，依次加 MTAM、VTA、TPCM 后达到 68.2%/49.8%、68.8%/50.5%、71.8%/57.4%，全模块集成后 73.9%/60.2%；对比 MGTH-OTAM（71.3%/58.5%）、MGTH-TRX（70.7%/57.8%）、MGTH-Bi-MHM（71.6%/58.9%），MGTH-TCH 最优。效率上 MTAM 相较 MGTH-C3D 减少约 15.7% FLOPs 与 31.3% 参数量且精度更高（SSv2 1-shot 56.7% vs 52.3%）。跨域实验（Kinetics-Small 源域→UCF-101/HMDB-51/SSv2）中 MGTH 全部最优，1-shot 分别达 72.2%/45.8%/35.9%，较 SEEN 提升显著；零样本识别在 HMDB-51 达 53.8%、UCF-101 约 76%，优于 ActionCLIP（40.8%/58.3%）、Vita-CLIP（48.6%/75.0%）、XCLIP（44.6%/72.0%），与 ViFi-CLIP（53.9%/76.2%）相当。t-SNE 与每类精度可视化也表明 TCH 与 TPCM 增强了类内紧凑性与类间可分性。

## 贡献与局限

主要贡献：(1) 提出 MTAM，在不使用 3D 卷积或光流的前提下同时编码互补的时空与运动特征；(2) 设计 TPCM，充分利用 CLIP 文本语义先验校准视频原型，并构造 VTA 目标以提升 CLIP 在少样本任务上的适配性；(3) 提出 TCH，融合帧级与元组级匹配并施加时间一致性正则化，缓解类内时间偏移与类间局部相似造成的度量偏差；(4) 在 HMDB-51、UCF-101、Kinetics、SSv2 上的大量实验及跨域、零样本扩展验证了方法的有效性。局限方面：多尺度自注意力、跨模态交叉注意力与混合匹配带来更高的 FLOPs 与推理延迟（SSv2 5-way 1-shot 下 CLIP-ResNet50 版约 11.9G FLOPs、105.6ms；CLIP-ViT-B 版约 34.2G FLOPs、133.7ms）；所用文本提示为手工设计的静态模板，对不同类别与场景的适应性有限。未来工作拟设计更高效的轻量架构，并引入可学习或条件式提示学习（如基于 CoOp 的改进）以提升对新颖类别的泛化。

---
DOI: 10.1016/j.neunet.2026.108930
