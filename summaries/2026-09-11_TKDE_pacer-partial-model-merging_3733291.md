# Rethinking Model Merging: Partial Merging via Conflict Mitigation and Adaptive Weighting 总结

## 基本信息
- **标题**: Rethinking Model Merging: Partial Merging via Conflict Mitigation and Adaptive Weighting
- **作者**: Haoyu Chen、Tiantong Wang、Yidong Li 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8470-8484
- **发表**: 2026-09-11
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3733291

## 一句话概括
PACER提出冲突缓解与自适应加权的部分模型合并方法，目标是在整合多个任务模型时保留任务能力，避免全量合并造成的参数干扰和性能退化。

## 问题与动机
直接合并独立微调模型可能因参数冲突损害单任务表现，静态权重也难照顾不同任务；如何选择应合并参数并抑制极端冲突？

## 方法
方法先自动筛选任务相关参数以压缩合并范围，再通过正则化与冲突缓解、适应性权重形成合并模型；作者还分析参数暴露带来的隐私风险，并明确该方案不等同形式化差分隐私。

## 实验与结果
实验覆盖视觉模型八项任务及语言模型多项自然语言推断任务，在不同架构与客户端设置下与合并基线比较；ViT-B/32 设置报告 PACER 准确率 78.3%，多项结果显示其精度和效率具竞争力（PDF 第 8 页）。

## 贡献与局限
贡献在于把部分选择、冲突控制和任务加权结合，提升多任务合并的适应性。评测集中于所选模型、数据集和任务组合，且参数保护不能替代正式隐私保证，其他规模与分布下仍需验证。

---
DOI: 10.1109/tkde.2026.3733291
