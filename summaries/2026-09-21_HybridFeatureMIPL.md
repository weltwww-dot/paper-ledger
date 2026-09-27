# Hybrid feature-based collaborative disambiguation for multi-instance partial-label learning 总结

## 基本信息
- **标题**: Hybrid feature-based collaborative disambiguation for multi-instance partial-label learning
- **作者**: Zhen Zhu、Yining Sun、Yuanbo Wang et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-21
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109648
- **PDF**: [NN_2026_HybridFeatureMIPL.pdf](papers/NN_2026_HybridFeatureMIPL.pdf)

## 一句话概括
本文提出混合特征协同消歧框架，通过袋级与实例级信息互补、正则化和流形传播，从多实例候选标签中识别真实标签。

## 问题与动机
多实例部分标签学习中，每个样本袋含多个实例，且候选标签集合中只有一个真实类别。既有方法常依赖单一特征空间或简单传播，难以同时处理实例差异、标签歧义及错误实例干扰。

## 方法
方法对齐袋表示与实例表示，通过双重消歧模块协同利用两类特征；正则化约束候选标签分布，流形传播利用样本结构，动态过滤抑制不可靠实例。实验覆盖多种基准及真实医疗数据。

## 实验与结果
论文报告图像、音频和医疗等任务上整体具有竞争力。单轮训练约 0.58 秒，快于 MIPLGP 的 1.03 秒、慢于 DEMIPL 的 0.41 秒；相较 MIPLGP 约快 43.7%，内存约 422 MB。作者还报告对若干参数变化具有稳定性。

## 贡献与局限
- 联合建模袋级与实例级特征，并结合协同消歧和动态过滤。
- 在多个基准及一个真实医疗任务上验证准确率与效率。
- 结果仍限于论文的数据与设定；复杂真实场景以及其他健康、生物信息任务需进一步验证。

---
DOI: 10.1016/j.neunet.2026.109648
