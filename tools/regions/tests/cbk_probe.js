// 가상 충북: 장면별 화면·스팟 확인
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/',REPO='/home/claude/drcote777-art.github.io',D=S+'doc/cb/';
const three=fs.readFileSync('/root/cruise/node_modules/three/build/three.min.js','utf8');
const LOC=process.env.LOC||'en-US',SHOTS=JSON.parse(process.env.SHOTS||'null');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,locale:LOC,timezoneId:'Asia/Seoul'});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e.stack||e).slice(0,400)));
 await p.route('**/*',r=>{const u=r.request().url();if(u.includes('three.min.js'))return r.fulfill({body:three,contentType:'application/javascript'});
  if(u.startsWith('http://site.test/')){let pa=new URL(u).pathname;let f=pa==='/cbk.html'?S+'cbk.html':REPO+'/dist-seoul'+pa;
   if(fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.js')?'application/javascript':'application/octet-stream'});return r.fulfill({status:404,body:''});}
  return r.abort();});
 await p.goto('http://site.test/cbk.html');await p.waitForSelector('#enter:not([disabled])',{timeout:30000});await p.click('#enter');await p.waitForTimeout(2500);
 const ev=(f,a)=>p.evaluate(f,a);
 const closeAll=()=>ev(()=>{const pn=document.getElementById('pan');if(!pn.hidden){const c=pn.querySelector('[data-close]');if(c)c.click();}if(!document.getElementById('talk').hidden)document.getElementById('talkX').click();});
 const shots=SHOTS||[['sst',.8],['dyt',.02],['dyt',.3],['dyt',.5],['dyt',.8],['dds',.2],['dds',.45],['mch',.1],['mch',.35],['ulj',.1],['ulj',.5],['cpc',.1],['cpc',.35],['sag',.2],['sag',.6],['sag',.95],['cjk',.15],['cjk',.55],['cjk',.85],['nbu',.4]];
 let last='';
 for(const [id,t] of shots){await ev(([id,t])=>window.__go(id,t),[id,t]);await p.waitForTimeout(1600);await closeAll();
  if(id!==last){console.log('==',id,await ev(()=>document.getElementById('placeName').textContent),JSON.stringify(await ev(()=>window.__spots())));last=id;}
  await p.screenshot({path:D+id+'_'+t+'.jpg',type:'jpeg',quality:70});}
 console.log('ERR',JSON.stringify(errs.slice(0,6),null,1));await b.close();})();
