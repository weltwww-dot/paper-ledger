# Traceable Registered Functional Encryption for Unbounded Inner Product in Web Service Platforms 总结

## 基本信息

- **标题**: Traceable Registered Functional Encryption for Unbounded Inner Product in Web Service Platforms
- **作者**: Jinmei Tian, Jianting Ning, Jian Shen, Kai Zhang, Weijing You, Lefeng Zhang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3716326
- **arXiv**: 无
- **PDF**: [TDSC_2026_TraceableRegisteredUIPFE.pdf](papers/TDSC_2026_TraceableRegisteredUIPFE.pdf)

## 一句话概括

面向 Web 服务平台，提出无需混淆电路即可支持无界内积计算并可公开黑盒追踪泄密者的可追踪注册函数加密方案 TRFE-UIP。

## 问题与动机

Web 服务平台（在线医疗、精准营销、社交网络等）的相似度检索、推荐与付费查询等核心服务依赖高维用户数据的内积运算，但平台服务器通常并非完全可信，可能非法解析甚至泄露敏感数据。函数加密（FE）允许在密文上直接计算而不知明文，却受限于预设向量维数、依赖不可区分混淆（iO），且普遍缺少对恶意共享功能密钥用户的问责机制；传统 FE 还依赖单一可信机构（TA），存在密钥托管（key escrow）风险。现有注册函数加密（RFE）虽引入无秘密的密钥策展人（KC）缓解托管问题，但已有方案要么依赖 iO 等黑盒原语、只支持固定维度，要么只达到 IND 安全性且缺乏可追踪性，难以同时满足无界内积计算与泄密用户精确追踪。

## 方法

论文提出可追踪注册函数加密框架 TRFE-UIP：客户端本地生成公私钥对，通过透明的密钥策展人（KC）注册，KC 只聚合公钥、发布主公钥 mpk 与辅助解密密钥 hsk，不掌握任何秘密信息；系统实体包括 CRS 生成器、KC、数据拥有者/数据使用者、半诚实的 Web 服务器及中央追踪权威（CTA）。技术上，采用向量切分把任意长度向量拆为单元素子向量并施加随机填充，利用正交条件自动消除无效位，从而在无需 iO 的条件下实现无界内积；注册时为每个用户分配唯一标签 qi，将其嵌入注册函数向量并存入公开目录 pd，追踪时 CTA 构造面向不同用户子集的区分性密文，通过黑盒测试观察解码器行为差异定位恶意用户（traitor），被追踪者由 KC 撤销并加入撤销列表 R。构造基于双线性配对与线性空间 QA-NIZK，包含 Setup、KeyGen、IsValid、Aggr、Enc、TraceD、Dec 算法。

## 实验与结果

方案在 (k,ℓ,d)-MDDH 假设的标准模型下被证明满足 Sel∗-SIM（very selective simulation-based）安全与公开黑盒可追踪性，且无需 iO。实验在 Intel Core i5-4210U @1.7 GHz、2 GB RAM、Ubuntu 64 环境下用 C 语言与 MIRACL 实现，采用嵌入次数 12 的 Type F 曲线、256 位素数阶，对比 [TT18]、[YG24]、[ZL24]、[DP20]、[QH24]、[BL24] 六种方案（统一安全级别、λ=256、L=100、n=100、μ(λ)=0.05，每项独立运行 100 次取均值）。结果表明：Ours-1 的 Setup 计算开销约 5408.6 ms（优于 [ZL24]，高于 [TT18] 与 [YG24]），单次 KeyGen 约 1077.2n+1309.919 ms，加密约 98.6L+394.4 ms，解密开销为 7nTp；当消息维数 n 与注册客户端数 L 均达 100 时，总通信开销与 n、L 近线性增长，消除了对 L 的高阶耦合项（如 [DP20] 中的 (n−1)|GT|、(n+1)L|GT| 主导项）；总计算开销较当前主流方案 [ZL24] 降低约 96.4%，且在高维场景下优于同类方案。

## 贡献与局限

- 首次将无界内积计算、注册式密钥管理与公开黑盒追踪原生集于一体，是首个无需 iO 即可同时实现上述三者的 TRFE-UIP 方案。
- 系统形式化 TRFE-UIP 的定义框架、Sel∗-SIM 安全与公开黑盒追踪的安全模型；利用槽位索引匿名真实用户身份，兼顾可追踪性与用户隐私。
- 通信与计算开销随 n、L 近线性增长，实测总计算成本比主流方案低 96.4%，适合大规模用户与高维向量的 Web 场景。
- 局限：仅达到选择性（Sel∗-SIM）而非自适应安全；CRS 生成器与 KC 被假定为可信（一次性初始化可信），解密需在消息空间有界约束下经暴力/BSGS 恢复离散对数。未来工作拟构造分布式 CRS 生成与去中心化 KC 治理，并实现自适应 SIM 安全的 RFE。

---
DOI: 10.1109/tdsc.2026.3716326
