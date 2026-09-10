# Multimodal-guided self-distillation for unified person search 总结

## 基本信息

- **标题**: Multimodal-guided self-distillation for unified person search
- **作者**: Xi Yang、Hexun Zhou、Haiyang Zhu、Nannan Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-02
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109581
- **arXiv**: 无
- **PDF**: [NN_2026_Paper10.pdf](papers/NN_2026_MultimodalGuidedPersonSearch.pdf)

## 一句话概括

MGSD 用多模态语言描述和自蒸馏改善统一行人搜索中的身份表示与未标注身份泛化。

## 问题与动机

统一行人搜索需要同时利用图像和文本等信息，但 one-hot 身份标签忽略行人之间的语义关系。CUHK-SYSU 中有 72.7% 行人缺少身份标注，限制了监督学习。研究希望用更细粒度的语义描述填补身份表示的碎片化。

## 方法

方法包含 Multimodal LLM-Assisted Text Generation（MLTG），为行人生成服饰、外观和环境等细粒度描述。文本引导模块利用这些描述学习跨身份关系，再通过自蒸馏把教师信息传给视觉表示，并针对未标注身份增强表示学习。

## 实验与结果

作者在统一行人搜索基准上评测，并报告在 PRW 数据集上达到 mAP 56.1%，同时保持面向大规模应用的计算效率。实验还显示方法对光照、遮挡和背景干扰具有更好的泛化表现。

## 贡献与局限

贡献是把多模态 LLM 描述、自蒸馏和统一行人搜索结合，利用语义关系缓解身份标签稀疏。局限是文本生成质量、视觉–语言模型偏差和额外推理成本可能影响部署，跨数据集标注体系的稳定性仍需验证。

---
DOI: 10.1016/j.neunet.2026.109581

