/* ---------- 맛집 물어보기: 길에서 만난 사람에게 물으면 → 구글 지도 별점(Places UI Kit)으로 추천 → 메타버스 안에서 길 이어 주기 → 거리뷰로 가게 앞 구경 → 메뉴·사진·후기 → 실제 길찾기 ----------
   구글 약관(서비스별 약관 15장): Places UI Kit는 구글 외 지도·화면과 함께 써도 됨. 위도·경도만 30일까지 임시 저장 가능 — 여기서는 저장하지 않고 화면에 있는 동안만 씀.
   가게 이름·별점·사진·후기는 구글이 만든 화면 요소 안에서만 보여 주고, 구글 출처 표시를 가리지 않음.
   키가 없거나 불러오기에 실패하면: 구글 지도(핀을 누르면 별점) · 네이버 지도 · 카카오맵으로 연결만 함 (가짜 별점을 지어내지 않음). */
const GCFG=Object.assign({gmapsKey:'',gmapsBilling:false},window.SEOUL_CFG||{});
const FOODS=[
 {k:'김밥',e:'kimbap',s:'Kimbap',ic:'🍙',re:/김밥|kimbap|gimbap/i},
 {k:'떡볶이',e:'tteokbokki',s:'Tteokbokki',ic:'🌶',re:/떡볶이|분식|tteok|bunsik|rice cake/i},
 {k:'칼국수',e:'kalguksu noodles',s:'Noodles',ic:'🍜',re:/칼국수|국수|noodle|kalguksu|guksu/i},
 {k:'냉면',e:'naengmyeon cold noodles',s:'Cold noodles',ic:'🥢',re:/냉면|naengmyeon|cold noodle/i},
 {k:'비빔밥',e:'bibimbap',s:'Bibimbap',ic:'🍚',re:/비빔밥|bibimbap/i},
 {k:'고기구이',e:'Korean BBQ',s:'Korean BBQ',ic:'🥩',re:/고기|삼겹|갈비|바비큐|bbq|barbecue|samgyeop|galbi/i},
 {k:'치킨',e:'Korean fried chicken',s:'Fried chicken',ic:'🍗',re:/치킨|chicken/i},
 {k:'만두',e:'mandu dumplings',s:'Dumplings',ic:'🥟',re:/만두|dumpling|mandu/i},
 {k:'국밥',e:'gukbap soup',s:'Gukbap soup',ic:'🍲',re:/국밥|해장국|설렁탕|곰탕|gukbap/i},
 {k:'카페',e:'cafe',s:'Café',ic:'☕',re:/카페|커피|cafe|café|coffee/i},
 {k:'빙수',e:'bingsu dessert',s:'Bingsu',ic:'🍧',re:/빙수|디저트|bingsu|dessert/i},
 {k:'빵집',e:'bakery',s:'Bakery',ic:'🥐',re:/빵|베이커리|bakery|bread/i},
 {k:'채식 식당',e:'vegetarian restaurant',s:'Vegetarian',ic:'🥗',re:/채식|비건|vegan|vegetarian/i}];
