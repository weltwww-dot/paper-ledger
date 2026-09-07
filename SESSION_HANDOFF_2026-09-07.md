# 工作交接：论文台账更新 + InstSci 批量获取 + 129 篇本地入库

> **最新状态（2026-09-07，本轮提交前）**：用户已授权提交并推送。全库 586 份六段式总结已完成中文文案审校：展示内容不再含流程性确认措辞；已重写 4 份检出的失真摘要。新增 `scripts/summary_quality_gate.py`，并接入 `update / advance / publish`；自动直译入口已停用，后续新增记录须由执行 agent 对照可核验原文写中文六段式，且 PDF 获取仍在该环节前完整执行。实测五道闸门均通过、顶层 273 个 PDF 均有效、28 项测试通过。台账状态仍为 complete 222 / partial 304 / pending 60；58 篇 `partial+PDF` 为历史技术债。

> **维护约定（2026-09-07 用户指示）**：本文件是**持续更新的交接文档**——今后每个 agent 接手工作时都先读本文件；每次工作进展、状态变化、未完成事项的更新**直接改这一个文件**（更新对应小节 + 在文末「更新日志」追加一行），不要再新建一次性快照。
>
> 面向后续接手的 agent。先读本文件；稳定流程与字段定义以 `更新工作流.md`、`CONTEXT.md` 及项目脚本为准。
> 本文件记录当前工作已做的事、仓库现状、**还没做完的事**及续做路径（会随会话持续更新）。

## 0.1 接手时先做什么

1. 先读本文件，再运行四道验收：`python scripts/summary_gate.py --check`、`python scripts/theme_gate.py --check`、`python scripts/pdf_gate.py --check`、`python scripts/workflow_gate.py --check`。
2. 日常“更新”只用 `python scripts/run_update.py update`；它必须经过本地中文翻译、PDF 探测/下载/校验/证据登记、同步和四道闸门，不能只运行抓取步骤。
3. 继续补全文时，先处理 `contentState=pending`；有全文后必须“读全文 → 自己写中文六段式 → 复制规范 PDF 到 `papers/` → 删除占位 → sync → 四道闸门”。不要重复处理已完成的 `verified_resume/` 76 个文件。
4. 当前仍有 60 篇 pending、31 篇 Elsevier 续跑 DOI 和 58 篇历史 `partial+PDF` 技术债；后两者分别按 §3.2、§3.4 处理。WAF 续跑必须等用户明确说开始，GitHub 发布必须等用户明确授权。
5. 完成后只更新本文件对应小节，并在 §6 追加一行；不要创建新的 handoff 快照。

## 0. 一句话概述

执行了一次「更新」闭环（无真正新增论文），用 InstSci（中国农业大学 CARSI 机构通道）完成待补全 PDF 的获取与整理。前一批 129 篇加上续跑目录中的 76 个文件已完成核验：其中 73 篇研究论文已全部规范化入库（中文六段式总结 + 规范 PDF + 内容状态更新 + 同步 + 闸门通过），另有 3 个 TNNLS 文件核验为非研究性期刊页面并明确排除。当前台账保持 586 篇，顶层有效 PDF 为 273 个。**未执行 advance / publish / git push（用户当前仍未要求发布）**。

> 注：原文件名带日期 `SESSION_HANDOFF_2026-09-07.md`，作为长期维护文档保留该文件名即可，内容按「更新日志」持续追加。

## 1. 本会话完成了什么

### 1.1 修复阻塞 bug（已改 2 个脚本，均已编译验证）
- 症状：`python scripts/run_update.py update` 启动即失败 `WinError 206（文件名或扩展名太长）`。
- 根因：`scripts/run_update.py fetch()` 把 data/papers.js 全量标题（586+ 条）逗号拼接成 `--existing-titles` 命令行参数，超过 Windows 命令行上限。
- 修复：
  - `scripts/run_update.py`：新增 `write_temp_json()`，把 `dois` 与 `titles` 写到系统临时 JSON；`fetch()` 改为传 `--existing-dois-file` / `--existing-titles-file`；`finally` 清理临时文件。新增 `import os, tempfile`。
  - `scripts/fetch_incremental.py`：新增 `--existing-dois-file` / `--existing-titles-file` 参数（JSON 数组文件），与原逗号参数兼容合并。

