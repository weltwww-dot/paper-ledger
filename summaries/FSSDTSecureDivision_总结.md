# FSS-DT: Secure Division-Free Decision Tree Training and Inference via Function Secret Sharing 总结

## 基本信息

- **标题**: FSS-DT: Secure Division-Free Decision Tree Training and Inference via Function Secret Sharing
- **作者**: Anxiao Song, Shujie Cui, Ke Cheng et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing, 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3695949

## 一句话概括

论文提出面向垂直划分数据的两方安全决策树框架 FSS-DT，通过无除法训练算法和基于函数秘密共享的轻量级比较协议，降低 MPC 决策树训练与推理的计算和通信开销。

## 问题与动机

垂直联邦场景中，不同数据所有者持有同一批样本的不同特征，需要在不暴露原始数据的条件下协同训练决策树。现有 MPC 决策树的主要瓶颈是除法和大量比较：除法不适合秘密计算，而已有安全比较协议在大规模数据上仍然代价较高。

## 方法

作者设计 MPC 友好的 division-free decision tree（DFDT），以避免按候选切分重复执行昂贵除法，同时尽量保持明文决策树的切分质量。安全比较部分基于优化的 distributed comparison function，结合 0/1 编码压缩函数秘密共享密钥，并用 early termination 在比较结果已确定时提前停止；训练和推理协议以两方加法秘密共享为基础。

## 实验与结果

原型在 4 个 UCI 数据集和 2 个 Kaggle 垂直联邦数据集上测试，并与 Pivot、Swan 比较。FSS-DT 与明文 DFDT 相比无准确率损失；在 Poker Hand 数据集上，LAN/WAN 训练速度分别约为 Pivot 的 17.5 倍和 51.1 倍、Swan 的 8.4 倍和 8.8 倍，训练通信量为 6.0 GB。平均 1000 个样本推理耗时 12 ms，通信量约 0.1 KB。

## 贡献与局限

论文将无除法树训练与高效 FSS 比较协议组合成可运行的两方框架，并通过原型实验展示其在高延迟网络中的收益。局限是评估主要覆盖两方、半诚实式垂直数据协作与有限数据集；恶意安全模型、更多参与方、动态特征和更深更大规模树的代价仍需研究。

---
DOI: 10.1109/tdsc.2026.3695949
