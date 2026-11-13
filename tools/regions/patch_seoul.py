import re,os
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
s=open(S+'cruise_new.html',encoding='utf8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,('COUNT',c,a[:80]);s=s.replace(a,b)
def cut(a,b,new):
    global s
    i=s.index(a);j=s.index(b,i);s=s[:i]+new+s[j:]
M=lambda a,b:"{t:%r,side:%d"%(a,b)
# ---- 돈: 원화 ----
s=s.replace('€','₩').replace('.toFixed(2)','.toLocaleString()').replace('.toFixed(0)','.toLocaleString()')
rep("const G0={eur:300,","const G0={eur:300000,skyMode:'live',")
s=s.replace("cruise_game3","seoul_game1").replace("cruise_stamps","seoul_stamps")
rep('<script>window.WEB_SITE="cruise";</script>','<script>window.WEB_SITE="seoul";</script>')
rep("<title>지중해 크루즈 8일</title>","<title>Virtual Seoul · 가상 서울 3일</title>")
# ---- 언어 ----
rep("/* ---------- 여행 자료 (10/2 최종 일정표 기준) ---------- */",r"""const LANG=(()=>{try{const v=localStorage.getItem('seoul_lang');if(v)return v;}catch(e){}return (navigator.language||'en').toLowerCase().indexOf('ko')===0?'ko':'en';})();
const L=(e,k)=>LANG==='ko'?k:e;
const TRP=[['다음 할 일 ▸','Next ▸'],['다음 날로 ▸','Next day ▸'],['대화하기','Talk'],['🧍 일어나기','🧍 Stand up'],['밖으로 나가기','Go outside'],['타고 이동','Ride'],['승차권 ','Fare '],['실제 사진 · 설명 · 거리뷰','Real photo · facts · Street View'],['설명 · 실제 사진','Facts · real photo'],['앉아서 주문','Sit and order'],['안으로 들어가 먹기','Go in and eat'],['이 자리에 앉기','Sit here'],['바깥 자리에서 주문','Order outside'],['구경하고 사기','Browse and buy'],['젤라토 주문','Order'],['💺 앉기','💺 Sit'],['빈자리','Free seat'],['⏭ 건너뛰기','⏭ Skip'],['바로 도착','Arrive now'],['다음 정류장: ','Next stop: '],[' — 내릴 곳이에요.',' — your stop.'],[' — 정차해요.',' — stopping.'],[' 도착! 내려요.',' — arrived. Getting off.'],['에서 내려요.',': getting off.'],['🚶 ','🚶 '],[' 안으로 들어가요.',': going in.'],['밖으로 나가요.','Going outside.'],['명소 끝까지 걸어가서 찍어요. 일정 버튼으로 바로 갈 수도 있어요.','Walk to the end of this area to stamp.'],['스탬프는 이미 찍었어요.',' stamp is already done.'],[' 스탬프 쾅!',' stamp!'],['찰칵! ','Click! '],['에서 한 장.',''],['가상 유로가 모자라요. 카지노에서 따거나, 가방에서 처음부터 다시 시작할 수 있어요.','Not enough virtual won. Reset from the bag to start over.'],['주문 받았어요. 잠시만요!','coming right up!'],[' 나왔어요. 맛있게 드세요!',' is served. Enjoy!'],['맛있게 먹었어요! ','That was delicious! '],[' 받았어요!',' — here you go!'],['푹 잤어요. 다음 날 아침이에요.','Good morning! A new day in Seoul.'],['둘러본 곳 ','Seen '],['웨이터 ','Server '],['직원','Staff'],['크루','Guide'],['안으로','(go in)'],['샀어요',' bought'],['까지. 차 안을 걸어 다니거나 빈자리에 앉아도 돼요.','. Walk around or take a free seat.'],['에서 ',' → '],[' 승강장으로',' platform']];
const tr=t=>{if(LANG==='ko'||!t)return t;for(const [k,e] of TRP)if(t.indexOf(k)>=0)t=t.split(k).join(e);return t;};
/* ---------- 여행 자료 ---------- */""")
rep("function toast(t){const e=$('toast');e.textContent=t;","function toast(t){const e=$('toast');e.textContent=tr(t);")
rep("function fadeMsg(t,cb){const f=$('fade');$('fadeT').textContent=t;","function fadeMsg(t,cb){const f=$('fade');$('fadeT').textContent=tr(t);")
rep("function say(t,who){const s=$('sub');if(!t){s.classList.add('off');return;}$('subWho').textContent=who||'크루';$('subText').textContent=t;","function say(t,who){const s=$('sub');if(!t){s.classList.add('off');return;}t=tr(t);$('subWho').textContent=tr(who||'크루');$('subText').textContent=t;")
rep("u.lang='ko-KR';","u.lang=LANG==='ko'?'ko-KR':'en-US';")
rep("b.innerHTML='<b>'+x.b+'</b>'+(x.s?'<small>'+x.s+'</small>':'');b.onclick=()=>x.fn(b);a.appendChild(b);","b.innerHTML='<b>'+tr(x.b)+'</b>'+(x.s?'<small>'+tr(x.s)+'</small>':'');b.onclick=()=>x.fn(b);a.appendChild(b);")
rep("$('placeSub').textContent=n?('다음: '+(n.q.t?n.q.t+' ':'')+n.q.n):'오늘 코스 완료! 일정에서 다음 날로';","$('placeSub').textContent=n?(L('Next: ','다음: ')+(n.q.t?n.q.t+' ':'')+n.q.n):L('All done today! Sleep at the hotel for the next day.','오늘 코스 완료! 호텔에서 자면 다음 날이에요.');")
rep("toast('✔ '+DAYS[dayI].q[i].n);","toast('✔ '+DAYS[dayI].q[i].n);")
# ---- 자료 ----
cut("const STAMPS=[","const LS=",r"""const STAMPS=[{id:'myd',name:L('Myeongdong','명동'),date:'D1',c:'#e83a5a'},{id:'nam',name:L('Namsan','남산'),date:'D1',c:'#7fc8a9'},{id:'gbk',name:L('Gyeongbokgung','경복궁'),date:'D2',c:'#d8a05a'},{id:'bkc',name:L('Bukchon·Insadong','북촌·인사동'),date:'D2',c:'#c9a2e3'},{id:'gjm',name:L('Gwangjang·DDP','광장시장·DDP'),date:'D2',c:'#ef8a6a'},{id:'hdc',name:L('Hongdae','홍대'),date:'D3',c:'#8fb4e8'},{id:'hgr',name:L('Han River','한강'),date:'D3',c:'#6fc0d8'},{id:'gng',name:L('Gangnam·Jamsil','강남·잠실'),date:'D3',c:'#e3b860'}];
""")
s=s.replace("'/6</b>'","'/'+STAMPS.length+'</b>'").replace("n===6?","n===STAMPS.length?")
cut("const SCN={","/* 날짜별 할 일",r"""const SCN={
 icn:{b:'airport',o:{},name:L('Incheon Airport T1 · Arrivals','인천공항 1터미널 · 도착')},icnOut:{b:'airport',o:{out:true},name:L('Incheon Airport · Departures','인천공항 · 출국')},
 hotel:{b:'hotel',name:L('Hotel room · Myeongdong','명동 호텔 방')},
 myd:{b:'seoul',o:{city:'myd'},name:L('Myeongdong','명동')},nam:{b:'seoul',o:{city:'nam'},name:L('Namsan · N Seoul Tower','남산 · N서울타워')},
 gbk:{b:'seoul',o:{city:'gbk'},name:L('Gyeongbokgung Palace','경복궁')},bkc:{b:'seoul',o:{city:'bkc'},name:L('Bukchon · Insadong','북촌 · 인사동')},
 gjm:{b:'seoul',o:{city:'gjm'},name:L('Gwangjang Market · Cheonggyecheon · DDP','광장시장 · 청계천 · DDP')},hdc:{b:'seoul',o:{city:'hdc'},name:L('Hongdae','홍대')},
 hgr:{b:'seoul',o:{city:'hgr'},name:L('Yeouido Hangang Park','여의도 한강공원')},gng:{b:'seoul',o:{city:'gng'},name:L('COEX · Lotte World Tower','코엑스 · 롯데월드타워')},
 r_myd:{b:'resto',o:{k:'myd',back:['myd',.4]},name:'Myeongdong Kyoja'},r_bkc:{b:'resto',o:{k:'bkc',back:['bkc',.7]},name:L('Traditional tea house','전통찻집')},
 ride:{b:'ride',name:''}};
const SHIPMAP=[['myd',L('Myeongdong','명동'),L('Line 4','4호선')],['nam',L('Namsan','남산'),L('Cable car','케이블카')],['gbk',L('Gyeongbokgung','경복궁'),L('Line 3','3호선')],['bkc',L('Bukchon·Insadong','북촌·인사동'),L('Anguk, Line 3','3호선 안국')],['gjm',L('Gwangjang·DDP','광장시장·DDP'),L('Jongno 5-ga, Line 1','1호선 종로5가')],['hdc',L('Hongdae','홍대'),L('Line 2','2호선')],['hgr',L('Han River','한강'),L('Yeouinaru, Line 5','5호선 여의나루')],['gng',L('COEX·Jamsil','코엑스·잠실'),L('Line 2 / 9','2·9호선')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')],['icn',L('Airport','인천공항'),'AREX']];

""")
cut("const BF={","/* 메뉴 (게임 속 가상 가격) */",r"""const DAYS=[
 {tag:'DAY 1',title:L('Arrival · Myeongdong · Namsan','도착 · 명동 · 남산'),time:L('Airport → AREX 43 min → Myeongdong → N Seoul Tower night view','공항 → 공항철도 43분 → 명동 → N서울타워 야경'),q:[
  {t:'',n:L('Immigration','입국심사'),sc:'icn',at:.02,a:'immi',r:'icn'},
  {t:'',n:L('Pick up baggage','짐 찾기'),sc:'icn',at:.35,a:'bag'},
  {t:'',n:L('Buy a T-money transit card','티머니 교통카드 사기'),sc:'icn',at:.72,a:'tmoney',r:'tmoney'},
  {t:'',n:L('AREX Express to Seoul Station, Line 4 to Myeongdong','공항철도 직통열차 → 서울역 → 4호선 명동'),sc:'icn',at:1,a:'arex',r:'arex'},
  {t:'',n:L('Walk Myeongdong street','명동 거리 걷기'),sc:'myd',at:.25,near:1,r:'myd'},
  {t:'',n:L('Street food: hotteok or tteokbokki','길거리 음식: 호떡·떡볶이'),sc:'myd',at:.3,a:'eat_st'},
  {t:'',n:L('Myeongdong Cathedral','명동성당'),sc:'myd',at:.5,near:1,r:'cath'},
  {t:'',n:L('Dinner: kalguksu at Myeongdong Kyoja','저녁: 명동교자 칼국수'),sc:'r_myd',at:0,a:'eat_myd',r:'kyoja'},
  {t:'',n:L('Namsan Cable Car','남산 케이블카 타기'),sc:'myd',at:.97,a:'cable',r:'cable'},
  {t:'',n:L('Love locks terrace','사랑의 자물쇠'),sc:'nam',at:.45,near:1},
  {t:'',n:L('N Seoul Tower observatory','N서울타워 전망대'),sc:'nam',at:.6,a:'ntower',r:'ntower'},
  {t:'',n:L('Namsan stamp','남산 스탬프'),sc:'nam',at:.97,a:'stamp'},
  {t:'',n:L('Cable car back down','케이블카로 내려가기'),sc:'nam',at:0,a:'cable2'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Palace · Hanok village · Market','궁궐 · 한옥마을 · 시장'),time:L('Gyeongbokgung (guard ceremony 10:00/14:00) → Bukchon → Insadong → Gwangjang Market → DDP','경복궁(수문장 교대 10:00·14:00) → 북촌 → 인사동 → 광장시장 → DDP'),q:[
  {t:'',n:L('Subway Line 4 → Line 3 to Gyeongbokgung','지하철 4호선 → 3호선 경복궁역'),sc:'myd',at:.02,a:'m_gbk',r:'subway'},
  {t:'',n:L('Buy a palace ticket (free in hanbok)','경복궁 입장권 (한복은 무료)'),sc:'gbk',at:.12,a:'ticket',r:'gbk'},
  {t:'10:00',n:L('Royal guard changing ceremony','수문장 교대의식'),sc:'gbk',at:.2,a:'guard',r:'guard'},
  {t:'',n:L('Geunjeongjeon throne hall','근정전'),sc:'gbk',at:.6,near:1,r:'geun'},
  {t:'',n:L('Gyeonghoeru pavilion','경회루'),sc:'gbk',at:.97,near:1,r:'gyeong'},
  {t:'',n:L('Gyeongbokgung stamp','경복궁 스탬프'),sc:'gbk',at:.97,a:'stamp'},
  {t:'',n:L('Walk to Bukchon Hanok Village','북촌한옥마을로 걸어가기'),sc:'gbk',at:.97,a:'w_bkc'},
  {t:'',n:L('Hanok alley viewpoint','한옥 골목 전망'),sc:'bkc',at:.35,near:1,r:'bukchon'},
  {t:'',n:L('Tea house in Insadong','인사동 전통찻집'),sc:'r_bkc',at:0,a:'eat_bkc',r:'insa'},
  {t:'',n:L('Ssamziegil','쌈지길'),sc:'bkc',at:.88,near:1},
  {t:'',n:L('Bukchon·Insadong stamp','북촌·인사동 스탬프'),sc:'bkc',at:.97,a:'stamp'},
  {t:'',n:L('Line 1 to Jongno 5-ga','1호선 종로5가역'),sc:'bkc',at:.97,a:'m_gjm'},
  {t:'',n:L('Bindaetteok at Gwangjang Market','광장시장 빈대떡'),sc:'gjm',at:.22,a:'eat_gjm',r:'gwangjang'},
  {t:'',n:L('Cheonggyecheon stream','청계천'),sc:'gjm',at:.62,near:1,r:'cheong'},
  {t:'',n:L('DDP at night','DDP 야경'),sc:'gjm',at:.95,near:1,r:'ddp'},
  {t:'',n:L('Gwangjang·DDP stamp','광장시장·DDP 스탬프'),sc:'gjm',at:.97,a:'stamp'},
  {t:'',n:L('Line 4 back to Myeongdong','4호선으로 명동 복귀'),sc:'gjm',at:.97,a:'m_back'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Hongdae · Han River · Gangnam','홍대 · 한강 · 강남'),time:L('Hongdae → Yeouido Hangang Park → COEX → Lotte World Tower → airport','홍대 → 여의도 한강공원 → 코엑스 → 롯데월드타워 → 공항'),q:[
  {t:'',n:L('Line 2 to Hongik University','2호선 홍대입구역'),sc:'myd',at:.02,a:'m_hdc'},
  {t:'',n:L('Watch street busking','버스킹 구경'),sc:'hdc',at:.48,a:'busk',r:'hongdae'},
  {t:'',n:L('Hongdae stamp','홍대 스탬프'),sc:'hdc',at:.97,a:'stamp'},
  {t:'',n:L('Subway to Yeouinaru','지하철로 여의나루역'),sc:'hdc',at:.97,a:'m_hgr'},
  {t:'',n:L('Han River ramen','한강 라면'),sc:'hgr',at:.4,a:'eat_hgr',r:'hangang'},
  {t:'',n:L('Chicken and beer picnic','치킨과 맥주 소풍'),sc:'hgr',at:.6,a:'eat_chi'},
  {t:'',n:L('Hangang Bus pier','한강버스 선착장'),sc:'hgr',at:.85,near:1,r:'hbus'},
  {t:'',n:L('Han River stamp','한강 스탬프'),sc:'hgr',at:.97,a:'stamp'},
  {t:'',n:L('Line 9 to Bongeunsa (COEX)','9호선 봉은사역 (코엑스)'),sc:'hgr',at:.97,a:'m_gng'},
  {t:'',n:L('Starfield Library','별마당도서관'),sc:'gng',at:.25,near:1,r:'starfield'},
  {t:'',n:L('Bongeunsa Temple','봉은사'),sc:'gng',at:.45,near:1,r:'bongeun'},
  {t:'',n:L('Seoul Sky observatory','서울스카이 전망대'),sc:'gng',at:.72,a:'sky',r:'lotte'},
  {t:'',n:L('Gangnam·Jamsil stamp','강남·잠실 스탬프'),sc:'gng',at:.97,a:'stamp'},
  {t:'',n:L('Back to Incheon Airport','인천공항으로'),sc:'gng',at:.02,a:'m_icn'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'icnOut',at:.9,a:'trip'}]}];

""")
MT="ride:{kind:'metro',scen:'tunnel',"
cut("/* 항구별 장소","const CRUISE_INFO=",r"""const mt=(id,t,side,n,line,col,stops,dest,intro)=>({t,side,k:'metro',id,n,fare:1550,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 myd:{noBoard:1,rinfo:'kyoja',spots:[
   mt('m_gbk',.03,1,L('Myeongdong Stn → Gyeongbokgung','명동역 → 경복궁역'),L('Line 4 → Line 3','4호선 → 3호선'),'#f08a1f',[L('Myeongdong','명동'),L('Chungmuro (transfer)','충무로 (환승)'),L('Jongno 3-ga','종로3가'),L('Anguk','안국'),L('Gyeongbokgung','경복궁')],{sc:'gbk',at:0},L('🚇 Line 4 one stop to Chungmuro, transfer to Line 3 (orange), four more stops.','🚇 4호선으로 충무로까지 한 정거장, 3호선(주황색)으로 갈아타 네 정거장.')),
   mt('m_hdc',.06,-1,L('Euljiro 1-ga Stn → Hongdae','을지로입구역 → 홍대입구역'),L('Line 2','2호선'),'#2fae6a',[L('Euljiro 1-ga','을지로입구'),L('City Hall','시청'),L('Sinchon','신촌'),L('Hongik Univ.','홍대입구')],{sc:'hdc',at:0},L('🚇 Line 2 (green) from Euljiro 1-ga, six stops to Hongik University.','🚇 을지로입구역에서 2호선(초록색)으로 여섯 정거장.')),
   st('eat_st',.3,1,L('Street food stall','길거리 음식 노점'),L('Mrs. Kim','김 사장님'),[[L('Hotteok (sweet pancake)','호떡'),3000],[L('Tteokbokki (spicy rice cakes)','떡볶이'),5000],[L('Grilled skewer','닭꼬치'),5000]],'🍢'),
   {t:.4,side:-1,k:'resto',id:'eat_myd',n:'Myeongdong Kyoja',w:L('Jisoo','지수'),menu:{title:'Myeongdong Kyoja · 명동교자',sub:L('Since 1966 · example prices','1966년부터 · 예시 가격'),items:[[L('Kalguksu (knife-cut noodle soup)','칼국수'),11000],[L('Mandu (dumplings)','만두'),13000],[L('Bibim-guksu (spicy cold noodles)','비빔국수'),11000]]}},
   {t:.97,side:1,k:'shuttle',id:'cable',n:L('Namsan Cable Car','남산 케이블카'),fare:15000,ride:{kind:'bus',scen:'country',title:L('Namsan Cable Car','남산 케이블카'),col:'#c8202a',stops:[L('Lower station','아래 승강장'),L('Namsan top','남산 위')],gap:260,vmax:7,intro:L('🚡 Round trip ₩15,000. Open 10:00–23:00.','🚡 왕복 15,000원. 10:00~23:00 운행.'),intro2:L('The cabin glides up over the pine trees. The city spreads out behind you.','캐빈이 소나무 숲 위로 올라가요. 뒤로 도심이 펼쳐져요.'),dest:{sc:'nam',at:0}}}],
  sights:[{t:.2,side:-1,id:'myd'},{t:.52,side:1,id:'cath'},{t:.9,side:-1,id:'cable'}],
  doors:[{t:.1,side:1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  cit:[{t:.34,n:L('Minho','민호'),role:L('Seoul local shopping in Myeongdong','명동에 나온 서울 시민'),p:'명동을 잘 아는 서울 청년. 길거리 음식과 환전, 화장품 가게 이야기를 한다.'},{t:.7,n:L('Yuna','유나'),role:L('University student','대학생'),p:'서울 대학생. 남산 야경과 케이블카 타는 법을 알려 준다.'}]},
 nam:{noBoard:1,spots:[{t:.01,side:1,k:'shuttle',id:'cable2',n:L('Cable car down to Myeongdong','케이블카로 명동으로'),ride:{kind:'bus',scen:'country',title:L('Namsan Cable Car','남산 케이블카'),col:'#c8202a',stops:[L('Namsan top','남산 위'),L('Lower station','아래 승강장')],gap:260,vmax:7,dest:{sc:'myd',at:.1}}},
   st('buy_lock',.42,1,L('Love lock stand','사랑의 자물쇠 가게'),L('Owner','주인'),[[L('Heart lock (small)','하트 자물쇠 (작은 것)'),12000]],'🔒')],
  sights:[{t:.5,side:-1,id:'ntower'}],lifts:[{id:'ntower',y:44,n:L('N Seoul Tower observatory','N서울타워 전망대'),fare:29000,msg:L('The elevator shoots up to the observatory…','엘리베이터가 전망대로 올라가요…'),top:L('Seoul in every direction. The dark ribbon is the Han River.','사방으로 서울이 보여요. 어두운 띠가 한강이에요.')}],
  cit:[{t:.3,n:L('Hyejin','혜진'),role:L('Local on an evening walk','저녁 산책 나온 시민'),p:'남산을 자주 걷는 서울 시민. 해 질 무렵이 가장 예쁘다고 알려 준다.'}]},
 gbk:{noBoard:1,spots:[st('hanbok',.05,-1,L('Hanbok rental','한복 대여점'),L('Owner Park','박 사장님'),[[L('Hanbok rental (2 hours)','한복 대여 (2시간)'),20000]],'👘')],
  sights:[{t:.08,side:1,id:'gbk'},{t:.24,side:-1,id:'guard'},{t:.58,side:1,id:'geun'},{t:.93,side:1,id:'gyeong'}],
  shows:[{id:'guard',t:.2,b:L('💂 Watch the guard ceremony','💂 수문장 교대의식 보기'),s:'10:00 · 14:00',say:L('Drums roll. Guards in red robes march through Gwanghwamun and exchange the gate key box.','북소리가 울려요. 붉은 옷의 수문장들이 광화문을 지나며 교대해요.')}],
  tix:{t:.12,id:'ticket',fare:3000},links:[{t:.985,id:'w_bkc',to:'bkc',at:0,n:L('🚶 Walk to Bukchon','🚶 북촌으로 걸어가기'),s:L('about 10 min','약 10분')}],
  cit:[{t:.4,n:L('Mr. Lee','이 선생님'),role:L('Volunteer palace guide','궁궐 해설 자원봉사자'),p:'경복궁 해설 봉사자. 근정전과 경회루, 수문장 교대의식 시간을 정확히 안내한다.'}]},
 bkc:{noBoard:1,rinfo:'insa',spots:[{t:.7,side:1,k:'resto',id:'eat_bkc',n:L('Tea house','전통찻집'),w:L('Eunji','은지'),menu:{title:L('Traditional tea house','전통찻집'),sub:L('Insadong · example prices','인사동 · 예시 가격'),items:[[L('Omija tea','오미자차'),8000],[L('Jujube tea','대추차'),8000],[L('Rice cake set','떡 모둠'),7000]]}},
   {t:.8,side:-1,k:'stall',id:'buy_ins',n:L('Craft shop','공예품 가게'),w:L('Owner','주인'),items:[[L('Hanji notebook','한지 공책'),8000],[L('Celadon cup','청자 잔'),25000],[L('Norigae charm','노리개'),12000]]},
   mt('m_gjm',.985,1,L('Jongno 3-ga → Jongno 5-ga','종로3가역 → 종로5가역'),L('Line 1','1호선'),'#1f4f91',[L('Jongno 3-ga','종로3가'),L('Jongno 5-ga','종로5가')],{sc:'gjm',at:0},L('🚇 Line 1 (dark blue), one stop. Exit 8 for the market.','🚇 1호선(남색) 한 정거장. 시장은 8번 출구.'))],
  sights:[{t:.3,side:-1,id:'bukchon'},{t:.62,side:-1,id:'insa'}],
  cit:[{t:.2,n:L('Grandma Sun','순이 할머니'),role:L('Bukchon resident','북촌 주민'),p:'북촌에 오래 산 할머니. 주민이 사는 동네라 조용히 다녀 달라고 부드럽게 말한다. 방문 시간은 10시~17시.'},{t:.75,n:L('Dohyun','도현'),role:L('Gallery owner','화랑 주인'),p:'인사동 화랑 주인. 전통차와 공예품을 소개한다.'}]},
 gjm:{noBoard:1,spots:[st('eat_gjm',.22,1,L('Bindaetteok stall','빈대떡집'),L('Auntie','이모'),[[L('Bindaetteok (mung-bean pancake)','녹두빈대떡'),5000],[L('Mayak gimbap (mini rolls)','마약김밥'),4000],[L('Yukhoe (beef tartare)','육회'),19000]],'🥞'),
   {t:.3,side:-1,k:'stall',id:'buy_gj',n:L('Fabric and hanbok shop','원단·한복 가게'),w:L('Owner','주인'),items:[[L('Silk pouch','비단 주머니'),6000],[L('Bojagi wrapping cloth','보자기'),9000]]},
   mt('m_back',.985,1,L('Dongdaemun History & Culture Park → Myeongdong','동대문역사문화공원역 → 명동역'),L('Line 4','4호선'),'#2e8fd0',[L('Dongdaemun Hist. & Culture Park','동대문역사문화공원'),L('Chungmuro','충무로'),L('Myeongdong','명동')],{sc:'myd',at:.1},L('🚇 Line 4 (light blue), two stops to Myeongdong.','🚇 4호선(하늘색) 두 정거장.'))],
  sights:[{t:.12,side:-1,id:'gwangjang'},{t:.62,side:1,id:'cheong'},{t:.9,side:1,id:'ddp'}],
  cit:[{t:.18,n:L('Mr. Choi','최 사장님'),role:L('Market vendor','시장 상인'),p:'광장시장에서 오래 장사한 상인. 빈대떡과 마약김밥, 육회를 추천한다.'}]},
 hdc:{noBoard:1,spots:[st('eat_hd',.2,1,L('Café window','테이크아웃 카페'),L('Barista','바리스타'),[[L('Iced Americano','아이스 아메리카노'),4500],[L('Croffle','크로플'),6000]],'☕'),
   mt('m_hgr',.985,1,L('Hongik Univ. → Yeouinaru','홍대입구역 → 여의나루역'),L('AREX → Line 5','공항철도 → 5호선'),'#8a4fd0',[L('Hongik Univ.','홍대입구'),L('Gongdeok (transfer)','공덕 (환승)'),L('Mapo','마포'),L('Yeouinaru','여의나루')],{sc:'hgr',at:0},L('🚇 One stop to Gongdeok, transfer to Line 5 (purple), two stops across the river.','🚇 공덕까지 한 정거장, 5호선(보라색)으로 갈아타 강 건너 두 정거장.'))],
  sights:[{t:.4,side:-1,id:'hongdae'}],shows:[{id:'busk',t:.48,b:L('🎸 Watch the busking','🎸 버스킹 보기'),s:L('Street performance','거리 공연'),say:L('A band starts a song and people gather in a circle, clapping along.','밴드가 노래를 시작하자 사람들이 둥글게 모여 박수를 쳐요.')}],
  cit:[{t:.55,n:L('Jay','제이'),role:L('Busker','버스커'),p:'홍대에서 거리 공연을 하는 음악가. 홍대의 인디 음악과 공연 시간대를 이야기한다.'}]},
 hgr:{noBoard:1,spots:[st('eat_hgr',.4,1,L('Convenience store ramen','편의점 한강 라면'),L('Clerk','직원'),[[L('Instant ramen (cook it yourself)','즉석 라면 (직접 끓이기)'),4000],[L('Triangle gimbap','삼각김밥'),1500]],'🍜'),
   st('eat_chi',.6,-1,L('Chicken delivery zone','치킨 배달존'),L('Rider','배달 기사'),[[L('Fried chicken','후라이드 치킨'),22000],[L('Beer','맥주'),4000],[L('Cola','콜라'),2500]],'🍗'),
   mt('m_gng',.985,1,L('Yeouido → Bongeunsa (COEX)','여의도역 → 봉은사역 (코엑스)'),L('Line 9','9호선'),'#b8862a',[L('Yeouido','여의도'),L('Express Bus Terminal','고속터미널'),L('Bongeunsa','봉은사')],{sc:'gng',at:0},L('🚇 Line 9 (gold) runs along the south bank to Bongeunsa.','🚇 9호선(황금색)으로 강 남쪽을 따라 봉은사역까지.'))],
  sights:[{t:.15,side:-1,id:'hangang'},{t:.85,side:1,id:'hbus'}],
  cit:[{t:.5,n:L('Seoyeon','서연'),role:L('Picnicking local','소풍 나온 시민'),p:'한강에서 친구들과 치맥을 즐기는 시민. 돗자리와 라면, 한강버스 이야기를 한다.'}]},
 gng:{noBoard:1,spots:[mt('m_icn',.03,-1,L('To Incheon Airport','인천공항으로'),L('Line 2 → AREX','2호선 → 공항철도'),'#f08a1f',[L('Jamsil','잠실'),L('Hongik Univ. (transfer)','홍대입구 (환승)'),L('Incheon Airport T1','인천공항1터미널')],{sc:'icnOut',at:0},L('🚇 Line 2 to Hongik University, then the AREX all-stop train to the airport.','🚇 2호선으로 홍대입구, 공항철도 일반열차로 공항까지.'))],
  sights:[{t:.22,side:1,id:'starfield'},{t:.43,side:-1,id:'bongeun'},{t:.66,side:1,id:'lotte'}],lifts:[{id:'sky',y:70,n:L('Seoul Sky observatory','서울스카이 전망대'),fare:27000,msg:L('The Sky Shuttle elevator rises to the 118th floor in about a minute…','스카이셔틀 엘리베이터가 약 1분 만에 118층으로 올라가요…'),top:L('About 500 m above the ground. On the glass floor you see the street far below.','지상 약 500m예요. 유리 바닥 아래로 거리가 까마득해요.')}],
  cit:[{t:.3,n:L('Daniel','다니엘'),role:L('Office worker in Gangnam','강남 직장인'),p:'강남 직장인. 코엑스 별마당도서관과 봉은사, 롯데월드타워 가는 길을 알려 준다.'}]}};

""")
cut("const CRUISE_INFO=","const NPC_RULES=",r"""const CRUISE_INFO="이 게임은 외국인 여행자가 인천공항에 도착해 2박 3일 동안 서울을 도는 가상 3D 여행이다. 1일: 입국심사·짐 찾기·티머니 카드 → 공항철도 직통열차(13,000원, 인천공항1터미널→서울역 43분, 지정석; 일반열차는 약 4,750원·59분) → 4호선 명동 → 명동 거리·명동성당·명동교자 → 남산 케이블카(왕복 15,000원, 10:00~23:00) → N서울타워 전망대(29,000원, 타워 높이 236.7m). 2일: 경복궁(3,000원, 한복 착용 무료, 화요일 휴궁, 수문장 교대의식 10:00·14:00) → 북촌한옥마을(레드존 방문은 10:00~17:00만) → 인사동 → 광장시장(먹자골목 9~23시쯤) → 청계천 → DDP. 3일: 홍대 → 여의도 한강공원(한강버스 1회 3,000원) → 코엑스 별마당도서관·봉은사 → 롯데월드타워 서울스카이(27,000원, 555m 123층) → 인천공항. 서울 지하철 기본요금은 교통카드 1,550원, 30분 안에 갈아타면 환승. 기후동행카드 단기권은 1일 5,000원·3일 10,000원이지만 공항철도 인천공항 구간에서는 못 쓴다. 게임 속 돈은 가상 원화이고 식당 메뉴 가격은 예시다.";
""")
cut("const NPC_RULES=","\n",r"""const NPC_RULES=LANG==='ko'?"규칙: 한국어 존댓말로, 맡은 사람다운 따뜻한 말투로 2~3문장, 140자 이내로 답한다. 실제 시간·가격·장소는 위 자료에 있는 것만 정확히 말하고, 자료에 없으면 지어내지 말고 모른다고 말한다.":"Rules: Answer in friendly, simple English, 2-3 short sentences, in character. State times, prices and places only from the facts above; if it is not there, say you are not sure instead of inventing it. You may add the Korean name in brackets.";""")
# ---- REAL ----
REAL=r"""const REAL={
 icn:{n:L('Incheon International Airport','인천국제공항'),sub:'ICN · Terminal 1',ll:[37.4492,126.4510],q:'Incheon International Airport Terminal 1',f:[L('After landing: immigration (passport, fingerprints, photo) → baggage claim → customs → arrivals hall.','도착 후: 입국심사(여권·지문·사진) → 짐 찾기 → 세관 → 도착층.'),L('You can file the free e-Arrival Card online before you fly; check the official immigration site for the current rule.','무료 전자입국신고서를 출발 전에 온라인으로 낼 수 있어요. 최신 규정은 공식 누리집에서 확인하세요.'),L('Convenience stores in the arrivals hall sell and top up T-money cards.','도착층 편의점에서 티머니 카드를 사고 충전할 수 있어요.')]},
 tmoney:{n:L('T-money transit card','티머니 교통카드'),sub:'T-money',q:'T-money card',f:[L('The card itself costs about ₩2,500–4,000, then you add credit.','카드값은 약 2,500~4,000원이고 따로 충전해요.'),L('Seoul subway base fare with a card is ₩1,550 (up to 10 km, then ₩100 per 5 km).','서울 지하철 기본요금은 교통카드 1,550원(10km까지, 이후 5km마다 100원).'),L('Tap in and tap out. Transfer within 30 minutes without paying the base fare again.','탈 때와 내릴 때 찍어요. 30분 안에 갈아타면 기본요금을 다시 내지 않아요.'),L('Climate Card short passes: 1 day ₩5,000, 3 days ₩10,000 — not valid on the airport section of AREX.','기후동행카드 단기권: 1일 5,000원, 3일 10,000원 — 공항철도 인천공항 구간에서는 못 써요.')]},
 arex:{n:L('AREX Airport Railroad','공항철도 AREX'),sub:L('Incheon Airport ↔ Seoul Station','인천공항 ↔ 서울역'),ll:[37.5547,126.9707],q:'Seoul Station AREX',f:[L('Express: ₩13,000, non-stop, about 43 minutes from Terminal 1, reserved seats, every 30–50 minutes.','직통열차: 13,000원, 무정차, 1터미널에서 약 43분, 지정석, 30~50분 간격.'),L('All-stop train: about ₩4,750 with a transit card, about 59 minutes, every 5–10 minutes, no reservation.','일반열차: 교통카드 약 4,750원, 약 59분, 5~10분 간격, 예매 없이 탑승.'),L('All-stop stations include Gimpo Airport, Hongik University and Gongdeok.','일반열차는 김포공항, 홍대입구, 공덕 등에 서요.')]},
 subway:{n:L('Seoul Subway','서울 지하철'),sub:L('Lines by number and colour','번호와 색으로 구분'),q:'Seoul Subway',f:[L('Every line has a number and a colour: Line 2 green, Line 3 orange, Line 4 light blue.','노선마다 번호와 색이 있어요: 2호선 초록, 3호선 주황, 4호선 하늘색.'),L('Signs and announcements are in Korean and English.','표지판과 안내 방송은 한국어와 영어로 나와요.'),L('Base fare ₩1,550 with a card. A single-use ticket costs ₩1,650 plus a ₩500 deposit.','교통카드 기본요금 1,550원. 1회용 카드는 1,650원에 보증금 500원.')]},
 myd:{n:L('Myeongdong','명동'),sub:L('Shopping street · Line 4','쇼핑 거리 · 4호선'),ll:[37.5636,126.9850],q:'Myeongdong Shopping Street',f:[L('Seoul\'s best-known shopping street for cosmetics and fashion.','화장품과 패션으로 가장 잘 알려진 쇼핑 거리예요.'),L('Street food stalls line the main street from late afternoon.','오후 늦게부터 큰길에 길거리 음식 노점이 늘어서요.')]},
 cath:{n:L('Myeongdong Cathedral','명동성당'),sub:'1898',ll:[37.5633,126.9873],q:'Myeongdong Cathedral',f:[L('Completed in 1898, it is Korea\'s first brick Gothic church.','1898년에 완성한 한국 최초의 벽돌 고딕 성당이에요.'),L('It is the cathedral of the Archdiocese of Seoul.','천주교 서울대교구의 주교좌 성당이에요.')]},
 kyoja:{n:'Myeongdong Kyoja · 명동교자',sub:L('Kalguksu since 1966','1966년부터 칼국수'),q:'Myeongdong Kyoja',f:[L('Famous for kalguksu (knife-cut noodles in chicken broth) and mandu dumplings.','닭 육수 칼국수와 만두로 유명해요.'),L('Menu and prices in the game are examples.','게임 속 메뉴와 가격은 예시예요.')]},
 cable:{n:L('Namsan Cable Car','남산 케이블카'),sub:L('Myeongdong Station exit 3, 10 min uphill','명동역 3번 출구에서 오르막 10분'),ll:[37.5567,126.9840],q:'Namsan Cable Car',f:[L('Adult round trip ₩15,000, one way ₩12,000.','성인 왕복 15,000원, 편도 12,000원.'),L('Runs daily 10:00–23:00.','매일 10:00~23:00 운행.'),L('The free Namsan Oreumi inclined elevator near exit 4 saves the climb (closed Mondays).','4번 출구 근처 무료 경사 엘리베이터 "남산 오르미"를 타면 오르막을 줄여요(월요일 쉼).')]},
 ntower:{n:L('N Seoul Tower','N서울타워'),sub:L('Namsan','남산'),ll:[37.5512,126.9882],q:'N Seoul Tower',f:[L('The tower is 236.7 m tall and stands about 480 m above sea level.','타워 높이 236.7m, 해발 약 480m예요.'),L('Observatory ticket: adult ₩29,000.','전망대 입장료: 성인 29,000원.'),L('Go 30–60 minutes before sunset to see both day and night views.','해 지기 30분~1시간 전에 가면 낮 풍경과 야경을 다 봐요.')]},
 gbk:{n:L('Gyeongbokgung Palace','경복궁'),sub:L('Main palace of Joseon · 1395','조선의 법궁 · 1395'),ll:[37.5759,126.9769],q:'Gyeongbokgung Palace',f:[L('Admission ₩3,000. Free if you wear hanbok.','관람료 3,000원. 한복을 입으면 무료.'),L('Closed on Tuesdays. Nov–Feb hours 09:00–17:00; last entry one hour before closing.','화요일 휴궁. 11~2월은 09:00~17:00, 입장 마감은 1시간 전.'),L('Gyeongbokgung Station (Line 3) is the nearest subway stop.','가까운 역은 3호선 경복궁역이에요.')]},
 guard:{n:L('Royal guard changing ceremony','수문장 교대의식'),sub:L('Gwanghwamun','광화문'),ll:[37.5759,126.9769],q:'Gwanghwamun Gate',f:[L('Held twice a day at 10:00 and 14:00, about 20 minutes.','하루 두 번 10:00, 14:00에 약 20분 열려요.'),L('Not held on Tuesdays, when the palace is closed.','궁이 쉬는 화요일에는 열리지 않아요.')]},
 geun:{n:L('Geunjeongjeon','근정전'),sub:L('Throne hall · National Treasure','정전 · 국보'),q:'Geunjeongjeon Hall',f:[L('The throne hall where kings were crowned and received envoys.','왕의 즉위식과 사신 접견이 열리던 정전이에요.'),L('It is designated a National Treasure.','국보로 지정돼 있어요.')]},
 gyeong:{n:L('Gyeonghoeru','경회루'),sub:L('Banquet pavilion on a pond','연못 위의 누각'),q:'Gyeonghoeru Pavilion',f:[L('A two-storey pavilion on a pond, used for royal banquets.','연못 위 2층 누각으로 왕실 연회가 열렸어요.'),L('It is also a National Treasure.','이곳도 국보예요.')]},
 bukchon:{n:L('Bukchon Hanok Village','북촌한옥마을'),sub:L('Between two palaces','두 궁궐 사이'),ll:[37.5826,126.9836],q:'Bukchon Hanok Village',f:[L('A hillside neighbourhood of traditional tiled-roof houses where people still live.','지금도 주민이 사는 기와집 동네예요.'),L('In the red zone (Bukchon-ro 11-gil) visitors are allowed only 10:00–17:00.','레드존(북촌로11길)은 10:00~17:00에만 방문할 수 있어요.'),L('Fines of ₩100,000 apply outside those hours (enforced since March 2025).','그 외 시간에는 과태료 10만 원(2025년 3월부터 단속).')]},
 insa:{n:L('Insadong','인사동'),sub:L('Galleries · tea houses','화랑 · 전통찻집'),ll:[37.5743,126.9849],q:'Insadong Ssamziegil',f:[L('A street of galleries, craft shops and traditional tea houses.','화랑, 공예품 가게, 전통찻집이 이어진 거리예요.'),L('Ssamziegil is a courtyard building with a spiral walkway of small shops.','쌈지길은 작은 가게들이 나선형 길로 이어진 건물이에요.')]},
 gwangjang:{n:L('Gwangjang Market','광장시장'),sub:L('Jongno 5-ga Station exit 8','종로5가역 8번 출구'),ll:[37.5701,126.9996],q:'Gwangjang Market',f:[L('One of Korea\'s oldest markets, dating from 1904–05.','1904~05년에 시작된 오래된 시장이에요.'),L('Famous for bindaetteok, mayak gimbap and yukhoe.','빈대떡, 마약김밥, 육회가 유명해요.'),L('Food alley about 9:00–23:00; shops close earlier and rest on Sundays.','먹자골목은 9:00~23:00쯤, 일반 상점은 더 일찍 닫고 일요일에 쉬어요.')]},
 cheong:{n:L('Cheonggyecheon Stream','청계천'),sub:L('Restored 2005','2005년 복원'),ll:[37.5692,126.9787],q:'Cheonggyecheon Stream',f:[L('A stream through downtown, uncovered and restored in 2005.','도심을 흐르는 하천으로 2005년에 복원했어요.'),L('You walk below street level along the water.','길보다 낮은 물가를 따라 걸어요.')]},
 ddp:{n:L('Dongdaemun Design Plaza','동대문디자인플라자'),sub:'DDP · Zaha Hadid',ll:[37.5665,127.0092],q:'Dongdaemun Design Plaza',f:[L('Designed by Zaha Hadid, opened in 2014.','자하 하디드가 설계해 2014년에 문을 열었어요.'),L('Its curved aluminium skin is lit at night.','곡선의 알루미늄 외벽이 밤에 빛나요.')]},
 hongdae:{n:L('Hongdae','홍대'),sub:L('Hongik Univ. Station exit 9','홍대입구역 9번 출구'),ll:[37.5563,126.9236],q:'Hongdae Street',f:[L('The area around Hongik University, known for indie music, clubs and street performances.','홍익대학교 주변으로 인디 음악, 클럽, 거리 공연으로 알려져 있어요.'),L('AREX all-stop trains from the airport stop here.','공항에서 오는 공항철도 일반열차가 여기 서요.')]},
 hangang:{n:L('Yeouido Hangang Park','여의도 한강공원'),sub:L('Yeouinaru Station exit 2','여의나루역 2번 출구'),ll:[37.5284,126.9340],q:'Yeouido Hangang Park',f:[L('A riverside park where people picnic, cycle and order fried chicken to the delivery zone.','소풍, 자전거, 치킨 배달로 붐비는 강변 공원이에요.'),L('"Han River ramen" is instant ramen cooked on a machine at the convenience store.','"한강 라면"은 편의점 조리기로 끓여 먹는 라면이에요.')]},
 hbus:{n:L('Hangang Bus','한강버스'),sub:L('River ferry','수상 버스'),q:'Hangang Bus Yeouido pier',f:[L('A public ferry with seven piers from Magok to Jamsil; full service resumed 1 March 2026.','마곡에서 잠실까지 선착장 7곳. 2026년 3월 1일 전 구간 운항을 재개했어요.'),L('₩3,000 per ride, card only.','1회 3,000원, 카드만 받아요.'),L('Yeouido pier is a 4-minute walk from Yeouinaru Station exit 2.','여의도 선착장은 여의나루역 2번 출구에서 걸어서 4분.')]},
 starfield:{n:L('Starfield Library','별마당도서관'),sub:'COEX Mall',ll:[37.5116,127.0595],q:'Starfield Library COEX',f:[L('An open library in the middle of COEX Mall with shelves 13 m high.','코엑스몰 한가운데 13m 높이 서가가 있는 열린 도서관이에요.'),L('Free to enter. Check opening hours before you go.','입장은 무료예요. 운영 시간은 가기 전에 확인하세요.')]},
 bongeun:{n:L('Bongeunsa Temple','봉은사'),sub:L('Founded 794','794년 창건'),ll:[37.5147,127.0573],q:'Bongeunsa Temple',f:[L('A Buddhist temple founded in 794, facing the COEX towers.','794년에 세운 절로 코엑스 빌딩과 마주 보고 있어요.')]},
 lotte:{n:L('Lotte World Tower · Seoul Sky','롯데월드타워 · 서울스카이'),sub:L('555 m · 123 floors','555m · 123층'),ll:[37.5126,127.1025],q:'Lotte World Tower',f:[L('Korea\'s tallest building: 555 m, 123 floors.','한국에서 가장 높은 건물이에요. 555m, 123층.'),L('Seoul Sky ticket: adult ₩27,000. Sun–Thu 10:30–22:00, Fri–Sat until 23:00.','서울스카이 성인 27,000원. 일~목 10:30~22:00, 금·토는 23:00까지.'),L('The elevator reaches the 118th floor in about one minute.','엘리베이터로 118층까지 약 1분.')]}
};
const PH=%s;
"""
ph=open(S+'PH_seoul.js',encoding='utf8').read() if os.path.exists(S+'PH_seoul.js') else '{}'
cut("const REAL={","const SV=",REAL%ph)
rep("c.innerHTML='실제 사진 · <a target=\"_blank\" rel=\"noopener\"></a>';","c.innerHTML=L('Real photo · ','실제 사진 · ')+'<a target=\"_blank\" rel=\"noopener\"></a>';")
rep("a.textContent='🌍 구글 거리뷰로 실제 거리 보기';","a.textContent=L('🌍 See the real street (Street View)','🌍 구글 거리뷰로 실제 거리 보기');")
rep("m.textContent='🗺 지도에서 찾기';","m.textContent=L('🗺 Find on the map','🗺 지도에서 찾기');")
rep("p[1]+' · '+p[2]+' · 위키미디어 공용'","p[1]+' · '+p[2]+' · Wikimedia Commons'")
rep("c.fillText('📷 실제 모습 보기',256,160);","c.fillText(L('📷 Real view','📷 실제 모습 보기'),256,160);")
cut("function factsFor(id){","/* ---------- 안으로 들어가기","function factsFor(id){return '';}\n")
# ---- 장면 모듈 ----
rep("/* ---------- 기존 장면에 사람·장소 더하기 ---------- */\nconst ENH={};","/* ---------- 기존 장면에 사람·장소 더하기 ---------- */\nconst ENH={};\n")
rep("/* ---------- 상태 ---------- */",open(S+'K_seoul.js',encoding='utf8').read()+"\n/* ---------- 상태 ---------- */")
rep(" const b=at(0,1,4);\n if(city==='rom')"," const b=at(0,1,4);\n if(D.noBoard){}else if(city==='rom')")
rep("b:s.k==='gelato'?'🍨 '+s.n:'🛍 '+s.n,","b:s.k==='gelato'?(s.ic||'🍨')+' '+s.n:'🛍 '+s.n,")
rep("ENH.terminal0=ENH.terminal;ENH.terminal=","ENH.terminal0=ENH.terminal;ENH.terminalX=")
rep("}[k];\n const wl=repMat('rw'+k,","}[k]||{fl:['#b98b62','#a77b55'],wall:'#f1e7d2',band:'#6b4a35',info:CITY[k].rinfo};\n const wl=repMat('rw'+k,")
rep("notes:[[0,N0]],acts:[],people:list,npcs,spots,walk:{box:[-W/2+.8,","notes:[[0,N0||L('Take a free seat and order.','빈자리에 앉아 주문해요.')]],acts:[],people:list,npcs,spots,walk:{box:[-W/2+.8,")
rep("name:'웨이터 '+sp.w,role:sp.n+' 직원',p:sp.n+'에서 일하는 직원.","name:L('Server ','직원 ')+sp.w,role:sp.n,p:sp.n+'에서 일하는 직원.")
rep("quick:['추천 메뉴는?','여기 유명한 게 뭐예요?'],lines:['어서 오세요! 빈자리에 앉으시면 주문 받을게요.']});\n infoSpot","quick:[L('What do you recommend?','추천 메뉴는?')],lines:[L('Welcome! Take any free seat.','어서 오세요! 빈자리에 앉으세요.')]});\n infoSpot")
rep("const w=cur.npcs.find(n=>/웨이터|바텐더|바리스타|셰프|젤라토|주인/.test(n.name));","const w=cur.npcs.find(n=>/웨이터|직원|Server|주인|Owner|Auntie|이모|Clerk|Barista|Rider|사장|Mrs|기사|바리스타/.test(n.name));")
rep("name:(s.k==='gelato'?'젤라토 가게 ':'')+s.w,role:s.n+' 주인',","name:s.w,role:s.n,")
rep("lines:['어서 오세요! 천천히 구경하세요.']});","lines:[L('Welcome! Take your time.','어서 오세요! 천천히 구경하세요.')]});")
rep("quick:['이 동네 추천 장소는?','맛집 알려 주세요'],lines:['반가워요! 여행 중이세요?','이 동네는 천천히 걸어 다니는 게 제일 좋아요.']","quick:[L('What should I see here?','이 동네 추천 장소는?'),L('Where should I eat?','맛집 알려 주세요')],lines:[L('Hi! Are you travelling?','반가워요! 여행 중이세요?')]")
rep("name:'크루 지아',role:'이 크루즈의 한국어 안내 크루',p:'손님을 따라다니며 일정과 선내 시설, 기항지 관광을 안내하는 밝은 크루. 일정표 자료를 정확히 알고 있다.',x:0,z:0,quick:['오늘 일정 알려 주세요','지금 뭐 하면 좋아요?','승선 시간이 언제예요?'],lines:['무엇이든 물어보세요!','오늘 할 일은 위쪽 일정 버튼에서 볼 수 있어요.']}",
    "name:L('Guide Jia','가이드 지아'),role:L('Your Seoul tour guide','서울 여행 가이드'),p:'여행자를 따라다니며 서울 2박 3일 코스와 교통, 요금을 안내하는 밝은 가이드. 위 자료를 정확히 알고 있다.',x:0,z:0,quick:[L('What is the plan today?','오늘 일정 알려 주세요'),L('How do I pay for the subway?','지하철 요금은 어떻게 내요?')],lines:[L('Ask me anything about Seoul!','서울에 대해 무엇이든 물어보세요!')]}")
rep("' 게임 속에서는 통역기 덕분에 손님과 한국어로 이야기한다.'","''")
rep("'\\n지금 손님이 있는 곳: '","'\\n'+wxText()+'\\n지금 손님이 있는 곳: '")
rep("  if(cur.rideTick)cur.rideTick(dt);","  if(cur.rideTick)cur.rideTick(dt);liveTick(dt);")
# seoul 전용: 표 사기 · 걸어서 이동
rep("ENH.seoul=(c,o)=>{ENH.port(c,o);const D=CITY[o.city];","ENH.seoul=(c,o)=>{ENH.port(c,o);const D=CITY[o.city];if(D.tix){const q=S[Math.round(D.tix.t*(SN-1))];c.spots.push({x:q.x+3,z:q.z,y:q.y,r:7,b:L('🎫 Palace ticket','🎫 경복궁 입장권'),s:L('₩3,000 · free in hanbok','3,000원 · 한복은 무료'),fn:()=>{const hb=G.bag.some(x=>/Hanbok|한복/.test(x));if(!hb&&!charge(D.tix.fare))return;say(hb?L('You are wearing hanbok, so admission is free!','한복을 입어서 무료예요!'):L('One adult ticket, ₩3,000.','성인 1장, 3,000원이에요.'));markAct(D.tix.id);}});}(D.links||[]).forEach(f=>{const q=S[Math.round(f.t*(SN-1))];c.spots.push({x:q.x,z:q.z+3,y:q.y,r:7,b:f.n,s:f.s,fn:()=>{markAct(f.id);fadeMsg(f.n,()=>go(f.to,f.at));}});});")
# ---- 화면 글자 ----
rep('<span class="tag" id="dayTag">DAY 1 · 10/4(일)</span><b id="placeName">크루즈 터미널</b><span class="s" id="placeSub"></span>','<span class="tag" id="dayTag">DAY 1</span><b id="placeName"></b><span class="s" id="placeSub"></span><span class="s" id="wx" style="color:var(--brass);display:block"></span>')
rep('<button id="mapBtn" type="button">🛗 배 안</button>','<button id="mapBtn" type="button">🚇</button><button id="skyBtn" type="button">🕒</button><button id="langBtn" type="button">한/EN</button>')
cut('<div id="start"><div class="card">','<script>window.WEB_SITE',r"""<div id="start"><div class="card">
  <div class="eyebrow">INCHEON AIRPORT → SEOUL</div>
  <h1 id="stH">Virtual Seoul<br>3 days</h1>
  <p id="stP"></p>
  <p class="route" id="stR"></p>
  <button id="enterCath" type="button" hidden></button>
  <button id="enter" type="button" disabled>Start</button>
  <button id="stLang" type="button" style="display:block;margin:12px auto 0;background:transparent;color:var(--ink);border:1px solid rgba(255,255,255,.4);border-radius:999px;padding:8px 18px;font-size:14px">한국어 / English</button>
  <span id="loading">…</span>
</div></div>

""")
rep("const FROMCITY=location.hash==='#board';$('enterCath').onclick=()=>{location.href='cathedral.html#cruise';};",r"""const FROMCITY=false;{const sw=()=>{try{localStorage.setItem('seoul_lang',LANG==='ko'?'en':'ko');}catch(e){}location.reload();};$('stLang').onclick=sw;$('langBtn').onclick=sw;
 $('stH').innerHTML=L('Virtual Seoul<br>3 days','가상 서울<br>2박 3일');$('stP').textContent=L('Land at Incheon Airport, clear immigration, buy a T-money card and ride the airport train into the city. Walk Myeongdong, ride the cable car up Namsan, enter Gyeongbokgung, eat at Gwangjang Market, picnic by the Han River and go up Lotte World Tower. The sky follows the real time and weather in Seoul, and every sight has real facts, photos and Street View.','인천공항에 내려 입국심사를 받고, 티머니 카드를 사서 공항철도로 서울에 들어가요. 명동을 걷고, 케이블카로 남산에 오르고, 경복궁에 들어가고, 광장시장에서 먹고, 한강에서 소풍하고, 롯데월드타워에 올라가요. 하늘은 지금 서울의 실제 시각과 날씨를 따르고, 명소마다 확인한 설명과 사진, 거리뷰가 있어요.');
 $('stR').textContent=L('Airport · Myeongdong · Namsan · Gyeongbokgung · Bukchon · Insadong · Gwangjang Market · DDP · Hongdae · Han River · COEX · Lotte World Tower','공항 · 명동 · 남산 · 경복궁 · 북촌 · 인사동 · 광장시장 · DDP · 홍대 · 한강 · 코엑스 · 롯데월드타워');$('enter').textContent=L('Start at the airport','공항에서 시작하기');$('loading').textContent='';
 $('planBtn').textContent=L('📋 Plan','📋 일정');$('stampBtn').textContent=L('Stamps','스탬프');$('voiceBtn').textContent=L('Voice','음성');$('hint').textContent=L('Drag on the left to walk · drag on the right to look around','왼쪽을 누른 채 끌면 걷기 · 오른쪽을 끌면 둘러보기');
 document.querySelectorAll('[data-close]').forEach(b=>b.textContent=L('Close','닫기'));$('talkIn').placeholder=L('Say something','말을 걸어 보세요');$('talkSend').textContent=L('Send','보내기');document.querySelector('#pass h2').textContent=L('Seoul stamps','서울 스탬프');
 $('auto').innerHTML='<b>'+L('Follow the guide','가이드 따라가기')+'</b><small>'+L('Walk the route automatically','길 따라 자동으로 걷기')+'</small>';
 const sk=()=>{$('skyBtn').textContent={live:'🕒',day:'☀',night:'🌙'}[G.skyMode||'live'];};sk();$('skyBtn').onclick=()=>{G.skyMode={live:'day',day:'night',night:'live'}[G.skyMode||'live'];saveG();sk();toast({live:L('Live Seoul time and weather','지금 서울 시각·날씨 그대로'),day:L('Always daytime','항상 낮'),night:L('Always night','항상 밤')}[G.skyMode]);go(curId,tPos);};}
$('enterCath').onclick=()=>{};""")
rep("$('auto').querySelector('b').textContent=v?'멈추기':'크루 따라가기';","$('auto').querySelector('b').textContent=v?L('Stop','멈추기'):L('Follow the guide','가이드 따라가기');")
rep("p.textContent='할 일을 누르면 그 자리로 바로 가요. 걸어가도 되고, 해내면 ✔가 붙어요. 📷를 누르면 그곳의 실제 사진과 설명, 거리뷰가 나와요.';","p.textContent=L('Tap a task to jump there. Finished tasks get ✔. Tap 📷 for real facts, photos and Street View.','할 일을 누르면 그 자리로 바로 가요. 해내면 ✔가 붙어요. 📷를 누르면 실제 설명과 사진, 거리뷰가 나와요.');")
rep("openPanel('일정 · 관광 코스',","openPanel(L('3-day plan','일정 · 관광 코스'),")
rep("openPanel('배 안 이동',(b)=>{const p=document.createElement('p');p.className='lead';p.textContent='엘리베이터를 타고 선내 어디든 갈 수 있어요.';b.append(p);const rb=document.createElement('button');rb.type='button';rb.className='row';rb.innerHTML='<span>📷 실제 코스타 토스카나</span><b>사진 · 설명</b>';rb.onclick=()=>openReal('ship');b.append(rb);","openPanel(L('Jump to an area','지역으로 바로 가기'),(b)=>{const p=document.createElement('p');p.className='lead';p.textContent=L('Skip the ride and go straight to an area.','탈것을 건너뛰고 바로 가요.');b.append(p);const rb=document.createElement('button');rb.type='button';rb.className='row';rb.innerHTML='<span>📷 '+REAL.subway.n+'</span><b>'+L('fares','요금')+'</b>';rb.onclick=()=>openReal('subway');b.append(rb);")
rep("fadeMsg('엘리베이터로 '+nm+'에 가요.',()=>go(id));","fadeMsg('→ '+nm,()=>go(id));")
rep("$('passLead').textContent=end?","$('passLead').textContent=LANG!=='ko'?(end?'Trip finished. Stamps '+n+'/'+STAMPS.length+'. Have a great real trip to Seoul!':'Collect a stamp at the end of each area.'):end?")
rep("if(FROMCITY)go('terminal',0.02);else go(nextQ()?nextQ().q.sc:'terminal',nextQ()?nextQ().q.at:0);","dayI=Math.min(dayI,DAYS.length-1);go(nextQ()?nextQ().q.sc:'icn',nextQ()?nextQ().q.at:0);")
rep("go('terminal');};b.append(rs);","go('icn');};b.append(rs);")
rep("case 'sleep':fadeMsg(","case 'sleep':markAct('sleep');fadeMsg(")

# ---- 건물·사물 통과 못 하게 ----
rep("/* ---------- 루프 ---------- */",r"""/* 건물·사물에 막히기 */
let SOL=[];const _cv=new T.Vector3(),_cb=new T.Box3();
function buildSolids(){SOL=[];if(!cur||cur.rideTick)return;cur.g.updateMatrixWorld(true);cur.g.traverse(o=>{if(!o.isMesh||!o.geometry||/Plane/.test(o.geometry.type))return;for(let p=o;p&&p!==cur.g;p=p.parent){if(p.userData&&(p.userData.rig||p.userData.pass))return;}
  if(!o.geometry.boundingBox)o.geometry.computeBoundingBox();_cb.copy(o.geometry.boundingBox).applyMatrix4(o.matrixWorld);const sx=_cb.max.x-_cb.min.x,sz=_cb.max.z-_cb.min.z,sy=_cb.max.y-_cb.min.y;if(Math.max(sx,sz)>80||sy<.25)return;
  SOL.push({b:o.geometry.boundingBox,inv:new T.Matrix4().copy(o.matrixWorld).invert(),y0:_cb.min.y,y1:_cb.max.y,cx:(_cb.min.x+_cb.max.x)/2,cz:(_cb.min.z+_cb.max.z)/2,r:Math.hypot(sx,sz)/2+.6});});}
function hitAt(x,z,out){for(const s of SOL){if(s.y1<me.y+.4||s.y0>me.y+1.5)continue;const dx=x-s.cx,dz=z-s.cz;if(dx*dx+dz*dz>s.r*s.r)continue;_cv.set(x,Math.min(s.y1-.05,Math.max(s.y0+.05,me.y+.9)),z).applyMatrix4(s.inv);const b=s.b,m=.3;if(_cv.x>b.min.x-m&&_cv.x<b.max.x+m&&_cv.z>b.min.z-m&&_cv.z<b.max.z+m&&_cv.y>b.min.y-m&&_cv.y<b.max.y+m)out.add(s);}}
function collide(ox,oz){if(!SOL.length)return;const A=new Set();hitAt(ox,oz,A);const ok=(x,z)=>{const B=new Set();hitAt(x,z,B);for(const s of B)if(!A.has(s))return false;return true;};
 if(ok(me.x,me.z))return;if(ok(me.x,oz)){me.z=oz;return;}if(ok(ox,me.z)){me.x=ox;return;}me.x=ox;me.z=oz;}
/* ---------- 루프 ---------- */""")
rep("me.x+=dx*sp*dt;me.z+=dz*sp*dt;constrain(ox,oz,dt);","me.x+=dx*sp*dt;me.z+=dz*sp*dt;constrain(ox,oz,dt);collide(ox,oz);")
rep(" placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);"," placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);buildSolids();")
rep("function mkGate(){const g=new T.Group(),","function mkGate(){const g=new T.Group();g.userData.pass=1;const ")
rep("function mkLotte(){const g=new T.Group(),","function mkLotte(){const g=new T.Group();g.userData.pass=1;const ")

# ---- 값어치: 예행연습 · 예산 · 표현 · 360 ----
rep("function charge(eur){if(G.eur+1e-9<eur){","function charge(eur,lab){if(G.eur+1e-9>=eur&&eur>0){G.sp=G.sp||[];G.sp.push([lab||SCN[curId].name,eur,dayI]);}if(G.eur+1e-9<eur){")
rep("r.onclick=()=>{if(pr&&!charge(pr))return;closePanel();serve(nm,ctx,actId,stand);};","r.onclick=()=>{if(pr&&!charge(pr,nm))return;closePanel();serve(nm,ctx,actId,stand);};")
rep("r.onclick=()=>{if(!charge(pr))return;G.bag.push(nm);","r.onclick=()=>{if(!charge(pr,nm))return;G.bag.push(nm);")
rep("if(s.fare){if(!charge(s.fare))return;","if(s.fare){if(!charge(s.fare,s.n))return;")
rep("if(!charge(23000))return;","if(!charge(23000,L('T-money card + top-up','티머니 카드 + 충전')))return;")
rep("if(!charge(13000))return;","if(!charge(13000,L('AREX Express','공항철도 직통열차')))return;")
rep("if(!charge(f.fare))return;","if(!charge(f.fare,f.n))return;")
rep("if(!hb&&!charge(D.tix.fare))return;","if(!hb&&!charge(D.tix.fare,L('Gyeongbokgung ticket','경복궁 입장권')))return;")
rep("/* ---------- 상태 ---------- */",open(S+'L_value.js',encoding='utf8').read()+"const PANOS="+(open(S+'PANO_seoul.js',encoding='utf8').read() if os.path.exists(S+'PANO_seoul.js') else '{}')+";\n/* ---------- 상태 ---------- */")
rep("say(f.say);playTune(10,true);markAct(f.id);}});});};","say(f.say);playTune(10,true);markAct(f.id);}});});addQuiz(c,o.city);};")
rep("m.textContent=L('🗺 Find on the map','🗺 지도에서 찾기');k.append(m);","m.textContent=L('🗺 Find on the map','🗺 지도에서 찾기');k.append(m);if(PANOS[id]){const a=document.createElement('a');a.className='sv';a.href='#';a.textContent=L('🌐 Look around in 360°','🌐 360도로 둘러보기');a.onclick=(e)=>{e.preventDefault();openPano(id);};k.prepend(a);}")
rep("function frame(now){const dt=Math.min(.05,(now-last)/1000);last=now;clock+=dt;","function frame(now){const dt=Math.min(.05,(now-last)/1000);last=now;clock+=dt;if(PV){panoFrame();requestAnimationFrame(frame);return;}")
rep('<button id="skyBtn" type="button">🕒</button>','<button id="skyBtn" type="button">🕒</button><button id="tripBtn" type="button">🧾</button><button id="phrBtn" type="button">🗣</button>')
rep('<div id="toast" hidden></div>','<div id="toast" hidden></div>\n<div id="pv" hidden style="position:fixed;inset:0;z-index:40;touch-action:none;cursor:grab"><button id="pvX" type="button" style="position:absolute;right:14px;top:calc(env(safe-area-inset-top,0px) + 14px);padding:10px 16px;border-radius:999px;border:0;background:rgba(15,29,51,.85);color:#fff;font-size:16px">✕</button><div style="position:absolute;left:0;right:0;bottom:calc(env(safe-area-inset-bottom,0px) + 14px);text-align:center;color:#fff;font-size:12.5px;text-shadow:0 1px 3px #000;pointer-events:none"><div id="pvH" style="font-size:14.5px;margin-bottom:4px"></div><span id="pvC"></span></div></div>\n<style>@media print{body>*{display:none!important}#pan{display:block!important;position:static!important;background:#fff!important}#pan .in{max-height:none!important;background:#fff!important;color:#000!important;box-shadow:none!important}#pan *{color:#000!important}#pan .row{border:0!important;border-bottom:1px solid #ccc!important;background:none!important;border-radius:0!important}#pan .close,#pan .noprint{display:none!important}}</style>')
rep("$('enterCath').onclick=()=>{};","$('enterCath').onclick=()=>{};$('tripBtn').onclick=openTrip;$('phrBtn').onclick=openPhrases;$('pvX').onclick=closePano;$('pvH').textContent=L('Drag to look around','끌어서 둘러보세요');{let d=null;const v=$('pv');v.addEventListener('pointerdown',e=>{if(e.target.id==='pvX')return;d={x:e.clientX,y:e.clientY};});v.addEventListener('pointermove',e=>{if(!d||!PV)return;PV.yaw-=(e.clientX-d.x)*.005;PV.pit=Math.max(-1.3,Math.min(1.3,PV.pit+(e.clientY-d.y)*.005));d={x:e.clientX,y:e.clientY};});const u=()=>d=null;v.addEventListener('pointerup',u);v.addEventListener('pointercancel',u);}")
rep("Answer in friendly, simple English, 2-3 short sentences, in character.","Answer in the same language the visitor writes in (any language; default English), friendly and simple, 2-3 short sentences, in character.")

# ---- 그림자·조명·재질 (3D 애니메이션 느낌) + 거리 360 ----
rep("const R=new T.WebGLRenderer({canvas,antialias:true,powerPreference:'high-performance'});","const R=new T.WebGLRenderer({canvas,antialias:true,powerPreference:'high-performance'});R.shadowMap.enabled=true;R.shadowMap.type=T.PCFSoftShadowMap;")
rep("const sun=new T.DirectionalLight(0xffffff,0.9);scene.add(sun);","const sun=new T.DirectionalLight(0xffffff,0.9);scene.add(sun);scene.add(sun.target);sun.shadow.mapSize.set(2048,2048);sun.shadow.bias=-.0006;sun.shadow.normalBias=.04;{const c=sun.shadow.camera;c.left=-70;c.right=70;c.top=70;c.bottom=-70;c.near=1;c.far=420;c.updateProjectionMatrix();}const SUND=new T.Vector3(.4,.75,-.5);")
rep("const cam=new T.PerspectiveCamera(66,1,0.1,5000);","const EXPO=1.55;const cam=new T.PerspectiveCamera(66,1,0.1,5000);")
s=s.replace("const EXPO=1.55;const cam=","const cam=",1).replace("const R=new T.WebGLRenderer({canvas,antialias:true,powerPreference:'high-performance'});R.shadowMap","const EXPO=1.55;const R=new T.WebGLRenderer({canvas,antialias:true,powerPreference:'high-performance'});R.shadowMap",1)
rep("MC[k]=new T.MeshLambertMaterial(Object.assign({color:c},o||{}));}return MC[k];}","MC[k]=new T.MeshStandardMaterial(Object.assign({color:c,roughness:.8,metalness:.02},o||{}));}return MC[k];}")
rep("sun.position.set(...s.sun).multiplyScalar(100);","sun.position.set(...s.sun).multiplyScalar(100);SUND.set(...s.sun).normalize();")
rep(" placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);buildSolids();"," placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);buildSolids();dressScene();")
rep("/* 건물·사물에 막히기 */",r"""/* 그림자: 해를 따라 사람과 건물 그림자가 생겨요 */
let fpsT=0,fpsN=0;
const AMB=new T.AmbientLight(0xffffff,.1);scene.add(AMB);
function dressScene(){const out=cur.sky!=='indoor'&&!cur.dark;AMB.intensity=cur.sky==='indoor'?.5:cur.sky==='night'?.3:.1;sun.castShadow=!!(G.hd!==false&&out);cur.g.traverse(o=>{if(!o.isMesh)return;const m=o.material,tr=m&&!Array.isArray(m)&&m.transparent;if(!o.geometry.boundingSphere)o.geometry.computeBoundingSphere();const big=o.geometry.boundingSphere.radius*Math.max(o.scale.x,o.scale.z)>260;o.castShadow=!tr&&!big&&!/Plane/.test(o.geometry.type);o.receiveShadow=!tr;});fpsT=0;fpsN=0;}
function sunFollow(dt){sun.target.position.set(me.x,me.y,me.z);sun.position.set(me.x+SUND.x*160,me.y+Math.max(.25,SUND.y)*160,me.z+SUND.z*160);if(sun.castShadow&&fpsN>=0){fpsT+=dt;fpsN++;if(fpsT>5){if(fpsN/fpsT<20){G.hd=false;saveG();sun.castShadow=false;toast(L('Shadows turned off to keep it smooth','부드럽게 움직이도록 그림자를 껐어요'));}fpsN=-1;}}}
/* 건물·사물에 막히기 */""")
rep("if(cur.rideTick)cur.rideTick(dt);liveTick(dt);","if(cur.rideTick)cur.rideTick(dt);liveTick(dt);sunFollow(dt);")
rep("rb.onclick=()=>openReal('subway');b.append(rb);","rb.onclick=()=>openReal('subway');b.append(rb);[['st1',L('Crossroads','네거리')],['st2',L('Market entrance','시장 입구')],['st3',L('Back alley','뒷골목')]].forEach(([k,n])=>{const x=document.createElement('button');x.type='button';x.className='row';x.innerHTML='<span>🌐 '+L('Real Seoul street in 360° · ','실제 서울 거리 360도 · ')+n+'</span><b>'+L('look around','둘러보기')+'</b>';x.onclick=()=>openPano(k);b.append(x);});const nt=document.createElement('p');nt.className='lead';nt.textContent=L('The 360° photos show ordinary Seoul streets (exact location not identified), not the landmarks.','360도 사진은 명소가 아니라 평범한 서울 거리예요(정확한 위치는 확인하지 못했어요).');b.append(nt);")

# ---- 만화 영화 느낌: 툰 셰이딩 · 윤곽선 · 큰 머리와 눈 · 무료 3D 모델(Kenney) ----
rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>','<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n<script src="assets3d/gltf-loader.js"></script>\n<script src="assets3d/outline-effect.js"></script>')
rep("MC[k]=new T.MeshStandardMaterial(Object.assign({color:c,roughness:.8,metalness:.02},o||{}));}return MC[k];}","MC[k]=new T.MeshToonMaterial(Object.assign({color:c,gradientMap:GRAD},o||{}));}return MC[k];}")
rep("const MC={},TC={};","const MC={},TC={};const GRAD=new T.DataTexture(new Uint8Array([105,175,255]),3,1,T.LuminanceFormat);GRAD.minFilter=GRAD.magFilter=T.NearestFilter;GRAD.needsUpdate=true;\nlet FX=null;try{if(T.OutlineEffect)FX=new T.OutlineEffect(R,{defaultThickness:.0032,defaultColor:[.16,.12,.1],defaultAlpha:.9});}catch(e){FX=null;}\nconst KN={},KNQ=[];function knLoad(){if(!T.GLTFLoader)return;const ld=new T.GLTFLoader();[['cloud','p/cloud.glb'],['tree','c/grass-trees.glb'],['tree2','c/grass-trees-tall.glb'],['fountain','c/pavement-fountain.glb']].forEach(([k,u])=>ld.load('assets3d/'+u,g=>{KN[k]=g.scene;KNQ.filter(q=>q.k===k).forEach(q=>q.f());},undefined,()=>{}));}\nfunction deco(g,k,x,y,z,size,ry){const put=()=>{if(!g.parent&&g!==cur.g)return;const m=KN[k].clone(true);m.scale.setScalar(size);m.position.set(x,y,z);m.rotation.y=ry||0;m.traverse(o=>{if(o.isMesh){o.castShadow=k!=='cloud';o.receiveShadow=k!=='cloud';if(k==='cloud')o.material.userData.outlineParameters={visible:false};}});g.add(m);if(k==='cloud'){g.userData.clouds=g.userData.clouds||[];g.userData.clouds.push(m);}};if(KN[k])put();else KNQ.push({k,f:put});}")
rep(" const hd=new T.Mesh(new T.SphereGeometry(.14,14,10),sk);hd.position.y=.08;head.add(hd);"," const hd=new T.Mesh(new T.SphereGeometry(.14,14,10),sk);hd.position.y=.08;head.add(hd);head.scale.setScalar(1.32);for(const ex of[-.052,.052]){const w=new T.Mesh(new T.SphereGeometry(.03,8,6),M('#ffffff'));w.position.set(ex,.095,.118);w.scale.z=.5;head.add(w);const pu=new T.Mesh(new T.SphereGeometry(.016,8,6),M('#1a1410'));pu.position.set(ex,.095,.134);pu.scale.z=.5;head.add(pu);}{const mo=new T.Mesh(new T.BoxGeometry(.05,.012,.01),M('#a8473a'));mo.position.set(0,.03,.136);head.add(mo);}")
rep(" skyMesh.position.copy(cam.position);stars.position.copy(cam.position);"," if(cur&&cur.g.userData.clouds)cur.g.userData.clouds.forEach((c,i)=>{c.position.x+=dt*(1.2+i%3*.5);if(c.position.x>me.x+500)c.position.x=me.x-500;});skyMesh.position.copy(cam.position);stars.position.copy(cam.position);")
s=s.replace("R.render(scene,cam);requestAnimationFrame(frame);}","(FX&&G.hd!==false?FX:R).render(scene,cam);requestAnimationFrame(frame);}")
rep("function dressScene(){","function dressScene(){[skyMesh,sea,stars].forEach(o=>{if(o&&o.material)o.material.userData.outlineParameters={visible:false};});if(RAIN)RAIN.material.userData.outlineParameters={visible:false};if(cur.sky!=='indoor'&&!cur.dark&&cur.sky!=='night'){RND=5;for(let i=0;i<12;i++)deco(cur.g,'cloud',me.x-500+rnd()*1000,70+rnd()*60,me.z-400+rnd()*800,22+rnd()*26,rnd()*6.28);}const TR={hgr:[[-40,34],[-90,38],[-150,34],[-210,38],[-20,-2],[-130,-3]],nam:[[-20,18],[-50,22],[-80,-22],[-40,-24]],gbk:[[40,-20],[-50,-30],[60,-90],[40,-140],[-60,60],[60,60]],gng:[[-150,-16],[-170,-16],[-30,16]],bkc:[[-230,12],[-290,-14]]}[cur.city]||[];TR.forEach(([x,z],i)=>deco(cur.g,i%2?'tree2':'tree',x,0,z,i%2?13:11,i*1.3));const FT={hgr:[-100,22],gng:[-110,-16],myd:[-60,-18]}[cur.city];if(FT)deco(cur.g,'fountain',FT[0],0,FT[1],7,0);")
rep("o.castShadow=!tr&&!big&&!/Plane/.test(o.geometry.type);o.receiveShadow=!tr;});","o.castShadow=!tr&&!big&&!/Plane/.test(o.geometry.type);o.receiveShadow=!tr;if(m&&!Array.isArray(m)&&(tr||m.isMeshBasicMaterial||/Plane/.test(o.geometry.type)||big))m.userData.outlineParameters={visible:false};});")
rep("wxLoad();setInterval(wxLoad,600000);","wxLoad();setInterval(wxLoad,600000);knLoad();")
rep("L('Meal and shop prices in this app are examples. Check opening hours before you go.','이 앱의 식사·가게 가격은 예시예요. 운영 시간은 가기 전에 확인하세요.')]","L('Meal and shop prices in this app are examples. Check opening hours before you go.','이 앱의 식사·가게 가격은 예시예요. 운영 시간은 가기 전에 확인하세요.'),L('3D trees, clouds and fountain models: Kenney (kenney.nl). Photos: Wikimedia Commons.','3D 나무·구름·분수 모델: Kenney (kenney.nl). 사진: 위키미디어 공용.')]")

# ---- 메모리 아끼기: 장면을 떠날 때 사진·재질 비우기, 폰에서는 작은 360 사진 ----
rep("function disposeG(g){g.traverse(o=>{if(o.geometry)o.geometry.dispose();});}","function disposeG(g){const keep=new Set(Object.values(MC)),kt=new Set(Object.values(TC));g.traverse(o=>{if(o.geometry)o.geometry.dispose();const ms=o.material?(Array.isArray(o.material)?o.material:[o.material]):[];ms.forEach(m=>{if(keep.has(m))return;if(m.map&&!kt.has(m.map)&&m.map!==GRAD)m.map.dispose();m.dispose();});});try{R.renderLists.dispose();}catch(e){}}")
rep("ld.load(phU(p,p[4]),t=>{","ld.load(phU(p,PHONE?1920:p[4]),t=>{")
rep("let PV=null;","let PV=null;const PHONE=!!(window.matchMedia&&matchMedia('(pointer:coarse)').matches);if(PHONE)sun.shadow.mapSize.set(1024,1024);")
rep("<title>Virtual Seoul · 가상 서울 3일</title>",'<title>Virtual Seoul · 가상 서울 3일</title>\n<link rel="manifest" href="seoul.webmanifest">\n<meta name="theme-color" content="#0f1d33">\n<link rel="icon" href="assets3d/seoul-192.png">\n<link rel="apple-touch-icon" href="assets3d/seoul-192.png">')

# ---- 거리뷰·지도를 새 탭이 아니라 화면 안에서 열기 ----
rep("const SV=ll=>'https://www.google.com/maps/@?api=1&map_action=pano&viewpoint='+ll[0]+','+ll[1];","const SV=ll=>'https://www.google.com/maps/@?api=1&map_action=pano&viewpoint='+ll[0]+','+ll[1];const SVE=ll=>'https://maps.google.com/maps?q=&layer=c&cbll='+ll[0]+','+ll[1]+'&cbp=11,0,0,0,0&output=svembed&hl='+LANG;const MAPE=q=>'https://maps.google.com/maps?q='+encodeURIComponent(q)+'&z=16&output=embed&hl='+LANG;\nfunction openEmbed(src,full){$('emF').src=src;$('emL').href=full;$('em').hidden=false;}\nfunction closeEmbed(){$('em').hidden=true;$('emF').src='about:blank';}")
rep("a.href=SV(r.ll);a.textContent=L('🌍 See the real street (Street View)','🌍 구글 거리뷰로 실제 거리 보기');","a.href=SV(r.ll);a.onclick=(e)=>{e.preventDefault();openEmbed(SVE(r.ll),SV(r.ll));};a.textContent=L('🌍 See the real street (Street View)','🌍 구글 거리뷰로 실제 거리 보기');")
rep("m.href=MAPQ(r.q||r.n);m.textContent=L('🗺 Find on the map','🗺 지도에서 찾기');","m.href=MAPQ(r.q||r.n);m.onclick=(e)=>{e.preventDefault();openEmbed(MAPE(r.q||r.n),MAPQ(r.q||r.n));};m.textContent=L('🗺 Find on the map','🗺 지도에서 찾기');")
rep("c.innerHTML=L('Real photo · ','실제 사진 · ')+'<a target=\"_blank\" rel=\"noopener\"></a>';","c.innerHTML=L('Real photo · ','실제 사진 · ')+'<a></a>';")
rep('<div id="toast" hidden></div>','<div id="toast" hidden></div>\n<div id="em" hidden style="position:fixed;inset:0;z-index:45;background:#0f1d33;display:flex;flex-direction:column"><div style="display:flex;gap:8px;align-items:center;padding:calc(env(safe-area-inset-top,0px) + 8px) 10px 8px"><button id="emX" type="button" style="padding:10px 16px;border-radius:999px;border:0;background:var(--brass);color:var(--navy);font-size:16px"></button><a id="emL" style="color:#cfe0f0;font-size:12.5px;margin-left:auto;text-align:right"></a></div><iframe id="emF" title="Google Maps" style="flex:1;border:0;width:100%" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>\n<style>#em[hidden]{display:none!important}</style>')
rep("$('tripBtn').onclick=openTrip;","$('emX').onclick=closeEmbed;$('emX').textContent=L('← Back to Virtual Seoul','← 가상 서울로 돌아가기');$('emL').textContent=L('Not showing? Open in Google Maps (use the phone Back button to return)','안 보이면 구글 지도로 열기 (돌아올 때는 폰의 뒤로 가기)');$('tripBtn').onclick=openTrip;")

# ---- 미니어처 느낌: 위아래 흐림, 또렷한 색 ----
rep('<div id="toast" hidden></div>\n<div id="em"','<div id="toast" hidden></div>\n<style>#c{filter:saturate(1.18) contrast(1.06)}.tilt{position:fixed;left:0;right:0;pointer-events:none;z-index:1;-webkit-backdrop-filter:blur(3.5px);backdrop-filter:blur(3.5px)}#tiltT{top:0;height:24vh;-webkit-mask-image:linear-gradient(#000,transparent);mask-image:linear-gradient(#000,transparent)}#tiltB{bottom:0;height:20vh;-webkit-mask-image:linear-gradient(transparent,#000);mask-image:linear-gradient(transparent,#000)}</style><div class="tilt" id="tiltT"></div><div class="tilt" id="tiltB"></div>\n<div id="em"')

# ---- 서울시 3D 지도 S-Map 연결 ----
rep("k.append(m);if(PANOS[id]){","k.append(m);if(id!=='icn'&&id!=='tmoney'&&id!=='kyoja'){const sm=document.createElement('a');sm.href=SMAP;sm.textContent=L('🏙 Real 3D Seoul (S-Map, city of Seoul)','🏙 서울시 실사 3D 지도 (S-Map)');sm.onclick=(e)=>{e.preventDefault();openEmbed(SMAP,SMAP);toast(L('In S-Map, search for: ','S-Map에서 검색하세요: ')+r.n);};k.append(sm);}if(PANOS[id]){")
rep("function openEmbed(src,full){","const SMAP='https://smap.seoul.go.kr/m/';\nfunction openEmbed(src,full){")
rep("rb.onclick=()=>openReal('subway');b.append(rb);","rb.onclick=()=>openReal('subway');b.append(rb);{const x=document.createElement('button');x.type='button';x.className='row';x.innerHTML='<span>🏙 '+L('S-Map: the real 3D model of Seoul (official)','S-Map: 서울시가 만든 실사 3D 서울')+'</span><b>'+L('open','열기')+'</b>';x.onclick=()=>{closePanel();openEmbed(SMAP,SMAP);};b.append(x);}")

# ---- 지도 창: 안내 글자를 열린 곳에 맞추고, 열려 있는 동안 3D 그리기 멈추기 ----
rep("$('emL').href=full;$('em').hidden=false;}","$('emL').href=full;$('emL').textContent=/smap/.test(full)?L('Not showing? Open S-Map directly','안 보이면 S-Map 바로 열기'):L('Not showing? Open in Google Maps (use the phone Back button to return)','안 보이면 구글 지도로 열기 (돌아올 때는 폰의 뒤로 가기)');$('em').hidden=false;}")
rep("if(PV){panoFrame();requestAnimationFrame(frame);return;}","if(PV){panoFrame();requestAnimationFrame(frame);return;}if(!document.getElementById('em').hidden){requestAnimationFrame(frame);return;}")

# ---- AI가 그린 명소 그림: 도착하면 천천히 움직이며 크게 떠요 ----
rep("/* ---------- 상태 ---------- */",r"""/* AI가 그린 명소 그림 */
const AIPIC={icn:'assets3d/ai/icn.jpg'};
const SCAI={icn:'icn',myd:'myd',nam:'ntower',gbk:'gbk',bkc:'bukchon',gjm:'gwangjang',hdc:'hongdae',hgr:'hangang',gng:'lotte'};
let AIP=null;
function aiSeen(id){return !!(G.ai&&G.ai[id]);}
function aiArrive(id){if(!id||!AIPIC[id]||aiSeen(id))return;if(!$('start').hidden){AIP=id;return;}showAI(id);}
function showAI(id){const u=AIPIC[id],r=REAL[id];if(!u||!r)return;G.ai=G.ai||{};G.ai[id]=1;saveG();const o=$('ai');$('aiBg').style.backgroundImage='url("'+u+'")';$('aiI').src=u;$('aiI').alt=r.n;$('aiN').textContent=r.n;$('aiSub').textContent=r.sub||'';$('aiReal').onclick=()=>{closeAI();openReal(id);};o.hidden=false;o.classList.remove('on');requestAnimationFrame(()=>requestAnimationFrame(()=>o.classList.add('on')));blip(784,.5,'sine',.08);setTimeout(()=>blip(1175,.6,'sine',.06),180);}
function closeAI(){const o=$('ai');o.classList.remove('on');setTimeout(()=>{o.hidden=true;$('aiI').removeAttribute('src');$('aiBg').style.backgroundImage='';},350);}
/* ---------- 상태 ---------- */""")
rep("placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);buildSolids();dressScene();","placeAt(atT!==undefined?Math.round(atT*(SN-1)):0,true);buildSolids();dressScene();aiArrive(SCAI[id]);")
rep("$('start').hidden=true;if(cur.notes[0])","$('start').hidden=true;if(AIP){const k=AIP;AIP=null;setTimeout(()=>showAI(k),700);}if(cur.notes[0])")
rep("photoBoard(g,p.x,p.y,p.z,p.face,s.id);c.spots.push(","photoBoard(g,p.x,p.y,p.z,p.face,s.id);if(AIPIC[s.id])(c.aiNear=c.aiNear||[]).push({x:p.x,y:p.y,z:p.z,id:s.id});c.spots.push(")
rep("nearT-=dt;if(nearT<0){nearT=.5;","nearT-=dt;if(nearT<0){nearT=.5;if(cur.aiNear&&$('ai').hidden&&$('start').hidden&&!me.ride)cur.aiNear.forEach(a=>{if(!aiSeen(a.id)&&Math.hypot(a.x-me.x,a.z-me.z)<10&&Math.abs(a.y-me.y)<6)showAI(a.id);});")
rep("k.append(m);if(id!=='icn'","k.append(m);if(AIPIC[id]){const ai=document.createElement('a');ai.className='sv';ai.href='#';ai.textContent=L('🎨 See the AI picture','🎨 AI 그림으로 보기');ai.onclick=(e)=>{e.preventDefault();closePanel();showAI(id);};k.prepend(ai);}if(id!=='icn'")
rep("if(!document.getElementById('em').hidden){requestAnimationFrame(frame);return;}","if(!document.getElementById('em').hidden||!document.getElementById('ai').hidden){requestAnimationFrame(frame);return;}")
rep("$('emX').onclick=closeEmbed;","$('aiGo').onclick=closeAI;$('aiGo').textContent=L('Continue ▸','계속 ▸');$('aiReal').textContent=L('📷 Real photo & facts','📷 실제 사진·설명');$('aiTag').textContent=L('🎨 AI-generated picture · may differ from reality','🎨 AI가 그린 그림 · 실제와 다를 수 있어요');$('emX').onclick=closeEmbed;")
rep('<div id="toast" hidden></div>','<div id="toast" hidden></div>\n<div id="ai" hidden><div id="aiBg"></div><img id="aiI" alt=""><div class="aitop"><span id="aiTag"></span></div><div class="aibot"><small id="aiSub"></small><b id="aiN"></b><div class="aibtn"><button id="aiReal" type="button"></button><button id="aiGo" type="button"></button></div></div></div>\n<style>#ai{position:fixed;inset:0;z-index:44;background:#0b1424;overflow:hidden;opacity:0;transition:opacity .35s}#ai.on{opacity:1}#ai[hidden]{display:none!important}#aiBg{position:absolute;inset:-60px;background-size:cover;background-position:center;filter:blur(28px) brightness(.5)}#aiI{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;transform-origin:50% 45%;animation:aikb 18s ease-in-out infinite alternate}@keyframes aikb{from{transform:scale(1) translateY(0)}to{transform:scale(1.16) translateY(-2.5%)}}#ai::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(110deg,transparent 40%,rgba(255,255,255,.07) 50%,transparent 60%);background-size:250% 100%;animation:aish 9s linear infinite}@keyframes aish{from{background-position:150% 0}to{background-position:-50% 0}}#ai .aitop{position:absolute;z-index:2;top:calc(env(safe-area-inset-top,0px) + 12px);left:12px;right:12px}#aiTag{display:inline-block;background:rgba(15,29,51,.8);color:#f3e6c8;border-radius:999px;padding:6px 12px;font-size:12.5px}#ai .aibot{position:absolute;z-index:2;left:0;right:0;bottom:0;padding:70px max(16px,env(safe-area-inset-left,0px)) calc(env(safe-area-inset-bottom,0px) + 16px);background:linear-gradient(rgba(8,14,26,0),rgba(8,14,26,.9) 55%);color:#fff}#aiSub{display:block;font-size:13px;color:#f0c419;margin-bottom:2px}#aiN{display:block;font-family:var(--disp);font-weight:400;font-size:27px;line-height:1.2;margin-bottom:12px}#ai .aibtn{display:flex;gap:8px}#ai .aibtn button{flex:1;padding:12px 10px;border-radius:999px;font-size:15.5px;border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.08);color:#fff}#ai .aibtn #aiGo{background:var(--brass);color:var(--navy);border-color:transparent}@media (prefers-reduced-motion:reduce){#aiI,#ai::after{animation:none}}</style>')

# ---- 가게와 연결 (O2O): NPC 대화 엔진 → 상품·쿠폰·예약 카드 → 쿠폰함·캘린더 ----
rep("/* ---------- 상태 ---------- */",open(S+'M_o2o.js',encoding='utf8').read()+"\n/* ---------- 상태 ---------- */")
rep("addLine(n.name,hi);markAct('talk');}","addLine(n.name,hi);markAct('talk');o2oOpen(n);}")
rep("const input='너는 이 게임 속 '","const input=(n.shop?o2oPrompt(n):'')+'너는 이 게임 속 '")
rep("onText:({text})=>{if(text)line.lastChild.textContent=text.trim();}","onText:({text})=>{if(text)line.lastChild.textContent=o2oStrip(text).trim();}")
rep(r"if(!a)a=localReply(n,q);a=a.replace(/\s+/g,' ').slice(0,240);line.lastChild.textContent=a;",r"let tg=[];if(a){const o=o2oParse(a);a=o.text;tg=o.tags;}if(!a)a=(n.shop&&o2oLocal(n,q))||localReply(n,q);a=a.replace(/\s+/g,' ').slice(0,240);line.lastChild.textContent=a;if(n.shop)o2oAfter(n,q,tg);")
rep("ENH.seoul=(c,o)=>{ENH.port(c,o);const D=CITY[o.city];","ENH.seoul=(c,o)=>{ENH.port(c,o);const D=CITY[o.city];if(o.city==='myd')o2oStore(c);")
rep('<button id="tripBtn" type="button">🧾</button>','<button id="tripBtn" type="button">🧾</button><button id="walBtn" type="button">🎫</button>')
rep("$('tripBtn').onclick=openTrip;","$('tripBtn').onclick=openTrip;$('walBtn').onclick=openWallet;")
rep("[.3,L('Street food stalls open in the late afternoon","[.2,L('The K-Goods Studio on the right is a demo shop: chat with the owner, get a coupon, book a class or order for pickup.','오른쪽 K-굿즈 공방은 시범 가게예요. 사장님과 대화하고 쿠폰을 받고, 체험을 예약하거나 픽업 주문을 해 보세요.')],[.3,L('Street food stalls open in the late afternoon")
rep('<div id="toast" hidden></div>','<div id="toast" hidden></div>\n<style>.oc{align-self:stretch;background:#f7f1e3;color:#1d1915;border-radius:14px;padding:9px 10px;font-size:14px;line-height:1.45}.oc h4{margin:0 0 4px;font-size:12.5px;color:#7a5a1a;font-weight:700}.oc p{margin:0}.oc-info{background:rgba(255,255,255,.08);color:var(--ink);font-size:13px}.oc-ok{background:#e4f3ea}.oci{display:flex;gap:8px;align-items:center;padding-top:6px}.oce{font-size:26px;width:34px;text-align:center;flex:0 0 34px}.oci div{flex:1;min-width:0}.oci div b{display:block;font-size:14.5px}.oci div small{color:#6b6250;font-size:12px}.ocp{color:#9a3324;font-variant-numeric:tabular-nums;white-space:nowrap}.ocb{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}.ocb button,.ocb a{flex:1 1 auto;padding:7px 10px;border-radius:999px;border:1px solid #c9b88f;background:#fff;color:#1d1915;font-size:13px;text-align:center;text-decoration:none;line-height:1.3}.ocb .pri{background:#1f2f4a;color:#fff;border-color:#1f2f4a}.oc-info .ocb a,.oc-info .ocb button,.panel .ocb button{background:rgba(255,255,255,.1);color:var(--ink);border-color:rgba(255,255,255,.25)}.cpn{border:2px dashed #c9a23f;border-radius:12px;padding:8px;text-align:center}.cpn b{display:block;font-size:16.5px}.cpn code{display:block;font-size:17px;letter-spacing:.08em;margin:4px 0;font-family:ui-monospace,monospace}.cpn small{color:#6b6250;font-size:12px}.ochips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}.ochips button{padding:8px 12px;border-radius:999px;font-size:14px}.ochips button.on{background:var(--brass);color:var(--navy);border-color:transparent}</style>')
rep("window.__go=(id,t)=>{go(id,t);};","window.__go=(id,t)=>{go(id,t);};window.__talk=(id)=>{const n=cur.npcs.find(x=>x.id===id);if(n)openTalk(n);return !!n;};window.__ask=(q)=>ask(q);window.__wal=()=>JSON.stringify({cp:WAL.cp.length,bk:WAL.bk.length,wish:WAL.wish.length,last:WAL.bk[0]&&[WAL.bk[0].type,WAL.bk[0].date,WAL.bk[0].time,WAL.bk[0].demo]});window.__parse=(a)=>JSON.stringify(o2oParse(a));window.__ics=()=>WAL.bk[0]?icsDown(WAL.bk[0]):'';")
# ---- 맛집 물어보기 (구글 지도 별점 · 메타버스 길 안내 · 거리뷰 · 메뉴) ----
rep("/* ---------- 상태 ---------- */",open(S+'N_food.js',encoding='utf8').read()+"\n/* ---------- 상태 ---------- */")
rep("const line=addLine(n.name,'……');let a='';","const line=addLine(n.name,'……');let a='';const fq=foodQ(q);if(fq){a=foodReply(n,fq);line.lastChild.textContent=a;n.hist.push({who:'손님',t:q},{who:n.name,t:a});speak(a);n.busy=false;foodGo(n,fq);return;}")
rep("else if(auto){aIdx+=(cur.walkSp||5)*.8*dt;","else if(auto){aIdx+=(cur.walkSp||5)*.8*dt*(FW?FW.dir:1);if(FW&&(FW.dir>0?aIdx>=FW.i:aIdx<=FW.i)){aIdx=FW.i;fwDone();}if(aIdx<0)aIdx=0;")
rep("function setAuto(v){auto=v;","function setAuto(v){auto=v;if(!v)FW=null;")
rep("if(!cur.closed&&aIdx>=SN-2)aIdx=0;}}","if(!cur.closed&&aIdx>=SN-2&&!FW)aIdx=0;}}")
rep('<script>window.WEB_SITE="seoul";</script>','<script>window.WEB_SITE="seoul";</script><script src="seoul-config.js"></script>')
rep("quick:[L('What should I see here?','이 동네 추천 장소는?'),L('Where should I eat?','맛집 알려 주세요')]","quick:[L('What should I see here?','이 동네 추천 장소는?'),L('Where should I eat?','맛집 알려 주세요'),L('Good kimbap place nearby?','김밥 맛집 어디예요?')]")
rep("[.5,L('The red-brick church on the hill is Myeongdong Cathedral (1898).'","[.36,L('Tip: ask a local \"Where is a good kimbap place?\" and they will check Google Maps ratings for you.','팁: 길에서 만난 사람에게 \"김밥 맛집 어디예요?\" 하고 물어보세요. 구글 지도 별점으로 찾아 드려요.')],[.5,L('The red-brick church on the hill is Myeongdong Cathedral (1898).'")
rep('<div id="toast" hidden></div>','<div id="toast" hidden></div>\n<style>.gbox{background:#fff;color:#1b1b1b;border-radius:14px;overflow:auto;max-height:50vh;margin:6px 0 10px;color-scheme:light}.gbox.off{background:rgba(255,255,255,.08);color:var(--ink);padding:10px 12px;font-size:14px;line-height:1.5;max-height:none;overflow:visible}.gbox.off p{margin:0 0 6px}.gbox.off small{display:block;opacity:.75;margin-top:8px;font-size:12px}.gbox .gwait{padding:14px;font-size:14px;color:#555}.gbox.off .gwait{color:inherit;padding:0}gmp-place-search,gmp-place-details,gmp-place-details-compact{display:block;width:100%}.panel .ocb a{background:rgba(255,255,255,.1);color:var(--ink);border-color:rgba(255,255,255,.25)}.panel .ocb .pri{background:var(--brass);color:var(--navy);border-color:transparent}.fdl small.fdn{flex-basis:100%;font-size:11.5px;opacity:.75;text-align:center;margin-top:2px}.fdh{margin:10px 0 2px;font-size:13.5px;color:var(--brass)}</style>')
rep("window.__go=(id,t)=>{go(id,t);};","window.__go=(id,t)=>{go(id,t);};window.__fd=()=>FD?JSON.stringify({ti:FD.ti,ni:me.ni,arr:FD.arrived,d:Math.round(FD.d),auto,spots:cur.spots.length,chev:FD.chev.length}):'null';window.__fdq=(q)=>{const r=foodQ(q);return r?(r.f?r.f.k:'generic'):'none';};window.__near=(id)=>{const n=cur.npcs.find(x=>x.id===id);if(!n)return false;const p=n.rig.position;me.x=p.x+1.3;me.z=p.z+1.3;me.ni=nearestIdx(me.x,me.z);return me.ni;};")
# ---- 바로 가기 링크: seoul.html?food=1 → 명동 민호 앞에서 대화창 열림 ----
rep("go(nextQ()?nextQ().q.sc:'icn',nextQ()?nextQ().q.at:0);requestAnimationFrame(frame);","const DEEP=/[?&#]food/.test(location.search+location.hash);if(DEEP){go('myd',.33);const n=cur.npcs.find(x=>x.id==='cit0');if(n){const p=n.rig.position;placeAt(nearestIdx(p.x,p.z),true);}}else go(nextQ()?nextQ().q.sc:'icn',nextQ()?nextQ().q.at:0);requestAnimationFrame(frame);")
rep("if(AIP){const k=AIP;AIP=null;setTimeout(()=>showAI(k),700);}if(cur.notes[0]){say(cur.notes[0][1]);firedN.add(0);}};","if(AIP&&!DEEP){const k=AIP;AIP=null;setTimeout(()=>showAI(k),700);}if(DEEP){AIP=null;setTimeout(()=>{const n=cur.npcs.find(x=>x.id==='cit0');if(n)openTalk(n);},800);}else if(cur.notes[0]){say(cur.notes[0][1]);firedN.add(0);}};")
# ---- 공개용: 서울 페이지에서는 '가족 암호' 창(이메일 노출)을 띄우지 않음. 암호를 이미 넣은 가족 브라우저에서만 AI 대화 ----
rep('<script>window.WEB_SITE="seoul";</script>','<script>window.WEB_SITE="seoul";window.__askedCode=true;</script>')
rep('<a href="index.html" aria-label="처음 화면">🏠</a>','')
# ---- 대화창에서 내 말 이름표: 영어 화면이면 'Me' ----
rep("addLine('나',q,true);","addLine(L('Me','나'),q,true);")
# ---- 크루즈 시절 문구 정리 (가방 · 스탬프 결과 · 돈 부족) ----
rep("openPanel('가방',(b)=>{const p=document.createElement('p');p.className='lead';p.textContent='게임 속 돈은 가상 유로예요.';b.append(p);","openPanel(L('Bag','가방'),(b)=>{const p=document.createElement('p');p.className='lead';p.textContent=L('Money in the game is virtual won.','게임 속 돈은 가상 원화예요.');b.append(p);")
rep("w.innerHTML='<div><small>지갑</small><b>₩'+G.eur.toLocaleString()+'</b></div><div><small>카지노 칩</small><b>'+G.chips+'</b></div><div><small>스탬프</small><b>'+updStamps()+'/6</b></div>';","w.innerHTML='<div><small>'+L('Wallet','지갑')+'</small><b>₩'+G.eur.toLocaleString()+'</b></div><div><small>'+L('Stamps','스탬프')+'</small><b>'+updStamps()+'/'+STAMPS.length+'</b></div>';")
rep("h.textContent='산 물건';","h.textContent=L('Things you bought','산 물건');")
rep("e.textContent='아직 산 물건이 없어요. 면세점이나 기항지 가게에서 사 보세요.';","e.textContent=L('Nothing yet. Buy something at a shop or stall.','아직 산 물건이 없어요. 가게나 노점에서 사 보세요.');")
rep("rs.textContent='처음부터 다시 시작';let arm=0;rs.onclick=()=>{if(!arm){arm=1;rs.textContent='정말 지울까요? 한 번 더 누르면 지워져요';return;}","rs.textContent=L('Start over','처음부터 다시 시작');let arm=0;rs.onclick=()=>{if(!arm){arm=1;rs.textContent=L('Erase everything? Tap again to confirm.','정말 지울까요? 한 번 더 누르면 지워져요');return;}")
rep("(n===STAMPS.length?'여섯 항구 스탬프를 모두 모았어요. 일주일 지중해 여행 끝!':'하선 완료. 스탬프 '+n+'/6 — 일정에서 빠진 항구로 다시 가 볼 수 있어요.'):'항구마다 명소 끝에서 스탬프를 찍어요. 이 기기에 저장돼요.'","(n===STAMPS.length?'스탬프를 모두 모았어요. 여행 끝! 실제 여행도 즐겁게 다녀오세요.':'여행 완료! 스탬프 '+n+'/'+STAMPS.length+' — 일정에서 빠진 곳에 다시 가 볼 수 있어요.'):'곳마다 끝에서 스탬프를 찍어요. 이 기기에 저장돼요.'")
rep("say('가상 유로가 모자라요. 카지노에서 따거나, 가방에서 처음부터 다시 시작할 수 있어요.');","say(L('Not enough money. You can start over from the bag (🎒).','돈이 모자라요. 가방(🎒)에서 처음부터 다시 시작할 수 있어요.'));")
rep("(stamped[s.id]?'':'<br>빈칸')","(stamped[s.id]?'':'<br>'+L('empty','빈칸'))")
# ---- 가게 버튼 · 가게 주인 말: 크루즈 시절 '젤라토' · '유로' 문구 정리 (음식 노점 버튼이 '젤라토 주문'으로 보이던 것) ----
rep("s:s.k==='gelato'?'젤라토 주문':'구경하고 사기'","s:s.k==='gelato'?'주문하기':'구경하고 사기'")
rep("['젤라토 주문','Order']","['주문하기','Order']")
rep("손님에게 물건이나 젤라토를 권하고 동네 이야기를 해 준다.","손님에게 메뉴와 물건을 권하고 동네 이야기를 해 준다.")
s=s.replace("가격은 게임 속 가상 유로.","가격은 게임 속 가상 원화.")
# ---- 날씨: 맑은 밤에는 해 대신 달 ----
rep("current=temperature_2m,weather_code&timezone","current=temperature_2m,weather_code,is_day&timezone")
rep("c>=2?'☁':'☀';","c>=2?'☁':WX.is_day===0?'🌙':'☀';")
# ---- 지역 고르기 (첫 화면): 서울 · 부산·경남 · 준비 중인 지역 ----
rep('<p class="route" id="stR"></p>','<p class="route" id="stR"></p><div id="stReg" class="reg"></div>\n<style>.reg{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:0 0 16px}.reg .h{width:100%;font-size:12px;opacity:.75}.reg a,.reg span{font-size:12.5px;line-height:1.2;padding:6px 11px;border-radius:999px;border:1px solid rgba(255,255,255,.35);color:#fff;text-decoration:none}.reg a.on{background:var(--brass);color:var(--navy);border-color:var(--brass);font-weight:700}.reg span{opacity:.45}</style>')
REGJS=r"""const REG_ID='seoul';const REGIONS=[['seoul','seoul.html',L('Seoul','서울')],['busan','busan.html',L('Busan · Gyeongnam','부산·경남')],['east','east.html',L('East coast','동해안')],['jnm','jnm.html',L('Jeonnam · Gwangju','전남·광주')],['cbk','',L('Chungbuk','충북')],['cnm','',L('Chungnam · Daejeon','충남·대전')],['gbk','',L('Gyeongbuk · Daegu','경북·대구')],['jbk','',L('Jeonbuk','전북')],['ggi','',L('Gyeonggi','경기')]];
{const r=$('stReg');if(r){const h=document.createElement('div');h.className='h';h.textContent=L('Choose a region','지역 고르기');r.append(h);REGIONS.forEach(([id,f,n])=>{let e;if(id===REG_ID){e=document.createElement('a');e.className='on';e.textContent=n;}else if(f){e=document.createElement('a');e.href=f;e.textContent=n;}else{e=document.createElement('span');e.textContent=n+' · '+L('soon','준비 중');}r.append(e);});}}
"""
_m=re.search(r"\$\('stR'\)\.textContent=L\('(?:[^'\\]|\\.)*','(?:[^'\\]|\\.)*'\);",s);assert _m
s=s[:_m.end()]+REGJS+s[_m.end():]
# ---- 휴대폰 화면 맞춤 (없으면 휴대폰이 980px 데스크톱 폭으로 그려 글자·버튼이 아주 작아짐) ----
if '<meta name="viewport"' not in s:
    s='<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+s
# ---- HTML 문서 틀 (<html>, <head>, <body>) ----
# 클라우드플레어 방문 통계는 배포할 때 측정 코드를 <head>/<body> 자리에 자동으로 붙임.
# 틀이 없으면 붙일 자리가 없어 방문이 0으로만 찍힘.
# <!doctype html>은 일부러 넣지 않음: 넣으면 표준 모드로 바뀌어 위쪽 안내판이 5~10px 내려감
# (2026-11-13 비교 시험). 틀만 넣으면 브라우저가 만드는 화면은 지금과 똑같음.
if '<head>' not in s[:300]:
    i=s.index('</style>')+len('</style>')   # 맨 앞 설정·글꼴·스타일까지가 머리(head)
    assert '<canvas id="c">' in s[i:] and '<canvas' not in s[:i]
    s='<html>\n<head>\n'+s[:i]+'\n</head>\n<body>\n'+s[i:].lstrip('\n')+'\n</body>\n</html>\n'
open(S+'seoul.html','w',encoding='utf8').write(s);print('ok',len(s))
