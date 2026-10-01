# Benchmarking post-processing methods in local differential privacy for utility and adversarial robustness 总结

## 基本信息
- **标题**: Benchmarking post-processing methods in local differential privacy for utility and adversarial robustness
- **作者**: Alireza Khodaie、Berkay Kemal Balioglu、M. Emre Gursoy
- **期刊 / 会议**: Computers & Security 2026（在线发表；正式版卷期标注 2027）
- **发表**: 2026-09-25
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105166
- **PDF**: [COSE_2026_BenchmarkingPostProcessingMethodsLocal.pdf](papers/COSE_2026_BenchmarkingPostProcessingMethodsLocal.pdf)

## 一句话概括
LDP3+ 系统比较本地差分隐私统计的后处理方法，研究它们何时能改善统计效用和攻击鲁棒性。

## 问题与动机
隐私噪声会损害频率与排序估计，但现有后处理方案缺少跨协议、数据分布及攻击场景的统一评估。某种方法在一个指标上有效，并不代表能在不同隐私预算下持续胜出。

## 方法
平台以模块化、多线程方式组合 6 种 LDP 协议、7 种后处理方法和 3 类攻击，同时评估频率误差、排序保持及对抗指标。研究改变隐私预算、取值域和数据分布，区分普通效用、投毒、预算推断与纵向观察的影响。

## 实验与结果
实验使用 Adult、Kosarak、BMS-POS 及三类合成数据。Norm-Sub 和 Norm-Mul 通常较适合频率估计，Norm-Cut 在多数排序场景占优，但没有普遍最优的方法。后处理可间接缓解部分投毒与预算推断攻击，却对依赖重复用户观察的纵向攻击保护有限。

## 贡献与局限
贡献是提供可扩展的联合效用与对抗评测平台，并解释选择后处理方法时的任务依赖。结果受协议、预算、数据特征和指标影响；改善统计误差或部分攻击指标不能理解为增强了原有隐私保证，也不能替代针对纵向攻击的防护。

---
DOI: 10.1016/j.cose.2026.105166