const FASK=/어디|추천|맛집|잘하는|유명한|가볼|찾아|근처|where|recommend|best|good (place|spot|one)|nearby|around here/i;
const FGEN=/맛집|밥집|식당|뭐 ?먹|먹을 ?(곳|데)|배고|where.*\beat\b|\beat\b.*where|restaurant|hungry|good food/i;
const AREAKO={myd:'명동',cath:'명동',cable:'명동',ntower:'남산',gbk:'경복궁',guard:'광화문',geun:'경복궁',gyeong:'경복궁',bukchon:'북촌',insa:'인사동',gwangjang:'광장시장',cheong:'청계천',ddp:'동대문',hongdae:'홍대',hangang:'여의도',hbus:'여의도',starfield:'코엑스',bongeun:'코엑스',lotte:'잠실'};
let FD=null,FW=null,FDQ=null;const GM={p:null,fail:false};
function fdCity(){const sc=SCN[curId];const c=sc&&sc.b==='seoul'&&sc.o?sc.o.city:((/^r_(\w+)/.exec(curId||'')||[])[1]);return c&&CITY[c]?c:null;}
function fdCenter(c){const t=SN>1?me.ni/(SN-1):0;let best=null,bd=9;for(const s of (CITY[c].sights||[])){const r=REAL[s.id];if(!r||!r.ll)continue;const d=Math.abs(s.t-t);if(d<bd){bd=d;best={id:s.id,n:r.n,ll:r.ll};}}return best;}
function foodQ(q){const c=fdCity();if(!c)return null;const f=FOODS.find(x=>x.re.test(q));if(f&&(FASK.test(q)||FGEN.test(q)))return {f,c};if(!f&&FGEN.test(q))return {f:null,c};return null;}
function foodReply(n,fq){const ctr=fdCenter(fq.c),an=ctr?ctr.n:SCN[curId].name;
 if(!fq.f)return L('What would you like to eat? Pick one below and I will check Google Maps ratings nearby.','뭐 드시고 싶어요? 아래에서 고르면 근처 맛집을 구글 지도 별점으로 찾아 드릴게요.');
 return L('Let me check Google Maps ratings for '+fq.f.e+' around '+an+'!',an+' 근처 '+fq.f.k+' 맛집, 구글 지도 별점으로 찾아볼게요!');}
function foodGo(n,fq){if(!fq.f){const qk=$('talkQuick');qk.innerHTML='';FOODS.forEach(f=>{const b=document.createElement('button');b.type='button';b.textContent=f.ic+' '+L(f.s,f.k);b.onclick=()=>ask(L('Good '+f.e+' place nearby?',f.k+' 맛집 어디예요?'));qk.append(b);});return;}
 const ctr=fdCenter(fq.c);if(!ctr)return;setTimeout(()=>fdOpen(fq.f,ctr,n.name),450);}
function fdKo(ctr,f){return ((AREAKO[ctr.id]||'')+' '+f.k).trim();}
function fdBounds(ll,m){const dl=m/111320,dg=m/(111320*Math.cos(ll[0]*Math.PI/180));return {north:ll[0]+dl,south:ll[0]-dl,east:ll[1]+dg,west:ll[1]-dg};}
function fdLL(pl){const o=pl&&pl.location;if(!o)return null;const la=typeof o.lat==='function'?o.lat():o.lat,ln=typeof o.lng==='function'?o.lng():o.lng;return isFinite(la)&&isFinite(ln)?[+la,+ln]:null;}
function fdDist(a,b){const R=6371000,r=Math.PI/180,dl=(b[0]-a[0])*r,dg=(b[1]-a[1])*r;const x=Math.sin(dl/2)**2+Math.cos(a[0]*r)*Math.cos(b[0]*r)*Math.sin(dg/2)**2;return 2*R*Math.asin(Math.sqrt(x));}
function fdSV(ll){return GCFG.gmapsKey&&GCFG.gmapsBilling?'https://www.google.com/maps/embed/v1/streetview?key='+encodeURIComponent(GCFG.gmapsKey)+'&location='+ll[0]+','+ll[1]+'&fov=80&language='+LANG:SVE(ll);}
function gmLoad(){if(GM.p)return GM.p;
 GM.p=new Promise((res,rej)=>{const ok=()=>{try{google.maps.importLibrary('places').then(res,rej);}catch(e){rej(e);}};
  if(window.google&&google.maps&&google.maps.importLibrary)return ok();
  window.__gmReady=ok;window.gm_authFailure=()=>{GM.fail=true;document.querySelectorAll('#panB .gbox').forEach(x=>{if(FDQ&&FDQ.f&&FDQ.ctr)fdNoKey(x,FDQ.f,FDQ.ctr,fdKo(FDQ.ctr,FDQ.f),true);else{x.className='gbox off';x.textContent=L('Google Maps could not load right now. Use the map buttons.','지금 구글 지도를 불러오지 못했어요. 지도 버튼을 써 주세요.');}});};
  const s=document.createElement('script');s.async=true;s.src='https://maps.googleapis.com/maps/api/js?key='+encodeURIComponent(GCFG.gmapsKey)+'&v=weekly&loading=async&language='+(LANG==='ko'?'ko':'en')+'&region=KR&callback=__gmReady';
  s.onerror=()=>rej(new Error('load'));document.head.append(s);setTimeout(()=>rej(new Error('timeout')),15000);});
 GM.p.catch(()=>{GM.fail=true;});return GM.p;}
