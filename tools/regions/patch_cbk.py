# 가상 충북 2박 3일 (cbk.html): 단양 · 제천 · 청주, 서울역 출발 · 서울고속버스터미널 도착
# 공통 생성기(region_base.py)가 서울 엔진을 받고, 이 파일의 자료로 바꿔 끼웁니다.
# 사실 출처(2026-11-18 확인):
#  KTX-이음 서울역→단양 일반실 20,200원, 서울역 출발 하루 3회(10:59·12:55·16:11), 1시간 46~52분 (info.koreacharts.com 2026-11-05 시간표)
#  KTX-이음 청량리→단양 18,600원, 하루 6회 05:40~19:00, 1시간 20~29분 (train.asamaru.net 2026-11-18)
#  단양구경시장 마늘 먹거리(흑마늘 닭강정 등), 시내버스 배차 길어 택시도 현실적 (travelmapjourney 2026-10-06, trvlogue)
#  단양강 잔도 편도 약 1.12km(30분), 무료, 야간 조명 (travelmapjourney 2026-10-06)
#  도담삼봉 입장 무료(시설 이용료 별도), 주차 소형 3,000원, 09:00~18:00(시설별 상이), 연중무휴, 단양팔경 제1경, 삼도정, 이황·김홍도 (ktriptips 2026-11-11)
#  만천하스카이워크 어른 4,000원, 하절기 09:00~18:00(매표 17:00)·동절기 09:00~17:00(매표 16:00), 남한강 절벽 80~90m, 짚와이어 980m, 알파인코스터 1,000m (ktriptips 2026-11-11),
#   주차장 셔틀버스 화요일 미운행 (ktriptips 2026-09-04), 4~10월 하절기·11~3월 동절기 (travelmapjourney 2026-10-06). 휴무일은 출처마다 달라 적지 않음.
#  단양→제천 기차 14~16분, 무궁화 2,600·ITX-마음 4,800·KTX-이음 8,400원, 하루 12회 (asamaru 2026-11-18)
#  의림지 무료·상시·연중무휴, 삼한시대 축조, 우륵·박의림 이야기 (ktriptips 2026-11-11); 제천역에서 31·35번 등 약 20분 (trvlogue 2026-09-23, travelmapjourney 2026-10-02)
#  청풍호반케이블카 일반 캐빈 어른 왕복 18,000원·크리스탈 23,000원, 2.3km, 편도 약 10분, 09:30~18:00(매표 17:30, 달마다 바뀜) (ktriptips 2026-10-28, trvlogue 2026-10-30)
#  제천버스터미널→청주시외버스터미널 하루 2회(09:25·13:50), 2시간 17~48분, 12,700원 (asamaru 2026-11-10); 제천→청주역 기차 하루 12회 1시간 21~31분, 무궁화 7,000원 (asamaru 2026-11-18)
#  수암골 무료·상시(21시 이후 방문 자제), 6·25 피란민 마을, 2007년 공공미술, 드라마 촬영지, 노을 (ktriptips 2026-11-03)
#  청주고인쇄박물관 무료, 09:00~18:00, 월요일·1월 1일 휴관, 직지 (ktriptips 2026-04-15); 직지 1377년 청주 흥덕사 금속활자, 프랑스 국립도서관 소장, 2001년 세계기록유산 (BnF)
#  국립현대미술관 청주 1~4층 무료·5층 기획전 2,000원, 10:00~18:00(입장 17:00), 월요일·1월 1일 휴관, 옛 연초제조창, 2018년 개관 (ktriptips 2025-10-24)
#  청주고속버스터미널→서울고속버스터미널(경부) 하루 76회 05:40~23:10, 약 2시간 4분, 일반 9,900·우등 14,500·프리미엄 18,800원 (asamaru 2026-11-07)
#  서울고속버스터미널: 경부·영동선 방면, 고속터미널역 3·7·9호선 (서울시 내 손안에 서울)
import os,sys
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
sys.path.insert(0,S)
from region_base import Region
R=dict(id='cbk',title='Virtual Chungbuk · 가상 충북 3일',money=300000,metro='ktx',start='sst',
 top=['K_region_top.js','K_jnm_top.js','K_cbk_top.js'],br=['K_region_br.js','K_cbk_br.js'],ph='ph/PH_cbk.json',
 enter=('Start at Seoul Station','서울역에서 시작하기'),hotel=('Danyang','단양'),
 hotel_note=('Your hotel room for tonight: Danyang on night 1, Cheongju on night 2.','오늘 밤 묵을 호텔 방이에요. 첫날 밤은 단양, 둘째 날 밤은 청주예요.'),
 chip=('Good garlic dakgangjeong place nearby?','마늘 닭강정 맛집 어디예요?'),deep=('dyt',.33),eyebrow='SEOUL → DANYANG · JECHEON · CHEONGJU',
 stH=('Virtual Chungbuk<br>3 days','가상 충북<br>2박 3일'),wx=('36.9845','128.3655'),city_name=('Chungbuk','충북'),
 stamps_title=('Chungbuk stamps','충북 스탬프'),guide_role=('Your Chungbuk tour guide','충북 여행 가이드'),
 course_ko='충북 2박 3일 코스',guide_line=('Ask me anything about Danyang, Jecheon and Cheongju!','단양·제천·청주에 대해 무엇이든 물어보세요!'),
 virtual=('Virtual Chungbuk','가상 충북','가상 충북으로'))

R['stamps']="""const STAMPS=[{id:'dds',name:L('Dodamsambong','도담삼봉'),date:'D1',c:'#2f8a6a'},{id:'mch',name:L('Mancheonha','만천하'),date:'D1',c:'#2e8fd0'},{id:'ulj',name:L('Uirimji','의림지'),date:'D2',c:'#4f9a3a'},{id:'cpc',name:L('Cheongpung Lake','청풍호'),date:'D2',c:'#1f6fa8'},{id:'sag',name:L('Suamgol','수암골'),date:'D2',c:'#e8833a'},{id:'cjk',name:L('Cheongju · Jikji','청주 · 직지'),date:'D3',c:'#8a5a2a'}];
"""

