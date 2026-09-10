# Consistency guided multiple plane image construction for novel view synthesis 总结

## 基本信息
- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: Consistency guided multiple plane image construction for novel view synthesis
- **作者**: Yichang Lv, Shuo Zhang, Jiajun Chen, Chen Gao, Youfang Lin
- **期刊 / 会议**: Neural Networks 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108955
- **PDF**: [ConsistencyMPIViewSynthesis.pdf](papers/ConsistencyMPIViewSynthesis.pdf)

## 一句话概括
论文提出一致性引导的 MPI 构造方法 CG-MPI，通过由近及远逐层生成多平面图像并累积跨视图、跨层信息，提升稀疏输入下的新视角合成和多帧去噪。

## 问题与动机
MPI 能以可泛化的场景表示支持未知场景的新视角合成，但现有方法常并行预测各深度层，难以处理遮挡和复杂几何，且需要较多深度平面、计算成本较高。层间缺乏显式上下文还会导致表面不连续、边缘伪影和前后景不一致。

## 方法
方法沿深度方向串行构造 MPI，逐层累积前景信息。cross-view consistency mask 把不同输入视图中的遮挡/可见性差异引入当前层；cross-layer consistency mask 约束层间关系；depth guidance strategy 注入场景深度上下文，帮助网络理解几何结构。作者实现了 16 层与 48 层两种配置。

## 实验与结果
实验使用 Spaces（100 个场景，90/10 训练测试）和 Real Forward-Facing（48 个场景，40/8 训练测试）数据集，评估固定/变化视图位置、稀疏视图和多帧去噪。方法在视图合成上较 SOTA 提升约 0.6%–1.1%，去噪任务提升约 2.1%；在较少参数和相对较低计算成本下改善遮挡、深度不连续区域的细节与一致性。

## 贡献与局限
贡献是将跨视图一致性、跨层一致性和深度引导统一进逐层 MPI 构造，并在合成与去噪任务上验证泛化和效率。局限是仍依赖预先设定的离散深度平面，连续表面和大深度变化可能出现离散化伪影；自适应深度采样、动态场景和移动端部署仍需研究。

---
DOI: 10.1016/j.neunet.2026.108955

