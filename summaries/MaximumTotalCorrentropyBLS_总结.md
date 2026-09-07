# Maximum total correntropy-based broad learning system with robust M-estimator 总结

## 基本信息

- **标题**: Maximum total correntropy-based broad learning system with robust M-estimator
- **作者**: Tao Chen, Xi Chen, Wei Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108917
- **arXiv**: 无
- **PDF**: [NN_2026_MaximumTotalCorrentropyBLS.pdf](papers/NN_2026_MaximumTotalCorrentropyBLS.pdf)

## 一句话概括

针对宽度学习系统（BLS）难以处理训练样本输入噪声且对核宽选择敏感的问题，本文提出基于最大总体相关熵（MTC）的 MTC-BLS，并融合 M 估计器构造 MMTC-BLSa/MMTC-BLSb，在时序、回归与图像数据集上显著提升了噪声鲁棒性。

## 问题与动机

BLS 凭借随机映射构造特征节点与增强节点、仅用伪逆求解输出权重的轻量结构在诸多领域得到应用，但其目标函数基于最小均方误差（MMSE），只能在无噪声或高斯噪声环境下表现良好。现有的鲁棒改进（如误差熵类 BLS-QMEE、M 估计器类 RBLS、基于最大相关熵准则的变体）大多只假设输出含噪，无法有效处理输入数据中的噪声，且 RBLS 在极端离群值下易被离群值主导。此外，最大相关熵类方法在核宽偏离最优值时性能会明显恶化。为此，作者希望构建既能同时抑制输入与输出噪声、又能降低对核宽依赖的鲁棒 BLS。

## 方法

首先提出 MTC-BLS：保持 BLS 节点生成方式不变，将输出权重的求解由岭回归改为最大化总体相关熵（MTC）准则，其带归一化加权误差 ‖𝑨𝑖𝑾−𝒀𝑖‖²/‖𝑾̄‖² 的结构吸收了总体最小二乘（TLS）处理输入噪声的思想，而高斯核的指数项则继承 MCC 抑制大残差离群值的能力。为降低对核宽的依赖，进一步提出两类方法：MMTC-BLSa 将 M 估计器代价函数直接并入目标函数，与 MTC 构成双约束，通过拉格朗日乘子与 KKT 条件导出重加权最小二乘形式的权重表达式；MMTC-BLSb 则以 M 估计器的加权函数（如 Cauchy 权重）作为 MTC 准则内的样本权重系数，用于补偿核宽偏差造成的模型误差。Huber、Cauchy、Bisquare、Welsch 等 M 估计器均可选用，其阈值由中位数规则 p = Tuning·med(|𝒆|)/0.6745 确定。三种算法均采用不动点迭代求解输出权重，并基于 Banach 不动点定理给出了核宽满足 σ ≥ max{σ⋆, σ∗} 时收敛的充分条件，分析了与迭代次数、样本数和网络节点数相关的计算复杂度。

## 实验与结果

实验平台为 NVIDIA GeForce RTX 4090 GPU、256 GB 内存，Python 3.10 与 CUDA 12.4 环境，数据归一化到 (0, 1)。评测覆盖 7 个回归数据集（Abalone、Basketball、Mortgage、Photovoltaic Power1/2、SPARK-Raw、Batch）、2 个时间序列数据集（Mackey-Glass、Sunspots）与 4 个图像数据集（MNIST、NORB、CIFAR-10、CIFAR-100），基线为 BLS、C-BLS、MGC-BLS-Huber、GCN-LSTM、UQAE；回归用 RMSE 与鲁棒性指数 RI（=RMSE₀/RMSE_x×100%）衡量，图像分类用准确率，污染水平覆盖 10%–60% 的高斯噪声与 α-stable 噪声。结果显示：在时间序列与回归任务中，MTC-BLS 无需 M 估计器即可达到与 MGC-BLS-Huber 相当或更好的精度，引入 M 估计器的 MMTC-BLSa/b 进一步领先，其中 MMTC-BLSb-Welsch 在 Mackey-Glass 上取得最低 RMSE（60% 污染时 15.28×10⁻²，优于 BLS 的 22.44×10⁻²）；图像分类中 MMTC-BLSb-Huber 在四个数据集上准确率最高（MNIST 99.27%、NORB 91.62%、CIFAR-10 90.84%、CIFAR-100 83.19%），训练时间却远低于 GCN-LSTM 与 UQAE（如 MNIST 上约 62 秒对 400 秒量级）。Friedman 事后检验中 MMTC-BLSb-Huber 平均秩最低（1.98），与 BLS/C-BLS 相比 p 值远小于 0.05；各算法 RMSE 均在 10 次迭代内稳定收敛，且核宽敏感性实验显示 MTC-BLS 对核宽偏离较敏感，而 MMTC-BLSa/b 的性能随核宽变化保持稳定。

## 贡献与局限

主要贡献包括：一是重建 BLS 目标函数得到 MTC-BLS，融合 TLS 与 MCC 准则的优点，可同时处理输入与输出噪声；二是提出 MMTC-BLSa（M 估计器与 MTC 双约束）与 MMTC-BLSb（M 估计器作为 MTC 内加权系数）两类降低核宽依赖的鲁棒方法；三是为三种算法引入不动点迭代求解，并给出收敛性（充分条件）与计算复杂度分析；四是通过时间序列、回归与图像分类的多组实验验证了有效性与优越性。局限在于：最优网络结构依赖耗时的网格搜索确定，作者计划未来采用蚁群、遗传算法等高效启发式优化自动确定参数，并将方法进一步推广到更多分类等任务。

---
DOI: 10.1016/j.neunet.2026.108917
