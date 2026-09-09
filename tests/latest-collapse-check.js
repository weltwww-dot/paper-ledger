#!/usr/bin/env node
"use strict";

/* “查看全部”后，无论滚动到列表何处，都必须有可见的就近收起控制。 */

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
    let scrollIntoViewCalls = 0;
    const nativeScrollIntoView = Element.prototype.scrollIntoView;
    Element.prototype.scrollIntoView = function(...args) {
      scrollIntoViewCalls += 1;
      return nativeScrollIntoView.apply(this, args);
    };
    window.addEventListener('load', () => {
      const more = document.querySelector('#latest-more');
      const latest = document.querySelector('#latest');
      more.click();
      const scrollTarget = latest.offsetTop + 600;
      document.documentElement.style.scrollBehavior = 'auto';
      document.documentElement.scrollTop = scrollTarget;
      document.body.scrollTop = scrollTarget;
      requestAnimationFrame(() => requestAnimationFrame(() => {
        const control = document.querySelector('#latest-collapse-floating');
        const rect = control && control.getBoundingClientRect();
        const style = control && getComputedStyle(control);
        const visible = Boolean(control && !control.hidden && style.display !== 'none' &&
          rect.bottom > 0 && rect.top < innerHeight && rect.right > 0 && rect.left < innerWidth);
        const beforeCollapse = window.scrollY;
        scrollIntoViewCalls = 0;
        if (control) control.click();
        window.setTimeout(() => {
          const afterCollapse = window.scrollY;
          const preservedScroll = Math.abs(afterCollapse - beforeCollapse) <= 40;
          const collapsed = !more.hidden && more.textContent.includes('查看全部');
          const noForcedScroll = scrollIntoViewCalls === 0;
          const pass = visible && preservedScroll && collapsed && noForcedScroll;
          document.documentElement.dataset.collapseTest = pass ? 'pass' : 'fail';
          document.querySelector('#collapse-test').textContent = pass ? '' : JSON.stringify({
            reason: !visible ? '滚动后没有可见的收起控制' :
              !preservedScroll ? '收起时滚动位置发生跳转' :
              !noForcedScroll ? '收起时调用了强制滚动' : '列表没有收起',
            visible,
            preservedScroll,
            collapsed,
            noForcedScroll,
            scrollIntoViewCalls,
            beforeCollapse,
            afterCollapse,
            latestTop: latest.offsetTop,
            pageHeight: document.documentElement.scrollHeight,
          });
        }, 600);
      }));
    });
  </script></body>`);

try {
  fs.writeFileSync(fixtureFile, html, "utf8");
  server = spawn("python", ["-m", "http.server", String(port), "--bind", "127.0.0.1", "--directory", ROOT], {
    stdio: "ignore",
    windowsHide: true,
  });
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 300);
  const run = spawnSync(edge, [
    "--headless=new",
    "--disable-gpu",
    "--allow-file-access-from-files",
    `--user-data-dir=${profileDir}`,
    "--window-size=1280,900",
    "--virtual-time-budget=2000",
    "--dump-dom",
    `http://127.0.0.1:${port}/${path.basename(fixtureFile)}`,
  ], { encoding: "utf8", timeout: 15000, maxBuffer: 64 * 1024 * 1024 });
  if (run.error) throw run.error;
  if (run.status !== 0 || !/data-collapse-test="pass"/.test(run.stdout)) {
    const detail = (run.stdout.match(/<output id="collapse-test">([^<]*)<\/output>/) || [])[1] || run.stderr || "检测失败";
    console.error(`FAIL: ${detail}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 展开全部并滚动后，收起控件可见且不会强制滚动页面。");
  }
} finally {
  if (server) server.kill();
  fs.rmSync(fixtureFile, { force: true });
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolved = fs.realpathSync(profileDir);
  if (!resolved.startsWith(tempRoot + path.sep)) throw new Error(`拒绝清理临时目录之外的路径：${resolved}`);
  fs.rmSync(resolved, { recursive: true, force: true });
}
