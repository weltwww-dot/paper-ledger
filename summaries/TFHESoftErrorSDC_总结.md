# Soft Error Rate Evaluation and Silent Data Corruption Detection for Reliable TFHE Computations on GPUs 总结

## 基本信息

- **标题**: Soft Error Rate Evaluation and Silent Data Corruption Detection for Reliable TFHE Computations on GPUs
- **作者**: Masakazu Yoshida, Kotaro Matsuoka, Masanori Hashimoto
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3714766
- **arXiv**: 无
- **PDF**: [TDSC_2026_TFHESoftErrorSDC.pdf](papers/TDSC_2026_TFHESoftErrorSDC.pdf)

## 一句话概括

本文首次通过质子加速辐照实验评估了 GPU 上 TFHE 同态计算的地面软错误率，并提出基于电路冗余与相位分布的两种静默数据损坏检测方法。

## 问题与动机

全同态加密（FHE）可在不解密的情况下在云端对加密数据执行任意计算，是实现隐私保护云计算的重要手段，但其计算开销巨大，需要大规模服务器与 GPU 持续并行运行。宇宙射线诱发的中子/质子会产生瞬态软错误，造成系统崩溃（DUE）或输出错误却不触发任何告警的静默数据损坏（SDC）；而同态计算中的中间值始终处于加密状态，云服务器无法像明文那样做取值范围等常规校验，且 TFHE 解密输出只有 0/1 两种取值，缺少可用于检错的显式冗余。此前针对 FHE 的软错误率评估完全空白，因此在真实系统上量化 TFHE 的软错误风险并设计可行的 SDC 检测手段，是部署基于 TFHE 的云服务前必须解决的问题。

## 方法

作者在日本若狭湾能源研究中心使用 96 MeV 质子束（可等效 50 MeV 以上中子）对 NVIDIA RTX A4000 GPU 芯片进行加速辐照实验，注量选为 2.6×10^6 p/cm²/s，总注量 8.7×10^10 p/cm²，只让准直后的质子束照射 GPU 芯片。实验测量片上存储（寄存器堆、共享内存）的 SEU 截面，以及 HomNAND、HomXOR、HomMUX 等 HomGate 和由 188 个 HomGate（102 个 HomNAND、63 个 HomXOR、23 个 HomNOT）组成的 32 位加法器 HomCircuit 的 SDC/DUE 截面，运行环境基于 cuFHE 与 Iyokan。随后用面向 Ampere 架构改造的 NVBitFI 注入 2000 次故障以验证辐照结果的可复现性。最后提出两种 SDC 检测方法：方法 1 复制 HomCircuit 并用同态 HomXOR 比较两份密文主输出，产生加密错误检测信号交用户解密判定；方法 2 利用 TLWE 噪声服从模高斯分布的特性，让用户解密全部 HomGate 输出，检查 bootstrap 前的原始相位是否落在 k 倍标准差范围内，越界即判定发生软错误，k 为用户可选参数。

## 实验与结果

实测单个 HomGate 的单次 SDC 截面约为 7.93×10^-11 至 9.18×10^-11 cm²/HomGate，突发 SDC 截面为 1.59×10^-11 至 4.74×10^-11 cm²/HomGate，各门类型之间差别不大；32 位加法器 HomCircuit 级 SDC 截面为 6.02×10^-10 cm²，潜在 SDC 截面为 0（加法器中门级扰动几乎必然传播到主输出）。按 JESD89B 地面高能中子通量 3.6×10^-3 n/cm²/s 折算，HomGate 级单次 SDC 率约 1.03–1.19 FIT、突发约 0.205–0.614 FIT，32 位加法器 HomCircuit 的 SDC 率为 7.80 FIT。故障注入估计整体比实测偏高约 2–2.5 倍，电路级截面估计为 2.7×10^-10 cm²、误差约 −55%，作者认为与束流时间有限及 σC 与 N 成正比假设有关。按电路规模比例外推，10×10 矩阵乘法 SDC 率达 0.41%；按更细致的乘法结构估算，100×100 与 500×500 矩阵乘法的出错概率分别约 0.012% 和 1.6%。将 7.80 FIT 按 CUDA 核心数折算到含 16384 块 H100 的集群（参考 LLaMA 3.1 训练规模），估计约每月 0.219 次 SDC。检测方法评估中，方法 1 在地面环境下漏检概率 P_missed 约为 3.8×10^-26，把无防护时的 SDC 概率从 3.9×10^-12 大幅降低，但服务器端开销超过 2 倍、吞吐量降到约 50%；方法 2 不增加服务器同态计算量，却要求用户解密并传输全部门输出，通信开销显著，其精度-召回率以方法 1 更优（k 扫描范围 1×10^-20 至 1）。

## 贡献与局限

主要贡献包括：首次完成 FHE/TFHE 在商用 GPU 上的地面软错误率评估（含片上存储、HomGate 与 HomCircuit 三层的截面数据），并给出大规模 TFHE 应用中 SDC 风险的数量级估计；提出了两种基于 TFHE 密文特点的 SDC 检测方法（电路级冗余与相位分布检查），定量比较了检测性能与服务器算力、通信开销之间的权衡，并给出漏检概率分析；通过辐照实验与故障注入的对照验证了评估结果的可复现性。局限方面：辐照束流时间有限导致观测事件少、估计误差较大；NVBitFI 故障注入无法模拟"写后未读即重写"的实际位翻转场景，造成约 2–2.5 倍的高估；突发 SDC 的具体成因（如块调度器故障或 bootstrap key 损坏）尚未完全明确；矩阵乘法与外推到 H100 集群的 FIT 换算依赖比例性等假设；两种方法各有开销短板，仅依赖选择性冗余、部分门解密与 ABFT 等作为未来改进方向。

---
DOI: 10.1109/tdsc.2026.3714766
