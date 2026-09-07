# Uncovering Bluetooth vulnerabilities with binary coverage-guided fuzz testing and controller emulation 总结

## 基本信息

- **标题**: Uncovering Bluetooth vulnerabilities with binary coverage-guided fuzz testing and controller emulation
- **作者**: Zhao Min Chen, Tien-Chih Lin, Guan-Yan Yang, Yu-Sheng Lin, Farn Wang, Kuo-Hui Yeh
- **期刊 / 会议**: Computers & Security 168 (2026)
- **发表**: 2026-09-01（2025-07-27 投稿，2026-04-16 录用，2026-04-25 在线）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104929
- **arXiv**: 无
- **PDF**: [COSE_2026_UncoveringBluetoothFuzz.pdf](papers/COSE_2026_UncoveringBluetoothFuzz.pdf)

## 一句话概括

本文提出 FuBuKi，一个基于二进制重宿主与控制器模拟的覆盖率引导蓝牙模糊测试框架，无需物理设备与源码即可对 BR/EDR 应用层协议（如 SDP、RFCOMM、AVRCP）进行漏洞挖掘。

## 问题与动机

Bluetooth BR/EDR 广泛内嵌于消费电子与车载系统中，且其漏洞数量近年显著增长，尤其在 AVRCP、PBAP、SDP 等高层应用配置文件上（如 BlueBorne、BleedingTooth、Pwn2Own 2023 中利用蓝牙入侵特斯拉等事件）。现有蓝牙模糊测试研究主要存在三类局限：一是只能探测协议栈底层（如针对 L2CAP 的 L2Fuzz）；二是依赖物理设备、目标源码或特定仪器化手段（如 SweynTooth、VirtFuzz）；三是整体覆盖率低或未知（如 ToothPicker 在 iOS 蓝牙栈仅达到约 3% 覆盖率）。高层配置文件大多是有状态的，需先完成连接建立、信道协商乃至配对，如何高效地把变异字节送入 L2CAP 之上的应用层解析器是核心难题。

## 方法

FuBuKi 是一个基于 AFL++ 的二进制覆盖率引导模糊测试框架，专门面向 BR/EDR 主机侧应用配置文件（L2CAP 之上），架构包含四部分：(1) Profile-Aware Proxy——以真实蓝牙协议栈作为对端建立合法会话，并用用户编写的 profile 专用 Input Transformer（基于 Bumble/Scapy 等 Python 库，评估中 43–217 行 Python，另有一车载目标需 108 行平台相关 C 辅助代码）把 AFL++ 的变异缓冲注入合法报文模板的指定载荷字段（如 SDP 的 ServiceSearchAttributeRequest），保持底层头部与校验有效；(2) Target Environment——用 LIEF 对逆向出的目标二进制做一次性补丁，注入 trampoline 式 harness 以稳定截获并反复重入目标解析入口（如 avrcp_handle_pdu），配合 fork-server 模式从保留的准备态（已建立的 ACL/L2CAP/配置文件上下文）派生子进程逐条执行变异报文；(3) HCI Emulation Bridge——基于 Google Rootcanal 模拟蓝牙控制器，并用自研 Virtual Serial Shim 将目标栈按 UART（PTY）收发 HCI H4 帧转换为 Rootcanal 所需的 TCP 报文，实现无物理硬件的控制器虚拟化；(4) Fuzzing Engine——采用 AFL++ QEMU 模式收集运行时二进制覆盖率。整体为固定前缀、单报文变异模型，支持多实例并行模糊。

## 实验与结果

实验平台为 AMD Ryzen 9 7900X + 64 GB 内存 + Ubuntu 22.04，物理对照使用树莓派 4B 配 TP-Link UB500 蓝牙 5.0 适配器；设计了覆盖 BlueZ L2CAP、BlueZ RFCOMM、BTstack SDP、商业汽车固件 ECU（闭源、媒体控制服务）、BlueZ AVRCP（CVE-2023-27349 元数据解析）五个场景。首次崩溃时间（对比 L2Fuzz 与 Frankenstein，基线均未触发崩溃）：场景 A 11 秒、B 22 分 22 秒、C 13 分 17 秒、D 9 秒、E 41 秒。案例一在汽车 ECU 固件 9 秒内发现栈缓冲区溢出（CWE-121，位于解析厂商媒体属性的函数）；案例二 41 秒复现 CVE-2023-27349——将 AVRCP PDU ID 变异为非法值 0x82，使 avrcp_handle_pdu 的 switch 缺少 default 分支而断言崩溃。RQ1 仿真开销：1000 次 SDP 请求平均延迟物理约 0.08 秒、仿真约 0.23 秒（约 3 倍），但可并行消除硬件瓶颈；RQ3 24 小时对比中，post-handshake 设置下 FuBuKi 在 BTstack A2DP 源服务器上的累计基本块覆盖率持续高于 L2Fuzz，且内存稳定（L2Fuzz 反复出现内存尖峰），pre-handshake 端到端设置下覆盖率也显著高于 Frankenstein；RQ4 并行扩展（BTstack SDP 客户端）：单机实例从 5 增至 55，聚合吞吐从 2.15 升至 17.05 exec/s（约 7.9 倍），单实例吞吐从约 0.42–0.44 降至 0.31 exec/s，55 实例时平均内存仅 4.30 GB，60 实例时 CPU 过载。另用 angr 静态分析估计 FuBuKi 覆盖了 A2DP 子系统可达 BR/EDR 基本块的约 80.6%。

## 贡献与局限

贡献：提出 FuBuKi——首个针对 L2CAP 之上 BR/EDR 应用配置文件、无需源码与物理设备的二进制重宿主蓝牙模糊器；设计了 profile-aware proxy + Input Transformer 以有效抵达高层配置文件（包括需配对/绑定的 AVRCP 等）；架构支持并行模糊显著缩短漏洞发现时间；在真实商业汽车固件中发现此前未报告的崩溃，并复现已知 CVE-2023-27349。局限：当前采用固定前缀、单报文变异模型，尚不支持对同次交互中多报文联合变异的一般序列模糊；基于 LIEF 的离线补丁不适用于加壳或强签名/文件完整性保护的二进制（拟以 QEMU 插件或 DBI 动态挂钩替代）；仿真引入约 3 倍每报文延迟且每次迭代重建连接带来 0.5–1.4 秒握手开销（拟引入 Nyx 式快照模糊约可提升一个数量级）；对无 UART 接口的平台（如 Windows 驱动栈、ESP32 等 IoT 固件的 MMIO）可移植性受限；另计划用 LLM 辅助生成 Input Transformer 骨架并辅以校验以减少人工适配。

---
DOI: 10.1016/j.cose.2026.104929
