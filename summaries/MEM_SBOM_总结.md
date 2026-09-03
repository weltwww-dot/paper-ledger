# What You See Is Not What You Execute 总结

## 基本信息

- **标题**: What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security
- **作者**: Hala Ali, Andrew Case, Irfan Ahmed
- **期刊 / 会议**: Computers & Security 2026
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105125
- **arXiv**: 2606.22827
- **PDF**: [COSE_2026_MemoryRuntime.pdf](papers/COSE_2026_MemoryRuntime.pdf)

## 一句话概括

提出 MEM-SBOM，首个内存取证框架：直接从 Python 应用的运行时内存状态生成软件物料清单（SBOM），无需预先埋点，为供应链安全提供「实际执行了什么」的可信视图。

## 问题与动机

现代软件开发重度依赖公共仓库的第三方组件，扩大了软件供应链攻击面。SBOM 是提升透明度的标准化机制，但基于元数据或文件系统工件生成的 SBOM 无法捕获运行时实际加载执行的组件（尤其 Python 这类动态生态）；基于插桩的运行时 SBOM 又要求提前部署监控并全程可观测，在生产与应急响应场景难以满足。

## 方法

利用易失性内存（volatile memory）恢复应用真实运行时状态：从 Python 解释器内部结构恢复模块，解析包版本，分析字节码构建依赖图并识别可达的易受攻击函数；以 Volatility 3 插件套件形式实现。

## 实验与结果

对 51 个真实 Python 应用评估：模块提取准确率 100%；识别出 Streamlit 是唯一调用 tornado 依赖中漏洞例程的应用；恢复出现有 SBOM 工具遗漏的全部运行时包，依赖图更准确、漏洞评估更好（数字来自原文）。

## 贡献与局限

- 贡献一：首个直接从运行时内存生成 SBOM 的取证框架，无需预先插桩。
- 贡献二：字节码级依赖图 + 可达漏洞函数识别，提供更准确的供应链风险评估。
- 局限：当前聚焦 Python 生态；其他语言与大规模部署场景的覆盖待扩展。

---

DOI: 10.1016/j.cose.2026.105125
