# Measuring network-level internet censorship: DNS and IP-based filtering across Iraqi residential ISPs 总结

## 基本信息

- **标题**: Measuring network-level internet censorship: DNS and IP-based filtering across Iraqi residential ISPs
- **作者**: Ameer Al-Dujaily, Bahaa Al-Musawi
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104956
- **arXiv**: 无
- **PDF**: [COSE_2026_Paper02.pdf](papers/COSE_2026_Paper02.pdf)

## 一句话概括

本文通过四个伊拉克住宅网络的主动测量，比较 DNS 干扰与 IP 封锁，并揭示集中政策在不同 ISP 上产生的不均衡过度封锁。

## 问题与动机

伊拉克的监管和网络架构较为分散，互联网过滤的执行方式、透明度和责任边界缺少实证测量。作者关注 DNS 与 IP 层过滤在不同住宅 ISP 上是否一致，以及共享托管导致的附带影响。

## 方法

研究在 2025 年对四个住宅网络开展两轮为期一个月的主动测量，包括三个固定 ISP 和一个移动运营商。测试集合包含 Majestic Million 的 50,000 个热门域名及超过 100,000 个通信部官方测试列表域名；使用 ZDNS 检测 DNS 干扰、Nmap 评估 IP 可达性、IPinfo 进行域名到 IP 映射，并用 FortiGuard 分类内容。

## 实验与结果

在热门域名列表中，386 个域名在四个网络上均被阻断；四网共有 195 个被阻断 IP 地址。DNS 干扰是最一致的机制，而 IP 封锁在 ISP 之间差异更大，并因共享 IP 造成商业、信息技术和教育类域名的过度封锁。

## 贡献与局限

贡献是提供了伊拉克住宅网络层面的可复现实测证据，并区分了 DNS 与 IP 封锁的治理后果。局限是覆盖范围集中于住宅网络和有限测量期，未来仍需扩展到其他地区、企业网络以及 HTTP/TLS 应用层验证。

---
DOI: 10.1016/j.cose.2026.104956
