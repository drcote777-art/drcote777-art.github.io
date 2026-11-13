# 가상 전남·광주 2박 3일 (jnm.html): 광주 · 담양 · 순천만 · 여수, 서울역 출발 · 용산역 도착
# 공통 생성기(region_base.py)가 서울 엔진을 받고, 이 파일의 자료로 바꿔 끼웁니다.
# 사실 출처(2026-11 확인):
#  KTX 서울역→광주송정 일반실 42,400원, 서울역 출발 하루 5~6회 06:22~19:29, 최단 2시간 3분 (train.asamaru.net 2026-11-13)
#  KTX·SRT 통합(2026-09-01)으로 용산→광주송정 46,800→42,000원 (MTN 2026-09-07, 이투데이)
#  전남광주통합특별시 2026-07-01 출범, 약 316만 명 (경향신문 2026-06-01)
#  광주 도시철도 1호선 교통카드 1,250원·현금 1,400원 (2025-05 요금표) · 광주 시내버스 교통카드 1,250원 (아시아경제 2026-07-08)
#  5·18민주광장: ACC 앞, 상시 개방, 1980년 5월 14~16일 민족민주화대성회, 분수대·상무관·시계탑 보존, 민주의 종(2005) (ktriptips 2026-11-11)
#  옛 전남도청: 5·18 최후 항쟁지, 2026-05-18 복원 공개, 6개 건물 1980년 5월 모습, 본관 총탄 자국 (더팩트 2026-05-18)
#  ACC 실내 보통 10:00~18:00, 월요일·1월 1일 휴관, 바깥 06:00~22:00 (travelmapjourney 2026-10-21, 공식 안내 인용)
#  광주→담양 시외버스 30~40분 하루 41회 06:17~21:37, 시내버스 311번 06:20~22:05 (travelmapjourney 2026-06)
#  죽녹원 어른 3,000원, 11~2월 09:00~18:00(입장 마감 17:30), 연중무휴, 산책로 2.2km 8가지 길 (ktriptips 2026-09-28)
#  관방제림 무료·상시, 1648년 성이성, 약 2km 185그루 (travelmapjourney 2026-06)
#  광주종합버스터미널→순천 시외버스 하루 24회, 약 1시간 13분, 일반 9,200원·우등 12,000원 (asamaru 2026-11-06)
#  순천만국가정원 어른 10,000원(같은 날 순천만습지 입장), 10~6월 09:00~20:00 입장 마감 19:00, 매월 마지막 주 월요일 휴무 (ktriptips 2026-11-11, NOL 2026)
#  순천만습지 탐방로 입구→용산전망대 약 1.5km 25~30분 (travelmapjourney 2026-05)
#  순천→여수EXPO 기차 19~26분, 무궁화 2,600·ITX 4,800·KTX 7,500원, 하루 35~39회 (asamaru 2026-11-12)
#  오동도 무료·상시, 동백열차 편도 1,000원(11~2월 들어가는 열차 09:30~17:00, 30분 간격, 12~13시 운휴), 동백꽃 2월 중순~3월 중순, 남쪽 끝 등대 (ktriptips 2026-11-11)
#  여수 해상케이블카 일반 캐빈 어른 왕복 17,000원·편도 14,000원, 크리스탈 24,000원, 09:30~21:30, 자산 정류장은 오동도 입구 근처 (ktriptips 2026-06-30, trvlogue 2026-10)
#  KTX 여수EXPO→용산 하루 23~26회 05:05~21:54, 최단 2시간 50분, 일반실 45,400원 (asamaru 2026-11-13)
import os,sys
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
sys.path.insert(0,S)
from region_base import Region
R=dict(id='jnm',title='Virtual Jeonnam · Gwangju · 가상 전남·광주 3일',money=300000,metro='gjmetro',start='sst',
 top=['K_region_top.js','K_jnm_top.js'],br=['K_region_br.js','K_jnm_br.js'],ph='ph/PH_jnm.json',
 enter=('Start at Seoul Station','서울역에서 시작하기'),hotel=('Gwangju','광주'),
 hotel_note=('Your hotel room for tonight: Gwangju on night 1, Suncheon on night 2.','오늘 밤 묵을 호텔 방이에요. 첫날 밤은 광주, 둘째 날 밤은 순천이에요.'),
 chip=('Good tteokgalbi place nearby?','떡갈비 맛집 어디예요?'),deep=('dmy',.5),eyebrow='SEOUL → GWANGJU · SUNCHEON · YEOSU',
 stH=('Virtual Jeonnam<br>3 days','가상 전남·광주<br>2박 3일'),wx=('35.1595','126.8526'),city_name=('Gwangju','광주'),
 stamps_title=('Jeonnam · Gwangju stamps','전남·광주 스탬프'),guide_role=('Your Jeonnam · Gwangju tour guide','전남·광주 여행 가이드'),
 course_ko='전남·광주 2박 3일 코스',guide_line=('Ask me anything about Gwangju, Damyang, Suncheon and Yeosu!','광주·담양·순천·여수에 대해 무엇이든 물어보세요!'),
 virtual=('Virtual Jeonnam','가상 전남·광주','가상 전남·광주로'))

R['stamps']="""const STAMPS=[{id:'acc',name:L('Gwangju','광주'),date:'D1',c:'#e83a5a'},{id:'dmy',name:L('Damyang','담양'),date:'D1',c:'#4f9a3a'},{id:'scw',name:L('Suncheon Bay','순천만'),date:'D2',c:'#c99a3a'},{id:'odo',name:L('Odongdo','오동도'),date:'D3',c:'#d8202a'},{id:'ycb',name:L('Yeosu','여수'),date:'D3',c:'#2e8fd0'}];
"""

R['scn']="""const SCN={
 sst:{b:'seoul',o:{city:'sst'},name:L('Seoul Station · KTX','서울역 · KTX')},gsj:{b:'seoul',o:{city:'gsj'},name:L('Gwangju Songjeong Station','광주송정역')},
 acc:{b:'seoul',o:{city:'acc'},name:L('May 18 Democracy Square · ACC','5·18민주광장 · 국립아시아문화전당')},dmy:{b:'seoul',o:{city:'dmy'},name:L('Damyang Juknokwon · Gwanbangjerim','담양 죽녹원 · 관방제림')},
 scw:{b:'seoul',o:{city:'scw'},name:L('Suncheonman Bay Wetland','순천만습지')},odo:{b:'seoul',o:{city:'odo'},name:L('Yeosu EXPO Station · Odongdo','여수EXPO역 · 오동도')},
 ycb:{b:'seoul',o:{city:'ycb'},name:L('Yeosu Maritime Cable Car','여수 해상케이블카')},sar:{b:'seoul',o:{city:'sar'},name:L('Yongsan Station','용산역')},
 hotel:{b:'hotel',name:L('Hotel room · Gwangju / Suncheon','호텔 방 · 광주 / 순천')},ride:{b:'ride',name:''}};
const SHIPMAP=[['sst',L('Seoul Station','서울역'),'KTX'],['gsj',L('Gwangju Songjeong','광주송정'),'KTX'],['acc',L('May 18 Square · ACC','5·18광장 · ACC'),L('Line 1','1호선')],['dmy',L('Damyang','담양'),L('Bus','버스')],['scw',L('Suncheon Bay','순천만'),L('Intercity bus','시외버스')],['odo',L('Odongdo','오동도'),L('Train','기차')],['ycb',L('Cable car','케이블카'),L('Walk','걷기')],['sar',L('Yongsan','용산'),'KTX'],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

"""

