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
  let filter = null; // direction name or null
  let showAll = false;

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
    if (!filter) return papers;
    return papers.filter((p) => p.direction === filter);
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
      line.textContent = papers.length === 0 ? "尚无论文收录。" : "该方向下暂无收录论文。";
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
  }

  function filterChip(label, value, count) {
    const btn = el("button", "chip" + (filter === value ? " is-active" : ""));
    btn.type = "button";
    btn.setAttribute("aria-pressed", String(filter === value));
    btn.textContent = `${label} ${count}`;
    btn.addEventListener("click", () => setFilter(value));
    return btn;
  }

  function paperCell(p) {
    const cell = el("details", "paper");
    cell.dataset.id = p.id;

    const summary = el("summary", "paper__summary");
    const metaRow = el("div", "paper__meta-row");
    if (p.direction) metaRow.appendChild(el("span", "tag", p.direction));
    metaRow.appendChild(el("span", "tag", p.journal + " · " + p.year));
    if (p.sample) metaRow.appendChild(el("span", "tag tag--sample tag--accent", "示例"));

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
    const removeBtn = el("button", "paper__remove", p.sample ? "移除示例" : "移除");
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

  /* ── render: directions ─────────────────────────────────────────── */
  function renderDirections() {
    const list = document.querySelector("#directions-list");
    const empty = document.querySelector("#directions-empty");
    const count = document.querySelector("#directions-count");
    const directions = uniqueDirections();

    list.textContent = "";
    const all = el("button", "direction" + (filter === null ? " is-active" : ""));
    all.type = "button";
    all.setAttribute("aria-pressed", String(filter === null));
    all.appendChild(el("span", "direction__name", "全部"));
    all.appendChild(el("span", "direction__count", String(papers.length)));
    all.addEventListener("click", () => setFilter(null));
    list.appendChild(all);

    for (const [name, n] of directions) {
      const btn = el("button", "direction" + (filter === name ? " is-active" : ""));
      btn.type = "button";
      btn.dataset.direction = name;
      btn.setAttribute("aria-pressed", String(filter === name));
      btn.appendChild(el("span", "direction__name", name));
      btn.appendChild(el("span", "direction__count", String(n)));
      btn.addEventListener("click", () => setFilter(name));
      list.appendChild(btn);
    }

    empty.hidden = directions.length !== 0;
    count.textContent = directions.length ? `${directions.length} 个方向` : "";
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
    row.appendChild(el("p", "qrow__question", p.question));

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

  /* ── filter ─────────────────────────────────────────────────────── */
  function setFilter(name) {
    filter = name;
    showAll = false;
    renderAll();
  }

  /* ── mutations ──────────────────────────────────────────────────── */
  function removePaper(id) {
    papers = store.remove(id);
    if (filter && !papers.some((p) => p.direction === filter)) filter = null;
    renderAll();
  }

  function addEntry(entry) {
    papers = store.add(entry);
    /* 新文章强制置顶：清除方向筛选，确保它在收录列表最上面可见 */
    filter = null;
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
    showImportPreview(parsedEntry);
  });

  importConfirmBtn.addEventListener("click", () => {
    if (!parsedEntry) return;
    parsedEntry.direction = importDirection.value.trim();
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
      document.querySelector("#latest").scrollIntoView({ behavior: "smooth", block: "start" });
    }, 350);
  });

  /* ── latest rail expand ─────────────────────────────────────────── */
  document.querySelector("#latest-more").addEventListener("click", () => {
    showAll = !showAll;
    renderLatest();
  });

  /* ── date ───────────────────────────────────────────────────────── */
  function stampDate() {
    const node = document.querySelector("#band-date");
    if (!node) return;
    try {
      node.textContent = new Intl.DateTimeFormat("zh-CN", {
        year: "numeric",
        month: "long",
      }).format(new Date());
    } catch (err) {
      /* keep static text */
    }
  }

  /* ── boot ───────────────────────────────────────────────────────── */
  function renderAll() {
    renderStats();
    renderFilterChips();
    renderDirections();
    renderQuestions();
    renderLatest();
  }

  bindValidation();
  stampDate();
  renderAll();
})();