R['scn']="""const SCN={
 sst:{b:'seoul',o:{city:'sst'},name:L('Seoul Station · KTX','서울역 · KTX')},dyt:{b:'seoul',o:{city:'dyt'},name:L('Danyang · Gugyeong Market · Jando','단양 · 구경시장 · 잔도')},
 dds:{b:'seoul',o:{city:'dds'},name:L('Dodamsambong','도담삼봉')},mch:{b:'seoul',o:{city:'mch'},name:L('Mancheonha Skywalk','만천하스카이워크')},
 ulj:{b:'seoul',o:{city:'ulj'},name:L('Jecheon · Uirimji','제천 · 의림지')},cpc:{b:'seoul',o:{city:'cpc'},name:L('Cheongpung Lake Cable Car','청풍호반케이블카')},
 sag:{b:'seoul',o:{city:'sag'},name:L('Cheongju · Suamgol','청주 · 수암골')},cjk:{b:'seoul',o:{city:'cjk'},name:L('Early Printing Museum · MMCA Cheongju','청주고인쇄박물관 · 국립현대미술관 청주')},
 nbu:{b:'seoul',o:{city:'nbu'},name:L('Seoul Express Bus Terminal','서울고속버스터미널')},hotel:{b:'hotel',name:L('Hotel room · Danyang / Cheongju','호텔 방 · 단양 / 청주')},ride:{b:'ride',name:''}};
const SHIPMAP=[['sst',L('Seoul Station','서울역'),'KTX-이음'],['dyt',L('Danyang','단양'),'KTX-이음'],['dds',L('Dodamsambong','도담삼봉'),L('Taxi','택시')],['mch',L('Mancheonha','만천하'),L('Taxi','택시')],['ulj',L('Uirimji','의림지'),L('Train + bus','기차 + 버스')],['cpc',L('Cheongpung Lake','청풍호'),L('Taxi','택시')],['sag',L('Suamgol','수암골'),L('Intercity bus','시외버스')],['cjk',L('Cheongju museums','청주 박물관'),L('Bus · taxi','버스·택시')],['nbu',L('Seoul Express Bus Terminal','서울고속버스터미널'),L('Express bus','고속버스')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

"""

R['days']="""const DAYS=[
 {tag:'DAY 1',title:L('Seoul → Danyang','서울 출발 · 단양'),time:L('Seoul Station KTX-Eum (about 1 h 46 min+) → Danyang → Gugyeong Market → Dodamsambong → Mancheonha Skywalk → night walk on the Jando','서울역 KTX-이음(약 1시간 46분~) → 단양 → 구경시장 → 도담삼봉 → 만천하스카이워크 → 잔도 밤 산책'),q:[
  {t:'',n:L('Find your train on the departure board','전광판에서 열차 확인'),sc:'sst',at:.45,near:1,r:'sst'},
  {t:'',n:L('Board the KTX-Eum to Danyang (₩20,200)','단양행 KTX-이음 타기 (20,200원)'),sc:'sst',at:.82,a:'ktx',r:'ktx'},
  {t:'',n:L('Lunch at Gugyeong Market: garlic snacks','구경시장 점심: 마늘 먹거리'),sc:'dyt',at:.33,a:'eat_gm',r:'gugyeong'},
  {t:'',n:L('Bus or taxi to Dodamsambong','버스·택시로 도담삼봉'),sc:'dyt',at:.45,a:'l_dds'},
  {t:'',n:L('The three peaks of Dodamsambong','도담삼봉 세 봉우리'),sc:'dds',at:.45,near:1,r:'dodam'},
  {t:'',n:L('Dodamsambong stamp','도담삼봉 스탬프'),sc:'dds',at:.97,a:'stamp'},
  {t:'',n:L('Taxi to Mancheonha Skywalk','택시로 만천하스카이워크'),sc:'dds',at:.92,a:'l_mch'},
  {t:'',n:L('Up the skywalk (₩4,000)','스카이워크 오르기 (4,000원)'),sc:'mch',at:.3,a:'msky',r:'mancheonha'},
  {t:'',n:L('Mancheonha stamp','만천하 스탬프'),sc:'mch',at:.99,a:'stamp'},
  {t:'',n:L('Back to Danyang town','단양 읍내로'),sc:'mch',at:.04,a:'l_dyt'},
  {t:'',n:L('Night walk on the Danyanggang Jando','단양강 잔도 밤 산책'),sc:'dyt',at:.8,near:1,r:'jando'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Jecheon → Cheongju','제천 · 청주'),time:L('Train Danyang → Jecheon (about 15 min) → Uirimji → taxi to the Cheongpung Lake Cable Car → intercity bus to Cheongju → Suamgol at sunset','기차로 단양 → 제천(약 15분) → 의림지 → 택시로 청풍호반케이블카 → 시외버스로 청주 → 해 질 녘 수암골'),q:[
  {t:'',n:L('Train to Jecheon (₩2,600)','제천 가는 기차 (2,600원)'),sc:'dyt',at:.04,a:'t_jcn',r:'jcntrain'},
  {t:'',n:L('Walk around Uirimji','의림지 둘레길 걷기'),sc:'ulj',at:.45,near:1,r:'uirimji'},
  {t:'',n:L('Uirimji stamp','의림지 스탬프'),sc:'ulj',at:.97,a:'stamp'},
  {t:'',n:L('Taxi to the cable car','택시로 케이블카'),sc:'ulj',at:.92,a:'l_cpc'},
  {t:'',n:L('Cable car up Bibongsan (₩18,000)','비봉산 케이블카 (18,000원)'),sc:'cpc',at:.3,a:'cpcable',r:'cpcable'},
  {t:'',n:L('Cheongpung Lake stamp','청풍호 스탬프'),sc:'cpc',at:.99,a:'stamp'},
  {t:'',n:L('Intercity bus to Cheongju (₩12,700)','청주 가는 시외버스 (12,700원)'),sc:'cpc',at:.06,a:'b_cj',r:'cjbus'},
  {t:'',n:L('Suamgol mural village','수암골 벽화마을'),sc:'sag',at:.6,near:1,r:'suamgol'},
  {t:'',n:L('Suamgol stamp','수암골 스탬프'),sc:'sag',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Cheongju · back to Seoul','청주 · 서울로'),time:L('Early Printing Museum (Jikji) → MMCA Cheongju → express bus to Seoul (about 2 h 4 min)','청주고인쇄박물관(직지) → 국립현대미술관 청주 → 고속버스로 서울(약 2시간 4분)'),q:[
  {t:'',n:L('Bus or taxi to the Early Printing Museum','버스·택시로 고인쇄박물관'),sc:'sag',at:.04,a:'l_cjk'},
  {t:'',n:L('Jikji, printed in 1377','1377년에 찍은 직지'),sc:'cjk',at:.28,a:'jikji',r:'jikji'},
  {t:'',n:L('MMCA Cheongju (free)','국립현대미술관 청주 (무료)'),sc:'cjk',at:.62,near:1,r:'mmca'},
  {t:'',n:L('Cheongju stamp','청주 스탬프'),sc:'cjk',at:.97,a:'stamp'},
  {t:'',n:L('Express bus to Seoul (₩9,900)','서울 가는 고속버스 (9,900원)'),sc:'cjk',at:.93,a:'bus_sel',r:'cjexp'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'nbu',at:.85,a:'trip'}]}];

"""

