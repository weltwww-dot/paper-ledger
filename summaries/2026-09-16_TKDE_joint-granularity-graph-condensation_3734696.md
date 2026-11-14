# Heterogeneous Graph Condensation via Joint-Granularity Gradient Matching 总结

## 基本信息
- **标题**: Heterogeneous Graph Condensation via Joint-Granularity Gradient Matching
- **作者**: Shenao Yu、Fenglin Cen、Ji Xu 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8250-8263
- **发表**: 2026-09-16
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3734696

## 一句话概括
JGGM针对异构图数据压缩，提出联合粒度梯度匹配以生成小型代表图，在显著压缩数据规模时尽量保留节点分类和链接预测所需的结构与语义信息。

## 问题与动机
现有异构图凝缩可能损失语义结构，超节点初始化也会限制表示质量；极低压缩率下，如何让小图仍支持有效下游训练？

## 方法
方法采用两阶段梯度匹配，并以 leading tree 初始化超节点；评估覆盖不同图神经网络骨干、压缩率和迁移设置，同时分析存储与训练时间。

## 实验与结果
在六个异构图基准上测试；链接预测压缩率 r=0.01 时，JGGM 在各数据集均优于 GCond 与 HGCond，部分设置的压缩图仍达到原图准确率的 90% 以上。DBLP 存储从 242.50 MB 降至约 30%–50%；DBLP 上方法耗时 90.80 秒，高于 GCond 的 21.93 秒（PDF 第 13 页）。

## 贡献与局限
结果表明压缩后可保留较强任务效用并减少存储，初始化策略尤其关键。凝缩阶段计算成本偏高，文中亦指出超参数与下游评测耗时；收益依赖数据集、压缩率和评测模型，尚不能据此断言普遍适用。

---
DOI: 10.1109/tkde.2026.3734696
