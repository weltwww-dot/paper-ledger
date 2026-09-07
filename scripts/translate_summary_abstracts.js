#!/usr/bin/env node
/* 已停用：中文六段式由当前执行 agent 亲自撰写，禁止上传或调用本地翻译模型。 */

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
