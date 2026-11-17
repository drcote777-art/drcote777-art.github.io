const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const SP='/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/';
const REPO='/home/claude/drcote777-art.github.io';
exports.open=async(opt={})=>{const three=fs.readFileSync('/root/cruise/node_modules/three/build/three.min.js','utf8');
 const html=fs.readFileSync(REPO+'/dist-seoul/index.html','utf8');let pm={};try{pm=JSON.parse(fs.readFileSync(SP+'ph/local.json','utf8'));}catch(e){}
 for(const extra of (opt.pm||[])){try{Object.assign(pm,JSON.parse(fs.readFileSync(SP+extra,'utf8')));}catch(e){}}
 const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const ctx=await b.newContext({viewport:{width:opt.w||405,height:opt.h||720},deviceScaleFactor:opt.dsf||1,locale:opt.locale||'en-US',timezoneId:'Asia/Seoul'});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e)));
 await p.route('**/*',r=>{const u=r.request().url();
  if(u.includes('three.min.js'))return r.fulfill({body:three,contentType:'application/javascript'});
  if(u.includes('upload.wikimedia.org')){const k=decodeURIComponent(u.split('/').slice(-2,-1)[0]);const f=pm[k];if(f&&fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:'image/jpeg',headers:{'access-control-allow-origin':'*'}});return r.abort();}
  if(u.startsWith('http://site.test/')){const pa=new URL(u).pathname;if(pa==='/'||pa==='/index.html')return r.fulfill({body:html,contentType:'text/html; charset=utf-8'});const f=REPO+'/dist-seoul'+pa;if(fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.js')?'application/javascript':f.endsWith('.png')?'image/png':f.endsWith('.jpg')?'image/jpeg':f.endsWith('.webmanifest')?'application/manifest+json':'model/gltf-binary'});return r.fulfill({status:404,body:''});}
  if(u.startsWith('https://fonts.googleapis.com')||u.startsWith('https://fonts.gstatic.com'))return r.continue().catch(()=>{});
  return r.abort();});
 if(opt.clock)await p.clock.install({time:opt.time||new Date('2026-11-12T10:00:00+09:00')});
 if(opt.raf)await p.addInitScript(()=>{window.__rafQ=[];window.requestAnimationFrame=cb=>{window.__rafQ.push(cb);return window.__rafQ.length;};window.cancelAnimationFrame=()=>{};window.__step=()=>{const q=window.__rafQ;window.__rafQ=[];const t=performance.now();for(const cb of q){try{cb(t);}catch(e){console.error(e);}}return q.length;};});
 await p.goto('http://site.test/'+(opt.q||''));
 return {b,ctx,p,errs};};
exports.tick=async(p,ms,step=1000/24)=>{for(let t=0;t<ms;t+=step){await p.clock.runFor(step);await p.evaluate(()=>window.__step&&window.__step());}};