R['city']="""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1500,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 sst:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'ktx',n:L('KTX-Eum to Danyang','단양행 KTX-이음'),fare:20200,ride:{kind:'train',scen:'country',title:L('KTX-Eum Seoul → Danyang','KTX-이음 서울 → 단양'),col:'#1f4f91',stops:[L('Seoul','서울'),L('Cheongnyangni','청량리'),L('Danyang','단양')],gap:900,vmax:45,intro:L('🚆 KTX-Eum to Danyang, standard class ₩20,200: 3 trains a day from Seoul Station (Nov 2026), about 1 h 46–52 min. Cheongnyangni has more (6 a day, ₩18,600).','🚆 단양행 KTX-이음, 일반실 20,200원. 서울역에서 하루 3회(2026년 11월 기준), 약 1시간 46~52분. 청량리역에서는 하루 6회, 18,600원이에요.'),dest:{sc:'dyt',at:0}}},
   st('eat_sst',.3,-1,L('Station kiosk','역 매점'),L('Clerk','직원'),[[L('Gimbap roll','김밥 한 줄'),4000],[L('Bottled water','생수'),1200],[L('Coffee','커피'),4500]],'🥤')],
  sights:[{t:.14,side:1,id:'sst'},{t:.75,side:-1,id:'ktx'}],
  shows:[{id:'cyr',t:.2,b:L('🚉 More trains from Cheongnyangni','🚉 청량리역에서 더 많이 떠나요'),s:L('Jungang Line KTX-Eum','중앙선 KTX-이음'),say:L('Only 3 KTX-Eum trains a day go from Seoul Station to Danyang (Nov 2026). From Cheongnyangni there are 6, 05:40–19:00, about 1 h 20–29 min, ₩18,600.','서울역에서 단양 가는 KTX-이음은 하루 3회예요(2026년 11월 기준). 청량리역에서는 하루 6회(05:40~19:00), 약 1시간 20~29분, 18,600원이에요.')}],
  cit:[{t:.5,n:L('Jihun','지훈'),role:L('Korail station staff','코레일 역무원'),p:'서울역 역무원. KTX 표 사는 곳(코레일톡 앱·매표창구·자동발매기), 전광판 보는 법, 호차와 좌석 찾기를 안내한다. 서울역에서 단양까지 KTX-이음 일반실 20,200원, 하루 3회(2026년 11월 5일 기준 10:59·12:55·16:11), 약 1시간 46~52분. 중앙선 KTX-이음은 청량리역에서 더 많이 떠나고(하루 6회, 05:40~19:00) 청량리→단양은 18,600원, 약 1시간 20~29분이다.'}]},
 dyt:{noBoard:1,spots:[{t:.04,side:1,k:'shuttle',id:'t_jcn',n:L('Train to Jecheon','제천 가는 기차'),fare:2600,ride:{kind:'train',scen:'country',title:L('Train Danyang → Jecheon','기차 단양 → 제천'),col:'#c8202a',stops:[L('Danyang','단양'),L('Jecheon','제천')],gap:600,vmax:22,intro:L('🚆 Danyang → Jecheon: 14–16 min, 12 trains a day. Mugunghwa ₩2,600, ITX-Maeum ₩4,800, KTX-Eum ₩8,400. From Jecheon Station, city buses 31 or 35 go to Uirimji in about 20 min.','🚆 단양 → 제천 14~16분, 하루 12회. 무궁화 2,600원, ITX-마음 4,800원, KTX-이음 8,400원. 제천역에서 시내버스 31·35번 등으로 의림지까지 약 20분.'),dest:{sc:'ulj',at:0}}},
   st('eat_gm',.33,-1,L('Garlic dakgangjeong shop','마늘 닭강정 가게'),L('Owner','사장님'),[[L('Black-garlic dakgangjeong (small box)','흑마늘 닭강정 (작은 상자)'),15000],[L('Garlic bread','마늘빵'),4000],[L('Garlic sundae','마늘 순대'),8000]],'🍗')],
  links:[{t:.45,id:'l_dds',n:L('🚕 Bus or taxi to Dodamsambong','🚕 도담삼봉까지 버스·택시'),s:L('Buses are infrequent','버스 배차가 길어요'),to:'dds',at:0}],
  sights:[{t:.27,side:1,id:'gugyeong'},{t:.75,side:-1,id:'jando'}],doors:[{t:.5,side:-1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  cit:[{t:.4,n:L('Mrs. Kim','김 사장님'),role:L('Gugyeong Market vendor','구경시장 상인'),p:'단양구경시장에서 마늘 먹거리를 파는 상인. 단양 마늘로 만든 흑마늘 닭강정·마늘빵·마늘 순대를 권하고, 도담삼봉(입장 무료, 단양팔경 제1경)과 만천하스카이워크(어른 4,000원), 밤에 조명이 켜지는 단양강 잔도(편도 약 1.12km, 무료)를 안내한다. 시내버스는 배차가 길어 택시가 편할 때가 많다고 말한다. 메뉴 가격은 게임 속 예시다.'}]},
 dds:{noBoard:1,spots:[],links:[{t:.92,id:'l_mch',n:L('🚕 Taxi to Mancheonha Skywalk','🚕 만천하스카이워크까지 택시'),s:L('Jeokseong-myeon, Danyang','단양 적성면'),to:'mch',at:0}],
  sights:[{t:.45,side:-1,id:'dodam'}],
  cit:[{t:.6,n:L('Mr. Choi','최 선생님'),role:L('Danyang culture guide','단양 문화관광해설사'),p:'도담삼봉의 문화관광해설사. 남한강 가운데 솟은 세 봉우리가 단양팔경 제1경이고, 가장 큰 봉우리 위 정자가 삼도정이라고 설명한다. 퇴계 이황과 단원 김홍도 같은 조선의 선비·화가가 이곳을 글과 그림으로 남겼다. 입장 무료, 연중무휴, 09:00~18:00(시설마다 다름), 주차 소형차 3,000원.'}]},
 mch:{noBoard:1,spots:[],links:[{t:.04,id:'l_dyt',n:L('🚕 Taxi back to Danyang town','🚕 단양 읍내로 택시'),s:L('Jando night walk','잔도 밤 산책'),to:'dyt',at:.6}],
  sights:[{t:.25,side:1,id:'mancheonha'}],
  lifts:[{id:'msky',y:30,ic:'🗼',down:L('🗼 Walk back down','🗼 걸어서 내려가기'),n:L('Mancheonha Skywalk','만천하스카이워크'),fare:4000,msg:L('Up the spiral ramp around the tower…','탑을 감싼 나선형 길을 따라 올라가요…'),top:L('Three glass-floored decks stick out over a cliff 80–90 m above the Namhan River.','유리 바닥 전망대 세 갈래가 남한강 위 80~90m 절벽 밖으로 뻗어 있어요.')}],
  cit:[{t:.12,n:L('Ms. Jang','장 매니저'),role:L('Skywalk staff','스카이워크 직원'),p:'만천하스카이워크 직원. 어른 4,000원, 하절기(4~10월) 09:00~18:00(매표 17:00까지), 동절기(11~3월) 09:00~17:00(매표 16:00까지)라고 안내한다. 남한강 절벽 80~90m 높이에 유리 전망대가 있고, 짚와이어(980m)·알파인코스터(1,000m)·슬라이드는 따로 요금을 낸다. 주차장 셔틀버스는 화요일에 운행하지 않는다. 날씨가 나쁘면 운영이 멈출 수 있다.'}]},
 ulj:{noBoard:1,spots:[],links:[{t:.92,id:'l_cpc',n:L('🚕 Taxi to the Cheongpung Lake Cable Car','🚕 청풍호반케이블카까지 택시'),s:L('Cheongpung-myeon, Jecheon','제천 청풍면'),to:'cpc',at:0}],
  sights:[{t:.45,side:-1,id:'uirimji'}],
  cit:[{t:.6,n:L('Mr. Han','한 선생님'),role:L('Jecheon local','제천 시민'),p:'의림지를 산책하는 제천 시민. 의림지는 삼한 시대에 만들었다고 전하는 저수지로 입장 무료에 늘 열려 있고, 신라 진흥왕 때 우륵이 처음 둑을 쌓았고 뒤에 현감 박의림이 고쳐 쌓았다는 이야기를 들려준다. 제천역에서 시내버스 31·35번 등으로 약 20분, 청풍호반케이블카는 택시로 가는 것이 편하다고 말한다.'}]},
 cpc:{noBoard:1,spots:[{t:.06,side:1,k:'bus',id:'b_cj',n:L('Intercity bus to Cheongju','청주 가는 시외버스'),fare:12700,ride:{kind:'bus',scen:'country',title:L('Intercity bus Jecheon → Cheongju','시외버스 제천 → 청주'),col:'#2e5a86',stops:[L('Jecheon Bus Terminal','제천버스터미널'),L('Cheongju Intercity Bus Terminal','청주시외버스터미널')],gap:1300,vmax:30,intro:L('🚌 Take a taxi to Jecheon Bus Terminal. Intercity buses to Cheongju run only twice a day (09:25 and 13:50): 2 h 17 min–2 h 48 min, ₩12,700. Or take the train Jecheon → Cheongju Station: 1 h 21–31 min, 12 a day, Mugunghwa ₩7,000. In Cheongju, a taxi or city bus to Suamgol.','🚌 택시로 제천버스터미널에 가요. 청주 가는 시외버스는 하루 2회(09:25, 13:50)뿐이고 2시간 17분~2시간 48분, 12,700원. 기차를 타도 돼요: 제천 → 청주역 1시간 21~31분, 하루 12회, 무궁화 7,000원. 청주에서는 택시나 시내버스로 수암골에 가요.'),dest:{sc:'sag',at:0}}}],
  sights:[{t:.2,side:-1,id:'cpcable'}],
  lifts:[{id:'cpcable',y:57,ic:'🚡',down:L('🚡 Cable car down','🚡 케이블카로 내려가기'),n:L('Cheongpung Lake Cable Car','청풍호반케이블카'),fare:18000,msg:L('The cable car climbs 2.3 km to the top of Bibongsan: about 10 minutes…','케이블카가 비봉산 정상까지 2.3km를 올라가요. 약 10분…'),top:L('Cheongpung Lake spreads out below like an inland sea.','발아래로 청풍호가 바다처럼 펼쳐져요.')}],
  cit:[{t:.3,n:L('Ms. Seo','서 매니저'),role:L('Cable car staff','케이블카 직원'),p:'청풍호반케이블카 직원. 물태리역에서 비봉산 정상까지 2.3km, 편도 약 10분. 일반 캐빈 어른 왕복 18,000원, 바닥이 투명한 크리스탈 캐빈 왕복 23,000원. 운영은 09:30~18:00(매표 17:30까지)이지만 달마다, 날씨에 따라 바뀔 수 있어 누리집을 확인하라고 안내한다.'}]},
 sag:{noBoard:1,spots:[st('eat_sag',.5,-1,L('Hillside café','언덕 카페'),L('Barista','바리스타'),[[L('Americano','아메리카노'),4500],[L('Hot chocolate','핫초코'),5500]],'☕')],
  links:[{t:.04,id:'l_cjk',n:L('🚌 Bus or taxi to the Early Printing Museum','🚌 고인쇄박물관까지 버스·택시'),s:L('Heungdeok-gu, Cheongju','청주 흥덕구'),to:'cjk',at:0}],
  sights:[{t:.66,side:-1,id:'suamgol'}],doors:[{t:.1,side:-1,to:'hotel',n:L('Hotel in Cheongju','청주 호텔'),lab:'HOTEL'}],
  cit:[{t:.4,n:L('Mr. Yoon','윤 사장님'),role:L('Suamgol café owner','수암골 카페 사장님'),p:'수암골에서 카페를 하는 사장님. 6·25 전쟁 뒤 피란민이 모여 살던 마을이 2007년 공공미술 프로젝트로 벽화를 그리며 다시 살아났고, 드라마 촬영지로 알려졌다고 이야기한다. 입장 무료, 늘 열려 있지만 주민이 사니 21시 이후 방문은 삼가 달라고 부탁한다. 해 질 녘 청주 시내 풍경을 권한다.'}]},
 cjk:{noBoard:1,spots:[{t:.93,side:-1,k:'bus',id:'bus_sel',n:L('Express bus to Seoul Express Bus Terminal','서울고속버스터미널 가는 고속버스'),fare:9900,ride:{kind:'bus',scen:'country',title:L('Express bus Cheongju → Seoul','고속버스 청주 → 서울'),col:'#2e5a86',stops:[L('Cheongju Express Bus Terminal','청주고속버스터미널'),L('Seoul Express Bus Terminal','서울고속버스터미널')],gap:1200,vmax:30,intro:L('🚌 Cheongju Express Bus Terminal → Seoul Express Bus Terminal (Gyeongbu Line): 76 buses a day, 05:40–23:10, about 2 h 4 min. Standard ₩9,900, premium ₩14,500, Premium ₩18,800.','🚌 청주고속버스터미널 → 서울고속버스터미널(경부선): 하루 76회, 05:40~23:10, 약 2시간 4분. 일반 9,900원, 우등 14,500원, 프리미엄 18,800원.'),dest:{sc:'nbu',at:0}}}],
  sights:[{t:.18,side:1,id:'jikji'},{t:.62,side:-1,id:'mmca'},{t:.86,side:1,id:'cjexp'}],
  shows:[{id:'jikji',t:.28,b:L('📜 Jikji, printed in 1377','📜 1377년에 찍은 직지'),s:L('Metal movable type','금속활자'),say:L('Jikji was printed in 1377 at Heungdeoksa temple in Cheongju, with cast metal movable type. Its only surviving volume is kept at the National Library of France in Paris, and it has been on UNESCO’s Memory of the World Register since 2001.','직지는 1377년 청주 흥덕사에서 금속활자로 찍은 책이에요. 남아 있는 한 권은 프랑스 국립도서관(파리)에 있고, 2001년 유네스코 세계기록유산이 됐어요.')}],
  cit:[{t:.4,n:L('Ms. Park','박 해설사'),role:L('Museum guide','박물관 해설사'),p:'청주고인쇄박물관 해설사. 직지는 1377년 청주 흥덕사에서 금속활자로 찍었고, 남아 있는 한 권(하권)은 프랑스 국립도서관에 있으며 2001년 유네스코 세계기록유산이 됐다고 설명한다. 박물관은 입장 무료, 09:00~18:00, 매주 월요일과 1월 1일 휴관. 국립현대미술관 청주(내덕동, 옛 연초제조창, 1~4층 무료, 10:00~18:00, 월요일 휴관)도 권한다.'}]},
 nbu:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'seoulexp'}],cit:[{t:.55,n:L('Ms. Lim','임 선생님'),role:L('Terminal information desk','터미널 안내원'),p:'서울고속버스터미널 안내원. 경부·영동선 방면 고속버스가 서는 터미널이고, 고속터미널역에서 지하철 3·7·9호선으로 갈아탈 수 있다고 안내한다. 호남선 방면은 바로 옆 센트럴시티에서 탄다.'}],fin:{t:.85,s:L('3 days in Chungbuk','충북 2박 3일')}}};

"""

