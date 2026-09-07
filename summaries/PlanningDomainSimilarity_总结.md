# Similarity of Planning Domain Models via Answer Set Programming 总结

## 基本信息

- **标题**: Similarity of Planning Domain Models via Answer Set Programming
- **作者**: Lukáš Chrpa, Carmine Dodaro, Marco Maratea, Marco Mochi, Mauro Vallati
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01（Journal Pre-proof；2024-07-25 投稿，2026-08-26 修回，2026-08-31 录用）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104620
- **arXiv**: 无
- **PDF**: [AIJ_2026_PlanningDomainSimilarity.pdf](papers/AIJ_2026_PlanningDomainSimilarity.pdf)

## 一句话概括

本文形式化规划领域模型的结构等价与强等价，提出用回答集程序把领域模型相似性建模为图编辑距离变体，从而算出使两个模型强等价所需的最少修改步数。

## 问题与动机

自动规划中，领域模型是编码领域知识的关键部分，但缺少支持知识工程过程的比较工具，尤其没有能"diff"出两个模型版本差异的方法。现有工作要么聚焦单一问题实例的最优计划（如模型协调问题 MRP），要么要求被比较模型共享谓词与算子（如 D-VAL、Coulter 等人方法），都不能对整体模型给出差异度量。随着 LLM 被用于生成规划模型，低质量模型大量涌现的风险进一步凸显了对自动化模型比较手段的需求。作者因此希望定义并求解"领域模型相似性"问题：两个模型需要经过多少次最小修改才能变得强等价。

## 方法

作者先形式化结构等价与强等价：强等价指两个领域模型除命名外完全一致（谓词与算子存在保持元数、匹配前件/删/增效应的双射），结构等价是强等价的必要条件。为此引入有向图表示：接地层面的 Domain Model Graph (DMG)、lifted 层面的 Lifted Domain Model Graph (LDMG，带变量绑定标签的边)、以及支持负前件、PDDL2.1 持续动作与动作代价的扩展版 ELDMG；定理证明模型结构等价当且仅当其 (E)LDMG 同构，强等价还需匹配算子数值属性（时长/代价）相等。在此基础上把相似性定义为两个模型 (E)LDMG 之间一种图编辑距离变体上的最小基本操作数（增加/删除谓词或算子、向算子增删谓词集合成员、改写属性值）。求解采用完全声明式的 ASP 编码（弱约束分两级先最小化结构改动数再最小化参数重映射数，并给出正确性命题），另配一个命令式"问题感知预接地"预处理阶段只生成有意义的候选映射以提升可扩展性；最优答案集经处理后输出人类可读的修改指令，扩展领域（持续动作、代价）通过额外 ASP 程序 Π′′ 处理。

## 实验与结果

基准含经典与时间两类：经典域取自 IPC 的 Barman、Blocksworld、简化 Logistics、Rovers、Satellite、Sokoban 及 ICKEPS 2016 的 RPG、Match-3（算子 2–12 个、谓词 4–25 个），并通过对原模型做纠缠/宏动作重构或直接比较两队独立建模（RPG）生成对比对；时间域取自 IPC 2018 的 Cushing、Floortile、Parking、Sokoban（持续动作 3–6 个、谓词 3–10 个）。实验环境为 Apple M1 3.22 GHz、8 GB 内存，单次限 6 GB 内存与 5 CPU 分钟，ASP 求解器用 CLINGO 5.6.2（--parallel-mode=4），经 PYSPEL 实现。结果显示：启用预处理后所有域的强等价判定都在 0.1 CPU 秒内完成，而纯声明式编码在 Barman、Rovers 上超内存；一般比较中预处理方案在全部基准上 1 CPU 秒内找到最优解（如 Satellite 生成约 5 千条规则 vs 无预处理超 50 万条），RPG vs Match-3 需增加 4 个节点并改动 78 条边也在 1 秒内完成；相似域的最优解数量通常很少（最多 4 个），而时间域相似模型可多达 256（Sokoban）或 720（Cushing）个最优解；跨域时间比较中无预处理仅有 1 例可证明最优，且两例生成超 100 万条规则（如 Sokoban vs Floortile 1,995,031 条 vs 预处理 7,732 条）。在 Logistics/Driverlog/Depots 三模型上提取公共核，得到 move/drive-truck/drive、load/load-truck/load、unload/unload-truck/unload 三组共享动作，其中 Logistics 全部动作构成公共核。

## 贡献与局限

主要贡献：首次形式化领域模型的结构等价与强等价并给出对应图同构刻画；提出领域模型相似性这一新概念及其优化问题；给出首个基于 ASP 的最优求解方案，能算出使模型强等价的最少修改并输出可读修改清单，且对扩展算子（负前件、持续动作、动作代价）给出完整理论（命题与证明）；论文还论证了该方法在模型 diff 工具、自动模型获取工具（如 LOCM）评测、抄袭检测、ICKEPS 建模竞赛评测以及计算领域模型"公共核"以支持继承与模块化建模等场景的应用价值。局限方面：纯声明式 ASP 编码在大模型与差异悬殊的对比对上会超内存，必须依赖预处理；目前仅覆盖 STRIPS 与 PDDL2.1 的部分特性，对涉及多函数符号/常量的算术表达式属性尚不支持；领域模型相似性问题的计算复杂度（是否 NP 难）仍未解决；作者将扩展 PDDL+ 等更富表达力的语言、改进输出解释并推进上述实际应用作为未来工作。

---
DOI: 10.1016/j.artint.2026.104620
