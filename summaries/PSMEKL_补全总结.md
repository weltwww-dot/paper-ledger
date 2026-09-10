# PSMEKL: Positional and structural multiple empirical kernel learning for node embedding 总结

## 基本信息
- **标题**: PSMEKL: Positional and structural multiple empirical kernel learning for node embedding
- **作者**: Zonghai Zhu, Xinshuai Wei, Huanlai Xing, Li Feng, De Chen, Yuge Xu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108898
- **PDF**: [NN_2026_PSMEKL.pdf](papers/NN_2026_PSMEKL.pdf)

## 一句话概括
PSMEKL 通过多经验核学习同时编码节点位置关系和全局结构，兼容属性图与非属性图。

## 问题与动机
传统 GNN 难以同时捕获 positional 与 structural information，已有节点嵌入方法也常只适用于一种图类型。需要统一的结构—位置表示。

## 方法
模型结合 kernel mapping 与 community detection，构造多个经验核表达位置关系和全局结构，并通过专门准则优化节点嵌入，服务于下游节点任务。

## 实验与结果
属性图和非属性图基准实验显示 PSMEKL 具有有效的嵌入和下游任务表现。摘要未列出具体数值。

## 贡献与局限
贡献是统一位置—结构多核嵌入。局限是核函数和社区发现质量会影响结果，大规模动态图与噪声边场景仍需评估。

---
DOI: 10.1016/j.neunet.2026.108898
