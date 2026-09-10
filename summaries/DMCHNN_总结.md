# A discrete memristive cyclic Hopfield neural network with multi-cavity-like attractors and application in secure communication 总结

## 基本信息

- **标题**: A discrete memristive cyclic Hopfield neural network with multi-cavity-like attractors and application in secure communication
- **作者**: Gang Yang、Chunhua Wang、Quanli Deng
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108953
- **arXiv**: 无
- **PDF**: [NN_2026_Paper13.pdf](papers/NN_2026_DiscreteMemristiveHopfield.pdf)

## 一句话概括

DMCHNN 用离散忆阻器循环 Hopfield 网络产生多腔超混沌吸引子，并验证其在安全通信中的抗噪能力。

## 问题与动机

具有突触样特性的离散忆阻器有助于模拟神经网络的复杂动力学，但如何产生可控、多样且可硬件实现的超混沌吸引子仍是问题。研究希望把吸引子调控、随机性评估和安全通信实现连接起来。

## 方法

作者提出离散余弦忆阻器模型，并将其嵌入循环 Hopfield 神经网络形成 DMCHNN。通过耦合强度 k 和权重 w31 的幅度调制控制混沌范围与多腔吸引子数量。研究还分析初始值引起的同质/异质偏置增强行为和熵性能，并在 FPGA 上实现。

## 实验与结果

数值分析显示，系统可产生多种同质和异质吸引子，熵评估支持其随机性。硬件实验在 FPGA 上成功实现吸引子；基于 DMCHNN 构造的 HE-DCSK 通信系统相较其他混沌映射表现出更好的抗噪性能。

## 贡献与局限

贡献是提出可调控的离散忆阻循环 Hopfield 结构并完成 FPGA 与通信验证。局限是安全性主要由混沌和抗噪实验支撑，实际密钥管理、攻击模型和大规模硬件部署仍需独立分析。

---
DOI: 10.1016/j.neunet.2026.108953

