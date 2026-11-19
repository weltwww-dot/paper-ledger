# Improving cross-architecture black-box adversarial transferability via hybrid structure-aware feature perturbations 总结

## 基本信息
- **标题**: Improving cross-architecture black-box adversarial transferability via hybrid structure-aware feature perturbations
- **作者**: Qirui Lu、Liansong Zong、Furan Liu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109535
- **发表**: 2026-08-20
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109535

## 一句话概括
论文研究如何通过结构感知的特征扰动提升黑盒对抗样本跨架构迁移性，重点改善视觉Transformer生成扰动迁移至卷积网络时容易衰减的问题。

## 问题与动机
迁移式黑盒鲁棒性评估依赖替代模型生成的扰动能否影响未知目标模型。既有方法多优化扰动方向，却较少控制其空间组织及跨网络层级的分配；ViT与CNN特征归纳偏置不同，ViT产生的碎片化扰动可能被CNN局部聚合和平滑。

## 方法
作者提出混合的结构感知特征扰动策略，在特征空间共同考虑扰动位置、连通结构和随网络深度变化的强度，并以空间特征度量（含Moran's I）刻画扰动空间相关性。设计目标是使扰动保留对分类有影响的结构线索，并提高从ViT替代模型到CNN目标模型的跨架构可迁移性。

## 实验与结果
实验覆盖ViT到ViT、ViT到CNN迁移，多个替代/目标模型组合，并加入消融、参数敏感性、输入变换防御和与现有迁移策略兼容性分析。作者报告方法在多数模型组合上获得最佳或相当的攻击成功率，平均迁移表现提升在ViT到CNN这一较难场景尤为明显；但并非每个ViT到ViT目标都胜过基线，近似架构配对仍可能使其他方法有竞争力。

## 贡献与局限
工作把扰动的空间结构和网络归纳偏置纳入迁移性设计，为跨架构模型的黑盒鲁棒性评估提供一种分析路径。结果是基准上的攻击成功率评估，不等同于真实系统风险的直接估计；不同架构配对的收益并不均匀，且输入压缩等防御会影响表现。

---
DOI: 10.1016/j.neunet.2026.109535
