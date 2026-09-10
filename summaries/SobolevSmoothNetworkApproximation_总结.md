# On the approximation capability of shallow and deep neural networks having smooth activations with respect to the Sobolev norm 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: On the approximation capability of shallow and deep neural networks having smooth activations with respect to the Sobolev norm
- **作者**: Hyeokjoo Park
- **期刊 / 会议**: Neural Networks 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108935
- **PDF**: [SobolevSmoothNetworkApproximation.pdf](papers/SobolevSmoothNetworkApproximation.pdf)

## 一句话概括

论文从理论上证明，使用光滑非多项式激活函数的浅层和固定深度神经网络，可以在 Sobolev 范数下同时逼近函数及其导数，并对网络宽度、深度和逼近误差给出明确阶数。

## 问题与动机

物理信息机器学习、Sobolev training 和含导数约束的模型不仅要求函数值逼近，还要求导数同时逼近。经典通用逼近结果多在 Lp 范数下讨论函数误差，不能直接说明导数误差；已有结果还常限制激活函数、目标函数空间或网络深度。因此，论文研究光滑激活、有限深度、大宽度网络在 Sobolev 空间中的系统逼近能力。

## 方法

作者先用 de la Vallée Poussin 型多项式逼近 Sobolev 函数，再用中心有限差分构造每个单项式的浅层神经网络表示，从而控制函数及各阶导数的误差。随后对隐藏层数作数学归纳，把浅层结果扩展到任意固定深度；对解析函数还结合 Taylor 多项式得到指数型误差界。证明在有界区域上进行，并允许 sigmoid、tanh、arctan、Gaussian、Softplus 和 SiLU 等光滑非多项式激活。

## 实验与结果

论文以理论证明为主，没有数据集、机器学习基线或大规模数值实验。定理 1 证明在 Ω=[−1,1]^d 上，单隐藏层宽度 O(N^d) 的网络达到 W^{k,p} 误差 O(N^{k−s})；定理 2 将其扩展为任意 L≥2 的固定深度网络，其中一层宽度 O(N^d)、其余层宽度 O(1)，保持相同误差阶。对满足导数增长条件的解析函数，定理 3 给出 O(exp(−N)) 的 W^{s,∞} 误差；一个单项式数值例子验证了误差随有限差分步长呈 O(h^2) 衰减。

## 贡献与局限

主要贡献是统一给出光滑非多项式激活网络在 Sobolev 范数下的浅层与固定深度逼近定理，明确了宽度—误差关系，并覆盖比同阶 Barron/Hölder 结果更一般的 Sobolev 目标空间。局限是结论建立在有界区域及特定构造上，权重和偏置的尺度可能较大；无界域、可编码参数以及随深度增加而改善误差界的问题仍未解决。

DOI: 10.1016/j.neunet.2026.108935

