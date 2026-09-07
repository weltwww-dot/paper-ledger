# Verifiable Encrypted Timed Signature Scheme and Its Application in Blockchains 总结

## 基本信息

- **标题**: Verifiable Encrypted Timed Signature Scheme and Its Application in Blockchains
- **作者**: Yuan Li, Junzuo Lai, Yi Liu, Liang Zhang, Haiyan Wang, Ke Ma, Jiheng Zhang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3715374
- **arXiv**: 无
- **PDF**: [TDSC_2026_VerifiableEncryptedTimedSignature.pdf](papers/TDSC_2026_VerifiableEncryptedTimedSignature.pdf)

## 一句话概括

本文提出可验证加密定时签名（VETS），把公开验证与基于时间的提取解耦，只有收到解锁密钥后才可顺序计算提取签名，并以“先发布后求解”的原子交换协议消除高性能硬件提前求解威胁、降低普通用户机会成本。

## 问题与动机

Verifiable Timed Signatures（VTS，CCS '20）允许求解者在开始顺序计算前验证定时签名中确含有效签名，并已用于脚本化受限区块链（如 Monero、Zcash）上的原子交换与支付通道。然而现有 VTS 方案中，求解者一收到定时签名即可开始求解；在原子交换场景里，拥有高性能硬件的恶意发起方可能比对手方预期更快解出定时签名并提前赎回资金，威胁对手方资产安全。增大时间参数 T 虽可缓解，却会延长普通用户的锁定时间，带来冻结资金、错过交易机会等不可忽视的机会成本。作者由此提出一个开放问题：能否设计一种定时签名原语，允许求解者验证被封装签名的有效性，但只有在预定条件满足后才启动耗时 T 的顺序计算以恢复签名。

## 方法

作者提出 VETS 原语：任何人都能验证定时签名内封装的是消息 m 在公钥 pk 下的有效签名，但无法仅凭顺序计算提取它，必须先在解锁密钥 UK（与链上事件或外部条件绑定）发布后，才能执行 VETS.ForceOp 进行求解。构造遵循一次性密码本思想，在 VTS 的 n 个时间锁谜题上额外加锁；为避免产生 n 个解锁密钥，利用 Shamir 秘密共享由单一 UK 派生各谜题密钥 {yi}（阈值 n/2+1，签名者在验证阶段已揭示其中 t 个份额，接收方获 UK 后可用拉格朗日插值重建其余份额）。方案以 ECDSA 实例化（亦兼容 BLS、Schnorr），包含 Setup/Commit/Verify/Open/ForceOp 五个算法，安全性依赖 LHTLP、仿真可靠 NIZK 与随机预言机 H′，并证明了 Soundness 与 Privacy 两个定理。在应用层，作者把 VETS 嵌入 UAS 框架（同样适用于 PipeSwap）设计原子交换协议，包含 Freeze、Swap、Refund、Punish 阶段，Alice 只有在链上观察到 Bob 的退款交易后才能提取 UK 并开始求解，且以截止时间 Tc 与惩罚交易抵御 Bob 无限期扣押退款交易的 grief 攻击。

## 实验与结果

实验平台为 AMD Ryzen 5 7500F（5 GHz）CPU 与 16 GB 内存。作者对比了 1024 位模平方延迟：VDF 竞赛中 FPGA 达到每平方 25.2 纳秒的最低延迟，而本平台用 GMP 库实测为 398 纳秒/次；据此，FPGA 上 1 小时可解的 VTS 谜题在本平台约需 15.8 小时，说明专用硬件与通用处理器差距显著（性能比 K≈15.8）。在机会成本方面，UAS 总锁定时间为 T_UAS = K·(Tb+Δ)，而 VETS 为 T_VETS = Tb + K·Δ，节省 (K−1)·Tb：以 Tb=24 小时计可节省约 355.2 小时有效锁定时长。计算开销方面，设置 n ∈ {20,30,40,50}、t=n/2、|N|=1024 位，Freeze 阶段双方各约 640 毫秒（主要来自定时签名与等值证明的生成验证），Swap 阶段每方不足 24 毫秒，表明方案对终端用户仅带来适度开销；协议原子性在 Universal Composability 框架下分析（正式 UC 证明见附录）。

## 贡献与局限

贡献包括：其一，提出 VETS 这一新密码原语，在可验证定时签名基础上加入条件激活，允许高效验证有效签名存在性、又阻止在获得解锁密钥前通过顺序计算提取签名；其二，设计了“先发布后求解”范式的原子交换协议，将顺序计算的起始与链上事件对齐，移除早期构造对计算能力的脆弱性，并降低普通用户机会成本；其三，对 VETS 方案与协议进行了安全分析（UC 框架）并给出性能评估。方案还兼容 UAS 与 PipeSwap，可拓展到无寿命限制的脚本化支付通道与匿名加密货币上的条件延迟支付。局限在于：后两类应用仅给出概念框架，完整协议构造与形式化安全分析留待未来工作；具体构造以 ECDSA 为主展示，且假设顺序求解天然串行、T≥Δ；性能实验也未覆盖不同网络参数与更大规模密钥下的全部开销。

---
DOI: 10.1109/tdsc.2026.3715374
