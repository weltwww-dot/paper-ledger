# Uncertainty-Aware Dynamic Learning With Fuzzy-Guided Temporal Aggregation for Reliable Anomaly Detection 总结

## 基本信息

- **标题**: Uncertainty-Aware Dynamic Learning With Fuzzy-Guided Temporal Aggregation for Reliable Anomaly Detection
- **作者**: Dongqing Jia, Jin Yang, Ye Wang, Yanzhen Zhu, Huijia Liang, Mingming Zhan
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3706099
- **arXiv**: 无
- **PDF**: [TDSC_2026_FuzzyGuidedTemporalAggregation.pdf](papers/TDSC_2026_FuzzyGuidedTemporalAggregation.pdf)

## 一句话概括

提出 FuzzyWatcher 框架，将模糊置信先验注入溯源图的时序消息传递与聚合，实现对隐蔽持久攻击的可靠异常检测。

## 问题与动机

现代网络攻击常采用隐蔽、长期存活的技巧（如 APT），容易绕过传统检测器；系统溯源图（provenance graph）为异常检测提供了丰富上下文，但确定性节点表示难以刻画不确定性，会模糊语义并降低可解释性。部署中面临两大缺口：一是属性、边语义与演化拓扑中的不确定性，会被日志中断和开放世界模仿放大；二是长期运行可靠性问题，校准不良会累积误报并动摇阈值稳定性。因此需要一种既能感知不确定性、又能在非平稳环境中长期稳定运行的溯源图异常检测方法。

## 方法

作者提出 FuzzyWatcher，一个不确定性感知的动态图学习框架。审计日志被建模为异构时序图，采用仅含良性数据的自监督链路预测训练，无需攻击标签。骨干网络由 TGN（事件级时序建模）与 GraphSAGE（全局拓扑增强）组成。两个互补模块被注入消息传递与时序融合：FCEM（模糊置信评估矩阵）基于时间稀有度 IDF、特征偏离 FR 与结构偏离 LOF 三个统计量，经可学习权重经 sigmoid 融合为 [0,1] 置信度，作为前件隶属度与认知不确定性代理；DFMA（动态模糊机制聚合）以最近 K 个历史嵌入为可训练后件，用基于表示漂移与邻域 JS 散度的复合距离经 softmax 生成稀疏激活，并按置信度插值融合当前与历史表示，其有界性与梯度稳定性有理论证明。异常评分在窗口级整合异常度（标准化重建损失）、稀有度与跨窗传播三方面证据，并用基于 GPD 的 POT 极值阈值实现稳定校准。

## 实验与结果

在 DARPA TC（E3/E5 的 THEIA、CADETS、ClearScope）与 StreamSpot 共七个公开数据集上评估，实验于 64GB 内存、Intel i9-14900K CPU（无 GPU）上运行。结果显示近完美的召回率与有竞争力的 AUC/F1：E3-THEIA 上 Accuracy 0.993、AUC 0.996；E3-CADETS 与 E5-THEIA、E5-CADETS- 上多项指标达 1.000；CADETS+ 上以 Precision 1.000、F1 0.923 显著优于 KAIROS（0.438/0.609）；StreamSpot 图级任务与 KAIROS 持平且 FPR/EER 为零。节点级 ADP 对比中在 E3-CADETS、E3/E5-ClearScope、E5-CADETS 上最优。运行期每窗口处理时间中位数约 9 秒、吞吐约 3.4k 事件/秒、平均内存 214MB；冷启动后 1000+ 窗口阈值稳定（均值约 2.774）、误报率接近零；对抗扰动下 AUC 由 0.9904 仅降至 0.9804。消融显示完整模型 Precision 88.4%、Recall 100%、F1 93.6%、AUC 99.8%，去掉 FCEM 后 Precision 降至 56.5%，去掉 DFMA 后 Recall 降至 76.1%、AUC 87.4%，说明 FCEM 主要抑制误报而 DFMA 恢复弱而持续的异常信号。

## 贡献与局限

贡献：提出不确定性感知的神经模糊溯源异常检测框架，无需攻击标签与显式规则；FCEM 与 DFMA 两个可微、可审计模块注入统计性模糊置信先验，并有有界性与梯度稳定性理论保证；窗口队列结合多准则评分与 POT 极值阈值，缩小分析者排查空间并稳定长期运行阈值；在多个基准与真实审计日志上验证了有效性、可部署性与对抗鲁棒性。局限：仅显式建模认知不确定性，未建模审计日志中的偶然（aleatoric）噪声；缺少在生产级安全运营中心（SOC）中面向任务流程的用户研究，如首次正确分诊时间等指标仍需纵向评估；跨审计模式、实体类型与系统语义的迁移适应留待未来工作。

---
DOI: 10.1109/tdsc.2026.3706099
