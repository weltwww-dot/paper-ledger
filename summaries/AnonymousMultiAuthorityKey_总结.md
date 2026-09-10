# An Anonymous Multi-Authority Key-Policy Attribute-Based Encryption Scheme With Expressive Keyword Search 总结

## 基本信息

- **标题**：An Anonymous Multi-Authority Key-Policy Attribute-Based Encryption Scheme With Expressive Keyword Search
- **作者**：Chenbin Zhao，Xiaocong Lin，Jing Chen，Weijing You，Jie Cui，Zhongyun Hua
- **期刊 / 年份**：IEEE Transactions on Dependable and Secure Computing，2026
- **研究方向**：属性基加密、可搜索加密、隐私保护
- **DOI**:10.1109/tdsc.2026.3699384
- **PDF**：[TDSC_2026_AnonymousMultiAuthorityKey.pdf](papers/TDSC_2026_AnonymousMultiAuthorityKey.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文先提出具有策略隐藏能力的匿名多授权机构 key-policy attribute-based encryption（MA-KPABE），再将其扩展为支持表达式多关键词检索的 MA-ASE，在分散密钥管理的同时隐藏用户属性、访问策略和搜索关键词相关信息。

## 问题与动机

现有 attribute-based searchable encryption 往往依赖单一可信机构，造成密钥管理的集中负担和单点信任；许多方案还在密文或搜索令牌中暴露属性、访问结构或策略，可能泄露用户意图并支持推断攻击。论文因此希望在多授权机构架构中同时实现细粒度访问控制、属性/策略隐私和表达式关键词搜索。

## 方法

MA-KPABE 将访问策略嵌入用户密钥但隐藏其敏感信息，并用 partially hidden structures 隐藏密文中的属性值，仅公开用于匹配的名称；多个独立 attribute authorities 分别生成参数和密钥，避免单一中心。基于该基础，MA-ASE 将多关键词、AND/OR 等表达式策略与 trapdoor/search 机制结合，在不向云服务器暴露完整属性、策略或关键词的情况下完成检索。作者在标准密码学模型中分别证明 IND-CPA、匿名性和 MA-ASE 的 IND-CKA 安全性。

## 实验与结果

实现基于 Charm 0.5、Python 3.6 和 MNT224 配对曲线，并与 A-KP-ABE、XHM、YLX 及 FEASE 比较。9 个属性机构执行 AASetup 时，MA-KPABE 用时 0.28 s，XHM 为 1.15 s；100 个属性的 KeyGen 为 0.32 s，100 属性加密为 0.21 s，而 XHM/YLX 分别为 1.00/1.47 s。100 属性的 AND 解密为 0.05 s，仅比 A-KP-ABE 增加 0.02 s；MA-ASE 对 100 个关键词的 TrapGen 和 Search 分别为 0.35 s 和 0.05 s，且分布式设计降低了单个机构的计算负担。多授权带来的额外 G2 元素随机构数线性增加，但论文认为在机构数较少时开销可接受。

## 贡献与局限

论文把匿名、策略/属性隐藏、多授权 KP-ABE 与表达式关键词搜索统一到一个构造中，并给出相应安全证明和与代表性方案的存储、计算比较。主要代价是多授权结构引入随机构数 k 增长的 G2 存储和指数运算；在仅 OR 的访问结构下，解密时间会随匹配属性增加，论文报告其相对部分对比方案存在额外延迟。实验基于 MNT224 和仿真环境，结论仍需在不同配对曲线及更复杂机构配置下进一步验证。
