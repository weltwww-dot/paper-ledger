# CRP-MIL: A channel re-partitioning based multiple instance learning method for whole slide image classification 总结

## 基本信息
- **标题**: CRP-MIL: A channel re-partitioning based multiple instance learning method for whole slide image classification
- **作者**: Yining Xie、Wenchao Yin、Zequn Liu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109786
- **发表**: 2026-10-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109786

## 一句话概括
CRP-MIL通过通道重分区与两级注意力协同建模局部和全局信息，改善仅有切片级标签的病理全切片分类。

## 问题与动机
病理全切片被拆成大量图块后，常规多实例学习容易忽略邻域关联，整体语义也难以充分聚合；论文探索能否从特征通道组织入手，补足以图块关系为主的建模方式。

## 方法
将图块特征均分为四个通道子空间，三个子空间经不同尺度窗口的IN-CRSA建模，另一个保留原始信息；CCIM以共享记忆槽交换跨区域信息，再用门控注意力聚合和子空间加权完成分类。

## 实验与结果
在Camelyon16、TCGA-NSCLC和TCGA-BRCA上比较ABMIL、TransMIL、RRT-MIL等。使用ResNet-50特征时，CRP-MIL在前两组数据上的AUC分别为97.19±1.22%和96.03±1.33%，RRT-MIL分别为96.08±2.13%和95.88±1.28%。CRP-MIL在BRCA上的AUC为92.49±1.41%。三组数据分别使用三折、五折、五折交叉验证，结果为均值±标准差。

## 贡献与局限
贡献是可接入既有特征提取流程的通道维局部—全局协同机制。不过，CTransPath实验中对若干强基线的差异不显著；重排后的二维邻域并非真实组织空间拓扑，跨更多病理场景的泛化仍待验证。

---
DOI: 10.1016/j.neunet.2026.109786
