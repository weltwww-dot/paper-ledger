# From static tasks to dynamic reasoning 总结

## 基本信息

- **标题**: From static tasks to dynamic reasoning: a characterization framework and study of large language model-based agents
- **作者**: Hanbo Yu, Shahrear Iqbal, Euclides Carlos Pinto Neto, Scott Buffett, Adrian Taylor
- **期刊 / 会议**: IJIS 2026
- **发表**: 2026-08-29
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01321-2
- **PDF**: [IJIS_2026_LLMAgents.pdf](papers/IJIS_2026_LLMAgents.pdf)

## 一句话概括

提出一个表征框架，从四个维度刻画网络安全中的「动态」任务，并系统调研大语言模型智能体在七个网络安全领域的应用现状与局限。

## 问题与动机

LLM 在网络安全中的多数工业应用仍集中在静态一次性任务（分类、实体抽取、摘要），无法覆盖真实安全工作流的复杂性——这些工作流随时间展开、输入不断演化、需要多步推理。需要系统理解 LLM 在需要上下文感知、工具交互与自适应决策的动态任务中能做什么、不能做什么。

## 方法

提出动态网络任务表征框架，沿四个互补维度刻画：操作目标（operational goal）、知识接地（knowledge grounding）、协作模式（collaboration mode）、认知复杂度（cognitive complexity）；并据此调研七个核心领域：威胁情报、数据隐私与安全、漏洞检测、恶意软件检测、入侵检测、应急响应与红队自动化。

## 实验与结果

调研发现当前系统受限于四类问题：隐私与部署约束、威胁知识陈旧或不完整、反馈驱动动作缺乏验证、缺乏可量化的运营收益证据；并给出相应改进方向（隐私感知部署、及时检索与知识维护、面向可测量安全结果的过程级评估、受控混合自动化中的人工监督）。原文以框架与调研为主，未提供量化对比。

## 贡献与局限

- 贡献一：首个面向动态网络任务的 LLM 智能体表征框架，统一了跨领域的分析维度。
- 贡献二：系统梳理七个安全领域的现状与瓶颈，给出可执行的改进方向。
- 局限：以定性调研为主；具体任务上的量化评估待后续工作。

---

DOI: 10.1007/s10207-026-01321-2
