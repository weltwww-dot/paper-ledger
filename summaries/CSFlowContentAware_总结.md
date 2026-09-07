# CSFlow: A Content-Aware Secure Flow Control System for Encrypted Data Sharing in Cloud-Edge 总结

## 基本信息

- **标题**: CSFlow: A Content-Aware Secure Flow Control System for Encrypted Data Sharing in Cloud-Edge
- **作者**: Caiqun Shi, Qinlong Huang, Chao Wang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3714374
- **arXiv**: 无
- **PDF**: [TDSC_2026_CSFlowContentAware.pdf](papers/TDSC_2026_CSFlowContentAware.pdf)

## 一句话概括

提出内容感知的云边加密数据流控制系统 CSFlow，通过带细粒度发送方策略的跨域访问控制加密（CACE）同时约束"谁能与谁通信"和"能传什么内容"，防止授权发送方泄露敏感数据。

## 问题与动机

云-边（cloud-edge）计算被广泛用于跨域数据共享（如 GDPR 监管下医院与科研机构共享电子病历 EMR），但云服务商是半可信的。传统属性基加密（CP-ABE）能控制谁能解密，却无法阻止恶意发送方或中毒设备把数据加密给未经授权的接收者；基于访问控制加密（ACE）的流控制系统虽能在净化器（sanitizer）处过滤违规密文，但其访问控制策略与数据内容无关，导致"已被授权的发送方仍可能把超出授权范围的敏感内容发给合法接收者"。此外，现有 ACE 方案的解密密钥大小随授权属性数线性增长，解密需要 O(n) 次配对运算。因此需要一种在云边环境下同时支持细粒度发送方策略、无密钥净化（keyless sanitization）且开销合理的跨域 ACE 方案。

## 方法

作者提出 CSFlow，一种内容感知的安全流控制系统，系统含全局权威（GA）、发送方权威（SA）、接收方权威（RA）、监督者（supervisors）、发送方、边缘节点、云服务器与接收方八类实体：边缘节点作为净化器监控并净化所有发往云端的密文。为实例化 CSFlow，作者定义了新的原语 CACE——带细粒度发送方策略的跨域访问控制加密：每条消息被打上内容标签 ctag，发送方的加密密钥绑定"属性向量 ⃗v + 内容标签 stag"的细粒度策略，接收方解密密钥对应谓词向量 ⃗u；发送前需向至少 t+1 名监督者收集部分标签签名消息并组合成带时限的标签签名消息 msig。净化器验证 NIZKP 证明、EQS 签名与 TSIG 签名，确认密文的接收者与内容标签符合发送方策略（要求 stag = ctag）后才将其再随机化为净化密文；接收方在 ⟨⃗v, ⃗u⟩ = 0 时用 3 次配对即可解密。CACE 由可净化内积加密（SIPE）、BLS 门限签名（TSIG）、等价类签名（EQS）与 Schnorr NIZKP（配合 Fiat-Shamir 启发式）构造，并对选择性的 no-read 规则、no-write 规则与 soundness（发送方只能发送符合其细粒度策略的消息）给出形式化安全证明。

## 实验与结果

作者用 JPBC 框架与 BN254 曲线实现 CACE，并与最新方案 Sedaghat 的 LSSS CD-ABACE、Wang 的 ABACE 及 CD-IPACE 对比，在 Intel Core i7-9750H CPU、16 GB 内存设备上按边缘网络拓扑仿真，策略采用 FAME 式 "Attr1 AND Attr2 AND … AND Attrℓ" 形式，属性数 ℓ 从 2 到 20。结果显示：加密密钥生成虽随 ℓ 线性增长但 CACE 优于 CD-ABACE 与 ABACE（ℓ=20 时仅 0.23 s）；加密耗时 CACE 最佳，从 0.13 s 增至 0.31 s；净化阶段 ℓ=4 时 CACE 为 1.36 s，优于 CD-ABACE（1.60 s）与 ABACE（3.32 s），但略高于 CD-IPACE（0.32 s）；解密阶段 CACE 与 CD-IPACE 均只需 3 次配对（ℓ=20 时为 0.26 s），显著优于 ABACE 与 CD-ABACE（2.34 s）。存储方面，CACE 加密密钥从 0.56 KB 增至 1.69 KB，解密密钥为常量大小（ℓ=20 时 0.34 KB，与 CD-IPACE 相同，远小于 CD-ABACE 的 1.5 KB 与 ABACE 的 2.75 KB），净化后密文小于原始密文（ℓ=10 时原始 3.5 KB、净化后 1.13 KB）。门限 t 从 1 增至 9 时 SA 初始化仅从 108 ms 增至 116 ms，单个部分标签签名消息生成约 9 ms（0.89 KB），聚合时间从 9 ms 增至 36 ms。案例分析覆盖电子病历共享、电网用电数据上报与跨行可疑交易监测建模等场景。

## 贡献与局限

主要贡献：一是提出 CSFlow 系统并引入新原语 CACE（带细粒度发送方策略的跨域 ACE），由 SIPE、TSIG、EQS 与 NIZKP 给出完整构造，让净化器可基于内容标签与接收者属性实施内容感知净化；二是给出选择性 no-read、no-write 与 soundness 的形式化安全定义，并基于底层构件安全性完成系统安全分析；三是通过理论分析与实验表明 CACE 相比 CD-ABACE 与 ABACE 具有更高效的加密、净化与解密，同时相对 CD-IPACE 获得细粒度发送方策略而未显著增加计算与存储开销，面向云边跨域数据流控制具有实用性。

局限：安全结论依赖威胁模型假设（RA 与 SA 完全可信、边缘节点半可信但不合谋、云服务器半可信、对手最多腐化 t 名监督者）；发送方每次发消息都需联系至少 t+1 名监督者获取标签签名消息，且该消息带时限（|time − time0| ≤ expiry），重复发送需重新申请，带来额外交互与延迟；性能评估基于单机仿真与合成策略，未在真实大规模多域部署上验证；内容标签的认定依赖监督者事先审核，系统需额外引入监督治理角色。

---
DOI: 10.1109/tdsc.2026.3714374
