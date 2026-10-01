# Collusion-Minimized TLS Attestation Protocol for Decentralized Applications 总结

## 基本信息

- **标题**: Collusion-Minimized TLS Attestation Protocol for Decentralized Applications
- **作者**: Ugur Sen, Murat Osmanoglu, Oguz Yayla, Ali Aydin Selcuk, Ali Doganaksoy
- **期刊 / 会议**: IEEE TDSC 2026
- **发表**: 2026-09-01
- **内容状态**: 完整
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3716834
- **PDF**: [TDSC_2026_TLS_Attestation.pdf](papers/TDSC_2026_TLS_Attestation.pdf)

## 一句话概括

提出 Πcoll-min，一个最小化共谋的 TLS 证明框架：把既有 DCTLS 构造改造成可公开导出、可联合验证的版本，让去中心化应用里的多个验证者共同验证链下 TLS 数据，同时把证明方复杂度从 O(n) 降到 O(1)。

## 问题与动机

去中心化预言机（DON）等场景需要可认证的链下数据，但现有 Designated Commitment TLS（DCTLS）构造依赖指定验证者：不支持公开验证，且链上环境中易出现证明方-验证方共谋。多验证者场景若各自独立跑会话，证明方负担随验证者数线性增长。

## 方法

两层组合：(1) dx-DCTLS 通用变换层——把现有 DCTLS 构造中不可验证的部分替换为可验证对应物，升级为可导出（exportable）版本；(2) 去中心化验证层——基于分布式可验证随机函数（DVRF）与阈值签名方案（TSS），让多个验证者联合验证 TLS 证明。论文形式化定义阈值证明不可伪造性（threshold attestation unforgeability），并在标准假设下证明安全性。

## 实验与结果

给出端到端原型实现，并与基于 DECO 的多会话复制基线对比：在高阈值规模下框架仍高效，仅引入适度额外开销，验证了面向智能合约环境的可联合验证 TLS 证明的可行性；用例包括 Aave 借款中基于收入证明的动态抵押（Bob 需与至少 t−1 个验证者合谋才能伪造证明）。

## 贡献与局限

- 贡献一：从“多验证者各跑独立会话”转向统一可导出的证明框架，证明方复杂度由 O(n) 降为 O(1)。
- 贡献二：形式化多验证者环境下的阈值证明不可伪造性，并在标准假设下给出安全证明。
- 局限：阈值规模较高时开销随参与者增长；工程原型仍需更广的智能合约/预言机生态与真实链上成本评估。

---

DOI: 10.1109/tdsc.2026.3716834