function fdA(box,t,u){const x=document.createElement('a');x.href=u;x.target='_blank';x.rel='noopener';x.textContent=t;box.append(x);return x;}
function fdLinks(ko,P,f){const d=document.createElement('div');d.className='ocb fdl';
 if(P)fdA(d,'🗺 '+L('Google Maps directions (transit)','구글 지도 길찾기 (대중교통)'),'https://www.google.com/maps/dir/?api=1&destination='+encodeURIComponent(f.k)+'&destination_place_id='+encodeURIComponent(P.id)+'&travelmode=transit');
 fdA(d,'🟢 '+L('Naver Map · menus & prices','네이버 지도 · 메뉴·가격'),'https://map.naver.com/p/search/'+encodeURIComponent(ko));
 fdA(d,'🟡 '+L('Kakao Map','카카오맵'),'https://map.kakao.com/link/search/'+encodeURIComponent(ko));
 const s=document.createElement('small');s.className='fdn';s.textContent=L('Map apps open in a new window. Naver and Kakao show their own results for “'+ko+'”.','지도 앱은 새 창으로 열려요. 네이버·카카오는 “'+ko+'” 검색 결과를 보여 줘요.');d.append(s);return d;}
function fdOpen(f,ctr,who){FDQ={f,ctr,who};const ko=fdKo(ctr,f),live=!!GCFG.gmapsKey&&!GM.fail;
 openPanel(L('Google Maps picks nearby','구글 지도 별점 추천'),b=>{
  const p=document.createElement('p');p.className='lead';
  p.textContent=f.ic+' '+(live?L(f.s+' near '+ctr.n+' — places rated 4★ or more on Google Maps. Tap one and I will lead you there in Virtual Seoul.',ctr.n+' 근처 '+f.k+' — 구글 지도 별점 4점 이상인 곳이에요. 하나를 누르면 메타버스 안에서 그곳까지 길을 이어 드려요.'):L(f.s+' near '+ctr.n+' on Google Maps.',ctr.n+' 근처 '+f.k+' — 구글 지도 별점으로 보여 드릴게요.'));b.append(p);
  const box=document.createElement('div');box.className='gbox';b.append(box);
  if(live)fdSearch(box,f,ctr,4);else fdNoKey(box,f,ctr,ko,false);
  b.append(fdLinks(ko,null,f));});}
async function fdSearch(box,f,ctr,minR){box.className='gbox';box.innerHTML='<div class="gwait">'+L('Loading Google Maps…','구글 지도 불러오는 중…')+'</div>';
 try{await gmLoad();}catch(e){fdNoKey(box,f,ctr,fdKo(ctr,f),true);return;}
 if(!box.isConnected)return;
 const ps=document.createElement('gmp-place-search'),rq=document.createElement('gmp-place-text-search-request');ps.setAttribute('selectable','');
 rq.textQuery=LANG==='ko'?f.k:f.e;rq.locationRestriction=fdBounds(ctr.ll,1000);rq.maxResultCount=5;if(minR)rq.minRating=minR;
 const at=document.createElement('gmp-place-attribution');at.setAttribute('light-scheme-color','gray');at.setAttribute('dark-scheme-color','white');
 ps.append(rq,document.createElement('gmp-place-all-content'),at);let done=false;
 ps.addEventListener('gmp-load',()=>{done=true;const w=box.querySelector('.gwait');if(w)w.remove();
  if(!(ps.places&&ps.places.length)){if(minR)fdSearch(box,f,ctr,0);else box.insertAdjacentHTML('afterbegin','<div class="gwait">'+L('No places found nearby. Try the map buttons below.','근처에서 찾지 못했어요. 아래 지도 버튼을 써 보세요.')+'</div>');}});
 ps.addEventListener('gmp-select',e=>{const pl=e.place;if(pl)fdPick(pl,f,ctr);});
 ps.addEventListener('gmp-error',()=>{GM.fail=true;fdNoKey(box,f,ctr,fdKo(ctr,f),true);});
 box.append(ps);
 setTimeout(()=>{if(!done&&box.isConnected){const w=box.querySelector('.gwait');if(w)w.textContent=L('Google Maps is slow right now. You can use the map buttons below.','구글 지도가 늦어요. 아래 지도 버튼을 써도 돼요.');}},10000);}