R['info']='const CRUISE_INFO="이 게임은 여행자가 서울역에서 KTX-이음을 타고 단양에 가서 2박 3일 동안 단양·제천·청주를 돌고 고속버스로 서울고속버스터미널에 돌아오는 가상 3D 여행이다. 1일: 서울역 KTX-이음(단양까지 일반실 20,200원, 서울역 출발 하루 3회 10:59·12:55·16:11, 약 1시간 46~52분, 2026년 11월 기준; 청량리역 출발이 더 많아 하루 6회 05:40~19:00, 18,600원, 약 1시간 20~29분) → 단양역(시내버스 배차가 길어 택시가 편할 때가 많음) → 단양구경시장(단양 마늘 먹거리: 흑마늘 닭강정·마늘빵·마늘 순대) → 버스·택시로 도담삼봉(남한강 가운데 세 봉우리, 단양팔경 제1경, 큰 봉우리 위 정자 삼도정, 이황·김홍도가 글과 그림으로 남김; 입장 무료, 연중무휴, 09:00~18:00 시설마다 다름, 주차 소형차 3,000원) → 택시로 만천하스카이워크(단양 적성면; 어른 4,000원; 4~10월 09:00~18:00 매표 17:00, 11~3월 09:00~17:00 매표 16:00; 남한강 절벽 80~90m 위 유리 전망대 세 갈래, 나선형 길; 짚와이어 980m·알파인코스터 1,000m·슬라이드는 별도 요금; 주차장 셔틀버스 화요일 미운행; 날씨가 나쁘면 운영 중단 가능) → 단양 읍내 → 밤에 단양강 잔도(남한강 절벽 데크길, 편도 약 1.12km 30분, 무료, 야간 조명) → 단양 호텔. 2일: 기차로 단양 → 제천(14~16분, 하루 12회, 무궁화 2,600원·ITX-마음 4,800원·KTX-이음 8,400원) → 제천역에서 시내버스 31·35번 등 약 20분 → 의림지(삼한 시대에 만들었다고 전하는 저수지, 신라 우륵·현감 박의림 이야기; 입장 무료, 상시 개방, 연중무휴) → 택시로 청풍호반케이블카(제천 청풍면 물태리역 → 비봉산 정상 2.3km, 편도 약 10분; 일반 캐빈 어른 왕복 18,000원, 크리스탈 캐빈 23,000원; 09:30~18:00 매표 17:30, 달마다·날씨에 따라 바뀜; 정상에서 청풍호가 바다처럼 보임) → 택시로 제천버스터미널 → 청주 시외버스(하루 2회 09:25·13:50, 2시간 17~48분, 12,700원) 또는 기차 제천→청주역(하루 12회, 1시간 21~31분, 무궁화 7,000원·ITX-마음 10,400원) → 수암골(우암산 자락 벽화마을, 6·25 피란민 마을, 2007년 공공미술 프로젝트로 벽화, 드라마 촬영지, 카페, 해 질 녘 청주 시내 풍경; 무료, 상시, 21시 이후 방문 자제) → 청주 호텔. 3일: 버스·택시로 청주고인쇄박물관(흥덕구 직지대로 713; 무료, 09:00~18:00, 매주 월요일·1월 1일 휴관; 직지: 1377년 청주 흥덕사에서 금속활자로 찍은 책, 남은 한 권은 프랑스 국립도서관 소장, 2001년 유네스코 세계기록유산) → 국립현대미술관 청주(청원구 상당로 314 내덕동, 옛 청주 연초제조창, 2018년 개관; 1~4층 무료, 5층 기획전 2,000원; 10:00~18:00 입장 17:00; 매주 월요일·1월 1일 휴관) → 청주고속버스터미널 → 서울고속버스터미널(경부선; 하루 76회 05:40~23:10, 약 2시간 4분, 일반 9,900원·우등 14,500원·프리미엄 18,800원) → 고속터미널역(지하철 3·7·9호선). 게임 속 식사·가게 가격은 예시다.";\n'

