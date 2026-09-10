# Identity-Based Encryption With Equality Test and Flexible Time-Based Authorization for Cloud Computing 总结

## 基本信息

- **标题**: Identity-Based Encryption With Equality Test and Flexible Time-Based Authorization for Cloud Computing
- **作者**: Cong Li, Xinyu Feng, Qingni Shen, Zhonghai Wu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3702092
- **arXiv**: 无
- **PDF**: [TDSC_2026_IdentityEncryptionEqualityTest.pdf](papers/TDSC_2026_IdentityEncryptionEqualityTest.pdf)

## 一句话概括

本文提出 IBEET-FTBA，在身份基加密相等性测试中用带通配符的时间模式向量表达多个授权时间段，并在标准模型下证明安全，从而减少多时间段授权所需的陷门数量。

## 问题与动机

身份基加密相等性测试允许云服务器判断不同身份下的两个密文是否加密了同一消息，但把陷门交给服务器后，用户通常无法继续控制其有效范围。已有 IBEET-DBA 只能表达单个连续时间段、授权类型局限于年/月/日，并且安全性建立在随机预言机模型上；例如授权服务器检查 2024 年每月 7 日的数据时，需要生成 12 个陷门。作者希望同时支持多个时间段、任意或自定义时间粒度，并在不依赖随机预言机的标准模型中给出安全方案。

## 方法

作者用层次化时间区间树组织标准和自定义时间段，把密文的创建时间编码为时间向量，把带通配符的模式向量嵌入陷门，从而用一个模式表达多个匹配时间。方案包括 Setup、KeyGen、Trapdoor、Encrypt、Test 和 Decrypt 算法：相等性测试先检查身份和时间模式是否匹配，再通过双线性配对恢复可比较的消息相关值。安全性方面，方案在截断决策 q-ABDHE 假设下，对持有测试陷门的 Type-I 敌手证明 OW-ID-CCA2 安全，对不持有陷门的 Type-II 敌手证明 IND-ID-CCA2 安全，且不调用随机预言机。论文还给出支持多个模式向量集合的扩展，以表达跨年份的复杂时间区间。

## 实验与结果

理论分析显示，在 12 个时间段的场景中，IBEET-DBA 需要调用 12 次陷门生成，而 IBEET-FTBA 只需一次；相较 IBEET-DBA，陷门生成阶段少 50 次 G 中指数运算，陷门存储开销约降低 85.42%，计算开销约降低 83.33%。实验使用 jPBC 2.0.0，在 AMD Ryzen 7 8845HS、32 GB 内存、Windows 11 和 JDK 21.0.8 环境下重复 200 次取平均，并比较 Type A 与 Type D 双线性配对。单时间段时，IBEET-DBA 的陷门生成更快；当时间段数大于 2 时，IBEET-FTBA 更高效，例如时间段数为 5 时速度超过 IBEET-DBA 的两倍。随着时间树深度、时间向量或模式向量长度增加，Setup、Trapdoor、Encrypt 和部分 Test 的执行时间总体近似线性增长；时间树深度为 50 时，Type A/Type D 的 Setup 约为 374.86/1161.27 ms。

## 贡献与局限

本文把通配符、多时间段授权和标准模型安全性同时引入 IBEET，既减少重复陷门，又允许分钟、秒、毫秒或自定义时间区间等更细粒度授权，并通过理论与实现对比验证了多时间段场景的优势。局限在于支持灵活时间表达会增加公开参数、加密和解密成本；实验基于 JPBC 和桌面环境，尚未验证大规模云服务部署。作者后续计划限制陷门生命周期、降低陷门与加密算法的计算和参数开销，并探索格基 IBEET-FTBA 方案。

---
DOI: 10.1109/TDSC.2026.3702092
