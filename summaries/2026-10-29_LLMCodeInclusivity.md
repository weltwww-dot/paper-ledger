# Evaluating security and inclusivity in LLM-generated code 总结

## 基本信息
- **标题**: Evaluating security and inclusivity in LLM-generated code
- **作者**: Bilal Naqvi、Waleed Shahid、Janne Parkkila 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105208
- **发表**: 2026-10-29
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105208
- **PDF**: [COSE_2026_LLMCodeInclusivity.pdf](papers/COSE_2026_LLMCodeInclusivity.pdf)

## 一句话概括
比较不同包容性需求描述下LLM生成代码的表现，并检验LLM评审与人类专家在包容性、安全评分上的差异。

## 问题与动机
安全系统使用者的认知与能力存在差异，但代码生成需求往往没有明确表达这些差异。模型给出的包容性界面和安全实现，也不能只凭模型自评认定可靠。

## 方法
设置两个用户故事，每个包含三种需求详细程度，每种重复生成十次；先由六个LLM按量表评价，再把高分制品交给十名包容性专家和十名安全专家。结合静态、动态工具分析，并用混合效应模型比较评分。

## 实验与结果
更详细的需求与较高包容性评分相关；人类与LLM的包容性评分差异未达显著，安全评分则存在显著差异，LLM通常更乐观。未观察到评分层面的安全—包容性取舍，不等于证明不存在真实安全代价（PDF第15页）。

## 贡献与局限
展示明确需求及人机互补评审的价值。两个用户故事和优选高分样本限制外推；评分差异不显著不能推出等效，专家或LLM的感知评分也不能替代实际神经多样性用户测试与漏洞验证。

---
DOI: 10.1016/j.cose.2026.105208 | PDF: [COSE_2026_LLMCodeInclusivity.pdf](papers/COSE_2026_LLMCodeInclusivity.pdf)
