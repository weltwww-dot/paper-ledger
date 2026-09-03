/*
 * 台账存储引擎（浏览器端）
 * 小接口：list() / add(entry) / remove(id)
 * 实现隐藏：schema 迁移、内置(seed)与用户数据合并、删除记忆、持久化。
 * 调用方不需要知道任何升级分支；内部规则修一处、处处生效。
 *
 * 用法（浏览器）:
 *   const store = LedgerStore.create({
 *     seed: window.PAPERLEDGER_SEED || [],
 *     storageKey: "paperledger.v1",
 *     deletedKey: "paperledger.deleted.v1",
 *     storage: window.localStorage,
 *   });
 *   let papers = store.list();
 *   papers = store.add(entry);    // 置顶 + 持久化
 *   papers = store.remove(id);    // 内置条目记入删除记忆
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.LedgerStore = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  /* 旧版/不完整条目 → 统一数据模型 */
  function normalize(p) {
    return {
      id: p.id,
      title: p.title || "",
      authors: p.authors || "",
      journal: p.journal || "",
      year: p.year || "",
      published: p.published || "",
      doi: p.doi || "",
      arxiv: p.arxiv || "",
      pdf: p.pdf || "",
      link: p.link || "",
      direction: p.direction || "",
      summary: p.summary || p.intro || "",
      question: p.question || "",
      method: p.method || "",
      experiments: p.experiments || "",
      contribution: p.contribution || "",
      tags: Array.isArray(p.tags) ? p.tags.map((t) => String(t).trim()).filter(Boolean) : [],
      sample: !!p.sample,
    };
  }

  function createLedgerStore(options) {
    const seed = (options.seed || []).map((p) => ({ ...p }));
    const storageKey = options.storageKey;
    const deletedKey = options.deletedKey;
    const storage = options.storage;

    function readStorage(key) {
      try {
        return storage.getItem(key);
      } catch (err) {
        return null;
      }
    }

    function writeStorage(key, value) {
      try {
        storage.setItem(key, value);
      } catch (err) {
        /* private mode or quota — keep working in memory */
      }
    }

    function getDeletedIds() {
      const raw = readStorage(deletedKey);
      if (!raw) return [];
      try {
        return JSON.parse(raw) || [];
      } catch (err) {
        return [];
      }
    }

    function persist(papersList) {
      writeStorage(storageKey, JSON.stringify(papersList));
    }

    /* 加载 + 迁移 + 合并：
       - 无数据 → seed
       - 仅内置数据（旧 seed/示例）→ 用最新 seed 全量升级（跳过已删除）
       - 含用户条目 → 用户条目保留；保留的内置条目用 seed 最新版刷新
         （方向等字段随数据文件更新）；用户删除过的内置条目不恢复；新增内置补上 */
    function load() {
      const raw = readStorage(storageKey);
      if (raw) {
        try {
          const parsed = JSON.parse(raw);
          if (Array.isArray(parsed)) {
            const deleted = getDeletedIds();
            const hasUserData = parsed.some((p) => /^(p-|i-)/.test(p.id || ""));
            if (hasUserData) {
              const userEntries = parsed
                .filter((p) => /^(p-|i-)/.test(p.id || ""))
                .map(normalize)
                .filter((p) => !p.sample);
              const seedById = new Map(seed.map((s) => [s.id, s]));
              const keptBuiltin = parsed
                .filter((p) => /^r-/.test(p.id || ""))
                .map(normalize)
                .filter((p) => !p.sample);
              const merged = [...userEntries];
              for (const k of keptBuiltin) {
                merged.push(seedById.has(k.id) ? { ...seedById.get(k.id) } : k);
              }
              const known = new Set(merged.map((p) => p.id));
              for (const s of seed) {
                if (!known.has(s.id) && !deleted.includes(s.id)) merged.push({ ...s });
              }
              persist(merged);
              return merged;
            }
            const available = seed.filter((s) => !deleted.includes(s.id)).map((p) => ({ ...p }));
            persist(available);
            return available;
          }
        } catch (err) {
          /* corrupt storage — fall through to seed */
        }
      }
      return seed.map((p) => ({ ...p }));
    }

    let papers = load();

    return {
      list() {
        return papers;
      },
      add(entry) {
        papers = [normalize(entry), ...papers];
        persist(papers);
        return papers;
      },
      remove(id) {
        papers = papers.filter((p) => p.id !== id);
        if (/^r-/.test(id || "")) {
          const deleted = getDeletedIds();
          if (!deleted.includes(id)) {
            deleted.push(id);
            writeStorage(deletedKey, JSON.stringify(deleted));
          }
        }
        persist(papers);
        return papers;
      },
      /* 撤销删除：插回原位置；内置条目同时移出删除记忆 */
      restore(entry, index) {
        const normalized = normalize(entry);
        const idx = Math.max(0, Math.min(index == null ? papers.length : index, papers.length));
        papers.splice(idx, 0, normalized);
        if (/^r-/.test(normalized.id || "")) {
          const deleted = getDeletedIds().filter((d) => d !== normalized.id);
          writeStorage(deletedKey, JSON.stringify(deleted));
        }
        persist(papers);
        return papers;
      },
      /* 备份：导出全部论文与删除记忆 */
      exportData() {
        return {
          papers: papers.map((p) => ({ ...p })),
          deleted: getDeletedIds(),
        };
      },
      /* 备份：整体替换（导入前由调用方确认覆盖） */
      importData(data) {
        papers = (data.papers || []).map(normalize).filter((p) => !p.sample);
        writeStorage(deletedKey, JSON.stringify(data.deleted || []));
        persist(papers);
        return papers;
      },
    };
  }

  return { create: createLedgerStore };
});
