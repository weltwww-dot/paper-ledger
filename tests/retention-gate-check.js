'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process');
const root=fs.mkdtempSync(path.join(os.tmpdir(),'paper-window-gate-'));
try {
  const target=path.join(root,'papers.js');
  const run=entries=>{
    fs.writeFileSync(target,'window.PAPERLEDGER_SEED = '+JSON.stringify(entries)+';');
    return cp.spawnSync(process.execPath,[path.join(__dirname,'../scripts/retention-check.js'),'--data',target,'--as-of','2026-10-01'],{encoding:'utf8'});
  };
  assert.equal(run([{doi:'10.1/within',published:'2026-07-01'}]).status,0);
  for(const date of ['2026-06-30','2026-10-02','2026','bad-date']) {
    const result=run([{doi:'10.1/invalid',published:date}]);
    assert.equal(result.status,1,date);
    assert.match(result.stdout+' '+result.stderr,/10\.1\/invalid/);
  }
  console.log('PASS: retention gate rejects old, future and unverified dates.');
} finally {fs.rmSync(root,{recursive:true,force:true});}
