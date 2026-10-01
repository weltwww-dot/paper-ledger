/* One rolling three-calendar-month policy for sync, browser caches and validation. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.PublicationWindow = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';
  function today() {
    return new Intl.DateTimeFormat('sv-SE', {timeZone:'Asia/Shanghai',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  }
  function day(y, m, d) {
    const v = new Date(Date.UTC(y, m - 1, d));
    return v.getUTCFullYear() === y && v.getUTCMonth() === m - 1 && v.getUTCDate() === d ? v.toISOString().slice(0,10) : null;
  }
  function interval(value) {
    const text = String(value || '').trim();
    let m = text.match(/^(\d{4})-(\d{1,2})-(\d{1,2})(?:$|[\s（(])/)
      || text.match(/^(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日/);
    if (m) { const v = day(+m[1],+m[2],+m[3]); return v ? {first:v,last:v} : null; }
    m = text.match(/^(\d{4})-(\d{2})$/);
    if (m) {
      const first = day(+m[1],+m[2],1);
      if (!first) return null;
      const lastDay = new Date(Date.UTC(+m[1],+m[2],0)).getUTCDate();
      return {first,last:day(+m[1],+m[2],lastDay)};
    }
    m = text.match(/^(\d{4})(?:年)?$/);
    return m ? {first:m[1]+'-01-01',last:m[1]+'-12-31'} : null;
  }
  function windowStart(asOf) {
    const date = asOf || today();
    const v = interval(date);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !v || v.first !== v.last) throw new Error('asOf must be a valid YYYY-MM-DD date');
    const [y,m,d] = date.split('-').map(Number);
    const first = new Date(Date.UTC(y,m-4,1));
    const lastDay = new Date(Date.UTC(first.getUTCFullYear(),first.getUTCMonth()+1,0)).getUTCDate();
    return day(first.getUTCFullYear(),first.getUTCMonth()+1,Math.min(d,lastDay));
  }
  function classify(value, asOf) {
    const now = asOf || today(), start = windowStart(now), span = interval(value);
    if (!span) return 'unknown';
    if (span.last < start) return 'expired';
    if (span.first > now) return 'future';
    if (span.first >= start && span.last <= now) return 'recent';
    return 'unknown';
  }
  function filterRecent(papers, asOf) {
    const now = asOf || today();
    return papers.filter(p => classify(p.published,now) === 'recent');
  }
  return {today,windowStart,classify,filterRecent};
});
