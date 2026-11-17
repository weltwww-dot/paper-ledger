# Mitigating unreliable syntactic dependencies in aspect-based sentiment analysis via sentiment-aware graph anomaly detection and mix convolution 总结

## 基本信息
- **标题**: Mitigating unreliable syntactic dependencies in aspect-based sentiment analysis via sentiment-aware graph anomaly detection and mix convolution
- **作者**: Jiawen Wang、Zhaojian Cui、Haokai Gao 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109490
- **发表**: 2026-08-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109490

## 一句话概括
SAGAM 通过情感一致性图去噪和多跳边特征卷积改善方面级情感分类，在三个公开数据集上优于消融版本，但全局情感约束过强会削弱局部极性变化建模。

## 问题与动机
如何减轻依存句法图中的无关边干扰，并捕捉方面词与观点词之间跨多条边的情感联系？

## 方法
先用图异常检测及情感一致性评价筛除误导性依存关系，再以融合多跳传播和边特征的混合卷积聚合局部与远距离语义。

## 实验与结果
在 Restaurant14、Laptop14 和 Twitter 三个数据集上评估准确率与宏 F1，并进行模块消融；完整模型分别取得 88.02/82.66、82.28/79.43、78.88/78.08 的准确率/宏 F1，移除去噪或混合卷积后均下降；过强一致性约束会降低表现（PDF 第7–10页）。

## 贡献与局限
将情感导向的图清理与多跳边融合结合，改善依存结构噪声下的方面级情感判断；验证范围限于三个基准，情感一致性约束需避免抹平句内极性转折。

---
DOI: 10.1016/j.neunet.2026.109490
