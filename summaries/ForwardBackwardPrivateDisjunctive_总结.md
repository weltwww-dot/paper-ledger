# Forward and Backward Private Disjunctive Dynamic Searchable Symmetric Encryption With Leakage Suppression 总结

## 基本信息

- **标题**: Forward and Backward Private Disjunctive Dynamic Searchable Symmetric Encryption With Leakage Suppression
- **作者**: Xiaojun Zhang, Lei Xu, Xingliang Yuan, Yifeng Zheng, Lin Mei, Chungen Xu
- **期刊 / 年份**: IEEE Transactions on Dependable and Secure Computing, 2026
- **研究方向**: 可搜索对称加密、动态加密检索、前向/后向隐私、泄露抑制
- **DOI**: 10.1109/TDSC.2026.3698827
- **PDF**: [TDSC_2026_ForwardBackwardPrivateDisjunctive.pdf](papers/TDSC_2026_ForwardBackwardPrivateDisjunctive.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文形式化了带动态更新的析取可搜索对称加密安全模型，提出 D2SSE：以 TWINSSE 的元关键词转换为基础，结合对称子集谓词加密、增量可穿孔加密、CPRF 和 XorFilter，同时实现前向隐私、Type III 后向隐私并抑制关键词对结果模式泄露。

## 问题与动机

析取动态可搜索对称加密（DDSSE）允许在加密数据上查询多个关键词的并集，但既有方案存在通信开销高、更新/查询泄露多、缺少后向隐私等问题。将静态 TWINSSE 直接替换为动态合取 SSE 还会造成共享元关键词下的错误删除、由每次更新元关键词数量暴露的更新量模式，以及元关键词对结果模式（Meta-KPRP）泄露。论文因此重新定义析取查询场景下的泄露，包括单个查询内的关键词交集、多个查询间的查询重叠模式，以及不把更新时间关联到具体关键词的后向隐私要求。

## 方法

D2SSE 将关键词空间分桶，并用 TWINSSE 的元关键词把析取查询变为合取元关键词查询。为避免共享元关键词造成错误删除，更新条目绑定“关键词||文档标识符”；为隐藏不同关键词对应的元关键词数量，使用预定义元关键词集合将每次更新填充到桶内最大容量。系统维护 EDBT（带唯一标签的加密文档）、EDBD（删除文档的可穿孔标签和密钥）、EDBX（元关键词共现的私密子集检查）及搜索缓存。

新增文档时，D2SSE 使用 CPRF、哈希、对称加密和增量可穿孔加密写入条目；删除时对对应标签穿孔，使后续查询无法恢复被删文档。查询时，客户端生成元关键词查询、CPRF 约束密钥和 S2PE 子集密钥，服务器检索最不频繁的元关键词候选，过滤删除条目，再在不揭示具体集合元素的情况下检查其他元关键词是否共现。安全证明在 PRF、CPRF、随机预言机、IND-CPA 对称加密、IND-PUN-CPA 可穿孔加密及选择性安全 S2PE 假设下，通过混合游戏证明自适应前向和后向隐私。

## 实验与结果

作者用 C++ 实现 D2SSE、DIEX 和朴素方案 TWINODXT，在 Enron Email 与 Wikimedia 数据库上评估，密码组件包括 AES-256-CBC、BLAKE2b、HMAC-BLAKE2b 和假阳性率 10^-6 的 XorFilter；后续实验采用桶大小 n=8。更新方面，D2SSE 时间约为 DIEX 的 1.8 倍、TWINODXT 的 1.6 倍，但在数据规模达到 10^6 时单次更新延迟仍为 29 ms。

查询长度为 25 时，D2SSE 相比 TWINODXT 最多快 13 倍，并在该长度上相对 DIEX 的搜索延迟约为 0.25 倍；客户端存储在 10^6 规模时约为 DIEX 的 0.06 倍，但服务器端在交集稀疏的 Enron 上约为 DIEX 的 7.2 倍，在交集更密集的 Wikimedia 上接近 DIEX。查询令牌长度在查询长度 25 时约为 DIEX 的 0.8 倍、TWINODXT 的 0.7 倍；D2SSE 返回的无关文档与相关文档比例在两数据集上均低于 12%。这些开销换取了隐藏 Meta-KPRP 和同时提供前向/后向隐私；DIEX 虽无无关结果，但不提供后向隐私且泄露 KPRP。

## 贡献与局限

论文的主要贡献是面向析取动态查询完善安全模型，给出能消除错误删除、更新量模式和 Meta-KPRP 泄露的 D2SSE 构造，并通过理论证明和真实数据实验验证其正确性、隐私和搜索可扩展性。局限主要体现为安全—效率—存储的权衡：S2PE/XorFilter 与可穿孔密钥带来更高的更新和服务器存储成本，TWINSSE 转换仍可能返回无关文档，且实验中无关/相关比率低于 12% 而非为零。安全结论依赖所列密码原语和模型假设，全文未报告更强后向隐私类型、恶意服务器正确性验证或更广泛部署环境下的测量。
