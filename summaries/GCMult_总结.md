# A novel FPGA-based garbled circuit accelerator for secure two-party multiplication 总结

## 基本信息

- **标题**: A novel FPGA-based garbled circuit accelerator for secure two-party multiplication (GCMult)
- **研究方向**: 信息安全
- **作者**: Hiva Assasi, Shahram Etemadi Borujeni
- **期刊 / 会议**: IJIS 2026
- **发表**: 2026-08-23
- **DOI**: 10.1007/s10207-026-01315-0
- **PDF**: [IJIS_2026_GCMult.pdf](papers/IJIS_2026_GCMult.pdf)

## 一句话概括

提出 GCMult，一个基于 FPGA 的乱码电路（garbled circuit）安全两方乘法加速器：把单次乘法分解为可并行的子运算，用 Karatsuba 算法提升并发并显著减少门数量。

## 问题与动机

隐私保护函数计算（如云端机器学习、物联网）依赖乱码电路，但其计算与通信开销很高；乘法是基础运算，直接影响整体效率。已有工作探索独立操作的并行执行，但没有研究过在乱码电路框架内把单次乘法分解成更小的并发子运算。

## 方法

对布尔电路采用并行化分解技术：应用 Karatsuba 算法增强并发，同时大幅减少门数量（尤其是高成本的 AND 门）；面向乱码乘法电路设计专门的硬件加速器，同时提升计算速度与通信效率。

## 实验与结果

FPGA 实验表明：与最佳现有硬件加速器相比，乱码时间平均降低 258%，通信带宽平均改善超过 60%；与已知最快的软件实现相比实现 4140% 的加速（数字来自原文摘要）。

## 贡献与局限

- 贡献一：首次在乱码电路框架内分解单次乘法为并发子运算，并给出 GCMult 硬件加速器。
- 贡献二：Karatsuba 分解同时降低门数与通信开销，实验验证了跨软硬件的大幅收益。
- 局限：评测以 FPGA 实现为主，更广泛的安全性与部署场景原文摘要未展开。

---

DOI: 10.1007/s10207-026-01315-0
