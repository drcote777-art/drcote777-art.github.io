// 가상 동해안: 실제로 눌러 보는 시험 — 지역 고르기, 3일 일정 전체(탈것·퀴즈·가게·스탬프·호텔·케이블카·여행 마치기)
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const REPO='/home/claude/drcote777-art.github.io',D=__dirname+'/ef/';fs.mkdirSync(D,{recursive:true});
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
 // 1) 서울 첫 화면의 지역 고르기 → 동해안
 await p.goto('http://site.test/');await p.waitForTimeout(2000);
 say('SEOUL chips',JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('#stReg a,#stReg span')].map(a=>a.textContent+(a.getAttribute('href')?'→'+a.getAttribute('href'):'')))));
 await p.click('#stReg a[href="east.html"]');await p.waitForTimeout(2500);say('TITLE',await p.title());
 await p.waitForSelector('#enter:not([disabled])',{timeout:20000});say('ENTER',await p.textContent('#enter'));await p.click('#enter');await p.waitForTimeout(2500);
 say('START',await place(),JSON.stringify(await st()));
 // DAY 1
 await near(['sst',.45]);
 await p.evaluate(()=>window.__go('sst',.82));await p.waitForTimeout(1200);say('SST spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 await ride(/강릉행 KTX-이음/,'27,600','강릉역');await p.screenshot({path:D+'1_gns.png'});
 say('GNS spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 await ride(/안목 가는 버스/,null,'안목해변 · 커피거리');
 await buy(['anm',.45],/바다 보이는 카페/,'핸드드립');
 await stamp(['anm',.97]);
 await p.evaluate(()=>window.__go('anm',.93));await p.waitForTimeout(1200);
 await ride(/경포대로/,'약 7km','경포대 · 경포해변');
 await near(['gyp',.1]);await buy(['gyp',.3],/초당순두부집/,'순두부 백반');await near(['gyp',.55]);await stamp(['gyp',.97]);
 await p.evaluate(()=>window.__go('gyp',.93));await p.waitForTimeout(1200);
 await ride(/오죽헌으로/,'바닷물로 굳혀요','오죽헌');
 await p.evaluate(()=>window.__spot(/매표소/));say('OJK quiz',await quiz('율곡 이이'));await p.waitForTimeout(500);await clickText(/어른 입장권/,'#pan button');await p.waitForTimeout(800);await clickText(/닫기|Close/);
 say('OJK ticket',JSON.stringify(await st()));
 await near(['ojk',.5]);await stamp(['ojk',.97]);
 await p.evaluate(()=>window.__go('ojk',.97));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/호텔/));await p.waitForTimeout(2500);say('HOTEL',await place());await p.screenshot({path:D+'2_hotel.png'});
 await p.evaluate(()=>window.__act('sleep'));await p.waitForTimeout(3000);await cont();await p.waitForTimeout(1500);say('DAY2',await place(),JSON.stringify(await st()));
 // DAY 2
 if((await place())!=='강릉역'){await p.evaluate(()=>window.__go('gns',.12));await p.waitForTimeout(1200);}
 await ride(/정동진 가는 기차/,'약 15분','정동진 · 모래시계공원');await p.screenshot({path:D+'3_jdj.png'});
 await near(['jdj',.15]);await near(['jdj',.55]);await near(['jdj',.95]);await stamp(['jdj',.97]);
 await p.evaluate(()=>window.__go('jdj',.06));await p.waitForTimeout(1200);
 await ride(/기차 \+ 시외버스로 속초/,'광화문의 정동쪽이라서','속초 시장 · 갯배 · 아바이마을');
 await buy(['skc',.27],/닭강정 가게/,'닭강정 \\(중\\)');await near(['skc',.58]);await buy(['skc',.69],/갯배 요금/,'갯배 어른 편도');await buy(['skc',.8],/아바이순대집/,'아바이순대');await stamp(['skc',.97]);
 await p.evaluate(()=>window.__go('skc',.97));await p.waitForTimeout(1200);await p.evaluate(()=>window.__spot(/호텔/));await p.waitForTimeout(2500);
 await p.evaluate(()=>window.__act('sleep'));await p.waitForTimeout(3000);await cont();await p.waitForTimeout(1500);say('DAY3',await place(),JSON.stringify(await st()));
 // DAY 3
 if((await place())!=='속초 시장 · 갯배 · 아바이마을'){await p.evaluate(()=>window.__go('skc',.04));await p.waitForTimeout(1200);}
 await ride(/설악산 가는 7·7-1번 버스/,'승객이 줄을 당겨서','설악산 · 신흥사 · 케이블카');
 await near(['srk',.4]);await buy(['srk',.2],/설악동 식당/,'산채비빔밥');
 await p.evaluate(()=>window.__go('srk',.64));await p.waitForTimeout(1300);say('SRK spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 const lb=await p.evaluate(()=>window.__spot(/🚡 설악케이블카/));say('LIFT',lb,await quiz('₩16,000'));await p.waitForTimeout(4000);
 say('LIFT top y',await p.evaluate(()=>Math.round(window.__me.y)),JSON.stringify(await st()));await p.screenshot({path:D+'4_summit.png'});
 await stamp(['srk',.99]);
 await p.evaluate(()=>window.__go('srk',.08));await p.waitForTimeout(1200);
 await ride(/동서울 가는 고속버스/,'약 2시간 반','동서울종합터미널');
 await p.evaluate(()=>window.__go('nbu',.85));await p.waitForTimeout(1500);say('NBU spots',JSON.stringify(await p.evaluate(()=>window.__spots())));
 await p.evaluate(()=>window.__spot(/여행 마치기/));await p.waitForTimeout(2500);
 say('PASS',await p.evaluate(()=>{const h=document.querySelector('#pass h2');return (h?h.textContent:'')+' | '+(document.querySelector('#passLead')||{}).textContent;}));
 say('END',await p.evaluate(()=>{const e=document.querySelector('#passLead');return e?e.textContent:'(no passLead)';}),JSON.stringify(await st()));
 await p.screenshot({path:D+'5_end.png'});
 console.log(log.join('\n'));console.log('ERRORS',JSON.stringify(errs,null,1));await b.close();})();
