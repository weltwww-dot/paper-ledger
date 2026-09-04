/*
 * 主题统计模块（研究热点 / 收录趋势）
 * 浏览器（<script> → window.ThemeStats）与 Node（require）共用。
 * 纯函数：输入论文列表（含 direction / tags 数组，顺序 = 收录倒序），
 * 输出热点排行与近/前两窗口的趋势对比，不做任何 DOM 操作。
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.ThemeStats = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  const RECENT_DEFAULT = 12;
  const WINDOW_DAYS_DEFAULT = 90;

  /* "a；b、c,d" → ["a","b","c","d"] */
  function splitTags(value) {
    return String(value || "")
      .split(/[；;、,，|]/)
      .map((s) => s.trim())
      .filter(Boolean);
  }

  /* 单篇去重后的标签集合 */
  function tagsOf(paper) {
    return Array.isArray(paper.tags) ? [...new Set(paper.tags.map((t) => String(t).trim()).filter(Boolean))] : [];
  }

  function byDirection(papers, direction) {
    if (!direction || direction === "全部") return papers;
    return papers.filter((p) => p.direction === direction);
  }

  /*
   * 统计窗口：只保留 published >= since 的论文（since = 'YYYY-MM-DD'）。
   * since 为空时不做时间过滤，保持旧行为（测试/兼容）。
   */
  function byWindow(papers, since) {
    if (!since) return papers;
    return papers.filter((p) => p.published && p.published >= since);
  }

  /* 方向 + 时间窗口组合过滤（热点/趋势/统计范围 chips 共用） */
  function filterScope(papers, options) {
    return byWindow(byDirection(papers, options && options.direction), options && options.since);
  }

  /* 各研究方向的篇数（全部 / 信息安全 / 人工智能），用于统计范围 chips */
  function scopeCounts(papers, directions, since) {
    const out = new Map();
    out.set("全部", filterScope(papers, { since }).length);
    for (const d of directions || []) out.set(d, 0);
    for (const p of papers) {
      if (p.direction && out.has(p.direction) && (!since || (p.published && p.published >= since))) {
        out.set(p.direction, out.get(p.direction) + 1);
      }
    }
    return out;
  }

  /*
   * 热点：范围内每篇论文的标签实例数排行。
   * 返回 [{ tag, count, share }]（share = count / 范围内总篇数），按 count 降序、标签名升序。
   */
  function hotTags(papers, options) {
    const scope = filterScope(papers, options);
    const total = scope.length;
    const count = new Map();
    for (const p of scope) {
      for (const t of tagsOf(p)) count.set(t, (count.get(t) || 0) + 1);
    }
    return [...count.entries()]
      .map(([tag, n]) => ({ tag, count: n, share: total ? n / total : 0 }))
      .sort((a, b) => b.count - a.count || (a.tag < b.tag ? -1 : a.tag > b.tag ? 1 : 0));
  }

  /*
   * 趋势：按论文「发表时间」（published，YYYY-MM-DD）倒序取最近 recentK 篇，
   * 与此前发表的论文做标签占比对比。数组本身无需保持任何顺序——
   * module 内部先按 published 排序（缺失日期的排最后），不再信任调用方顺序。
   * 返回 { recentN, olderN, rows }：
   *   row.state: "new"（此前没有）| "rising" | "falling"
   *   row.delta = 近窗口占比 - 前窗口占比（百分点单位由调用方换算）
   */
  function trend(papers, options) {
    const scope = filterScope(papers, options);
    const ordered = [...scope].sort((a, b) => {
      const da = a.published || "";
      const db = b.published || "";
      if (da && db) return da < db ? 1 : da > db ? -1 : 0;
      if (da) return -1; // 有日期的在前（倒序），无日期的沉底
      if (db) return 1;
      return 0;
    });
    const recentN = Math.max(1, Math.min(options && options.recentK ? options.recentK : RECENT_DEFAULT, ordered.length));
    const recent = ordered.slice(0, recentN);
    const older = ordered.slice(recentN);
    const olderN = older.length;

    function tally(list) {
      const map = new Map();
      for (const p of list) {
        for (const t of tagsOf(p)) map.set(t, (map.get(t) || 0) + 1);
      }
      return map;
    }
    const rMap = tally(recent);
    const oMap = tally(older);
    const names = new Set([...rMap.keys(), ...oMap.keys()]);

    const rows = [];
    for (const tag of names) {
      const cR = rMap.get(tag) || 0;
      const cO = oMap.get(tag) || 0;
      if (cR === 0 && cO === 0) continue;
      const shareR = cR / recentN;
      const shareO = olderN ? cO / olderN : 0;
      const delta = olderN ? shareR - shareO : shareR;
      const state = cO === 0 && cR > 0 ? "new" : olderN === 0 ? "rising" : delta > 0 ? "rising" : delta < 0 ? "falling" : null;
      if (state) rows.push({ tag, countR: cR, countO: cO, shareR, shareO, delta, state });
    }
    rows.sort(
      (a, b) =>
        (b.state === "new" ? 1 : 0) - (a.state === "new" ? 1 : 0) ||
        b.delta - a.delta
    );
    return { recentN, olderN, rows };
  }

  return {
    splitTags,
    tagsOf,
    byDirection,
    byWindow,
    filterScope,
    scopeCounts,
    hotTags,
    trend,
    RECENT_DEFAULT,
    WINDOW_DAYS_DEFAULT,
  };
});