R['days']="""const DAYS=[
 {tag:'DAY 1',title:L('Seoul → Gwangju · Damyang','서울 출발 · 광주 · 담양'),time:L('Seoul Station KTX (about 2 h 3 min+) → Gwangju Songjeong → Line 1 → May 18 Democracy Square · Old Provincial Office · ACC → bus to Damyang Juknokwon','서울역 KTX(약 2시간 3분~) → 광주송정역 → 지하철 1호선 → 5·18민주광장 · 옛 전남도청 · ACC → 버스로 담양 죽녹원'),q:[
  {t:'',n:L('Find your train on the departure board','전광판에서 열차 확인'),sc:'sst',at:.45,near:1,r:'sst'},
  {t:'',n:L('Board the KTX to Gwangju Songjeong (₩42,400)','광주송정행 KTX 타기 (42,400원)'),sc:'sst',at:.82,a:'ktx',r:'ktx'},
  {t:'',n:L('Subway Line 1 to Munhwajeondang','지하철 1호선으로 문화전당역'),sc:'gsj',at:.8,a:'m_acc',r:'gjmetro'},
  {t:'',n:L('The fountain and clock tower of May 1980','1980년 5월의 분수대와 시계탑'),sc:'acc',at:.3,near:1,r:'may18'},
  {t:'',n:L('Old South Jeolla Provincial Office','옛 전남도청'),sc:'acc',at:.55,near:1,r:'oldoffice'},
  {t:'',n:L('Asia Culture Center (ACC)','국립아시아문화전당(ACC)'),sc:'acc',at:.85,near:1,r:'acc'},
  {t:'',n:L('Gwangju stamp','광주 스탬프'),sc:'acc',at:.97,a:'stamp'},
  {t:'',n:L('Bus to Damyang','버스로 담양'),sc:'acc',at:.05,a:'b_dmy',r:'dmybus'},
  {t:'',n:L('Juknokwon ticket (₩3,000)','죽녹원 입장권 (3,000원)'),sc:'dmy',at:.04,a:'tk_jnk',r:'juknok'},
  {t:'',n:L('Walk the bamboo paths','대숲 산책로 걷기'),sc:'dmy',at:.4,near:1},
  {t:'',n:L('Lunch: tteokgalbi','점심: 떡갈비'),sc:'dmy',at:.55,a:'eat_tg'},
  {t:'',n:L('Gwanbangjerim riverside forest','관방제림 둑길 숲'),sc:'dmy',at:.85,near:1,r:'gwanbang'},
  {t:'',n:L('Damyang stamp','담양 스탬프'),sc:'dmy',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Suncheon Bay','순천만'),time:L('Intercity bus Gwangju → Suncheon (about 1 h 13 min) → Suncheonman Bay Wetland: reed boardwalk · Yongsan Observatory (one ticket with the National Garden)','시외버스 광주 → 순천(약 1시간 13분) → 순천만습지: 갈대 데크길 · 용산전망대 (국가정원과 같은 입장권)'),q:[
  {t:'',n:L('Intercity bus to Suncheon (₩9,200)','순천 가는 시외버스 (9,200원)'),sc:'acc',at:.06,a:'b_scn',r:'scbus'},
  {t:'',n:L('Suncheon Bay ticket (₩10,000)','순천만 입장권 (10,000원)'),sc:'scw',at:.08,a:'tk_scw',r:'scgarden'},
  {t:'',n:L('Dinner: mudskipper soup or cockles','저녁: 짱뚱어탕 또는 꼬막'),sc:'scw',at:.14,a:'eat_jd'},
  {t:'',n:L('Boardwalk through the reeds','갈대밭 데크길'),sc:'scw',at:.4,near:1,r:'scbay'},
  {t:'',n:L('Yongsan Observatory','용산전망대'),sc:'scw',at:.98,near:1},
  {t:'',n:L('Suncheon Bay stamp','순천만 스탬프'),sc:'scw',at:.99,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Yeosu · back to Seoul','여수 · 서울로'),time:L('Train Suncheon → Yeosu EXPO (about 20 min) → Odongdo → Maritime Cable Car → KTX to Yongsan (2 h 50 min+)','기차로 순천 → 여수EXPO(약 20분) → 오동도 → 해상케이블카 → KTX로 용산(2시간 50분~)'),q:[
  {t:'',n:L('Train to Yeosu EXPO (₩2,600)','여수EXPO 가는 기차 (2,600원)'),sc:'scw',at:.04,a:'t_ysu',r:'ysutrain'},
  {t:'',n:L('Breakwater road to Odongdo','오동도 방파제 길'),sc:'odo',at:.5,near:1,r:'odongdo'},
  {t:'',n:L('Camellia forest and lighthouse','동백숲과 등대'),sc:'odo',at:.95,near:1},
  {t:'',n:L('Odongdo stamp','오동도 스탬프'),sc:'odo',at:.97,a:'stamp'},
  {t:'',n:L('Walk to the cable car','케이블카 타는 곳으로'),sc:'odo',at:.38,a:'l_ycb'},
  {t:'',n:L('Cable car over the sea (₩17,000)','바다 위 케이블카 (17,000원)'),sc:'ycb',at:.3,a:'ycable',r:'ycable'},
  {t:'',n:L('Yeosu stamp','여수 스탬프'),sc:'ycb',at:.99,a:'stamp'},
  {t:'',n:L('KTX to Yongsan (₩45,400)','용산 가는 KTX (45,400원)'),sc:'ycb',at:.08,a:'ktx_ys',r:'ktxys'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'sar',at:.85,a:'trip'}]}];

"""