### 1.2 完整更新闭环（无新增）
- `python scripts/run_update.py update` 完整跑通，exit 0。
- 抓取结果：17 刊双来源审计无失败；候选 4 条（3×IEEE TDSC + 1×TNNLS）**均早已在库**（586 篇内、已有总结），导入层按 DOI 正确去重 → **本轮实际 0 新增**，翻译/主题 0 篇属正常。
- 四道闸门（summary/theme/pdf/workflow）全绿；25 项单元测试通过。

### 1.3 InstSci 机构 PDF 获取（成功 129 篇）
- 队列：`run_update.py instsci` 生成 236 篇 pending 队列（`skill-runs/fulltext_queue.txt`），按出版社拆分 IEEE 103 / Elsevier 133。
- 机构路线：CARSI SSO，IdP=中国农业大学（`.instsci` 配置已有，只读了机构字段，未动/未提交任何凭据）。
- route-check：无代理直连，判定通过；出口为北京电信宽带 IP（非校园网），但实际经 stampPDF 机构授权通道成功，PDF 水印为 "Authorized licensed use limited to: China Agricultural University"——机构访问真实有效。
- CloakBrowser：本机已有缓存 `C:\Users\Administrator\.cloakbrowser\chromium-146.0.7680.177.5`，设置 `$env:CLOAKBROWSER_CACHE_DIR="C:\Users\Administrator\.cloakbrowser"` 避免重复下载。
- 结果：
  - **IEEE 103 → 53 篇**（OA-first / publisher_open_pdf / 浏览器流程混合），50 未完成。
  - **Elsevier 133 → 76 篇**（primary 74 成功 + 少量 OA），5 篇失败有诊断证据（`pdf_not_captured` / 下载超时），57 未完成。
  - 两批均已主动停止（job_kill），原因：ScienceDirect 触发 WAF 风控（页面提示「检测到异常活动，会自动解除，请稍后重试」），继续跑只会加剧封锁。

### 1.4 129 篇本地规范化入库（前一批核心成果）
- 已获 129 篇 PDF 全部入库，方式：每篇由独立子代理**读全文文本 → 撰写完整中文六段式总结 → 复制规范 PDF 到 papers/ 顶层 → 删除旧「待补全_xxx.md」占位文件**。
- 总量核对：129 新总结文件 + 129 规范 PDF + 129 占位删除，一一对应，无重复。
- PDF 命名规范：`papers/<期刊前缀>_<年份>_<slug>.pdf`（如 `TDSC_2026_AlphaBetaCore.pdf`、`NN_2026_PGMNO.pdf`）；slug 由子代理按标题拟定并查重。
- 总结格式：六段式（基本信息/一句话概括/问题与动机/方法/实验与结果/贡献与局限），基本信息含真实作者、DOI、PDF 链接，内容状态标「完整 · 已基于机构授权全文完成中文六段式总结」。
- 全程纪律：不编造数字/作者/结论；个别 DOI（如 TAI 刊头页 Publication Information）如实标注为非研究论文，不硬编方法实验。
- 支撑文件（可复用）：
  - `skill-runs/instsci_tasks.json`：124 篇（129−5 试点）任务清单（doi/title/journal/prefix/txt/placeholder/pdf_src）。
  - `skill-runs/instsci_doi_pdf_map.json`：DOI → 原始 PDF 路径映射（135 条）。
  - `skill-runs/instsci_batch_guide.md`：批量子代理操作协议（格式模板 + 步骤 + 自检）。
  - `skill-runs/tasks/instsci_task_001.json` … `_124.json`：单篇任务 JSON。
  - `skill-runs/txt/instsci/*.txt`：从 PDF 提取的全文（fitz/PyMuPDF，InstSci venv `C:\Users\Administrator\Documents\Codex\tools\instsci-venv\Scripts\python.exe` 有 fitz）。已被 `.gitignore` 排除。
- 数据同步：`node scripts/sync-papers.js` 已跑，`data/papers.js` 586 篇无重复，版本号已更新（index.html）。