R['real']="""const REAL={
 sst:{n:L('Seoul Station','서울역'),sub:L('KTX-Eum to Danyang','단양행 KTX-이음'),ll:[37.5555,126.9707],q:'Seoul Station',f:[L('3 KTX-Eum trains a day leave here for Danyang (Nov 2026). Cheongnyangni Station has 6 a day.','단양 가는 KTX-이음이 하루 3회 여기서 떠나요(2026년 11월 기준). 청량리역에서는 하루 6회.'),L('The domed red-brick old station (1925) is now Culture Station Seoul 284.','붉은 벽돌 돔의 옛 서울역(1925)은 지금 문화역서울284예요.')]},
 ktx:{n:L('KTX-Eum','KTX-이음'),sub:L('Seoul → Danyang','서울 → 단양'),q:'단양역',f:[L('Standard class from Seoul Station ₩20,200, about 1 h 46–52 min (3 a day: 10:59, 12:55, 16:11 on 5 Nov 2026).','서울역에서 일반실 20,200원, 약 1시간 46~52분(2026년 11월 5일 기준 하루 3회 10:59·12:55·16:11).'),L('From Cheongnyangni: ₩18,600, about 1 h 20–29 min, 6 a day (05:40–19:00).','청량리역에서: 18,600원, 약 1시간 20~29분, 하루 6회(05:40~19:00).'),L('Back from Danyang to Seoul Station: 4 a day, about 1 h 52–58 min, ₩20,200.','단양에서 서울역으로: 하루 4회, 약 1시간 52~58분, 20,200원.')]},
 gugyeong:{n:L('Danyang Gugyeong Market','단양구경시장'),sub:L('Garlic snacks','마늘 먹거리'),q:'단양구경시장',f:[L('Danyang is known for garlic: try black-garlic dakgangjeong, garlic bread or garlic sundae.','단양은 마늘로 유명해요. 흑마늘 닭강정, 마늘빵, 마늘 순대를 먹어 봐요.'),L('Popular shops can have long queues at weekends.','주말에는 인기 가게 줄이 길 수 있어요.')]},
 jando:{n:L('Danyanggang Jando','단양강 잔도'),sub:L('Cliff-side walkway','절벽 데크길'),q:'단양강 잔도',f:[L('A deck path fixed to the cliff above the Namhan River: about 1.12 km one way (about 30 min). Free.','남한강 절벽에 붙여 만든 데크길이에요. 편도 약 1.12km(약 30분). 무료.'),L('Lit up after dark, it is a popular night walk.','해가 지면 조명이 켜져 밤 산책으로 인기예요.')]},
 dodam:{n:L('Dodamsambong','도담삼봉'),sub:L('First of the Eight Views of Danyang','단양팔경 제1경'),q:'도담삼봉',f:[L('Three rock peaks in the Namhan River; the pavilion on the largest is Samdojeong.','남한강 가운데 세 바위 봉우리예요. 가장 큰 봉우리 위 정자가 삼도정이에요.'),L('Free; open every day, 09:00–18:00 (each facility differs). Parking: small cars ₩3,000.','입장 무료, 연중무휴, 09:00~18:00(시설마다 달라요). 주차 소형차 3,000원.'),L('A national scenic site and part of the Danyang National Geopark.','국가 명승이자 단양 국가지질공원의 명소예요.')]},
 mancheonha:{n:L('Mancheonha Skywalk','만천하스카이워크'),sub:L('Glass decks above the Namhan River','남한강 위 유리 전망대'),q:'만천하스카이워크',f:[L('Adult ₩4,000. Apr–Oct 09:00–18:00 (tickets until 17:00); Nov–Mar 09:00–17:00 (tickets until 16:00).','어른 4,000원. 4~10월 09:00~18:00(매표 17:00까지), 11~3월 09:00~17:00(매표 16:00까지).'),L('On a cliff 80–90 m above the river. Zipwire (980 m), alpine coaster (1,000 m) and slide cost extra.','강 위 80~90m 절벽에 있어요. 짚와이어(980m), 알파인코스터(1,000m), 슬라이드는 따로 요금을 내요.'),L('The shuttle bus from the car park does not run on Tuesdays; bad weather can close the site.','주차장 셔틀버스는 화요일에 다니지 않아요. 날씨가 나쁘면 운영이 멈출 수 있어요.')]},
 jcntrain:{n:L('Danyang → Jecheon train','단양 → 제천 기차'),sub:L('Jungang Line','중앙선'),q:'단양역',f:[L('14–16 minutes, 12 trains a day. Mugunghwa ₩2,600, ITX-Maeum ₩4,800, KTX-Eum ₩8,400. (Nov 2026)','14~16분, 하루 12회. 무궁화 2,600원, ITX-마음 4,800원, KTX-이음 8,400원. (2026년 11월 기준)')]},
 uirimji:{n:L('Uirimji','의림지'),sub:L('Ancient reservoir, Jecheon','제천의 오래된 저수지'),q:'제천 의림지',f:[L('Said to date from the Samhan period. Free, always open.','삼한 시대에 만들었다고 전해요. 입장 무료, 늘 열려 있어요.'),L('Legend: the musician Ureuk first built the bank in Silla times; magistrate Park Ui-rim later rebuilt it.','신라 때 우륵이 처음 둑을 쌓았고, 뒤에 현감 박의림이 고쳐 쌓았다는 이야기가 전해요.'),L('From Jecheon Station: city buses 31 or 35, about 20 minutes.','제천역에서 시내버스 31·35번 등으로 약 20분.')]},
 cpcable:{n:L('Cheongpung Lake Cable Car','청풍호반케이블카'),sub:L('Multae-ri → Bibongsan','물태리 → 비봉산'),q:'청풍호반케이블카',f:[L('Standard cabin: adult ₩18,000 round trip. Crystal (glass floor): ₩23,000.','일반 캐빈 어른 왕복 18,000원. 크리스탈(투명 바닥) 23,000원.'),L('2.3 km to the top of Bibongsan, about 10 minutes one way.','비봉산 정상까지 2.3km, 편도 약 10분.'),L('09:30–18:00 (tickets until 17:30); hours change by month and weather.','09:30~18:00(매표 17:30까지). 달마다, 날씨에 따라 바뀌어요.')]},
 cjbus:{n:L('Jecheon → Cheongju','제천 → 청주'),sub:L('Bus or train','버스 또는 기차'),q:'제천버스터미널',f:[L('Intercity bus: only 2 a day (09:25, 13:50), 2 h 17 min–2 h 48 min, ₩12,700.','시외버스: 하루 2회(09:25, 13:50)뿐, 2시간 17분~2시간 48분, 12,700원.'),L('Train Jecheon → Cheongju Station: 12 a day, 1 h 21–31 min. Mugunghwa ₩7,000, ITX-Maeum ₩10,400. (Nov 2026)','기차 제천 → 청주역: 하루 12회, 1시간 21~31분. 무궁화 7,000원, ITX-마음 10,400원. (2026년 11월 기준)')]},
 suamgol:{n:L('Suamgol Mural Village','수암골 벽화마을'),sub:L('Cheongju','청주'),q:'청주 수암골',f:[L('Free, always open, but people live here: please avoid visiting after 21:00.','입장 무료, 늘 열려 있어요. 주민이 사는 곳이라 21시 이후 방문은 삼가요.'),L('Refugees settled here after the Korean War; a 2007 public art project added the murals.','6·25 전쟁 뒤 피란민이 모여 살던 마을에 2007년 공공미술 프로젝트로 벽화가 생겼어요.'),L('Known as a drama filming location, with a sunset view over central Cheongju.','드라마 촬영지로 알려졌고, 해 질 녘 청주 시내 풍경이 좋아요.')]},
 jikji:{n:L('Cheongju Early Printing Museum','청주고인쇄박물관'),sub:L('Home of Jikji','직지의 고장'),q:'청주고인쇄박물관',f:[L('Free. 09:00–18:00; closed Mondays and 1 January.','입장 무료. 09:00~18:00, 매주 월요일과 1월 1일 휴관.'),L('Jikji was printed in 1377 at Heungdeoksa in Cheongju with metal movable type.','직지는 1377년 청주 흥덕사에서 금속활자로 찍은 책이에요.'),L('Its only surviving volume is at the National Library of France in Paris. UNESCO Memory of the World since 2001.','남아 있는 한 권은 프랑스 국립도서관(파리)에 있어요. 2001년 유네스코 세계기록유산.')]},
 mmca:{n:L('MMCA Cheongju','국립현대미술관 청주'),sub:L('In the old tobacco factory','옛 연초제조창'),q:'국립현대미술관 청주',f:[L('Floors 1–4 free; 5th-floor special exhibitions ₩2,000.','1~4층 무료, 5층 기획전 2,000원.'),L('10:00–18:00 (last entry 17:00). Closed Mondays and 1 January.','10:00~18:00(입장 17:00까지). 매주 월요일과 1월 1일 휴관.'),L('Opened in 2018 in the rebuilt Cheongju tobacco factory, Naedeok-dong.','2018년 내덕동 옛 청주 연초제조창을 고쳐 문을 열었어요.')]},
 cjexp:{n:L('Cheongju → Seoul express bus','청주 → 서울 고속버스'),sub:L('Cheongju Express Bus Terminal','청주고속버스터미널'),q:'청주고속버스터미널',f:[L('To Seoul Express Bus Terminal (Gyeongbu Line): 76 a day, 05:40–23:10, about 2 h 4 min.','서울고속버스터미널(경부선)까지 하루 76회, 05:40~23:10, 약 2시간 4분.'),L('Standard ₩9,900, premium ₩14,500, Premium ₩18,800. (Nov 2026)','일반 9,900원, 우등 14,500원, 프리미엄 18,800원. (2026년 11월 기준)')]},
 seoulexp:{n:L('Seoul Express Bus Terminal','서울고속버스터미널'),sub:L('Gyeongbu · Yeongdong lines','경부·영동선'),q:'서울고속버스터미널',f:[L('Express buses to Gyeonggi, Chungcheong, Gyeongsang and Gangwon arrive here.','경기·충청·경상·강원 방면 고속버스가 서는 터미널이에요.'),L('Change at Express Bus Terminal Station: subway Lines 3, 7 and 9.','고속터미널역에서 지하철 3·7·9호선으로 갈아타요.')]},
};
"""

