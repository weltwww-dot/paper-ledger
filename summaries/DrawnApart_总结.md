# DRAWNAPART: A Device Identification and Spoofing Detection Technique Based on Remote GPU Fingerprinting 总结

## 基本信息

- **标题**: DRAWNAPART: A Device Identification and Spoofing Detection Technique Based on Remote GPU Fingerprinting
- **作者**: Tomer Laor、Naif Mehanna、Antonin Durey et al.
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **发表**: 2026-09-07
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3830402
- **arXiv**: 无
- **PDF**: [TOPS_2026_DrawnApart.pdf](papers/TOPS_2026_DrawnApart.pdf)

## 一句话概括

DrawnApart 利用同型号 GPU 的制造差异建立远程硬件指纹，在传统浏览器指纹基础上增强同配置设备区分能力，并可检测伪造 GPU 渲染器信息的设备冒充。

## 问题与动机

浏览器指纹可用于安全识别与跟踪，但软件版本和配置会随时间变化，使长期指纹容易与采用相似软硬件的其他设备混淆。攻击者还可能伪造设备属性，绕过依赖“熟悉设备”的二次认证机制。

## 方法

方法通过浏览器可执行的图形工作负载，测量名义上相同 GPU 因制造差异产生的稳定响应特征，从而形成远程 GPU 指纹。它既可与 FP-Stalker 等传统指纹组合，也能核验浏览器报告的 GPU renderer 字符串是否符合实际硬件行为。

## 实验与结果

摘要称，该技术能在软硬件配置相同的设备之间带来具有实际意义的识别精度改进；在设备环境更异构时，与传统浏览器指纹联合使用效果最佳。它还能识别通过模仿受害者设备属性绕过二次认证的欺骗尝试，但摘要未提供具体准确率。

## 贡献与局限

贡献是把 GPU 制造差异引入远程设备识别，并兼顾安全防伪与细粒度区分。局限在于强指纹能力本身可能加剧隐私跟踪风险；长期稳定性、浏览器隔离策略及驱动更新对特征的影响仍需进一步判断。

---
DOI: 10.1145/3830402
