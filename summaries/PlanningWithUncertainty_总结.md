# Planning with uncertainty: symmetries, policy inference, and solution compression 总结

## 基本信息

- **标题**: Planning with uncertainty: symmetries, policy inference, and solution compression
- **作者**: Frederico Messa, André Grahl Pereira
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-09-01（Accepted for publication in Artificial Intelligence，CC-BY-NC-ND 4.0）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104574
- **arXiv**: 2403.19883v2
- **PDF**: [AIJ_2026_PlanningWithUncertainty.pdf](papers/AIJ_2026_PlanningWithUncertainty.pdf)

## 一句话概括

本文面向全可观测非确定（FOND）规划，提出策略等价剪枝、群论规范状态对称性、多项式时间策略推断（concretizer）与整数规划解压缩（compressor）等成套技术，把显式 best-first 策略空间搜索算法 AND* 提升为与最先进 FOND 规划器竞争的方法。

## 问题与动机

FOND（fully-observable non-deterministic）规划是人工智能不确定性规划的核心范式：它通过具有非确定效应的动作来建模不确定性，要求智能体为所有可能出现的偶然情况预先准备好动作策略。FOND 求解已被广泛用于定性数值规划、超性质验证、多智能体规划、弹性规划等场景，其最坏情况复杂度为 EXPTIME-complete。已有方法多采用经典规划启发式迭代精化或编译到 SAT 等范式，而本文聚焦显式策略空间 best-first 搜索（AND* 算法，Messa and Pereira 2023）。作者研究 FOND 策略与策略空间搜索的结构，目标是发展一套技术提升 AND* 的性能：利用策略间的等价关系剪去部分搜索空间、利用状态对称性强化等价定义，并给出两项超出策略空间搜索本身的技术——多项式时间地从策略定义域推断解策略的 concretizer，以及把完整状态解策略压缩为最少部分状态表示的整数规划过程。

## 方法

论文围绕 AND*（在"构造性策略空间"上做 best-first 搜索，初始为空策略，每次从 remain(π) 中选一个状态补充映射生成后继）提出四类贡献。其一，签名式等价剪枝：用 sign(π) 做查重剪枝；对 sign=⟨dom,escape⟩ 的 domain-escape 剪枝，论文证明仅靠 escape 集合会丢失映射而破坏完备性，于是设计 concretizer——给定"空心策略"⟨D,E⟩ 在 O(|D|²·|D∪E|·|Π|) 时间内构造出 proper 且 dom=D、escape⊆E 的策略（高效实现为 O(|D|·|D∪E|·|Π|)），使该剪枝在 AND* 中 sound 且 complete，并在用 ∆↓(hLM-Cut) 引导时保持最小 domain size 最优性。其二，escape 等价剪枝即使配 concretizer 仍不完备（会出现交叉互剪），故采用两阶段混合：先用 escape 剪枝（sound 但不完备）求解，失败才回退到 domain-escape 剪枝。其三，用结构状态对称性强化等价定义：把状态按结构对称（Aut(Π) 置换群轨道）归入同一类，采用 Nauty 计算 PDG 自同构生成元、GAP 计算 stabilizer chain 与逆横断，首次将 Jefferson et al. (2019) 的 canonical image 技术用于规划，从而可完美计算规范对称签名（对比文献的贪心 hill-climbing 近似）。其四，compressor：对任意定义在完整状态上的解策略 π，逐动作地把问题拆成独立子问题，迭代求解递增 k 的部分状态整数规划（IBM ILOG CPLEX），产出最少部分状态数、与 π 在 dom(π) 上动作一致且不映射 escape(π) 的无歧义部分策略 τ。为提升覆盖率还开启了死锁检测、f=2∆↓−|dom(π)| 的加权引导并改用 hFF 启发式（牺牲最优性的 satisficing 配置）。

## 实验与结果

