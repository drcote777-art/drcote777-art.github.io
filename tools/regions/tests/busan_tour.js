// 가상 부산 페이지: 첫 화면 → 장면마다 이동해 사진 찍고, 페이지 오류를 모읍니다.
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const REPO='/home/claude/drcote777-art.github.io',D=__dirname+'/bt/';fs.mkdirSync(D,{recursive:true});
const three=fs.readFileSync('/root/cruise/node_modules/three/build/three.min.js','utf8');
const PAGE=process.env.PAGE||'busan.html',VW=+(process.env.VW||390),VH=+(process.env.VH||844),LOC=process.env.LOC||'ko-KR';
const SC=(process.env.SC||'sst:.02,sst:.45,sst:.8,bsn:.05,bsn:.7,nmp:.05,nmp:.2,nmp:.45,nmp:.62,nmp:.8,nmp:.995,gmc:.05,gmc:.45,hud:.1,hud:.35,hud:.92,ygs:.05,ygs:.35,ygs:.6,gal:.2,gal:.5,tyg:.05,tyg:.4,tyg:.75,tyg:.995,nbu:.5,hotel:0').split(',');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const ctx=await b.newContext({viewport:{width:VW,height:VH},isMobile:VW<700,hasTouch:VW<700,deviceScaleFactor:+(process.env.DSF||1),locale:LOC,timezoneId:'Asia/Seoul'});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e.stack||e).slice(0,700)));p.on('console',m=>{if(m.type()==='error')errs.push('console: '+m.text().slice(0,200));});
 await p.route('**/*',r=>{const u=r.request().url();if(u.includes('three.min.js'))return r.fulfill({body:three,contentType:'application/javascript'});
  if(u.startsWith('http://site.test/')){let pa=new URL(u).pathname;if(pa==='/')pa='/index.html';const f=REPO+'/dist-seoul'+pa;
   if(fs.existsSync(f))return r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.js')?'application/javascript':f.endsWith('.png')?'image/png':f.endsWith('.jpg')?'image/jpeg':f.endsWith('.webmanifest')?'application/manifest+json':'model/gltf-binary'});return r.fulfill({status:404,body:''});}
  return r.abort();});
 await p.goto('http://site.test/'+PAGE);await p.waitForTimeout(2500);await p.screenshot({path:D+'00_start.png'});
 const info={title:await p.title(),reg:await p.evaluate(()=>[...document.querySelectorAll('#stReg a,#stReg span')].map(e=>(e.className==='on'?'*':'')+e.textContent+(e.getAttribute('href')?'→'+e.getAttribute('href'):'')))};
 const en=await p.waitForSelector('#enter:not([disabled])',{timeout:15000}).then(()=>1).catch(()=>0);if(!en){console.log('ENTER DISABLED; errors:',JSON.stringify(errs,null,1));await b.close();return;}await p.click('#enter');await p.waitForTimeout(3000);await p.screenshot({path:D+'01_first.png'});
 info.first=await p.evaluate(()=>({place:document.getElementById('placeName').textContent,sub:document.getElementById('placeSub').textContent,wx:(document.getElementById('wx')||{}).textContent}));
 info.scenes=[];
 for(const [i,x] of SC.entries()){const [id,t]=x.split(':');await p.evaluate(([id,t])=>window.__go(id,+t),[id,t]);await p.waitForTimeout(1800);
  const r=await p.evaluate(()=>({place:document.getElementById('placeName').textContent,spots:[...document.querySelectorAll('#acts button b')].map(b=>b.textContent).slice(0,6)}));
  info.scenes.push(id+':'+t+' | '+r.place+' | '+r.spots.join(' / '));await p.screenshot({path:D+String(i+2).padStart(2,'0')+'_'+id+'_'+t+'.png'});}
 info.errs=errs;console.log(JSON.stringify(info,null,1));await b.close();})();
