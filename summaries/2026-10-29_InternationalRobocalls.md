# Robocalls: A worldwide or US-only problem? Analyzing spam and fraud in international phone calls 总结

## 基本信息
- **标题**: Robocalls: A worldwide or US-only problem? Analyzing spam and fraud in international phone calls
- **作者**: Kemal Altwlkany、Andro Merćep、Tomislav Ðuričić 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105222
- **发表**: 2026-10-29
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105222
- **PDF**: [COSE_2026_InternationalRobocalls.pdf](papers/COSE_2026_InternationalRobocalls.pdf)

## 一句话概括
用跨国电话蜜罐和多模态数据分析自动骚扰与诈骗呼叫，揭示美国与其他地区的模式差异。

## 问题与动机
自动呼叫跨语言和司法辖区，公开数据稀少且有隐私限制。只看美国报告或单一语言，难以判断国际活动、共同针对行为和相似话术。

## 方法
结合跨国背景报告与九个月蜜罐数据，分析呼叫时间、地域、文本语言、回拨号码、语音质量及活动聚类。蜜罐数据覆盖65个被叫国家；178个显示主叫国家代码可能被伪造，不直接证明主叫位置。以无监督聚类和少样本LLM分类整理活动与话术（PDF第9页）。

## 实验与结果
蜜罐登记960万次呼叫，公开部分为870万条呼叫详单、839份转录和677份录音，识别28个活动簇。该蜜罐中美国号码的呼叫率明显高于合并的非美国号码；登记总量与公开数据量不能混为同一分母（PDF第1、21页）。

## 贡献与局限
提供跨国、多模态的公开研究资源与呼叫模式证据。号码选择、可接通性、录音与语言处理会造成采样偏差，蜜罐率不等于全球人口发生率；话术或音频分类结果也不直接证明电话源身份、诈骗损失或治理效果。

---
DOI: 10.1016/j.cose.2026.105222 | PDF: [COSE_2026_InternationalRobocalls.pdf](papers/COSE_2026_InternationalRobocalls.pdf)
