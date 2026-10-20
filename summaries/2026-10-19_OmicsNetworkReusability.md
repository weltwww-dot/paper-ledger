# Reusability report: multi-sample omics network inference operates in distinct robustness regimes defined by prior knowledge and data availability 总结

## 基本信息
- **标题**: Reusability report: multi-sample omics network inference operates in distinct robustness regimes defined by prior knowledge and data availability
- **作者**: Xabier Martínez-de-Morentin、Sumeer A. Khan、Itziar Cenzano 等
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **卷期 / 页码**: 8，1616—1631
- **发表**: 2026-10-19
- **日期来源**: 正式PDF首页Published online及Crossref published-online一致
- **文献类型**: Reusability report；正式版标为Article，含复现、扩展实验与方法改进
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01311-y
- **PDF**: [NMI_2026_OmicsNetworkReusability.pdf](papers/NMI_2026_OmicsNetworkReusability.pdf)

## 一句话概括
复现并扩展CORNETO，说明多样本组学网络联合推断的稳定性收益取决于先验完整度、数据量与生物异质性，并检验两种稳健化策略。

## 问题与动机
不同调控网络可能解释同一组观测数据，预测准确并不保证找到了真实调控机制。作者关注何时联合推断更稳定，以及过强正则化和剪枝何时损失细胞特异信息，而非宣称发现新的因果网络。

## 方法
复现原框架，并在造血分化与成人皮层单细胞数据上评估iMAT、KPNN、Steiner tree及CARNIVAL，各自沿用适合该任务的指标而不混成统一排名。系统改变正则化、先验网络完整度与条件数，再引入bootstrap聚合和选择性重新扩展，以恢复稳定结构及被过度剪枝丢失的信息。

## 实验与结果
联合推断主要改善稳定性，未在所有任务和生物情境下一致提高预测表现。造血KPNN剪枝后重新加入被排除的100个高信息量基因，准确率从0.576升至0.906、macro F1从0.424升至0.848，边数也从267增至11,924；先验网络仅保留20%时，iMAT各次运行均未产生活跃反应（PDF第6页）。这些指标不是对真实因果相互作用的独立验证。

## 贡献与局限
将复现、受控扰动和结果级修正结合，给出按数据条件选择联合推断与正则化的实践依据。动态和相对稳定情境各仅一个数据集，结论是案例支持的假设而非所有组织的普遍规律；缺少完整实验真值，重采样重复也不是生物重复，大规模混合整数优化仍有计算瓶颈（PDF第7—8、13—14页）。

---
DOI: 10.1038/s42256-026-01311-y | PDF: [NMI_2026_OmicsNetworkReusability.pdf](papers/NMI_2026_OmicsNetworkReusability.pdf)
