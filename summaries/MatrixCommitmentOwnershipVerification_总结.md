# Matrix Commitment-Based Ownership Verification for Distributed Machine Learning 总结

## 基本信息

- **标题**: Matrix Commitment-Based Ownership Verification for Distributed Machine Learning
- **作者**: Tianxiu Xie, Keke Gai, Jing Yu, Liehuang Zhu, Qi Wu
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 分布式机器学习安全、密码学承诺与知识产权保护
- **DOI**: 10.1109/TPAMI.2026.3687640
- **PDF**: [TPAMI_2026_MatrixCommitmentOwnershipVerification.pdf](papers/TPAMI_2026_MatrixCommitmentOwnershipVerification.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 MAMMON，用矩阵承诺记录分布式机器学习客户端的权重检查点和训练历史，在不公开数据的前提下验证客户端对最终模型的部分所有权、训练完整性与执行正确性。

## 问题与动机

分布式训练发布最终权重后，客户端难以证明自己的更新确实被纳入模型，恶意参与者则可能伪造训练历史或窃取他人的所有权。模型水印容易在聚合中暴露、干扰或衰减，重放训练会泄露数据，而 SNARK/可验证计算通常需要把训练过程算术化并频繁刷新证明，客户端成本较高。因此需要简洁、可更新、可聚合且不暴露训练数据的来源证明。

## 方法

MAMMON 把每个客户端的权重检查点组织成权重矩阵 W，并以 Client Training Record（CTR）作为每轮训练的最小审计单元。矩阵承诺用双变量多项式承诺单个矩阵，局部向量证明通过 multi-linear tree 生成；证明可沿树路径更新，并用 IPA 聚合多个位置的证明。三个 Training Specifications 分别检查相邻检查点分布相似性、随机独立初始化以及到最终权重的距离单调性；客户端私钥还被嵌入证明形成身份水印，CTR 更新摘要记录在 append-only distributed ledger 上。

## 实验与结果

理论分析给出 MAMMON 的承诺成本为线性量级、证明更新为 O(L + logN)、单点验证为 O(L·logN)。实现使用 BLS12-381 和 mcl，在 LeNet、ResNet18、AlexNet、VGG16、CLIP、Bert-Large、Stable Diffusion v1.4、Whisper-Large 等模型上评估，并与 Merkle-SNARK 的 SHA-256、Pedersen、Poseidon 实现比较。作者报告在 L=N=512 时聚合证明验证约 1.6 s，Whisper-Large 的更新延迟上限为 7.71 s；在 LeNet 中聚合耗时随 η 从 2² 增至 2¹¹ 为 0.087–38.444 s。CFA 和 REA 实验显示三种 TS 能识别伪造检查点；GIA 实验则显示 MAMMON 在两组梯度反演设置中将标签恢复准确率降至 0%，且本地模型精度与原模型基本一致。

## 贡献与局限

贡献包括：用可维护的 multi-linear tree 实现 DML 权重证明的快速更新与聚合；用身份绑定水印和同态承诺支持不可窃取、隐私保护的多客户端所有权审计；用 TS 验证训练轨迹而不改变模型结构和训练算法。局限是当前 TS 主要假设公开基准数据上的平滑轨迹，在 Non-IID 客户漂移、DP-SGD 噪声、检查点存储受限场景中可能失效；作者计划采用数据一致性或信息论判据，并探索只把 TS 编码进 zk-SNARK。DOI: 10.1109/TPAMI.2026.3687640
