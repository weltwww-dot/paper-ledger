# D3CNet: Long-term time series prediction based on dual decomposition and dual-channel hybrid network 总结

## 基本信息

- **标题**: D3CNet: Long-term time series prediction based on dual decomposition and dual-channel hybrid network
- **作者**: Bo He, Yunya Bo, Longbing Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108893
- **arXiv**: 无
- **PDF**: [NN_2026_D3CNetDualChannel.pdf](papers/NN_2026_D3CNetDualChannel.pdf)

## 一句话概括

提出基于二次分解（EMD 分解加季节成分重构，S-EMD）与双通道混合网络（1D-CNN 与 GRU）的长时序预测方法 D3CNet，在六个公开数据集上显著降低预测误差。

## 问题与动机

时序预测广泛用于金融、交通、天气、电力等领域，特征提取是核心，但数据复杂多样使传统分解方法难以适应。一方面，不同尺度信息混合，EMD 分解常出现模态混叠，趋势与季节成分难以被充分利用；另一方面，单通道模型无法同时捕捉多元时序的长程相关与局部特征——CNN 长程依赖捕捉弱，RNN/GRU 长序列易梯度问题，Transformer 复杂度高，而线性模型过于简化易过拟合。

## 方法

D3CNet 采用"二次分解 + 双通道混合网络"架构。首先用 EMD（EMD-Block）将时序自适应分解为多个不同频率的本征模态函数 IMF，并通过相关分析滤除高频噪声；随后对去噪序列做季节分解重构（SC-Block）：取对数将乘法模型 Yt=Tt×St×Et 化为加法关系，用滑动平均估计趋势，按季节周期分组求均值估计季节成分并标准化，再经反变换得到拟合值与残差，从而获得更平滑、带季节特征的序列（S-EMD 二次分解）。数据经标准化 Z=(x−u)/σ 后输入双通道混合网络：GRU 通道处理原始序列以捕捉长期依赖，1D-CNN 通道（卷积、池化、全连接层）处理分解后序列以捕捉局部与季节特征；两通道特征经 concatenate 融合，再接全连接层与输出层完成预测。

## 实验与结果

在六个常用数据集上做了多元与单变量实验：ETTh1/ETTh2（小时级）与 ETTm1/ETTm2（15 分钟级）各 7 维、Weather（21 维气象指标）、Exchange_rate（8 国外汇日度数据），预测长度 {96,192,336,720}，采用 MSE、MAE 指标（并用 R² 与 SparseTSF 对比），基线含 SparseTSF、PatchTST、TimeMixer、DLinear、Linear。多元预测中，D3CNet 在四个 ETT 数据集上相对 SparseTSF 平均 MSE 提升超 20%、MAE 降低 15.1%（摘要称 ETT 平均 MSE 降 29.4%、MAE 降 15.7%），其中 ETTh1 平均 MSE/MAE 为 0.028/0.124（平均 MSE 提升 45%、MAE 提升 65%），ETTh2 为 0.142/0.335，ETTm1 为 0.056/0.137，ETTm2 为 0.08/0.243；Weather 上平均 MSE 降 35%、MAE 降 11%（0.0013/0.0267）；Exchange_rate 上相对 PatchTST 平均 MSE 降 56.57%、MAE 降 21.74%（0.185/0.360），预测步长 720 时仍保持低 MSE。单变量实验中相对表内最优方法平均 MSE 提升 42.2%、MAE 提升 23.3%（ETTh 上相对 SparseTSF 平均 MSE 提升 54.7%、MAE 提升 26.4%）。消融实验（ETTh2/ETTm2/Exchange_rate）表明移除 S-EMD、conv1D 或 GRU 任一模块性能均明显下降，conv1D 对周期性数据的 ETTh2/ETTm2 影响最大，GRU 对无周期性的 Exchange_rate 影响最大；Weather 上 R² 平均 0.58（SparseTSF 为 0.2），对数据转折点的拟合更准。鲁棒性上，对 ETTh1 注入 0.1×N(0,1) 高斯噪声，平均 MSE 变化小于 3%、MAE 变化小于 0.5%；以 ETTh1 为例，模型平均参数量 44,581，训练约 150 秒，预测约 70 毫秒。

## 贡献与局限

- 贡献一：面向长期时序预测构建基于分解的双通道混合网络模型，实现更高效、更准确的预测。
- 贡献二：提出 S-EMD 模块，在 EMD 基础上加入季节因素以缓解模态混叠、有效提取多尺度特征，并使数据更平滑、优化迭代过程、提升整体计算效率。
- 贡献三：设计 GRU 与 CNN 分别处理原始与分解数据的双通道混合网络，各通道专注不同数据特征，融合结果增强鲁棒性并降低过拟合风险。
- 局限：多维度特征筛选中尚不能有效剔除无用特征，导致模型复杂度上升、训练效率降低；未来拟引入基于信息熵、互信息或稀疏表示的特征选择算法，配合 L1 等正则化技术及多任务学习下的特征共享机制加以改进。

---
DOI: 10.1016/j.neunet.2026.108893
