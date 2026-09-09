# 599 篇论文 PDF 全量复核实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 审计当前 599 条论文记录，找出漏掉、损坏、错配或缺证据的 PDF，只对异常项分层重抓，并把新确认的 PDF 按项目标准完成归档、总结、主题和验收。

**Architecture:** 采用“全量只读盘点 → OA 暂存复核 → 身份校验 → 出版社/InstSci 分批补抓 → 主 agent 处理新全文 → 统一门禁”的流水线。现有有效 PDF 不重写；所有新下载先进入 `skill-runs/pdf_full_audit_2026-09-09/`，验证通过后才进入 `papers/`。出版社批次按队列串行执行，避免共享 CloakBrowser profile 和 ScienceDirect WAF 互相影响。

**Tech Stack:** Python 3、Node.js、PowerShell、PyMuPDF/pdfinfo（可用时）、现有 `paper-summarize-fetch` OA/PDF 工具、InstSci 可见 CloakBrowser、项目六道质量门禁。

**Spec:** `docs/superpowers/specs/2026-09-09-full-pdf-audit-spec.md`

## Global Constraints

- 台账基线是 599 条；当前实时状态为 `complete 238 / partial 300 / pending 61`，285 条有 PDF 字段，顶层有效 PDF 290 个。
- 任何 PDF 成功结论都必须同时有 `%PDF`、`%%EOF`、页数和 DOI/标题身份证据；文件名或 HTTP 200 单独不能算成功。
- 现有有效 PDF 不删除、不覆盖；新文件全部先写入 `skill-runs/pdf_full_audit_2026-09-09/`。
- InstSci 只允许本机直连/机构授权路线；`route_check.py --require-direct` 失败就停止，不用通用代理冒充机构 IP。
- InstSci 单批最多 25 篇、并发 1；遇到 WAF、验证码、SSO 或人工验证循环立即记录并停批，不绕过验证。
- 中文六段式最终由当前主 agent 对照全文亲自完成；不使用本地翻译模型、在线翻译服务或子代理代写最终总结。
- `SESSION_HANDOFF_2026-09-07.md` 只在本地更新；commit、push、Pages 发布必须等用户明确授权。

## File Map

- Create: `scripts/audit_all_pdfs.py` — 读取 599 条台账、本地 PDF 和尝试证据，生成只读盘点、异常分类和出版社队列。
- Test: `tests/test_audit_all_pdfs.py` — 覆盖缺失、无效、路径越界、身份不确定和有效 PDF 分类。
- Create: `scripts/reconcile_pdf_audit.py` — 将已验证的暂存 PDF 安全归档到顶层，并生成待总结队列；禁止覆盖已有有效文件。
- Test: `tests/test_reconcile_pdf_audit.py` — 覆盖安全复制、碰撞拒绝、PDF 链接更新和失败项不入库。
- Runtime only: `skill-runs/pdf_full_audit_2026-09-09/` — 全量审计 JSON、OA 结果、暂存下载、分出版社队列和失败证据；不把浏览器 profile、cookie、代理或凭据写入仓库。
- Modify only after verified candidates exist: `summaries/`, `papers/`, `data/papers.js`, `data/theme-tags.json`, `index.html`。
- Local-only handoff: `SESSION_HANDOFF_2026-09-07.md`。

### Task 1: 建立全量只读 PDF 盘点器

**Files:**
- Create: `scripts/audit_all_pdfs.py`
- Test: `tests/test_audit_all_pdfs.py`
- Runtime output: `skill-runs/pdf_full_audit_2026-09-09/inventory.json`, `records.json`, `unresolved.json`, `queues/by-publisher/*.txt`

**Interfaces:**
- Command: `python scripts/audit_all_pdfs.py --output-dir skill-runs/pdf_full_audit_2026-09-09`
- Input: `data/papers.js`, `summaries/`, `papers/`, `skill-runs/pdf_attempts.json`
- Row fields: `doi`, `title`, `journal`, `content_state`, `pdf_field`, `resolved_path`, `file_status`, `identity_status`, `identity_evidence`, `recommended_action`。
- `file_status` 只能为 `verified`, `missing`, `invalid`, `outside_canonical_dir`, `unreadable`；`identity_status` 只能为 `matched`, `mismatch`, `unconfirmed`, `not_applicable`。

