// 가상 부산 틱톡 영상: 24fps 프레임 녹화 (405x720, DSF 2) — 서울 영상(vcap2.js)과 같은 방식
const B=require('./base.js');const fs=require('fs');
const FPS=24,DIR=process.env.DIR||'frames_busan',DSF=+(process.env.DSF||2);
fs.rmSync(DIR,{recursive:true,force:true});fs.mkdirSync(DIR);
const CSS=fs.readFileSync(__dirname+'/vcss.css','utf8')+`
#toast{visibility:hidden!important}
#vend .url{line-height:1.25}
#vend .url small{display:block;font-size:20px;font-weight:900}`;
(async()=>{const {b,p,errs}=await B.open({clock:true,raf:true,w:405,h:720,dsf:DSF,q:'busan.html',pm:['ph/local_busan.json']});
 let n=0,tap=0,tapXY=null;const log=[];
 const ev=(f,a)=>p.evaluate(f,a);
 const frame=async()=>{await p.clock.runFor(1000/FPS);await ev(()=>window.__step&&window.__step());
  if(tap>0){await ev(([x,y,k])=>{const t=document.getElementById('vtap');t.style.display='block';t.style.left=x+'px';t.style.top=y+'px';t.style.opacity=String(Math.min(1,k/6));t.style.transform='translate(-50%,-50%) scale('+(1.25-k/40)+')';},[tapXY[0],tapXY[1],tap]);tap--;if(!tap)await ev(()=>{document.getElementById('vtap').style.display='none';});}
  await p.screenshot({path:`${DIR}/f${String(n++).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});};
 const rec=async s=>{const k=Math.round(s*FPS);for(let i=0;i<k;i++)await frame();};
 const cap=(t,s,l)=>ev(([t,s,l])=>{document.getElementById('vcap').innerHTML=t?('<b>'+t+'</b>'+(s?'<br><small>'+s+'</small>':'')+(l?'<br><span class="loc">📍 '+l+'</span>':'')):'';},[t,s||'',l||'']);
 const tapEl=async(sel,re)=>{const xy=await ev(([sel,re])=>{const el=[...document.querySelectorAll(sel)].find(e=>new RegExp(re).test(e.textContent));if(!el)return null;const r=el.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2];},[sel,re]);if(xy){tapXY=xy;tap=8;}return xy;};
 const clickEl=(sel,re)=>ev(([sel,re])=>{const el=[...document.querySelectorAll(sel)].find(e=>new RegExp(re).test(e.textContent));if(el)el.click();return !!el;},[sel,re]);
 const closeAll=()=>ev(()=>{const pn=document.getElementById('pan');if(!pn.hidden){const c=pn.querySelector('[data-close]');if(c)c.click();}if(!document.getElementById('talk').hidden)document.getElementById('talkX').click();const a=document.getElementById('ai');if(a&&!a.hidden){const g=document.getElementById('aiGo');g&&g.click();}});
 const autoOn=()=>ev(()=>{const a=document.getElementById('auto');if(a.getAttribute('aria-pressed')!=='true')a.click();});
 const autoOff=()=>ev(()=>{const a=document.getElementById('auto');if(a.getAttribute('aria-pressed')==='true')a.click();});
 const place=()=>ev(()=>document.getElementById('placeName').textContent);
 const note=async s=>{log.push('#'+n+' '+s+' | '+(await place()));};
 // 화면 끌기로 카메라 돌리기 (마우스 드래그: 가로 1px = 0.006rad, 세로 1px = 높이 0.02)
 const look=async(dyaw,dh)=>{const dx=-dyaw/0.006,dy=dh/0.02;await p.mouse.move(200,420);await p.mouse.down();const k=8;for(let i=1;i<=k;i++)await p.mouse.move(200+dx*i/k,420+dy*i/k);await p.mouse.up();};
 // 준비
 for(let i=0;i<200;i++){await p.waitForTimeout(50);await B.tick(p,100);if(await ev(()=>{const e=document.getElementById('enter');return e&&!e.disabled;}))break;}
 await p.click('#enter');await B.tick(p,1200);await closeAll();
 const now=await ev(()=>Date.now());await p.clock.pauseAt(now+1000); // 시계 멈춤: 프레임마다 정확히 1/24초씩만 흐름
 await p.addStyleTag({content:CSS});
 await ev(()=>{const d=document.createElement('div');d.id='vcap';document.body.append(d);const t=document.createElement('div');t.id='vtap';document.body.append(t);const e=document.createElement('div');e.id='vend';e.innerHTML='<div class="k">SEOUL → BUSAN · TONGYEONG</div><h1>Virtual Busan</h1><p>Rehearse a 3-day Busan trip<br>before you go</p><div class="chips"><span>Free</span><span>No app</span><span>English & 한국어</span></div><div class="url">seoul-rehearsal.pages.dev<small>/busan.html</small></div>';document.body.append(e);});
 // S1 서울역 KTX 승강장 (훅) 3.0s
 await ev(()=>window.__go('sst',.55));await B.tick(p,700);await closeAll();await autoOn();await B.tick(p,900);
 await cap('Going to Busan soon? 🚄','Rehearse the trip here first','Seoul Station · KTX');await note('S1');await rec(3.0);
 // S2 KTX 요금 퀴즈 3.75s
 await autoOff();await ev(()=>window.__go('sst',.8));await B.tick(p,600);await closeAll();
 await ev(()=>window.__spot(/KTX to Busan/));await B.tick(p,300);
 await cap('Know the real fares before you go 🎫');await note('S2');await rec(1.25);
 await tapEl('#pan button','54,400');await rec(0.25);await clickEl('#pan button','54,400');await rec(2.25);
 // S3 KTX 타기 3.0s
 {const from=await place();await clickEl('#pan button','Continue');for(let i=0;i<120;i++){await B.tick(p,100);if((await place())!==from)break;}}
 await B.tick(p,1600);await cap('Ride the KTX to Busan','Real fares & times','KTX · Seoul → Busan');await note('S3');await rec(3.0);
 await ev(()=>window.__act('skipride'));for(let i=0;i<200;i++){await B.tick(p,100);if((await place())==='Busan Station')break;}await closeAll();
 // S4 부산 동네 몽타주 4.5s
 for(const [id,t,lo] of [['nmp',.16,'Jagalchi Market'],['gmc',.38,'Gamcheon Culture Village'],['hud',.55,'Haeundae Beach']]){
  await cap('Walk Jagalchi, Gamcheon & Haeundae','Fish market · painted village · beach',lo);await closeAll();await ev(([id,t])=>window.__go(id,t),[id,t]);await B.tick(p,700);await closeAll();await autoOn();await B.tick(p,900);await note('S4 '+id);await rec(1.5);await autoOff();}
 // S5 광안리 드론쇼 (밤) 3.75s
 await closeAll();await ev(()=>{window.__G().skyMode='night';});await ev(()=>window.__go('gal',.6));await B.tick(p,800);await closeAll();
 await ev(()=>window.__spot(/Drone light show/));{const ry=await ev(()=>window.__me.ry);await look(Math.PI-ry+0.07,-1.2);}
 await B.tick(p,400);await closeAll();
 await cap('Gwangalli drone show ✨','Every Saturday night');await note('S5');await rec(3.75);
 await ev(()=>{window.__G().skyMode=null;});
 // S6 통영 케이블카 정상 2.25s (천천히 둘러보기: 바다·섬 → 항구 마을)
 await closeAll();await ev(()=>window.__go('tyg',.8));await B.tick(p,600);await closeAll();
 await ev(()=>window.__spot(/🚡 Tongyeong Cable Car/));await B.tick(p,2950);await closeAll();
 await look(-.5,.8);await B.tick(p,100);
 await cap('Day 3: Tongyeong cable car','','Tongyeong · Mireuksan');await note('S6');
 await p.mouse.move(320,420);await p.mouse.down();{const k=Math.round(2.25*FPS);for(let i=1;i<=k;i++){await p.mouse.move(320-i*(0.9/0.006/k),420);await frame();}}await p.mouse.up();
 // S7 실제 사진 비교 3.75s
 await closeAll();await ev(()=>window.__go('gmc',.3));await B.tick(p,600);await closeAll();
 await ev(()=>window.__spot(/📷 Gamcheon Culture Village/));await B.tick(p,400);await p.waitForTimeout(800);await B.tick(p,200);
 await cap('Compare with real photos & Street View');await note('S7');await rec(3.75);
 // S8 마지막 화면 3.0s
 await cap('');await ev(()=>{document.getElementById('vend').style.display='flex';});await note('S8');await rec(3.0);
 console.log(log.join('\n'));console.log('frames',n,'errs',JSON.stringify(errs.slice(0,5)));await b.close();})();
