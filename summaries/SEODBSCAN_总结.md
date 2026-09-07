# SEO-DBSCAN: Securely and Efficiently Outsourcing Density-Based Clustering 总结

## 基本信息

- **标题**: SEO-DBSCAN: Securely and Efficiently Outsourcing Density-Based Clustering
- **作者**: Ke Cheng, Xinghui Zhu, Jiaxuan Fu, Zhiwei Zhang, Jian Yang, Aijing Sun, Haichang Gao, Yulong Shen
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3711460
- **arXiv**: 无
- **PDF**: [TDSC_2026_SEODBSCAN.pdf](papers/TDSC_2026_SEODBSCAN.pdf)

## 一句话概括

本文提出 SEO-DBSCAN，一种基于双云不共谋架构、由常数轮安全比较协议与密码友好型 DBSCAN 变体构成的密文外包密度聚类框架，在达到与明文一致的聚类质量的同时实现全隐私与近二次方的高效扩展。

## 问题与动机

将 DBSCAN 等聚类任务外包给云平台虽能缓解计算与存储压力，但云服务器并非完全可信，且聚类常涉及多方敏感数据。已有安全外包聚类研究多集中于 K-means，无法处理非凸簇与噪声；而现有安全 DBSCAN 方案仍会泄露簇分配、簇大小等敏感统计信息。首个全隐私外包 DBSCAN 方案 ppDBSCAN 基于 ABY 框架，复杂度高达 O(N³)，对 5000 个二维点需运行一周以上且需预设迭代上界；PPA-DBSCAN 靠 ρ-近似牺牲精度且依赖昂贵的安全集合运算；FSS-DBSCAN 虽降低在线轮数，但函数秘密共享密钥生成与分发带来高昂的端到端设置开销。此外，安全比较是 DBSCAN 的基础构件，现有方案要么计算代价高、要么轮数复杂度过高（如 FSS-DBSCAN 每次比较需 5 轮交互），而 DBSCAN 本身迭代、数据依赖的执行路径若不加以数据无关化改造也会泄露访问模式。

## 方法

SEO-DBSCAN 采用两个不共谋云服务器 S0、S1 的架构：各数据所有者将数据做 2-out-of-2 算术秘密共享后分别上传，随后的计算全由两服务器在秘密共享态上协作完成，数据所有者上传后即可离线。密码层上，作者设计了常数轮安全比较协议 SecureCompare（4 轮通信、与输入位长无关），其由 BinaryStringEqual、PlainLessThan（基于 0-encoding/1-encoding 将小于问题化为并行相等测试）与 ComputeLSB（检测模回绕并提取 LSB）三个通用子协议构成，并利用奇域上 MSB(a)=LSB(2a) 的性质把 MSB 比较转化为 LSB 提取，避免位分解与进位传播。算法层上，作者提出密码友好型 DBSCAN：用固定 N 轮双层循环替代依赖队列的明文 DBSCAN，引入 C1、C2 秘密谓词把条件分支转为数据无关的算术迭代，CurrentClusterID 全程以秘密共享形式确定性递增，使可观测执行轨迹与数据无关，保证不泄露簇数目与大小等中间信息；邻域查询并行化计算平方欧氏距离并与 ϵ² 比较。整体服务器间复杂度为 O(N²)。

## 实验与结果

系统用 Python 3.12 与基于 PyTorch 的轻量安全多方计算库 NssMPClib 实现，Zp 模数为 32 位奇素数，测试环境为两台 Ubuntu 20.04 服务器（3.7 GHz Intel Core i9-10900K、128 GB RAM、RTX 3090），LAN 往返时延 0.22 ms、10 Gbps 带宽。真实数据集含 Lsun（400 点 3 簇）、zelnik5（511 点 5 簇）、Longsquare（900 点 6 簇）与 S1（5000 点 15 簇）。聚类质量上，以 V-measure、ARI、AMI 为指标，SEO-DBSCAN 在 Lsun、zelnik5、Longsquare 上与明文 DBSCAN 及 FSS-DBSCAN 得分完全相同，优于 K-means 与 Affinity Propagation。效率上，2 万个二维点的秘密共享约 10 ms；CPU 下 2 万点总耗时约 254,376 秒（SOC 阶段占大头），GPU 下降至 79,343 秒（约 3.2× 加速），总通信量达 10.8 TB（SOC 约占 6.7 TB）。与 ppDBSCAN 相比，1000 点时提速 8.65×（675 s vs 5839.50 s）、800 点时 7.23×，通信由 438 GB 降至 5.24 GB（约 83.7× 缩减）。真实数据集上 CPU 运行时分别为 Lsun 125 s、zelnik5 189 s、Longsquare 543 s、S1 16,233 s，而 ppDBSCAN 在 S1 上超过 620,000 秒不可实用；S1 上通信量比 FSS-DBSCAN 减少逾 30%，并在 CPU/GPU 运行时与通信上全面优于 FSS-DBSCAN 与 PPA-DBSCAN。

## 贡献与局限

- **贡献**：提出一组面向并行计算优化的轻量密码学原语与基于算术秘密共享的常数轮安全两方比较协议（4 轮，独立于输入位长），可作为通用构件用于更广泛的安全计算；设计密码友好型 DBSCAN 变体，使外包聚类达到与明文一致的聚类质量、完整隐私（半诚实模型下仅泄露最终输出，采用模拟器与 Canetti 组合定理证明）与 O(N²) 的实践可行复杂度；实现系统原型并在合成与真实数据集上验证了相对 ppDBSCAN 最高 8.65× 计算加速、83.7× 通信缩减，以及相对 FSS-DBSCAN、PPA-DBSCAN 的全面性能优势。
- **局限**：协议基于双云不共谋与半诚实敌手假设，难以直接抵御恶意云或共谋场景；算法需固定执行 N 轮外层迭代且采用全量两两距离比较，通信量仍呈二次增长（2 万点已达 TB 级），在更大规模数据或低带宽广域网场景下开销仍然可观。

---
DOI: 10.1109/tdsc.2026.3711460
