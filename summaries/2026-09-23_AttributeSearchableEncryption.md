# A novel attribute-based searchable encryption scheme with attribute revocation 总结

## 基本信息
- **标题**: A novel attribute-based searchable encryption scheme with attribute revocation
- **作者**: Zixin Xiong、Jun Ye
- **期刊 / 会议**: International Journal of Information Security 2026
- **发表**: 2026-09-23
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01334-x
- **PDF**: [IJIS_2026_AttributeSearchableEncryptionRevocation.pdf](papers/IJIS_2026_AttributeSearchableEncryptionRevocation.pdf)

## 一句话概括
本文提出支持属性撤销的属性基可搜索加密方案，使云端数据按访问策略检索，并在用户属性变化时更新密钥而无需重新加密全部数据。

## 问题与动机
云存储需要细粒度访问控制和密文关键词检索；用户属性撤销时，重加密数据或重发密钥会带来较高成本。作者希望降低撤销更新开销，同时给出形式化安全论证。

## 方法
方案基于双线性映射构造初始化、密钥生成、数据加密、搜索、解密和属性撤销算法。属性更新密钥处理属性变化，论文以安全游戏分析自适应安全性，并比较计算及通信开销。

## 实验与结果
论文给出标准模型下的自适应安全性证明，并报告属性撤销时可更新相关密钥与密文，无需重新加密整个数据集。性能分析显示撤销过程较所比较方案更高效；实际成本仍取决于策略规模和属性数量。

## 贡献与局限
- 将属性撤销融入属性基可搜索加密，兼顾细粒度授权与密文检索。
- 提供形式化安全分析及算法开销比较。
- 证明依赖论文采用的模型和假设；属性隐私、可信中心可用性以及大规模云环境成本仍需结合具体系统评估。

---
DOI: 10.1007/s10207-026-01334-x
