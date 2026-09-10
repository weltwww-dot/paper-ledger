# Fast sparse supervised learning framework with BLinex loss function 总结

## 基本信息

- **标题**: Fast sparse supervised learning framework with BLinex loss function
- **作者**: Tiantian Jiang、Guolin Yu、Jun Ma
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108843
- **arXiv**: 无
- **PDF**: [NN_2026_PBLTELM_SparseBlinexLearning.pdf](papers/NN_2026_PBLTELM_SparseBlinexLearning.pdf)

## 一句话概括

PBLTELM 将 BLinex 鲁棒损失、Lp 稀疏约束和 Adam 优化结合，用于快速的大规模分类。

## 问题与动机

相对大规模分类任务需要同时具备准确性、抗噪性和计算效率。传统极限学习机或孪生模型可能产生稠密解、对异常值敏感，非凸非光滑优化还会增加求解难度。研究希望在保持可扩展性的同时获得稀疏模型。

## 方法

作者提出 Lp-norm sparse Blinex Twin Extreme Learning Machine（PBLTELM）。Blinex loss 用于增强鲁棒性，0<p<1 的 Lp 约束近似 L0 稀疏解，双层优化结合迭代权重更新和 Adam 算法处理非凸非光滑问题。理论部分分析局部驻点收敛。

## 实验与结果

实验覆盖二维人工数据集、CMU facial expression、12 个 UCI 数据集和 7 个较大规模 libsvm 数据集。结果显示，PBLTELM 相比 state-of-the-art 方法在分类准确率和计算速度上均有统计显著改进。

## 贡献与局限

贡献是把鲁棒损失、稀疏建模和无需矩阵求逆的 Adam 优化组合成可扩展框架。局限是非凸优化只保证局部性质，参数选择、类别不平衡和超大规模在线数据下的性能仍需进一步评估。

---
DOI: 10.1016/j.neunet.2026.108843
