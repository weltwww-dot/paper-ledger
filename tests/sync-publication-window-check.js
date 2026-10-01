'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process');
const root=fs.mkdtempSync(path.join(os.tmpdir(),'paper-window-test-'));
try {
  for(const d of ['scripts','shared','data','summaries'])fs.mkdirSync(path.join(root,d));
  for(const f of ['scripts/sync-papers.js','shared/paper-parser.js','shared/publication-window.js'])fs.copyFileSync(path.join(__dirname,'..',f),path.join(root,f));
  fs.writeFileSync(path.join(root,'index.html'),'<script src="data/papers.js"></script><script src="shared/ledger-store.js?v=old"></script><script src="app.js?v=old"></script>');
  const recent={id:'r-new',title:'Recent paper',doi:'10.1000/recent',published:'2026-07-01'};
  const old={id:'r-old',title:'Old paper',doi:'10.1000/old',published:'2026-06-30'};
  const held={id:'r-held',title:'Unverified date',doi:'10.1000/held',published:'2026-09-01'};
  fs.writeFileSync(path.join(root,'data/papers.js'),'window.PAPERLEDGER_SEED = '+JSON.stringify([old,recent,held])+';');
  fs.mkdirSync(path.join(root,'summaries/date-unverified'));
  fs.writeFileSync(path.join(root,'summaries/date-unverified/held.md'),'## 基本信息\n- **标题**: Unverified date\n- **DOI**: 10.1000/held\n- **发表**: 2026-09-01\n');
  fs.writeFileSync(path.join(root,'data/theme-tags.json'),JSON.stringify({'10.1000/recent':['机器学习方法'],'10.1000/old':['机器学习方法']}));
  fs.writeFileSync(path.join(root,'data/retired-papers.json'),JSON.stringify({retired:[{doi:'10.1000/retired',online_date:'2026-06-29'}]}));
  for(const [slug,title,doi,date]of [['new','Recent paper','recent','2026-07-01'],['old','Old paper','old','2026-06-30'],['retired','Bad restored date','retired','2026-09-30']]){
    fs.writeFileSync(path.join(root,'summaries',slug+'.md'),`## 基本信息\n- **标题**: ${title}\n- **DOI**: 10.1000/${doi}\n- **发表**: ${date}\n`);
  }
  // Missing window filtering or tombstone checks makes expired/restored entries reappear.
  cp.execFileSync(process.execPath,[path.join(root,'scripts/sync-papers.js'),'--as-of','2026-10-01']);
  const read=()=>{const s=fs.readFileSync(path.join(root,'data/papers.js'),'utf8');return JSON.parse(s.slice(s.indexOf('['),s.lastIndexOf(']')+1));};
  assert.deepEqual(read().map(p=>p.doi),['10.1000/recent']);
  assert.equal(read()[0].id,'r-new');
  assert.doesNotMatch(fs.readFileSync(path.join(root,'index.html'),'utf8'),/\?v=old/);
  cp.execFileSync(process.execPath,[path.join(root,'scripts/sync-papers.js'),'--as-of','2026-10-01']);
  assert.deepEqual(read().map(p=>p.doi),['10.1000/recent']);
  console.log('PASS: sync does not restore expired or retired papers; recent IDs stay stable.');
} finally {fs.rmSync(root,{recursive:true,force:true});}
