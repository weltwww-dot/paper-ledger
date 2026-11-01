# Transductive Learning via Validation Risk Minimization for Semi-supervised Learning 总结

## 基本信息
- **标题**: Transductive Learning via Validation Risk Minimization for Semi-supervised Learning
- **作者**: Yan Lv、Zhen Wang、Lan Bai
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109803
- **发表**: 2026-10-26
- **日期来源**: 出版社正式PDF的Available online；2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109803
- **PDF**: [NN_2026_ValidationRiskTransduction.pdf](papers/NN_2026_ValidationRiskTransduction.pdf)

## 一句话概括
将验证风险最小化用于直推学习，以验证集或交叉验证约束未标注样本的候选标签分配。

## 问题与动机
标注样本过少时，训练误差低不代表未标注样本分类可靠，低密度分割等先验也可能失效。研究目标是预测已知的未标注样本集合，不能直接等同于对任意未来样本的泛化。

## 方法
提出验证集框架TLFVS和交叉验证框架TLFCV，把标签推断写为双层优化。以内层最小二乘支持向量机的解析结构，将具体实例化问题化为线性或二次整数规划，并设计相应求解方法。

## 实验与结果
十个UCI基准中TLFCV-LSSVM平均排名2.65，优于DIFFormer的3.00，但两者差异未达Holm校正显著性。PCam的2,000图像子集上准确率78.18%；所报分类时间不含预提取特征成本，不能与完整ResNet微调时间直接作端到端比较（PDF第8页）。

## 贡献与局限
将验证原则引入候选标签优化，交叉验证版本兼顾稳定性但代价更高。结果并非全面支配全部基线；当前依赖LSSVM的可处理结构，推广到无解析解的学习器及大规模双层整数问题仍有计算挑战。

---
DOI: 10.1016/j.neunet.2026.109803 | PDF: [NN_2026_ValidationRiskTransduction.pdf](papers/NN_2026_ValidationRiskTransduction.pdf)
