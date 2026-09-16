#!/usr/bin/env node
"use strict";

const assert = require("assert");
const Parser = require("../shared/paper-parser.js");

function summary(lines) {
  return `# 测试论文 总结\n\n## 基本信息\n\n${lines.join("\n")}\n\n## 一句话概括\n\n测试。`;
}

const legacyVenue = Parser.parseSummary(summary([
  "- **标题**：旧模板期刊年份字段",
  "- **期刊 / 年份**：IEEE Transactions on Knowledge and Data Engineering，2026",
]));
assert.deepStrictEqual(
  { journal: legacyVenue.journal, year: legacyVenue.year, published: legacyVenue.published },
  { journal: "IEEE Transactions on Knowledge and Data Engineering", year: "2026", published: "2026" },
  "旧模板的‘期刊 / 年份’必须保留期刊并以已知年份作为发表时间兜底",
);

const volumeVenue = Parser.parseSummary(summary([
  "- **标题**：卷期字段",
  "- **期刊 / 卷号文章号**：Machine Learning, 115:217 (2026)",
]));
assert.deepStrictEqual(
  { journal: volumeVenue.journal, year: volumeVenue.year, published: volumeVenue.published },
  { journal: "Machine Learning, 115:217", year: "2026", published: "2026" },
  "卷期中的年份必须被识别，不能让台账丢失期刊与时间",
);

const semanticDateVenue = Parser.parseSummary(summary([
  "- **标题**：日期语义字段",
  "- **期刊 / 日期语义**：IEEE Transactions on Pattern Analysis and Machine Intelligence；原始出版：2024（全文注明 2024-04-29，版权为 © 2024 IEEE）；当前版本年份：2026",
]));
assert.deepStrictEqual(
  { journal: semanticDateVenue.journal, year: semanticDateVenue.year, published: semanticDateVenue.published },
  { journal: "IEEE Transactions on Pattern Analysis and Machine Intelligence", year: "2024", published: "2024-04-29" },
  "日期语义字段应优先采用原始出版日期，而非任务批次年份",
);

console.log("PASS: 旧版元信息字段可稳定解析为期刊、年份和发表时间。");
