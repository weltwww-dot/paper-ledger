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
html = html.replace('<script src="data/papers.js?v=tladzu" defer></script>', `<script>
window.PAPERLEDGER_SEED = [
  { id: "invalid-day", title: "Invalid day", published: "2026-02-30", direction: "人工智能" },
  { id: "same-iso", title: "Same-day ISO", published: "2026-09-10", direction: "人工智能" },
  { id: "invalid-text", title: "Invalid text", published: "日期未知", direction: "人工智能" },
  { id: "year-only", title: "Year only", published: "2026年", direction: "人工智能" },
  { id: "same-zh", title: "Same-day Chinese", published: "2026年9月10日", direction: "人工智能" },
  { id: "missing", title: "Missing date", published: "", direction: "人工智能" },
  { id: "older-iso", title: "Older ISO", published: "2026-09-09", direction: "人工智能" },
  { id: "prior-year", title: "Prior year", published: "2025-12-31", direction: "人工智能" },
];
</script>`);
html = html.replace("</body>", `<output id="publication-order-test"></output>
<script>
window.addEventListener("load", () => {
  window.setTimeout(() => {
    const more = document.querySelector("#latest-more");
    if (more && !more.hidden && /查看全部/.test(more.textContent)) more.click();
    const actual = [...document.querySelectorAll("#latest-list .paper")].map((card) => card.dataset.id);
    const expected = ["same-iso", "same-zh", "older-iso", "year-only", "prior-year", "invalid-day", "invalid-text", "missing"];
    const pass = JSON.stringify(actual) === JSON.stringify(expected);
    document.documentElement.dataset.publicationOrderTest = pass ? "pass" : "fail";
    document.querySelector("#publication-order-test").textContent = pass ? "" : JSON.stringify({
      expected,
      actual,
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
    const state = (run.stdout.match(/data-publication-order-test="([^\"]+)"/) || [])[1] || "未执行";
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
