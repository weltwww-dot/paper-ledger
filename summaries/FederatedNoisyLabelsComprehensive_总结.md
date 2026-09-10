# Federated learning with noisy labels: A comprehensive and concise review of current methodologies and future directions 总结

## 基本信息

- **标题**: Federated learning with noisy labels: A comprehensive and concise review of current methodologies and future directions
- **作者**: Jia Dong、Rui Zhu、Xinyi Shang、Jing-Hao Xue
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108889
- **arXiv**: 无
- **PDF**: [NN_2026_FederatedNoisyLabelsComprehensive.pdf](papers/NN_2026_FederatedNoisyLabelsComprehensive.pdf)

## 一句话概括

本文系统梳理带噪标签联邦学习（FLNL）的挑战、方法分类与未来研究方向。

## 问题与动机

联邦学习保护本地数据，但标签噪声也被分散在各客户端，难以由服务器集中发现和修正。全文归纳了本地噪声、客户端间噪声异质性、对噪声的局部过拟合以及基准不足四个核心问题。作者希望弥合联邦学习与噪声标签学习交叉领域缺少系统综述的空白。

## 方法

文章采用综述与分类框架，将现有 FLNL 研究分为 sample-wise、client-wise、model-wise 和 benchmark-wise 四类。分类分别对应样本层噪声处理、客户端层差异、模型层鲁棒学习和评测基准建设。作者比较各类方法如何处理隐私约束、数据异质性、噪声校正和模型收敛，并据此提出研究议程。

## 实验与结果

本文不是提出单一算法的实验论文，而是对既有研究进行综合分析。全文明确指出，现有工作在四类挑战上形成了不同技术路线，但 benchmark-wise 研究仍不足，跨客户端噪声异质性与真实部署条件下的可比评测仍是薄弱环节。

## 贡献与局限

贡献在于给出面向 FLNL 的首个综合且精炼的专门综述、四挑战 taxonomy 及对应的未来方向。局限是综述结论依赖既有文献的覆盖与报告质量，不能替代统一数据、统一噪声协议下的实证比较。

---
DOI: 10.1016/j.neunet.2026.108889
