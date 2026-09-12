#!/usr/bin/env node
"use strict";

/* 本地 PDF 必须在新标签页打开，避免返回时重载台账并丢失页面状态。 */

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
  console.error("FAIL: 未找到 Microsoft Edge，无法执行 PDF 导航回归测试。");
  process.exit(1);
}

const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "paper-ledger-pdf-nav-"));
const fixtureFile = path.join(ROOT, `.pdf-navigation-${process.pid}.html`);
const port = 19000 + (process.pid % 10000);
let server;
let html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
html = html.replace("</body>", `<output id="pdf-navigation-test"></output>
  <script>
    window.addEventListener('load', () => {
      window.setTimeout(() => {
        const pdfLink = [...document.querySelectorAll('.paper__foot a')]
          .find((link) => link.textContent.includes('PDF'));
        const pass = Boolean(pdfLink && pdfLink.target === '_blank' &&
          pdfLink.rel.split(/\\s+/).includes('noopener') &&
          pdfLink.rel.split(/\\s+/).includes('noreferrer'));
        document.documentElement.dataset.pdfNavigationTest = pass ? 'pass' : 'fail';
        document.querySelector('#pdf-navigation-test').textContent = pass ? '' : JSON.stringify({
          reason: !pdfLink ? '首屏没有可测试的 PDF 链接' : 'PDF 没有在独立标签页安全打开',
          href: pdfLink && pdfLink.getAttribute('href'),
          target: pdfLink && pdfLink.target,
          rel: pdfLink && pdfLink.rel,
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
  if (run.status !== 0 || !/data-pdf-navigation-test="pass"/.test(run.stdout)) {
    const state = (run.stdout.match(/data-pdf-navigation-test="([^"]+)"/) || [])[1] || "未执行";
    const detail = (run.stdout.match(/<output id="pdf-navigation-test">([^<]*)<\/output>/) || [])[1] ||
      "未返回诊断详情";
    console.error(`FAIL: state=${state}; ${detail}; browserStatus=${run.status}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 本地 PDF 在新标签页打开，原台账页面不会被替换。");
  }
} finally {
  if (server) server.kill();
  fs.rmSync(fixtureFile, { force: true });
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolved = fs.realpathSync(profileDir);
  if (!resolved.startsWith(tempRoot + path.sep)) throw new Error(`拒绝清理临时目录之外的路径：${resolved}`);
  fs.rmSync(resolved, { recursive: true, force: true });
}