R['city']="""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1250,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 sst:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'ktx',n:L('KTX to Gwangju Songjeong','광주송정행 KTX'),fare:42400,ride:{kind:'train',scen:'country',title:L('KTX Seoul → Gwangju Songjeong','KTX 서울 → 광주송정'),col:'#1f4f91',stops:[L('Seoul','서울'),L('Gwangju Songjeong','광주송정')],gap:900,vmax:50,intro:L('🚆 KTX to Gwangju Songjeong, standard class ₩42,400. The fastest trains take about 2 h 3 min. (Stops differ by train.)','🚆 광주송정행 KTX, 일반실 42,400원. 가장 빠른 열차는 약 2시간 3분이에요. (정차역은 열차마다 달라요.)'),dest:{sc:'gsj',at:0}}},
   st('eat_sst',.3,-1,L('Station kiosk','역 매점'),L('Clerk','직원'),[[L('Gimbap roll','김밥 한 줄'),4000],[L('Bottled water','생수'),1200],[L('Coffee','커피'),4500]],'🥤')],
  sights:[{t:.14,side:1,id:'sst'},{t:.75,side:-1,id:'ktx'}],
  shows:[{id:'ysn',t:.2,b:L('🚉 More trains from Yongsan','🚉 용산역에서 더 많이 떠나요'),s:L('Honam Line KTX','호남선 KTX'),say:L('From Seoul Station only 5–6 KTX trains a day go to Gwangju Songjeong (Nov 2026); most leave from Yongsan, ₩42,000. Fares fell on 1 Sept 2026, when KTX and SRT merged.','서울역에서 광주송정 가는 KTX는 하루 5~6회예요(2026년 11월 기준). 대부분은 용산역에서 떠나고 요금은 42,000원이에요. 2026년 9월 1일 KTX·SRT 통합으로 요금이 내렸어요.')}],
  cit:[{t:.5,n:L('Jihun','지훈'),role:L('Korail station staff','코레일 역무원'),p:'서울역 역무원. KTX 표 사는 곳(코레일톡 앱·매표창구·자동발매기), 전광판 보는 법, 호차와 좌석 찾기를 안내한다. 서울역에서 광주송정까지 일반실 42,400원, 하루 5~6회(06:22~19:29, 2026년 11월 기준), 가장 빠른 열차 약 2시간 3분. 호남선 KTX는 용산역에서 더 많이 떠나고 용산→광주송정은 42,000원이다. 2026년 9월 1일 KTX·SRT 통합으로 요금이 약 10% 내렸다.'}]},
 gsj:{noBoard:1,spots:[mt('m_acc',.8,1,L('Line 1 to Munhwajeondang','1호선 문화전당역 방면'),L('Gwangju Metro Line 1','광주 지하철 1호선'),'#2e8fd0',[L('Gwangju Songjeong','광주송정역'),L('Sangmu','상무'),L('Geumnamno 4-ga','금남로4가'),L('Munhwajeondang','문화전당')],{sc:'acc',at:0},L('🚇 Gwangju Metro Line 1 to Munhwajeondang (Asia Culture Center). Fare ₩1,250 by transport card, ₩1,400 cash.','🚇 광주 지하철 1호선으로 문화전당역(아시아문화전당)까지 가요. 교통카드 1,250원, 현금 1,400원.')),
   st('eat_gsj',.45,-1,L('Station café','역 카페'),L('Barista','바리스타'),[[L('Americano','아메리카노'),4500],[L('Bottled water','생수'),1200]],'☕')],
  sights:[{t:.36,side:1,id:'gsj'},{t:.62,side:-1,id:'gjmetro'}],
  cit:[{t:.55,n:L('Minji','민지'),role:L('Gwangju local','광주 시민'),p:'광주송정역에서 만난 친절한 광주 시민. 지하철 1호선으로 문화전당역 가는 법(교통카드 1,250원), 2026년 7월 1일 광주와 전남이 합쳐 전남광주통합특별시가 된 이야기, 광주 상추튀김과 떡갈비를 이야기한다.'}]},
 acc:{noBoard:1,spots:[{t:.05,side:1,k:'bus',id:'b_dmy',n:L('Bus to Damyang','담양 가는 버스'),fare:1250,ride:{kind:'bus',scen:'country',title:L('Bus Gwangju → Damyang','버스 광주 → 담양'),col:'#2fae6a',stops:[L('Gwangju','광주'),L('Damyang','담양'),L('Juknokwon','죽녹원')],gap:800,vmax:22,intro:L('🚌 Intercity buses from Gwangju Bus Terminal (U-Square) reach Damyang in about 30–40 min (41 a day, 06:17–21:37). City bus 311 runs too: Gwangju base fare ₩1,250 by card; the fare to Damyang may differ.','🚌 광주종합버스터미널(유스퀘어)에서 담양 가는 시외버스로 약 30~40분(하루 41회, 06:17~21:37). 시내버스 311번도 다녀요. 광주 시내버스 기본요금은 교통카드 1,250원이고, 담양까지는 요금이 다를 수 있어요.'),dest:{sc:'dmy',at:0}}},
   {t:.06,side:-1,k:'bus',id:'b_scn',n:L('Intercity bus to Suncheon','순천 가는 시외버스'),fare:9200,ride:{kind:'bus',scen:'country',title:L('Intercity bus Gwangju → Suncheon','시외버스 광주 → 순천'),col:'#2e5a86',stops:[L('Gwangju Bus Terminal (U-Square)','광주종합버스터미널(유스퀘어)'),L('Suncheon Bus Terminal','순천종합버스터미널'),L('Suncheonman Bay','순천만')],gap:1100,vmax:30,intro:L('🚌 From Gwangju Bus Terminal (U-Square): 24 buses a day, about 1 h 13 min, standard ₩9,200 (premium ₩12,000). Then a city bus or taxi to Suncheonman Bay.','🚌 광주종합버스터미널(유스퀘어)에서 하루 24회, 약 1시간 13분, 일반 9,200원(우등 12,000원). 순천에서 시내버스나 택시로 순천만에 가요.'),dest:{sc:'scw',at:0}}}],
  sights:[{t:.22,side:-1,id:'may18'},{t:.5,side:-1,id:'oldoffice'},{t:.78,side:-1,id:'acc'}],doors:[{t:.97,side:1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  cit:[{t:.4,n:L('Mr. Park','박 선생님'),role:L('May 18 culture guide','5·18 해설사'),p:'5·18민주광장의 해설사. 1980년 5월 14~16일 이 광장에서 학생과 시민이 민족민주화대성회를 열었고, 분수대와 시계탑, 상무관이 그때 모습으로 남아 있다고 설명한다. 옛 전남도청은 5·18 최후 항쟁지로, 2026년 5월 18일 복원해 시민에게 공개됐고 본관 벽에 총탄 자국이 남아 있다. 민주의 종(2005)은 5월 18일과 광복절에 울린다. 추모 공간이니 조용히 둘러보길 부탁한다. 국립아시아문화전당 실내는 보통 10:00~18:00, 매주 월요일과 1월 1일 휴관.'}]},
 dmy:{noBoard:1,spots:[st('tk_jnk',.04,1,L('Juknokwon ticket office','죽녹원 매표소'),L('Staff','직원'),[[L('Adult ticket','어른 입장권'),3000]],'🎫'),
   st('eat_tg',.55,1,L('Tteokgalbi restaurant','떡갈비집'),L('Owner','사장님'),[[L('Tteokgalbi (grilled beef patties)','떡갈비'),25000],[L('Daetongbap (rice cooked in bamboo)','대통밥'),15000]],'🍖')],
  sights:[{t:.25,side:-1,id:'juknok'},{t:.82,side:-1,id:'gwanbang'}],doors:[{t:.97,side:-1,to:'hotel',n:L('Back to the hotel in Gwangju','광주 호텔로'),lab:'HOTEL'}],
  cit:[{t:.5,n:L('Mrs. Song','송 사장님'),role:L('Tteokgalbi restaurant owner','떡갈비집 사장님'),p:'담양에서 떡갈비집을 하는 사장님. 담양 떡갈비와 대나무 통에 지은 대통밥을 권한다. 죽녹원(어른 3,000원, 11~2월 09:00~18:00, 입장 마감 17:30, 산책로 2.2km)과 관방제림(무료, 1648년부터 둑에 심은 숲)을 안내한다. 메뉴 가격은 게임 속 예시다.'}]},
 scw:{noBoard:1,spots:[{t:.04,side:1,k:'shuttle',id:'t_ysu',n:L('Train to Yeosu EXPO','여수EXPO 가는 기차'),fare:2600,ride:{kind:'train',scen:'port',title:L('Train Suncheon → Yeosu EXPO','기차 순천 → 여수EXPO'),col:'#c8202a',stops:[L('Suncheon','순천'),L('Yeocheon','여천'),L('Yeosu EXPO','여수EXPO')],gap:600,vmax:22,intro:L('🚆 Bus or taxi to Suncheon Station (15–20 min), then the train to Yeosu EXPO: 19–26 min. Mugunghwa ₩2,600, ITX ₩4,800, KTX ₩7,500. 35–39 trains a day.','🚆 시내버스나 택시로 순천역(15~20분), 기차로 여수EXPO까지 19~26분. 무궁화 2,600원, ITX 4,800원, KTX 7,500원. 하루 35~39회.'),dest:{sc:'odo',at:0}}},
   st('tk_scw',.08,-1,L('Suncheon Bay ticket office','순천만 매표소'),L('Staff','직원'),[[L('Adult ticket (Garden + Wetland, same day)','어른 입장권 (국가정원·습지, 같은 날)'),10000]],'🎫'),
   st('eat_jd',.14,1,L('Suncheon Bay restaurant','순천만 식당'),L('Owner','사장님'),[[L('Jjangttungeo-tang (mudskipper soup)','짱뚱어탕'),12000],[L('Cockle set meal','꼬막정식'),18000]],'🍲')],
  sights:[{t:.2,side:-1,id:'scgarden'},{t:.5,side:-1,id:'scbay'}],doors:[{t:.25,side:-1,to:'hotel',n:L('Hotel in Suncheon','순천 호텔'),lab:'HOTEL'}],
  cit:[{t:.45,n:L('Ms. Lee','이 해설사'),role:L('Wetland guide','습지 해설사'),p:'순천만습지 해설사. 순천만국가정원 입장권(어른 10,000원)으로 같은 날 습지에 들어올 수 있고, 국가정원은 10~6월 09:00~20:00(입장 마감 19:00), 매월 마지막 주 월요일 휴무라고 안내한다. 갈대 데크길, 가을의 황금빛 갈대, 탐방로 입구에서 용산전망대까지 약 1.5km(걸어서 25~30분), S자 물길과 해 질 녘 노을, 짱뚱어 이야기를 한다.'}]},
 odo:{noBoard:1,spots:[],links:[{t:.38,id:'l_ycb',n:L('🚶 To the cable car (Jasan station)','🚶 케이블카 타는 곳으로 (자산 정류장)'),s:L('By the Odongdo entrance','오동도 입구 옆'),to:'ycb',at:0}],
  sights:[{t:.12,side:-1,id:'yexpo'},{t:.6,side:1,id:'odongdo'}],
  shows:[{id:'dtrain',t:.5,b:L('🚃 Camellia Train','🚃 동백열차'),s:L('₩1,000 one way','편도 1,000원'),say:L('The little Camellia Train runs along the breakwater every 30 minutes: ₩1,000 one way. Nov–Feb, trains into the island run 09:30–17:00, with a lunch break 12:00–13:00.','작은 동백열차가 방파제를 따라 30분마다 다녀요. 편도 1,000원. 11~2월에는 섬으로 들어가는 열차가 09:30~17:00에 다니고, 12~13시는 점심시간이라 쉬어요.')}],
  cit:[{t:.7,n:L('Mr. Jeong','정 선생님'),role:L('Yeosu local','여수 시민'),p:'오동도를 산책하는 여수 시민. 오동도는 입장 무료에 늘 열려 있고, 동백꽃은 2월 중순부터 피기 시작해 3월 중순에 가장 많이 핀다고 말한다. 동백열차는 편도 1,000원. 섬 남쪽 끝의 오동도 등대, 해상케이블카 자산 정류장이 오동도 입구 근처라는 것, 여수 게장백반과 돌산 갓김치를 이야기한다.'}]},
 ycb:{noBoard:1,spots:[{t:.08,side:1,k:'shuttle',id:'ktx_ys',n:L('KTX to Yongsan','용산 가는 KTX'),fare:45400,ride:{kind:'train',scen:'country',title:L('KTX Yeosu EXPO → Yongsan','KTX 여수EXPO → 용산'),col:'#1f4f91',stops:[L('Yeosu EXPO','여수EXPO'),L('Yongsan','용산')],gap:1100,vmax:50,intro:L('🚆 From Yeosu EXPO Station: 23–26 KTX trains a day (05:05–21:54). The fastest take 2 h 50 min; most about 2 h 50 min–3 h 12 min. Standard class ₩45,400. (Stops differ by train.)','🚆 여수EXPO역에서 KTX 하루 23~26회(05:05~21:54). 가장 빠른 열차 2시간 50분, 보통 2시간 50분~3시간 12분. 일반실 45,400원. (정차역은 열차마다 달라요.)'),dest:{sc:'sar',at:0}}}],
  sights:[{t:.2,side:-1,id:'ycable'}],
  lifts:[{id:'ycable',y:60,ic:'🚡',down:L('🚡 Cable car back','🚡 케이블카로 돌아가기'),n:L('Yeosu Maritime Cable Car','여수 해상케이블카'),fare:17000,msg:L('The cable car glides out over the sea toward Dolsan…','케이블카가 바다 위로 돌산을 향해 가요…'),top:L('Sea below your feet: Odongdo, the harbour and the islands of Yeosu.','발아래가 바다예요. 오동도와 여수 항구, 섬들이 보여요.')}],
  cit:[{t:.3,n:L('Ms. Han','한 매니저'),role:L('Cable car staff','케이블카 직원'),p:'여수 해상케이블카 직원. 자산(해야) 정류장은 오동도 입구 근처, 반대편은 돌산(놀아) 정류장이다. 일반 캐빈 어른 왕복 17,000원·편도 14,000원, 바닥이 투명한 크리스탈 캐빈 왕복 24,000원·편도 19,000원, 매일 09:30~21:30(매표 마감 21:00), 날씨에 따라 바뀔 수 있다고 안내한다.'}]},
 sar:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'yongsan'}],cit:[{t:.55,n:L('Mr. Oh','오 역무원'),role:L('Yongsan Station staff','용산역 역무원'),p:'용산역 역무원. 지하철 1호선과 경의·중앙선으로 갈아타는 길을 안내한다. 호남선·전라선 KTX가 많이 서는 역이다.'}],fin:{t:.85,s:L('3 days in Jeonnam · Gwangju','전남·광주 2박 3일')}}};

"""

