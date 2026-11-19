# Multi-FedLinks: Highly reliable decentralized multibiometric federated learning links 总结

## 基本信息
- **标题**: Multi-FedLinks: Highly reliable decentralized multibiometric federated learning links
- **作者**: Jian Guo、Hengyu Mu、Hengyi Ren 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109519
- **发表**: 2026-08-22
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109519

## 一句话概括
Multi-FedLinks 面向分布式多生物特征识别，设计去中心化联邦协作机制并关注链路可靠性与安全风险。

## 问题与动机
既有生物特征联邦学习多处理单一模态，且较少覆盖纵向多模态数据分散在不同终端的现实情形；多终端协作还面临拜占庭和投毒风险。

## 方法
Multi-FedLinks 由多个具拜占庭鲁棒性的 FedLink 结构组成，同模态客户端先在各自链接内协作，再由第三方服务器连接不同模态链接实现纵向多生物特征训练；论文同时评估标签翻转、模型投毒和数据异质性。

## 实验与结果
在 NUPT-FPV 上评估识别与攻击鲁棒性。表11中该数据集投毒比例20%时，Krum 的 EER/TAR 为1.26%/98.51%，Trim-mean 为1.49%/97.85%，Gaussian 为0.96%/99.05%；表13 FedLink 运行568.76秒，FedAvg 为224.53秒，显示安全机制有计算代价。

## 贡献与局限
工作将纵向多模态联邦扩展到生物特征识别，并以 FedLink 链接抵御拜占庭行为。威胁评估并非所有攻击皆被消除：表12分类器后门 ASR 两者均为100%，因此不应把“高安全”解读为全面防护；数据也主要来自单一基准。

---
DOI: 10.1016/j.neunet.2026.109519
