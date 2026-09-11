# What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security

## 基本信息

- 标题: What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security
- 作者: Hala Ali, Andrew Case, Irfan Ahmed
- 期刊 / 会议: Computers & Security 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1016/j.cose.2026.105125
- PDF: [COSE_2026_MemoryRuntime.pdf](papers/COSE_2026_MemoryRuntime.pdf)

- 标题: What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security
- 作者: Hala Ali, Andrew Case, Irfan Ahmed
- 期刊 / 会议: Computers & Security 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

作者为 Hala Ali、Andrew Case、Irfan Ahmed；发表于 *Computers & Security* 171 (2026) 105125。论文面向 Python 应用运行时的软件供应链盘点，提出从易失内存生成 SBOM、版本信息、字节码依赖图和可达漏洞函数信息。DOI: 10.1016/j.cose.2026.105125
## 一句话概括

MEM-SBOM 通过 Volatility 3 从运行中 Python 进程的内存恢复实际加载和执行的模块，弥补静态、构建期和部署期 SBOM 看不到动态依赖与真实函数可达性的缺口。

## 问题与动机

传统 SBOM 主要记录源代码、构建产物或部署包，无法可靠覆盖运行时动态导入、被删除的文件、被修改的模块或解释器内实际执行的依赖；部署后再插桩也可能已经太晚。仅按包名匹配漏洞还会产生大量误报，因为程序可能安装了易受攻击包，却没有调用易受攻击函数。论文希望在不预先改变应用的情况下，从内存恢复更接近运行事实的组件和漏洞可达性。

## 方法

MEM-SBOM 以多层内存取证流程遍历 `sys.modules`、线程上下文、垃圾回收对象、解释器 arena 和堆区域，逐级寻找 Python 模块对象、包元数据、版本与字节码。它结合模块属性、安装元数据和 PyPI 信息解析版本，输出 CycloneDX SBOM；再对字节码反汇编，构建模块/函数依赖图，并结合漏洞信息进行函数级可达性分析。多层设计还用于恢复被删除、覆盖、绕过正常导入、置于子解释器或受 GC 影响的模块。

## 实验与结果

作者在 51 个真实 Python 应用上评估，其中 23 个用于代表性比较；非对抗条件下对已安装、已导入和动态加载包的提取精确率与召回率均为 100%，检测到 10 个版本不一致。六种规避场景表明较低层内存扫描可以找回上层枚举遗漏的模块，但原生扩展或缺少 Python 模块对象时仍有限制。在 Tornado 漏洞案例中，六个应用按包级别都会被标记，只有 Streamlit 能到达易受攻击函数，函数级分析将 83.3% 的包级误报排除。与 8 个工具比较时，MEM-SBOM 的组件、包、依赖准确率和完整图指标均为 100%，版本准确率为 99.32%，漏洞识别 F1 为 100%；Syft 等工具的组件/依赖指标明显较低。单次处理时间约 70–3107 秒，堆扫描和图构建是主要开销。

## 贡献与局限

贡献是把运行时内存取证、SBOM 生成、版本校验和函数可达性连接起来，展示了比包清单更接近实际执行面的供应链审计方式。局限是当前聚焦 Python，内存扫描成本高，100% 结果主要来自非对抗样本；对恶意原生扩展、不同解释器/平台以及更强的内存混淆还缺少系统评估，函数图也依赖可恢复字节码与漏洞描述。后续应扩展到更多语言和原生代码，并加强对抗场景分析。

DOI: 10.1016/j.cose.2026.105125
