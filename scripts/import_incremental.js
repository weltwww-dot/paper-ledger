#!/usr/bin/env node
/*
 * 把一次增量抓取结果登记为可审阅的待处理条目。
 * 不伪造作者、六段式总结或本地 PDF；已有 DOI 会跳过。
 * 用法: node scripts/import_incremental.js [--dry-run]
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = path.resolve(__dirname, "..");
const RUNS = path.join(ROOT, "skill-runs");
const SUMMARIES = path.join(ROOT, "summaries");
const DATA_FILE = path.join(ROOT, "data", "papers.js");
const RECORDS_FILE = path.join(RUNS, "records_inc.json");
const OA_FILE = path.join(RUNS, "oa_inc.json");
const CONTENT_FILE = path.join(RUNS, "content_inc.json");
const dryRun = process.argv.includes("--dry-run");

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function existingPapers() {
  const source = fs.readFileSync(DATA_FILE, "utf8");
  const match = source.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
  if (!match) throw new Error("data/papers.js 解析失败");
  return JSON.parse(match[1]);
}

function existingSummaryDois() {
  const out = new Set();
  for (const file of fs.readdirSync(SUMMARIES).filter((name) => name.endsWith(".md"))) {
    const text = fs.readFileSync(path.join(SUMMARIES, file), "utf8");
    for (const match of text.matchAll(/10\.\d{4,9}\/[\-._;()/:A-Z0-9]+/gi)) {
      out.add(match[0].toLowerCase().replace(/[),.;]+$/, ""));
    }
  }
  return out;
}

function slugFor(doi) {
  return crypto.createHash("sha1").update(doi).digest("hex").slice(0, 12);
}

function directionFor(journal) {
  if (/security|privacy|cyber|dependable|secure/i.test(journal)) return "信息安全";
  if (/pattern analysis|neural networks|machine learning|artificial intelligence|nature machine/i.test(journal)) return "人工智能";
  if (/knowledge and data engineering/i.test(journal)) return "数据工程";
  return "待分类";
}

function cleanText(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function splitSentences(text) {
  return cleanText(text).split(/(?<=[.!?。！？])\s+/).filter((part) => part.length >= 8);
}

function selectSentences(parts, pattern, fallback) {
  const matched = parts.filter((part) => pattern.test(part));
  return cleanText((matched.length ? matched : fallback).slice(0, 3).join(" "));
}

function draftSections(record, abstract) {
  if (!abstract) {
    const title = `《${record.title}》`;
    const direction = directionFor(record.source);
    return {
      summary: `该研究围绕${title}所描述的任务展开，所属方向为${direction}。`,
      question: `从题目可判断，论文关注${title}对应的${direction}问题，研究重点由标题所述任务界定。`,
      method: `题目表明研究围绕标题中的核心技术路线展开；仅凭现有题录无法可靠确定具体模型结构与实现步骤。`,
      experiments: "现有题录没有给出可核验的实验数据、对照方法或评价指标，因此这里不补写未经证实的结果。",
      contribution: `可确认的贡献定位是处理${title}所述任务；具体创新点、适用条件和局限仍需以论文正文为准。`,
    };
  }
  const parts = splitSentences(abstract);
  const first = parts.slice(0, 2);
  return {
    summary: cleanText(first.join(" ") || abstract),
    question: cleanText(first.join(" ") || abstract),
    method: selectSentences(parts, /propos|introduc|develop|design|method|model|framework|algorithm|approach/i, parts.slice(1, 3)),
    experiments: selectSentences(parts, /experiment|result|show|demonstrat|outperform|improv|reduc|evaluat/i, ["The available abstract does not report verifiable experimental settings or numerical results; no unsupported result is added here."]),
    contribution: selectSentences(parts, /contribut|novel|first|provide|enable|overall|conclu/i, parts.slice(-2)),
  };
}

function markdownFor(record, oa, content) {
  const abstract = cleanText(content && content.kind === "ok" ? content.text : "");
  const hasAbstract = Boolean(abstract);
  const state = hasAbstract ? "部分" : "待补全";
  const note = hasAbstract
    ? "已取得公开摘要；当前 agent 须据此完成中文审校"
    : "当前仅有题录；以下内容明确区分题目推断与未证实细节";
  const draft = draftSections(record, abstract);
  const arxiv = cleanText(oa && oa.arxiv_id);
  const year = String(record.year || record.date || "").slice(0, 4);
  return `# ${record.title} 总结

## 基本信息

- **标题**: ${record.title}
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: ${record.source} ${year}
- **发表**: ${record.date || "待补全"}
- **内容状态**: ${state} · ${note}
- **研究方向**: ${directionFor(record.source)}
- **DOI**: ${record.doi}
- **arXiv**: ${arxiv || "无"}
- **PDF**: 待探测

## 一句话概括

${draft.summary}

## 问题与动机

${draft.question}

## 方法

${draft.method}

## 实验与结果

${draft.experiments}

## 贡献与局限

${draft.contribution}

---
DOI: ${record.doi}
`;
}

function main() {
  const records = readJson(RECORDS_FILE);
  const oa = new Map(readJson(OA_FILE).map((item) => [String(item.doi).toLowerCase(), item]));
  const content = new Map(readJson(CONTENT_FILE).map((item) => [String(item.doi).toLowerCase(), item]));
  const known = new Set(existingPapers().map((paper) => String(paper.doi || "").toLowerCase()));
  for (const doi of existingSummaryDois()) known.add(doi);

  const fresh = records.filter((record) => !known.has(String(record.doi).toLowerCase()));
  if (dryRun) {
    console.log(`待导入 ${fresh.length} 篇（抓取记录 ${records.length} 篇，已知 DOI ${known.size} 个）`);
    return;
  }

  fs.mkdirSync(SUMMARIES, { recursive: true });
  for (const record of fresh) {
    const key = String(record.doi).toLowerCase();
    const file = `待补全_${slugFor(record.doi)}.md`;
    fs.writeFileSync(path.join(SUMMARIES, file), markdownFor(record, oa.get(key), content.get(key)), "utf8");
  }
  console.log(`已生成 ${fresh.length} 个待处理总结文件 → summaries/`);
}

main();
