# Adaptive DBSCAN-Enhanced Oversampling for Imbalanced Network Intrusion Detection: A Boundary-Aware Approach

## 基本信息

- **标题**：Adaptive DBSCAN-Enhanced Oversampling for Imbalanced Network Intrusion Detection: A Boundary-Aware Approach
- **作者**：Jingnan Dong、Boran Zhang、Shigen Shen、Jun Liu、Guangxia Xu、Zhiquan Liu
- **期刊 / 会议**：IEEE Transactions on Dependable and Secure Computing 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：信息安全
- **DOI**：10.1109/tdsc.2026.3703615
- **arXiv**：无
- **PDF**：[TDSC_2026_AdaptiveDBSCANEnhancedOversampling.pdf](papers/TDSC_2026_AdaptiveDBSCANEnhancedOversampling.pdf)

## 一句话概括

本文提出 ADEO 入侵检测数据增强框架，用深度 Q 网络自适应选择 DBSCAN 参数，再在少数类的几何安全边界内生成样本，从而缓解极端类别不平衡并减少决策边界附近的合成噪声。

## 问题与动机

网络入侵检测中的高风险攻击往往是少数类，随机过采样和 SMOTE 容易破坏原有流形结构，尤其会在类别边界附近制造噪声，导致少数攻击漏检或误报增加。不同数据集的攻击分布、密度和特征维度差异明显，人工设置 DBSCAN 的邻域半径和最小样本数难以稳定适配；同时，粗粒度类别合并会掩盖不同攻击家族的行为特征。论文因此希望让聚类参数、采样区域、攻击类别映射和攻击相关特征都能随数据集与类别特性自适应调整。

## 方法

ADEO 由自适应 DBSCAN 参数优化、边界几何建模和约束采样三部分组成。首先把 DBSCAN 的邻域半径 ε 与 minPts 选择建模为马尔可夫决策过程，使用三层全连接 DQN 根据样本量、维度、类别比例、特征波动和 k 近邻距离等状态，通过平均召回率、纯度、噪声比例和聚类规模指标构造奖励。随后对每个攻击类的聚类结构选择凸包、最小包围椭圆或轴对齐包围盒，在安全边界内生成合成样本，避免越过真实类分布的决策边缘。框架还采用分层类别映射，并为侦察、后门、利用等攻击提取端口多样性、流量不对称性、包长变异等特征；最终将平衡数据交给 LightGBM、XGBoost、CatBoost、随机森林和 ExtraTrees 组成的加权软投票集成分类器。

## 实验与结果

实验在 Windows 11、Python 3.11、PyTorch 2.8.0 和 RTX 4070 上进行，使用 NSL-KDD、UNSW-NB15 与 CICIDS2017，分别包含 148,516、2,540,047 和 2,830,743 个样本；大数据集采用每批 10,000 行读取，所有方法使用五折交叉验证，DQN 每个数据集训练 15 个 episode。NSL-KDD 上 ADEO 的精确率、召回率和 F1 均约为 99.41%，FPR 为 0.0022、AUC 为 0.9992；UNSW-NB15 的准确率为 99.06%，FPR 为 0.0059、AUC 为 0.9988；CICIDS2017 的准确率为 99.82%，F1 为 0.9981、FPR 为 0.0008、AUC 为 0.9992。与主流过采样方法相比，ADEO 在准确率、精确率、召回率、F1、FPR 和 AUC 上整体更优，对 Backdoor、Heartbleed 等极端少数类的改善尤其明显。

## 贡献与局限

论文把深度强化学习的密度参数选择、攻击类别特征工程和边界约束过采样统一到一个入侵检测流程中，既提高了少数类识别能力，也尽量保持了真实攻击分布的拓扑结构。局限在于验证仍基于三个公开基准和离线集成分类器，合成样本在加密流量、未知攻击和真实在线流量中的有效性尚未充分检验；DQN 权重、边界扩张系数与类别映射仍需针对场景调节。后续工作应结合表示学习从原始流量提取低维特征，并检验对加密流量和未知攻击的泛化能力。

---
DOI: 10.1109/tdsc.2026.3703615
