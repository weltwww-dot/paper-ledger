#!/usr/bin/env node
/*
 * 论文台账 · 自动同步脚本
 * 扫描 summaries/*.md（paper-summarize-fetch 六段式总结），生成 data/papers.js。
 * 已收录条目保持原 id 与相对顺序；新总结排在最前（作为最新收录）。
 * 用法: node scripts/sync-papers.js
 */

const fs = require("fs");
const path = require("path");
const Parser = require(path.join(__dirname, "..", "shared", "paper-parser.js"));

const ROOT = path.resolve(__dirname, "..");
const SUMMARIES_DIR = path.join(ROOT, "summaries");
const OUT_DIR = path.join(ROOT, "data");
const OUT_FILE = path.join(OUT_DIR, "papers.js");

/* ── 主流程 ──────────────────────────────────────────────────────── */
function main() {
  if (!fs.existsSync(SUMMARIES_DIR)) {
    console.error("summaries/ 目录不存在:", SUMMARIES_DIR);
    process.exit(1);
  }

  const files = fs.readdirSync(SUMMARIES_DIR).filter((f) => f.endsWith(".md")).sort();
  const parsed = [];
  for (const f of files) {
    const md = fs.readFileSync(path.join(SUMMARIES_DIR, f), "utf8");
    const entry = Parser.parseSummary(md);
    if (!entry.title) {
      console.warn("跳过（无标题）:", f);
      continue;
    }
    entry.id = Parser.entryId(entry.title);
    entry._file = f;
    parsed.push(entry);
  }

  /* 读取现有数据，保持已收录条目的相对顺序；新条目（按标题判断）放最前 */
  let existing = [];
  if (fs.existsSync(OUT_FILE)) {
    try {
      const src = fs.readFileSync(OUT_FILE, "utf8");
      const m = src.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
      if (m) existing = JSON.parse(m[1]);
    } catch (err) {
      console.warn("现有 data/papers.js 解析失败，重新生成:", err.message);
      existing = [];
    }
  }

  const existingTitles = new Set(existing.map((p) => p.title));
  const fresh = parsed.filter((p) => !existingTitles.has(p.title));
  const known = parsed.filter((p) => existingTitles.has(p.title));
  const knownOrder = [];
  for (const ex of existing) {
    const match = known.find((p) => p.title === ex.title);
    if (match) knownOrder.push(match);
  }
  for (const k of known) {
    if (!knownOrder.some((p) => p.title === k.title)) knownOrder.push(k);
  }

  const ordered = [...fresh, ...knownOrder].map(({ _file, ...p }) => p);

  fs.mkdirSync(OUT_DIR, { recursive: true });
  const body = `/* 自动生成: node scripts/sync-papers.js · 请勿手改 */\nwindow.PAPERLEDGER_SEED = ${JSON.stringify(ordered, null, 2)};\n`;
  fs.writeFileSync(OUT_FILE, body, "utf8");

  /* 数据文件版本号：更新 index.html 引用，绕过浏览器/CDN 缓存 */
  const stamp = Math.floor(Date.now() / 1000).toString(36);
  const indexFile = path.join(ROOT, "index.html");
  let indexSrc = fs.readFileSync(indexFile, "utf8");
  const next = `data/papers.js?v=${stamp}`;
  indexSrc = indexSrc.replace(/data\/papers\.js(\?v=[a-z0-9]+)?/g, next);
  fs.writeFileSync(indexFile, indexSrc, "utf8");

  console.log(`已同步 ${ordered.length} 篇 → data/papers.js`);
  console.log(`版本号已更新 → index.html 引用 ${next}`);
  if (fresh.length) {
    console.log("新增:", fresh.map((p) => "  " + p.title.slice(0, 70)).join("\n"));
  } else {
    console.log("无新增总结。");
  }
}

main();
