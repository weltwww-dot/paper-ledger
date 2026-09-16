/*
 * 六段式总结解析器（paper-summarize-fetch 输出格式）
 * 浏览器（<script> → window.PaperParser）与 Node（require）共用同一实现，
 * 避免解析逻辑在两处复制后漂移。纯函数，零 DOM / 零 Node 依赖。
 *
 * 接口:
 *   parseSummary(md: string) → PaperEntry
 *   parseAll(mds: string[]) → PaperEntry[]   （过滤无标题条目）
 *   entryId(title: string) → string           （标题哈希稳定 id）
 *   sectionize / pickLine / splitVenue        （低层，供测试与扩展）
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.PaperParser = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  /* 把 Markdown 按 ## 标题切成段落 */
  function sectionize(md) {
    const sections = {};
    let current = null;
    for (const raw of md.split(/\r?\n/)) {
      const m = raw.match(/^#{1,3}\s*(.+?)\s*$/);
      if (m) {
        current = m[1].replace(/[*_`]/g, "").trim();
        sections[current] = [];
      } else if (current) {
        sections[current].push(raw);
      }
    }
    const out = {};
    for (const [k, v] of Object.entries(sections)) {
      out[k] = v.join("\n").replace(/\n{2,}/g, "\n").trim();
    }
    return out;
  }

  /* 从基本信息区逐行提取 `- **键**: 值`（容忍加粗与行首符号） */
  function pickLine(text, key) {
    if (!text) return "";
    for (const raw of text.split("\n")) {
      const line = raw.replace(/^[-*]\s+/, "").replace(/\*\*/g, "").trim();
      const m = line.match(new RegExp("^" + key + "\\s*[:：]\\s*(.+)$", "i"));
      if (m) return m[1].trim();
    }
    return "";
  }

  /*
   * "期刊 2026" / "期刊-2026" / "期刊 201 (2026)" → { journal, year }
   *
   * 早期总结曾使用“期刊 / 年份”“期刊 / 卷号文章号”等字段，值中还可能带
   * 卷期、文章号或日期说明。年份不必恰好位于行尾；保留卷期，剥离年份后的
   * 说明文字，避免台账因旧模板而显示为空。
   */
  function splitVenue(venue) {
    const original = String(venue || "").trim();
    if (!original) return { journal: "", year: "" };

    /* “日期语义”字段以分号附带来源说明；期刊名只取第一个分号前的部分。 */
    const source = original.split(/[；;]/, 1)[0].trim();
    const year = ((original.match(/\b(?:19|20)\d{2}\b/) || [])[0] || "").trim();
    if (!year) return { journal: source, year: "" };

    let journal = source
      .replace(new RegExp("\\s*[（(]\\s*" + year + "\\s*[）)].*$"), "")
      .replace(new RegExp("[\\s,，:：;；\\-—–]+" + year + ".*$"), "")
      .replace(/[·,，:：;；\-—–\s]+$/g, "")
      .trim();
    if (!journal) journal = source;
    return { journal, year };
  }

  /* Markdown 六段式总结 → 论文条目（字段与台账数据模型一致） */
  function parseSummary(md) {
    const s = sectionize(md);
    const basicRaw = s["基本信息"] || "";
    const basic = basicRaw
      .split("\n")
      .map((l) => l.replace(/^[-*]\s+/, "").replace(/\*\*/g, "").trim())
      .join("\n");
    const venueRaw =
      pickLine(basic, "期刊\\s*[/／]\\s*会议") ||
      pickLine(basic, "期刊\\s*[/／]\\s*年份") ||
      pickLine(basic, "期刊\\s*[/／]\\s*卷号文章号") ||
      pickLine(basic, "期刊\\s*[/／]\\s*日期语义") ||
      pickLine(basic, "会议与年份") ||
      pickLine(basic, "会议") ||
      pickLine(basic, "期刊");
    const { journal, year } = splitVenue(venueRaw);
    const semanticDate = (String(venueRaw).match(/\b(?:19|20)\d{2}-\d{2}-\d{2}\b/) || [])[0] || "";
    /* 未提供精确发表日时，只展示来源中明确给出的年份，不能凭空补日期。 */
    const published = pickLine(basic, "发表") || pickLine(basic, "发表年份") || semanticDate || pickLine(basic, "年份") || year;
    const contentRaw = pickLine(basic, "内容状态");
    let contentState = "";
    let contentNote = "";
    if (contentRaw) {
      const m = contentRaw.match(/^(完整|已完整|待补全|部分)\s*[·,，;；:：]?\s*(.*)$/);
      const state = m ? m[1] : "";
      contentState = state === "待补全" ? "pending" : state === "部分" ? "partial" : state === "完整" || state === "已完整" ? "complete" : "";
      contentNote = (m && m[2] ? m[2] : contentRaw).trim();
    }

    const arxiv =
      (String(basic).match(/arXiv[:：#\s]*(\d{4}\.\d{4,5}(v\d+)?)/i) || [])[1] || "";
    const doi =
      (String(basic).match(/10\.\d{4,9}\/[-._;()/:A-Z0-9]+/i) || [])[0] || "";
    const pdf =
      (String(basic).match(/\[([^\]]+\.pdf)\]\(\s*([^)\s]+)\s*\)/i) || [])[2] ||
      (String(basic).match(/https?:\/\/\S+\.pdf/i) || [])[0] ||
      "";

    return {
      title: pickLine(basic, "标题"),
      authors: pickLine(basic, "作者"),
      journal,
      year,
      published,
      contentState,
      contentNote,
      doi,
      arxiv,
      pdf,
      link: arxiv ? "https://arxiv.org/abs/" + arxiv : doi ? "https://doi.org/" + doi : "",
      direction: pickLine(basic, "研究方向"),
      summary: s["一句话概括"] || "",
      question: s["问题与动机"] || "",
      method: s["方法"] || "",
      experiments: s["实验与结果"] || "",
      contribution: s["贡献与局限"] || "",
      sample: false,
    };
  }

  function parseAll(mds) {
    const out = [];
    for (const md of mds) {
      const entry = parseSummary(md);
      if (entry.title) out.push(entry);
    }
    return out;
  }

  /* 稳定 id：标题哈希 → 同一标题永远同一 id（跨语言、跨顺序稳定） */
  function titleHash(title) {
    let h = 0;
    for (let i = 0; i < title.length; i++) {
      h = (Math.imul(31, h) + title.charCodeAt(i)) | 0;
    }
    return (h >>> 0).toString(36);
  }

  function entryId(title) {
    return "r-" + titleHash(title);
  }

  return {
    sectionize,
    pickLine,
    splitVenue,
    parseSummary,
    parseAll,
    entryId,
  };
});
