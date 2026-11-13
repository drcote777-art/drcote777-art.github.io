/* ---------- 가게와 연결 (O2O): NPC 대화 → 상품·쿠폰·예약 카드 → 쿠폰함·캘린더 ----------
   partner: 'demo' 시범 가게(가상, 전송 안 함) · 'none' 실제 가게(제휴 전: 지도 연결만) · 'live' 제휴 가게(window.O2O_URL 로 전송) */
const SHOPS={
 demo:{id:'demo',partner:'demo',name:L('K-Goods Studio (demo shop)','K-굿즈 공방 (시범 가게)'),owner:L('Owner Hana','사장님 하나'),
  items:[{id:'g1',e:'📔',n:L('Hanji notebook','한지 공책'),p:9000,d:L('Handmade from Korean mulberry paper, 80 pages','닥나무 한지로 만든 공책, 80쪽')},
   {id:'g2',e:'🎐',n:L('Norigae charm','노리개 장식'),p:15000,d:L('Traditional knotted tassel for your bag','가방에 다는 전통 매듭 장식')},
   {id:'g3',e:'🍵',n:L('Celadon tea cup','청자 찻잔'),p:28000,d:L('Jade-green glaze, gift box included','비색 유약, 선물 상자 포함')},
   {id:'g4',e:'🖌',n:L('Calligraphy name class · 30 min','내 이름 붓글씨 체험 · 30분'),p:20000,d:L('Write your name in Korean with a brush','붓으로 한글 이름 쓰기'),book:1}],
  coupon:{t:L('10% off your first purchase','첫 구매 10% 할인'),code:'SEOUL-DEMO10',days:30},
  book:{t:L('Calligraphy name class','붓글씨 체험'),times:['11:00','14:00','16:00'],max:6}},
 kyoja:{id:'kyoja',partner:'none',name:'Myeongdong Kyoja · 명동교자',q:'명동교자 본점'}};
const SHOPN={o2o_demo:'demo',eat_myd_w:'kyoja'};
const WK='seoul_wallet';let WAL=LS.get(WK,null)||{cp:[],bk:[],wish:[]};function walSave(){LS.set(WK,WAL);}
const O2O={url:window.O2O_URL||'',async send(type,sh,data){const rec=Object.assign({id:type[0]+Date.now().toString(36),type,shop:sh.id,shopName:sh.name,at:Date.now(),demo:sh.partner!=='live'||!this.url},data);
  if(!rec.demo){try{const r=await fetch(this.url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(rec)});rec.sent=r.ok;}catch(e){rec.sent=false;}}
  (type==='coupon'?WAL.cp:type==='wish'?WAL.wish:WAL.bk).unshift(rec);walSave();return rec;}};
/* 대화 맥락: 손님 말에서 하려는 일을 찾아요 */
const OI={book:/예약|자리|체험|수업|book|reserv|class|table/i,coupon:/쿠폰|할인|coupon|discount|deal/i,pick:/주문|포장|픽업|order|pick ?up|take ?out/i,price:/얼마|가격|price|how much|cost/i,menu:/메뉴|뭐 ?팔|상품|추천|인기|뭐가 좋|menu|recommend|popular|sell|best/i,where:/어디|위치|영업|몇 ?시|where|location|hours|open/i};
function o2oIntent(q){return Object.keys(OI).filter(k=>OI[k].test(q));}
function o2oOpen(n){if(!n.shop&&SHOPN[n.id])n.shop=SHOPN[n.id];const sh=SHOPS[n.shop];if(!sh)return;n.cx=n.cx||{seen:0,cp:false};
 if(sh.partner==='demo')oCard(null,L('Demo shop · nothing here is sent to a real shop','시범 가게 · 여기서 하는 일은 실제 가게로 전송되지 않아요'),'info');
 else if(sh.partner==='none')oCard(null,L('Not a partner of this app yet · booking and coupons are not available here','이 앱과 제휴 전인 가게 · 여기서는 예약·쿠폰이 안 돼요'),'info',mapActs(sh));}
