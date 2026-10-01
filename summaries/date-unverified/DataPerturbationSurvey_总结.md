# Data-Centric Challenges, Techniques, and Impacts: A Survey on Image Data Perturbation 总结

## 基本信息

- **标题**: Data-Centric Challenges, Techniques, and Impacts: A Survey on Image Data Perturbation
- **作者**：Peng-Fei Zhang, Guangdong Bai, Xin-Shun Xu, Zi Huang
- **期刊 / 会议**：IEEE Transactions on Knowledge and Data Engineering，2026
- **研究方向**：数据中心化机器学习、图像扰动、对抗鲁棒性与安全
- **DOI**:10.1109/tkde.2026.3709786 · **PDF**：[TKDE_2026_DataCentricChallengesTechniques.pdf](papers/TKDE_2026_DataCentricChallengesTechniques.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文以图像分类为主线，从数据中心化视角统一综述 data perturbation 的类型、生成方式、攻击/防御应用及其对深度模型鲁棒性的影响，解释扰动如何既暴露模型脆弱性又帮助构建更可靠的模型。

## 问题与动机

深度模型依赖具有代表性的数据，但真实数据会受到传输、压缩、传感器误差、天气、光照、分布变化和恶意攻击等影响，导致可靠性与泛化能力下降。已有综述往往按某一种攻击、某一种防御或某类模型组织，缺少对扰动类型、跨范式关系、内在脆弱机制及攻击—防御共演化的统一理解。

## 方法

作者首先按生成是否涉及优化将扰动分为启发式扰动（HP）和优化引导扰动（OP），再从攻击意图、幅度约束、尺度、作用范围、知识可得性等维度建立分类。随后系统整理 evasion、poisoning/backdoor、augmentation、输入预处理、randomized smoothing 和 adversarial training，覆盖 CNN、ViT 与 MLLM，并讨论对抗迁移、黑盒查询效率、不可感知性、多扰动鲁棒性、鲁棒性—准确率权衡、过拟合和物理部署等机制与解决策略。

## 实验与结果

本文是综述论文，没有提出新的训练模型或独立实验；主要产出是扰动分类表、应用与策略对照表、HP/OP 攻击和防御的结构化总结，以及对代表性鲁棒性 benchmark 的批判性分析。作者指出现有基准多依赖合成扰动，覆盖的扰动类型、学习阶段和行为指标仍不足，因而未报告统一的新量化比较结果。

## 贡献与局限

- 贡献一：以扰动特征而非单一攻击公式组织文献，统一覆盖攻击、防御、挑战与解决方案，并分析其内在联系。
- 贡献二：跨 CNN、ViT、MLLM 及数字/物理场景归纳脆弱性机制，强调扰动在压力测试和鲁棒性增强中的双重作用。
- 局限：主体范围集中在图像分类，其他模态、任务及多扰动共存场景仍不充分；现有 benchmark 的真实性、覆盖面和跨训练—部署阶段评估仍是开放问题，未来方向部分由作者放在补充材料中。

---

DOI: 10.1109/tkde.2026.3709786
