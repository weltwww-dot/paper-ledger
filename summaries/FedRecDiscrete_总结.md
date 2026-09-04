# Towards Efficient Federated Recommendation with Discrete Graph Convolutional Network 总结

## 基本信息

- **标题**: Towards Efficient Federated Recommendation with Discrete Graph Convolutional Network
- **作者**: Yang Li, Weike Pan, Qiang Yang, Zhong Ming
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104607
- **PDF**: [AIJ_2026_FedRec.pdf](papers/AIJ_2026_FedRec.pdf)

## 一句话概括

提出 FedHashRec：把哈希（离散表示）引入联邦图卷积推荐，用三重保护框架（TriPro）在服务端构造“假全局图”，让每个用户只持有自己的子图也能协同训练，在保护隐私的同时显著降低通信与计算开销。

## 问题与动机

联邦图卷积推荐（FedGCN）允许各用户持有自己的用户-物品二分图并通过协同训练捕获高阶信息，但现有工作建立在全精度连续嵌入上，存在两个痛点：(1) 邻域聚合需要频繁的客户端-服务器通信，高维稠密连续嵌入消耗大量带宽，客户端本地训练开销高；(2) 在隐私约束下，如何低成本地构造准确且不泄露隐私的全局用户-物品二分图仍是开放问题。把学习哈希（learning to hash）引入推荐可把相似度计算变成汉明空间的 XOR 检索，但离散函数不可微；已有两类方案（代理函数两阶段、近似梯度）分别牺牲了训练效率或引入优化偏差。

## 方法

两部分：(1) HashRec——哈希图卷积方法：设计符号约束损失（sign-constrained loss）引导优化，使嵌入逐步趋向二进制/三值汉明码并提升表征能力，配合改进的图卷积规则学习用户-物品间的节点信息；训练与推理全程离散，相似度用汉明空间高效计算。(2) TriPro——带三重保护（适配区、秘密区、验证区）的隐私框架：每次卷积只需做一次秘密分享，服务器聚合三个区域的信息即可更新物品哈希码并得到“假全局图”所需的关键信息；论文严格证明服务器由此获得的信息是无损的，且服务器与其他客户端推断某用户哈希码的概率仅为 1/3^K（与随机猜无异）。

## 实验与结果

在四个真实数据集（ML1M、XING、Amazon-KS 等）上用 NDCG@、Pre@、Rec@（5/20/50）评测，对比 LSH、LightGCN、FedPerGNN、P-GCN、FedHoG、DCF、HashGNN、HS-GCN 等基线：FedHashRec/HashRec 在精度与效率上均优于现有 fully discrete 方法。消融显示去掉符号约束损失（w/o Lsign）或加入初值正则化（w/ Lini）都会在全部数据集上下降（如 ML1M 的 NDCG@5：HashRec 0.3089 vs w/o Lsign 0.2969）。资源分析：三值汉明码每个值仅需 2 bit，训练/推理嵌入存储为 2×K×(m+n)，远低于全精度的 32×K×(m+n)，且 HashRec 在全部数据集上训练效率最高。

## 贡献与局限

- 贡献一：HashRec——面向推荐的全离散哈希图卷积方法，用符号约束损失解决离散优化难题，兼顾精度与训练/存储效率。
- 贡献二：TriPro——三重保护隐私框架，以单次秘密分享构造无损“假全局图”，并给出信息无损与隐私的严格理论证明。
- 贡献三：开源四个数据集的代码与脚本，支持复现（github.com/YannickCodeHome/FedHashRec）。
- 局限：离散优化仍采用 STE 近似梯度，存在梯度偏差；未来拟研究更精确的梯度估计方法与更深的图卷积关系建模；论文当前为接受后 preprint（2026-08-26 录用，尚未正式排版）。

---

DOI: 10.1016/j.artint.2026.104607