function o2oPrompt(n){const sh=SHOPS[n.shop];if(!sh)return'';
 if(sh.partner==='none')return '[이 앱과 가게의 관계] '+sh.name+'은(는) 이 앱과 제휴하지 않은 실제 가게다. 이 앱에서는 예약·쿠폰·주문을 할 수 없고, 게임 속 메뉴 가격은 예시다. 실제 예약 가능 여부·영업시간·가격은 모른다고 말하고 지도 앱에서 확인하라고 안내한다. 예약을 물으면 대답 끝에 [[book]], 위치나 영업시간을 물으면 [[map]]을 붙인다.\n';
 return '[가게 자료 — 이것만 사실로 말한다] '+sh.name+'은(는) 이 앱의 시범 가게(가상)다. 물으면 솔직히 시범 가게라고 말한다.\n상품: '+sh.items.map(i=>i.id+' '+i.n+' '+i.p+'원 ('+i.d+')').join(' / ')+'\n쿠폰: '+sh.coupon.t+' (시범)\n예약: '+sh.book.t+' '+sh.book.times.join('·')+', 최대 '+sh.book.max+'명\n규칙: 상품을 소개하면 대답 끝에 [[item:상품id]]를, 쿠폰을 주면 [[coupon]]을, 예약 이야기면 [[book]]을, 픽업 주문이면 [[pick]]을 붙인다. 태그는 대답 맨 끝에만, 꼭 필요할 때만 쓴다.\n';}
function o2oStrip(t){return String(t).replace(/\[\[[^\]]*\]\]/g,'').replace(/\[\[[^\]]*$/,'');}
function o2oParse(a){const tags=[];String(a).replace(/\[\[(item|coupon|book|pick|map)(?::([\w-]+))?\]\]/g,(m,k,v)=>{tags.push([k,v||'']);return'';});return {text:o2oStrip(a).trim(),tags};}
function o2oLocal(n,q){const sh=SHOPS[n.shop];if(!sh)return'';const it=o2oIntent(q);
 if(sh.partner==='none'){if(it.includes('book')||it.includes('coupon')||it.includes('pick'))return L("This app can't book or order at this restaurant yet (not a partner). Please check a map app for real booking options.",'이 앱에서는 아직 이 가게 예약·주문이 안 돼요(제휴 전). 실제 예약 가능 여부는 지도 앱에서 확인해 주세요.');if(it.includes('where'))return L('Please check the location and opening hours on the map.','위치와 영업시간은 지도에서 확인해 주세요.');return '';}
 if(it.includes('book'))return L('The calligraphy class runs at 11:00, 14:00 and 16:00. Pick a date and group size on the card below.','붓글씨 체험은 11시·14시·16시에 있어요. 아래 카드에서 날짜와 인원을 골라 주세요.');
 if(it.includes('coupon'))return L('First time here? Take this 10% coupon and save it in your wallet.','처음 오셨죠? 10% 쿠폰 드릴게요. 쿠폰함에 저장해 두세요.');
 if(it.includes('pick'))return L('Order now and pick it up at the shop. You pay when you pick it up.','미리 주문하고 가게에서 찾아가세요. 결제는 찾을 때 해요.');
 if(it.includes('price')||it.includes('menu'))return L('Our bestseller is the hanji notebook. Here is what we have today.','제일 인기는 한지 공책이에요. 오늘 있는 물건 보여 드릴게요.');
 if(it.includes('where'))return L('This is a demo shop, so it has no real address yet.','시범 가게라 아직 실제 주소는 없어요.');
 return '';}
function o2oAfter(n,q,tags){const sh=SHOPS[n.shop];if(!sh)return;const it=new Set(o2oIntent(q));tags.forEach(([k])=>it.add(k==='item'?'menu':k==='map'?'where':k));
 if(sh.partner==='none'){if(['book','coupon','pick','where','menu','price'].some(k=>it.has(k)))oCard(L('Real booking, menu and hours','실제 예약·메뉴·영업시간'),L('This restaurant is not a partner of this app yet. The menu prices in the game are examples. Check the real information in a map app.','이 가게는 이 앱과 제휴 전이에요. 게임 속 메뉴 가격은 예시예요. 실제 정보는 지도 앱에서 확인하세요.'),'info',mapActs(sh));return;}
 const ids=tags.filter(t=>t[0]==='item'&&t[1]).map(t=>t[1]),showItems=ids.length||it.has('menu')||it.has('price');
 if(showItems)itemCard(sh,ids);if(it.has('coupon'))couponCard(sh);if(it.has('book'))bookCard(sh);if(it.has('pick'))pickCard(sh);
 if(showItems)n.cx.seen++;
 if(n.cx.seen>=2&&!n.cx.cp&&!it.has('coupon')&&!WAL.cp.some(c=>c.shop===sh.id)){n.cx.cp=true;setTimeout(()=>{if(talkN!==n)return;addLine(n.name,L('You seem to like our things! Here is a first-visit coupon.','마음에 드시나 봐요! 첫 방문 쿠폰 드릴게요.'));couponCard(sh);},900);}}
