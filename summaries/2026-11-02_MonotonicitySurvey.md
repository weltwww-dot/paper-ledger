# Monotonicity constraints in neural networks: A survey and future directions 总结

## 基本信息
- **标题**: Monotonicity constraints in neural networks: A survey and future directions
- **作者**: Junpeng Sun、Juan Luis Suárez、Weiping Ding、Salvador García
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109832
- **发表**: 2026-11-02
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109832
- **PDF**: [NN_2026_MonotonicitySurvey.pdf](papers/NN_2026_MonotonicitySurvey.pdf)

## 一句话概括
梳理神经网络如何实现单调约束，并以统一协议比较约束保证、预测效果与灵活性的取舍。

## 问题与动机
领域规则有时要求预测随某些输入只增不减或只减不增。架构约束、训练诱导和事后验证给出的保证不同，分散的评估方式也使方法难以横向比较。

## 方法
综述将方法分为结构式与非结构式两类。前者在架构或参数中施加约束，后者通过优化、验证或认证处理单调性，并用统一划分在真实表格数据上比较代表方法。

## 实验与结果
在12个数据集上，无约束MLP平均预测排名最高。多重比较校正后的Nemenyi检验未发现MLP与CoMNN、SMM、UMNN或HLL存在显著差异，简单权重符号约束的MLPwc平均排名最弱（PDF第17、22、25页）。

## 贡献与局限
提供了可复用的分类和比较协议，说明结构设计影响单调约束下的表达能力。未达显著差异不足以判定性能等效，排名还会随数据集与参数配置改变。

---
DOI: 10.1016/j.neunet.2026.109832 | PDF: [NN_2026_MonotonicitySurvey.pdf](papers/NN_2026_MonotonicitySurvey.pdf)
