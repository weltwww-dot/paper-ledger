# Hardware-anchored assurance: A trusted resilience framework for critical edge infrastructure 总结

## 基本信息

- **标题**: Hardware-anchored assurance: A trusted resilience framework for critical edge infrastructure
- **作者**: Xinzhu Jiang, Bo Zhao, Peiwen Chen, Chunyu Yang, Juncheng Tong
- **期刊 / 会议**: Computers & Security · 2026首次在线；172 (2027): 105137
- **发表**: 2026-09-06
- **日期来源**: 出版社正式PDF第1页Available online；卷期年份不替代首次在线日期
- **内容状态**: 完整
- **内容说明**: 已对照16页出版社正式版复核中文与实验条件，替换原Journal Pre-proof
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105137
- **版本**: 出版社正式版（Version of Record），16页
- **PDF**: [COSE_2026_HardwareAnchoredAssurance.pdf](papers/COSE_2026_HardwareAnchoredAssurance.pdf)

## 一句话概括

TRCI将硬件信任锚、动态文件保护和可信恢复结合起来，使关键边缘设备在操作系统失陷、不配合恢复时仍能触发受控恢复。

## 问题与动机

静态硬件保护难以适应频繁更新的软件，纯软件监控又可能被高权限攻击绕过。关键基础设施既需要灵活指定受保护文件，也需要不依赖已失陷系统配合的恢复通道。

## 方法

Dual-Lock机制把软件定义的关键文件保护，与TPM支撑的身份验证、可信恢复执行结合。远程韧性管理方验证设备状态并签发延迟许可；异常或许可超时后由看门狗触发恢复，在隔离执行环境中还原可信文件（PDF第3—10页）。

## 实验与结果

在Raspberry Pi 4B与生产级x86网关上测试篡改、内存攻击及通信干扰。ARM平台500MB固件启动时间从3200增至3350毫秒，开销约4.7%；x86恢复500KB配置、50MB程序和500MB固件分别为74毫秒、439毫秒和3.76秒。结果依赖文件规模和硬件，不能当作固定恢复延迟（PDF第10—14页）。

## 贡献与局限

贡献是用已有硬件原语组织可更新、可强制触发的保护与恢复链。它不保证阻止全部内核内存攻击；物理完整性与可信基础设施是前提，侧信道等不在保障范围。恢复时屏蔽中断，因而不适合严格硬实时控制，也尚未验证大规模设备群协同恢复（PDF第14—15页）。

---
DOI: 10.1016/j.cose.2026.105137 | PDF: [COSE_2026_HardwareAnchoredAssurance.pdf](papers/COSE_2026_HardwareAnchoredAssurance.pdf)
