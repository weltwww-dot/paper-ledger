# Class-based Obfuscation with Multi-objective Evolutionary Algorithms on Source Code 总结

## 基本信息
- **标题**: Class-based Obfuscation with Multi-objective Evolutionary Algorithms on Source Code
- **作者**: Guan-Yan Yang、Tsung-Han Liu、Farn Wang et al.
- **期刊 / 会议**: International Journal of Information Security 2026
- **发表**: 2026-09-23
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01297-z
- **PDF**: [IJIS_2026_MOCCOClassBasedObfuscation.pdf](papers/IJIS_2026_MOCCOClassBasedObfuscation.pdf)

## 一句话概括
MOCCO 将类级源代码变换表述为多目标优化，在提升结构混淆程度与控制执行代价之间搜索折衷方案。

## 问题与动机
代码混淆可增加逆向分析难度，但强结构变换通常带来运行开销，也可能改变程序行为。作者尝试同时兼顾混淆强度、执行成本与功能保持，避免采用单一固定变换。

## 方法
MOCCO 使用多目标进化算法搜索类级变换，以圈复杂度、嵌套结构和 token 相似度等指标近似混淆效果，并纳入成本指标。实验与开源混淆工具比较，并检查变换后程序的功能保持。

## 实验与结果
论文报告 MOCCO 在所用结构代理指标上优于对照工具，运行开销相近或更低，并通过测试集上的功能保持检查。评价以结构和性能代理指标为主，没有直接测量专业逆向人员或自适应分析工具的破解成本。

## 贡献与局限
- 将类级混淆中的强度与成本权衡转化为可搜索的多目标优化问题。
- 进化搜索产生不同折衷解，为开发者提供选择空间。
- 圈复杂度、嵌套度和 token 相似度只是难度代理，不等同于对人类分析或反编译器的真实抵抗力，不能据此宣称已证明安全。

---
DOI: 10.1007/s10207-026-01297-z