### 1.5 续跑目录 76 个文件的最终整理
- `papers/instsci/verified_resume/` 中 76 个文件已按 DOI 与全文内容逐一核验：73 篇是真正研究论文，全部已完成中文六段式总结和顶层 PDF 规范化；3 篇 TNNLS 文件分别是出版信息页、学会委员会名单页和作者投稿须知页，已保留审计记录但未伪装成研究论文入库。
- 本轮新增两篇 TKDE 的完整总结与 PDF：`TCAAAnchorAlignment_总结.md` / `TKDE_2026_TCAAAnchorAlignment.pdf`，`OCDMMultistageCausalDiscovery_总结.md` / `TKDE_2026_OCDMMultistageCausalDiscovery.pdf`。
- 修复 `scripts/sync-papers.js` 的 DOI 优先对账逻辑：删除占位文件后，已有记录若暂时没有替代总结也不会从 `data/papers.js` 静默丢失；已通过 586 篇台账和全部闸门校验。

## 2. 当前仓库状态（2026-09-07，76 个续跑文件已整理后）

> 注：本表为当前工作区实测口径。`verified_resume/` 中的 76 个文件已完成分类：73 篇研究论文已入库，3 篇非研究性页面只保留审计证据，没有复制到顶层研究论文库。

| 项 | 值 |
| --- | --- |
| 台账论文总数 | 586 篇（未变） |
| contentState 分布 | complete 222、partial 304、pending 60、空 '' 0 |
| data/papers.js 带 PDF 字段 | 268 篇 |
| papers/ 顶层有效 PDF | 273 个 |
| 历史技术债：有 PDF 但 contentState=partial | 58 篇（后续全文补全时升级为 complete） |
| **续跑文件（verified_resume/）** | **76 个已完成分类（研究论文 73 个已入库；非研究页面 3 个排除）** |
| papers/instsci（原始下载） | 已加入 .gitignore，不入库 |
| pdf_attempts.json | 489 条（blocked 48 / not-oa 437 / no-file 1 / non_research_document 3） |
| 四道闸门 | summary ✅ / theme ✅ / pdf ✅ / workflow ✅ |
| 单元测试 | 25 项 OK |
| git | 变更全部未 commit、未 push |

工作区未提交变更大致分五类：
1. 脚本修复：`scripts/run_update.py`、`scripts/fetch_incremental.py`、`.gitignore`（新增 `papers/instsci/` 排除）。
2. 生成数据：`data/papers.js`、`data/theme-tags.json`、`index.html`、`skill-runs/*.json`（collection_audit/records_inc/oa_inc/content_inc/pdf_probe/pdf_downloads/content_attempts）。
3. 新增 129 份总结 `summaries/<slug>_总结.md` + 129 个 `papers/<前缀>_<年>_<slug>.pdf`。
4. 删除 129 个占位 `summaries/待补全_*.md`。
5. 标准流程整改：新增 `scripts/workflow_gate.py`、`skill-runs/workflow_baseline.json` 及测试；`run_update.py` 已将总体验收接入 update/advance/publish；补齐 3 条旧总结的内容状态；更新 `更新工作流.md`、`README.md` 和本交接文件。

## 3. 未完成事项与职责分工（2026-09-07 更新）

> **当前分工约定（用户指示）**：WAF 续跑仍由本会话 agent 负责，必须等用户明确说“开始跑”后执行；本批 76 个已下载文件的本地整理已完成，后续只需维护本文件中的真实状态。

### 3.1 职责总览

| 事项 | 负责方 | 状态 |
| --- | --- | --- |
| WAF 续跑 107 篇 PDF（第一轮） | 本会话 agent（我） | ✅ 已完成部分：IEEE 50/50 全补齐；Elsevier 26 篇新获（见 §3.2 与 §6） |
| Elsevier 剩余 31 篇续跑（第二轮） | 本会话 agent（我） | ⏸ 已暂停（用户指示），续跑清单已更新，待用户再次说开始时继续 |
| 续跑结果记录 | 本会话 agent（我） | ✅ 已写入 §6 更新日志 + 本节 |
| 已下载 PDF 的本地入库（76 个续跑文件） | 本会话 agent | ✅ 已完成：73 篇研究论文入库，3 篇非研究页面排除 |
| 内容状态收尾（空状态 3 条等） | 本会话 agent | ✅ 已补齐，当前无空状态；剩余 60 篇 pending 按补全队列推进 |
| advance / publish / git push | 待用户指示 | ⏸ 用户要求先只整理本地 |

