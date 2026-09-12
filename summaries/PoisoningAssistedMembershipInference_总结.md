# Poisoning-Assisted Membership Inference in Federated Learning 总结

## 基本信息

- **标题**: Poisoning-Assisted Membership Inference in Federated Learning
- **作者**: Xukun Luan, Yuanguo Bi, Kuan Zhang et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing, 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3699355
- **PDF**: [TDSC_2026_PoisoningAssistedMembershipInference.pdf](papers/TDSC_2026_PoisoningAssistedMembershipInference.pdf)

## 一句话概括

论文在授权防御研究语境下分析联邦学习的成员隐私风险，提出面向黑盒 FL 模型的时间演化投毒效应（TEPE）审计方案，并设计 RR-Group 作为对应防御。

## 问题与动机

现有成员推断攻击往往依赖目标模型或良性客户端训练数据的先验知识，在黑盒联邦服务中性能会明显下降。论文关注攻击者只控制自身客户端、无法观察内部训练过程时，如何从投毒对目标样本预测的持续影响中识别成员关系，同时评估联邦系统对这类风险的防护能力。

## 方法

TEPE 分为投毒和评分两个阶段：在不同审计需求下使用 Adv、Spy、Adv&Spy 三种策略施加受控投毒，再量化目标样本预测随时间的变化，并以无监督推断模型提取成员特征。其依据是被良性客户端训练过的样本对投毒扰动可能更不易改变。针对该风险，RR-Group 在训练阶段对预测或标签进行分组随机响应，以兼顾模型性能和隐私保护。

## 实验与结果

实验覆盖 Purchase-100、MNIST、Fashion-MNIST、CIFAR-10 和 CIFAR-100，采用 5 个客户端、FedAvg 和 25 轮全局聚合，并与多种成员推断方法比较。TEPE 在不掌握目标模型和良性数据的条件下仍取得有竞争力的推断准确率与 F1-score，且可避开两种代表性防御；在 CIFAR-10 上，TEPE 在 FedAvg、Krum 和 Trimmed Mean 三种聚合规则下的 F1-score 均为 0.851，另有实验表明 RR-Group 能降低 TEPE 的推断性能。

## 贡献与局限

论文揭示了黑盒 FL 中投毒效应的时间轨迹可以成为成员推断信号，并给出覆盖不同攻击知识条件的 TEPE 与配套防御。局限是结论依赖模拟客户端、特定投毒比例和模型设置；真实部署中的安全聚合、客户端采样、强鲁棒聚合及更复杂攻击者协作仍需持续验证。本文内容仅用于授权的隐私风险评估与防御设计。

---
DOI: 10.1109/tdsc.2026.3699355
