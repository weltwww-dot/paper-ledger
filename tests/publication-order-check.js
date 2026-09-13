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