function fdNoKey(box,f,ctr,ko,failed){box.className='gbox off';box.innerHTML='';
 const p=document.createElement('p');p.textContent=(failed?L('Google Maps could not load here right now. ','지금은 구글 지도를 여기서 불러오지 못했어요. '):'')+L('Open the map: tap a red pin to see its Google stars and reviews.','지도를 열고 빨간 핀을 누르면 그 가게의 구글 별점과 후기가 보여요.');box.append(p);
 const r=document.createElement('div');r.className='ocb';const bt=document.createElement('button');bt.type='button';bt.className='pri';bt.textContent='⭐ '+L('See Google Maps ratings','구글 지도 별점 보기');bt.onclick=()=>openEmbed(MAPE(ko),MAPQ(ko));r.append(bt);box.append(r);
 const s=document.createElement('small');s.textContent=L('Walking there together inside Virtual Seoul turns on when Google Maps is connected to this site.','메타버스 안에서 그 가게까지 길을 이어 주는 기능은 이 사이트에 구글 지도가 연결되면 켜져요.');box.append(s);}
function fdPick(pl,f,ctr){const ll=fdLL(pl);if(!ll||SN<12)return;fdClear();closePanel();closeTalk();
 const d=fdDist(ctr.ll,ll),k=Math.round(Math.max(14,Math.min(70,d*.09))),fwd=SN-5-me.ni,back=me.ni-4;
 const dir=fwd>=k?1:back>=k?-1:(fwd>=back?1:-1),kk=Math.max(4,Math.min(k,dir>0?fwd:back)),ti=Math.max(2,Math.min(SN-3,me.ni+dir*kk));
 const side=(ll[1]>=ctr.ll[1])?1:-1; /* 실제로 동쪽이면 오른쪽에 둠 — 메타버스 배치는 대략적인 표현 */
 const a=S[ti-1],b=S[ti+1],tx=b.x-a.x,tz=b.z-a.z,tl=Math.hypot(tx,tz)||1,s0=S[ti];
 const pos={x:s0.x-tz/tl*side*3.2,y:s0.y,z:s0.z+tx/tl*side*3.2};
 const g=new T.Group();g.userData.pass=1;
 const beam=new T.Mesh(new T.CylinderGeometry(.75,.75,28,18,1,true),new T.MeshBasicMaterial({color:'#ffc23a',transparent:true,opacity:.45,depthWrite:false,side:T.DoubleSide}));beam.position.set(pos.x,pos.y+14,pos.z);g.add(beam);
 const core=new T.Mesh(new T.CylinderGeometry(.16,.16,28,8),new T.MeshBasicMaterial({color:'#fff6c8',transparent:true,opacity:.85,depthWrite:false}));core.position.copy(beam.position);g.add(core);
 const ring=new T.Mesh(new T.RingGeometry(1,1.35,40),new T.MeshBasicMaterial({color:'#ffcf33',transparent:true,opacity:.9,side:T.DoubleSide,depthWrite:false}));ring.rotation.x=-Math.PI/2;ring.position.set(pos.x,pos.y+.06,pos.z);g.add(ring);
 const lab=label(g,L('⭐ Google pick','⭐ 구글 추천 맛집'),pos.x,pos.y+4.4,pos.z,0,3.6,'#1d1915','#ffd34d');
 const chev=[];for(let i=me.ni+dir*2;dir>0?i<ti-1:i>ti+1;i+=dir*2){const p0=S[i],p1=S[Math.max(0,Math.min(SN-1,i+dir))];
  const cm=new T.Mesh(new T.CircleGeometry(.55,3),new T.MeshBasicMaterial({color:'#ffc23a',transparent:true,opacity:.9,depthWrite:false}));cm.geometry.rotateX(-Math.PI/2);cm.position.set(p0.x,p0.y+.12,p0.z);cm.renderOrder=2;cm.rotation.y=Math.atan2(-(p1.z-p0.z),p1.x-p0.x);g.add(cm);chev.push(cm);}
 cur.g.add(g);const min=Math.max(1,Math.round(d*1.3/75));
 const sp={x:pos.x,z:pos.z,y:pos.y,r:4.6,b:'⭐ '+L('Google pick','구글 추천 맛집'),s:L('Look · menu · real directions','구경 · 메뉴 · 실제 길찾기'),fn:()=>fdArrive(true)};cur.spots.push(sp);
 FD={cur,g,pos,place:{id:pl.id,ll},f,ctr,d,min,ti,ring,lab,chev,sp,arrived:false};
 say(L('Follow the golden light! In real life it is about '+Math.round(d)+' m from '+ctr.n+' in a straight line, around '+min+' min on foot.','노란 빛 기둥을 따라가세요! 실제로는 '+ctr.n+'에서 직선 약 '+Math.round(d)+'m, 걸어서 '+min+'분쯤이에요.'),FDQ&&FDQ.who);
 FW={i:ti,dir};setAuto(true);ctxKey='';updCtx();requestAnimationFrame(fdTick);}
