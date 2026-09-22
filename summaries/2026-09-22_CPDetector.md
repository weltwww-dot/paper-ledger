# CPDetector: Automated detection of excessive permissions in Chrome extensions 总结

## 基本信息

- **标题**: CPDetector: Automated detection of excessive permissions in Chrome extensions
- **作者**: Xiaoyu Cheng、Zhi Wang、Wanpeng Li et al.
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-18
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105173
- **arXiv**: 无
- **PDF**: [COSE_2026_CPDetectorChromePermissions.pdf](papers/COSE_2026_CPDetectorChromePermissions.pdf)

## 一句话概括

CPDetector 通过静态比对 Chrome 扩展 manifest 中声明的权限与源码中检测到的 API 调用，筛出权限—API 不匹配候选，并以 PermissionGuard 在用户侧提示潜在的过度授权风险。

## 问题与动机

Chrome 的权限模型粒度较粗，用户通常只能整体接受扩展权限；未实际使用的高权限会扩大后续更新、供应链接管或动态加载代码的潜在攻击面。权限与 API 不匹配本身不等同于恶意行为，但面对近二十万扩展，缺少可扩展的初筛工具会使最小权限原则难以审计。

## 方法

框架依次收集 Chrome Web Store 元数据和 CRX 包、解析 manifest 的 API 与 host 权限、扫描 JavaScript 中的 API 标识符，并以权限—API 映射表发现未见相应调用的声明。针对 host 权限另设条件化判据以处理 cookies 等 API 与 host scope 的强制耦合；随后将候选结果供 PermissionGuard 在安装或使用扩展时提示，而不是将候选直接定性为恶意扩展。

## 实验与结果

作者截至 2025 年 5 月分析 199,058 个扩展，CPDetector 标记 98,072 个（49.3%）为 API 权限不匹配候选，共记录 197,646 项不匹配；其中 activeTab 和 scripting 分别占 25.11% 与 17.51%。AST 对比版本标记 92,481 个（46.5%），论文将差异归因于 AST 较精确但运行开销更高；修订后的 host-permission 程序标记比例为 5.68%–9.15%。

## 贡献与局限

- 给出面向 Web Store 规模的权限—API 静态初筛管线，并同时考虑 Manifest V2/V3 与 host 权限情形。
- 将检测结果接入 PermissionGuard，帮助用户在扩展使用阶段识别需要进一步审查的权限组合。
- 局限：JavaScript 动态拼接、远程配置、代码混淆和未触发路径都会造成静态分析假阳性或假阴性；被标记仅是风险分诊信号，不能证明扩展存在恶意行为。

---
DOI: 10.1016/j.cose.2026.105173
