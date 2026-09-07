# Accountable-Authority Identity-Based Matchmaking Encryption and Its Application 总结

## 基本信息

- **标题**: Accountable-Authority Identity-Based Matchmaking Encryption and Its Application
- **作者**: Axin Wu, Weiqi Luo, Anjia Yang, Yinghui Zhang, Yuer Yang, Feixiang Zhao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3714500
- **arXiv**: 无
- **PDF**: [TDSC_2026_AccountableAuthorityIBME.pdf](papers/TDSC_2026_AccountableAuthorityIBME.pdf)

## 一句话概括

本文首次提出可问责权威的身份基匹配加密（A-IB-ME）概念并给出基于静态假设、无需随机预言机的具体构造，在保留双边访问控制、消息认证与身份隐私的同时缓解密钥托管问题并对密钥滥用实现可追溯问责。

## 问题与动机

身份基匹配加密（IB-ME）是匹配加密（ME，Ateniese 等人在 CRYPTO 2019 提出）在身份基设定下的实例化，能同时提供身份隐私、双边访问控制以及消息的机密性与真实性，但因权威可以为任意身份生成加密密钥与解密密钥，存在固有的密钥托管（key escrow）问题，且在密钥被滥用时缺乏责任界定能力：当发现用户 Alice 的 encipher box 或 Bob 的 decoder box 被恶意传播时，由于用户与权威都有生成能力，现有 IB-ME 无法判定责任方。减少对权威信任的朴素思路（多权威方案、现有 A-IBE 方案）代价高昂且难以直接扩展：A-IBE 需要对密文做健全性检查导致匿名性丢失，且只考虑接收方相关的恶意行为，而 A-IB-ME 需要同时覆盖发送方相关与接收方相关的权威恶意行为。作者据此提出需要新的语法与安全模型来刻画这些行为。

## 方法

作者定义了 A-IB-ME 的正式语法，在 IB-ME 基础上加入密钥格式健全性检查（EKeySanity/DKeySanity）与追踪算法（Trace1 判定 encipher box 来源为发送方或权威，Trace2 判定 decoder box 来源为接收方或权威）。技术上借鉴 A-IBE [5]：为发送方与接收方分配与身份无关的虚拟属性集作为私有输入，通过完全可模拟的 k-out-of-n 不经意传输（OT）协议与权威交互获取加密/解密密钥；主密钥 β 用随机 d−1 次多项式共享，权威不知道用户实际获得哪 k 个分量，因而无法冒充用户生成可用的 encipher/decoder box。为不泄露身份隐私，作者采用 splitting 技术（[19]）改造解密密钥与对应密文分量，使敌手无法仅凭公钥与密文测试出接收方身份；消息真实性通过把秘密值嵌入密文分量 C、接收方仅在正确解密后才能确认认证来实现。构造还包含 Setup、交互式 EKGen/DKGen、Enc、Dec 等算法，正确性要求满足 d 阈值交集条件。

## 实验与结果

安全上，作者将 A-IBE 的安全模型扩展至 A-IB-ME 场景，形式化定义了隐私、真实性、不诚实发送方安全、不诚实接收方安全与不诚实权威安全五种性质，Theorem 1 表明在 DBDH、D-Lin、CBDH 假设下 A-IB-ME 语义安全（证明见在线附录），且无需随机预言机，不依赖非交互零知识证明等额外工具。性能上，作者在 Windows 10 Pro 21H2、11 代 Intel Core i7-11800H 2.30 GHz 8 核、24 GB RAM 平台上基于 JPBC 2.0.0 默认 Type A 椭圆曲线实现（p 为 160 位、G 阶 512 位，每阶段 20 次平均），OT 用 [40] 的协议实例化，代码公开于 GitHub（SchemeAAIBME）。实验（Fig.1）显示：密钥生成开销随虚拟属性 n、k 增加而上升且 n 影响更大；加密解密开销随 k 与多项式次数 d 增加，k 的影响大于 d（k 主要增加加密中的指数运算、d 主要增加解密中的双线性配对）；密钥健全性检查与各组件存储开销均与 k 线性相关。与 A-IBE、IB-ME 相比，A-IB-ME 计算与存储开销略高但处于同一数量级，以适度开销换取更丰富的功能。

## 贡献与局限

贡献主要有三点：一是首次提出 A-IB-ME 概念并给出完整语法与安全定义，削弱对权威的信任、缓解密钥托管并实现恶意行为问责；二是给出具体构造，在 DBDH、D-Lin、CBDH 等静态假设下（无需随机预言机）证明隐私、真实性、不诚实发送方/接收方/权威安全；三是理论结合实验评估性能，并以移动社交网络中的隐私保护用户匹配为实例（匿名公告板上的六步流程）说明其应用价值，问责机制可通过 Trace1/Trace2 追查 encipher box 与 decoder box 的制造者。局限方面：较 IB-ME 与 A-IBE 增加的计算与存储开销源于更丰富的功能与更强的安全目标（如身份隐私与消息认证），是合理的折中；方案需要交互式 k-out-of-n OT 密钥颁发流程，实际效率依赖 OT 实例化选择；作者在结语中指出未来工作将考虑更高效的追踪算法。

---
DOI: 10.1109/tdsc.2026.3714500
