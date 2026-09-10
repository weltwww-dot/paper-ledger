# Towards continual low-light image enhancement through causal inference 总结

## 基本信息
- **标题**: Towards continual low-light image enhancement through causal inference
- **作者**: Fan Ji, Hao Li, Jiangmeng Li, Xiongxin Tang, Fanjiang Xu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108947
- **PDF**: [NN_2026_ContinualLowLightCausal.pdf](papers/NN_2026_ContinualLowLightCausal.pdf)

## 一句话概括
论文以因果推断处理连续低照度增强中的光照分布变化和灾难性遗忘。

## 问题与动机
传统增强模型依赖训练与测试光照分布一致，连续学习不同光照任务时会遗忘旧知识。需要识别混杂因素并学习跨任务不变表示。

## 方法
作者构建结构因果模型，以 backdoor adjustment 减轻混杂影响，提出 Rehearsal-based Invariant Structure Regularizer 扩大可调整变量的取值集合，并设计频域通道机制辅助增强。

## 实验与结果
连续低照度任务实验显示该方法改善跨分布泛化并减轻遗忘。摘要未给出统一指标数字。

## 贡献与局限
贡献是将因果结构引入连续低照度增强。局限是因果假设和回放策略依赖任务分布，真实设备变化和长期任务流仍需验证。

---
DOI: 10.1016/j.neunet.2026.108947
