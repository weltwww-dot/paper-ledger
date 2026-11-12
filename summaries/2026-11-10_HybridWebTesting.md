# A hybrid framework for web applications security vulnerabilities detection 总结

## 基本信息
- **标题**: A hybrid framework for web applications security vulnerabilities detection
- **作者**: James A. Stewart、Gheida Shahrour、Amro Al-Said Ahmad
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25（2026），文章号187
- **发表**: 2026-11-10
- **日期来源**: Springer 官网 citation_online_date，与正式 PDF 的 DOI 和文章号一致
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01346-7
- **PDF**: [IJIS_2026_HybridWebTesting.pdf](papers/IJIS_2026_HybridWebTesting.pdf)

## 一句话概括
结合黑盒扫描与基于模型的测试，提高受控 Web 应用的漏洞检测覆盖并检查扫描器报告的一致性。

## 问题与动机
黑盒测试的路径覆盖受限，建模又需要维护成本。扫描器不同界面还可能对同一次检测给出不同计数，导致安全团队误读覆盖率或风险。

## 方法
研究把黑盒与基于模型的测试组合为六级评估方案，通过多轮对照、统计分析和人工抽验区分覆盖增益与工具报告偏差。

## 实验与结果
在 OWASP ZAP 对 Juice Shop 的受控案例中，作者报告严重漏洞检测计数由平均 2.0 增至 23.7，研究人员复核了三处抽样发现。图 6 还记录了扫描器界面计数差异（PDF 第 16、22 页）。

## 贡献与局限
贡献包括渐进式评估框架和可复核的工具可靠性分析。数据来自单一工具和示范应用，计数增益及资源成本需在其他应用中重新测量。

---
DOI: 10.1007/s10207-026-01346-7 | PDF: [IJIS_2026_HybridWebTesting.pdf](papers/IJIS_2026_HybridWebTesting.pdf)
