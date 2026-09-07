# On Convergence of Adam With Data Dependent Stepsize 总结

## 基本信息

- **标题**: On Convergence of Adam With Data Dependent Stepsize
- **作者**: Alokendu Mazumder, Rishab Sabharwal, Bhartendu Kumar, Manan Tayal, Chirag Garg, Arnab Roy, Punit Rathore
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-01-22（收稿 2025-11-12，录用 2026-01-15，刊于 2026 年 9 月期）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3656866
- **arXiv**: 无
- **PDF**: [TAI_2026_AdamDataStepsize.pdf](papers/TAI_2026_AdamDataStepsize.pdf)

## 一句话概括

提出由网络动态与数据（初始损失、损失 Lipschitz 光滑度、训练轮数）决定的 Adam 恒定步长估计 αours=√(2L(w0)/(K̂T))，省去衰减调度与穷举调参，并首次给出 Adam 以常数步长全局收敛的理论保证。

## 问题与动机

Adam 是神经网络训练中最常用的优化算法之一，但其性能对步长（learning rate/stepsize）这一超参数高度敏感；在大模型与大尺度数据集上穷举调步长既昂贵又耗时。为逼近非凸损失轨迹，文献常采用衰减式步长调度（如线性衰减、指数衰减、步进衰减），但这些调度在快速衰减时反而可能造成发散或收敛缓慢，且已有 Adam 收敛性充分条件大多要求步长随迭代衰减（如 αt=α/t^a）或对连续步长比 Γt 施加正定性、时间去相关等约束，条件苛刻且不易验证。作者因此提出三个问题：常数或非增步长下 αt=α/√T 是否足以保证 Adam 更好收敛？步长中是否需要纳入模型与数据动态相关的项？若存在这样的项，是否会带来更好收敛？本文目标是给出一个依赖模型与数据动态的精确常数步长，同时消除"衰减调度易出问题"与"必须穷举搜索步长"两大痛点。

## 方法

本文从理论上推导 Adam 在固定步长下的收敛充分条件，并提出实用的步长估计公式 αours=√(2L(w0)/(K̂T))（其中 L(w0) 为初始损失，K̂ 为损失关于网络参数的 Lipschitz 光滑度估计，T 为训练总迭代/轮数；对最小值为 0 的交叉熵损失取 L(w*)=0）。具体包括：(1) 定理 1 与定理 2 证明在 K-光滑非凸损失、梯度/二阶矩有界、β1<ε/(ε+γ) 且 ρ 足够大的假设下，确定性 Adam 与随机 Adam 取 α=√(2(L(w0)−L(w*))/(KT)) 时分别满足 ∥∇L(wt)∥2≤ε 与 E[∥∇L(wt)∥2]≤ε（t≤T），收敛率为 O(1/T^1/4)，与 SGD 同阶，且无需 Γt 正定性与快速衰减步长；(2) 提出 Algorithm 2 估计 Lipschitz 光滑度：按 Kaiming He 均匀分布随机采样网络权重，用幂法求 Hessian 谱范数并取最大值作为保守估计 K̂，定理 4 证明 N→∞ 时 K̂ 依分布收敛到真实光滑度 K，且该估计对应 L2 正则损失（MAP 准则），可规避尖锐极小值导致步长消失的问题；(3) 通过大量实验验证：全连接网络的全批量与小批量（batch 5000）玩具实验、LeNet/VGG-9/ResNet-18/MobileNet-V2 及 ViT-Base 在 MNIST/CIFAR-10/CIFAR-100/ImageNet-100 上的训练、全量 ImageNet 上 ResNet-18（batch 256、100 epochs）的大规模实验，以及 LLaMA-3.2-3B-Instruct 与 Qwen-3-4B-Instruct 的 LoRA 微调（SQuAD 问答生成与 AG News 分类，LoRA rank=16、α=32、dropout=0.05、batch 16、3125 步、约 1 epoch）。对照基准包括五种衰减调度、常数步长集合 {10^-1,…,10^-5}、2×αours 与 αours/2 变体，以及 AdaBound、Yogi、MSVAG、RAdam、AdamW 等现代自适应优化器。

## 实验与结果

实验表明所提步长与穷举搜索得到的最佳步长非常接近且更稳定。在全量 ImageNet 上用 ResNet-18（αours=5.9×10^-4）：Adam+αours 的 Top-1 准确率为 67.53%，αours/2 达 67.79%，显著高于所有 Adam 步长调度（linear 62.77%、cosine 62.53%、exponential 62.59%、inverse time 60.59%、sqrt 62.28%、step 57.33%）；与其他优化器相比（AdaBelief 70.08%、Yogi 68.23%、AdaBound 68.13%、AdamW 67.93%、RAdam 67.62%、Adam 63.79%、MSVAG 65.99%），本文方法虽未超过 AdaBelief/Yogi，但以对 Adam 的最小改动取得与 AdamW 相当并超过 RAdam、MSVAG 的性能。在 ViT-Base + ImageNet-100 上，常数步长 10^-1 自训练开始即产生 NaN（精度 NA），而常见调度器测试精度仅约 1.65%–13.22%，αours/2 达 59.14%、αours 达 54.68%（约为部分对照的 3 倍以上）；LeNet/MobileNet-V2 等实验中本文步长与最优调度的梯度范数差距可达 10^-1 量级，全批量 toy 实验中 100 epochs 后与最优调度（指数衰减）的梯度范数差距约 10^-2 量级且压向零更激进。LLM 微调（SQuAD/AG News）中固定步长一致优于各 Adam 调度：SQuAD 上 αours/2 的 Exact Match/F1 最高，LLaMA-3.2-3B 为 0.7141/0.8585，Qwen-3-4B 为 0.7176/0.8660；AG News 上 αours/2 的 Accuracy/F1 分别为 0.9166/0.9162 与 0.9132/0.9134，且在 cosine 调度下与 AdaBelief、AdamW、RAdam 等相当并稳定超过 Yogi、AdaBound。LLM LoRA 场景是唯一 αours/2 优于 αours 的场景。

## 贡献与局限

贡献：(1) 推导出精确常数步长 αours=√(2L(w0)/(K̂T))，无需穷举搜索即可逼近最佳步长；(2) 该步长可在一定条件下直接作为各类衰减调度的即插即用替代品，省去调度调参时间；(3) 据作者所知首次在理论上保证 Adam 以依赖模型与数据动态的精确常数步长实现全局收敛（损失梯度范数收敛到 0），同时覆盖确定性与随机版本，无需 Γt 正定性；(4) 提出简单可行的损失 Lipschitz 光滑度估计方法（Algorithm 2），并给出其依分布收敛的保证；(5) 在图像分类、全量 ImageNet 与 LLM 微调等跨领域任务中广泛验证，全程稳定无发散。局限与未来工作：(1) 实验仅限交叉熵损失，其他损失函数待研究；(2) 收紧 Adam 收敛率仍是开放问题（当前为 O(1/T^1/4)）；(3) 随机版本定理需梯度符号一致等较强假设，理论分析仅针对固定步长；(4) LLM LoRA 微调中理论步长略激进（受仅更新适配器导致的各向异性曲率、batch=16 的高梯度噪声与约 3K 步短训练影响），该场景以 αours/2 更优，且 LLM 实验定位为稳健性检验而非全面基准。

---
DOI: 10.1109/tai.2026.3656866
