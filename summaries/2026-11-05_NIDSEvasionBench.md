# Revisiting adversarial robustness in NIDS: a multi-dataset evaluation of test-time evasion attacks 总结

## 基本信息
- **标题**: Revisiting adversarial robustness in NIDS: a multi-dataset evaluation of test-time evasion attacks
- **作者**: Rifa Tasfia、Anitha Chennamaneni、Abhijit Kumar Nag
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25，文章号184
- **发表**: 2026-11-05
- **日期来源**: Springer出版社文章网页的Published和citation_online_date
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01353-8
- **PDF**: [IJIS_2026_NIDSEvasionBench.pdf](papers/IJIS_2026_NIDSEvasionBench.pdf)

## 一句话概括
在三套网络流量数据上比较两类神经入侵检测器面对多种白盒与黑盒规避的稳健性。

## 问题与动机
检测器在干净测试集上准确率很高，部署时仍可能遇到蓄意修改的输入。不同流量域、攻击知识和样本比例会改变脆弱性评估。

## 方法
用ART在UNR-IDD、CICIOMT-2024和UAV-IDS-2025上评估全连接网络和一维卷积网络。比较AutoAttack、Auto-PGD、C&W白盒扰动与HopSkipJump黑盒扰动，改变纳入攻击评估的测试样本比例。

## 实验与结果
干净数据上的准确率在部分配置中接近或达到100%，C&W和HopSkipJump可在部分设置下大幅拉低准确率。两种架构的稳健性随数据集、攻击和评估比例变化（PDF第13、19页）。

## 贡献与局限
给出了多场景、多攻击知识条件下的对照。实验在离线特征空间施加扰动，无法直接证明修改能在真实网络协议约束下实现，也无法由两种模型得出普遍排序。

---
DOI: 10.1007/s10207-026-01353-8 | PDF: [IJIS_2026_NIDSEvasionBench.pdf](papers/IJIS_2026_NIDSEvasionBench.pdf)