- [ ] **Step 1: 写失败测试**：使用临时目录和手工构造的台账记录，断言缺失文件进入 `missing`、文件头/尾不合法进入 `invalid`、`../outside.pdf` 进入 `outside_canonical_dir`，不能把 `pdf_attempts.json` 的旧记录直接算作成功；对一个真实有效 PDF fixture 断言页数和标题/DOI匹配结果被记录。
- [ ] **Step 2: 运行测试确认失败**：运行 `python -m unittest tests.test_audit_all_pdfs -v`；预期因 `audit_all_pdfs.py` 尚未存在而失败，修正测试夹具后仍保持功能缺失红灯。
- [ ] **Step 3: 实现最小盘点器**：解析 `data/papers.js`；规范化 DOI；解析 PDF 字段只能落在 `papers/` 内；先检查 `%PDF`/`%%EOF`，再用 `pdfinfo` 或已配置的 PyMuPDF 读取页数；提取前两页文本并对规范化 DOI、标题 token 做身份判断；无法提取身份时写 `unconfirmed`，不能升级为 `verified`。输出确定性 JSON，不修改台账。
- [ ] **Step 4: 运行测试确认通过**：运行 `python -m unittest tests.test_audit_all_pdfs -v`，再执行 `python scripts/audit_all_pdfs.py --output-dir skill-runs/pdf_full_audit_2026-09-09`；预期生成 599 行 inventory，行数与台账严格一致。
- [ ] **Step 5: 记录任务提交**：只提交脚本和测试，不提交运行目录、PDF、浏览器证据或 handoff。

### Task 2: 对全量记录做 OA/arXiv 复核并暂存下载

**Files:**
- Read: `skill-runs/pdf_full_audit_2026-09-09/records.json`
- Write runtime only: `skill-runs/pdf_full_audit_2026-09-09/oa_full.json`, `oa_downloads/`, `crawler_targets.json`, `download_manifest.json`
- Reuse: `D:\codex\.codex\skills\paper-summarize-fetch\scripts\oa_check.py`
- Reuse: `D:\codex\.codex\skills\paper-summarize-fetch\scripts\download_parallel.py`

**Interfaces:**
- OA command: `python D:\codex\.codex\skills\paper-summarize-fetch\scripts\oa_check.py -i skill-runs\pdf_full_audit_2026-09-09\records.json -o skill-runs\pdf_full_audit_2026-09-09\oa_full.json --arxiv --concurrent`
- Staging command: `python D:\codex\.codex\skills\paper-summarize-fetch\scripts\download_parallel.py --oa skill-runs\pdf_full_audit_2026-09-09\oa_full.json --outdir skill-runs\pdf_full_audit_2026-09-09\oa_downloads --workers 4 --per-file 120 --budget 1200 --crawl-out skill-runs\pdf_full_audit_2026-09-09\crawler_targets.json`

- [ ] **Step 1: 固定全量输入**：由 Task 1 生成 599 条 `records.json`；将当前已有 PDF 和当前无 PDF 都保留在输入中，但下载器只对 `missing/invalid/unconfirmed` 或缺少可核验 OA 结果的行发起网络请求。
- [ ] **Step 2: 运行 OA 复核**：执行上面的 `oa_check.py` 命令；预期每条 DOI 都有 OA 状态、最佳 PDF URL、arXiv 回退和错误字段，供应商失败不能静默变成 `not-oa`。
- [ ] **Step 3: 暂存下载**：执行 `download_parallel.py`；只写入审计目录，保留 `cached/missing/auth_required/crawl_pending` 等原始状态，不把暂存文件直接当作台账 PDF。
- [ ] **Step 4: 重新盘点暂存结果**：对 `oa_downloads/` 再运行 Task 1 的身份逻辑；输出 `oa_verified.json` 和 `oa_unresolved.json`，统计“新找到 PDF / 已有 PDF 重复命中 / 身份不确定 / 仍缺失”。
- [ ] **Step 5: 检查运行产物**：确认审计目录没有 cookie、token、代理 URL、CloakBrowser profile 或凭据；确认 599 条仍全部可追溯。

### Task 3: 安全归档 OA 复核通过的 PDF

**Files:**
- Create: `scripts/reconcile_pdf_audit.py`
- Test: `tests/test_reconcile_pdf_audit.py`
- Modify after approval by evidence: `papers/`, `summaries/`, `data/papers.js`, `data/theme-tags.json`, `index.html`

**Interfaces:**
- Command: `python scripts/reconcile_pdf_audit.py --audit-dir skill-runs/pdf_full_audit_2026-09-09 --apply-verified`
- Input contract: 只接受 `identity_status=matched` 且文件校验通过的 staged rows。
- Output: `reconciled.json`、`new_fulltext_queue.json`；任何拒绝复制的 row 必须写明原因。

