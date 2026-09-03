# Patient-independent seizure onset zone localization 总结

## 基本信息

- **标题**: Patient-independent seizure onset zone localization with generalizable feature learning and multi-task supervision
- **作者**: Jinjie Guo, Tao Feng, Yiping Wang, Yanfeng Yang, Guixia Kang, Guoguang Zhao
- **期刊 / 会议**: Neural Networks 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109538

## 一句话概括

提出一种基于发作期立体脑电（ictal SEEG）的深度学习癫痫灶（SOZ）定位方法，通过临床引导的特征学习与多任务监督实现患者无关（patient-independent）的跨受试者泛化。

## 问题与动机

现有发作期 SEEG 的 SOZ 定位方法大多依赖患者特定训练，因发作记录稀缺与受试者间差异大而限制临床适用性；实现鲁棒的患者无关 SOZ 定位是主要挑战。

## 方法

为缓解跨受试者域偏移：交叉频率耦合（CFC）机制捕获频带间与 SOZ 相关的异常交互；自比较（SC）机制突出 SEEG 通道内发作起始的演化模式；在多头（multi-task）学习框架中加入发作检测辅助任务，提供发作起始相关的时间监督，提升时间感知与泛化能力。

## 实验与结果

在公开 OpenNeuro HUP 数据集上相较现有方法取得显著提升；额外在私有临床数据集上验证了鲁棒性与跨患者泛化能力（原文摘要未给出具体数字）。

## 贡献与局限

- 贡献一：首个以临床引导特征学习实现患者无关 SOZ 定位的深度学习方法。
- 贡献二：CFC + SC + 多任务时间监督的组合，同时保留发作时间特征并缓解域偏移。
- 局限：具体数字原文摘要未提供；更大规模多中心临床验证待展开。

---

DOI: 10.1016/j.neunet.2026.109538
