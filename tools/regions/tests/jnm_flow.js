// 가상 동해안: 실제로 눌러 보는 시험 — 지역 고르기, 3일 일정 전체(탈것·퀴즈·가게·스탬프·호텔·케이블카·여행 마치기)
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const REPO='/home/claude/drcote777-art.github.io',D=__dirname+'/jf/';fs.mkdirSync(D,{recursive:true});
const three=fs.readFileSync('/root/cruise/node_modules/three/build/three.min.js','utf8');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1,locale:'ko-KR',timezoneId:'Asia/Seoul'});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e.stack||e).slice(0,500)));
 await p.route('**/*',r=>{const u=r.request().url();if(u.includes('three.min.js'))return r.fulfill({body:three,contentType:'application/javascript'});
  if(u.startsWith('http://site.test/')){let pa=new URL(u).pathname;if(pa==='/')pa='/index.html';const f=REPO+'/dist-seoul'+pa;
   if(fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.js')?'application/javascript':f.endsWith('.png')?'image/png':f.endsWith('.jpg')?'image/jpeg':'model/gltf-binary'});return r.fulfill({status:404,body:''});}
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
 const buy=async(go,spotRe,item)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1300);const r=await p.evaluate((s)=>window.__spot(new RegExp(s)),spotRe.source);await p.waitForTimeout(800);
  const c=await clickText(new RegExp(item),'#pan button');await p.waitForTimeout(900);await clickText(/닫기|Close/);const s=await st();say('BUY',r,'→',c,'| ₩'+s.eur,'| done',s.done,'| next:',s.next);};
 const stamp=async(go)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1200);say('  stamp btn',await p.evaluate(()=>{const b=[...document.querySelectorAll('#acts button')].find(x=>/스탬프|Stamp/.test(x.textContent));if(b){b.click();return b.textContent;}return 'NO STAMP BUTTON';}));await p.waitForTimeout(900);await cont();await clickText(/닫기|Close/);const s=await st();say('STAMP',go[0],'| done',s.done,'| next:',s.next);};
 const near=async(go)=>{await p.evaluate(([id,t])=>window.__go(id,t),go);await p.waitForTimeout(1500);const s=await st();say('NEAR',go.join(':'),'| done',s.done,'| next:',s.next);};
 // 1) 서울 첫 화면의 지역 고르기 → 전남·광주
 await p.goto('http://site.test/');await p.waitForTimeout(2000);
 say('SEOUL chips',JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('#stReg a,#stReg span')].map(a=>a.textContent+(a.getAttribute('href')?'→'+a.getAttribute('href'):'')))));
 await p.click('#stReg a[href="jnm.html"]');await p.waitForTimeout(2500);say('TITLE',await p.title());
 await p.waitForSelector('#enter:not([disabled])',{timeout:20000});await p.click('#enter');await p.waitForTimeout(2500);
 say('START',await place(),JSON.stringify(await st()));
 // DAY 1
 await near(['sst',.45]);await p.evaluate(()=>window.__go('sst',.82));await p.waitForTimeout(1200);
 await ride(/광주송정행 KTX/,'42,400','광주송정역');
 await p.evaluate(()=>window.__go('gsj',.8));await p.waitForTimeout(1200);say('GSJ spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 await ride(/1호선 문화전당역 방면/,'하나의 특별시가 됐어요','5·18민주광장 · 국립아시아문화전당');
 await near(['acc',.3]);await near(['acc',.55]);await near(['acc',.85]);await stamp(['acc',.97]);
 await p.evaluate(()=>window.__go('acc',.05));await p.waitForTimeout(1200);
 await ride(/담양 가는 버스/,'민주의 종','담양 죽녹원 · 관방제림');
 await p.evaluate(()=>window.__go('dmy',.04));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/죽녹원 매표소/));say('DMY quiz',await quiz('약 2.2km'));await p.waitForTimeout(500);await clickText(/어른 입장권/,'#pan button');await p.waitForTimeout(800);await clickText(/닫기|Close/);
 say('DMY ticket',JSON.stringify(await st()));
 await near(['dmy',.4]);await buy(['dmy',.55],/떡갈비집/,'떡갈비');await near(['dmy',.85]);await stamp(['dmy',.97]);
 await p.evaluate(()=>window.__go('dmy',.97));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/광주 호텔로/));await p.waitForTimeout(2500);say('HOTEL',await place());
 await p.evaluate(()=>window.__act('sleep'));await p.waitForTimeout(3000);await cont();await p.waitForTimeout(1500);say('DAY2',await place(),JSON.stringify(await st()));
 // DAY 2
 if((await place())!=='5·18민주광장 · 국립아시아문화전당'){await p.evaluate(()=>window.__go('acc',.06));await p.waitForTimeout(1200);}
 await ride(/순천 가는 시외버스/,null,'순천만습지');
 await p.evaluate(()=>window.__go('scw',.08));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/순천만 매표소/));say('SCW quiz',await quiz('순천만습지'));await p.waitForTimeout(500);await clickText(/어른 입장권/,'#pan button');await p.waitForTimeout(800);await clickText(/닫기|Close/);
 say('SCW ticket',JSON.stringify(await st()));
 await buy(['scw',.14],/순천만 식당/,'짱뚱어탕');await near(['scw',.4]);await near(['scw',.98]);await stamp(['scw',.99]);
 await p.evaluate(()=>window.__go('scw',.25));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/순천 호텔/));await p.waitForTimeout(2500);
 await p.evaluate(()=>window.__act('sleep'));await p.waitForTimeout(3000);await cont();await p.waitForTimeout(1500);say('DAY3',await place(),JSON.stringify(await st()));
 // DAY 3
 if((await place())!=='순천만습지'){await p.evaluate(()=>window.__go('scw',.04));await p.waitForTimeout(1200);}
 await ride(/여수EXPO 가는 기차/,'약 20분','여수EXPO역 · 오동도');
 await near(['odo',.5]);await near(['odo',.95]);await stamp(['odo',.97]);
 await p.evaluate(()=>window.__go('odo',.38));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/케이블카 타는 곳으로/));say('ODO link',await quiz('동백꽃'));
 await p.waitForFunction(()=>document.getElementById('placeName').textContent==='여수 해상케이블카',null,{timeout:15000}).catch(()=>{});say('AFTER LINK',await place(),JSON.stringify(await st()));
 await p.evaluate(()=>window.__go('ycb',.3));await p.waitForTimeout(1300);say('YCB spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 const lb=await p.evaluate(()=>window.__spot(/🚡 여수 해상케이블카/));say('LIFT',lb,await quiz('₩17,000'));await p.waitForTimeout(4000);
 say('LIFT top y',await p.evaluate(()=>Math.round(window.__me.y)),JSON.stringify(await st()));await p.screenshot({path:D+'4_cabin.png'});
 await stamp(['ycb',.99]);
 await p.evaluate(()=>window.__go('ycb',.08));await p.waitForTimeout(1200);
 await ride(/용산 가는 KTX/,'약 2시간 50분','용산역');
 await p.evaluate(()=>window.__go('sar',.85));await p.waitForTimeout(1500);say('SAR spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 await p.evaluate(()=>window.__spot(/여행 마치기/));await p.waitForTimeout(2500);
 say('PASS',await p.evaluate(()=>{const h=document.querySelector('#pass h2');return (h?h.textContent:'')+' | '+(document.querySelector('#passLead')||{}).textContent;}));
 say('END',JSON.stringify(await st()));
 await p.screenshot({path:D+'5_end.png'});
 console.log(log.join('\n'));console.log('ERRORS',JSON.stringify(errs,null,1));await b.close();})();