function fdTick(){if(!FD)return;if(FD.cur!==cur||!FD.g.parent){FD=null;return;}const tt=performance.now()/1000;
 FD.ring.scale.setScalar(1+.12*Math.sin(tt*3));FD.lab.lookAt(cam.position.x,FD.lab.position.y,cam.position.z);
 FD.chev.forEach((c,i)=>{c.material.opacity=.45+.55*Math.max(0,Math.sin(tt*4-i*.7));});
 if(!FD.arrived&&Math.hypot(me.x-FD.pos.x,me.z-FD.pos.z)<4.4)fdArrive();requestAnimationFrame(fdTick);}
function fwDone(){FW=null;setAuto(false);if(FD){me.ry=Math.atan2(-(FD.pos.x-me.x),-(FD.pos.z-me.z));camYaw=me.ry;fdArrive();}}
function fdArrive(force){if(!FD)return;if(FD.arrived&&!force)return;FD.arrived=true;if(auto){FW=null;setAuto(false);}
 const P=FD.place,f=FD.f,ctr=FD.ctr,ko=fdKo(ctr,f);
 openPanel(L('Arrived · Google pick','도착 · 구글 추천 맛집'),b=>{
  const p=document.createElement('p');p.className='lead';p.textContent=L('In real life this place is about '+Math.round(FD.d)+' m from '+FD.ctr.n+' in a straight line (about '+FD.min+' min on foot). Inside Virtual Seoul the walk is shortened.','실제로는 '+FD.ctr.n+'에서 직선 약 '+Math.round(FD.d)+'m (걸어서 '+FD.min+'분쯤) 떨어진 곳이에요. 메타버스 안에서는 거리를 줄여서 보여 드려요.');b.append(p);
  const box=document.createElement('div');box.className='gbox';b.append(box);fdDetails(box,P.id,true);
  const r=document.createElement('div');r.className='ocb';const btn=(t,fn,pri)=>{const x=document.createElement('button');x.type='button';x.textContent=t;if(pri)x.className='pri';x.onclick=fn;r.append(x);return x;};
  btn('👀 '+L('Look at the real storefront (Street View)','실제 가게 앞 구경 (거리뷰)'),()=>openEmbed(fdSV(P.ll),'https://www.google.com/maps/@?api=1&map_action=pano&viewpoint='+P.ll[0]+','+P.ll[1]),1).className+=' fdsv';
  btn('📋 '+L('Menu · photos · reviews','메뉴·사진·후기'),()=>fdMore()).className+=' fdmn';
  btn('↩ '+L('Another place','다른 곳 추천받기'),()=>fdOpen(f,ctr,FDQ&&FDQ.who));
  btn('✕ '+L('Clear the route','길 표시 지우기'),()=>{fdClear();closePanel();});b.append(r);
  const h=document.createElement('h4');h.className='fdh';h.textContent='🧭 '+L('Real directions','실제로 가는 길');b.append(h,fdLinks(ko,P,f));});}
