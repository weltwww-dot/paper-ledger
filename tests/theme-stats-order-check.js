#!/usr/bin/env node
"use strict";

const assert = require("assert");
const { sortByPublished } = require("../shared/theme-stats.js");

const papers = [
  { id: "same-iso", published: "2026-09-10（在线发表）" },
  { id: "same-zh", published: "2026年9月10日" },
  { id: "older-iso", published: "2026-09-09" },
  { id: "year-only", published: "2026年" },
  { id: "prior-year", published: "2025-12-31" },
  { id: "invalid-day", published: "2026-02-30" },
  { id: "invalid-text", published: "日期未知" },
  { id: "missing", published: "" },
];
const before = JSON.parse(JSON.stringify(papers));

assert.deepStrictEqual(
  sortByPublished(papers).map((paper) => paper.id),
  ["same-iso", "same-zh", "older-iso", "year-only", "prior-year", "invalid-day", "invalid-text", "missing"]
);
assert.deepStrictEqual(papers, before);
console.log("PASS: 发表时间支持 ISO、中文、年份及无效值的稳定倒序，且不修改输入列表。");
