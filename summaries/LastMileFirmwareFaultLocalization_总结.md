# The Last Mile of Fuzzing: An Efficient Fault Localization Framework for ARM Embedded Firmware 总结

## 基本信息

- **标题**: The Last Mile of Fuzzing: An Efficient Fault Localization Framework for ARM Embedded Firmware
- **作者**: Boyu Chang, Binbin Zhao, Bo Xu, Qiao Zhang, Peiyu Liu, Qinge Xie, Guozhu Meng, Shouling Ji
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3712723
- **arXiv**: 无
- **PDF**: [TDSC_2026_LastMileFirmwareFaultLocalization.pdf](papers/TDSC_2026_LastMileFirmwareFaultLocalization.pdf)

## 一句话概括

针对模糊测试（fuzzing）发现的 ARM 嵌入式固件崩溃，提出基于事件驱动足迹收集与历史驱动逆向执行的自动化故障定位框架 FIRMLOCATOR，将根因候选指令定位在 Top-10 内，成功率达 98.3%。

## 问题与动机

模糊测试已被广泛用于发现嵌入式固件漏洞，但崩溃后的故障定位作为漏洞发现流水线的"最后一公里"仍极具挑战，当前高度依赖人工调试。嵌入式环境普遍缺少 sanitizer 等调试机制，且固件二进制通常被 strip 掉符号，导致分析人员面对大量过度污染、嘈杂的可疑指令，逐条人工审查控制流与数据流极其耗时且易错。此外，内存别名问题（多个指针指向同一内存）给崩溃用例的数据流跟踪带来不确定性，进一步妨碍自动化根因分析。

## 方法

FIRMLOCATOR 是一个面向崩溃后（postmortem）固件分析的故障定位框架，由三大组件构成。第一，事件驱动足迹收集机制：基于固件重宿主（rehosting）在崩溃复现时捕获数据事件与动作事件——数据事件记录每次成功内存读/写的访问类型、指令地址、实际读写数据与内存地址，动作事件在每个指令执行时记录 PC 值，从而重建完整执行轨迹与具体内存访问。第二，历史驱动逆向执行：由动作事件迭代重建执行轨迹并构造细粒度 use-define 链，依据 ARMv7-M 规范实现 43 类 ARM Cortex-M 指令的逆处理器反向恢复寄存器旧值，并利用数据事件直接恢复被内存别名遮蔽的具体数据，避免昂贵的别名推断开销。第三，根因分析流水线：先以崩溃指令涉及的寄存器/内存地址为污点源做后向污点分析得到初始可疑指令集，再用两条互补启发式打分排序——冗余循环污点抑制（压低 memcpy 式紧循环中重复指令的分数）与历史写污点优先（提高远离崩溃点却向崩溃相关地址写入的指令分数），最终保守输出至多 5 条根因候选指令。评估上采用语义化 ground truth：对每个崩溃用例人工标注至多 5 条关键指令，任一命中 Top-k 即视为定位成功。

## 实验与结果

实验基于 Fuzzware 及 GDMA、Hoedur 等公开基准，覆盖 19 个 ARM 固件镜像与 59 个可复现崩溃用例（C1–C59），在 56 核 Xeon E5-2680 v4、256 GB 内存、Ubuntu 22.04 环境下与移植到 ARM Cortex-M 的 POMP、POMP++ 对比。RQ1：完整执行轨迹下 FIRMLOCATOR 在 59 例中成功定位 58 例（98.3%），而 POMP 与 POMP++ 分别仅 5.1% 与 35.6%，且二者仅能完成 13.6% 与 79.7% 的用例（大量超时）；限制在崩溃前最后 50% 轨迹时 FIRMLOCATOR 仍有 84.7%（POMP 10.2%、POMP++ 54.2%）；深度根因（ΔRoot>50%）11 例全部成功，仅 C32（中断上下文恢复中数据段已被破坏）失败。RQ2：事件足迹收集平均额外耗时 10.68 s（约 0.73 倍）、日志增大 23.58 MB，根因分析阶段平均仅 7.22 s；随分析深度线性增加时 POMP 呈指数级耗时增长、POMP++ 为多项式级，FIRMLOCATOR 增幅平缓。RQ3 消融：历史写优先策略在 15 例（25.4%）显著改善，其 Top-1 命中率达 81.4%，高于完整版 FIRMLOCATOR 的 66.1%。RQ4：在最后 10,000 条指令的固定深度下，FIRMLOCATOR 的别名解析平均耗时小于 0.01 s，而 POMP 为 766.59 s、POMP++ 为 8.08 s。灵敏度分析显示 n=5 与 Top-10 组合可完全覆盖随机抽样的 18 个用例，且 88.1%（52/59）用例的人工标注 ground truth 不超过 5 条指令。

## 贡献与局限

贡献：一是重新设计并平衡多条启发式打分策略，使排名结果比会议版更稳定、更具普适性；二是将逆向执行引擎支持的 ARM Cortex-M 指令类别从 29 类扩展至 43 类，提升对高度优化真实固件的适用性；三是引入至多 5 条指令的规范化根因标注协议，显式处理指令级歧义；四是把评估扩展到 GDMA、Hoedur 等更丰富的数据集，相对 SOTA 在全轨迹分析能力上提升 20.3%、整体效率达多项式级加速、Top-10 成功率提高 62.7%，并开源（https://github.com/NESA-Lab/FirmLocator）。局限：作为 fuzzing 后分析框架，其适用性受底层 fuzzer 覆盖与平台支持限制；针对 stripped 裸固件仍只能给出排序指令而非消除人工研判；两条启发式与 43 条指令支持基于常见模式设计，泛化性有限；遇到 C32 这类中断上下文恢复崩溃时足迹收集可能失效。未来工作拟结合大语言模型生成更全面的根因自然语言描述。

---
DOI: 10.1109/tdsc.2026.3712723
