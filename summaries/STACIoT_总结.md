# STAC-IoT: A secure task-based access control for IoT-edge computing architecture 总结
## 基本信息
- **标题**: STAC-IoT: A secure task-based access control for IoT-edge computing architecture
- **作者**: Hicham Degdeg, Mohamed Lehsaini, Youcef Imine
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104915
- **PDF**: [COSE_2026_STACIoT.pdf](papers/COSE_2026_STACIoT.pdf)
## 一句话概括
STAC-IoT以多授权机构属性加密和边缘节点为基础，对IoT设备任务实施去中心化、细粒度访问控制。
## 问题与动机
集中式授权、粗粒度策略和较高计算开销不适合资源受限的边缘IoT。跨域用户还需要在各自管理属性的同时协作执行策略。
## 方法
协议使用多授权属性基加密保护任务令牌，各机构独立管理属性并协作制定策略；Shamir秘密共享保证凭证唯一性，边缘节点发放可复用凭证，设备本地检查权限。
## 实验与结果
智能制造场景验证了可扩展性、安全性和能效；形式化分析表明协议抵抗中间人、冒充和令牌伪造攻击。论文报告较低开销，但未在此处补写具体数值。
## 贡献与局限
贡献是结合任务级授权、多授权机构、边缘凭证和本地检查。局限是机构协作、撤销与密钥同步在大规模动态设备上的成本仍需评估。
---
DOI: 10.1016/j.cose.2026.104915