R['info']='const CRUISE_INFO="이 게임은 여행자가 서울역에서 KTX를 타고 광주에 가서 2박 3일 동안 광주·담양·순천·여수를 돌고 KTX로 용산역에 돌아오는 가상 3D 여행이다. 광주와 전남은 2026년 7월 1일 하나로 합쳐 전남광주통합특별시(약 316만 명)가 됐다. 1일: 서울역 KTX(광주송정 일반실 42,400원, 서울역 출발 하루 5~6회 06:22~19:29, 가장 빠른 열차 약 2시간 3분, 2026년 11월 기준; 호남선 KTX는 용산 출발이 더 많고 용산→광주송정 42,000원; 2026년 9월 1일 KTX·SRT 통합으로 요금 약 10% 인하) → 광주송정역 → 광주 지하철 1호선(교통카드 1,250원, 현금 1,400원) 문화전당역 → 5·18민주광장(국립아시아문화전당 앞 분수대 광장, 상시 개방; 1980년 5월 14~16일 민족민주화대성회; 분수대·상무관·시계탑을 그때 모습으로 보존; 민주의 종 2005년, 5월 18일과 광복절에 울림) → 옛 전남도청(5·18 최후 항쟁지, 2026년 5월 18일 6개 건물을 1980년 5월 모습으로 복원해 시민에게 공개, 본관 벽 총탄 자국) → 국립아시아문화전당 ACC(실내 보통 10:00~18:00, 매주 월요일·1월 1일 휴관, 바깥 06:00~22:00, 무료 공간과 유료 전시·공연이 섞여 있음) → 광주종합버스터미널(유스퀘어)에서 담양 시외버스 약 30~40분(하루 41회 06:17~21:37) 또는 시내버스 311번(광주 시내버스 기본 교통카드 1,250원) → 담양 죽녹원(어른 3,000원, 11~2월 09:00~18:00 입장 마감 17:30, 3~10월 09:00~19:00, 연중무휴, 산책로 2.2km 8가지 주제) → 떡갈비·대통밥 → 관방제림(무료, 상시, 1648년 담양부사 성이성이 홍수를 막으려 둑에 나무를 심기 시작, 약 2km에 185그루, 대부분 300살 넘음) → 광주 호텔. 2일: 광주종합버스터미널 → 순천종합버스터미널 시외버스(하루 24회, 약 1시간 13분, 일반 9,200원·우등 12,000원) → 순천만습지(순천만국가정원 입장권 어른 10,000원으로 같은 날 입장; 국가정원 10~6월 09:00~20:00 입장 마감 19:00, 매월 마지막 주 월요일 휴무; 갈대밭 데크길, 가을 황금빛 갈대, 탐방로 입구에서 용산전망대까지 약 1.5km 걸어서 25~30분, S자 물길과 노을; 짱뚱어탕·꼬막정식) → 순천 호텔. 3일: 시내버스·택시로 순천역(15~20분) → 기차로 여수EXPO역(19~26분, 무궁화 2,600원·ITX 4,800원·KTX 7,500원, 하루 35~39회) → 오동도(입장 무료, 상시 개방; 동백열차 편도 1,000원, 30분 간격, 11~2월 들어가는 열차 09:30~17:00, 12~13시 운휴; 동백꽃 2월 중순부터 3월 중순 절정; 섬 남쪽 끝 오동도 등대) → 오동도 입구 근처 자산(해야) 정류장 → 여수 해상케이블카(바다 건너 돌산(놀아) 정류장, 일반 캐빈 어른 왕복 17,000원·편도 14,000원, 크리스탈 캐빈 왕복 24,000원·편도 19,000원, 매일 09:30~21:30 매표 마감 21:00) → 여수EXPO역 KTX(용산까지 하루 23~26회 05:05~21:54, 가장 빠른 열차 2시간 50분, 일반실 45,400원) → 용산역(지하철 1호선·경의중앙선). 게임 속 식사·가게 가격은 예시다.";\n'

