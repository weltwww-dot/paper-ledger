# Zero-Shot Neural Network Evaluation With Sample-Wise Activation Patterns 总结

## 基本信息

- **标题**: Zero-Shot Neural Network Evaluation With Sample-Wise Activation Patterns
- **作者**: Yameng Peng、Andy Song、Haytham M. Fayek、Vic Ciesielski、Xiaojun Chang
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3691075
- **arXiv**: 无
- **PDF**: [TPAMI_2026_ZeroShotEvaluationSample.pdf](papers/TPAMI_2026_ZeroShotEvaluationSample.pdf)

## 一句话概括

该文提出样本级激活模式 SWAP 及其派生指标 SWAP-Score，用一种免训练的零样本度量同时刻画卷积神经网络与 Transformer 的表达能力，在视觉与语言任务上均比现有零样本指标更准确地预测网络真实性能。

## 问题与动机

零样本代理指标（又称免训练度量）因无需训练而在神经架构搜索等场景被广泛用于替代昂贵的网络评估。但现有指标普遍存在两类缺陷：与网络真实性能的相关性偏弱，且跨架构族与跨任务泛化能力差——多数指标只适用于 CNN 或只适用于 Transformer，难以兼得；部分指标甚至不如参数量、FLOPs 这类朴素基线稳定。作者希望找到一种在架构族与任务域上都通用、且与真实精度高度相关的免训练度量。

## 方法

作者提出样本级激活模式（Sample-Wise Activation Patterns, SWAP）及由其派生的 SWAP-Score。其核心思想是在一个小批量样本上统计网络的激活模式，以此刻画网络在分段线性与非线性激活下的表达能力：SWAP 以 Signum 函数作为指示函数记录激活模式，并按样本逐条统计，从而保留标准激活模式所丢失的结构信息。SWAP-Score 的显著特点是不依赖标签，因而可前移到语言模型的预训练阶段去估计其下游表现。作者还给出带正则化的变体，通过尺度归一化抑制单纯由网络规模带来的偏置，使指标既含结构信息又消除尺寸偏好。

## 实验与结果

评测覆盖五类架构空间（NAS-Bench-101、NAS-Bench-201、NAS-Bench-301、TransNAS-Bench-101-Micro/Macro）上的 ReLU 卷积网络，横跨八项计算机视觉任务，并与 15 种现有免训练度量对比；同时在 GELU 类 Transformer 的 FlexiBERT 架构空间上结合 GLUE 任务做对照。结果显示：SWAP-Score 与 DARTS CNN 在 CIFAR-10 验证精度的斯皮尔曼相关系数达 0.93，FlexiBERT Transformer 在 GLUE 任务上为 0.71，均优于对比的现有零样本指标。将 SWAP-Score 接入演化搜索形成 SWAP-NAS 后，在 CIFAR-10 与 ImageNet 上分别仅需约 6 分钟与 9 分钟 GPU 时间即可取得与先进 NAS 方法相当的结果。

## 贡献与局限

- 提出 SWAP 与 SWAP-Score：一种同时适用于 CNN 与 Transformer、跨越视觉与语言任务的免训练零样本度量，相关性显著优于同类最优指标。
- 指标与标签无关，可用于预训练阶段的语言模型性能预估，扩展了零样本度量的适用时点。
- 与演化搜索结合形成 SWAP-NAS，以极低 GPU 开销获得竞争性架构搜索结果。
- 局限：指示函数目前固定采用 Signum 函数，尚无法刻画激活值内部的细粒度差异；预训练数据集与超参对零样本估计的影响也尚未系统研究，均列为未来工作。

---
DOI: 10.1109/tpami.2026.3691075
