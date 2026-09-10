# HQT-TI: An Efficient Hilbert Curve Based Index for Spatial Keyword Queries 总结

## 基本信息

- **标题**: HQT-TI: An Efficient Hilbert Curve Based Index for Spatial Keyword Queries
- **作者**: Lianyin Jia, Yongwang Miao, Suprio Ray, Jiaman Ding, Xiaodong Fu, Xiuxing Li
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-06-02
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/TKDE.2026.3699763
- **arXiv**: 无
- **PDF**: [TKDE_2026_HQTTIEfficientHilbert.pdf](papers/TKDE_2026_HQTTIEfficientHilbert.pdf)

## 一句话概括

本文提出 HQT-TI 空间—文本索引及 HS-SKQ 查询算法，以 Hilbert 曲线结合 Quadtree 处理空间范围，以 Trie 和倒排索引处理关键词，从而减少候选对象与列表交集成本。

## 问题与动机

空间关键词查询要求同时满足空间范围和关键词条件。既有 SFC-Quad 等方法通常使用 Z-order 和粗粒度 ID 范围，忽略关键词分布偏斜，容易返回大量不相关 ID；R-tree、Quadtree 与文本倒排结构的简单组合也会增加交集和 I/O 代价。作者希望利用 Hilbert 曲线更好的空间邻近性，并让查询深度和高频词索引适应数据分布。

## 方法

HQT 将 Hilbert 曲线与 Quadtree 建立直接对应关系，使空间节点映射为更紧凑的 ID 区间。HQT-SQ 从包含查询框的节点开始向下钻取，并采用深度优先与有限宽度扩展，减少重叠检查和无关对象。TI 将 Trie 与倒排列表结合，对高频词物化列表并保留非高频词列表；SLI-KQ 按多个不相交 ID 段进行交集，尽量先处理短列表。HQT-SQ 与 SLI-KQ 共同形成 HS-SKQ。

## 实验与结果

实验在 Windows 11、Intel i7-14650HX 5.2 GHz、48 GB RAM 上进行，使用 DS1（KGPOI+BMS）、DS2（ROAD+KOSARAK）和 Foursquare 的 DS3；对比 IF-R*、WIR-Tree、IR-Tree、CIR-Tree、SFC-Quad、ARM-SQ、LSTI 和 WISK。每组生成 1000 个查询并重复 5 次取平均。HS-SKQ 相对无钻取版本最高提升 1.06×，相对最优固定深度最高提升 36.9%；在高频关键词数 X=10 时，相对 SFC-Quad 最高提升 139.46×，相对 ARM-SQ 提升 5.46×。在 DS3、X=6 时，其 #AID 仅为 SFC-Quad/ARM-SQ 的 28.4%，#AIO 分别为 4.3% 和 31.7%。

## 贡献与局限

贡献是：把 Hilbert 曲线、Quadtree 和 Trie-倒排索引统一为 HQT-TI，并通过自适应钻取与分段交集降低查询代价；在三种真实空间—文本数据上验证了对关键词偏斜和查询范围变化的效率优势。局限是钻取会增加空间查询成本，索引还需额外存储物化倒排列表；作者指出未来应进一步处理空间偏斜，并扩展到时空关键词查询。

---
DOI: 10.1109/TKDE.2026.3699763
