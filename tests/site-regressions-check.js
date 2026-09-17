#!/usr/bin/env node
"use strict";

/* 一次真实浏览器会话覆盖：长文本布局、收起交互、PDF 新标签及发表时间倒序。 */

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
  console.error("FAIL: 未找到 Microsoft Edge，无法执行网站回归测试。");
  process.exit(1);
}

const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "paper-ledger-regressions-"));
const fixtureFile = path.join(ROOT, `.site-regressions-${process.pid}.html`);
const port = 21000 + (process.pid % 10000);
const longToken = "EXPTIMECOMPLETE".repeat(32);
const dates = [
  ["invalid-day", "2026-02-30"],
  ["same-iso", "2026-09-10"],
  ["invalid-text", "日期未知"],
  ["year-only", "2026年"],
  ["same-zh", "2026年9月10日"],
  ["missing", ""],
  ["older-iso", "2026-09-09"],
  ["prior-year", "2025-12-31"],
];
const expectedOrder = ["same-iso", "same-zh", "older-iso", "year-only", "prior-year", "invalid-day", "invalid-text", "missing"];
const seed = dates.map(([id, published]) => ({
  id,
  title: id === "same-iso" ? longToken : `Regression ${id}`,
  journal: "Regression Journal",
  year: "2026",
  published,
  direction: "人工智能",
  summary: "用于验证论文台账前端回归的测试摘要。",
  question: "用于验证展开、收起与排序交互是否保持稳定。",
  method: id === "same-iso" ? longToken : "通过受控测试数据验证关键交互。",
  experiments: "浏览器端执行布局、导航与排序断言。",
  contribution: "以一次浏览器会话覆盖四类关键回归。",
  doi: `10.1000/${id}`,
  pdf: id === "same-iso" ? `papers/${longToken}.pdf` : "",
}));

let server;
let html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
html = html.replace(/<script src="data\/papers\.js(?:\?v=[^"]*)?" defer><\/script>/, `<script>window.PAPERLEDGER_SEED = ${JSON.stringify(seed)};</script>`);
html = html.replace("</body>", `<output id="site-regressions-test"></output>
  <script>
    const expectedOrder = ${JSON.stringify(expectedOrder)};
    let scrollRequest = null;
    Element.prototype.scrollIntoView = function(options) {
      scrollRequest = { target: this.id, behavior: options && options.behavior, block: options && options.block };
    };
    function report() {
      const failures = [];
      const latest = document.querySelector('#latest');
      const more = document.querySelector('#latest-more');
      const floating = document.querySelector('#latest-collapse-floating');
      if (more && !more.hidden && /查看全部/.test(more.textContent)) more.click();

      const actualOrder = [...document.querySelectorAll('#latest-list .paper')].map((card) => card.dataset.id);
      if (JSON.stringify(actualOrder) !== JSON.stringify(expectedOrder)) {
        failures.push('发表时间顺序:' + JSON.stringify({ expected: expectedOrder, actual: actualOrder }));
      }

      document.querySelectorAll('#latest-list .paper').forEach((card) => { card.open = true; });
      document.querySelectorAll('#latest-list .paper').forEach((card, cardIndex) => {
        const cardBox = card.getBoundingClientRect();
        card.querySelectorAll('.paper__blocks, .paper__block, .paper__block-text, .paper__foot, .paper__foot .link').forEach((node) => {
          const box = node.getBoundingClientRect();
          if (box.left < cardBox.left - 1 || box.right > cardBox.right + 1 || node.scrollWidth > node.clientWidth + 1) {
            failures.push('横向溢出:' + cardIndex + ':' + node.className + ':' + node.clientWidth + '/' + node.scrollWidth);
          }
        });
      });

      const pdfLink = [...document.querySelectorAll('.paper__foot a')].find((link) => link.textContent.includes('PDF'));
      if (!pdfLink || pdfLink.target !== '_blank' || !pdfLink.rel.split(/\\s+/).includes('noopener') || !pdfLink.rel.split(/\\s+/).includes('noreferrer')) {
        failures.push('PDF导航:' + JSON.stringify({ href: pdfLink && pdfLink.getAttribute('href'), target: pdfLink && pdfLink.target, rel: pdfLink && pdfLink.rel }));
      }

      const expandedCardCount = document.querySelectorAll('.paper').length;
      const rect = floating && floating.getBoundingClientRect();
      const style = floating && getComputedStyle(floating);
      const floatingVisible = Boolean(floating && !floating.hidden && style.display !== 'none' && rect.bottom > 0 && rect.top < innerHeight && rect.right > 0 && rect.left < innerWidth);
      scrollRequest = null;
      if (floating) floating.click();
      const stayedExpandedDuringScroll = more.textContent.includes('收起') && document.querySelectorAll('.paper').length === expandedCardCount;
      const smoothRequested = Boolean(scrollRequest && scrollRequest.target === 'latest' && scrollRequest.behavior === 'smooth' && scrollRequest.block === 'start');
      window.dispatchEvent(new Event('scrollend'));
      window.setTimeout(() => {
        const collapsed = !more.hidden && more.textContent.includes('查看全部') && document.querySelectorAll('.paper').length < expandedCardCount;
        if (!floatingVisible || !smoothRequested || !stayedExpandedDuringScroll || !collapsed) {
          failures.push('收起交互:' + JSON.stringify({ floatingVisible, smoothRequested, stayedExpandedDuringScroll, collapsed, scrollRequest, latestTop: latest && latest.getBoundingClientRect().top }));
        }
        document.documentElement.dataset.siteRegressionsTest = failures.length ? 'fail' : 'pass';
        document.querySelector('#site-regressions-test').textContent = failures.join('|');
      }, 0);
    }
    window.addEventListener('load', () => window.setTimeout(report, 0));
  </script></body>`);

try {
  fs.writeFileSync(fixtureFile, html, "utf8");
  server = spawn("python", ["-m", "http.server", String(port), "--bind", "127.0.0.1", "--directory", ROOT], { stdio: "ignore", windowsHide: true });
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 1000);
  const run = spawnSync(edge, [
    "--headless=new", "--edge-skip-compat-layer-relaunch", "--disable-gpu",
    `--user-data-dir=${profileDir}`, "--window-size=1280,900", "--virtual-time-budget=5000", "--dump-dom",
    `http://127.0.0.1:${port}/${path.basename(fixtureFile)}`,
  ], { encoding: "utf8", timeout: 15000, maxBuffer: 64 * 1024 * 1024 });
  if (run.error) throw run.error;
  if (run.status !== 0 || !/data-site-regressions-test="pass"/.test(run.stdout)) {
    const state = (run.stdout.match(/data-site-regressions-test="([^"]+)"/) || [])[1] || "未执行";
    const detail = (run.stdout.match(/<output id="site-regressions-test">([^<]*)<\/output>/) || [])[1] || "未返回诊断详情";
    console.error(`FAIL: state=${state}; ${detail}; browserStatus=${run.status}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 一次浏览器会话通过布局、收起、PDF 导航与发表时间顺序回归。 ");
  }
} finally {
  if (server) server.kill();
  fs.rmSync(fixtureFile, { force: true });
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolvedProfile = fs.realpathSync(profileDir);
  if (!resolvedProfile.startsWith(tempRoot + path.sep)) throw new Error(`拒绝清理临时目录之外的路径：${resolvedProfile}`);
  fs.rmSync(resolvedProfile, { recursive: true, force: true });
}
