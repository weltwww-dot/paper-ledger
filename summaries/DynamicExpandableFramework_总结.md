# Dynamic expandable framework for incremental anomaly detection 总结

## 基本信息

- **标题**: Dynamic expandable framework for incremental anomaly detection
- **作者**: Yuxuan Tan, Hongxia Gao, Tongtong Liu, Xiaoqin Wen
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108949
- **arXiv**: 无
- **PDF**: [NN_2026_DynamicExpandableFramework.pdf](papers/NN_2026_DynamicExpandableFramework.pdf)

## 一句话概括

DEF通过特征选择、类别专家隔离和动态路由缓解增量异常检测中的类别干扰与灾难性遗忘。

## 问题与动机

工业产品类别会不断增加，使异常检测模型必须持续学习。共享参数空间容易在新类别加入时覆盖旧知识，导致遗忘和类别间干扰，因此需要能够扩展并隔离类别知识的架构。

## 方法

框架包含历史加权特征选择HWFS、类别特定专家混合层CS-MoE和动态对比路由网络DCRN。HWFS挑选异常敏感通道，CS-MoE为类别分配专用参数，DCRN在推理时选择合适专家；t-SNE用于定性观察解码层的类别分离。

## 实验与结果

在MVTec-AD和VisA上进行实验。在MVTec-AD的“3-3 with 4 steps”设置中，DEF相对领先方法使ACC提高4.8%，FM降低2.15；训练计算量为3.52G FLOP、内存为4400MB。

## 贡献与局限

贡献是把显式类别解耦与动态专家选择用于增量异常检测，并同时关注遗忘和效率。局限是实验依赖工业异常基准及设定，新增类别规模、路由错误和真实生产流变化下的长期稳定性仍需评估。

---
DOI: 10.1016/j.neunet.2026.108949