/* 카드 */
function oCard(title,body,kind,acts){const d=document.createElement('div');d.className='oc'+(kind?' oc-'+kind:'');if(title){const h=document.createElement('h4');h.textContent=title;d.append(h);}if(body){if(typeof body==='string'){const p=document.createElement('p');p.textContent=body;d.append(p);}else d.append(body);}if(acts&&acts.length){const r=document.createElement('div');r.className='ocb';acts.forEach(a=>r.append(a));d.append(r);}$('talkBody').append(d);$('talkBody').scrollTop=1e6;return d;}
function oBtn(t,fn,pri){const b=document.createElement('button');b.type='button';b.textContent=t;if(pri)b.className='pri';b.onclick=()=>fn(b);return b;}
function oLink(t,href,fn){const a=document.createElement('a');a.textContent=t;a.href=href;if(fn)a.onclick=(e)=>{e.preventDefault();fn();};else{a.target='_blank';a.rel='noopener';}return a;}
function mapActs(sh){const q=sh.q||sh.name;return [oLink(L('Naver Map','네이버 지도'),'https://map.naver.com/p/search/'+encodeURIComponent(q)),oLink(L('Google Maps','구글 지도'),MAPQ(q),()=>openEmbed(MAPE(q),MAPQ(q)))];}
function itemCard(sh,ids){const list=(ids.length?sh.items.filter(i=>ids.includes(i.id)):sh.items).slice(0,4);if(!list.length)return;const w=document.createElement('div');
 list.forEach(i=>{const r=document.createElement('div');r.className='oci';r.innerHTML='<span class="oce"></span><div><b></b><small></small></div><b class="ocp"></b>';r.children[0].textContent=i.e;r.children[1].children[0].textContent=i.n;r.children[1].children[1].textContent=i.d;r.children[2].textContent='₩'+i.p.toLocaleString();
  const a=document.createElement('div');a.className='ocb';const saved=()=>WAL.wish.some(x=>x.shop===sh.id&&x.item===i.id);
  a.append(oBtn(saved()?L('♥ Saved','♥ 담았어요'):L('♡ Save','♡ 관심 상품'),async b=>{if(saved()){openWallet();return;}await O2O.send('wish',sh,{item:i.id,name:i.n,price:i.p});b.textContent=L('♥ Saved','♥ 담았어요');toast(L('Saved to your wallet','쿠폰함에 담았어요'));}),
   i.book?oBtn(L('📅 Book','📅 예약하기'),()=>bookForm(sh),true):oBtn(L('🛍 Order for pickup','🛍 픽업 주문'),()=>pickForm(sh,i),true));
  const box=document.createElement('div');box.append(r,a);w.append(box);});
 oCard(L('🛍 Today at the shop','🛍 오늘의 상품')+(sh.partner==='demo'?' · '+L('demo','시범'):''),w);}
function couponCard(sh){const c=sh.coupon;if(!c)return;const w=document.createElement('div');w.className='cpn';w.innerHTML='<b></b><code></code><small></small>';w.children[0].textContent=c.t;w.children[1].textContent=c.code;w.children[2].textContent=L('Valid '+c.days+' days · demo coupon, not usable in a real shop','받은 날부터 '+c.days+'일 · 시범 쿠폰(실제로는 못 써요)');
 const have=()=>WAL.cp.some(x=>x.shop===sh.id&&x.code===c.code);
 oCard(L('🎫 Coupon','🎫 쿠폰'),w,null,[oBtn(have()?L('✔ In your wallet','✔ 쿠폰함에 있어요'):L('Save to my wallet','쿠폰함에 저장'),async b=>{if(have()){openWallet();return;}await O2O.send('coupon',sh,{code:c.code,title:c.t,exp:Date.now()+c.days*864e5});b.textContent=L('✔ In your wallet','✔ 쿠폰함에 있어요');toast(L('🎫 Coupon saved','🎫 쿠폰을 저장했어요'));},true),oBtn(L('Share','공유'),()=>shareTxt(c.t+' · '+c.code+' · '+sh.name))]);}