R['real']="""const REAL={
 sst:{n:L('Seoul Station','서울역'),sub:L('KTX to Gwangju Songjeong','광주송정행 KTX'),ll:[37.5555,126.9707],q:'Seoul Station',f:[L('5–6 KTX trains a day leave here for Gwangju Songjeong (Nov 2026). Most Honam Line KTX trains leave from Yongsan.','광주송정 가는 KTX가 하루 5~6회 여기서 떠나요(2026년 11월 기준). 호남선 KTX는 대부분 용산역에서 떠나요.'),L('The domed red-brick old station (1925) is now Culture Station Seoul 284.','붉은 벽돌 돔의 옛 서울역(1925)은 지금 문화역서울284예요.')]},
 ktx:{n:'KTX',sub:L('Seoul → Gwangju Songjeong','서울 → 광주송정'),q:'KTX Gwangju Songjeong',f:[L('Standard class from Seoul Station ₩42,400; from Yongsan ₩42,000.','서울역에서 일반실 42,400원, 용산역에서 42,000원.'),L('Fares fell about 10% on 1 Sept 2026, when KTX and SRT merged (Yongsan → Gwangju Songjeong was ₩46,800).','2026년 9월 1일 KTX·SRT 통합으로 요금이 약 10% 내렸어요(용산→광주송정 46,800원이었어요).'),L('Fastest from Seoul Station: about 2 h 3 min.','서울역에서 가장 빠른 열차는 약 2시간 3분.')]},
 gsj:{n:L('Gwangju Songjeong Station','광주송정역'),sub:L('KTX · Metro Line 1','KTX · 지하철 1호선'),ll:[35.1378,126.7919],q:'광주송정역',f:[L('The KTX station for Gwangju, linked to Metro Line 1.','광주의 KTX역이에요. 지하철 1호선과 이어져 있어요.'),L('Since 1 July 2026 Gwangju and Jeonnam form one city: the Jeonnam-Gwangju Integrated Special City (about 3.16 million people).','2026년 7월 1일부터 광주와 전남이 합쳐 전남광주통합특별시가 됐어요(약 316만 명).')]},
 gjmetro:{n:L('Gwangju Metro Line 1','광주 지하철 1호선'),sub:L('Fares','요금'),q:'광주 지하철 1호선',f:[L('Adult fare ₩1,250 by transport card, ₩1,400 in cash.','어른 교통카드 1,250원, 현금 1,400원.'),L('City buses: base fare ₩1,250 by card (July 2026).','시내버스 기본요금 교통카드 1,250원(2026년 7월 기준).')]},
 may18:{n:L('May 18 Democracy Square','5·18민주광장'),sub:L('In front of the ACC','국립아시아문화전당 앞'),q:'5·18민주광장',f:[L('From 14 to 16 May 1980, students and citizens held mass rallies here for democracy.','1980년 5월 14~16일 학생과 시민이 이 광장에서 민족민주화대성회를 열었어요.'),L('The fountain, the Sangmugwan hall and the clock tower are kept as they were. Always open.','분수대와 상무관, 시계탑을 그때 모습으로 지켜 왔어요. 늘 열려 있어요.'),L('The Bell of Democracy (2005) rings on 18 May and Liberation Day.','민주의 종(2005)은 5월 18일과 광복절에 울려요.')]},
 oldoffice:{n:L('Old South Jeolla Provincial Office','옛 전남도청'),sub:L('Last stand of the May 18 Uprising','5·18 최후 항쟁지'),q:'옛 전남도청',f:[L('Restored to its May 1980 look (six buildings) and opened to the public on 18 May 2026.','6개 건물을 1980년 5월 모습으로 복원해 2026년 5월 18일 시민에게 문을 열었어요.'),L('Bullet marks can still be seen on the walls of the main building. Please visit quietly.','본관 벽에 총탄 자국이 남아 있어요. 조용히 둘러봐요.')]},
 acc:{n:L('Asia Culture Center (ACC)','국립아시아문화전당(ACC)'),sub:L('Gwangju','광주'),q:'국립아시아문화전당',f:[L('Indoor spaces usually 10:00–18:00; closed Mondays and 1 January. Outdoor spaces 06:00–22:00.','실내는 보통 10:00~18:00, 매주 월요일과 1월 1일 휴관. 바깥 공간은 06:00~22:00.'),L('Some spaces are free; exhibitions and shows may charge. Check each programme.','무료 공간도 있고 전시·공연은 유료일 수 있어요. 프로그램마다 확인해요.')]},
 dmybus:{n:L('Buses to Damyang','담양 가는 버스'),sub:L('From Gwangju','광주에서'),q:'광주종합버스터미널',f:[L('Intercity bus from Gwangju Bus Terminal (U-Square): about 30–40 min, 41 a day (06:17–21:37).','광주종합버스터미널(유스퀘어)에서 시외버스로 약 30~40분, 하루 41회(06:17~21:37).'),L('City bus 311 also runs between Gwangju and Damyang (06:20–22:05).','시내버스 311번도 광주와 담양을 오가요(06:20~22:05).')]},
 juknok:{n:L('Juknokwon','죽녹원'),sub:L('Bamboo forest, Damyang','담양 대나무 숲'),ll:[35.3261,126.9831],q:'담양 죽녹원',f:[L('Adult ₩3,000. Nov–Feb 09:00–18:00 (last entry 17:30); Mar–Oct 09:00–19:00. Open every day.','어른 3,000원. 11~2월 09:00~18:00(입장 마감 17:30), 3~10월 09:00~19:00. 연중무휴.'),L('Eight themed paths, 2.2 km in all.','8가지 주제의 산책로, 모두 2.2km.')]},
 gwanbang:{n:L('Gwanbangjerim','관방제림'),sub:L('Riverside forest · natural monument','강둑 숲 · 천연기념물'),q:'담양 관방제림',f:[L('Planted from 1648 by the county magistrate Seong I-seong to protect against floods.','1648년 담양부사 성이성이 홍수를 막으려고 둑에 나무를 심기 시작했어요.'),L('About 2 km long, 185 trees, most over 300 years old. Free, always open; it joins Juknokwon’s back gate.','약 2km에 185그루, 대부분 300살이 넘어요. 무료, 늘 열려 있고 죽녹원 후문과 이어져요.')]},
 scbus:{n:L('Gwangju → Suncheon bus','광주 → 순천 시외버스'),sub:L('Gwangju Bus Terminal (U-Square)','광주종합버스터미널(유스퀘어)'),q:'광주종합버스터미널',f:[L('24 buses a day, about 1 h 13 min. Standard ₩9,200, premium ₩12,000. (Nov 2026)','하루 24회, 약 1시간 13분. 일반 9,200원, 우등 12,000원. (2026년 11월 기준)')]},
 scgarden:{n:L('Suncheonman Bay National Garden','순천만국가정원'),sub:L('Korea’s first national garden','대한민국 제1호 국가정원'),ll:[34.9292,127.5006],q:'순천만국가정원',f:[L('Adult ₩10,000; the same ticket gets you into Suncheonman Bay Wetland on the same day.','어른 10,000원. 같은 날 이 입장권으로 순천만습지에도 들어가요.'),L('Oct–Jun 09:00–20:00 (last entry 19:00). Closed on the last Monday of each month.','10~6월 09:00~20:00(입장 마감 19:00). 매월 마지막 주 월요일 휴무.')]},
 scbay:{n:L('Suncheonman Bay Wetland','순천만습지'),sub:L('Reed fields · tidal flats','갈대밭 · 갯벌'),ll:[34.8829,127.5143],q:'순천만습지',f:[L('Boardwalks cross the reed beds; the reeds turn gold in autumn.','갈대밭 사이로 데크길이 이어져요. 가을에는 갈대가 황금빛이에요.'),L('Trail entrance → Yongsan Observatory: about 1.5 km, 25–30 minutes on foot. Famous for sunsets over the S-shaped channels.','탐방로 입구에서 용산전망대까지 약 1.5km, 걸어서 25~30분. S자 물길 위 노을이 유명해요.')]},
 ysutrain:{n:L('Suncheon → Yeosu EXPO train','순천 → 여수EXPO 기차'),sub:L('Jeolla Line','전라선'),q:'순천역',f:[L('19–26 minutes. Mugunghwa ₩2,600, ITX ₩4,800, KTX ₩7,500. 35–39 trains a day. (Nov 2026)','19~26분. 무궁화 2,600원, ITX 4,800원, KTX 7,500원. 하루 35~39회. (2026년 11월 기준)')]},
 yexpo:{n:L('Yeosu EXPO Station','여수EXPO역'),sub:L('KTX · Jeolla Line','KTX · 전라선'),ll:[34.7527,127.7503],q:'여수엑스포역',f:[L('The end of the Jeolla Line. Odongdo and the Jasan cable car station are close by.','전라선의 끝 역이에요. 오동도와 해상케이블카 자산 정류장이 가까워요.')]},
 odongdo:{n:L('Odongdo','오동도'),sub:L('Camellia island · free','동백섬 · 무료'),ll:[34.7434,127.7599],q:'여수 오동도',f:[L('Free, always open. Camellia Train ₩1,000 one way (every 30 min).','입장 무료, 늘 열려 있어요. 동백열차 편도 1,000원(30분 간격).'),L('Camellias begin in mid-February and peak around mid-March. The Odongdo Lighthouse stands at the southern tip.','동백꽃은 2월 중순부터 피기 시작해 3월 중순에 가장 많이 펴요. 섬 남쪽 끝에 오동도 등대가 있어요.')]},
 ycable:{n:L('Yeosu Maritime Cable Car','여수 해상케이블카'),sub:L('Jasan ↔ Dolsan','자산 ↔ 돌산'),q:'여수 해상케이블카',f:[L('Standard cabin: adult ₩17,000 round trip, ₩14,000 one way. Crystal (glass floor): ₩24,000 / ₩19,000.','일반 캐빈 어른 왕복 17,000원·편도 14,000원. 크리스탈(투명 바닥) 24,000원·19,000원.'),L('Daily 09:30–21:30 (tickets until 21:00); may change with the weather.','매일 09:30~21:30(매표 마감 21:00). 날씨에 따라 바뀔 수 있어요.')]},
 ktxys:{n:L('KTX Yeosu EXPO → Yongsan','KTX 여수EXPO → 용산'),sub:L('Back to Seoul','서울로'),q:'여수엑스포역',f:[L('23–26 trains a day (05:05–21:54). Fastest 2 h 50 min; most 2 h 50 min–3 h 12 min. Standard ₩45,400. (Nov 2026)','하루 23~26회(05:05~21:54). 가장 빠른 열차 2시간 50분, 보통 2시간 50분~3시간 12분. 일반실 45,400원. (2026년 11월 기준)')]},
 yongsan:{n:L('Yongsan Station','용산역'),sub:L('KTX · Line 1 · Gyeongui–Jungang','KTX · 1호선 · 경의중앙선'),ll:[37.53,126.9647],q:'용산역',f:[L('Most Honam and Jeolla Line KTX trains start and end here. Change to subway Line 1 or the Gyeongui–Jungang Line.','호남선·전라선 KTX가 많이 서는 역이에요. 지하철 1호선과 경의중앙선으로 갈아타요.')]},
};
"""

