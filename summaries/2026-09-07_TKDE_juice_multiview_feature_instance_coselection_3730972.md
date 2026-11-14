# Joint Learning of Unsupervised Multi-View Feature and Instance Co-Selection With Cross-View Imputation 总结

## 基本信息
- **标题**: Joint Learning of Unsupervised Multi-View Feature and Instance Co-Selection With Cross-View Imputation
- **作者**: Yuxin Cai、Yanyong Huang、Jinyuan Chang 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(11)，7598-7609
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3730972

## 一句话概括
不完整多视图数据中，先插补再筛选会割裂缺失恢复、特征选择和样本选择；简单拼接也会丢失视图互补关系。JUICE 在统一框架中联合处理三者，并以跨视图信息改善插补和共同筛选。

## 问题与动机
能否让被选择的样本关系反过来帮助缺失视图重建，并与特征筛选共同优化？

## 方法
JUICE 联合重建缺失视图、挑选信息特征与代表样本；再利用视图内外关系增强选择，交替优化各模块，并用分类准确率和 F1 衡量选择质量。

## 实验与结果
作者在八个数据集上与多种方法比较 ACC、F1，并报告消融结果：完整 JUICE 整体优于移除跨视图增强等变体；COIL 可视化中选取 20% 特征、30% 样本后，类别簇呈较清晰分离（PDF 第 9–11 页）。结果依赖聚类式评价和基准数据，实际缺失机制未必符合其视图关系假设（PDF 第 2 页）。

## 贡献与局限
把跨视图插补与无监督特征—样本共选择纳入同一学习过程，实验显示各组件对基准表现均有贡献。对真实世界缺失机制的适应性尚不能由这些数据集保证，且可视化分离不等同于下游任务收益。

---
DOI: 10.1109/tkde.2026.3730972
