# Evasion Games: Dissecting Malware Evasive Techniques Across Packers, Sandboxes, and Debuggers 总结

## 基本信息
- **标题**: Evasion Games: Dissecting Malware Evasive Techniques Across Packers, Sandboxes, and Debuggers
- **作者**: Daniele Mammone、Francesco Sidoti Migliore、Stefano Longari、Michele Carminati、Stefano Zanero、Mario Polino
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **卷期 / 文章号**: 29(4)，Article 45，31页；卷期标注2026年11月
- **发表**: 2026-10-26
- **日期来源**: Crossref published-online；11月卷期不替代首次在线日期
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3846178
- **PDF**: [TOPS_2026_EvasionGames.pdf](papers/TOPS_2026_EvasionGames.pdf)

## 一句话概括
扩展恶意软件规避分析技术的分类体系，对照加壳工具采用的技术与沙箱、调试器的应对能力，揭示单项防护与组合规避之间的差距。

## 问题与动机
分析工具即使能处理常见环境检测，也可能在时间行为、环境一致性或多种技术组合下失效；已有研究较少把加壳工具的实际采用情况与分析工具的覆盖范围联系起来。

## 方法
在既有分类体系中新增整理55项技术，区分反调试、反虚拟化和其他规避行为。用最小测试程序及受控探针分析25种加壳工具，并评估7个在线沙箱、4种调试器；除单项测试外，还比较各加壳工具所对应的技术组合。

## 实验与结果
沙箱对反调试、反虚拟化技术的平均应对比例约为72%和85%，对其他技术仅约42%；在加壳工具对应的组合测试中，表现最好的沙箱也只应对了不超过44%的组合。调试器处理反调试技术较弱，但摘要的27%与正文、结论统计口径不一致，不宜当作统一成功率引用（PDF第18—24、27页，表6—14）。

## 贡献与局限
把技术分类、加壳工具采用情况和分析环境能力对应起来，为防御工具定位薄弱环节。部分加壳工具仅测试试用版，结果依赖具体Windows环境、位数兼容性及当时工具版本；最小程序和逐项探针也不能替代真实恶意软件的完整行为评估，组合测试不代表真实样本检出率（PDF第11—14、22、27页）。

---
DOI: 10.1145/3846178 | PDF: [TOPS_2026_EvasionGames.pdf](papers/TOPS_2026_EvasionGames.pdf)
