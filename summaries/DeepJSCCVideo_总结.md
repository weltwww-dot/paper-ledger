# DeepJSCC for Video Semantic Communication with General Semantic Preservation 总结

## 基本信息

- **标题**: DeepJSCC for Video Semantic Communication with General Semantic Preservation
- **作者**: Junting Li、Xuechen Chen、Xiaoheng Deng
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109602
- **arXiv**: 无
- **PDF**: [NN_2026_DeepJSCCVideo.pdf](papers/NN_2026_DeepJSCCVideo.pdf)

## 一句话概括

该框架在端到端视频 DeepJSCC 中显式保持任务无关的通用语义和时间一致性，使无线传输后的重建视频既保持画面质量，也能更好支持多种未专门微调的下游任务。

## 问题与动机

无线视频会受到带宽限制、时变噪声和传输损伤影响，而像素重建质量高并不保证语义结构仍可用于自动驾驶、视频理解或远程医疗。已有学习式传输方法主要优化视觉失真，对跨任务可迁移语义和帧间连贯性关注不足。

## 方法

作者提出端到端视频联合信源—信道编码框架。Video-level Semantic Alignment Module 通过视频级对比学习缩小原始视频与重建视频的语义距离；Temporal Consistency Learning Module 预测未来帧的语义嵌入，以约束重建视频形成更稳定的时间动态。

## 实验与结果

实验显示，该方法的重建质量与现有 DeepJSCC 和传统传输方案相当，同时在多个视频下游任务上持续获得性能提升，而且不需要针对各任务额外微调。结果说明，显式保护通用语义不会以明显牺牲基础重建质量为代价。

## 贡献与局限

贡献是把任务无关语义对齐和未来语义预测同时纳入视频 DeepJSCC，改善传输后视频的可迁移性。局限是效果依赖训练时的语义表征模型；面对新型信道、超长视频、实时端侧算力限制及与训练分布差异较大的任务时仍需验证。

---
DOI: 10.1016/j.neunet.2026.109602