R['qz']="""const QZ={
 sst:[[/KTX to Gwangju Songjeong|광주송정행 KTX/,'jq1',L('How much is a standard-class KTX ticket from Seoul Station to Gwangju Songjeong?','서울역 → 광주송정 KTX 일반실 요금은?'),['₩32,400','₩42,400','₩59,800'],1,L('₩42,400 (₩42,000 from Yongsan), since the September 2026 fare cut.','2026년 9월 요금 인하 뒤 42,400원이에요(용산에서는 42,000원).')]],
 gsj:[[/Line 1|1호선/,'jq2',L('What happened to Gwangju and Jeonnam on 1 July 2026?','2026년 7월 1일 광주와 전남에는 무슨 일이 있었을까요?'),[L('They became one special city','하나의 특별시가 됐어요'),L('KTX fares doubled','KTX 요금이 두 배가 됐어요'),L('They changed their flags only','깃발만 바꿨어요')],0,L('They merged into the Jeonnam-Gwangju Integrated Special City (about 3.16 million people).','하나로 합쳐 전남광주통합특별시가 됐어요(약 316만 명).')]],
 acc:[[/Damyang|담양/,'jq3',L('Which bell rings at the square on 18 May and Liberation Day?','5월 18일과 광복절에 광장에서 울리는 종은?'),[L('The Bell of Democracy','민주의 종'),L('The Emille Bell','에밀레종'),L('Bosingak Bell','보신각종')],0,L('The Bell of Democracy, built in 2005.','2005년에 만든 민주의 종이에요.')]],
 dmy:[[/ticket office|매표소/,'jq4',L('How long are Juknokwon’s walking paths in all?','죽녹원 산책로는 모두 얼마나 될까요?'),[L('About 2.2 km','약 2.2km'),L('About 22 km','약 22km'),L('About 200 m','약 200m')],0,L('Eight themed paths, 2.2 km in all.','8가지 주제의 길, 모두 2.2km예요.')]],
 scw:[[/ticket office|매표소/,'jq5',L('With the National Garden ticket (₩10,000) you can also enter…','국가정원 입장권(10,000원)으로 같은 날 또 들어갈 수 있는 곳은?'),[L('Suncheonman Bay Wetland','순천만습지'),L('The Yeosu cable car','여수 케이블카'),L('Juknokwon','죽녹원')],0,L('Suncheonman Bay Wetland, on the same day.','같은 날 순천만습지에 들어가요.')],
  [/Yeosu EXPO|여수EXPO/,'jq6',L('About how long is the train from Suncheon to Yeosu EXPO?','순천에서 여수EXPO까지 기차로 얼마나 걸리나요?'),[L('About 20 min','약 20분'),L('About 2 h','약 2시간'),L('About 5 h','약 5시간')],0,L('19–26 minutes.','19~26분이에요.')]],
 odo:[[/cable car|케이블카/,'jq7',L('Odongdo is famous for which flower?','오동도는 어떤 꽃으로 유명할까요?'),[L('Camellia','동백꽃'),L('Cherry blossom','벚꽃'),L('Sunflower','해바라기')],0,L('Camellias: they peak around mid-March.','동백꽃이에요. 3월 중순에 가장 많이 펴요.')]],
 ycb:[[/🚡 (Yeosu|여수)/,'jq8',L('How much is a standard-cabin round trip for an adult?','일반 캐빈 어른 왕복 요금은?'),['₩7,000','₩17,000','₩27,000'],1,L('₩17,000 (Crystal cabin ₩24,000).','17,000원이에요(크리스탈 캐빈 24,000원).')],
  [/Yongsan|용산/,'jq9',L('About how long is the fastest KTX from Yeosu EXPO to Yongsan?','여수EXPO → 용산 가장 빠른 KTX는 약 얼마나 걸리나요?'),[L('About 1 h','약 1시간'),L('About 2 h 50 min','약 2시간 50분'),L('About 6 h','약 6시간')],1,L('2 h 50 min; most take up to about 3 h 12 min.','2시간 50분이에요. 보통 3시간 12분쯤까지 걸려요.')]]};
"""

