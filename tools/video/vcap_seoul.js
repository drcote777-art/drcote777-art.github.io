const B=require('./base.js');const fs=require('fs');
const FPS=24,DIR='frames';fs.rmSync(DIR,{recursive:true,force:true});fs.mkdirSync(DIR);
const CSS=`#top,#acts,#rail,#auto,#hint,#sub{visibility:hidden!important}
.panel{align-items:flex-start!important;padding-top:25vh!important;background:rgba(6,12,24,.55)!important}
.panel .in{transform:scale(.86) translateX(-2.5%);transform-origin:top center;border-radius:18px!important;max-height:none!important}
.panel .close{display:none!important}
#pan:not([hidden]) ~ #talk{visibility:hidden!important}
.talk{bottom:auto!important;top:25vh!important;transform:scale(.88) translateX(-2.5%);transform-origin:top center;border-radius:18px!important}
.real .lk a:not(.sv){display:none!important}
#vcap .loc{display:inline-block;margin-top:7px;background:rgba(9,15,28,.7);color:#fff;font-weight:700;font-size:14px;padding:5px 11px;border-radius:999px}
#vcap{position:fixed;left:50%;top:13%;transform:translateX(-50%);width:90%;z-index:2147483647;text-align:center;pointer-events:none;font-family:Inter,"Noto Sans",system-ui,sans-serif}
#vcap b{display:inline-block;background:rgba(9,15,28,.82);color:#fff;font-weight:800;font-size:24px;line-height:1.28;padding:9px 15px;border-radius:14px;box-shadow:0 6px 20px rgba(0,0,0,.35)}
#vcap small{display:inline-block;margin-top:7px;background:#f2c14e;color:#13233d;font-weight:800;font-size:16px;padding:6px 13px;border-radius:999px}
#vtap{position:fixed;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.45);border:3px solid #fff;transform:translate(-50%,-50%);z-index:2147483646;pointer-events:none;display:none;box-shadow:0 0 0 6px rgba(255,255,255,.18)}
#vend{position:fixed;inset:0;z-index:2147483647;display:none;flex-direction:column;align-items:center;justify-content:center;gap:14px;background:radial-gradient(120% 80% at 50% 30%,#1d3a63 0%,#0f1d33 60%,#0a1424 100%);font-family:Inter,"Noto Sans",system-ui,sans-serif;color:#fff;text-align:center;padding:0 26px}
#vend .k{color:#f2c14e;letter-spacing:.18em;font-size:12px;font-weight:700}
#vend h1{margin:0;font-size:44px;line-height:1.05;font-weight:900}
#vend p{margin:0;font-size:18px;opacity:.92;font-weight:600}
#vend .chips{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
#vend .chips span{border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:6px 12px;font-size:14px;font-weight:700}
#vend .url{margin-top:10px;background:#f2c14e;color:#13233d;font-weight:900;font-size:22px;padding:12px 18px;border-radius:14px}`;
(async()=>{const {b,p,errs}=await B.open({clock:true,raf:true,w:405,h:720,dsf:2});
 let n=0,tap=0,tapXY=null;
 const ev=(f,a)=>p.evaluate(f,a);
 const frame=async()=>{await p.clock.runFor(1000/FPS);await ev(()=>window.__step&&window.__step());
  if(tap>0){await ev(([x,y,k])=>{const t=document.getElementById('vtap');t.style.display='block';t.style.left=x+'px';t.style.top=y+'px';t.style.opacity=String(Math.min(1,k/6));t.style.transform='translate(-50%,-50%) scale('+(1.25-k/40)+')';},[tapXY[0],tapXY[1],tap]);tap--;if(!tap)await ev(()=>{document.getElementById('vtap').style.display='none';});}
  await p.screenshot({path:`${DIR}/f${String(n++).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});};
 const rec=async s=>{const k=Math.round(s*FPS);for(let i=0;i<k;i++)await frame();};
 const cap=(t,s,l)=>ev(([t,s,l])=>{document.getElementById('vcap').innerHTML=t?('<b>'+t+'</b>'+(s?'<br><small>'+s+'</small>':'')+(l?'<br><span class="loc">📍 '+l+'</span>':'')):'';},[t,s||'',l||'']);
 const tapEl=async(sel,re)=>{const xy=await ev(([sel,re])=>{const el=[...document.querySelectorAll(sel)].find(e=>new RegExp(re).test(e.textContent));if(!el)return null;const r=el.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2];},[sel,re]);if(xy){tapXY=xy;tap=8;}return xy;};
 const clickEl=(sel,re)=>ev(([sel,re])=>{const el=[...document.querySelectorAll(sel)].find(e=>new RegExp(re).test(e.textContent));if(el)el.click();return !!el;},[sel,re]);
 const closeAll=()=>ev(()=>{const pn=document.getElementById('pan');if(!pn.hidden){const c=pn.querySelector('[data-close]');if(c)c.click();}if(!document.getElementById('talk').hidden)document.getElementById('talkX').click();const a=document.getElementById('ai');if(!a.hidden){const g=document.getElementById('aiGo');g&&g.click();}});
 const autoOn=()=>ev(()=>{const a=document.getElementById('auto');if(a.getAttribute('aria-pressed')!=='true')a.click();});
 const autoOff=()=>ev(()=>{const a=document.getElementById('auto');if(a.getAttribute('aria-pressed')==='true')a.click();});
 // 준비
 for(let i=0;i<100;i++){await p.waitForTimeout(50);await B.tick(p,100);if(await ev(()=>{const e=document.getElementById('enter');return e&&!e.disabled;}))break;}
 await p.click('#enter');await B.tick(p,1200);await closeAll();
 await p.addStyleTag({content:CSS});
 await ev(()=>{const d=document.createElement('div');d.id='vcap';document.body.append(d);const t=document.createElement('div');t.id='vtap';document.body.append(t);const e=document.createElement('div');e.id='vend';e.innerHTML='<div class="k">INCHEON AIRPORT → SEOUL</div><h1>Virtual Seoul</h1><p>Rehearse your Seoul trip before you fly</p><div class="chips"><span>Free</span><span>No app</span><span>English & 한국어</span></div><div class="url">seoul-rehearsal.pages.dev</div>';document.body.append(e);});
 // S1 명동 걷기 (훅)
 await ev(()=>window.__go('myd',.1));await B.tick(p,800);await closeAll();await autoOn();await B.tick(p,1200);
 await cap('Going to Seoul soon? ✈️','Rehearse the trip here first','Myeongdong, Seoul');await rec(3.0);
 // S2 공항 입국 연습
 await autoOff();await ev(()=>window.__go('icn',0));await B.tick(p,600);await closeAll();
 await ev(()=>window.__spot(/Immigration/));await B.tick(p,300);
 await cap('Rehearse immigration, baggage & customs');await rec(1.4);
 await tapEl('#panB button','Foreign passports');await rec(0.25);await clickEl('#panB button','Foreign passports');await rec(2.35);
 // S3 공항철도
 await closeAll();await ev(()=>window.__spot(/AREX Express/));await B.tick(p,1600);
 await cap('Ride the airport train into the city','Real fares & times','AREX Airport Railroad');await rec(3.5);
 // S4 동네 몽타주
 for(const [id,t,lo] of [['nam',.32,'Namsan · N Seoul Tower'],['bkc',.25,'Bukchon Hanok Village'],['gng',.58,'COEX · Lotte World Tower']]){await cap('Walk Myeongdong, Namsan + 6 more areas','Palaces · hanok streets · markets · Han River',lo);await closeAll();await ev(([id,t])=>window.__go(id,t),[id,t]);await B.tick(p,700);await closeAll();await autoOn();await B.tick(p,900);await rec(1.5);await autoOff();}
 // S5 현지인에게 맛집 묻기 (Where should I eat? → Kimbap)
 await ev(()=>window.__go('myd',.31));await B.tick(p,600);await closeAll();await ev(()=>{window.__near('cit0');window.__talk('cit0');});await B.tick(p,300);
 await cap('Ask a local where to eat','Opens Google Maps ratings');
 {const n0=n;await rec(0.8);
 await tapEl('#talkQuick button','Where should I eat');await rec(0.25);await clickEl('#talkQuick button','Where should I eat');await rec(1.0);
 await tapEl('#talkQuick button','Kimbap');await rec(0.25);await clickEl('#talkQuick button','Kimbap');tap=0;await ev(()=>{document.getElementById('vtap').style.display='none';});
 while(n<n0+120)await frame();}
 // S6 실제 사진
 await closeAll();await ev(()=>window.__go('myd',.45));await B.tick(p,600);await closeAll();await ev(()=>window.__spot(/📷 Myeongdong Cathedral/));await B.tick(p,400);await p.waitForTimeout(600);await B.tick(p,200);
 await cap('Compare with real photos & Street View');await rec(4.0);
 // S7 마지막 화면
 await cap('');await ev(()=>{document.getElementById('vend').style.display='flex';});await rec(3.0);
 console.log('frames',n,'errs',JSON.stringify(errs.slice(0,5)));await b.close();})();
