# Data-Centric Challenges, Techniques, and Impacts: A Survey on Image Data Perturbation 总结

## 基本信息

- **标题**: Data-Centric Challenges, Techniques, and Impacts: A Survey on Image Data Perturbation
- **作者**: Peng-Fei Zhang, Guangdong Bai, Xin-Shun Xu, Zi Huang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering · 2026
- **发表**: 2026-08-07
- **日期来源**: openalex-publication-date，保留来源精度；预印本日期不替代期刊发表时间
- **内容状态**: 完整 · 已对照现有PDF审校中文六段式；版本按本条记录
- **研究方向**: 信息安全
- **DOI**: 10.1109/tkde.2026.3709786
- **版本**: 出版社正式正文（含内容已定稿的Early Access）
- **PDF**: [TKDE_2026_DataCentricChallengesTechniques.pdf](papers/TKDE_2026_DataCentricChallengesTechniques.pdf)

## 一句话概括

这篇综述以图像数据扰动为主线，统一梳理扰动生成、攻击与防御及其对深度模型鲁棒性的影响。

## 问题与动机

真实图像会受压缩、传感器误差、环境变化和恶意干预影响，而既有综述常局限于单一攻击、防御或模型。需要从数据出发解释不同扰动为何导致失效，又怎样用于增强鲁棒性。

## 方法

按生成过程是否显式优化目标，将方法分为启发式扰动和优化引导扰动，分析两者的互补关系。再串联推理逃逸、训练投毒与后门、数据增强、随机平滑及对抗训练，讨论跨模型迁移、黑盒查询、物理部署和准确率—鲁棒性权衡。

## 实验与结果

本文没有提出新模型或开展统一的新训练对比，成果是分类与策略对照、代表性基准汇总及文献证据分析。作者指出现有评估偏重合成扰动，真实分布变化、复合扰动、跨训练与部署阶段以及行为指标覆盖仍不足；不能把所引研究的结果当成本篇独立实验。

## 贡献与局限

贡献是把扰动揭示脆弱性与增强鲁棒性的双重作用放入统一框架，并比较数字和物理场景下的攻击、防御与成本。主体集中于图像分类，向其他任务和模态推广仍有限；基准真实性、多扰动联合评估及大规模计算成本是开放问题。

---
DOI: 10.1109/tkde.2026.3709786 | PDF: [TKDE_2026_DataCentricChallengesTechniques.pdf](papers/TKDE_2026_DataCentricChallengesTechniques.pdf)