R['rem']="h(L('Remember','꼭 기억할 것'));[L('KTX Seoul Station → Gwangju Songjeong ₩42,400 · fastest about 2 h 3 min · more trains from Yongsan','KTX 서울역 → 광주송정 42,400원 · 가장 빠른 열차 약 2시간 3분 · 용산 출발이 더 많아요'),L('Gwangju subway and city bus: ₩1,250 by card','광주 지하철·시내버스 교통카드 1,250원'),L('ACC closed on Mondays · May 18 Square always open','ACC 매주 월요일 휴관 · 5·18민주광장 늘 열림'),L('Juknokwon ₩3,000 · Nov–Feb 09:00–18:00 (last entry 17:30)','죽녹원 3,000원 · 11~2월 09:00~18:00(입장 마감 17:30)'),L('Suncheon Bay: one ₩10,000 ticket for Garden + Wetland · closed last Monday','순천만: 10,000원 한 장으로 정원·습지 · 매월 마지막 주 월요일 휴무'),L('Yeosu cable car ₩17,000 round trip · Odongdo free','여수 케이블카 왕복 17,000원 · 오동도 무료'),L('KTX Yeosu EXPO → Yongsan ₩45,400 · fastest 2 h 50 min','KTX 여수EXPO → 용산 45,400원 · 가장 빠른 열차 2시간 50분'),"