### 3.2 WAF 续跑（第一轮结果 · 2026-09-07）

**已执行并暂停。结果：**
- **IEEE 50/50 全部补齐**（`papers/instsci/ieee_batch_2/`，manifest 全 success + verified）。`skill-runs/instsci_ieee_remaining.txt` 已清空。
- **Elsevier 26/57 新获**（`papers/instsci/elsevier_batch_2/`）：26 篇 `pdf_response_captured + verified=True`（真论文）；2 篇 verified=False 为**期刊编委会/表单类非论文**（`10.1016/s0004-3702(26)00119-0` = AIJ 编委会页、`10.1016/s0893-6080(26)00678-7` = INN 会员申请表）；1 篇 `pdf_not_captured`（`10.1016/j.neunet.2026.108872`）。
- Elsevier 中断原因：`TargetClosedError`（浏览器上下文在第 30/57 篇时被关闭）——非 SD WAF。此前另一次失败根因是**残留 CloakBrowser 进程占用 chrome-profile**，已清理（`Stop-Process` 匹配 `\.cloakbrowser` + `instsci\chrome-profile` 的进程）。
- **汇总文件**：`skill-runs/instsci_resume_results.json`（ieee_batch2 50 条 + elsevier_batch2_verified 26 条 DOI 列表）。
- 剩余队列已更新：`skill-runs/instsci_ieee_remaining.txt` = 0 条；`skill-runs/instsci_elsevier_remaining.txt` = 31 条（待续跑）。

**第二轮续跑（等用户指示再跑）命令要点：**
```powershell
# 1) 预检清理（残留进程 + 浏览器缓存），每次跑批量前必做：
powershell -ExecutionPolicy Bypass -File scripts\instsci_preflight.ps1
# 2) 续跑 Elsevier 剩余队列（单批建议 ≤25 篇；命中 WAF 立即停）：
instsci papers skill-runs\instsci_elsevier_remaining.txt --publisher elsevier --institution "中国农业大学" --oa-first --login-timeout 900 --pdf-timeout 120 --concurrency 1 --output papers\instsci\elsevier_batch_3 --no-broker
```
- 命中 SD WAF 时**立即停止**等自动解除；Elsevier 触发风控时退回单 DOI。不要并发双出版社同打 SD。
- 续跑完成后：新 PDF 复制入 `papers/instsci/verified_resume/`，更新 remaining 清单，并在 §6 追加结果；本批本地整理已完成。

### 3.3 续跑文件本地整理结果（已完成）

> **续跑成果目录：`papers/instsci/verified_resume/`（76 个，IEEE 50 + Elsevier 26），全部通过 `%PDF` 校验。**对应 DOI 清单：`skill-runs/instsci_resume_results.json`。本批已经完成研究性筛选、全文总结、PDF 归位和台账同步。

**§3.3.1 先校验当前仓库自洽（不依赖新 PDF）：**
```powershell
python scripts/verify_papers.py --check          # papers/ 顶层 PDF 全部有效
python scripts/summary_gate.py --check           # 六段式 + 中文一句话
python scripts/theme_gate.py --check             # 主题标签
python scripts/pdf_gate.py --check               # 无 PDF 论文均有证据
python scripts/workflow_gate.py --check          # DOI/总结/状态/主题/PDF/证据一致
python -m unittest discover -s tests -v          # 25 项
git diff --check
```

