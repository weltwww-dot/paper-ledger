# Body-decoupled grounding via reduction: A novel approach on the Asp bottleneck 总结

## 基本信息
- **标题**: Body-decoupled grounding via reduction: A novel approach on the Asp bottleneck
- **作者**: Viktor Besin、Markus Hecher、Matthias König 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-08-11
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104600
- **PDF**: [AIJ_2026_BodyDecoupledGroundingReductionApproach.pdf](papers/AIJ_2026_BodyDecoupledGroundingReductionApproach.pdf)

## 一句话概括
论文提出 body-decoupled grounding，将规则体中的原子分开处理，以降低 Answer Set Programming（ASP）非地面规则实例化时的组合爆炸，并给出面向多类逻辑程序的正确性与复杂度结果。

## 问题与动机
ASP 求解前须把变量规则实例化为地面程序；变量、取值域及规则体规模增大时，传统方法可能产生难以处理的程序。作者聚焦于规则体较长、密集的情形，尝试通过翻译绕开这一 grounding bottleneck，同时保留成熟地面器与求解器可继续使用的工作流。

## 方法
核心是把不同 body atom 的变量实例化工作解耦，通过归约生成地面析取程序；对非紧致、正规及析取程序，分别加入 foundedness、排序或 epistemic logic 等编码机制。作者证明在谓词元数有界时，生成规模关于域大小为多项式；开源原型 newground 实现了面向非地面 tight 程序的优化归约，并允许只对指定规则采用新方法、其余仍交给传统地面器。

## 实验与结果
原型在五类基准上与 gringo、idlv 比较地面程序大小、grounding 时间及总求解表现，测试包含不同规模与密度的图实例及 stable-marriage 实例。多数基准中，newground 能更快处理较大、较密实例，地面程序规模最高缩至对照方法的约 1/50；部分对照方法生成超过 30 GB 的程序时，newground 仍可完成求解。结果支持将该归约与传统地面器组合使用，但不证明新方法在所有 ASP 任务上普遍占优。

## 贡献与局限
论文建立了 body-decoupled grounding 的多种归约及其复杂度分析，并以 newground 展示了部分归约与现有工具协作的可行性。实验是围绕 grounding bottleneck 设计的初步基准，且只比较 gringo、idlv 等完整地面器；作者明确指出结果不代表新方法总体胜出。后续方向是让地面器自动识别适合应用归约的程序部分。

---
DOI: 10.1016/j.artint.2026.104600
