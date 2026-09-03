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

  /* "期刊 2026" / "期刊-2026" → { journal, year } */
  function splitVenue(venue) {
    const m = String(venue).match(/^(.*?)\s*[-–—]\s*(\d{4})$|^(.*?)\s*(\d{4})\s*$/);
    if (!m) return { journal: venue, year: "" };
    const journal = (m[1] || m[3] || venue).replace(/[·,，:：;；\-—–\s]+$/g, "").trim();
    const year = (m[2] || m[4] || "").trim();
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
      pickLine(basic, "会议") ||
      pickLine(basic, "期刊");
    const { journal, year } = splitVenue(venueRaw);

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
