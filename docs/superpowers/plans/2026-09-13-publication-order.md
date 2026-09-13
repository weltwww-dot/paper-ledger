# Publication Date Ordering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render every filtered paper list from newest to oldest by publication date, with year-only records placed after exact dates in that year and unrecognized dates at the bottom.

**Architecture:** Keep `ThemeStats.sortByPublished(list)` as the single public sorting seam shared by the paper list and trend calculations. Add explicit, locale-independent parsing inside that module, prove it through the public interface, then add a real Edge page regression to the existing workflow validation module.

**Tech Stack:** Browser JavaScript, Node.js standard library (`assert`, `child_process`, `fs`, `os`, `path`), Python `unittest`, Microsoft Edge headless regression checks.

**Spec:** `docs/superpowers/specs/2026-09-13-publication-order-design.md`

## Global Constraints

- Repository root is `D:\codex\博客网站`.
- Do not rewrite existing summary files or `data/papers.js` date text.
- Do not add dependencies or expose a new date-parser interface.
- `ThemeStats.sortByPublished(list)` remains non-mutating and is the only public ordering seam.
- Exact ISO and Chinese dates sort by natural day descending; year-only entries follow exact dates in the same year; invalid and missing dates sink to the bottom; ties remain stable.
- Existing filtering, trends, storage, expand/collapse, PDF navigation, accessibility, and layout behavior must remain unchanged.
- Every implementer and reviewer uses ponytail full; dispatched models must be `gpt-5.6-luna`.

---

### Task 1: Correct the shared publication ordering

**Files:**
- Create: `tests/theme-stats-order-check.js`
- Create: `tests/publication-order-check.js`
- Modify: `shared/theme-stats.js`

**Interfaces:**
- Consumes: `ThemeStats.sortByPublished(list: Paper[]): Paper[]`, where each paper may contain `id` and `published` strings.
- Produces: the same public interface, now ordered by recognized date semantics without mutating `list`; both Node tests and `app.js` use it unchanged.

- [ ] **Step 1: Write the failing public-interface regression**

Create `tests/theme-stats-order-check.js` with a mixed-format fixture and assertions on both output order and input immutability:

```javascript
#!/usr/bin/env node
"use strict";

const assert = require("assert");
const { sortByPublished } = require("../shared/theme-stats.js");

const papers = [
  { id: "same-iso", published: "2026-09-10（在线发表）" },
  { id: "same-zh", published: "2026年9月10日" },
  { id: "older-iso", published: "2026-09-09" },
  { id: "year-only", published: "2026年" },
  { id: "prior-year", published: "2025-12-31" },
  { id: "invalid-day", published: "2026-02-30" },
  { id: "invalid-text", published: "日期未知" },
  { id: "missing", published: "" },
];
const before = JSON.parse(JSON.stringify(papers));

assert.deepStrictEqual(
  sortByPublished(papers).map((paper) => paper.id),
  ["same-iso", "same-zh", "older-iso", "year-only", "prior-year", "invalid-day", "invalid-text", "missing"]
);
assert.deepStrictEqual(papers, before);
console.log("PASS: 发表时间支持 ISO、中文、年份及无效值的稳定倒序，且不修改输入列表。");
```

- [ ] **Step 2: Write the failing real-page regression**

Create `tests/publication-order-check.js` with the complete real-browser check below. It expands the list, reads every paper including entries without a date tag, and uses an independent test-side key rather than calling the production sorter:

