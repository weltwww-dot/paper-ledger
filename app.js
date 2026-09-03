/* 论文台账 · ledger logic
   Data model follows the paper-summarize-fetch six-part template:
   basic info (title/authors/venue/year/doi/arxiv/pdf) → 一句话概括 summary
   → 问题与动机 question → 方法 method → 实验与结果 experiments → 贡献与局限 contribution.
   Older three-field entries are migrated on load. Data lives in localStorage. */

(() => {
  "use strict";

  const LATEST_LIMIT = 4;

  /* 共享模块：解析器 + 存储引擎（index.html 在 app.js 之前加载） */
  const Parser = window.PaperParser;
  const ThemeStats = window.ThemeStats;
  const store = window.LedgerStore.create({
    seed:
      typeof window !== "undefined" && Array.isArray(window.PAPERLEDGER_SEED)
        ? window.PAPERLEDGER_SEED
        : [],
    storageKey: "paperledger.v1",
    deletedKey: "paperledger.deleted.v1",
    storage: window.localStorage,
  });
  let papers = store.list();
  let directionFilter = null; // direction name or null
  let tagFilter = null; // theme tag or null
  let pulseScope = "全部"; // 热点/趋势的统计范围
  let pulseHotAll = false;
  let showAll = false;
  const PULSE_HOT_LIMIT = 10;

  /* ── helpers ────────────────────────────────────────────────────── */
  function uniqueDirections() {
    const seen = new Map();
    for (const p of papers) {
      if (!p.direction) continue;
      seen.set(p.direction, (seen.get(p.direction) || 0) + 1);
    }
    return [...seen.entries()].sort((a, b) => b[1] - a[1]);
  }

  function visiblePapers() {
    let out = papers;
    if (directionFilter) out = out.filter((p) => p.direction === directionFilter);
    if (tagFilter) out = out.filter((p) => (p.tags || []).includes(tagFilter));
    return out;
  }

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function linkEl(href, text, className) {
    const a = el("a", className, text);
    a.href = href;
    if (/^https?:/i.test(href)) {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    }
    return a;
  }

  function paperUrl(p) {
    if (p.link) return p.link;
    if (p.doi) return "https://doi.org/" + p.doi;
    if (p.arxiv) return "https://arxiv.org/abs/" + p.arxiv;
    return "";
  }

  /* ── render: stats ──────────────────────────────────────────────── */
  function renderStats() {
    const directions = uniqueDirections();
    const questions = papers.filter(hasQuestion).length;
    setNum("#stats-count", papers.length);
    setNum("#stats-directions", directions.length);
    setNum("#stats-questions", questions);
  }

  function setNum(selector, value) {
    const node = document.querySelector(selector);
    if (!node) return;
    node.textContent = String(value);
    node.dataset.count = String(value);
  }

  /* ── render: latest rail ────────────────────────────────────────── */
  function renderLatest() {
    const list = document.querySelector("#latest-list");
    const empty = document.querySelector("#latest-empty");
    const moreBtn = document.querySelector("#latest-more");
    const count = document.querySelector("#latest-count");
    const filtered = visiblePapers();

    list.textContent = "";
    const shown = showAll ? filtered : filtered.slice(0, LATEST_LIMIT);
    for (const p of shown) list.appendChild(paperCell(p));

    const hasMore = filtered.length > LATEST_LIMIT;
    moreBtn.hidden = !hasMore;
    moreBtn.textContent = showAll ? "收起 ↑" : "查看全部 →";

    empty.hidden = filtered.length !== 0;
    if (filtered.length === 0) {
      const line = empty.querySelector(".empty__line");
      const cond = [directionFilter && `${directionFilter}方向`, tagFilter && `主题「${tagFilter}」`]
        .filter(Boolean)
        .join(" · ");
      line.textContent = papers.length === 0 ? "尚无论文收录。" : cond ? `${cond}暂无收录论文。` : "该条件下暂无收录论文。";
    }

    count.textContent = filtered.length ? `共 ${filtered.length} 篇` : "";
  }

  /* 收录区的方向筛选 chips（全部 + 各研究方向） */
  function renderFilterChips() {
    const box = document.querySelector("#filter-chips");
    if (!box) return;
    box.textContent = "";
    box.appendChild(filterChip("全部", null, papers.length));
    for (const [name, n] of uniqueDirections()) {
      box.appendChild(filterChip(name, name, n));
    }
    if (tagFilter) {
      const tag = filterChip(`主题 · ${tagFilter}`, "__tag__", null);
      tag.classList.add("is-active");
      tag.setAttribute("aria-pressed", "true");
      tag.setAttribute("title", "点击清除主题筛选");
      box.appendChild(tag);
    }
  }

  function filterChip(label, value, count) {
    const isTag = value === "__tag__";
    const active = !isTag && directionFilter === value;
    const btn = el("button", "chip" + (active ? " is-active" : ""));
    btn.type = "button";
    btn.setAttribute("aria-pressed", String(active));
    btn.textContent = count == null ? label : `${label} ${count}`;
    btn.addEventListener("click", () => (isTag ? setTagFilter(null) : setDirectionFilter(value)));
    return btn;
  }

  function paperCell(p) {
    const cell = el("details", "paper");
    cell.dataset.id = p.id;

    const summary = el("summary", "paper__summary");
    const metaRow = el("div", "paper__meta-row");
    if (p.direction) metaRow.appendChild(el("span", "tag", p.direction));
    metaRow.appendChild(el("span", "tag", p.journal + " · " + p.year));
    for (const t of p.tags || []) {
      metaRow.appendChild(el("span", "tag tag--theme", t));
    }

    const title = el("h3", "paper__title", p.title);
    const journal = el("p", "paper__journal", `${p.journal} · ${p.year}`);
    const arrow = el("span", "paper__arrow");
    arrow.setAttribute("aria-hidden", "true");

    summary.append(metaRow, title, journal, arrow);
    cell.appendChild(summary);

    const body = el("div", "paper__body");
    const inner = el("div", "paper__body-inner");
    const blocks = el("div", "paper__blocks");

    blocks.appendChild(block("一句话概括", p.summary));
    blocks.appendChild(block("问题与动机", p.question));
    blocks.appendChild(block("方法", p.method));
    blocks.appendChild(block("实验与结果", p.experiments));
    blocks.appendChild(block("贡献与局限", p.contribution));
    inner.appendChild(blocks);

    const foot = el("div", "paper__foot");
    const url = paperUrl(p);
    if (url) foot.appendChild(linkEl(url, "原文 ↗", "link"));
    if (p.pdf) foot.appendChild(linkEl(p.pdf, "PDF ↗", "link"));
    const removeBtn = el("button", "paper__remove", "移除");
    removeBtn.type = "button";
    removeBtn.addEventListener("click", () => removePaper(p.id));
    foot.appendChild(removeBtn);

    inner.appendChild(foot);
    body.appendChild(inner);
    cell.appendChild(body);
    return cell;
  }

  function block(label, text) {
    const wrap = el("div", "paper__block");
    wrap.appendChild(el("span", "paper__block-label", label));
    wrap.appendChild(el("p", "paper__block-text", text && text.trim() ? text : "—"));
    return wrap;
  }

  /* ── render: questions ──────────────────────────────────────────── */
  function renderQuestions() {
    const list = document.querySelector("#questions-list");
    const empty = document.querySelector("#questions-empty");
    const count = document.querySelector("#questions-count");
    const withQuestions = visiblePapers().filter(hasQuestion);
    const seen = new Set();

    list.textContent = "";
    for (const p of withQuestions) {
      const key = p.question.trim();
      if (seen.has(key)) continue;
      seen.add(key);
      list.appendChild(questionRow(p));
    }

    empty.hidden = seen.size !== 0;
    count.textContent = seen.size ? `${seen.size} 条` : "";
  }

  function hasQuestion(p) {
    const q = (p.question || "").trim();
    return q !== "" && !q.startsWith("原文未提供");
  }

  function questionRow(p) {
    const row = el("div", "qrow");
    const question = el("p", "qrow__question", p.question);
    question.tabIndex = 0;
    question.setAttribute("role", "button");
    question.setAttribute("aria-expanded", "false");
    question.setAttribute("title", "点击展开 / 收起完整内容");
    const toggle = () => {
      const open = row.classList.toggle("is-open");
      question.setAttribute("aria-expanded", String(open));
    };
    question.addEventListener("click", toggle);
    question.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggle();
      }
    });
    row.appendChild(question);

    const meta = el("div", "qrow__meta");
    if (p.direction) meta.appendChild(el("span", "qrow__direction", p.direction));
    const url = paperUrl(p);
    if (url) {
      meta.appendChild(linkEl(url, p.title, "qrow__paper link"));
    } else {
      meta.appendChild(el("span", "qrow__paper", p.title));
    }
    row.appendChild(meta);

    const arrow = el("span", "qrow__arrow");
    arrow.setAttribute("aria-hidden", "true");
    row.appendChild(arrow);
    return row;
  }

  /* ── render: 研究热点与趋势（#pulse）────────────────────────────── */
  function pulseCounts() {
    const dirs = uniqueDirections().map(([name]) => name);
    const counts = ThemeStats.scopeCounts(papers, dirs);
    return dirs.length ? counts : new Map([["全部", papers.length]]);
  }

  function renderPulseScopeChips() {
    const box = document.querySelector("#pulse-scope-chips");
    if (!box) return;
    const counts = pulseCounts();
    box.textContent = "";
    for (const name of ["全部", ...uniqueDirections().map(([n]) => n)]) {
      const btn = el("button", "chip" + (pulseScope === name ? " is-active" : ""));
      btn.type = "button";
      btn.setAttribute("aria-pressed", String(pulseScope === name));
      btn.textContent = `${name} ${counts.get(name) || 0}`;
      btn.addEventListener("click", () => {
        pulseScope = name;
        pulseHotAll = false;
        renderPulse();
      });
      box.appendChild(btn);
    }
  }

  function renderPulse() {
    renderPulseScopeChips();
    const count = document.querySelector("#pulse-count");
    const scopePapers = ThemeStats.byDirection(papers, pulseScope);
    const hot = ThemeStats.hotTags(papers, { direction: pulseScope });
    const trend = ThemeStats.trend(papers, { direction: pulseScope });
    if (count) {
      count.textContent = scopePapers.length
        ? `${scopePapers.length} 篇 · ${hot.length} 个主题`
        : "";
    }

    /* 当前热点 */
    const hotList = document.querySelector("#pulse-hot-list");
    const hotEmpty = document.querySelector("#pulse-hot-empty");
    const hotMore = document.querySelector("#pulse-hot-more");
    hotList.textContent = "";
    const shownHot = pulseHotAll ? hot : hot.slice(0, PULSE_HOT_LIMIT);
    const maxCount = hot.length ? hot[0].count : 0;
    for (const h of shownHot) {
      const row = el("button", "pulse-hot");
      row.type = "button";
      row.dataset.tag = h.tag;
      row.setAttribute("title", `筛选主题「${h.tag}」的收录论文`);
      const top = el("span", "pulse-hot__top");
      top.append(el("span", "pulse-hot__name", h.tag), el("span", "pulse-hot__meta", `${h.count} 篇 · ${Math.round(h.share * 100)}%`));
      const bar = el("span", "pulse-bar");
      const fill = el("span", "pulse-bar__fill");
      fill.style.width = maxCount ? `${Math.round((h.count / maxCount) * 100)}%` : "0%";
      bar.appendChild(fill);
      row.append(top, bar);
      row.addEventListener("click", () => selectFromPulse(h.tag));
      hotList.appendChild(row);
    }
    if (hotEmpty) hotEmpty.hidden = hot.length !== 0;
    if (hotMore) {
      hotMore.hidden = hot.length <= PULSE_HOT_LIMIT;
      hotMore.textContent = pulseHotAll ? "收起 ↑" : `显示全部 ${hot.length} 个主题 →`;
    }

    /* 收录趋势 */
    const trendList = document.querySelector("#pulse-trend-list");
    const trendEmpty = document.querySelector("#pulse-trend-empty");
    const trendHint = document.querySelector("#pulse-trend-hint");
    trendList.textContent = "";
    if (trendHint) {
      trendHint.textContent = trend.olderN
        ? `按发表时间：最新 ${trend.recentN} 篇 vs 此前 ${trend.olderN} 篇 · 占比变化`
        : `按发表时间：最新 ${trend.recentN} 篇 · 尚无更早发表可对比`;
    }
    const MIN_DELTA = 0.05; // 5 个百分点以上才算明显变化；「新进」需至少出现 2 次
    const upRows = trend.rows
      .filter((r) => r.state !== "falling" && r.delta >= MIN_DELTA && (r.state !== "new" || r.countR >= 2))
      .slice(0, 6);
    const downRows = trend.rows
      .filter((r) => r.state === "falling" && -r.delta >= MIN_DELTA)
      .sort((a, b) => a.delta - b.delta)
      .slice(0, 3);
    for (const r of [...upRows, ...downRows]) {
      const row = el("button", "pulse-trend" + (r.state === "rising" ? " is-up" : r.state === "falling" ? " is-down" : " is-new"));
      row.type = "button";
      row.dataset.tag = r.tag;
      row.setAttribute(
        "title",
        `${r.tag}：最新发表 ${trend.recentN} 篇出现 ${r.countR} 次 / 此前${trend.olderN ? ` ${trend.olderN} 篇出现 ${r.countO} 次` : "无更早发表"}`
      );
      row.append(
        el("span", "pulse-trend__glyph", r.state === "new" ? "新" : r.state === "rising" ? "↑" : "↓"),
        el("span", "pulse-trend__name", r.tag),
        el(
          "span",
          "pulse-trend__delta",
          r.state === "new" ? `${r.countR} 篇` : `${Math.abs(Math.round(r.delta * 100))}%`
        )
      );
      row.addEventListener("click", () => selectFromPulse(r.tag));
      trendList.appendChild(row);
    }
    if (trendEmpty) {
      trendEmpty.hidden = upRows.length + downRows.length !== 0;
      trendEmpty.textContent = scopePapers.length < 2
        ? "收录论文还太少，积累几轮更新后这里会自动出现趋势。"
        : !trend.olderN
          ? "尚无更早发表的论文可对比，下一轮更新后自动出现趋势。"
          : "近前两个窗口的主题占比没有明显变化。";
    }
  }

  /* ── 数据备份：导出 / 导入 ─────────────────────────────────────── */
  function bindBackup() {
    const exportBtn = document.querySelector("#backup-export");
    const importBtn = document.querySelector("#backup-import-btn");
    const fileInput = document.querySelector("#backup-file");
    const note = document.querySelector("#backup-note");
    if (!exportBtn || !importBtn || !fileInput || !note) return;

    exportBtn.addEventListener("click", () => {
      const data = store.exportData();
      data.app = "paperledger";
      data.version = 1;
      data.exportedAt = new Date().toISOString();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      const a = el("a");
      a.href = URL.createObjectURL(blob);
      a.download = `论文台账备份_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(a.href);
      note.textContent = "已导出备份文件。";
    });

    importBtn.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        try {
          const data = JSON.parse(reader.result);
          if (!Array.isArray(data.papers)) throw new Error("bad backup");
          const ok = window.confirm(
            `导入将用备份替换当前 ${papers.length} 条记录（共 ${data.papers.length} 条，含删除记录），是否继续？`
          );
          if (!ok) {
            note.textContent = "已取消导入。";
            e.target.value = "";
            return;
          }
          papers = store.importData(data);
          directionFilter = null;
          tagFilter = null;
          showAll = false;
          renderAll();
          note.textContent = `已导入 ${data.papers.length} 条记录。`;
        } catch (err) {
          note.textContent = "无法识别该备份文件，请选择本台账导出的 JSON。";
        }
        e.target.value = "";
      };
      reader.readAsText(file);
    });
  }

  /* ── filter ─────────────────────────────────────────────────────── */
  function setDirectionFilter(name) {
    directionFilter = name;
    showAll = false;
    renderAll();
  }

  function setTagFilter(tag) {
    tagFilter = tag || null;
    showAll = false;
    renderAll();
  }

  /* 从热点/趋势点选主题：限定标签；统计范围非「全部」时同时限定该方向 */
  function selectFromPulse(tag) {
    tagFilter = tag;
    if (pulseScope !== "全部") directionFilter = pulseScope;
    showAll = false;
    renderAll();
    document.querySelector("#latest").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  /* ── mutations ──────────────────────────────────────────────────── */
  let undoTimer = null;

  function removePaper(id) {
    const index = papers.findIndex((p) => p.id === id);
    const removed = index >= 0 ? papers[index] : null;
    papers = store.remove(id);
    if (directionFilter && !papers.some((p) => p.direction === directionFilter)) directionFilter = null;
    if (tagFilter && !papers.some((p) => (p.tags || []).includes(tagFilter))) tagFilter = null;
    renderAll();
    if (removed) showUndoToast(removed, index);
  }

  function showUndoToast(entry, index) {
    const toast = document.querySelector("#undo-toast");
    if (!toast) return;
    const title = entry.title.length > 26 ? entry.title.slice(0, 26) + "…" : entry.title;
    toast.querySelector(".toast__label").textContent = `已移除「${title}」`;
    const undoBtn = toast.querySelector(".toast__undo");
    undoBtn.onclick = () => {
      papers = store.restore(entry, index);
      if (directionFilter && !papers.some((p) => p.direction === directionFilter)) directionFilter = null;
      if (tagFilter && !papers.some((p) => (p.tags || []).includes(tagFilter))) tagFilter = null;
      renderAll();
      hideUndoToast();
    };
    toast.hidden = false;
    requestAnimationFrame(() => toast.classList.add("is-visible"));
    clearTimeout(undoTimer);
    undoTimer = setTimeout(hideUndoToast, 8000);
  }

  function hideUndoToast() {
    const toast = document.querySelector("#undo-toast");
    if (!toast) return;
    toast.classList.remove("is-visible");
    clearTimeout(undoTimer);
    setTimeout(() => {
      if (!toast.classList.contains("is-visible")) toast.hidden = true;
    }, 200);
  }

  function addEntry(entry) {
    papers = store.add(entry);
    /* 新文章强制置顶：清除方向筛选，确保它在收录列表最上面可见 */
    directionFilter = null;
    tagFilter = null;
    showAll = false;
    renderAll();
  }

  /* ── form ───────────────────────────────────────────────────────── */
  const form = document.querySelector("#paper-form");
  const submitBtn = document.querySelector("#f-submit");

  const rules = {
    "f-title": {
      validate: (v) => v.trim().length >= 2,
      error: "缺少论文标题。填上正式标题后再录入。",
    },
    "f-journal": {
      validate: (v) => v.trim().length >= 1,
      error: "缺少期刊或会议名称。填上出处后再录入。",
    },
    "f-year": {
      validate: (v) => /^\d{4}$/.test(v.trim()),
      error: "年份应为四位数字，如 2017。",
    },
    "f-summary": {
      validate: (v) => v.trim().length >= 5,
      error: "一句话概括太短。写清提出什么、解决什么问题。",
    },
    "f-question": {
      validate: (v) => v.trim().length >= 5,
      error: "问题与动机太短。写明现有方法的痛点与重要性。",
    },
    "f-method": {
      validate: (v) => v.trim().length >= 5,
      error: "方法太短。写上核心思想与关键机制。",
    },
    "f-doi": {
      validate: (v) => v.trim() === "" || /^10\.\d{4,9}\/\S+$/i.test(v.trim()),
      error: "DOI 格式不正确，形如 10.xxxx/xxxxx。",
    },
    "f-arxiv": {
      validate: (v) => v.trim() === "" || /^\d{4}\.\d{4,5}(v\d+)?$/i.test(v.trim()),
      error: "arXiv ID 格式不正确，形如 2305.10601。",
    },
    "f-pdf": {
      validate: (v) => v.trim() === "" || /^https?:\/\/\S+$/i.test(v.trim()),
      error: "PDF 链接格式不正确。以 https:// 开头。",
    },
  };

  const touched = new Set();

  function fieldState(id) {
    const input = document.getElementById(id);
    const field = input.closest(".field");
    const helper = document.getElementById(id + "-help");
    return { input, field, helper };
  }

  function validateField(id) {
    const { input, field, helper } = fieldState(id);
    const rule = rules[id];
    const ok = rule.validate(input.value);
    field.classList.toggle("is-error", !ok);
    input.setAttribute("aria-invalid", String(!ok));
    if (ok) {
      helper.textContent = helper.dataset.default || "";
    } else {
      if (!helper.dataset.default) helper.dataset.default = helper.textContent;
      helper.textContent = rule.error;
    }
    return ok;
  }

  function bindValidation() {
    for (const id of Object.keys(rules)) {
      const { input } = fieldState(id);
      input.addEventListener("blur", () => {
        touched.add(id);
        validateField(id);
      });
      input.addEventListener("input", () => {
        if (touched.has(id)) validateField(id);
      });
    }
  }

  function validateAll() {
    let allOk = true;
    for (const id of Object.keys(rules)) {
      touched.add(id);
      if (!validateField(id)) allOk = false;
    }
    return allOk;
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!validateAll()) {
      const firstError = form.querySelector(".field.is-error .field__input");
      if (firstError) firstError.focus();
      return;
    }

    submitBtn.dataset.state = "loading";
    submitBtn.disabled = true;

    window.setTimeout(() => {
      const entry = {
        id: "p-" + Date.now().toString(36),
        title: fieldState("f-title").input.value.trim(),
        authors: fieldState("f-authors").input.value.trim(),
        journal: fieldState("f-journal").input.value.trim(),
        year: fieldState("f-year").input.value.trim(),
        doi: fieldState("f-doi").input.value.trim(),
        arxiv: fieldState("f-arxiv").input.value.trim(),
        pdf: fieldState("f-pdf").input.value.trim(),
        link: "",
        direction: fieldState("f-direction").input.value.trim(),
        tags: ThemeStats.splitTags(fieldState("f-tags").input.value),
        summary: fieldState("f-summary").input.value.trim(),
        question: fieldState("f-question").input.value.trim(),
        method: fieldState("f-method").input.value.trim(),
        experiments: fieldState("f-experiments").input.value.trim(),
        contribution: fieldState("f-contribution").input.value.trim(),
        sample: false,
      };

      addEntry(entry);
      form.reset();
      touched.clear();
      for (const id of Object.keys(rules)) {
        const { field, helper } = fieldState(id);
        field.classList.remove("is-error");
        if (helper.dataset.default) helper.textContent = helper.dataset.default;
      }

      submitBtn.dataset.state = "success";
      submitBtn.disabled = false;
      window.setTimeout(() => {
        submitBtn.dataset.state = "default";
        fieldState("f-title").input.focus();
      }, 1100);
    }, 350);
  });

  /* ── import: parse six-part summary (paper-summarize-fetch output) ─ */
  const importText = document.querySelector("#import-text");
  const importHelp = document.querySelector("#import-help");
  const importPreview = document.querySelector("#import-preview");
  const importFields = document.querySelector("#import-fields");
  const importDirection = document.querySelector("#import-direction");
  const importTags = document.querySelector("#import-tags");
  const importParseBtn = document.querySelector("#import-parse");
  const importConfirmBtn = document.querySelector("#import-confirm");
  let parsedEntry = null;

  function showImportPreview(entry) {
    importFields.textContent = "";
    const rows = [
      ["标题", entry.title],
      ["作者", entry.authors],
      ["期刊 / 会议", entry.journal + (entry.year ? " · " + entry.year : "")],
      ["DOI", entry.doi],
      ["arXiv", entry.arxiv],
      ["PDF", entry.pdf],
      ["主题", (entry.tags || []).join("；")],
      ["一句话概括", entry.summary],
      ["问题与动机", entry.question],
      ["方法", entry.method],
      ["实验与结果", entry.experiments],
      ["贡献与局限", entry.contribution],
    ];
    for (const [label, value] of rows) {
      const row = el("div");
      const dt = el("dt", "", label);
      const dd = el("dd", value ? "" : "is-empty", value || "—");
      row.append(dt, dd);
      importFields.appendChild(row);
    }
    importPreview.hidden = false;
    importParseBtn.dataset.state = "success";
    importParseBtn.querySelector(".btn__label").textContent = "已解析";
    window.setTimeout(() => {
      importParseBtn.dataset.state = "default";
      importParseBtn.querySelector(".btn__label").textContent = "解析";
    }, 1500);
  }

  importParseBtn.addEventListener("click", () => {
    const md = importText.value;
    if (!md.trim()) {
      importHelp.textContent = "先把 skill 生成的总结内容粘贴到上方文本框。";
      importHelp.classList.add("field__helper--error");
      return;
    }
    importHelp.textContent = importHelp.dataset.default || importHelp.textContent;
    importHelp.classList.remove("field__helper--error");
    parsedEntry = Parser.parseSummary(md);
    if (!parsedEntry.title) {
      importHelp.textContent = "没解析到「基本信息」里的标题。请确认粘贴的是六段式总结（含 ## 基本信息 等标题行）。";
      importHelp.classList.add("field__helper--error");
      return;
    }
    importDirection.value = parsedEntry.direction || "";
    if (importTags) importTags.value = (parsedEntry.tags || []).join("；");
    showImportPreview(parsedEntry);
  });

  importConfirmBtn.addEventListener("click", () => {
    if (!parsedEntry) return;
    parsedEntry.direction = importDirection.value.trim();
    parsedEntry.tags = ThemeStats.splitTags(importTags.value);
    importConfirmBtn.dataset.state = "loading";
    importConfirmBtn.disabled = true;
    window.setTimeout(() => {
      addEntry({ ...parsedEntry, id: "i-" + Date.now().toString(36) });
      importConfirmBtn.dataset.state = "success";
      importConfirmBtn.disabled = false;
      window.setTimeout(() => {
        importConfirmBtn.dataset.state = "default";
      }, 1100);
      importText.value = "";
      importPreview.hidden = true;
      parsedEntry = null;
      importDirection.value = "";
      if (importTags) importTags.value = "";
      document.querySelector("#latest").scrollIntoView({ behavior: "smooth", block: "start" });
    }, 350);
  });

  /* ── latest rail expand ─────────────────────────────────────────── */
  document.querySelector("#latest-more").addEventListener("click", () => {
    showAll = !showAll;
    renderLatest();
  });
  const pulseHotMore = document.querySelector("#pulse-hot-more");
  if (pulseHotMore) {
    pulseHotMore.addEventListener("click", () => {
      pulseHotAll = !pulseHotAll;
      renderPulse();
    });
  }

  /* ── boot ───────────────────────────────────────────────────────── */
  function renderAll() {
    renderStats();
    renderFilterChips();
    renderQuestions();
    renderLatest();
    renderPulse();
  }

  bindValidation();
  bindBackup();
  renderAll();
})();
