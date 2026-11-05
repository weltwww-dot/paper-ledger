# Detecting and preventing lateral movement and privilege escalation attacks within microsoft active directory 总结

## 基本信息
- **标题**: Detecting and preventing lateral movement and privilege escalation attacks within microsoft active directory
- **作者**: Tegha Hamza Akwo、Dekai Zhang、Lu Yu 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105206
- **发表**: 2026-10-29
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105206
- **PDF**: [COSE_2026_VACIRActiveDirectory.pdf](papers/COSE_2026_VACIRActiveDirectory.pdf)

## 一句话概括
把Active Directory攻击路径与服务约束一起建模，借助优化求解选择横向移动和权限提升风险的加固干预点。

## 问题与动机
AD中的ACL、委派与会话关系会组合出多步攻击路径。枚举路径后仍需人工决定修复顺序，而直接撤销权限又可能破坏合法服务。

## 方法
VACIR将SharpHound数据和漏洞情报映射为加权有向图，关联账户、权限和会话状态。利用整数线性规划与SMT表达干预成本、攻击路径切断和服务保留条件，在给定模型内寻找可行且低成本的加固动作。

## 实验与结果
在一个受控企业域和三个公开AD数据集上评估，与BloodHound Analyzer比较；CoZure面向Azure AD，在本地SharpHound数据上没有可用输出，不能视为同条件有效基线。表3的本地实验域有420个用户、159个被列为高风险，识别128条权限提升路径；这些不是实际企业攻击发生率或检测精确率（PDF第15—16页）。

## 贡献与局限
连接攻击路径识别与可约束的修复决策，并提供实验案例。优化保证依赖图、成本及服务约束的准确性；受控域和公开图快照不能证明所有真实业务中修复都无中断，部署前仍需验证权限变化影响。

---
DOI: 10.1016/j.cose.2026.105206 | PDF: [COSE_2026_VACIRActiveDirectory.pdf](papers/COSE_2026_VACIRActiveDirectory.pdf)
