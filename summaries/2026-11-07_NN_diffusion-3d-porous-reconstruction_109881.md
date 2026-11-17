# Diffusion-based reconstruction of three-dimensional porous media structures from two-dimensional image sequences 总结

## 基本信息
- **标题**: Diffusion-based reconstruction of three-dimensional porous media structures from two-dimensional image sequences
- **作者**: Zongshun Xu、Mingliang Gao、Yongpeng Tan 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109881
- **发表**: 2026-11-07
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109881

## 一句话概括
多尺度差异引导扩散模型利用相邻二维切片的变化信息逐层重建三维多孔结构，并在多组样本和消融实验中优于若干比较方法，但结果依赖有限样本及所选形态与物理约束。

## 问题与动机
如何从数量有限的二维图像序列重建能够保留孔隙形态连续性及相关物理特征的三维多孔介质结构？

## 方法
方法先将相邻切片的差分编码为序列表示，再以多尺度差异引导注意力和双路径特征提取同时建模孔隙骨架与细节；训练时通过融合形态特征和物理性质的多参数损失约束逐层扩散生成。

## 实验与结果
论文在多种多孔介质样本上评估重建结果，与代表性模型比较，并进行多角度消融；作者报告重建质量和效率具有竞争力，消融结果表明差分引导、注意力及融合损失共同改善表现（PDF 第 8–14 页）。结论受样本类型、二维切片数量和物理约束定义限制。

## 贡献与局限
研究把相邻切片差异纳入扩散式三维重建，并以形态和物性联合约束提升结构一致性；在未见材料、不同成像条件及下游物理模拟中的可靠性仍需验证。

---
DOI: 10.1016/j.neunet.2026.109881
