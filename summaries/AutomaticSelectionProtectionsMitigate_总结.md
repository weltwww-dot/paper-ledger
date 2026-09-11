# Automatic selection of protections to mitigate risks against software applications

## 基本信息

- 标题: Automatic selection of protections to mitigate risks against software applications
- 作者: Daniele Canavese, Leonardo Regano, Bjorn De Sutter, Cataldo Basile
- 期刊 / 会议: Computers & Security 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1016/j.cose.2026.104959
- PDF: [COSE_2026_AutomaticSelectionProtectionsMitigate.pdf](papers/COSE_2026_AutomaticSelectionProtectionsMitigate.pdf)

- 标题: Automatic selection of protections to mitigate risks against software applications
- 作者: Daniele Canavese, Leonardo Regano, Bjorn De Sutter, Cataldo Basile
- 期刊 / 会议: Computers & Security 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

作者为 Daniele Canavese、Leonardo Regano、Cataldo Basile、Bjorn De Sutter；发表于 *Computers & Security* 168 (2026) 104959。研究对象是面向移动代码分析与篡改（MATE）攻击的软件保护选择，实验包含搜索性能评估、三个 Android 概念验证应用和专家评价。DOI: 10.1016/j.cose.2026.104959
## 一句话概括

论文把攻击路径、资产、安全需求和保护措施形式化为一个攻防博弈，用带记忆的有界 minimax 搜索自动选择在安全性与运行开销之间更合适的软件保护组合。

## 问题与动机

MATE 攻击者可以获得应用的完整副本并反复尝试攻击；代码混淆、完整性检查等保护措施的效果、组合协同和性能代价又各不相同。现实中通常依赖少数专家手工挑选，难以覆盖复杂的攻击路径，也难以解释为何某一组保护最合适。论文因此希望把保护选择变成可计算、可比较且能考虑攻击者行为的优化问题。

## 方法

作者在 ESP 知识库中描述代码构件、资产、机密性/完整性需求、攻击步骤和候选保护，用保护强度、抗性、协同关系与开销构造 Software Protection Index（SPI）。防守方提出保护组合，攻击方在反复尝试中选择代价最低或成功概率最高的攻击路径；求解器使用有界深度优先 minimax、动态规划缓存、剪枝和代码相关集合（CCS）压缩搜索。框架可对接 ACTC、Tigress 等保护工具，并由专家提供或校准攻击与保护参数。

## 实验与结果

定量实验在 4–512 个保护选项、不同路径数和深度 3–6 的合成搜索空间上进行，结果显示运行时间随保护数和搜索深度呈指数增长，但 CCS 可显著减少组合；实验中每个攻击步骤平均关联少于 2 个保护、最多约 7 个，搜索通常在秒级。三个 Android 应用（OTP 生成器、许可证管理器、DRM 播放器）的两位专家认为自动选择的组合有针对性、保护性高且语义保持，开销可接受。对攻击概率、缓解效果、协同效应和权重作 ±5%/±10% 扰动时总体排序较稳健，协同参数最敏感；但渗透测试使用的是人工选择保护，不能直接证明 ESP 选择的组合优越。

## 贡献与局限

贡献是给出从威胁建模到保护配置的统一形式化方法、SPI 指标和可实现的自动搜索流程，并以定量与专家案例验证可行性。局限包括输入参数依赖专家判断，攻击步骤目录和开销模型较粗；有界搜索只保证所探索空间内的最优，模型对多于三个保护的指标预测会变差；实验规模小、缺少与其他求解器的系统比较，且主要依赖 ACTC/Tigress、Android/Linux ARMv7。未来需要自动反馈监控、更完整的攻击知识和更大规模实证。

DOI: 10.1016/j.cose.2026.104959
