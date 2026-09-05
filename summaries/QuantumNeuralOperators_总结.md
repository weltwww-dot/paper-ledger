# Quantum neural operators with implicit quadratic frame 总结

## 基本信息

- **标题**: Quantum neural operators with implicit quadratic frame and expressivity advantages
- **作者**: Ruocheng Wang, Xiaoqiu Zhong, Zhuo Xia, Junchi Yan
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **发表**: 2026-09-03
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01289-7
- **代码**: https://zenodo.org/records/21084057

## 一句话概括

引入硬件高效的量子神经算子（quantum neural operator），借助隐式二次框架（implicit quadratic frame）突破经典线性容量限制，在含噪中等规模量子（NISQ）时代加速求解微分方程的表示力。

## 问题与动机

神经算子用于学习微分方程的解算子，但经典实现受线性容量限制，难以高效表达复杂解空间；量子计算有望提供超越经典的表达优势，但需在 NISQ 硬件的噪声限制下设计硬件高效、可实现的量子神经算子。

## 方法

设计硬件高效的量子神经算子：以隐式二次框架为核心构造，利用量子态的二次相互作用提升表达力；针对 NISQ 设备做硬件友好设计，用于微分方程求解。

## 实验与结果

原文摘要（Nature 编辑摘要）确认方法提供加速表达力并适用于微分方程求解；具体数值原文摘要未展开。

## 贡献与局限

- 贡献一：首个面向微分方程求解的硬件高效量子神经算子，克服经典线性容量限制。
- 贡献二：隐式二次框架带来表达力优势，适配 NISQ 时代的硬件约束。
- 局限：具体性能数字原文摘要未提供；更大规模量子硬件与方程类的验证待后续工作。

---

DOI: 10.1038/s42256-026-01289-7
