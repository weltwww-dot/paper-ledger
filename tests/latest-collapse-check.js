#!/usr/bin/env node
"use strict";

/* 收起长列表时，先平滑返回收录区顶部，再缩短列表，避免页面高度骤减造成跳动。 */

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
  console.error("FAIL: 未找到 Microsoft Edge，无法执行收起交互回归测试。");
  process.exit(1);
}

const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "paper-ledger-collapse-"));
const fixtureFile = path.join(ROOT, `.latest-collapse-${process.pid}.html`);
const port = 18000 + (process.pid % 10000);
let server;
let html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
html = html.replace("</body>", `<output id="collapse-test"></output>
  <script>
    let scrollRequest = null;
    Element.prototype.scrollIntoView = function(options) {
      scrollRequest = {
        target: this.id,
        behavior: options && options.behavior,
        block: options && options.block,
      };
    };
    window.addEventListener('load', () => {
      const more = document.querySelector('#latest-more');
      const latest = document.querySelector('#latest');
      more.click();
      const scrollTarget = latest.offsetTop + 600;
      document.documentElement.style.scrollBehavior = 'auto';
      document.documentElement.scrollTop = scrollTarget;
      document.body.scrollTop = scrollTarget;
      window.setTimeout(() => {
        const control = document.querySelector('#latest-collapse-floating');
        const rect = control && control.getBoundingClientRect();
        const style = control && getComputedStyle(control);
        const visible = Boolean(control && !control.hidden && style.display !== 'none' &&
          rect.bottom > 0 && rect.top < innerHeight && rect.right > 0 && rect.left < innerWidth);
        const expandedCardCount = document.querySelectorAll('.paper').length;
        scrollRequest = null;
        if (control) control.click();
        const stayedExpandedDuringScroll = more.textContent.includes('收起') &&
          document.querySelectorAll('.paper').length === expandedCardCount;
        const smoothRequested = Boolean(scrollRequest && scrollRequest.target === 'latest' &&
          scrollRequest.behavior === 'smooth' && scrollRequest.block === 'start');
        window.dispatchEvent(new Event('scrollend'));
        window.setTimeout(() => {
          const collapsed = !more.hidden && more.textContent.includes('查看全部');
          const collapsedCardCount = document.querySelectorAll('.paper').length;
          const pass = visible && smoothRequested && stayedExpandedDuringScroll && collapsed &&
            collapsedCardCount < expandedCardCount;
          document.documentElement.dataset.collapseTest = pass ? 'pass' : 'fail';
          document.querySelector('#collapse-test').textContent = pass ? '' : JSON.stringify({
            reason: !visible ? '滚动后没有可见的收起控制' :
              !smoothRequested ? '没有平滑返回收录区顶部' :
              !stayedExpandedDuringScroll ? '滚动完成前列表已收起' : '滚动完成后列表没有收起',
            visible,
            smoothRequested,
            stayedExpandedDuringScroll,
            collapsed,
            scrollRequest,
            expandedCardCount,
            collapsedCardCount,
          });
        }, 0);
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
    "--allow-file-access-from-files",
    `--user-data-dir=${profileDir}`,
    "--window-size=1280,900",
    "--virtual-time-budget=5000",
    "--dump-dom",
    `http://127.0.0.1:${port}/${path.basename(fixtureFile)}`,
  ], { encoding: "utf8", timeout: 15000, maxBuffer: 64 * 1024 * 1024 });
  if (run.error) throw run.error;
  if (run.status !== 0 || !/data-collapse-test="pass"/.test(run.stdout)) {
    const state = (run.stdout.match(/data-collapse-test="([^"]+)"/) || [])[1] || "未执行";
    const detail = (run.stdout.match(/<output id="collapse-test">([^<]*)<\/output>/) || [])[1] ||
      run.stdout.slice(0, 500).replace(/\s+/g, " ") || "未返回诊断详情";
    console.error(`FAIL: state=${state}; ${detail}; browserStatus=${run.status}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 收起控件先平滑返回收录区顶部，再缩短列表。");
  }
} finally {
  if (server) server.kill();
  fs.rmSync(fixtureFile, { force: true });
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolved = fs.realpathSync(profileDir);
  if (!resolved.startsWith(tempRoot + path.sep)) throw new Error(`拒绝清理临时目录之外的路径：${resolved}`);
  fs.rmSync(resolved, { recursive: true, force: true });
}
