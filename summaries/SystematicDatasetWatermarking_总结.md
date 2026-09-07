# Systematic Evaluation of Dataset Watermarking for Intellectual Protection 总结

## 基本信息

- **标题**: Systematic Evaluation of Dataset Watermarking for Intellectual Protection
- **作者**: Zhen Lu, Boyu Kuang, Peng Wang, Yifeng Zheng, Anmin Fu, Yansong Gao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01（Vol. 23, No. 5, September/October 2026；全文标注 2026-07-07 在线发表）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3710863
- **arXiv**: 无
- **PDF**: [TDSC_2026_SystematicDatasetWatermarking.pdf](papers/TDSC_2026_SystematicDatasetWatermarking.pdf)

## 一句话概括

本文对截至 2025 年的 9 种数据集水印方法在统一"从零训练"评测框架下做端到端系统评估，发现多数方法存在目标类精度下降或数据整理（混合/类不平衡/对抗检测）下的鲁棒性缺陷，仅 Domain Watermark 满足全部维度但不支持图像以外模态。

## 问题与动机

深度学习高度依赖大规模高质量数据集，数据价值上升同时带来未授权使用、未经同意再分发与盗用风险（如 Clearview AI 抓取人脸数据），受 GDPR 与 EU AI Act 等监管框架推动。数据集版权保护主要有侵入式数据集水印（dataset watermarking）与非侵入式数据集指纹（fingerprinting）两条路线，其中水印因可靠建立知识产权所有权而被认为更实用可信。但现有水印研究存在两大缺口：一是缺乏统一评测框架，方法间难以端到端对比；二是很少在现实"数据整理"（data curation）场景下评估——现实中整理者（curator）常聚合多方数据（DaaS 范式，如 Appen、Amazon Mechanical Turk），既会在非对抗情形下做数据集混合（dataset mixture），也可能出于牟利目的用检测手段对抗性清除水印样本。已有工作对抗评测多采用 2018 年的过时检测手段（Spectral Signatures、Activation Clustering），最新 S&P 2025 SoK [9] 也未覆盖全面的对抗数据整理场景。本文旨在填补这些方法与其现实部署表现之间的 gap。

## 方法

作者提出两级分类学：粗粒度上按水印验证行为是否与主任务预测一致，分为预测一致（prediction-consistent：Radioactive Data、Data Isotopes、Domain Watermark、Style Transformation、EntropyMark 五种）与预测不一致（prediction-inconsistent：T&P、T&C、U&P、U&C 四种后门式）两大类；细粒度上再按标记训练样本是否为 clean-label、验证是否 target/untargeted、验证依赖 hard-label 还是 confidence 向量等划分。在统一从零训练协议下对所有 9 种方法进行端到端重实现与再评估，衡量三个维度：效用（整体 CDA 与类级 CDA）、验证能力（各方法原始协议中的 WSR、−log(p)、p 值等）、鲁棒性。非对抗鲁棒性考察模型架构迁移（ResNet-18 代理模型生成标记样本后训练 VGG-16）与数据集混合/缩减（保护者持有每类一半样本、仅持有 5 类全部样本、以及 Dirichlet(α=2) 构造的 10,000 样本类不平衡子集三种情形）；对抗鲁棒性采用三种现代检测器：Beatrix（NDSS'23，样本级离线，基于 Gram 矩阵）、TED（S&P'24，样本级在线，基于拓扑演化动力学）与 MM-BD（S&P'24，模型级、data-free、基于最大间隔统计量）。威胁模型假设数据整理者为对抗方。实验主要在 CIFAR-10（ResNet-18、120 epoch）上开展，另扩展到 Tiny-ImageNet、CIFAR-100、文本（IMDB、DBpedia）与图（COLLAB、REDDIT-MULTI-5K）数据集，并补充 PTQ/QAT 模型压缩与不同 API 查询预算下的黑盒可审计性实验。

## 实验与结果