实验基准沿用 Pereira et al. (2022) 的 IPC-FOND（379 个任务、12 个域）与 NEW-FOND（Geffner and Geffner 2018，211 个任务、5 个域），合并 blocksworld 两域并剔除 25 个无解 first-responders 任务后共 16 个域；硬件为 AMD Ryzen 9 3900X，限 8 GB 内存、每任务 30 分钟。等价剪枝上：domain-escape 相对 identity 使多数域生成策略数大降（acrobatics −99.5%、chain-of-rooms −90.0%、first-responders −42.1% 等），覆盖率由 0.453 略升至 0.482，acrobatics 由 0.50 升至 1；escape 剪枝把覆盖率从 0.482 提到 0.651，chain-of-rooms 0.30→1、elevators 0.47→0.80、tireworld-truck 0.18→0.46 等，平均生成策略数由 60,651 降至 6,305。对称性方面：16 个域中 8 个域至少 80% 任务存在非平凡对称，生成 Aut(Π) 生成元对所有有对称任务不超过 1.75 秒（限 5 秒）；贪心与规范对称都把覆盖率提升到约 0.73，生成策略数在 faults（−99.95%）、tireworld-spiky（−99.59%）、tireworld-truck（−99.09%）等 7 个域至少降 25%，规范签名比贪心每生成策略平均仅多约 45% 聚合时间，故此后采用规范对称。开启 satisficing 特性后覆盖率从 0.728 升至 0.900（blocksworld-original 0.53→1、blocksworld-advanced 0.2→0.82、zenotravel 0.33→0.87，仅 islands 降为 0.75）。compressor 对多数任务在 20 ms 内完成压缩（最难的 doors p15 需 55 秒，其解从 131,070 个状态压至极小表示），在 16 域中的 11 个域缩减了解规模，doors 的平均规模从 17,473.73 降至 18.00（三个数量级），doors 压缩解每个部分状态仅 1–2 个事实（对比完整状态 34 个事实）。与最先进规划器对比：AND* 覆盖率为 0.900，居 PR2（1.0）之后列第二，高于 PRP（0.812）、IDFSP（0.808）、CFOND-ASP（0.535）、FOND-SAT（0.426）；按子基准看 IPC-FOND 上 AND* 为 0.915、NEW-FOND 上为 0.868。虚拟最优组合"AND* 跑 14.8 s + PR2 跑 27.1 s"共 41.9 s 可解全部任务，而单用 PR2 需 250.9 s，说明 AND* 相对 PR2 仍带来增量价值。紧凑性上：AND* 在多数域返回的部分策略解比 PRP 小至少 10%（tireworld-truck −42.7%、tireworld-triangle −33.2%、earth-observation −24.0%、elevators −22.7%、zenotravel −20.0%），仅 blocksworld-advanced 平均大 2.3%；对 PR2 仅在 blocksworld-advanced（2.3%）与 miner（0.6%）更大；与 FOND-SAT、CFOND-ASP 的解规模差异基本在 10% 以内（earth-observation 上 AND* 比 CFOND-ASP 小 13.1%）。

## 贡献与局限

主要贡献：对策略等价关系及其剪枝能力做了系统研究，证明配 concretizer 的 domain-escape 剪枝可使 AND* sound、complete 且保最优；提出 concretizer——仅凭策略定义域集合就能在多项式时间内推断出匹配的解策略，为 FOND 规划开辟"改变搜索目标"的新可能，也可服务其他规划器与概率规划；用群论技术（Nauty+GAP+Jefferson et al. 规范像算法，首次用于规划）在实际中高效地完美计算 FOND 的结构状态对称性；提出 compressor，把任意规划器输出的完整状态解策略压缩为最少部分状态的无歧义表示，计算高效且多数域达到一流的解紧凑性并更易读；完整实验表明集合上述技术后显式策略空间搜索已具备与 PR2、PRP 等最先进规划器竞争的实力并与之互补。局限与未来方向：本文假设动作公平（fair），对抗性设定仅言及可扩展；escape 剪枝本身不完备，需混合回退机制（实验中被回退从未触发）；死锁检测与 satisficing 配置会使 AND* 失去最优性；compressor 的最优性相对"输入策略"而言，未必得到任务全局最紧凑的部分策略；最坏情况下自同构群规模阶乘级、只能借助 Nauty 等外部工具限时计算；作者将针对带等价剪枝的策略空间搜索设计专属启发式、在搜索中用部分状态压缩信息、吸收 PRP/PR2 的死端泛化技术，以及利用 concretizer 调用 ⟨D,S*⟩ 设计全新 FOND 算法列为未来工作。

---
DOI: 10.1016/j.artint.2026.104574
