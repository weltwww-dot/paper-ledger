# Fisher-Rao guided channel pruning with progressive re-estimation 总结

## 基本信息
- **标题**: Fisher-Rao guided channel pruning with progressive re-estimation
- **作者**: Xinjian Xiang、Mingjun Lin、Yongping Zheng 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109455
- **发表**: 2026-08-03
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109455

## 一句话概括
该方法按归一化 Fisher-Rao 通道分数分阶段剪枝并在每阶段重估重要性，在多个网络上实现不同程度的参数与计算削减，但准确率变化明显依赖骨干网络。

## 问题与动机
一次性通道剪枝忽略结构删减后通道重要性会改变的问题，如何在给定压缩预算下逐步删减并降低重要性估计失配？

## 方法
方法以门控通道的归一化 Fisher-Rao 分数评估重要性，每阶段按层移除低分通道，短暂微调后重新估分；当预算以参数量表示时先搜索对应剪枝比例。作者也讨论残差分支间依赖可能使局部重要性判断失准。

## 实验与结果
在 CIFAR-10 与 ImageNet、七种骨干网络上评估；主流程表中 ResNet-56 参数/FLOPs 保留 71.0%/56.2%，Top-1 从 93.34% 变为 93.85%，而 EfficientNet-B0 保留 77.2%/50.4% 时 Top-1 从 77.10% 降至 75.90%，显示收益并非跨骨干一致（PDF 第 7–9 页）。

## 贡献与局限
提出逐阶段重估的 Fisher-Rao 结构化剪枝流程，并通过多架构结果明确展示压缩与精度的骨干相关权衡；残差分支依赖和更广泛部署条件仍需进一步建模与验证。

---
DOI: 10.1016/j.neunet.2026.109455
