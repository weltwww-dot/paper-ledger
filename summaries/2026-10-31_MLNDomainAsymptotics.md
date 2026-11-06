# Domain size asymptotics for Markov logic networks 总结

## 基本信息
- **标题**: Domain size asymptotics for Markov logic networks
- **作者**: Vera Koponen
- **期刊 / 会议**: Artificial Intelligence 2026
- **卷期 / 文章号**: 362（2027），文章号104648
- **发表**: 2026-10-31
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104648
- **PDF**: [AIJ_2026_MLNDomainAsymptotics.pdf](papers/AIJ_2026_MLNDomainAsymptotics.pdf)

## 一句话概括
分析关系域增大时马尔可夫逻辑网络的分布极限，并用反例刻画其与提升贝叶斯网络的表达差异。

## 问题与动机
在有限域上调整软约束权重得到的直觉，未必适用于对象数持续增长的关系模型。理解这种差异有助于判断固定权重能否跨域大小复用。

## 方法
在受限的一阶语言中分析结构分布的极限，比较无量词马尔可夫逻辑网络与提升贝叶斯网络，并研究单一一元谓词的典型比例如何依赖权重。

## 实验与结果
理论结果给出了两类模型不能彼此普遍模拟的反例。在文中的特定图约束下，固定域大小后把权重推至无穷可使约束满足概率趋于1；固定有限权重后扩大域，满足概率则趋于0（PDF第1、18页）。

## 贡献与局限
分清了权重极限与域大小极限，并给出表达能力比较。结论依赖文中的语言、公式及权重条件，不能直接推广到任意逻辑语法和训练任务。

---
DOI: 10.1016/j.artint.2026.104648 | PDF: [AIJ_2026_MLNDomainAsymptotics.pdf](papers/AIJ_2026_MLNDomainAsymptotics.pdf)
