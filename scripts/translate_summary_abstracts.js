#!/usr/bin/env node
/* 兼容入口：统一转交给 D 盘的本地 Argos 英译中模型。 */

const { spawnSync } = require("child_process");
const path = require("path");

const python = process.env.PAPER_LEDGER_TRANSLATION_PYTHON ||
  "D:\\OpenSourceModels\\argos-translate\\.venv\\Scripts\\python.exe";
const script = path.join(__dirname, "translate_summary_abstracts_local.py");
const result = spawnSync(python, ["-X", "utf8", script], { stdio: "inherit" });
if (result.error) {
  console.error(`无法启动本地翻译模型: ${result.error.message}`);
  process.exit(1);
}
process.exit(result.status ?? 1);
