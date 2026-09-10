# An Advanced Persistent Threat Detection Framework Based on Graph Attention Networks With Spectral Feature Refinement 总结

## 基本信息

- **标题**: An Advanced Persistent Threat Detection Framework Based on Graph Attention Networks With Spectral Feature Refinement
- **作者**: Chun-I Fan, Chi-Hsien Wu, Cheng-Han Shie, Hsin-Nan Kuo, Bo-Yi Lee
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026年5月25日
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3695911
- **arXiv**: 无
- **PDF**: [TDSC_2026_AdvancedPersistentThreatDetection.pdf](papers/TDSC_2026_AdvancedPersistentThreatDetection.pdf)

## 一句话概括

论文从原始 Sysmon 日志构造规则过滤溯源图，并结合谱特征细化的 GAT 和区间偏置，实现可复现且高效的 APT 恶意节点检测。

## 问题与动机

现有基于溯源图的 APT 检测容易受到大规模图的内存和效率限制，许多公开数据集又隐藏了日志采集和属性映射过程，难以复现。依赖商业 EDR 或高质量威胁情报的方案也提高了实际部署门槛。论文因此使用公开 Sysmon 工具和开源规则，构造更贴近实际采集流程的数据。

## 方法

系统将 MITRE ATT&CK 技术匹配与开源 Sysmon 过滤规则结合，生成 Rule-Filtered Provenance Graph（RFPG），在保留安全语义的同时压缩图规模。文本节点属性使用 Sentence-BERT 编码，数值边属性使用数值编码，并以统一的节点、边表示建模异构实体和交互。模型以 GAT 进行恶意节点分类，再用 ChebConv 完成谱特征细化；区间偏置在训练或推理阶段调整分类分数，以可控的精度代价降低漏报。

## 实验与结果

论文在 Windows 10 虚拟机中用 Sysmon 采集日志，结合 MITRE APT29、APT3、数据外泄和 CALDERA 场景构造两个 RFPG 数据集；恶意节点比例分别为 4.7% 和 5.1%，约 88.79% 和 88.92% 的边匹配到 ATT&CK 技术。模型以 20% 数据训练、80% 测试并重复 10 次；两个数据集的精度分别达到 90.58% 和 93.14%，误报率为 3.6% 和 2.9%。总体系统报告的准确率为 98.25%、精确率为 90.58%、误报率为 0.36%；推理时间 0.82 秒、完整流水线约 5 秒，较基线推理时间最多降低 10.8%，GPU 内存降低 11.4%。

## 贡献与局限

论文贡献是提供从公开日志采集、ATT&CK 匹配、RFPG 构建到 GAT 检测的端到端可复现流程，并用谱特征细化和区间偏置兼顾效率与召回。局限是攻击场景仍以模拟和 CALDERA 为主，数据存在类别不平衡；规则过滤可能影响对规则外或自适应攻击的覆盖，且当前评估尚未证明对真实生产环境和未知攻击的普适性。

---
DOI: 10.1109/tdsc.2026.3695911
