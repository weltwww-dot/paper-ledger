#!/usr/bin/env node
"use strict";

/*
 * 展开论文卡片的真实浏览器布局回归：长公式、DOI 与连续英文不得撑出卡片。
 * 用法：node tests/layout-overflow-check.js
 */

const fs = require("fs");
const os = require("os");
const path = require("path");
const { pathToFileURL } = require("url");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const EDGE_CANDIDATES = [
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];
const edge = EDGE_CANDIDATES.find((candidate) => fs.existsSync(candidate));

if (!edge) {
  console.error("FAIL: 未找到 Microsoft Edge，无法执行布局回归测试。");
  process.exit(1);
}

const stylesUrl = pathToFileURL(path.join(ROOT, "styles.css")).href;
const tokensUrl = pathToFileURL(path.join(ROOT, "tokens.css")).href;
const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "paper-ledger-layout-"));
const fixtureFile = path.join(profileDir, "fixture.html");

const longToken = "EXPTIMECOMPLETE".repeat(32);
const html = `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="${tokensUrl}">
  <link rel="stylesheet" href="${stylesUrl}">
  <style>body{margin:0}.paper-grid{width:1200px;margin:0 auto}</style>
</head>
<body>
  <main class="paper-grid">
    ${Array.from({ length: 3 }, (_, index) => `
      <details class="paper" open>
        <summary class="paper__summary">
          <div class="paper__meta-row"><span class="tag">人工智能</span></div>
          <h3 class="paper__title">Expanded paper ${index + 1}</h3>
          <p class="paper__journal">Artificial Intelligence · 2026</p>
        </summary>
        <div class="paper__body"><div class="paper__body-inner">
          <div class="paper__blocks">
            <div class="paper__block">
              <span class="paper__block-label">方法</span>
              <p class="paper__block-text">${longToken}</p>
            </div>
          </div>
          <div class="paper__foot"><a class="link" href="#">${longToken}</a></div>
        </div></div>
      </details>`).join("")}
  </main>
  <output id="result"></output>
  <script>
    const failures = [];
    document.querySelectorAll('.paper').forEach((card, cardIndex) => {
      const cardBox = card.getBoundingClientRect();
      card.querySelectorAll('.paper__blocks, .paper__block, .paper__block-text, .paper__foot, .paper__foot .link')
        .forEach((node) => {
          const box = node.getBoundingClientRect();
          const outside = box.left < cardBox.left - 1 || box.right > cardBox.right + 1;
          const internallyOverflowing = node.scrollWidth > node.clientWidth + 1;
          if (outside || internallyOverflowing) {
            failures.push(cardIndex + ':' + node.className + ':' + node.clientWidth + '/' + node.scrollWidth);
          }
        });
    });
    document.documentElement.dataset.layoutTest = failures.length ? 'fail' : 'pass';
    document.getElementById('result').textContent = failures.join('|');
  </script>
</body>
</html>`;

try {
  fs.writeFileSync(fixtureFile, html, "utf8");
  const run = spawnSync(edge, [
    "--headless=new",
    "--edge-skip-compat-layer-relaunch",
    "--disable-gpu",
    "--allow-file-access-from-files",
    `--user-data-dir=${profileDir}`,
    "--window-size=1280,900",
    "--virtual-time-budget=1000",
    "--dump-dom",
    pathToFileURL(fixtureFile).href,
  ], { encoding: "utf8", timeout: 15000 });

  if (run.error) throw run.error;
  if (run.status !== 0) {
    console.error(run.stderr || `FAIL: Edge 退出码 ${run.status}`);
    process.exitCode = 1;
  } else if (!/data-layout-test="pass"/.test(run.stdout)) {
    const detail = (run.stdout.match(/<output id="result">([^<]*)<\/output>/) || [])[1] || "未取得检测结果";
    console.error(`FAIL: 展开卡片存在横向文字溢出：${detail}`);
    process.exitCode = 1;
  } else {
    console.log("PASS: 展开卡片的正文、长公式和链接均未越出卡片边界。");
  }
} finally {
  const tempRoot = fs.realpathSync(os.tmpdir());
  const resolvedProfile = fs.realpathSync(profileDir);
  if (!resolvedProfile.startsWith(tempRoot + path.sep)) {
    throw new Error(`拒绝清理临时目录之外的路径：${resolvedProfile}`);
  }
  fs.rmSync(resolvedProfile, { recursive: true, force: true });
}
