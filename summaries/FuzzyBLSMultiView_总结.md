# Fuzzy-driven broad learning system with class probability and density awareness for multi-view data 总结

## 基本信息

- **标题**: Fuzzy-driven broad learning system with class probability and density awareness for multi-view data
- **作者**: M. Tanveer, M. Pathak, M. Sajid, A. Quadir, Priyamvada
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108914
- **arXiv**: 无
- **PDF**: [NN_2026_FuzzyBLSMultiView.pdf](papers/NN_2026_FuzzyBLSMultiView.pdf)

## 一句话概括

CPBS-MvBLS用同时依赖类别概率和不平衡率的钟形模糊权重抑制噪声与离群点，并融合多视图互补信息。

## 问题与动机

BLS以随机权重和伪逆训练降低深度模型成本，但把所有样本等权处理，容易受离群点、标签噪声和类别不平衡影响。单视图鲁棒模型又无法利用复杂数据中的互补视角。

## 方法

CPBS-BLS为每个样本计算基于类别概率和不平衡率的自适应钟形隶属度，在密集可靠区域提高权重，在稀疏噪声区域降低影响。CPBS-MvBLS保留该加权机制并联合多视图特征，使决策边界同时利用样本可靠性和视图互补性。

## 实验与结果

实验覆盖UCI、KEEL和AwA基准。CPBS-BLS在单视图中提高鲁棒性，CPBS-MvBLS在多视图场景中进一步利用互补信息；论文报告其在准确率、抗噪和不平衡处理方面持续优于基线，并经统计显著性检验支持。

## 贡献与局限

贡献是把模糊隶属、类别概率、密度/不平衡意识与BLS多视图学习结合。局限是概率估计和隶属函数形状会影响权重，极端类别比例、缺失视图和超大规模多视图数据仍需验证。

---
DOI: 10.1016/j.neunet.2026.108914
