#!/usr/bin/env node
'use strict';
const fs=require('node:fs'),path=require('node:path');
const Window=require('../shared/publication-window.js');
const arg=(flag,fallback)=>process.argv.includes(flag)?process.argv[process.argv.indexOf(flag)+1]:fallback;
const target=arg('--data',path.join(__dirname,'../data/papers.js'));
const asOf=arg('--as-of',Window.today());
const source=fs.readFileSync(target,'utf8');
const match=source.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
if(!match)throw new Error('Cannot parse ledger');
const papers=JSON.parse(match[1]);
const invalid=papers.filter(p=>Window.classify(p.published,asOf)!=='recent');
if(invalid.length){
  console.error(`FAIL: ${invalid.length} papers outside verified three-month window`);
  for(const p of invalid.slice(0,20))console.error(`${p.doi}: ${p.published} (${Window.classify(p.published,asOf)})`);
  process.exitCode=1;
} else console.log(`PASS: ${papers.length} papers in ${Window.windowStart(asOf)}–${asOf}.`);
