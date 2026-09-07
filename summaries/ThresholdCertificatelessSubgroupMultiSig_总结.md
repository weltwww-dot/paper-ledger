# Threshold Secure Certificateless Subgroup Multi-Signature for Anonymously Consensus Mechanisms 总结

## 基本信息

- **标题**: Threshold Secure Certificateless Subgroup Multi-Signature for Anonymously Consensus Mechanisms
- **作者**: Zhiwei Wang, Siuming Yiu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3715447
- **arXiv**: 无
- **PDF**: [TDSC_2026_ThresholdCertificatelessSubgroupMultiSig.pdf](papers/TDSC_2026_ThresholdCertificatelessSubgroupMultiSig.pdf)

## 一句话概括

面向匿名共识机制提出一种基于 Bulletproofs 内积论证与 Univariate SumCheck 的无证书子群多重签名方案，在免去分布式密钥生成（DKG）的同时实现签名者匿名与门限人数证明。

## 问题与动机

在 IoT 与区块链等共识场景中，常需多个用户/矿工对同一消息共同签名，多重签名是合适原语，但传统 PKI 方案要求证书签发与验证、开销大；基于身份（IBC）方案存在密钥托管问题（恶意 KGC 可推导全部私钥）。无证书密码体制虽同时缓解证书管理与密钥托管，却缺少 CA 类可信中心来约束公钥注册，因而易受 rogue-key 攻击。此外，共识常需任意子群代替整体签名（存在 Byzantine 用户时），而传统阈值签名依赖 DKG 协议：需要可信第三方、阈值改变时必须重跑，在无证书设定下因需分发两把秘密钥而要执行两次，动态环境代价高昂。作者希望构造一个无证书子群多重签名，使参与签名者身份对验证者匿名、任意规模超过阈值的子群都能生成合法签名，且无需 DKG。

## 方法

方案基于 BLS 签名与 Sakai 的基于身份签名，包含 Setup、KeyGen、Extract、PSign、PVerify、Combine、KeyAgg、Verimul 八个概率多项式时间算法。将参与者的公钥、身份哈希与选择向量表示成向量，把聚合公钥表达为向量内积，并采用 Bulletproofs 简化版内积论证在验证时隐匿各参与者的公钥与身份；签名者预计算辅助值供聚合者本地执行内积论证，无需额外在线交互。用比特向量 d 经 ⟨d, d⟩ 计子群规模，并借用 Univariate SumCheck 引理（构造多项式 d(x) 及 qd、rd，仅需三个群元素与两条配对方程）向验证者证明子群规模 ≥ 门限 t′ 而不泄露成员身份。抵御 rogue-key 攻击选用基于哈希的第二种方法：将 ai = H2(IDi, pki, pk, ID) 作为标量参与聚合，使各签名贡献绑定到当前签名者全集。安全性通过两个游戏刻画：A1 为可替换任意公钥的恶意用户，A2 为掌握主私钥 msk 的恶意 KGC，并证明内积论证满足完美完备性与计算知识可靠性、方案在随机谕言模型下基于 CDH 假设与 BLS 不可伪造性不可伪造。

## 实验与结果

在 128 位安全强度、配对友好曲线（如 BLS12-381、|G|=48 字节）、n=512、阈值 t=256 的参数下做理论对比：相对阈值签名方案（如 FROST/Chelsea、Groth 的 SNARK 方案、Das 等的内积论证方案），主要优势为无需 DKG、改阈值无附加开销。通信量上，Galindo 等子群多重签名需 O(n) 即 512×48=24 KB 公钥列表，本方案 Full 版仅需 O(log n)=9 个群元素的内积论证加 3|G| 的 SumCheck 证明，合计约 12×48=576 字节，缩减 40 倍以上；验证端约 9 次指数运算加常数次配对。实现采用 Java 与 JPBC 库，平台为联想拯救者 R9000P（AMD Ryzen 7 6800H 3.20 GHz、16 GB 内存）：生成单个部分签名约 86 ms；聚合公钥耗时随签名者数量近线性增长，少于 500 名参与者时仅需数秒。与 Galindo 方案及 Kojima 等方案对比，密钥聚合开销同一量级；当参与者较多（n>100）时本方案总验证时间低于 Galindo 方案，n=1024 时证明规模仍保持对数增长，适合验证节点资源受限的大规模共识。

## 贡献与局限

主要贡献：(1) 基于 Bulletproofs 为无证书子群多重签名的聚合公钥设计了内积论证，并给出完美完备性与计算知识可靠性的严格证明；(2) 构造了同时实现签名者匿名与子群规模超过门限保证的无证书子群多重签名，用 Univariate SumCheck 完成门限比较，给出完整的不可伪造性证明；(3) 对方案进行系统性能评测并与相关方案对比，展示其在实际共识场景的可行性与效率。局限：签名阶段聚合者须从所有参与签名者收集辅助值，带来协调开销；SumCheck 证明依赖双线性配对，比普通群运算昂贵；动态成员变化需周期性重初始化系统参数；支持不同投票权重的加权门限仍是开放问题。

---
DOI: 10.1109/tdsc.2026.3715447
