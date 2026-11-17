# OnionAdapt: Cross-domain few-shot website fingerprinting attack from surface sites to onion services 总结

## 基本信息
- **标题**: OnionAdapt: Cross-domain few-shot website fingerprinting attack from surface sites to onion services
- **作者**: Yuwei Xu、Xinhe Fan、Zhengxin Xu 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173，文章号105231
- **发表**: 2026-11-10
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105231

## 一句话概括
研究比较普通网站与洋葱服务的加密流量，指出标注样本有限时仍可能暴露访问模式。

## 问题与动机
加密网络中的访问模式仍可能泄露网站类别，现有评估很难区分域差异与标注稀缺各自造成的影响。

## 方法
论文在受控环境中比较不同来源的加密访问流量，并评估少标注条件下识别性能的变化。作者用多种对照区分数据来源、标注量和模型因素对结果的影响。

## 实验与结果
四种数据迁移场景下，作者与五种基线对照，若干少样本设置的识别率提高。结果表明，在论文测试的网络环境里，加密流量仍存在可区分的访问模式（PDF 第 11–16 页）。

## 贡献与局限
研究为洋葱服务的流量隐私评估提供跨域量化证据。实验依赖所测网站和流量环境，专门防御措施能否降低识别风险仍待检验。

---
DOI: 10.1016/j.cose.2026.105231
