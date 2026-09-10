# Toward Personalized Differentially Private Learning for Decentralized Local Graphs 总结

## 基本信息

- **标题**: Toward Personalized Differentially Private Learning for Decentralized Local Graphs
- **作者**: Longzhu He, Peng Tang, Chaozhuo Li, Jinhu Fu, Litian Zhang, Li Sun, Philip S. Yu, Sen Su
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-07-07
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TKDE.2026.3710808
- **arXiv**: 无
- **PDF**: [TKDE_2026_PersonalizedDifferentiallyPrivateDecentralized.pdf](papers/TKDE_2026_PersonalizedDifferentiallyPrivateDecentralized.pdf)

## 一句话概括

论文提出 PPGNN，在去中心化图学习中为不同用户分配个性化隐私预算，并通过个性化扰动机制 PPM 与加权校准算法 FlexProp，在隐私强度异质时尽量保持节点分类效用。

## 问题与动机

社交平台、移动应用和边缘网络中的图数据通常由用户本地维护，节点属性和连接关系可能包含敏感信息。现有基于 Local Differential Privacy（LDP）的图学习方法大多给所有用户施加统一隐私级别，导致隐私需求较低的用户被过度加噪、整体图结构失真，并降低下游 GNN 的效用。论文关注不依赖可信服务器的个性化隐私与图学习性能平衡。

## 方法

PPGNN 由两阶段组成。第一阶段的 Personalized Perturbation Mechanism（PPM）包含 Multi-dimensional Local Randomizer，用于保护多维节点特征，以及 Extended Square Wave，用于保护离散的用户隐私级别。第二阶段 FlexProp 根据不同节点的隐私噪声和邻域信息进行加权传播，校准扰动后的特征；框架可接入 GCN、GraphSAGE 和 GAT。作者还分析隐私预算分配参数、传播步数和隐私级别范围对效用的影响。

## 实验与结果

实验使用 Cora、CiteSeer、Pubmed、LastFM、Facebook 和 Wikipedia 六个真实图数据集，与 NonPriv、BASE 和当前 LDP 图学习方法 LPGNN 比较，并采用 GCN、GraphSAGE、GAT 三种骨干。每个数据集按 50%/25%/25% 划分训练、验证和测试集，模型训练 500 个 epoch，测试结果为 10 次运行均值并给出基于 1000 次 bootstrap 的 95% 置信区间。在 ε=0.01 的示例中，PPGNN 与 LPGNN 相比 BASE 的准确率分别提高 26.8% 和 24.5%；在严格、宽松和双峰隐私分布下均优于 BASE，并在较宽松分布中更接近 NonPriv。

## 贡献与局限

贡献是提出面向图表示学习的个性化 LDP 框架、可保护隐私级别的 PPM，以及考虑多跳邻域和噪声差异的 FlexProp；六个真实数据集验证了其稳定性。局限是当极低隐私预算节点在某个邻域占主导时，FlexProp 仍可能存在残余偏差；同时方法假定用户能显式声明隐私级别，实际系统可能需要从行为信号推断或自适应校准隐私偏好。

---
DOI: 10.1109/tkde.2026.3710808
