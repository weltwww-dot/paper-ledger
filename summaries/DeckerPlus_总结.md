# DeckerPlus: Whole Program Attack Surface Reduction via Compiler Analysis and Transformations 总结

## 基本信息

- **标题**: DeckerPlus: Whole Program Attack Surface Reduction via Compiler Analysis and Transformations
- **作者**: Alexandra Hussar、Sharjeel Khan、Christopher Porter et al.
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **发表**: 2026-09-07
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3833877
- **arXiv**: 无
- **PDF**: [TOPS_2026_DeckerPlus.pdf](papers/TOPS_2026_DeckerPlus.pdf)

## 一句话概括

DeckerPlus 利用全程序静态分析与运行时函数集切换，在保留全部功能且无需用户配置的情况下，大幅压缩代码复用攻击可利用的 gadget 攻击面。

## 问题与动机

代码膨胀为攻击者提供大量可拼接的短指令序列，使 ROP/JOP 等代码复用攻击更易实施。已有去膨胀方法常依赖用户输入或配置，可能因删减过度破坏正常执行，也可能过于保守而留下大量攻击面。

## 方法

该方法通过静态分析确定不同执行阶段应启用或禁用的关键函数集合，再由运行时系统在指定程序点切换，使当前阶段无关的 gadget 不可达。作者还引入函数克隆与内联两种扩展，以进一步拆散可利用链。

## 实验与结果

基础方案在 SPEC CPU 2017、GNU coreutils 和四类应用负载上的 gadget 平均削减率分别为 70.3%、88.5% 和 89.0%；内联扩展进一步达到 77.6%、94.7% 和 97.8%。SPEC 平均减速为 6.5%，Linux 与 Windows 案例中均破坏了生成 shell 的攻击链。

## 贡献与局限

主要贡献是提出无需剥离功能的全程序攻击面缩减框架，并以编译变换进一步增强链破坏能力。其局限是结果集中于所选基准与服务程序，面对动态加载、即时编译及更复杂真实攻击链时仍需进一步检验。

---
DOI: 10.1145/3833877
