# DPAC: A tri-dimensional coordinated framework for breaking the efficiency ceiling in parameter-efficient fine-tuning 总结

## 基本信息
- **标题**: DPAC: A tri-dimensional coordinated framework for breaking the efficiency ceiling in parameter-efficient fine-tuning
- **作者**: Cheng Wang、Quan Wen、Yujian Huang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109524
- **发表**: 2026-08-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109524

## 一句话概括
DPAC 联合参数预算分配、权重分量协作和渐进调度，提升视觉语言模型参数高效微调的利用效率。

## 问题与动机
PEFT 方法常孤立优化低秩结构，未协调不同层预算、分解权重分量间合作及训练阶段适配，导致参数数目相同但利用效率不一。

## 方法
框架包含依赖感知秩分配 DARA、幅值与方向协同强化 MACR，以及渐进协调调度 PCR；按下游影响分配层预算，以相关性目标协调分量更新，再逐阶段加强协作，形成三维联合优化。

## 实验与结果
在 CLIP、BLIP 的 Flickr30k 与 MSCOCO 视觉语言检索基准上评估。消融显示三组件完整组合效率为 91.7%，高于任意两组件组合；分阶段目标相关性示例在 λbase=0.01 时达到目标 −0.50，DPAC 的 R@1 为 85.5%，固定策略为 84.3% 和 84.5%。

## 贡献与局限
贡献在于将预算分配、分量协作和训练调度作为耦合问题处理，并提供组件交互的实验与理论分析。指标“效率”依赖论文定义；实验集中于检索任务和指定骨干，不能直接推断所有大模型微调任务均获同幅收益。

---
DOI: 10.1016/j.neunet.2026.109524