- [ ] **Step 1: 写失败测试**：断言已存在的有效顶层 PDF 不被覆盖；同名但 DOI 不同的文件被拒绝；路径越界、身份不确定和无效文件不进入 `papers/`；安全复制后对应总结只增加一个规范 PDF 链接。
- [ ] **Step 2: 运行测试确认失败**：运行 `python -m unittest tests.test_reconcile_pdf_audit -v`，预期在归档器未实现时失败。
- [ ] **Step 3: 实现最小归档器**：按现有 ASCII 命名约定生成不冲突文件名；使用临时文件/原子替换；已有相同 DOI 的有效文件只登记 `already_present`，不重写；只更新总结中的 PDF 行，不改变中文六段式正文。
- [ ] **Step 4: 运行测试与真实盘点**：先运行专项测试，再以 `--apply-verified` 归档 OA 通过项；运行 `verify_papers.py --check` 和 `workflow_gate.py --check`，确认没有新增 `partial+PDF` 债务。
- [ ] **Step 5: 生成待全文队列**：任何由“无 PDF”转为“有 PDF”且 `contentState` 为 `pending/partial` 的条目进入 `new_fulltext_queue.json`，不得直接标记 complete。

### Task 4: 为剩余异常项生成出版社队列并串行执行 InstSci

**Files:**
- Read: `skill-runs/pdf_full_audit_2026-09-09/oa_unresolved.json`
- Runtime output: `skill-runs/pdf_full_audit_2026-09-09/queues/by-publisher/`, `instsci_runs/`
- Reuse: `scripts/instsci_preflight.ps1`, `scripts/instsci_batch_local_ip.ps1`, `scripts/route_check.py`

- [ ] **Step 1: 按出版社拆分队列**：只将 OA 未解决且未被确认是非研究页面的条目写入队列；按 IEEE、Elsevier、Springer、ACM/Oxford 等实际 publisher 分文件，每个文件最多 25 个 DOI；保留 DOI、标题、期刊、当前状态和上一步证据。
- [ ] **Step 2: 做本机直连预检**：逐批前运行 `powershell -ExecutionPolicy Bypass -File scripts\instsci_preflight.ps1 -RouteCheck`；若 `route_check.py --require-direct` 失败，停止并记录 `route_not_direct`，不启动浏览器。
- [ ] **Step 3: 串行运行单出版社批次**：使用以下模板，`Concurrency=1`，一个批次完成并保存 manifest 后才开始下一个：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\instsci_batch_local_ip.ps1 `
  -DoisFile skill-runs\pdf_full_audit_2026-09-09\queues\by-publisher\elsevier_01.txt `
  -Institution "中国农业大学" -Publisher elsevier `
  -OutputDir skill-runs\pdf_full_audit_2026-09-09\instsci_runs\elsevier_01 `
  -LoginTimeout 900 -PdfTimeout 120 -Concurrency 1
```

- [ ] **Step 4: 遵守人工验证边界**：可见浏览器中的登录、人机验证、WAF 页面由用户完成；不自动猜测、绕过或导出凭据。遇到 ScienceDirect WAF 或浏览器上下文关闭，立即停止当前批次，保存 `waf_blocked`/`capture_failed` 证据并转入下一步分析。
- [ ] **Step 5: 只接收 browser-verified 结果**：HTTP 预检、DOI 解析和 cookie 文件只能作为辅助证据；最终闭合访问 PDF 必须有可见 CloakBrowser manifest、文件校验和标题/DOI身份证据。
- [ ] **Step 6: 汇总各批次**：主 agent 读取每个 manifest，去重 DOI，生成 `instsci_verified.json`、`instsci_failed.json` 和下一轮队列；禁止直接将原始批次目录递归计数为新增 PDF。

### Task 5: 主 agent 处理新增全文，不委托最终翻译

**Files:**
- Input: `new_fulltext_queue.json`, `oa_verified.json`, `instsci_verified.json`
- Modify: 对应 `summaries/<slug>_总结.md`、`data/papers.js`、必要时 `papers/`
- Reuse: `scripts/sync-papers.js --fill-themes --python C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe`

- [ ] **Step 1: 读取全文证据**：对每个新确认 PDF 提取文本，按“基本信息 → 一句话概括 → 问题与动机 → 方法 → 实验与结果 → 贡献与局限”阅读；保留原文未提供的信息边界，不补造数字。
- [ ] **Step 2: 主 agent 亲自写中文六段式**：更新原有待补全/部分总结，只有全文支持时才升级 `contentState=complete`；不得调用本地模型、在线翻译或让子代理代写最终中文。
- [ ] **Step 3: 同步目录**：运行 `node scripts/sync-papers.js --fill-themes --python C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe`；确认一级方向仍只有人工智能/信息安全，细分方向仅作为 tags。
- [ ] **Step 4: 对每个新增/升级条目保存证据**：总结中的 DOI 后附真实 PDF 相对链接；非研究页面标记 `non_research_document`，不伪造研究总结。

### Task 6: 全量验收、更新本地 handoff 和提交前审查

**Files:**
- Read: all audit manifests and current gates
- Modify local-only: `SESSION_HANDOFF_2026-09-07.md`

- [ ] **Step 1: 运行全量门禁**：

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s tests -p 'test_*.py'
python scripts/summary_gate.py --check
python scripts/summary_quality_gate.py --check
python scripts/theme_gate.py --check
python scripts/pdf_gate.py --check
python scripts/workflow_gate.py --check
python scripts/verify_papers.py --check
node tests/layout-overflow-check.js
node tests/latest-collapse-check.js
node tests/pdf-navigation-check.js
git diff --check
```