function bookCard(sh){if(!sh.book)return;oCard(L('📅 Book: ','📅 예약: ')+sh.book.t,sh.book.times.join(' · ')+L(' · up to '+sh.book.max+' people',' · 최대 '+sh.book.max+'명'),null,[oBtn(L('Choose date and time','날짜·시간 고르기'),()=>bookForm(sh),true)]);}
function pickCard(sh){oCard(L('🛍 Order now, pick up at the shop','🛍 미리 주문하고 가게에서 픽업'),L('You pay at the shop when you pick it up.','결제는 찾을 때 가게에서 해요.'),null,[oBtn(L('Choose an item','상품 고르기'),()=>pickForm(sh,null),true)]);}
/* 고르는 창 */
function seoulDays(n){const out=[],now=Date.now();for(let i=0;i<n;i++){const d=new Date(now+i*864e5);out.push([new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Seoul',year:'numeric',month:'2-digit',day:'2-digit'}).format(d),new Intl.DateTimeFormat(LANG==='ko'?'ko-KR':'en-US',{timeZone:'Asia/Seoul',month:'numeric',day:'numeric',weekday:'short'}).format(d)]);}return out;}
function chips(w,title,opts,fmt,pick,sel){const h=document.createElement('h3');h.textContent=title;w.append(h);const r=document.createElement('div');r.className='ochips';opts.forEach((o,k)=>{const c=document.createElement('button');c.type='button';c.textContent=fmt?fmt(o):o;if(k===sel)c.classList.add('on');c.onclick=()=>{pick(o);[...r.children].forEach(x=>x.classList.toggle('on',x===c));};r.append(c);});w.append(r);}
function sendBtn(w,t,fn){const g=document.createElement('button');g.type='button';g.className='row';g.style.cssText='justify-content:center;background:var(--brass);color:var(--navy);margin-top:12px';g.textContent=t;g.onclick=fn;w.append(g);}
function formLead(w,sh){const p=document.createElement('p');p.className='lead';p.textContent=sh.name+(sh.partner==='demo'?' · '+L('Demo: nothing is sent to a real shop.','시범: 실제 가게로 전송되지 않아요.'):'');w.append(p);}
function bookForm(sh){const b=sh.book;openPanel(L('📅 Book · ','📅 예약 · ')+b.t,(w)=>{const st={d:null,t:null,n:2};formLead(w,sh);
 chips(w,L('Date','날짜'),seoulDays(7),o=>o[1],o=>st.d=o[0]);chips(w,L('Time','시간'),b.times,null,o=>st.t=o);chips(w,L('People','인원'),Array.from({length:b.max},(_,i)=>i+1),o=>o+L('','명'),o=>st.n=o,1);
 sendBtn(w,L('Send booking request','예약 요청 보내기'),async()=>{if(!st.d||!st.t){toast(L('Choose a date and time','날짜와 시간을 골라 주세요'));return;}const rec=await O2O.send('book',sh,{title:b.t,date:st.d,time:st.t,people:st.n,mins:30});closePanel();bookedCard(sh,rec);});});}
function pickForm(sh,item){const its=sh.items.filter(i=>!i.book);openPanel(L('🛍 Order for pickup','🛍 픽업 주문'),(w)=>{const st={i:item||null,d:null,t:null,n:1};formLead(w,sh);
 chips(w,L('Item','상품'),its,o=>o.e+' '+o.n+' ₩'+o.p.toLocaleString(),o=>st.i=o,item?its.indexOf(item):-1);chips(w,L('Pickup date','찾을 날'),seoulDays(3),o=>o[1],o=>st.d=o[0]);chips(w,L('Pickup time','찾을 시간'),['12:00','15:00','18:00'],null,o=>st.t=o);chips(w,L('Quantity','수량'),[1,2,3,4,5],o=>'×'+o,o=>st.n=o,0);
 const pay=document.createElement('p');pay.className='lead';pay.textContent=L('Payment: at the shop when you pick it up (online payment comes after the shop joins).','결제: 찾을 때 가게에서 (온라인 결제는 가게가 제휴한 뒤 연결돼요).');w.append(pay);
 sendBtn(w,L('Send pickup order','픽업 주문 보내기'),async()=>{if(!st.i||!st.d||!st.t){toast(L('Choose an item, date and time','상품·날짜·시간을 골라 주세요'));return;}const rec=await O2O.send('pick',sh,{title:st.i.n,item:st.i.id,price:st.i.p,qty:st.n,date:st.d,time:st.t,mins:15});closePanel();bookedCard(sh,rec);});});}
function bookedCard(sh,rec){const isP=rec.type==='pick',s=(isP?L('Pickup order','픽업 주문'):L('Booking request','예약 요청'))+': '+rec.title+' · '+rec.date+' '+rec.time+(rec.people?' · '+rec.people+L(' people','명'):'')+(rec.qty?' · ×'+rec.qty:'');
 if(talkN)addLine(talkN.name,rec.demo?L('Got it! (Demo — this was not sent to a real shop.)','접수했어요! (시범 — 실제 가게로는 전송되지 않았어요.)'):L('Sent to the shop. They will confirm soon.','가게로 보냈어요. 곧 확인 연락이 갈 거예요.'));
 oCard('✔ '+(isP?L('Pickup order','픽업 주문'):L('Booking','예약'))+(rec.demo?' · '+L('demo','시범'):''),s,'ok',[oBtn(L('📅 Add to calendar','📅 캘린더에 추가'),()=>icsDown(rec),true),oBtn(L('Share','공유'),()=>shareTxt(s+' · '+sh.name)),oBtn(L('🎫 Wallet','🎫 쿠폰함'),openWallet)]);
 if(!talkN)toast('✔ '+s);}
/* 폰으로 가져가기: 캘린더 파일 · 공유 */
function icsDown(rec){const [y,m,d]=rec.date.split('-').map(Number),[hh,mm]=rec.time.split(':').map(Number),s=new Date(Date.UTC(y,m-1,d,hh-9,mm)),e=new Date(s.getTime()+(rec.mins||60)*6e4);
 const f=x=>x.toISOString().replace(/[-:]/g,'').replace(/\.\d+/,''),esc=t=>String(t).replace(/([,;\\])/g,'\\$1').replace(/\n/g,'\\n');
 const ttl=(rec.type==='pick'?L('Pickup: ','픽업: '):'')+rec.title+' · '+rec.shopName+(rec.demo?' ('+L('demo','시범')+')':'');
 const txt=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Virtual Seoul//O2O//EN','BEGIN:VEVENT','UID:'+rec.id+'@virtual-seoul','DTSTAMP:'+f(new Date()),'DTSTART:'+f(s),'DTEND:'+f(e),'SUMMARY:'+esc(ttl),'DESCRIPTION:'+esc(L('Made in Virtual Seoul.','가상 서울에서 만든 일정.')+(rec.demo?' '+L('Demo only — not a real booking.','시범 — 실제 예약이 아니에요.'):'')),'END:VEVENT','END:VCALENDAR'].join('\r\n');
 try{const u=URL.createObjectURL(new Blob([txt],{type:'text/calendar'}));const a=document.createElement('a');a.href=u;a.download='seoul-'+rec.id+'.ics';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),4000);toast(L('Calendar file saved — open it to add','캘린더 파일을 저장했어요 — 열면 추가돼요'));}catch(err){toast(L('Could not make the calendar file','캘린더 파일을 만들지 못했어요'));}
 return txt;}
function shareTxt(t){if(navigator.share){navigator.share({title:'Virtual Seoul',text:t}).catch(()=>{});return;}try{navigator.clipboard.writeText(t);toast(L('Copied','복사했어요'));}catch(e){toast(t);}}
/* 내 쿠폰함 */
function openWallet(){openPanel(L('🎫 My wallet','🎫 내 쿠폰함'),(w)=>{const p=document.createElement('p');p.className='lead';p.textContent=L('Coupons, bookings and saved items from shops. Saved on this device only.','가게에서 받은 쿠폰, 예약, 관심 상품이에요. 이 기기에만 저장돼요.');w.append(p);
 const sec=(t,arr,row)=>{const h=document.createElement('h3');h.textContent=t+' ('+arr.length+')';w.append(h);if(!arr.length){const e=document.createElement('p');e.className='lead';e.textContent=L('None yet','아직 없어요');w.append(e);}arr.forEach(x=>w.append(row(x)));};
 const mk=(main,sub,acts,demo)=>{const r=document.createElement('div');r.className='row';r.style.flexWrap='wrap';const s=document.createElement('span');s.innerHTML='<b style="color:var(--ink);font-weight:400"></b><br><small></small>';s.querySelector('b').textContent=main;s.querySelector('small').textContent=sub+(demo?' · '+L('demo','시범'):'');r.append(s);const a=document.createElement('div');a.className='ocb';a.style.width='100%';acts.forEach(x=>a.append(x));r.append(a);return r;};
 sec(L('Coupons','쿠폰'),WAL.cp,c=>mk(c.title+' · '+c.code,c.shopName+' · '+L('until ','~')+new Date(c.exp).toLocaleDateString(LANG==='ko'?'ko-KR':'en-US'),[oBtn(L('Share','공유'),()=>shareTxt(c.title+' · '+c.code))],c.demo));
 sec(L('Bookings & pickups','예약·픽업'),WAL.bk,k=>mk(k.title+' · '+k.date+' '+k.time,k.shopName,[oBtn(L('📅 Calendar','📅 캘린더'),()=>icsDown(k)),oBtn(L('Share','공유'),()=>shareTxt(k.title+' '+k.date+' '+k.time+' · '+k.shopName)),oBtn(L('Cancel','취소'),()=>{WAL.bk=WAL.bk.filter(x=>x!==k);walSave();openWallet();})],k.demo));
 sec(L('Saved items','관심 상품'),WAL.wish,x=>mk(x.name+' · ₩'+x.price.toLocaleString(),x.shopName,[oBtn(L('Remove','빼기'),()=>{WAL.wish=WAL.wish.filter(y=>y!==x);walSave();openWallet();})],x.demo));});}
/* 명동의 시범 가게 */
function pathAt(t,side,off){const i=Math.max(1,Math.min(SN-2,Math.round(t*(SN-1)))),p=S[i],a=S[i-1],b=S[i+1];let tx=b.x-a.x,tz=b.z-a.z;const l=Math.hypot(tx,tz)||1;tx/=l;tz/=l;const nx=-tz*side,nz=tx*side;return {x:p.x+nx*off,y:p.y,z:p.z+nz*off,nx,nz,face:Math.atan2(-nx,-nz)};}
function o2oStore(c){const sh=SHOPS.demo,g=c.g,t=.24,b=pathAt(t,1,5.6),ry=Math.atan2(b.nx,b.nz);
 box(g,3.4,1.05,1.1,M('#2e5a86'),b.x,b.y,b.z,ry);box(g,3.5,.06,1.2,M('#f4efe2'),b.x,b.y+1.05,b.z,ry);
 for(const s of[-1,1]){const px=b.x-b.nz*s*1.6+b.nx*.9,pz=b.z+b.nx*s*1.6+b.nz*.9;cyl(g,.05,.05,2.7,M('#555'),px,b.y,pz,6);}
 box(g,3.8,.14,2.2,M('#f0c419'),b.x+b.nx*.5,b.y+2.7,b.z+b.nz*.5,ry);label(g,L('K-GOODS · DEMO','K-굿즈 공방 · 시범'),b.x-b.nx*.62,b.y+3.35,b.z-b.nz*.62,Math.atan2(-b.nx,-b.nz),3.6,'#fff','#2b3550');
 sh.items.forEach((i,k)=>{const o=(k-1.5)*.75;box(g,.32,.22,.32,M(['#e8d9b0','#e83a5a','#7fb8a0','#1d1915'][k]),b.x-b.nz*o,b.y+1.11,b.z+b.nx*o);});
 const v=pathAt(t,1,6.7),npc=mkNpc(g,c.npcs,{id:'o2o_demo',shop:'demo',name:sh.owner,role:sh.name,p:'K-굿즈 공방의 밝은 사장님. 한국 전통 공예품을 손님 언어로 소개한다. 이 가게는 이 앱의 시범 가게다.',x:v.x,y:v.y,z:v.z,ry:v.face,cloth:'#2e8fd0',apron:'#f4f6f7',longHair:1,quick:[L('What do you recommend?','추천해 주세요'),L('Any coupons?','쿠폰 있어요?'),L('Book the calligraphy class','붓글씨 체험 예약할래요'),L('Can I order for pickup?','픽업 주문 돼요?')],lines:[L('Welcome! Everything here is handmade in Korea. Ask me anything in your language.','어서 오세요! 전부 한국에서 손으로 만든 거예요. 편한 말로 물어보세요.')]});
 const s=pathAt(t,1,3.2);c.spots.push({x:s.x,z:s.z,y:s.y,r:4.8,b:'🛍 '+sh.name,s:L('Chat with the owner · coupon · booking','사장님과 대화 · 쿠폰 · 예약'),fn:()=>openTalk(npc)});}
