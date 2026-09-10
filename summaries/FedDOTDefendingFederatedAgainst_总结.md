# FedDOT: Defending Federated Learning Against Overwhelming Targeted Attacks 总结

## 基本信息

- **标题**：FedDOT: Defending Federated Learning Against Overwhelming Targeted Attacks
- **作者**：Priyesh Ranjan, Ashish Gupta, Federico Corò, Sajal K. Das
- **期刊 / 年份**：IEEE Transactions on Artificial Intelligence，2026
- **研究方向**：联邦学习安全与定向攻击检测
- **DOI**:10.1109/TAI.2026.3676747
- **PDF**：[TAI_2026_FedDOTDefendingFederatedAgainst.pdf](papers/TAI_2026_FedDOTDefendingFederatedAgainst.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

FedDOT 利用当前轮客户端模型更新之间的 Pearson 相关性，把客户端组织成相关图，并通过最大生成树攻击者检测（MST-AD）与最稠密图攻击者检测（density-AD）隔离协同攻击者，即使攻击者超过半数也能降低其聚合影响。

## 问题与动机

联邦学习隐藏客户端身份但无法阻止恶意客户端投毒；标签翻转和后门等定向攻击可以在保持总体模型表现的同时破坏目标类别，因而更难检测。许多防御假设攻击者少于良性客户端，或依赖欧氏距离、余弦相似度和 IID 数据，在攻击者占多数、非 IID 数据时会把良性更新误判为异常或被攻击者拉偏。本文针对攻击者人数超过参与者一半的 overwhelming targeted attack，目标是识别恶意集合并在聚合时将其更新权重置零。

## 方法

服务器对每轮客户端权重更新计算 Pearson 相关系数；该系数对更新的尺度与平移不敏感，更适合非 IID 客户端。FedDOT 假设具有共同目标的攻击者彼此更新更相似、且与良性更新更不相似，然后在相关图上运行两种检测器：MST-AD 使用最大生成树逐步识别并移除异常关联，density-AD 使用稠密子图结构定位相互靠近的攻击者。检测出的更新在 FedAvg 聚合中被强制置零。论文还给出了相关空间中的理论上下界、全部攻击者可检测的必要/充分条件及收敛分析；威胁模型假设服务器可信、攻击者不能观察良性训练或前轮检测结果，且至少有两个良性客户端。

## 实验与结果

实验使用 MNIST、fashion-MNIST 和 CIFAR-10，每个数据集有 60,000 个训练样本与 10,000 个测试样本，按 Dirichlet α=0.9 划分给 50 个客户端；攻击比例从 10% 到 70%，覆盖单标签翻转、多标签翻转、位置和宽度变化的后门及混合攻击，并与 FedAvg、FoolsGold、CONTRA、FedBAP 和 FLAME 比较。MNIST 上 A-70 单标签翻转时 MST-AD 与 density-AD 的 ASR 均为 0，而 FoolsGold 为 100%；在三数据集的 overwhelming 设置中，所提方法的 ASR 通常控制在 8% 以内，且论文摘要报告目标攻击 ASR 小于 10%、模型准确率下降小于 2%。在 K-49 的 50 客户 A-70 扩展实验中，density-AD 的单/多标签翻转准确率与 ASR 为 80.24%/0.46% 和 80.70%/1.13%，后门为 82.85%/5.99%。

## 贡献与局限

贡献包括：提出能处理恶意客户端占多数的 FedDOT 框架；以当前轮更新相关性结合 MST 与稠密图结构，降低对 honest-majority、IID 和固定攻击者比例的依赖；给出检测边界并在三种基准和 K-49 上验证低 ASR、较少误报及早期检测。局限是威胁模型不包含无目标攻击，攻击者不能改变策略且至少需两个良性客户端；后门在更复杂的 CIFAR-10 与 K-49 情况下仍有较高 ASR，未来还需处理无目标与目标混合攻击及更动态的对手。