async function fdDetails(box,id,compact){
 if(!GCFG.gmapsKey||GM.fail){box.className='gbox off';box.textContent=L('The Google place card is not available right now. Use the buttons below.','지금은 구글 가게 카드를 불러올 수 없어요. 아래 버튼을 써 주세요.');return;}
 box.innerHTML='<div class="gwait">'+L('Loading Google Maps…','구글 지도 불러오는 중…')+'</div>';
 try{await gmLoad();}catch(e){box.className='gbox off';box.textContent=L('Google Maps could not load right now.','지금 구글 지도를 불러오지 못했어요.');return;}
 if(!box.isConnected)return;
 const el=document.createElement(compact?'gmp-place-details-compact':'gmp-place-details'),rq=document.createElement('gmp-place-details-place-request');if(compact)el.setAttribute('orientation','vertical');
 rq.place=id;el.append(rq,document.createElement('gmp-place-all-content'));
 el.addEventListener('gmp-load',()=>{const w=box.querySelector('.gwait');if(w)w.remove();});
 el.addEventListener('gmp-error',()=>{box.className='gbox off';box.textContent=L('Google Maps could not load this place.','구글 지도에서 이 가게를 불러오지 못했어요.');});box.append(el);}
function fdMore(){if(!FD)return;const P=FD.place,f=FD.f,ko=fdKo(FD.ctr,f);
 openPanel(L('Menu · photos · reviews','메뉴·사진·후기'),b=>{
  const p=document.createElement('p');p.className='lead';p.textContent=L('Full menus are most accurate in Google Maps or Naver Map, so they open there. The photos and reviews below come from Google Maps.','메뉴판 전체는 구글 지도나 네이버 지도에서 보는 게 가장 정확해서 그쪽으로 열어요. 아래 사진·후기는 구글 지도 정보예요.');b.append(p);
  const r=document.createElement('div');r.className='ocb fdl';fdA(r,'📋 '+L('Menu on Google Maps','구글 지도에서 메뉴 보기'),'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(f.k)+'&query_place_id='+encodeURIComponent(P.id));fdA(r,'🟢 '+L('Menus & prices on Naver Map','네이버 지도에서 메뉴·가격'),'https://map.naver.com/p/search/'+encodeURIComponent(ko));b.append(r);
  const box=document.createElement('div');box.className='gbox';b.append(box);fdDetails(box,P.id,false);
  const bk=document.createElement('div');bk.className='ocb';const x=document.createElement('button');x.type='button';x.textContent='↩ '+L('Back','돌아가기');x.onclick=()=>fdArrive(true);bk.append(x);b.append(bk);});}
function fdClear(){if(!FD)return;const o=FD;FD=null;if(FW){FW=null;if(auto)setAuto(false);}if(o.g.parent)o.g.parent.remove(o.g);disposeG(o.g);
 if(o.cur===cur){const i=cur.spots.indexOf(o.sp);if(i>=0)cur.spots.splice(i,1);ctxKey='';updCtx();}}