R['qz']="""const QZ={
 sst:[[/KTX-Eum to Danyang|단양행 KTX-이음/,'cq1',L('How much is a standard-class KTX-Eum ticket from Seoul Station to Danyang?','서울역 → 단양 KTX-이음 일반실 요금은?'),['₩10,200','₩20,200','₩40,200'],1,L('₩20,200 (₩18,600 from Cheongnyangni).','20,200원이에요(청량리에서는 18,600원).')]],
 dyt:[[/Garlic dakgangjeong|마늘 닭강정/,'cq2',L('Which Danyang crop goes into many Gugyeong Market snacks?','구경시장 먹거리에 많이 들어가는 단양 특산물은?'),[L('Garlic','마늘'),L('Tangerines','귤'),L('Seaweed','김')],0,L('Garlic: black-garlic dakgangjeong, garlic bread and more.','마늘이에요. 흑마늘 닭강정, 마늘빵 같은 먹거리가 많아요.')]],
 dds:[[/Mancheonha|만천하/,'cq3',L('What is the pavilion on the largest Dodamsambong peak called?','도담삼봉 가장 큰 봉우리 위 정자 이름은?'),[L('Samdojeong','삼도정'),L('Gyeonghoeru','경회루'),L('Chokseongnu','촉석루')],0,L('Samdojeong.','삼도정이에요.')]],
 mch:[[/🗼 (Mancheonha|만천하)/,'cq4',L('How much is adult admission to Mancheonha Skywalk?','만천하스카이워크 어른 입장료는?'),['₩4,000','₩14,000','₩40,000'],0,L('₩4,000. The zipwire and coaster cost extra.','4,000원이에요. 짚와이어와 코스터는 따로 내요.')]],
 ulj:[[/Cheongpung|청풍/,'cq5',L('Uirimji is said to date from which period?','의림지는 언제 만들었다고 전해질까요?'),[L('The Samhan period','삼한 시대'),L('The Joseon dynasty','조선 시대'),L('The 1970s','1970년대')],0,L('The Samhan period, before the Three Kingdoms.','삼국 시대 전, 삼한 시대예요.')]],
 cpc:[[/🚡 (Cheongpung|청풍)/,'cq6',L('How much is a standard-cabin round trip for an adult?','일반 캐빈 어른 왕복 요금은?'),['₩8,000','₩18,000','₩28,000'],1,L('₩18,000 (Crystal cabin ₩23,000).','18,000원이에요(크리스탈 캐빈 23,000원).')]],
 sag:[[/📷 (Suamgol|수암골)/,'cq7',L('When did the Suamgol murals begin?','수암골 벽화는 언제 그리기 시작했을까요?'),['1957','1987','2007'],2,L('In 2007, with a public art project.','2007년 공공미술 프로젝트로 시작했어요.')]],
 cjk:[[/📜/,'cq8',L('Where is the only surviving volume of Jikji kept today?','지금 남아 있는 직지 한 권은 어디에 있을까요?'),[L('National Library of France, Paris','프랑스 국립도서관(파리)'),L('British Museum, London','영국박물관(런던)'),L('Tokyo National Museum','도쿄국립박물관')],0,L('In Paris, at the National Library of France. Printed in Cheongju in 1377.','파리의 프랑스 국립도서관에 있어요. 1377년 청주에서 찍었어요.')],
  [/Seoul Express Bus Terminal|서울고속버스터미널 가는/,'cq9',L('About how long is the express bus from Cheongju to Seoul?','청주 → 서울 고속버스는 약 얼마나 걸리나요?'),[L('About 2 h','약 2시간'),L('About 4 h','약 4시간'),L('About 6 h','약 6시간')],0,L('About 2 h 4 min; 76 buses a day.','약 2시간 4분이에요. 하루 76회 다녀요.')]]};
"""

