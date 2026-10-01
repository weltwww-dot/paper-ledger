'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path'), os = require('node:os');
const {spawnSync} = require('node:child_process');
const root = fs.mkdtempSync(path.join(os.tmpdir(),'ledger-retired-import-'));
try {
  for(const dir of ['scripts','data','summaries','skill-runs'])fs.mkdirSync(path.join(root,dir));
  fs.copyFileSync(path.join(__dirname,'../scripts/import_incremental.js'),path.join(root,'scripts/import_incremental.js'));
  fs.writeFileSync(path.join(root,'data/papers.js'),'window.PAPERLEDGER_SEED = [];');
  fs.writeFileSync(path.join(root,'data/retired-papers.json'),JSON.stringify({retired:[{doi:'10.1000/old'}]}));
  for(const name of ['oa_inc.json','content_inc.json'])fs.writeFileSync(path.join(root,'skill-runs',name),'[]');
  fs.writeFileSync(path.join(root,'skill-runs/records_inc.json'),JSON.stringify([{doi:'10.1000/old',title:'Expired paper',date:'2026-09-01',source:'Test Journal'}]));
  const result = spawnSync(process.execPath,[path.join(root,'scripts/import_incremental.js')],{encoding:'utf8'});
  assert.equal(result.status,0,result.stderr);
  assert.deepEqual(fs.readdirSync(path.join(root,'summaries')),[],'A stale cached batch must not recreate retired content');
  console.log('PASS: incremental registration cannot recreate retired summaries.');
} finally {fs.rmSync(root,{recursive:true,force:true});}