**§3.3.2 已完成的分类与入库：**
1. 73 篇研究论文均已由机构授权全文完成中文六段式总结，PDF 已按期刊与标题 slug 复制到 `papers/` 顶层，并删除对应占位总结。
2. 3 个非研究页面未写成伪论文总结：`10.1109/tnnls.2026.3723914`（出版信息页）、`10.1109/tnnls.2026.3723916`（学会委员会名单页）、`10.1109/tnnls.2026.3723918`（作者投稿须知页）。它们在 `skill-runs/pdf_attempts.json` 中标记为 `non_research_document`，占位文件保留为明确的排除说明，且没有顶层研究 PDF。
3. `node scripts/sync-papers.js` 已重新生成 `data/papers.js`，台账为 586 篇；同步脚本已按 DOI 优先保留原记录和 ID，避免占位删除导致条目丢失。
4. `verify_papers`、`summary_gate`、`theme_gate`、`pdf_gate`、`workflow_gate`、25 项单元测试和 `git diff --check` 均已通过。

**§3.3.3 后续维护：**
- 新一轮 PDF 入库或非研究页面排除后，继续只更新本文件 §2 和 §6；不要另建 handoff 快照。
- 不在其他文档复制或维护这些实时数字。

**§3.3.4 提交与发布（仅当用户说可以更新 GitHub 时）：**
- 用户当前要求：只整理本地。**不要 push**；commit 与否听用户指示。
- 如需 commit：分逻辑组（脚本修复 / InstSci 产物 / 总结+PDF / 生成数据），或按用户习惯整体提交。
- 发布（用户许可后）：`python scripts/run_update.py advance` → `python scripts/run_update.py publish`（push + 等 Pages 构建 + 线上篇数比对，以线上数量一致为准）。

### 3.4 内容状态收尾
- 当前 60 篇 pending（主要是剩余无 PDF 或非研究页面记录）与 304 篇 partial（已有部分内容）仍需后续按证据推进；已处理的 76 个续跑文件不再重复入库。
- 3 条历史空状态已补为 `完整 · 已基于公开摘要完成中文六段式总结`，重新同步后当前无空状态；以后 `workflow_gate.py` 会阻止空状态进入 advance/publish。
- 其中 58 篇是历史遗留的“已有 PDF 但 partial”条目，来源于早期只完成摘要翻译的流程；总体验收会显式警告，后续新增论文不得复制这种状态，补全时必须读全文并升级为 `complete`。

### 3.5 发布相关（用户暂缓，等指示）
- 用户明确：**先整理本地，暂不更新 GitHub**。
- 待用户说「可以了」后再执行：
  ```powershell
  python scripts/run_update.py advance    # 推进 last_update.json 基准（前置：四道闸门过）
  python scripts/run_update.py publish    # git push + 等 Pages 构建 + 线上篇数比对
  ```
- 发布前检查：`data/papers.js` 已重新生成；提交应同时包含事实来源（summaries、theme-tags、PDF/证据）与生成数据。
- commit 提示：把 411 个变更分逻辑组提交更清晰（脚本修复 / InstSci 产物 / 总结+PDF），或按用户习惯整体提交。

### 3.6 项目改进（2026-09-07 已落地）
- **新增 `scripts/workflow_gate.py`**：全量核对 586 条台账与 586 份总结的 DOI 集合、内容状态、主题、PDF 链接和 `pdf_attempts.json` 跳过证据；完整总结不能留下纯占位段落，非研究页面必须有可审计说明。
- **接入四道闸门**：`run_update.py update`、`advance`、`publish` 现在都会执行 `summary_gate`、`theme_gate`、`pdf_gate` 和 `workflow_gate`；单独执行 `pdf_gate.py --mark` 也要求合法原因与非空 note。
- **清理历史状态**：补齐 3 条旧总结的 `内容状态`，当前 `contentState` 为 complete 222 / partial 304 / pending 60 / 空 0。
- **记录历史技术债**：当前有 58 篇旧条目已具备 PDF 但仍为 `partial`；总体验收只警告并阻止数量继续扩大，后续应按全文六段式流程逐篇升级。
- **新增历史债务上限基线**：`skill-runs/workflow_baseline.json` 将 58 设为 `partial+PDF` 最大允许值；后续只允许下降，不允许新流程增加。
- **新增 `scripts/instsci_preflight.ps1`**：InstSci 批量前预检/清理脚本——自动清理残留 CloakBrowser 进程（修复 `TargetClosedError`）、探测并设置 `CLOAKBROWSER_CACHE_DIR`、检查残留 broker；已接入 `instsci_batch_local_ip.ps1` 出口预检之前。
- **`更新工作流.md` 新增 §9.4**「InstSci 机构 PDF 获取踩坑记录」：沉淀 2026-09-07 实测症状/根因/修复（残留进程、批量过大、SD WAF 风控、非论文页误入库、输出目录重复计数等）。
- **`更新工作流.md` §9.3 缓存路径修正**：`CLOAKBROWSER_CACHE_DIR` 示例统一为实测有效路径 `C:\Users\Administrator\.cloakbrowser`。

