// 가상 충남·서해안: 실제로 눌러 보는 시험 — 지역 고르기, 3일 일정 전체(기차·버스·택시·퀴즈·가게·스탬프·호텔·여행 마치기)
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/',REPO='/home/claude/drcote777-art.github.io',D=S+'doc/nf/';fs.mkdirSync(D,{recursive:true});
const three=fs.readFileSync('/root/cruise/node_modules/three/build/three.min.js','utf8');const LOC=process.env.LOC||'ko-KR';
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1,locale:LOC,timezoneId:'Asia/Seoul'});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e.stack||e).slice(0,500)));
 await p.route('**/*',r=>{const u=r.request().url();if(u.includes('three.min.js'))return r.fulfill({body:three,contentType:'application/javascript'});
  if(u.startsWith('http://site.test/')){let pa=new URL(u).pathname;let f=pa==='/'?REPO+'/tools/regions/seoul.html':pa==='/cnm.html'?REPO+'/tools/regions/cnm.html':REPO+'/dist-seoul'+pa;
   if(fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.js')?'application/javascript':'application/octet-stream'});return r.fulfill({status:404,body:''});}
  return r.abort();});
 const log=[];const say=(...a)=>{log.push(a.join(' '));};
 const place=()=>p.evaluate(()=>document.getElementById('placeName').textContent);
 const st=()=>p.evaluate(()=>window.__st());
 const clickText=async(re,sel)=>p.evaluate(([src,sel])=>{const re=new RegExp(src);const bs=[...document.querySelectorAll(sel||'button')].filter(x=>x.offsetParent&&re.test(x.textContent));if(bs[0]){bs[0].click();return bs[0].textContent.trim().slice(0,40);}return null;},[re.source,sel||'button']);
 const cont=async()=>{await p.waitForTimeout(500);return clickText(/계속 ▸|Continue ▸/);};
 const quiz=async(ans)=>{await p.waitForTimeout(700);const a=await clickText(new RegExp(ans.replace(/[.*+?^${}()|[\]\\₩]/g,'\\$&')),'#pan button');const c=await cont();return a?('answered '+a+(c?' +continue':'')):'no quiz';};
 const ride=async(spotRe,ans,dest)=>{await p.evaluate((s)=>window.__spot(new RegExp(s)),spotRe.source);let q='';if(ans)q=await quiz(ans);const from=await place();await p.waitForFunction((f)=>document.getElementById('placeName').textContent!==f,from,{timeout:15000}).catch(()=>{});await p.waitForTimeout(1500);
  await p.evaluate(()=>window.__act('skipride'));await p.waitForFunction((d)=>document.getElementById('placeName').textContent===d,dest,{timeout:60000}).catch(()=>{});
  await p.waitForTimeout(1200);const pl=await place();const s=await st();say('RIDE',spotRe.source,'|',q,'| →',pl,pl===dest?'OK':'**EXPECTED '+dest+'**','| ₩'+s.eur,'| done',s.done,'| next:',s.next);};
 const link=async(spotRe,ans,dest)=>{await p.evaluate((s)=>window.__spot(new RegExp(s)),spotRe.source);let q='';if(ans)q=await quiz(ans);await p.waitForFunction((d)=>document.getElementById('placeName').textContent===d,dest,{timeout:20000}).catch(()=>{});await p.waitForTimeout(1500);const pl=await place();const s=await st();say('LINK',spotRe.source,'|',q,'| →',pl,pl===dest?'OK':'**EXPECTED '+dest+'**','| done',s.done,'| next:',s.next);};
 const shop=async(go,spotRe,ans,item)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1300);const r=await p.evaluate((s)=>window.__spot(new RegExp(s)),spotRe.source);let q='';if(ans)q=await quiz(ans);await p.waitForTimeout(800);
  const c=await clickText(new RegExp(item),'#pan button');await p.waitForTimeout(900);await clickText(/닫기|Close/);const s=await st();say('SHOP',r,'|',q,'→',c,'| ₩'+s.eur,'| done',s.done,'| next:',s.next);};
 const stamp=async(go)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1200);const r=await p.evaluate(()=>{const b=[...document.querySelectorAll('#acts button')].find(x=>/스탬프|Stamp/.test(x.textContent));if(b){b.click();return 'ok';}return 'NO STAMP BUTTON';});await p.waitForTimeout(900);await cont();await clickText(/닫기|Close/);const s=await st();say('STAMP',go[0],r,'| done',s.done,'| next:',s.next);};
 const near=async(go)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1500);const s=await st();say('NEAR',go.join(':'),'| done',s.done,'| next:',s.next);};
 const lift=async(go,spotRe,ans,shot)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1300);const r=await p.evaluate((s)=>window.__spot(new RegExp(s)),spotRe.source);const q=ans?await quiz(ans):'';await p.waitForTimeout(4200);await clickText(/닫기|Close/);
  const y=await p.evaluate(()=>Math.round(window.__me.y));const s=await st();say('LIFT',r,'|',q,'| y',y,'| ₩'+s.eur,'| done',s.done,'| next:',s.next);await p.screenshot({path:D+shot});};
 const sleep=async(id,t,doorRe,shot)=>{await p.evaluate(([id,t])=>window.__go(id,t),[id,t]);await p.waitForTimeout(1200);await p.evaluate((s)=>window.__spot(new RegExp(s)),doorRe.source);await p.waitForTimeout(2600);say('HOTEL',await place());await p.screenshot({path:D+shot});
  await p.evaluate(()=>window.__act('sleep'));await p.waitForTimeout(3000);await cont();await p.waitForTimeout(1500);say('NEXT DAY',await place(),JSON.stringify(await st()));};
 // 서울 첫 화면 지역 고르기 → 충남·서해안
 await p.goto('http://site.test/');await p.waitForTimeout(2000);
 say('SEOUL chips',JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('#stReg a,#stReg span')].map(a=>a.textContent+(a.getAttribute('href')?'→'+a.getAttribute('href'):'')))));
 await p.click('#stReg a[href="cnm.html"]');await p.waitForTimeout(2500);say('TITLE',await p.title());
 await p.waitForSelector('#enter:not([disabled])',{timeout:20000});say('ENTER',await p.textContent('#enter'));await p.click('#enter');await p.waitForTimeout(2500);say('START',await place(),JSON.stringify(await st()));
 const K=LOC.startsWith('ko');
 // DAY 1
 await near(['yst',.45]);await p.screenshot({path:D+'0_yst.png'});await p.evaluate(()=>window.__go('yst',.82));await p.waitForTimeout(1200);
 await ride(K?/천안 가는 기차/:/Train to Cheonan/,'6,100',K?'천안 · 독립기념관':'Cheonan · Independence Hall');await p.screenshot({path:D+'1_cna.png'});
 await shop(['cna',.12],K?/호두과자 가게/:/Hodu-gwaja shop/,null,K?'호두과자 \\(작은':'Walnut cakes \\(small');
 await near(['cna',.35]);await stamp(['cna',.97]);await p.screenshot({path:D+'2_cna.png'});
 await p.evaluate(()=>window.__go('cna',.06));await p.waitForTimeout(1200);
 await ride(K?/온양온천 가는 기차/:/Train to Onyangoncheon/,K?'월요일':'Mondays',K?'아산 · 온양온천':'Asan · Onyang Hot Spring');
 await near(['ony',.35]);await p.screenshot({path:D+'3_ony.png'});await shop(['ony',.62],K?/온천탕/:/Hot spring bathhouse/,null,K?'온천탕 어른':'Hot spring bath');await stamp(['ony',.97]);
 await sleep('ony',.5,K?/온양 호텔/:/Hotel in Onyang/,'4_hotel.png');
 // DAY 2
 await p.evaluate(()=>window.__go('ony',.1));await p.waitForTimeout(1200);
 await ride(K?/당진 가는 시외버스/:/Intercity bus to Dangjin/,K?'약 1,300년':'About 1,300 years',K?'당진 · 왜목마을':'Dangjin · Waemok Village');
 await near(['wmk',.45]);await stamp(['wmk',.97]);await p.screenshot({path:D+'5_wmk.png'});
 await p.evaluate(()=>window.__go('wmk',.9));await p.waitForTimeout(1200);
 await link(K?/해미읍성까지 택시/:/Taxi to Haemieupseong/,K?'해돋이':'Sunrise',K?'서산 · 해미읍성':'Seosan · Haemieupseong');
 await near(['hmi',.45]);await stamp(['hmi',.97]);await p.screenshot({path:D+'6_hmi.png'});
 await p.evaluate(()=>window.__go('hmi',.06));await p.waitForTimeout(1200);
 await ride(K?/안면도 가는 버스/:/Bus to Anmyeondo/,'1491',K?'안면도 · 꽃지해수욕장':'Anmyeondo · Kkotji Beach');
 await near(['kkj',.4]);await shop(['kkj',.6],K?/해물 식당/:/Seafood restaurant/,null,K?'해물칼국수':'Seafood kalguksu');await stamp(['kkj',.97]);await p.screenshot({path:D+'7_kkj.png'});
 await sleep('kkj',.03,K?/안면도 호텔/:/Hotel on Anmyeondo/,'8_hotel.png');
 // DAY 3
 await p.evaluate(()=>window.__go('kkj',.08));await p.waitForTimeout(1200);
 await link(K?/해저터널 지나 택시/:/through the undersea tunnel/,K?'할미':'Halmi',K?'보령 · 대천해수욕장':'Boryeong · Daecheon Beach');
 await near(['dcb',.4]);await shop(['dcb',.55],K?/조개구이 집/:/Shellfish grill/,null,K?'바지락칼국수':'Shellfish kalguksu');await stamp(['dcb',.97]);await p.screenshot({path:D+'9_dcb.png'});
 await p.evaluate(()=>window.__go('dcb',.12));await p.waitForTimeout(1200);
 await ride(K?/용산 가는 기차/:/Train to Yongsan/,K?'보령머드축제':'Boryeong Mud',K?'용산역':'Yongsan Station');
 await p.evaluate(()=>window.__go('sar',.85));await p.waitForTimeout(1500);
 await p.evaluate(()=>window.__spot(/여행 마치기|Finish the trip/));await p.waitForTimeout(2500);
 say('END',await p.evaluate(()=>{const e=document.querySelector('#passLead');return e?e.textContent:'(no passLead)';}),JSON.stringify(await st()));
 await p.screenshot({path:D+'10_end.png'});
 console.log(log.join('\n'));console.log('ERRORS',JSON.stringify(errs,null,1));await b.close();})();
