"use strict";
const assert = require('node:assert/strict');
const Window = require('../shared/publication-window.js');
// Catches inclusive boundary errors, invalid calendar dates, and guessing a day from a year.
for (const [value, expected] of [
  ['2026-07-01', 'recent'], ['2026-06-30', 'expired'], ['2026-10-01', 'recent'],
  ['2026-10-02', 'future'], ['2026年7月1日', 'recent'],
  ['2026-07-01（在线发表）', 'recent'], ['2026-02-30', 'unknown'],
  ['2026-07', 'recent'], ['2026-06', 'expired'], ['2026-10', 'recent'], ['2025', 'expired'],
  ['2026', 'unknown'], ['', 'unknown'], ['日期未知', 'unknown'],
]) assert.equal(Window.classify(value, '2026-10-01'), expected, value);
assert.equal(Window.windowStart('2026-10-18'), '2026-07-01');
assert.equal(Window.classify('2026-07-01', '2026-10-18'), 'recent');
assert.equal(Window.classify('2026-07', '2026-10-18'), 'recent');
assert.equal(Window.classify('2026-10', '2026-10-18'), 'recent');
assert.equal(Window.classify('2026-11', '2026-10-18'), 'future');
assert.equal(Window.windowStart('2026-05-31'), '2026-02-01');
assert.equal(Window.windowStart('2024-05-31'), '2024-02-01');
assert.equal(Window.windowStart('2026-01-18'), '2025-10-01');
assert.throws(()=>Window.windowStart('2026-2-03'), /YYYY-MM-DD/);
assert.throws(()=>Window.windowStart('2026年10月1日'), /YYYY-MM-DD/);
const rows = [{id:'old',published:'2026-06-30'}, {id:'ok',published:'2026-07-01'}, {id:'unknown',published:'2026'}];
assert.deepEqual(Window.filterRecent(rows, '2026-10-01').map(p=>p.id), ['ok']);
assert.equal(rows.length, 3);
// A restored stale seed or import must not bypass the rolling window.
const Store = require('../shared/ledger-store.js');
const memory = new Map([['papers',JSON.stringify([
  {id:'r-old',title:'Retired built-in',published:'2026-06-30'},
  {id:'p-user',title:'User paper',published:'2026-09-01'},
])]]);
const storage = {getItem:k=>memory.get(k)||null, setItem:(k,v)=>memory.set(k,v)};
const store = Store.create({seed:[{id:'r-new',title:'New paper',published:'2026-10-01'}],storageKey:'papers',deletedKey:'deleted',storage,asOf:'2026-10-01'});
assert.deepEqual(store.list().map(p=>p.id), ['p-user','r-new']);
assert.deepEqual(JSON.parse(memory.get('papers')).map(p=>p.id), ['p-user','r-new']);
store.importData({papers:[{id:'r-old',published:'2026-06-30'},{id:'p-ok',published:'2026-09-29'}]});
assert.deepEqual(store.list().map(p=>p.id), ['p-ok']);
store.add({id:'p-outside',published:'2026-06-01'});
assert.deepEqual(store.list().map(p=>p.id), ['p-ok']);
// Old backup issue dates must not resurrect a built-in removed from the current seed.
store.importData({papers:[{id:'r-removed',published:'2026-09-01'}, {id:'r-new',published:'2026-08-01'}]});
assert.deepEqual(store.list().map(p=>[p.id,p.published]), [['r-new','2026-10-01']]);
store.restore({id:'r-removed',published:'2026-09-01'},0);
assert.deepEqual(store.list().map(p=>p.id), ['r-new']);
const movingOptions = {seed:[{id:'r-boundary',published:'2026-07-01'}],storageKey:'moving',deletedKey:'moving-deleted',storage,asOf:'2026-10-01'};
const moving = Store.create(movingOptions);
movingOptions.asOf='2026-10-02';
assert.deepEqual(moving.exportData().papers.map(p=>p.id), ['r-boundary']);
movingOptions.asOf='2026-11-01';
assert.deepEqual(moving.exportData().papers, []);
assert.deepEqual(JSON.parse(memory.get('moving')), []);
console.log('PASS: rolling publication window, calendar boundaries, stale cache and imports.');
const Stats = require('../shared/theme-stats.js');
const monthRows = [{id:'jul',published:'2026-07',direction:'人工智能',tags:['机器学习方法']},{id:'oct',published:'2026-10',direction:'人工智能',tags:['机器学习方法']},{id:'sep',published:'2026-09-20',direction:'人工智能',tags:['机器学习方法']},{id:'jun',published:'2026-06',direction:'人工智能',tags:['机器学习方法']}];
assert.deepEqual(Stats.filterScope(monthRows,{since:'2026-07-01'}).map(p=>p.id), ['jul','oct','sep']);
assert.equal(Stats.scopeCounts(monthRows,['人工智能'],'2026-07-01').get('人工智能'),3);
assert.deepEqual(Stats.sortByPublished(monthRows).map(p=>p.id), ['oct','sep','jul','jun']);
