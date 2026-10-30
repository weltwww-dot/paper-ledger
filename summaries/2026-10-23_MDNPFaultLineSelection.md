# Memory Dendritic Neural P Systems for Multi-ground Type Fault Line Selection in Distribution Networks 总结

## 基本信息
- **标题**: Memory Dendritic Neural P Systems for Multi-ground Type Fault Line Selection in Distribution Networks
- **作者**: Song Ma、Fei Li、Xiu Yin、Xiyu Liu、Yangheng Hu、Xing Zhang、Mingyao Ma
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109795
- **发表**: 2026-10-23
- **日期来源**: 出版社正式PDF首页Available online；2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109795
- **PDF**: [NN_2026_MDNPFaultLineSelection.pdf](papers/NN_2026_MDNPFaultLineSelection.pdf)

## 一句话概括
以记忆树突神经P系统学习不同接地方式下的故障特征，结合电网仿真和调度数据完成单相接地故障选线及在线更新。

## 问题与动机
中性点不接地和经消弧线圈接地时，故障信号分布不同；传统点神经元式P系统又难充分利用树突分支计算，需要兼顾识别能力和计算开销。

## 方法
引入记忆树突因子的触发规则、可调树突分支和自适应学习，使用CIM描述电网结构并构建多工况仿真，混合真实调度数据训练，再按在线方案持续更新选线模型。

## 实验与结果
现场应用评估含578个实时样本；不接地和经消弧线圈接地的选线准确率分别为98.2%和97.3%，数据采集至结果输出平均约1.78秒，另提供两个变电站故障案例。该响应时间不包含一次约200—240秒的模型重训练，且与混合数据集上的离线结果分别统计（PDF第13—14页，表11）。

## 贡献与局限
将树突式计算与电网结构、混合数据和实际案例结合。正文对混合数据总量有7,790与7,680的不一致表述，划分细节限制独立复核；真实调度量以2—4秒频率更新，主要考虑稳定高斯噪声，暂态故障、高频扰动和更广泛电网迁移仍需检验（PDF第11、14—15页）。

---
DOI: 10.1016/j.neunet.2026.109795 | PDF: [NN_2026_MDNPFaultLineSelection.pdf](papers/NN_2026_MDNPFaultLineSelection.pdf)
