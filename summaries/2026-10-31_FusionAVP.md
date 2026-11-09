# FusionAVP: A cross-attention-based heterogeneous feature fusion and contrastive learning strategy for antiviral peptide identification 总结

## 基本信息
- **标题**: FusionAVP: A cross-attention-based heterogeneous feature fusion and contrastive learning strategy for antiviral peptide identification
- **作者**: Aoyun Geng、Jinwei Wang、Chunyan Cui 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109845
- **发表**: 2026-10-31
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109845
- **PDF**: [NN_2026_FusionAVP.pdf](papers/NN_2026_FusionAVP.pdf)

## 一句话概括
将蛋白语言模型表征与人工设计的序列特征融合，用于筛选候选抗病毒肽。

## 问题与动机
蛋白语言模型能从氨基酸序列学习上下文，传统特征则显式编码理化性质和组成。直接拼接容易忽略两类信息在残基层面的对应关系，限制它们的互补作用。

## 方法
FusionAVP对齐ESM-2残基嵌入和传统特征，用交叉注意力学习两路特征的相互关系。再通过对比学习拉近同一样本的不同融合视图，分开其他样本，最后对肽序列分类。

## 实验与结果
在同一独立测试集上用10个随机种子重复实验，FusionAVP整体优于多种基线。各次运行仍有124至132个假阳性和28至35个假阴性。消融比较了特征融合方案，个案的注意力分布与部分已报道功能位点一致（PDF第6–9页）。

## 贡献与局限
为生物序列分类提供了可复用的异构特征融合方法。计算筛选可为实验确定优先级，但候选序列的抗病毒活性仍需实验验证，注意力与位点的对应也需要更多结构及突变数据检验。

---
DOI: 10.1016/j.neunet.2026.109845 | PDF: [NN_2026_FusionAVP.pdf](papers/NN_2026_FusionAVP.pdf)