## 4. 关键路径备忘（供续做 agent）

- 工作目录：`C:\Users\Administrator\Documents\ChatGPT\博客网站`
- 仓库：weltwww-dot/paper-ledger，main 分支，GitHub Pages: <https://weltwww-dot.github.io/paper-ledger/>
- 更新入口：`python scripts/run_update.py update`；分步与恢复见 `更新工作流.md`。
- **InstSci 批量取 PDF 前**：跑 `powershell -ExecutionPolicy Bypass -File scripts\instsci_preflight.ps1`（清理残留+设浏览器缓存）；踩坑与降级策略见 `更新工作流.md` §9.4。
- InstSci CLI：`instsci`（`C:\Users\Administrator\Documents\Codex\tools\bin\instsci.cmd`）；doctor 全过。
- PDF 文本提取：InstSci venv python 带 `fitz`（示例见 `skill-runs/txt/instsci/` 的产出）。
- 批量入库协议：`skill-runs/instsci_batch_guide.md` + `skill-runs/tasks/instsci_task_<NNN>.json`。
- 安全边界：不提交代理/凭据/Cookie/截图；不绕过 WAF/验证码；普通代理不得冒充机构出口；不能证明本机直连时改走机构 SSO。

## 5. 本会话运行过的关键命令（复现用）

```powershell
python scripts/run_update.py update                 # 完整闭环（修 bug 后）
python scripts/run_update.py instsci                # 生成 236 篇队列
python scripts/route_check.py                       # 出口自检：无代理直连
$env:CLOAKBROWSER_CACHE_DIR="C:\Users\Administrator\.cloakbrowser"
instsci papers <one_doi.txt> --publisher ieee --mode diagnose   # 单 DOI 诊断（成功）
instsci papers <ieee_list> --publisher ieee --institution 中国农业大学 --output papers\instsci\ieee_batch     # IEEE 批量
instsci papers <elsevier_list> --publisher elsevier --institution 中国农业大学 --output papers\instsci\elsevier_batch --concurrency 2   # Elsevier 批量
node scripts/sync-papers.js                         # 同步 → data/papers.js
python scripts/summary_gate.py --check
python scripts/theme_gate.py --check
python scripts/pdf_gate.py --check
python scripts/workflow_gate.py --check
python scripts/verify_papers.py --check
python -m unittest discover -s tests -v                 # 25 项
```

## 6. 更新日志

- **2026-09-07（中文文案审校）**：全量检查 586 份六段式总结，清除展示层中的流程性确认措辞，并将信息缺口统一改为基于公开材料的客观说明；重写 4 份检出的失真一句话概括。新增 `scripts/summary_quality_gate.py` 与 3 项测试，禁止流程性确认措辞、乱码及未解码 HTML 实体；接入 `run_update.py update / advance / publish`。自动直译入口已停用，新增记录必须由执行 agent 对照可核验原文写中文六段式；PDF 获取仍在该环节之前完整执行。用户已授权本轮提交并推送。

