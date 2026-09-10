# Orbit-based universal approximation via hypercyclicity on compact–open topology 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Orbit-based universal approximation via hypercyclicity on compact–open topology
- 作者：Farzona Mukhamedova, Ivan Tyukin, Farrukh Mukhamedov
- 期刊 / 年份：Neural Networks，2026（论文卷期标为 205，2027；在线日期为 2026）
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.109563
- PDF：[OrbitHypercyclicApproximation.pdf](papers/OrbitHypercyclicApproximation.pdf)

## 一句话概括

论文证明，在合适的激活函数和 compact–open topology 下，可以固定一个神经网络种子函数与一个加权平移算子，仅沿该算子的轨道迭代，就在紧集上一致逼近任意目标函数，而不必为每个目标重新优化网络参数。

## 问题与动机

经典 universal approximation 通常为每个目标函数重新选择权重，且许多结论建立在紧输入域上。论文关注能否把一族目标编码到一个固定函数中，再通过固定变换的迭代读取不同近似，从而把表达能力的一部分从反复训练转移到函数空间中的动力学轨道。

## 方法

作者研究加权平移算子 \((T_{λ,β}f)(x)=λf(x+β)\)，其中 λ、β 非零，并在一隐层网络类及其 compact–open 闭包上构造 hypercyclic vector，使其迭代轨道在相应函数空间中稠密。证明通过把局部目标放置在空间上分离的区块，并用平移迭代依次读出；同时构造稠密的周期点，得到 chaoticity。论文还在满足 compact-wise density 的条件下将机制推广到任意深度和高维输入。

## 实验与结果

这是纯理论研究，不使用数据集、数值基线或性能实验。主要结果是：一维情形存在轨道在 compact–open topology 下稠密的固定种子；加权平移算子 hypercyclic 且周期点稠密；任意网络深度、非零高维平移向量下也可得到相应的 hypercyclicity/chaoticity。论文还指出，若要求种子本身属于 C₀(R)，一侧区块构造需要 |λ|>1。

## 贡献与局限

贡献是建立“固定种子＋固定算子轨道”的通用逼近视角，证明其超循环和混沌结构，并扩展到更深和更高维网络。局限在于结论主要是存在性结果：尚未给出显式、数值稳定的种子、逼近速率或迭代索引选择算法；当迭代次数较大时可能出现病态放大，且其他拓扑、算子及实际训练程序仍需研究。

---
DOI: 10.1016/j.neunet.2026.109563