R['areako']="const AREAKO={sst:'서울역',ktx:'서울역',gsj:'광주송정역',gjmetro:'광주송정역',may18:'광주 5·18민주광장',oldoffice:'광주 금남로',acc:'국립아시아문화전당',dmybus:'광주종합버스터미널',juknok:'담양 죽녹원',gwanbang:'담양 관방제림',scbus:'순천종합버스터미널',scgarden:'순천만국가정원',scbay:'순천만습지',ysutrain:'순천역',yexpo:'여수엑스포역',odongdo:'여수 오동도',ycable:'여수 자산공원',ktxys:'여수엑스포역',yongsan:'용산역'};"

R['foods']="""
  {k:'떡갈비',e:'tteokgalbi',s:'Tteokgalbi',ic:'🍖',re:/떡갈비|tteokgalbi/i},
  {k:'대통밥',e:'daetongbap (bamboo rice)',s:'Bamboo rice',ic:'🎋',re:/대통밥|daetong|bamboo rice/i},
  {k:'상추튀김',e:'sangchu-twigim',s:'Lettuce & fritters',ic:'🥬',re:/상추튀김|sangchu/i},
  {k:'짱뚱어탕',e:'mudskipper soup',s:'Mudskipper soup',ic:'🍲',re:/짱뚱어|mudskipper/i},
  {k:'꼬막',e:'cockles (kkomak)',s:'Cockles',ic:'🐚',re:/꼬막|kkomak|cockle/i},
  {k:'게장백반',e:'gejang (marinated crab)',s:'Marinated crab',ic:'🦀',re:/게장|gejang|crab/i},"""

R['phrase']="['광주송정역 어디예요?','Gwangju-songjeong-yeok eodi-yeyo?',L('Where is Gwangju Songjeong Station?','광주송정역 어디예요?')]"
R['stP']="$('stP').textContent=L('Leave Seoul Station by KTX for Gwangju. Stand in the May 18 Democracy Square and see the restored Old Provincial Office, then walk the bamboo paths of Damyang’s Juknokwon. Cross the reed fields of Suncheon Bay, walk the breakwater to Yeosu’s camellia island Odongdo and ride the cable car over the sea before the KTX back to Seoul. Real fares, times and photos.','서울역에서 KTX로 광주에 가요. 5·18민주광장과 복원된 옛 전남도청을 보고, 담양 죽녹원 대숲을 걸어요. 순천만 갈대밭을 지나 여수 동백섬 오동도까지 방파제를 걷고, 바다 위 케이블카를 탄 뒤 KTX로 서울에 돌아와요. 실제 요금·시간·사진을 담았어요.');"
R['stR']="$('stR').textContent=L('Seoul Station · KTX · Gwangju Songjeong · May 18 Square · Old Provincial Office · ACC · Juknokwon · Gwanbangjerim · Suncheon Bay · Yeosu EXPO · Odongdo · Cable Car · Yongsan','서울역 · KTX · 광주송정 · 5·18민주광장 · 옛 전남도청 · ACC · 죽녹원 · 관방제림 · 순천만 · 여수EXPO · 오동도 · 해상케이블카 · 용산');"
R['rgn']="const RGN={ktx:'KTX  광주송정 GWANGJU',sst0:L('Seoul Station. KTX trains to Gwangju Songjeong leave from here too (5–6 a day). Buy tickets on the Korail Talk app, at a ticket window or a ticket machine.','서울역이에요. 광주송정 가는 KTX도 여기서 떠나요(하루 5~6회). 표는 코레일톡 앱, 매표창구, 자동발매기에서 사요.'),sst8:L('KTX Seoul → Gwangju Songjeong: ₩42,400 in standard class. The fastest train takes about 2 h 3 min.','KTX 서울 → 광주송정: 일반실 42,400원. 가장 빠른 열차는 약 2시간 3분.'),arr:'용산역 YONGSAN STATION',arrLine:'1 용산역 · LINE 1',arrLineCol:'#0052a4',arrNotes:[[0,L('Yongsan Station. Welcome back to Seoul!','용산역이에요. 서울에 돌아왔어요!')],[.5,L('Change here to subway Line 1 or the Gyeongui–Jungang Line.','여기서 지하철 1호선과 경의중앙선으로 갈아타요.')]]};"
r=Region(S);r.build(R);r.save('jnm.html')