- **2026-09-07**：文件建立（原名"会话交接"）。完成 update 闭环修复 + InstSci 获取 129 篇 + 全部本地规范化入库；107 篇待 WAF 解除续跑；advance/publish/push 待用户指示。确立本文件为**持续维护的交接文档**：后续更新直接修改本文件并在本日志追加一行（格式：日期 + 做了什么 + 状态变化）。
- **2026-09-07（职责分工）**：按用户指示明确分工——**WAF 续跑 107 篇归当前 agent 负责**（等风控自动解除且用户说开始后才跑，当前不执行），续跑结果记入本日志；**本地整理归另一个 agent**，新增 §3.3「给整理本地 agent 的操作指引」（校验 → 新增 PDF 入库 → 同步 → 闸门 → 更新快照/日志 → 用户许可后才 commit/publish）。未做内容不变（107 篇待续跑、3 条空状态、advance/publish 待指示）。
- **2026-09-07（第一轮续跑结果）**：用户指示开始后执行续跑。
  - **IEEE 50/50 全部补齐**（`papers/instsci/ieee_batch_2/`，全部 verified），`instsci_ieee_remaining.txt` 已清空。
  - **Elsevier 26 篇新获**（`elsevier_batch_2/`，26 verified=True；2 篇为期刊编委会/会员表非论文 verified=False；1 篇 pdf_not_captured）。
  - 过程中修复：Elsevier 曾两次失败——先因**残留 CloakBrowser 进程占用 chrome-profile**（`TargetClosedError`），清理后恢复；后因浏览器上下文在第 30/57 篇关闭而中断（非 WAF）。用户指示暂停，剩余 **31 篇**（`instsci_elsevier_remaining.txt`）待再次续跑。
  - **整理产出**：76 篇新 PDF（IEEE 50 + Elsevier 26）已复制到 `papers/instsci/verified_resume/` 并通过 %PDF 校验；全文已提取到 `skill-runs/txt/instsci/`；DOI 清单 `skill-runs/instsci_resume_results.json`。等待整理 agent 按 §3.3 入库（本 agent 只负责爬取，不代做本地入库）。
- **2026-09-07（交接收口）**：按用户指示清除了对并行 handoff 的引用；实时状态、待办与更新日志只在本文件维护，稳定流程改由 `更新工作流.md`、`CONTEXT.md` 与项目脚本提供。
- **2026-09-07（踩坑总结 → 项目改进）**：按用户要求把爬 PDF 实测坑沉淀为本地项目改进：① 新增 `scripts/instsci_preflight.ps1`（残留 CloakBrowser 进程清理 + 浏览器缓存自动探测设置，已接入 `instsci_batch_local_ip.ps1`）；② `更新工作流.md` 新增 §9.4「InstSci 机构 PDF 获取踩坑记录」（症状表 + 降级策略）；③ 修正 §9.3 缓存路径示例为实测有效值 `C:\Users\Administrator\.cloakbrowser`。坑要点：残留进程致 `TargetClosedError`、长批量浏览器崩溃（拆批 ≤25 + 断点续跑）、Elsevier 高并发触发 SD WAF（降 concurrency 1）、非论文页（编委会/会员表）勿当论文入库、输出目录重复归位勿直接 Recurse 计数。工作区变更仍未 commit/未 push。
- **2026-09-07（续跑文件整理完成）**：完成 `verified_resume/` 76 个文件的最终核验：73 篇研究论文已补齐中文六段式与规范 PDF，2 篇 TKDE（TCAA、OCDM）为本次收尾；3 篇 TNNLS 文件核验为出版信息/学会名单/投稿须知，标记 `non_research_document` 并排除。同步后台账 586 篇，contentState 为 complete 219 / partial 304 / pending 60 / 空 3，顶层有效 PDF 273 个；summary/theme/pdf 三道闸门与 21 项测试全通过。另修复 `scripts/sync-papers.js` 的 DOI 优先保留逻辑，避免删除占位后已有台账记录静默丢失。工作区仍未 commit/未 push。
- **2026-09-07（标准流程整改）**：把本次处理固化为可复用闭环：新增 `scripts/workflow_gate.py` 总体验收闸门和 `skill-runs/workflow_baseline.json` 历史债务上限，接入 `run_update.py` 的 `update / advance / publish`；严格核对 DOI、总结文件、内容状态、主题、PDF 链接和跳过证据，`pdf_gate.py --mark` 强制使用合法 reason 和非空 note。补齐 3 条历史空状态，记录 58 篇“已有 PDF 但 partial”的历史技术债，更新 `更新工作流.md`、`README.md` 和本文件的接手说明。当前实测：586 条台账、586 份总结、complete 222 / partial 304 / pending 60 / 空 0、顶层有效 PDF 273 个；四道闸门与 25 项测试全部通过。仍未 commit / push，advance 与 publish 等待用户明确指示。
