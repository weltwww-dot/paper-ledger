# Causal discovery by continuous optimization with weighted superstructure 总结

## 基本信息
- **标题**: Causal discovery by continuous optimization with weighted superstructure
- **作者**: Mingjie Chen, Yewei Xia, Hao Zhang, Ruxin Wang, Yuzhong Peng, Jihong Guan, Shuigeng Zhou
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108974
- **PDF**: [NN_2026_CausalDiscoveryWeightedSuperstructure.pdf](papers/NN_2026_CausalDiscoveryWeightedSuperstructure.pdf)

## 一句话概括
论文把低阶条件独立信息构造成加权 superstructure，并将其嵌入连续优化因果发现以改善少样本和异质噪声表现。

## 问题与动机
连续优化方法在高维、少样本和异质噪声中容易保留假边。约束式 CI 信息更稳健，但需要可靠地注入连续优化而不破坏其求解过程。

## 方法
作者使用 0 阶和 1 阶 CI 测试构造加权 superstructure，从中得到 WIC/WIR 约束，并给出受约束优化的收敛保证；约束用于抑制不可信边。

## 实验与结果
合成和真实数据实验显示方法改善连续优化因果发现，尤其在低样本情形；非线性实验中相对 DAG-GNN 的 SHD 降幅最高报告为 69.54%。

## 贡献与局限
贡献是把可靠低阶 CI 信息转为连续优化约束。局限是有限样本 Type II error 可能误删真实边，复杂稠密图上高阶测试的代价和稳定性仍需权衡。

---
DOI: 10.1016/j.neunet.2026.108974
