# Enhanced multi-agent interaction modeling with differential transformers for trajectory prediction 总结

## 基本信息
- **标题**: Enhanced multi-agent interaction modeling with differential transformers for trajectory prediction
- **作者**: Minghui Wei、Haimin Zhang、Stuart Perry 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109491
- **发表**: 2026-08-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109491
- **PDF**: [NN_2026_differential-transformer-trajectories_109491.pdf](papers/NN_2026_differential-transformer-trajectories_109491.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
本文提出差分 Transformer，通过显式编码个体状态与交互上下文的差异，提升多主体轨迹预测对复杂交互和多模态运动的建模能力。

## 问题与动机
标准自注意力聚合上下文时，个体自身信息与其他主体信息的贡献不易区分，层间可能累积信息损失；研究检验显式差分编码能否改善预测。

## 方法
在局部主体编码和全局交互编码中加入差分编码，将 token 自身表示与上下文表示之差并入更新特征，并以解码器生成多模态轨迹；该模块可并行集成到 Transformer。

## 实验与结果
在 Argoverse 1 与 Argoverse 2 上与既有预测模型比较，并进行组件消融；Argoverse 1 的 K=6 设置中，minFDE/minADE/MR 分别为 1.1142/0.7536/0.1055，完整差分编码优于不含差分编码的消融配置。结果限于两个基准数据集，尚不能据此推断真实部署表现（PDF 第 7–8 页）。

## 贡献与局限
结果支持在局部与全局交互层显式保留主体—上下文差异有助于轨迹预测；研究同时报告了 Argoverse 2 上的稳定收益，但证据范围仍是离线基准评测。

---
DOI: 10.1016/j.neunet.2026.109491 | PDF: [NN_2026_differential-transformer-trajectories_109491.pdf](papers/NN_2026_differential-transformer-trajectories_109491.pdf)
