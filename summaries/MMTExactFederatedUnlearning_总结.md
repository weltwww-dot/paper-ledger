# MMT: Achieving Exact Federated Unlearning with Improved Post-unlearning Performance 总结

## 基本信息
- **标题**: MMT: Achieving Exact Federated Unlearning with Improved Post-unlearning Performance
- **作者**: Ze Yu Zhang、Nhung Bui、Arun Verma、Bolin Ding、Bryan Kian Hsiang Low
- **期刊 / 会议**: Machine Learning 2026 · 115:245
- **研究方向**: 人工智能
- **发表**: 2026-10-12
- **内容状态**: 完整
- **内容说明**: 已依据24页出版社正式版全文及表格图像完成中文六段式总结
- **DOI**: 10.1007/s10994-026-07117-8
- **PDF**: [ML_2026_MMTExactFederatedUnlearning.pdf](papers/ML_2026_MMTExactFederatedUnlearning.pdf)

## 一句话概括
论文提出 BMT 与 MMT，在训练阶段保留相互隔离的本地及子联邦模型，删除客户端时仅聚合未受其影响的模型重新初始化，从而在论文的精确遗忘定义下改善遗忘后的模型性能与恢复速度。

## 问题与动机
客户端虽然不共享原始数据，其更新仍会经多轮聚合影响全局模型。删除客户端后从随机权重重新训练可以消除其影响，却会使模型性能骤降并延长服务恢复时间；近似遗忘又可能残留数据影响，因此作者研究如何兼顾精确移除与可用性（PDF第1—5页）。

## 方法
BMT 为每个客户端维护只用自身数据训练的独立模型；MMT 进一步以影响树组织子联邦模型，同层分支使用互不相交的客户端集合。遗忘时丢弃受影响的模型及优化器等训练状态，聚合未受影响的最大子树与本地模型，并以新状态继续训练；BMT 是不保留中间子模型的特例。给定客户端删除概率，Huffman 二叉树使影响退化分数 IDS，即删除后所需聚合模型数的期望，最小；这不是对测试准确率的全局最优保证（PDF第6—10、17—20页）。

## 实验与结果
实验覆盖 MNIST、FashionMNIST、CIFAR-10/100，以及 GPT-2、Llama-3.2-3B 的语言识别和多语言情感任务，比较从头重训 RfS、FedCIO、Exact-Fun 与 FATS。表4中，CIFAR-10 遗忘后达到45%准确率，MMT 需3轮通信、RfS 需162轮；CIFAR-100 达到40%则为37轮与54轮。图2结果取5个随机种子的均值。成员推断结果接近 RfS，但并非全部接近随机猜测：GPT-2 语言识别任务两者 AUC 均为0.632（PDF第10—13页）。

## 贡献与局限
贡献是通过训练期隔离与影响树复用，在精确移除客户端数据影响的同时缩短遗忘后的恢复过程。其精确性依赖固定随机性及服务器元数据、数据无关的调度与超参数选择，并要求完整清除受影响训练状态；不要求所得权重与 RfS 相同，也不代表所有隐私风险消失。代价是额外训练与存储：表6的 CIFAR-10 设置中，MMT 服务器内存为19.35GB，RfS 为2.15GB；研究主要针对可信中心服务器协调的跨机构联邦学习，大规模跨设备部署仍属后续工作（PDF第4、14、16、18—20页）。

---
DOI: 10.1007/s10994-026-07117-8 · PDF: [ML_2026_MMTExactFederatedUnlearning.pdf](papers/ML_2026_MMTExactFederatedUnlearning.pdf)
