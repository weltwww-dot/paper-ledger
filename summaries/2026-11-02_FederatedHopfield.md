# A federated many-to-one Hopfield model for associative neural networks 总结

## 基本信息
- **标题**: A federated many-to-one Hopfield model for associative neural networks
- **作者**: Andrea Alessandrelli、Fabrizio Durante、Andrea Ladiana 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109830
- **发表**: 2026-11-02
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109830
- **PDF**: [NN_2026_FederatedHopfield.pdf](papers/NN_2026_FederatedHopfield.pdf)

## 一句话概括
在联邦端共享低秩关联算子，用多层联想记忆重建跨客户端的共同原型。

## 问题与动机
客户端分布不一致时，简单平均参数可能冲淡共享结构，也可能忽略本地漂移。作者从联想记忆的角度分析可从各端提取的共同信号。

## 方法
客户端构建低秩Hebb关联算子，服务器聚合后用多层联想记忆分解出原型，并以本地熵反馈适应漂移。分析把原型可探测性与低秩信号加噪声模型中的谱阈值联系起来。

## 实验与结果
理论部分在给定噪声模型下推导初始化时的探测阈值，并讨论训练中维持谱分离所需的条件。论文的布尔–高斯受限玻尔兹曼机扩展在构造的结构化非独立同分布基准上优于FedAvg。

## 贡献与局限
把联邦聚合与联想记忆、谱可探测性统一起来。阈值依赖模型和噪声假设，共享低秩算子本身也不提供差分隐私或对抗安全保证。

---
DOI: 10.1016/j.neunet.2026.109830 | PDF: [NN_2026_FederatedHopfield.pdf](papers/NN_2026_FederatedHopfield.pdf)
