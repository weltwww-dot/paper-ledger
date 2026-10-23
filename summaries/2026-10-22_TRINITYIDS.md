# TRINITY-IDS: a tri-view hybrid architecture with adaptive drift-evidential learning for robust and continual intrusion detection 总结

## 基本信息
- **标题**: TRINITY-IDS: a tri-view hybrid architecture with adaptive drift-evidential learning for robust and continual intrusion detection
- **作者**: P. Palpandi、B. Sakthivel、R. Nandakumar、M. Ponnrajakumari
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25:179
- **发表**: 2026-10-22
- **日期来源**: Crossref published-online；不以2026-10-02录用日期替代
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01344-9
- **PDF**: [IJIS_2026_TRINITYIDS.pdf](papers/IJIS_2026_TRINITYIDS.pdf)

## 一句话概括
TRINITY-IDS融合统计、时序和拓扑三类网络流量表示，结合不确定性建模与漂移触发回放，研究持续入侵检测。

## 问题与动机
类别不平衡和数据集差异会影响检测，单一流量视图也难以同时表达局部属性、时间模式与实体关系。论文尝试在预测类别之外估计不确定性，并在分布变化后更新模型。

## 方法
先用Cluster-SMOTE与ENN处理不平衡，再以梯度反转抑制数据集来源特征。CNN、BiGRU和GAT分别编码三视图，动态融合后由Dirichlet证据分类头输出预测；Page-Hinkley检测漂移并触发经验回放。这里的对抗学习是域对齐，不等于已测试网络规避攻击。

## 实验与结果
表20中，随机80/20划分F1为98.29%，时间划分降至94.98%，跨网络为94.52%，未见攻击评估为93.18%。表18的漂移实验中，F1由漂移后88.94%逐轮恢复到95.00%（PDF第19—20页）。不同协议必须分开理解，不能把随机划分成绩当作真实持续部署或任意零日攻击成绩。

## 贡献与局限
将多视图、证据分类和漂移回放整合到同一检测流程。正文对漂移来源、时间切分及未见攻击类别的交代有限，数据来源与数据可用性声明也未充分协调，因此不足以确认自然漂移或可复现实网泛化。论文未提供端到端在线部署验证，降低复杂度与边缘部署仍列为后续工作（PDF第11、15、19—20页）。

---
DOI: 10.1007/s10207-026-01344-9 | PDF: [IJIS_2026_TRINITYIDS.pdf](papers/IJIS_2026_TRINITYIDS.pdf)
