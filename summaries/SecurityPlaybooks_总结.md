# Generating semi-automated security playbooks 总结

## 基本信息

- **标题**: Generating semi-automated security playbooks for vulnerability mitigation from unstructured advisory data
- **作者**: Daniel Oberhofer, Johannes Grill, Günther Pernul, Stefan Schönig
- **期刊 / 会议**: IJIS 2026
- **发表**: 2026-09-01
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01263-9
- **PDF**: [IJIS_2026_SecurityPlaybooks.pdf](papers/IJIS_2026_SecurityPlaybooks.pdf)

## 一句话概括

用大语言模型编排框架，从非结构化的 CERT 安全公告半自动生成标准化的漏洞缓解安全 playbook，并以 BPMN 可视化、分类为可执行任务。

## 问题与动机

自动化安全风险管理需要把公开安全公告中的缓解与修复策略落地执行。这类公告由各 CERT 定期发布，多为非结构化文本并附带额外安全信息源；人工把公告转成可执行方案成本高、易遗漏，需要自动化的语义理解与结构化生成。

## 方法

基于 LLM 编排框架：从非结构化公告生成标准化元模型（meta-model）的安全 playbook；用业务流程建模与标注（BPMN）图形可视化；把内容分类为可执行任务；实验生成 725 个安全 playbook 数据集。

## 实验与结果

对生成的 725 个 playbook 做内容分析：公告驱动的 playbook 以更新（update）任务为主，也涵盖禁用易受攻击策略、限制网络访问等防御主题（数字来自原文摘要）。

## 贡献与局限

- 贡献一：首个把 LLM 编排用于公告→安全 playbook 半自动生成的框架，含标准化元模型。
- 贡献二：725 个 playbook 数据集与内容分析，展示公告驱动的缓解策略分布。
- 局限：以更新类任务为主，覆盖的安全动作类型有限；自动化程度与误生成率原文摘要未量化。

---

DOI: 10.1007/s10207-026-01263-9
