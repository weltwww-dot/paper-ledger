# Exploiting CPython’s just-in-time optimization: StencilLeak attack 总结

## 基本信息
- **标题**: Exploiting CPython’s just-in-time optimization: StencilLeak attack
- **作者**: Seehwan Yoo、Youngpil Kim、Chuck Yoo
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105203
- **发表**: 2026-10-26
- **日期来源**: 出版社正式PDF首页Available online；2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105203
- **PDF**: [COSE_2026_StencilLeak.pdf](papers/COSE_2026_StencilLeak.pdf)

## 一句话概括
分析CPython实验性copy-and-patch JIT形成的代码复用攻击面，说明模板字节和运行时补丁如何共同影响劫持后的原生代码链。

## 问题与动机
JIT会生成新的可执行内存，安全评估需要同时考虑固定模板和动态填入的地址字节；仅检查解释器静态二进制不足以刻画新增攻击面。

## 方法
针对CPython 3.14的x86_64实现，区分模板固有片段与运行时补丁产生的非对齐片段。通过插桩提供既定内存和控制状态，验证劫持后代码复用；再用独立新进程测试完整所需片段集合的可获得性。

## 实验与结果
在启用ASLR、关闭垃圾回收、每进程最多搜索两小时的固定负载下，500次试验有251次找到全部所需片段，比例为50.2%。这是片段集合发现率；完整代码链的执行由另行提供前置能力的插桩实验验证，两者不能合并为端到端攻击成功率（PDF第1、11—13页，表10—11）。

## 贡献与局限
揭示固定模板与随机补丁字节共同构成的运行时代码复用风险。攻击依赖独立内存安全漏洞提供重复读取、可写存储及受控跳转，且所演示链受硬件影子栈等控制流防护约束；未验证真实完整漏洞链，结果也受具体构建、架构、负载和搜索预算限制（PDF第2—3、14—16页）。

---
DOI: 10.1016/j.cose.2026.105203 | PDF: [COSE_2026_StencilLeak.pdf](papers/COSE_2026_StencilLeak.pdf)
