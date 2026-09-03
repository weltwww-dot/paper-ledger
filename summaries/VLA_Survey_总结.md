# A Survey on Vision-Language-Action Models for Embodied AI 总结

## 基本信息

- **标题**: A Survey on Vision–Language–Action Models for Embodied AI
- **研究方向**: 人工智能
- **作者**: Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao 等 (et al.)
- **期刊 / 会议**: IEEE TNNLS 2026
- **DOI**: 10.1109/tnnls.2025.3650584
- **arXiv**: 2405.14093
- **PDF**: [TNNLS_2026_VLA_Survey.pdf](papers/TNNLS_2026_VLA_Survey.pdf)
- **资源仓库**: https://github.com/yueen-ma/Awesome-VLA

## 一句话概括

第一篇系统梳理 vision-language-action (VLA) 模型的综述：提出「组件 → 低级控制策略 → 高级任务规划器」三线分类法，并汇总数据集、仿真器与基准资源。

## 问题与动机

具身 AI 被视为通向 AGI 的基石，需要控制智能体在物理世界中完成语言条件化任务。LLM 与 VLM 的成功催生了能直接生成动作的 VLA 模型，但该领域发展极快、文献分散，缺少一份能帮助研究者把握全貌的系统梳理。

## 方法

三线分类法：第一条线聚焦 VLA 的个体组件（backbone、表征与动作 token 化等）；第二条线是能预测低级动作的 VLA 控制策略；第三条线是能把 long-horizon 任务分解为子任务序列的高级任务规划器。综述同时整理相关数据集、仿真器与基准，并维护公开资源仓库 Awesome-VLA。

## 实验与结果

综述性论文，无新实验。其「结果」体现为结构化的分类体系与资源清单：覆盖三条研究线的代表性方法，以及数据集、仿真器、基准的整理（原文以资源梳理为主，未给出量化对比）。

## 贡献与局限

- 贡献一：首个 VLA 综合综述与三线分类框架，为快速演进的领域提供地图。
- 贡献二：持续维护的 Awesome-VLA 资源仓库，降低入门与对比成本。
- 局限：领域变化极快，覆盖内容会迅速过时；数据稀缺与不一致是当前主要挑战，未来方向包括世界模型（预测未来状态）与模型自我改进等（原文列举）。

---

DOI: 10.1109/tnnls.2025.3650584
