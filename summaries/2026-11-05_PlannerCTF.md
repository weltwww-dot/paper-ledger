# Planner-directed multi-agent LLMs with on-demand skill-equipped specialists for CTF-based autonomous penetration testing 总结

## 基本信息
- **标题**: Planner-directed multi-agent LLMs with on-demand skill-equipped specialists for CTF-based autonomous penetration testing
- **作者**: Amir Amine、Samer Saab Jr.
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25，文章号183
- **发表**: 2026-11-05
- **日期来源**: Springer出版社文章网页的Published和citation_online_date
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01350-x
- **PDF**: [IJIS_2026_PlannerCTF.pdf](papers/IJIS_2026_PlannerCTF.pdf)

## 一句话概括
在授权CTF中检验持久规划器与短时专家的分工，并用资源匹配实验区分架构与模型能力的影响。

## 问题与动机
长时间解题需要跨步骤保留证据，同时控制上下文膨胀。只看总体解题率容易把更强模型带来的收益归给任务编排。

## 方法
持久规划器保留任务状态和证据，按需启动一个上下文隔离的短时专家，并通过共享执行环境与精简反馈协调工作。实验另外对规划架构和强模型升级做交叉比较。

## 实验与结果
在NYU CTF Bench的200题上，系统获41个判题通过，基线获4个。审计后确认实际解出分别为29题和3题。资源匹配的80题子集显示模型升级效应显著，规划架构主效应未达显著（OR 1.17，p=0.34）。

## 贡献与局限
把自动评分、解题真实性和资源匹配比较结合起来，使架构收益更容易归因。结果来自授权基准及指定配置，尚不能推及真实网络中的自主安全作业。

---
DOI: 10.1007/s10207-026-01350-x | PDF: [IJIS_2026_PlannerCTF.pdf](papers/IJIS_2026_PlannerCTF.pdf)