R['rem']="h(L('Remember','꼭 기억할 것'));[L('KTX-Eum Seoul Station → Danyang ₩20,200 · 3 a day · more from Cheongnyangni (₩18,600)','KTX-이음 서울역 → 단양 20,200원 · 하루 3회 · 청량리 출발이 더 많아요(18,600원)'),L('Danyang town buses are infrequent: taxis help','단양 시내버스는 배차가 길어요 · 택시가 편해요'),L('Dodamsambong free · Mancheonha Skywalk ₩4,000 (winter 09:00–17:00)','도담삼봉 무료 · 만천하스카이워크 4,000원(겨울 09:00~17:00)'),L('Danyang → Jecheon train 14–16 min · Uirimji free','단양 → 제천 기차 14~16분 · 의림지 무료'),L('Cheongpung Lake Cable Car ₩18,000 round trip','청풍호반케이블카 왕복 18,000원'),L('Jecheon → Cheongju bus only 2 a day (09:25, 13:50) · or train','제천 → 청주 시외버스 하루 2회(09:25, 13:50) · 기차도 있어요'),L('Cheongju museums free · closed Mondays','청주 박물관·미술관 무료 · 월요일 휴관'),L('Express bus Cheongju → Seoul ₩9,900 · about 2 h 4 min','고속버스 청주 → 서울 9,900원 · 약 2시간 4분'),"

