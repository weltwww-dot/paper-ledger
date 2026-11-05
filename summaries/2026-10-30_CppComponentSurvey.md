# A survey of C/C++ third-party component identification: Methods, assumptions, and evaluation reliability 总结

## 基本信息
- **标题**: A survey of C/C++ third-party component identification: Methods, assumptions, and evaluation reliability
- **作者**: Wei Guo、Xixing Li、Qiang Wei
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105221
- **发表**: 2026-10-30
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105221
- **PDF**: [COSE_2026_CppComponentSurvey.pdf](papers/COSE_2026_CppComponentSurvey.pdf)

## 一句话概括
系统梳理C/C++第三方组件识别的任务、方法与评估假设，指出闭世界实验不足以证明真实供应链环境中的可靠性。

## 问题与动机
当清单或构建记录缺失时，需要从源码、二进制和固件识别复用组件、版本与代码片段。优化、修改和参考库不完整会破坏匹配，而异构评估口径又容易造成性能误判。

## 方法
检索五个文献数据库，经筛选从3712条记录形成75篇论文语料，按研究任务、输入、识别方法、失效风险和实验评价编码比较。区分组件、版本、局部代码及修改复用，分析参考覆盖与构建条件等假设。

## 实验与结果
75篇中47篇主要采用闭世界设置，仅13篇评估未知组件、11篇评估修改代码复用；这些类别并非互斥，不能直接相加。特征匹配和多特征融合常见，但数据单位、输出粒度与真值差异限制跨研究排名（PDF第1、14页）。

## 贡献与局限
形成可追溯的任务与证据分类，提出开放集识别、版本补丁关系和局部证据要求。本文是综述，没有新检测系统的统一实测优胜结论；文献覆盖和编码仍受检索范围限制，未来需可复现的任务专属基准。

---
DOI: 10.1016/j.cose.2026.105221 | PDF: [COSE_2026_CppComponentSurvey.pdf](papers/COSE_2026_CppComponentSurvey.pdf)
