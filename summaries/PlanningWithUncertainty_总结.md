# Planning with uncertainty: symmetries, policy inference, and solution compression

## 基本信息

- 标题: Planning with uncertainty: symmetries, policy inference, and solution compression
- 作者: Frederico Messa, André Grahl Pereira
- 期刊 / 会议: Artificial Intelligence 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1016/j.artint.2026.104574
- PDF: [AIJ_2026_PlanningWithUncertainty.pdf](papers/AIJ_2026_PlanningWithUncertainty.pdf)

- 标题: Planning with uncertainty: symmetries, policy inference, and solution compression
- 作者: Frederico Messa, André Grahl Pereira
- 期刊 / 会议: Artificial Intelligence 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

作者为 Frederico Messa、André Grahl Pereira；发表于 *Artificial Intelligence* 358 (2026) 104574。论文研究 Fully Observable Non-Deterministic（FOND）规划中的策略空间搜索、对称性消除和策略表示压缩。DOI: 10.1016/j.artint.2026.104574
## 一句话概括

作者提出显式搜索策略空间的 AND*，结合策略等价剪枝、群论规范化对称性、策略具体化和整数规划压缩；对于适用的核心算法/配置，方法保持完备性，同时寻找更小、更可执行的 FOND 策略表示。

## 问题与动机

FOND 规划要求在动作结果不确定时生成策略，状态空间与策略空间都可能迅速膨胀。传统方法容易重复搜索等价策略，或输出包含大量重复部分状态的完整策略；而单纯追求压缩又可能损害可执行性。论文因此分别处理“哪些策略搜索节点等价”“如何从部分策略信息推断完整策略”和“怎样用最少部分状态表示完整策略”三个问题。

## 方法

AND* 从空策略开始以最佳优先方式扩展。作者定义 escape/domain-escape 策略等价关系，并给出 concretizer：给定域状态集 D 与逃逸状态集 E，可在多项式时间内推断正确策略，复杂度为 O(|D|²|D∪E||Π|)，并给出更高效实现。结构对称性通过策略依赖图、群 Aut(Π)、Nauty/GAP 和 canonical image 识别；solution compressor 则用 MILP/CPLEX 最小化能无歧义表示完整策略的部分状态数，同时辅以 hFF 启发式和死锁检测。

## 实验与结果

实验覆盖 IPC-FOND 379 个任务和 NEW-FOND 211 个任务，合并为 16 个领域，剔除 25 个不可解任务；每个任务限时 30 分钟。综合技术后的覆盖率为 0.900，低于 PR2 的 1.000，但高于 PRP 的 0.812、IDFSP 的 0.808、CFOND-ASP 的 0.535 和 FOND-SAT 的 0.426；在 IPC-FOND 与 NEW-FOND 上 AND* 覆盖率分别为 0.915 与 0.868。虚拟最佳组合的平均时间约为 41.9 秒（AND* 14.8 秒、PR2 27.1 秒）。16 个领域中有 8 个至少 80% 任务存在非平凡对称性，规范化生成通常不超过 1.75 秒；压缩器在多数任务低于 20 ms，11 个领域减少了策略大小，部分领域相对 PRP 减少约 20%–43%，最难的 doors 任务约需 55 秒。

## 贡献与局限

贡献是把策略等价、群对称、可证明的策略推断和优化压缩组合成可扩展的 FOND 求解流程，并同时评价覆盖、时间和表示大小。局限是 escape 剪枝单独并不完备，需要混合回退；启发式搜索偏向满意解而非最优解；压缩器只保证相对于输入完整策略的最小化；对称性可能有阶乘级最坏复杂度且依赖外部工具，结论也受 IPC/NEW-FOND 基准覆盖范围限制。

DOI: 10.1016/j.artint.2026.104574