R['areako']="const AREAKO={sst:'서울역',ktx:'단양역',gugyeong:'단양구경시장',jando:'단양강 잔도',dodam:'단양 도담삼봉',mancheonha:'단양 만천하스카이워크',jcntrain:'단양역',uirimji:'제천 의림지',cpcable:'제천 청풍호반케이블카',cjbus:'제천버스터미널',suamgol:'청주 수암골',jikji:'청주고인쇄박물관',mmca:'국립현대미술관 청주',cjexp:'청주고속버스터미널',seoulexp:'서울고속버스터미널'};"

R['foods']="""
  {k:'흑마늘 닭강정',e:'black-garlic dakgangjeong',s:'Garlic chicken',ic:'🍗',re:/닭강정|dakgangjeong/i},
  {k:'마늘빵',e:'garlic bread',s:'Garlic bread',ic:'🥖',re:/마늘빵|garlic bread/i},
  {k:'마늘 순대',e:'garlic sundae',s:'Garlic sundae',ic:'🌭',re:/순대|sundae/i},
  {k:'올갱이국',e:'olgaengi-guk (marsh snail soup)',s:'Snail soup',ic:'🍲',re:/올갱이|olgaengi|snail/i},
  {k:'짜글이',e:'jjageuri (pork stew)',s:'Pork stew',ic:'🥘',re:/짜글이|jjageuri/i},"""

R['phrase']="['단양역 어디예요?','Danyang-yeok eodi-yeyo?',L('Where is Danyang Station?','단양역 어디예요?')]"
R['stP']="$('stP').textContent=L('Take the KTX-Eum from Seoul Station to Danyang. Eat garlic snacks at Gugyeong Market, see the three river peaks of Dodamsambong, step onto the glass decks of Mancheonha Skywalk and walk the cliff-side Jando at night. Visit the ancient Uirimji reservoir in Jecheon, ride the cable car above Cheongpung Lake, watch the sunset from Suamgol in Cheongju and see the story of Jikji before the express bus back to Seoul. Real fares, times and photos.','서울역에서 KTX-이음으로 단양에 가요. 구경시장에서 마늘 먹거리를 먹고, 남한강의 도담삼봉과 만천하스카이워크 유리 전망대를 보고, 밤에는 절벽 잔도를 걸어요. 제천의 오래된 저수지 의림지와 청풍호 케이블카, 청주 수암골의 노을과 직지 이야기를 보고 고속버스로 서울에 돌아와요. 실제 요금·시간·사진을 담았어요.');"
R['stR']="$('stR').textContent=L('Seoul Station · KTX-Eum · Danyang · Gugyeong Market · Dodamsambong · Mancheonha Skywalk · Jando · Jecheon · Uirimji · Cheongpung Lake Cable Car · Cheongju · Suamgol · Early Printing Museum · MMCA Cheongju · Seoul Express Bus Terminal','서울역 · KTX-이음 · 단양 · 구경시장 · 도담삼봉 · 만천하스카이워크 · 잔도 · 제천 · 의림지 · 청풍호반케이블카 · 청주 · 수암골 · 고인쇄박물관 · 국립현대미술관 청주 · 서울고속버스터미널');"
R['rgn']="const RGN={ktx:'KTX-이음  단양 DANYANG',sst0:L('Seoul Station. KTX-Eum trains to Danyang leave from here (3 a day). Buy tickets on the Korail Talk app, at a ticket window or a ticket machine.','서울역이에요. 단양 가는 KTX-이음이 여기서 떠나요(하루 3회). 표는 코레일톡 앱, 매표창구, 자동발매기에서 사요.'),sst8:L('KTX-Eum Seoul → Danyang: ₩20,200 in standard class, about 1 h 46–52 min.','KTX-이음 서울 → 단양: 일반실 20,200원, 약 1시간 46~52분.'),term:'서울고속버스터미널 · SEOUL EXPRESS BUS TERMINAL',line:'3 7 9 고속터미널 · EXPRESS BUS TERMINAL',lineCol:'#ef7c1c',termNotes:[[0,L('Seoul Express Bus Terminal. Welcome back to Seoul!','서울고속버스터미널이에요. 서울에 돌아왔어요!')],[.5,L('Express Bus Terminal Station: subway Lines 3, 7 and 9.','고속터미널역에서 지하철 3·7·9호선으로 갈아타요.')]]};"
r=Region(S);r.build(R);r.save('cbk.html')