```javascript
#!/usr/bin/env node
"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawn, spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const edge = [
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
].find(fs.existsSync);

if (!edge) {
  console.error("FAIL: 未找到 Microsoft Edge，无法执行论文时间顺序回归测试。");
  process.exit(1);
}

const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "paper-ledger-order-"));
const fixtureFile = path.join(ROOT, `.publication-order-${process.pid}.html`);
const port = 20000 + (process.pid % 10000);
let server;
let html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
html = html.replace("</body>", `<output id="publication-order-test"></output>
<script>
function keyOf(text) {
  const value = String(text || "").trim();
  let match = value.match(/^(\\d{4})-(\\d{1,2})-(\\d{1,2})(?:$|[\\s（(])/);
  if (!match) match = value.match(/^(\\d{4})年(\\d{1,2})月(\\d{1,2})日/);
  if (match) {
    const year = Number(match[1]);
    const month = Number(match[2]);
    const day = Number(match[3]);
    const stamp = Date.UTC(year, month - 1, day);
    const roundTrip = new Date(stamp);
    if (roundTrip.getUTCFullYear() === year && roundTrip.getUTCMonth() === month - 1 && roundTrip.getUTCDate() === day) {
      return [1, year, 1, stamp];
    }
    return [0, 0, 0, 0];
  }
  match = value.match(/^(\\d{4})(?:年)?$/);
  return match ? [1, Number(match[1]), 0, 0] : [0, 0, 0, 0];
}

function beforeOrEqual(left, right) {
  for (let index = 0; index < left.length; index += 1) {
    if (left[index] !== right[index]) return left[index] > right[index];
  }
  return true;
}

window.addEventListener("load", () => {
  window.setTimeout(() => {
    const more = document.querySelector("#latest-more");
    if (more && !more.hidden && /查看全部/.test(more.textContent)) more.click();
    const cards = [...document.querySelectorAll("#latest-list .paper")];
    const keys = cards.map((card) => {
      const tag = card.querySelector(".tag--date");
      return keyOf(tag ? tag.textContent : "");
    });
    const badIndex = keys.findIndex((key, index) => index > 0 && !beforeOrEqual(keys[index - 1], key));
    const pass = cards.length > 4 && keys[0] && keys[0][0] === 1 && badIndex === -1;
    document.documentElement.dataset.publicationOrderTest = pass ? "pass" : "fail";
    document.querySelector("#publication-order-test").textContent = pass ? "" : JSON.stringify({
      count: cards.length,
      badIndex,
      previous: badIndex > 0 ? keys[badIndex - 1] : null,
      current: badIndex >= 0 ? keys[badIndex] : null,
    });
  }, 0);
});
</script></body>`);

try {
  fs.writeFileSync(fixtureFile, html, "utf8");
  server = spawn("python", ["-m", "http.server", String(port), "--bind", "127.0.0.1", "--directory", ROOT], {
    stdio: "ignore",
    windowsHide: true,
  });
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 1000);
  const run = spawnSync(edge, [
    "--headless=new",
    "--edge-skip-compat-layer-relaunch",
    "--disable-gpu",
    `--user-data-dir=${profileDir}`,
    "--window-size=1280,900",
    "--virtual-time-budget=5000",
    "--dump-dom",
    `http://127.0.0.1:${port}/${path.basename(fixtureFile)}`,
  ], { encoding: "utf8", timeout: 15000, maxBuffer: 64 * 1024 * 1024 });
  if (run.error) throw run.error;
  if (run.status !== 0 || !/data-publication-order-test="pass"/.test(run.stdout)) {
    const state = (run.stdout.match(/data-publication-order-test="([^"]+)"/) || [])[1] || "未执行";
    const detail = (run.stdout.match(/<output id="publication-order-test">([^<]*)<\/output>/) || [])[1] || "未返回诊断详情";
    console.error(`FAIL: state=${state}; ${detail}; browserStatus=${run.status}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 收录列表从上到下按发表时间倒序，最新论文位于顶部。");
  }
} finally {
  if (server) server.kill();
  fs.rmSync(fixtureFile, { force: true });
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolved = fs.realpathSync(profileDir);
  if (!resolved.startsWith(tempRoot + path.sep)) throw new Error(`拒绝清理临时目录之外的路径：${resolved}`);
  fs.rmSync(resolved, { recursive: true, force: true });
}
```

- [ ] **Step 3: Run both regressions and verify the existing implementation fails for the intended reason**

Run:

```powershell
node tests/theme-stats-order-check.js
node tests/publication-order-check.js
```

Expected: both commands exit non-zero because `sortByPublished` compares raw strings, placing Chinese and year-only 2026 values before later ISO dates.

- [ ] **Step 4: Implement the minimum locale-independent sorting key**

Inside `shared/theme-stats.js`, add private `publicationKey(value)` and `comparePublicationKeys(a, b)` functions immediately before `sortByPublished`. Match only the formats approved by the spec, validate day-level dates by UTC round-trip, and return a stable comparator result:

```javascript
function publicationKey(value) {
  const text = String(value || "").trim();
  let match = text.match(/^(\d{4})-(\d{1,2})-(\d{1,2})(?:$|[\s（(])/);
  if (!match) match = text.match(/^(\d{4})年(\d{1,2})月(\d{1,2})日/);
  if (match) {
    const year = Number(match[1]);
    const month = Number(match[2]);
    const day = Number(match[3]);
    const stamp = Date.UTC(year, month - 1, day);
    const date = new Date(stamp);
    if (date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day) {
      return { recognized: 1, year, precision: 1, stamp };
    }
    return { recognized: 0, year: 0, precision: 0, stamp: 0 };
  }
  match = text.match(/^(\d{4})(?:年)?$/);
  return match
    ? { recognized: 1, year: Number(match[1]), precision: 0, stamp: 0 }
    : { recognized: 0, year: 0, precision: 0, stamp: 0 };
}

function comparePublicationKeys(a, b) {
  return (
    b.recognized - a.recognized ||
    b.year - a.year ||
    b.precision - a.precision ||
    b.stamp - a.stamp
  );
}

function sortByPublished(list) {
  return [...list].sort((a, b) => comparePublicationKeys(publicationKey(a.published), publicationKey(b.published)));
}
```

- [ ] **Step 5: Run focused tests and verify green**

Run:

```powershell
node tests/theme-stats-order-check.js
node tests/publication-order-check.js
node tests/layout-overflow-check.js
node tests/latest-collapse-check.js
node tests/pdf-navigation-check.js
node --check shared/theme-stats.js
node --check app.js
```

Expected: every command exits zero; the two new tests print their PASS messages and all three existing browser regressions remain green.

- [ ] **Step 6: Commit the shared behavior**

```powershell
git add shared/theme-stats.js tests/theme-stats-order-check.js tests/publication-order-check.js
git commit -m "fix: order papers by normalized publication date"
```

### Task 2: Make publication ordering a release gate

**Files:**
- Modify: `tests/test_workflow_validation.py`
- Modify: `scripts/workflow_validation.py`
- Modify: `更新工作流.md`

**Interfaces:**
- Consumes: `_layout_check(log: Callable[[str], None], context: str) -> None` and executable `tests/publication-order-check.js` from Task 1.
- Produces: the same `_layout_check` interface, now running four browser regressions and rejecting publication when ordering fails.

- [ ] **Step 1: Extend the orchestration test first**

Change `test_browser_gate_runs_pdf_navigation_regression` to `test_browser_gate_runs_all_browser_regressions` and change its expected script list to:

```python
[
    "layout-overflow-check.js",
    "latest-collapse-check.js",
    "pdf-navigation-check.js",
    "publication-order-check.js",
]
```

- [ ] **Step 2: Run the focused Python test and verify red**

Run:

```powershell
python -m unittest tests.test_workflow_validation.WorkflowValidationTests.test_browser_gate_runs_all_browser_regressions
```

Expected: FAIL because `_layout_check` still launches only the original three scripts.

- [ ] **Step 3: Add the page-order regression to the shared validation module**

In `scripts/workflow_validation.py`, keep the public `_layout_check` and `validate_workflow` interfaces unchanged and replace the browser-check block with:

```python
log(f"网站布局、收起、PDF 导航与论文时间顺序检查{suffix}…")
for script in (
    "layout-overflow-check.js",
    "latest-collapse-check.js",
    "pdf-navigation-check.js",
    "publication-order-check.js",
):
    result = subprocess.run(
        ["node", ROOT / "tests" / script],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.stdout:
        log(result.stdout.rstrip())
    if result.stderr:
        log(result.stderr.rstrip())
    if result.returncode != 0:
        raise SystemExit("网站布局、收起、PDF 导航或论文时间顺序检查未通过，不能继续。")
```

- [ ] **Step 4: Document the enforced gate**

In `更新工作流.md`, update the validation description to say the real browser checks layout, collapse behavior, PDF navigation, and newest-first publication ordering. Add this row to the test-file table:

```markdown
| `tests/publication-order-check.js` | 用真实 Edge 展开全部收录，保证论文按发表时间倒序且最新论文置顶 |
```

- [ ] **Step 5: Run focused and full verification**

Run:

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m unittest discover -s tests -p 'test_*.py'
python scripts/summary_gate.py --check
python scripts/summary_quality_gate.py --check
python scripts/theme_gate.py --check
python scripts/pdf_gate.py --check
python scripts/workflow_gate.py --check
python scripts/verify_papers.py --check
node tests/theme-stats-order-check.js
node tests/layout-overflow-check.js
node tests/latest-collapse-check.js
node tests/pdf-navigation-check.js
node tests/publication-order-check.js
node --check shared/theme-stats.js
node --check app.js
git diff --check
```

Expected: all 49 Python tests pass; six data gates pass; all 629 existing PDFs are valid; all five Node regressions and both syntax checks pass; `git diff --check` exits zero. The existing warning about 51 historical `partial+PDF` records may remain but must not increase.

- [ ] **Step 6: Commit the release gate**

```powershell
git add scripts/workflow_validation.py tests/test_workflow_validation.py 更新工作流.md
git commit -m "test: gate publication date ordering"
```

### Task 3: Final review and handoff

**Files:**
- Review only: all files changed since commit `2cbdc3b`
- Modify only when review finds a defect: the file that owns that defect and its public-seam regression

**Interfaces:**
- Consumes: approved design, this plan, `ThemeStats.sortByPublished(list)`, `_layout_check(log, context)`, and the SDD task ledger.
- Produces: reviewed implementation with fresh verification evidence and no unresolved blocker.

- [ ] **Step 1: Run the SDD final broad review**

Review the branch diff against `docs/superpowers/specs/2026-09-13-publication-order-design.md`, checking date semantics, stable ordering, input immutability, actual DOM order, workflow-gate inclusion, dependency count, and unrelated behavior changes. Resolve every finding through the SDD fix/re-review loop.

- [ ] **Step 2: Run fresh completion evidence**

Repeat the full verification command block from Task 2 Step 5 after the final review. Record exact test counts, PDF counts, warnings, and failures in the SDD ledger.

- [ ] **Step 3: Enter branch integration**

Invoke `finishing-a-development-branch` and present its integration options. Do not merge, push, publish, discard, or remove the worktree until the user selects an option.
