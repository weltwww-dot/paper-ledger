# Dual CNN and ViT experts fusion for open set recognition 总结

## 基本信息
- **标题**: Dual CNN and ViT experts fusion for open set recognition
- **作者**: Kai Ding, Yu Mao, Hui Chen, Yaojin Lin
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108910
- **PDF**: [NN_2026_DualCNNViTExpertsFusion.pdf](papers/NN_2026_DualCNNViTExpertsFusion.pdf)

## 一句话概括
CVEF 融合 CNN 与 ViT 多专家，结合局部与全局特征识别已知类并检测未知类。

## 问题与动机
开放集识别不能把未知样本误判为已知类。现有方法多依赖 CNN，缺少 ViT 的全局上下文能力；生成式方案又有计算和泛化成本。

## 方法
CVEF 设置多个 CNN、ViT 专家，分别提取局部纹理和全局上下文，再自适应融合输出，利用专家关注区域的互补性完成已知/未知判别。

## 实验与结果
标准开放集识别基准实验显示 CVEF 有效且鲁棒，并优于单一 CNN 核心的方法。全文摘要未给出统一具体数值。

## 贡献与局限
贡献是把两类视觉归纳偏置引入开放集多专家融合。局限是专家数量、计算开销、阈值校准和极端未知分布下的行为仍需更多验证。

---
DOI: 10.1016/j.neunet.2026.108910