在 CIFAR-10 上（无标记 clean 模型 CDA=92.43%），多数方法整体 CDA 损失轻微：除 Data Isotopes 外各方法在 10% 标记率内下降不超过 0.81%，与原报告一致；但类级分析揭示被忽视的现象——clean-label 的 T&C 在 1% 标记率下目标类 CDA 下降达 3.6%（整体 CDA 仅下降不到 1%），10% 标记率时目标类特征被完全破坏、CDA 归零；U&C 在 1% 与 10% 标记率下整体 CDA 分别损失 2.46% 与 4.71%。验证方面：BadNets/Blended（T&P）与 T&C 在 1% 标记率即获 WSR>90%，而 U&P 与 U&C 需更高标记率，U&P 的 WSR 为 77.23%、U&C 仅 13.61%；预测一致方法中 Data Isotopes 在 1% 标记率下实现 TPR 100%/FPR 0%（配对 t 检验，5 轮×250 张×2 探针=2500 次查询），Domain Watermark 在 1% 标记率下 WSR 达 98.10%，EntropyMark 的配对 t 检验 p 值随标记率从无标记的 0.9998 降至 1% 的 0.0014、5% 的 0.0002、10% 的 0.0000；Style Transformation 用 grid search 可在 1% 标记率下恢复真实 60° 密钥，但 gradient-based 搜索失败（恢复 28°，超出真实区间 45°–75°），且验证必须复用标记阶段的原始图像，换图后密钥恢复为 0°。非对抗鲁棒性上：架构迁移（ResNet-18→VGG-16）中 U&C 的 WSR 大幅下降 50.90%；数据集混合场景中 U&C 与 Style Transformation 完全失败（仅采用 50% 贡献者数据训练时 Style Transformation 恢复密钥为 0°），类不平衡下 Radioactive Data 的 −log(p) 趋近于 0、Domain Watermark 的 WSR 明显下降，T&C 相对稳定。对抗检测上：对预测不一致水印，TED 对多数类型检测率高（U&C 除外），Beatrix 对 BadNet/Blended 有效但对 T&C/U&P/U&C 有限，MM-BD 能识别 BadNet/Blended/T&C 的水印目标类；而预测一致方法对三者均高度鲁棒——TED 检测率极低（EntropyMark 最高仅约 12%@5% 预设 FPR）、Beatrix 各设置均不超过 8%、MM-BD 全部无法识别。扩展实验表明：Tiny-ImageNet/CIFAR-100（150 epoch、1% 标记率）上后门式方法保持强验证，U&C 显著退化，Radioactive/EntropyMark 信号弱；T&P 水印在文本与图数据集上仍有效且 TED 仍能检出非平凡比例；PTQ/QAT（INT8）压缩后多数方法水印持续且 CDA 变化很小；黑盒查询预算（B∈{30,…,1000}，2000 验证样本）下后门式方法与 Domain Watermark 仅 30 次查询即近乎完美 TPR，Data Isotopes 小预算稳定，Radioactive Data 与 EntropyMark 对查询数敏感，Style Transformation 因需搜索 12 个候选密钥（12×N 查询）而最不节省查询。

## 贡献与局限

贡献：(1) 提出比 SoK [9] 更细的分层分类学（粗+细粒度判据），并以统一简洁方式重述预测一致类水印（Radioactive Data、Data Isotopes、Domain Watermark、Style Transformation、EntropyMark）的技术机理；(2) 首次在统一从零训练、端到端重实现框架下系统评估全部 9 种水印方法（至 2025 年），覆盖效用、验证能力与鲁棒性；(3) 揭示新发现：clean-label 水印在整体精度损失可忽略时仍可致目标类显著退化（如 3.6%），以及高度现实的数据集混合场景下 U&C 与 Style Transformation 完全失败等此前未知的隐患；(4) 建立针对数据集水印的对抗设置结构化分类，并用 Beatrix、TED、MM-BD 三个现代检测器替代 2018 年陈旧防御进行评估；(5) 将评测扩展到复杂数据集、跨模态（文本/图）、模型压缩与黑盒查询预算限制下的实证可审计性。局限：(1) 除 Domain Watermark 外其余 8 种方法均存在效用下降、验证能力减弱或不鲁棒中至少一项缺陷，而 Domain Watermark 仅面向图像模态、无法推广到其他模态，说明对抗数据整理下数据集 IP 保护仍是未解决的基础性挑战；(2) 分类学与评测主要面向分类任务，生成式任务需引入语义级一致性等更合适的一致性定义；(3) 统一的理论查询代价度量是开放难题，文中仅提供经验性的查询预算对比；(4) 结论限定于统一从零训练协议与所设鲁棒性场景，作者明确其并非对 SoK 的一对一复现，而是互补性实证分析；(5) 评测未主要考虑预防性（preventive）防御，因其盲目施加成本高且损害效用。

---
DOI: 10.1109/tdsc.2026.3710863