- [ ] **Step 2: 对账 599 条**：报告 `verified_local`、`verified_oa`、`verified_institution`、`missing_with_evidence`、`non_research_document`、`needs_manual_review` 的数量之和必须等于 599；PDF 字段、顶层文件、总结链接和 manifest DOI 集合必须一致。
- [ ] **Step 3: 更新 handoff**：写入真实日期、最终 counts、每个出版社成功/失败/暂停数量、WAF 或 route blocker、下一轮 DOI 清单和本轮未完成项；不复制过期的 `239/60`、489 条证据或 45 项测试。
- [ ] **Step 4: 生成提交前审查包**：列出 `git status`、`git diff --stat`、新增 PDF 与总结、所有运行目录；确认 handoff 被 `.gitignore` 忽略，凭据/浏览器状态没有进入差异。
- [ ] **Step 5: 提交**：只有用户明确授权时才 `git add`、commit；提交信息按实际内容写明全量 PDF 审计结果。未获授权时保留本地变更并在 handoff 标明“待发布”。

### Task 7: 用户授权后的 GitHub Pages 发布

**Files:**
- Modify: tracked project outputs from Tasks 3–6
- Read local-only: `SESSION_HANDOFF_2026-09-07.md`

- [ ] **Step 1: 发布前复核**：确认用户明确授权；运行 `python scripts/run_update.py advance`，确认更新基准与本轮审计一致。
- [ ] **Step 2: 发布**：运行 `python scripts/run_update.py publish`；该命令必须通过所有门禁、推送 `main`、等待 Pages 构建，并核对线上 `data/papers.js` 数量和 SHA-256 指纹。
- [ ] **Step 3: 发布后验证**：检查 `git ls-remote origin refs/heads/main`、Pages Actions 的 head SHA、线上 PDF 入口和线上 `papers.js` 指纹；随后只更新本地 handoff。

## Subagent Dispatch Map

子代理只承担可验证的审计、队列整理、脚本实现和 manifest 检查，不承担最终中文翻译、凭据输入、验证码、人机验证或 GitHub 发布：

1. Task 1：一个实现 agent 编写盘点器；一个 reviewer 检查身份判定的误报/漏报。
2. Task 2：一个数据 agent 执行 OA 复核与暂存下载；reviewer 检查 599 行完整性和错误分类。
3. Task 3：一个实现 agent 编写安全归档器；reviewer 检查不覆盖、不越界和 DOI 对账。
4. Task 4：按出版社分派新 agent 做 manifest 分析；InstSci 实际批次仍串行，避免共享 profile/WAF。
5. Task 5：主 agent 独立完成全文阅读和中文六段式；子代理只能做文本提取、页码/身份核对。
6. Task 6：主 agent 执行最终门禁；最终 reviewer 检查全量数量、失败证据和 handoff 实时性。

## Decision Ledger

- **Ruling:** 不直接把 599 个 DOI 同时送入 InstSci —— 先对全量做本地/ OA 审计，再只把异常项分出版社、每批不超过 25 篇；这样保留“599 条全量复核”覆盖，同时降低重复下载、共享浏览器冲突和 WAF 风险。
- **Ruling:** 现有有效 PDF 不重下载 —— 先验证文件完整性和身份；重复下载不会增加漏网发现能力，却会增加出版社限流和文件覆盖风险。
- **Ruling:** 新获得全文不由子代理翻译 —— 项目约定要求当前主 agent 亲自完成中文六段式，子代理只负责机械审计和证据整理。
- **Ruling:** 未获明确授权不 push —— PDF 复核可能生成大量数据/总结变更，属于外部共享分支写入，按 handoff 规则暂停在本地。
