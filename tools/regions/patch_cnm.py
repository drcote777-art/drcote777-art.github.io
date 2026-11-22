# 가상 충남·서해안 2박 3일 (cnm.html): 용산역 출발 · 천안 · 아산 온양온천 · 당진 왜목 · 서산 해미 · 태안 안면도 꽃지 · 보령 대천 · 용산역 도착
# 공통 생성기(region_base.py)가 서울 엔진을 받고, 이 파일의 자료로 바꿔 끼웁니다.
# 사실 출처(2026-11-22 확인):
#  용산→천안 기차 하루 37~38회 05:25~21:22, 1시간 00~20분, 무궁화 6,100원·ITX-마음/ITX-새마을/새마을 9,000원 (train.asamaru.net 2026-11-22)
#  천안→… 온양온천↔천안 13~16분, 하루 19회, 무궁화 2,600원·ITX 4,800원 (asamaru 2026-11-22); 용산→온양온천 1시간 23~35분, 하루 16회, 무궁화 7,000·새마을/ITX-마음 10,400원 (asamaru 2026-11-22)
#  독립기념관: 무료, 3~10월 09:30~18:00·11~2월 09:30~17:00(입장 마감 1시간 전), 월요일 휴관(공휴일이면 개관), 셔틀 어른 5,000원(문구 불분명) (ktriptips 2026-11-11, travelmapjourney 2026-10-21);
#   815번 버스가 천안아산역–천안역 동부광장–독립기념관 직통 (twig24 2024-11-04)
#  온양온천: 약 1,300년 국내에서 가장 오래된 온천, 세종·세조·숙종·영조·정조, 온양 온천 랜드 온천탕 대인 10,000원 (ktriptips 2026-04-08); 알칼리성 37~54°C (ktriptips 2025-05-12)
#  아산시외버스터미널→당진버스터미널 하루 13회 07:15~21:45, 1시간 2~13분, 7,100원 (transportation.asamaru.net 2026-11-17)
#  왜목마을: 당진 석문면, 태안반도 최북단, 일출·일몰·월출을 한 곳에서 보는 전국 유일의 곳 (ktriptips 2026-11-11)
#  해미읍성: 무료·주차 무료, 3~10월 05:00~21:00·11~2월 06:00~19:00, 연중무휴, 1491년(성종 22년), 둘레 약 1.8km·높이 5m, 1866년 천주교 신자 약 1,000명 처형 기록, 고문에 쓰인 고목 (ktriptips 2026-11-11)
#  안면도↔서산공용버스터미널 시외버스 하루 9회(안면 출발 07:25~17:40), 약 1시간 5~6분, 7,800원 (asamaru 2026-11-22)
#  꽃지해수욕장: 안면읍, 안면도 최대 해변, 상시 개방, 낙조 (ktriptips 2025-07-31); 할미할아비바위 명승 제69호(2009-12-09), 장보고·승언·미도 전설 (한국학중앙연구원 문화유산 위키)
#  보령해저터널: 6,927m 국내 최장·세계 5위, 2021-11-30 개통, 해수면 아래 약 80m, 대천항–원산도, 원산안면대교(1.8km, 2019-12)로 안면도 연결, 대천항→영목항 90분→10분 (서울신문 2021-11-04)
#  대천해수욕장: 백사장 약 3.5km, 보령머드체험관, 스카이바이크 해상 8~15m 왕복 2.3km 약 40분, 상시 (ktriptips 2026-11-12); 2026 보령머드축제 7/24~8/9, 대천역↔해수욕장 버스·택시 약 10~15분 (travelmapjourney 2026-06-15)
#  대천→용산 기차 하루 14~15회 06:17~21:11, 2시간 30~56분, 무궁화 11,700원·새마을 17,400원 (asamaru 2026-11-07)
import os,sys
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
sys.path.insert(0,S)
from region_base import Region
R=dict(id='cnm',title='Virtual Chungnam · West Coast · 가상 충남·서해안 3일',money=300000,metro='jhtrain',start='yst',
 top=['K_region_top.js','K_jnm_top.js','K_cbk_top.js','K_cnm_top.js'],br=['K_region_br.js','K_cnm_br.js'],ph='ph/PH_cnm.json',
 enter=('Start at Yongsan Station','용산역에서 시작하기'),hotel=('Onyang','온양'),
 hotel_note=('Your hotel room for tonight: Onyang on night 1, Anmyeondo on night 2.','오늘 밤 묵을 호텔 방이에요. 첫날 밤은 온양, 둘째 날 밤은 안면도예요.'),
 chip=('Good ganjang-gejang place nearby?','간장게장 맛집 어디예요?'),deep=('hmi',.4),eyebrow='SEOUL → CHEONAN · ASAN · SEOSAN · TAEAN · BORYEONG',
 stH=('Virtual Chungnam<br>West Coast · 3 days','가상 충남·서해안<br>2박 3일'),wx=('36.7898','127.0019'),city_name=('Chungnam','충남'),
 stamps_title=('Chungnam stamps','충남 스탬프'),guide_role=('Your Chungnam tour guide','충남 여행 가이드'),
 course_ko='충남·서해안 2박 3일 코스',guide_line=('Ask me anything about Cheonan, Onyang and the west coast!','천안·온양·서해안에 대해 무엇이든 물어보세요!'),
 virtual=('Virtual Chungnam','가상 충남','가상 충남으로'))

R['stamps']="""const STAMPS=[{id:'cna',name:L('Independence Hall','독립기념관'),date:'D1',c:'#1f4f91'},{id:'ony',name:L('Onyang Hot Spring','온양온천'),date:'D1',c:'#c8553d'},{id:'wmk',name:L('Waemok Village','왜목마을'),date:'D2',c:'#e8833a'},{id:'hmi',name:L('Haemieupseong','해미읍성'),date:'D2',c:'#8a5a2a'},{id:'kkj',name:L('Kkotji Beach','꽃지해수욕장'),date:'D2',c:'#2e8fd0'},{id:'dcb',name:L('Daecheon Beach','대천해수욕장'),date:'D3',c:'#5a3a26'}];
"""

R['scn']="""const SCN={
 yst:{b:'seoul',o:{city:'yst'},name:L('Yongsan Station · Janghang Line','용산역 · 장항선')},cna:{b:'seoul',o:{city:'cna'},name:L('Cheonan · Independence Hall','천안 · 독립기념관')},
 ony:{b:'seoul',o:{city:'ony'},name:L('Asan · Onyang Hot Spring','아산 · 온양온천')},wmk:{b:'seoul',o:{city:'wmk'},name:L('Dangjin · Waemok Village','당진 · 왜목마을')},
 hmi:{b:'seoul',o:{city:'hmi'},name:L('Seosan · Haemieupseong','서산 · 해미읍성')},kkj:{b:'seoul',o:{city:'kkj'},name:L('Anmyeondo · Kkotji Beach','안면도 · 꽃지해수욕장')},
 dcb:{b:'seoul',o:{city:'dcb'},name:L('Boryeong · Daecheon Beach','보령 · 대천해수욕장')},sar:{b:'seoul',o:{city:'sar'},name:L('Yongsan Station','용산역')},
 hotel:{b:'hotel',name:L('Hotel room · Onyang / Anmyeondo','호텔 방 · 온양 / 안면도')},ride:{b:'ride',name:''}};
const SHIPMAP=[['yst',L('Yongsan','용산'),L('Train','기차')],['cna',L('Cheonan','천안'),L('Train + bus','기차 + 버스')],['ony',L('Onyang','온양'),L('Train','기차')],['wmk',L('Waemok','왜목'),L('Bus · taxi','버스·택시')],['hmi',L('Haemi','해미'),L('Taxi','택시')],['kkj',L('Kkotji','꽃지'),L('Bus','버스')],['dcb',L('Daecheon','대천'),L('Undersea tunnel','해저터널')],['sar',L('Yongsan','용산'),L('Train','기차')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

"""

R['days']="""const DAYS=[
 {tag:'DAY 1',title:L('Yongsan → Cheonan · Onyang','용산 출발 · 천안 · 온양'),time:L('Train Yongsan → Cheonan (about 1 h) → Independence Hall → train to Onyangoncheon (about 15 min) → hot spring','기차로 용산 → 천안(약 1시간) → 독립기념관 → 기차로 온양온천(약 15분) → 온천'),q:[
  {t:'',n:L('Find your train on the departure board','전광판에서 열차 확인'),sc:'yst',at:.45,near:1,r:'yongsan'},
  {t:'',n:L('Train to Cheonan (₩6,100)','천안 가는 기차 (6,100원)'),sc:'yst',at:.82,a:'jh_cna',r:'jhtrain'},
  {t:'',n:L('The Tower of the Nation','겨레의 탑'),sc:'cna',at:.35,near:1,r:'indep'},
  {t:'',n:L('Independence Hall stamp','독립기념관 스탬프'),sc:'cna',at:.97,a:'stamp'},
  {t:'',n:L('Train to Onyangoncheon (₩2,600)','온양온천 가는 기차 (2,600원)'),sc:'cna',at:.06,a:'t_ony',r:'onytrain'},
  {t:'',n:L('Warm your feet at the foot bath','족욕장에서 발 담그기'),sc:'ony',at:.35,near:1,r:'onyang'},
  {t:'',n:L('Hot spring bath','온천욕'),sc:'ony',at:.62,a:'eat_ony'},
  {t:'',n:L('Onyang stamp','온양 스탬프'),sc:'ony',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Dangjin · Seosan · Anmyeondo','당진 · 서산 · 안면도'),time:L('Bus to Dangjin (about 1 h) → Waemok Village → taxi to Haemieupseong → bus via Seosan to Anmyeondo (about 1 h) → Kkotji Beach at sunset','버스로 당진(약 1시간) → 왜목마을 → 택시로 해미읍성 → 서산 거쳐 버스로 안면도(약 1시간) → 해 질 녘 꽃지해수욕장'),q:[
  {t:'',n:L('Bus to Dangjin (₩7,100)','당진 가는 버스 (7,100원)'),sc:'ony',at:.1,a:'b_dgj',r:'dgjbus'},
  {t:'',n:L('Waemok: sunrise and sunset in one place','왜목: 해돋이와 해넘이를 한 곳에서'),sc:'wmk',at:.45,near:1,r:'waemok'},
  {t:'',n:L('Waemok stamp','왜목 스탬프'),sc:'wmk',at:.97,a:'stamp'},
  {t:'',n:L('Taxi to Haemieupseong','택시로 해미읍성'),sc:'wmk',at:.9,a:'l_hmi'},
  {t:'',n:L('Walk the walls of Haemieupseong','해미읍성 성곽 걷기'),sc:'hmi',at:.45,near:1,r:'haemi'},
  {t:'',n:L('Haemieupseong stamp','해미읍성 스탬프'),sc:'hmi',at:.97,a:'stamp'},
  {t:'',n:L('Bus to Anmyeondo (₩7,800)','안면도 가는 버스 (7,800원)'),sc:'hmi',at:.06,a:'b_amy',r:'amybus'},
  {t:'',n:L('Sunset at the Halmi and Halabi Rocks','할미·할아비 바위 해넘이'),sc:'kkj',at:.4,near:1,r:'kkotji'},
  {t:'',n:L('Kkotji stamp','꽃지 스탬프'),sc:'kkj',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Boryeong · back to Seoul','보령 · 서울로'),time:L('Through the Boryeong Undersea Tunnel to Daecheon Beach → train Daecheon → Yongsan (about 2 h 30 min)','보령해저터널 지나 대천해수욕장 → 기차로 대천 → 용산(약 2시간 30분)'),q:[
  {t:'',n:L('Taxi through the undersea tunnel','택시로 해저터널 지나기'),sc:'kkj',at:.08,a:'l_dcb',r:'tunnel'},
  {t:'',n:L('Daecheon Beach and the Sky Bike','대천해수욕장과 스카이바이크'),sc:'dcb',at:.4,near:1,r:'daecheon'},
  {t:'',n:L('Grilled shellfish lunch','조개구이 점심'),sc:'dcb',at:.55,a:'eat_dcb'},
  {t:'',n:L('Daecheon stamp','대천 스탬프'),sc:'dcb',at:.97,a:'stamp'},
  {t:'',n:L('Train to Yongsan (₩11,700)','용산 가는 기차 (11,700원)'),sc:'dcb',at:.12,a:'jh_ys',r:'dctrain'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'sar',at:.85,a:'trip'}]}];

"""

R['city']="""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1500,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 yst:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'jh_cna',n:L('Train to Cheonan','천안 가는 기차'),fare:6100,ride:{kind:'train',scen:'country',title:L('Train Yongsan → Cheonan','기차 용산 → 천안'),col:'#c8202a',stops:[L('Yongsan','용산'),L('Cheonan','천안')],gap:1000,vmax:30,intro:L('🚆 Yongsan → Cheonan: 37–38 trains a day (05:25–21:22), 1 h 00–1 h 20 min. Mugunghwa ₩6,100; ITX-Maeum, ITX-Saemaeul and Saemaeul ₩9,000. From Cheonan Station, take a bus or taxi to the Independence Hall.','🚆 용산 → 천안: 하루 37~38회(05:25~21:22), 1시간 00~20분. 무궁화 6,100원, ITX-마음·ITX-새마을·새마을 9,000원. 천안역에서 버스나 택시로 독립기념관에 가요.'),dest:{sc:'cna',at:0}}},
   st('eat_yst',.3,-1,L('Station kiosk','역 매점'),L('Clerk','직원'),[[L('Gimbap roll','김밥 한 줄'),4000],[L('Coffee','커피'),4500],[L('Bottled water','생수'),1200]],'🥤')],
  sights:[{t:.14,side:1,id:'yongsan'},{t:.75,side:-1,id:'jhtrain'}],
  cit:[{t:.5,n:L('Mr. Oh','오 역무원'),role:L('Yongsan Station staff','용산역 역무원'),p:'용산역 역무원. 장항선 열차(무궁화·ITX-새마을·ITX-마음)가 천안·온양온천·대천 등 서해안으로 떠난다고 안내한다. 용산→천안 하루 37~38회, 1시간 00~20분, 무궁화 6,100원·ITX 9,000원. 용산→온양온천 1시간 23~35분, 하루 16회, 무궁화 7,000원·ITX-마음/새마을 10,400원(2026년 11월 기준). 표는 코레일톡 앱·창구·자동발매기에서 산다.'}]},
 cna:{noBoard:1,spots:[{t:.06,side:1,k:'shuttle',id:'t_ony',n:L('Train to Onyangoncheon','온양온천 가는 기차'),fare:2600,ride:{kind:'train',scen:'country',title:L('Train Cheonan → Onyangoncheon','기차 천안 → 온양온천'),col:'#c8202a',stops:[L('Cheonan','천안'),L('Asan','아산'),L('Onyangoncheon','온양온천')],gap:600,vmax:22,intro:L('🚆 Bus or taxi back to Cheonan Station, then the Janghang Line train to Onyangoncheon: 13–16 min, 19 a day. Mugunghwa ₩2,600, ITX ₩4,800.','🚆 버스나 택시로 천안역에 돌아가서 장항선 기차로 온양온천까지 13~16분, 하루 19회. 무궁화 2,600원, ITX 4,800원.'),dest:{sc:'ony',at:0}}},
   st('eat_cna',.12,-1,L('Hodu-gwaja shop','호두과자 가게'),L('Owner','사장님'),[[L('Walnut cakes (small box)','호두과자 (작은 상자)'),6000],[L('Walnut cakes (big box)','호두과자 (큰 상자)'),12000]],'🌰')],
  sights:[{t:.35,side:1,id:'indep'}],
  cit:[{t:.5,n:L('Ms. Han','한 해설사'),role:L('Independence Hall guide','독립기념관 해설사'),p:'독립기념관 해설사. 입장은 무료, 11~2월 09:30~17:00, 3~10월 09:30~18:00, 입장 마감은 닫기 1시간 전, 매주 월요일 휴관(월요일이 공휴일이면 연다)이라고 안내한다. 하얀 겨레의 탑과 큰 전시관, 독립운동 전시관을 소개한다. 천안아산역과 천안역 동부광장에서 815번 버스가 독립기념관으로 간다고 알려 주되 시간표는 그날 확인하라고 한다. 천안 명물 호두과자도 권한다. 가게 가격은 게임 속 예시다.'}]},
 ony:{noBoard:1,spots:[{t:.1,side:1,k:'bus',id:'b_dgj',n:L('Intercity bus to Dangjin','당진 가는 시외버스'),fare:7100,ride:{kind:'bus',scen:'country',title:L('Intercity bus Asan → Dangjin','시외버스 아산 → 당진'),col:'#2e5a86',stops:[L('Asan Intercity Bus Terminal','아산시외버스터미널'),L('Dangjin Bus Terminal','당진버스터미널'),L('Waemok Village','왜목마을')],gap:1100,vmax:30,intro:L('🚌 Asan Intercity Bus Terminal → Dangjin Bus Terminal: 13 a day (07:15–21:45), 1 h 2–13 min, ₩7,100. From Dangjin, a local bus or taxi to Waemok Village.','🚌 아산시외버스터미널 → 당진버스터미널: 하루 13회(07:15~21:45), 1시간 2~13분, 7,100원. 당진에서 시내버스나 택시로 왜목마을에 가요.'),dest:{sc:'wmk',at:0}}},
   st('eat_ony',.62,-1,L('Hot spring bathhouse','온천탕'),L('Staff','직원'),[[L('Hot spring bath, adult (example)','온천탕 어른 (예시)'),10000],[L('Banana milk','바나나우유'),1800]],'♨')],
  sights:[{t:.35,side:-1,id:'onyang'}],doors:[{t:.5,side:1,to:'hotel',n:L('Hotel in Onyang','온양 호텔'),lab:'HOTEL'}],
  cit:[{t:.45,n:L('Mrs. Lee','이 사장님'),role:L('Onyang bathhouse owner','온양 온천탕 사장님'),p:'온양온천역 근처에서 온천탕을 하는 사장님. 온양온천은 약 1,300년 역사로 우리나라에서 가장 오래된 온천이라고 전하고, 조선의 세종·세조·숙종·영조·정조가 쉬거나 병을 고치러 왔다고 이야기한다. 알칼리성 온천수로 37~54°C이고, 예를 들어 온양 온천 랜드 온천탕은 어른 10,000원이다. 역 근처 족욕장도 권한다. 메뉴 가격은 게임 속 예시다.'}]},
 wmk:{noBoard:1,spots:[],links:[{t:.9,id:'l_hmi',n:L('🚕 Taxi to Haemieupseong','🚕 해미읍성까지 택시'),s:L('Few buses on this route','이 구간은 버스가 적어요'),to:'hmi',at:0}],
  sights:[{t:.45,side:1,id:'waemok'}],
  cit:[{t:.6,n:L('Mr. Kim','김 선장님'),role:L('Waemok fisherman','왜목마을 어부'),p:'당진 석문면 왜목마을의 어부. 왜목마을은 태안반도 가장 북쪽 끝에 있어 해돋이와 해넘이, 달맞이까지 한 곳에서 볼 수 있는 전국 유일의 곳으로 유명하다고 자랑한다. 당진버스터미널에서 시내버스나 택시로 오고, 해미까지는 버스가 적어 택시가 편하다고 말한다.'}]},
 hmi:{noBoard:1,spots:[{t:.06,side:1,k:'bus',id:'b_amy',n:L('Bus to Anmyeondo','안면도 가는 버스'),fare:7800,ride:{kind:'bus',scen:'country',title:L('Bus Seosan → Anmyeondo','버스 서산 → 안면도'),col:'#2e5a86',stops:[L('Haemi','해미'),L('Seosan Bus Terminal','서산공용버스터미널'),L('Anmyeondo','안면도'),L('Kkotji Beach','꽃지해수욕장')],gap:1100,vmax:30,intro:L('🚌 City bus from Haemi to Seosan Bus Terminal, then the intercity bus to Anmyeondo: about 1 h 5 min, ₩7,800 (9 a day the other way, 07:25–17:40). From Anmyeon, a local bus or taxi to Kkotji Beach.','🚌 해미에서 시내버스로 서산공용버스터미널에 가서 안면도 가는 시외버스를 타요. 약 1시간 5분, 7,800원(반대 방향 하루 9회 07:25~17:40). 안면에서 시내버스나 택시로 꽃지해수욕장에 가요.'),dest:{sc:'kkj',at:.12}}}],
  sights:[{t:.45,side:-1,id:'haemi'}],
  cit:[{t:.3,n:L('Mr. Yoon','윤 해설사'),role:L('Haemieupseong guide','해미읍성 해설사'),p:'서산 해미읍성 문화관광해설사. 1491년(성종 22년)에 쌓은 읍성으로 둘레 약 1.8km, 높이 약 5m라고 설명한다. 입장·주차 무료, 연중무휴, 11~2월 06:00~19:00, 3~10월 05:00~21:00. 천주교 박해 때 충청도의 많은 신자가 끌려와 1866년에 약 1,000명이 처형됐다는 기록과 광장의 오래된 나무 이야기를 조심스럽게 들려준다. 서산 간장게장·어리굴젓 같은 먹거리도 권한다.'}]},
 kkj:{noBoard:1,spots:[st('eat_kkj',.6,-1,L('Seafood restaurant','해물 식당'),L('Owner','사장님'),[[L('Ganjang-gejang set (example)','간장게장 정식 (예시)'),25000],[L('Seafood kalguksu','해물칼국수'),12000]],'🦀')],
  links:[{t:.08,id:'l_dcb',n:L('🚕 Taxi through the undersea tunnel','🚕 해저터널 지나 택시'),s:L('To Daecheon Beach, Boryeong','보령 대천해수욕장으로'),to:'dcb',at:0}],
  sights:[{t:.4,side:1,id:'kkotji'},{t:.15,side:-1,id:'tunnel'}],doors:[{t:.03,side:-1,to:'hotel',n:L('Hotel on Anmyeondo','안면도 호텔'),lab:'HOTEL'}],
  cit:[{t:.5,n:L('Ms. Choi','최 사장님'),role:L('Kkotji café owner','꽃지 카페 사장님'),p:'꽃지해수욕장 앞 카페 사장님. 꽃지는 안면도에서 가장 큰 해변으로 늘 열려 있고 해넘이로 유명하다. 할미바위·할아비바위는 명승 제69호(2009년)이고, 장보고의 부하 승언이 돌아오지 않자 아내 미도가 바위에서 기다리다 돌이 됐다는 전설을 들려준다. 보령해저터널(6,927m, 2021년 11월 30일 개통, 국내 최장)과 원산안면대교로 대천까지 차로 금방이라고 말한다.'}]},
 dcb:{noBoard:1,spots:[{t:.12,side:1,k:'shuttle',id:'jh_ys',n:L('Train to Yongsan','용산 가는 기차'),fare:11700,ride:{kind:'train',scen:'country',title:L('Train Daecheon → Yongsan','기차 대천 → 용산'),col:'#c8202a',stops:[L('Daecheon','대천'),L('Onyangoncheon','온양온천'),L('Cheonan','천안'),L('Yongsan','용산')],gap:1100,vmax:30,intro:L('🚆 Bus or taxi to Daecheon Station (about 10–15 min). Daecheon → Yongsan: 14–15 trains a day (06:17–21:11), 2 h 30–56 min. Mugunghwa ₩11,700, Saemaeul ₩17,400.','🚆 버스나 택시로 대천역까지 약 10~15분. 대천 → 용산: 하루 14~15회(06:17~21:11), 2시간 30~56분. 무궁화 11,700원, 새마을 17,400원.'),dest:{sc:'sar',at:0}}},
   st('eat_dcb',.55,-1,L('Shellfish grill','조개구이 집'),L('Owner','사장님'),[[L('Grilled shellfish (example, 2 people)','조개구이 (예시, 2인)'),50000],[L('Shellfish kalguksu','바지락칼국수'),11000]],'🦪')],
  sights:[{t:.4,side:1,id:'daecheon'},{t:.2,side:-1,id:'dctrain'}],
  cit:[{t:.3,n:L('Mr. Jung','정 선생님'),role:L('Daecheon Beach information','대천해수욕장 안내원'),p:'대천해수욕장 안내원. 하얀 백사장이 약 3.5km이고 늘 열려 있다. 해마다 여름 보령머드축제가 열린다(2026년은 7월 24일~8월 9일). 스카이바이크는 바다 위 8~15m 레일로 대천항까지 왕복 2.3km, 약 40분이며 밀물 때 타기를 권한다. 해변 끝 보령머드체험관에 머드 사우나·머드팩이 있다. 대천역은 버스나 택시로 약 10~15분.'}]},
 sar:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'yongsan'}],cit:[{t:.55,n:L('Mr. Oh','오 역무원'),role:L('Yongsan Station staff','용산역 역무원'),p:'용산역 역무원. 지하철 1호선과 경의중앙선으로 갈아타는 길을 안내한다.'}],fin:{t:.85,s:L('3 days in Chungnam and the west coast','충남·서해안 2박 3일')}}};

"""

R['info']='const CRUISE_INFO="이 게임은 여행자가 용산역에서 기차를 타고 충남과 서해안을 2박 3일 동안 돌고(천안·아산 온양온천·당진 왜목마을·서산 해미읍성·태안 안면도 꽃지·보령 대천) 기차로 용산역에 돌아오는 가상 3D 여행이다. 1일: 용산→천안 기차(하루 37~38회, 1시간 00~20분, 무궁화 6,100원·ITX-마음/ITX-새마을/새마을 9,000원, 2026년 11월 기준) → 천안역에서 버스·택시로 독립기념관(무료; 11~2월 09:30~17:00, 3~10월 09:30~18:00, 입장 마감 1시간 전; 월요일 휴관, 공휴일이면 개관; 815번 버스가 천안아산역·천안역 동부광장과 독립기념관을 이어 줌; 겨레의 탑, 큰 전시관; 셔틀 어른 5,000원으로 안내돼 있으나 당일 확인) → 천안 호두과자 → 천안역에서 장항선 기차로 온양온천(13~16분, 하루 19회, 무궁화 2,600원·ITX 4,800원) → 온양온천(약 1,300년, 우리나라에서 가장 오래된 온천; 세종·세조·숙종·영조·정조가 다녀감; 알칼리성 37~54°C; 예: 온양 온천 랜드 온천탕 어른 10,000원; 역 근처 족욕장) → 온양 호텔. 2일: 아산시외버스터미널→당진버스터미널(하루 13회 07:15~21:45, 1시간 2~13분, 7,100원) → 시내버스·택시로 왜목마을(당진 석문면, 태안반도 최북단, 일출·일몰·월출을 한 곳에서 보는 전국 유일의 곳) → 버스가 적어 택시로 서산 해미읍성(무료·주차 무료, 연중무휴, 11~2월 06:00~19:00, 3~10월 05:00~21:00; 1491년 성종 22년, 둘레 약 1.8km 높이 5m; 1866년 천주교 신자 약 1,000명 처형 기록, 고문에 쓰인 고목) → 시내버스로 서산공용버스터미널 → 안면도 시외버스(약 1시간 5분, 7,800원, 안면 출발 하루 9회 07:25~17:40) → 꽃지해수욕장(안면읍, 안면도 최대 해변, 상시 개방, 해넘이 명소; 할미·할아비 바위 명승 제69호 2009년; 장보고의 부하 승언과 아내 미도 전설) → 안면도 호텔. 3일: 택시로 원산안면대교(1.8km, 2019년 12월)와 보령해저터널(6,927m, 국내 최장·세계 5위, 2021년 11월 30일 개통, 해수면 아래 약 80m; 대천항→영목항 90분이 약 10분으로) → 대천해수욕장(백사장 약 3.5km, 상시; 보령머드축제 2026년 7월 24일~8월 9일; 스카이바이크 바다 위 8~15m 왕복 2.3km 약 40분; 보령머드체험관 머드 사우나·머드팩) → 버스·택시로 대천역(약 10~15분) → 대천→용산 기차(하루 14~15회 06:17~21:11, 2시간 30~56분, 무궁화 11,700원·새마을 17,400원) → 용산역(지하철 1호선·경의중앙선). 게임 속 식사·가게 가격은 예시다.";\n'

R['real']="""const REAL={
 yongsan:{n:L('Yongsan Station','용산역'),sub:L('Janghang Line trains','장항선 열차'),ll:[37.53,126.9647],q:'용산역',f:[L('Janghang Line trains leave here for Cheonan, Onyangoncheon and the west coast.','장항선 열차가 여기서 천안·온양온천·서해안으로 떠나요.'),L('Change to subway Line 1 or the Gyeongui–Jungang Line.','지하철 1호선과 경의중앙선으로 갈아타요.')]},
 jhtrain:{n:L('Yongsan → Cheonan · Onyang','용산 → 천안 · 온양'),sub:L('Train fares (Nov 2026)','기차 요금 (2026년 11월 기준)'),q:'용산역',f:[L('To Cheonan: 37–38 a day, 1 h 00–1 h 20 min. Mugunghwa ₩6,100; ITX and Saemaeul ₩9,000.','천안: 하루 37~38회, 1시간 00~20분. 무궁화 6,100원, ITX·새마을 9,000원.'),L('To Onyangoncheon: 16 a day, 1 h 23–35 min. Mugunghwa ₩7,000; Saemaeul and ITX-Maeum ₩10,400.','온양온천: 하루 16회, 1시간 23~35분. 무궁화 7,000원, 새마을·ITX-마음 10,400원.')]},
 indep:{n:L('The Independence Hall of Korea','독립기념관'),sub:L('Cheonan','천안'),ll:[36.7836,127.2238],q:'독립기념관',f:[L('Free. Nov–Feb 09:30–17:00; Mar–Oct 09:30–18:00 (last entry 1 h before closing).','입장 무료. 11~2월 09:30~17:00, 3~10월 09:30~18:00(입장 마감은 닫기 1시간 전).'),L('Closed on Mondays (open when Monday is a public holiday).','매주 월요일 휴관(월요일이 공휴일이면 열어요).'),L('Bus 815 links Cheonan-Asan Station and Cheonan Station East Square with the hall.','815번 버스가 천안아산역·천안역 동부광장과 독립기념관을 이어 줘요.')]},
 onytrain:{n:L('Cheonan → Onyangoncheon','천안 → 온양온천'),sub:L('Janghang Line','장항선'),q:'온양온천역',f:[L('13–16 min, 19 a day. Mugunghwa ₩2,600, ITX ₩4,800. (Nov 2026)','13~16분, 하루 19회. 무궁화 2,600원, ITX 4,800원. (2026년 11월 기준)')]},
 onyang:{n:L('Onyang Hot Spring','온양온천'),sub:L('Asan','아산'),ll:[36.7802,127.0036],q:'온양온천역',f:[L('Said to be Korea’s oldest hot spring, about 1,300 years old.','약 1,300년 된 우리나라에서 가장 오래된 온천이라고 해요.'),L('Joseon kings Sejong, Sejo, Sukjong, Yeongjo and Jeongjo came here.','조선의 세종·세조·숙종·영조·정조가 다녀갔어요.'),L('Alkaline water, 37–54°C. Example: Onyang Oncheon Land, adult ₩10,000.','알칼리성, 37~54°C. 예: 온양 온천 랜드 어른 10,000원.')]},
 dgjbus:{n:L('Asan → Dangjin bus','아산 → 당진 버스'),sub:L('Intercity bus','시외버스'),q:'아산시외버스터미널',f:[L('13 a day (07:15–21:45), 1 h 2–13 min, ₩7,100. (Nov 2026)','하루 13회(07:15~21:45), 1시간 2~13분, 7,100원. (2026년 11월 기준)')]},
 waemok:{n:L('Waemok Village','왜목마을'),sub:L('Seongmun-myeon, Dangjin','당진 석문면'),ll:[37.0446,126.5242],q:'왜목마을',f:[L('At the northern tip of the Taean Peninsula.','태안반도 가장 북쪽 끝에 있어요.'),L('Known as the only place in Korea to see sunrise, sunset and moonrise from one spot.','해돋이·해넘이·달맞이를 한 곳에서 볼 수 있는 전국 유일의 곳으로 유명해요.')]},
 haemi:{n:L('Haemieupseong Walled Town','해미읍성'),sub:L('Seosan','서산'),ll:[36.7136,126.5489],q:'해미읍성',f:[L('Free, free parking, open every day. Nov–Feb 06:00–19:00; Mar–Oct 05:00–21:00.','입장·주차 무료, 연중무휴. 11~2월 06:00~19:00, 3~10월 05:00~21:00.'),L('Built in 1491; the wall is about 1.8 km around and 5 m high.','1491년에 쌓았어요. 둘레 약 1.8km, 높이 5m.'),L('About 1,000 Catholics are recorded as executed here in 1866.','1866년 이곳에서 천주교 신자 약 1,000명이 처형됐다는 기록이 있어요.')]},
 amybus:{n:L('Seosan ↔ Anmyeondo bus','서산 ↔ 안면도 버스'),sub:L('Intercity bus','시외버스'),q:'서산공용버스터미널',f:[L('About 1 h 5 min, ₩7,800. From Anmyeondo 9 a day (07:25–17:40). (Nov 2026)','약 1시간 5분, 7,800원. 안면도 출발 하루 9회(07:25~17:40). (2026년 11월 기준)')]},
 kkotji:{n:L('Kkotji Beach','꽃지해수욕장'),sub:L('Anmyeon-eup, Taean','태안 안면읍'),ll:[36.4977,126.3354],q:'꽃지해수욕장',f:[L('The largest beach on Anmyeondo, always open, famous for sunsets.','안면도에서 가장 큰 해변. 늘 열려 있고 해넘이로 유명해요.'),L('Halmi and Halabi Rocks: national Scenic Site No. 69 (2009).','할미·할아비 바위: 명승 제69호(2009년).'),L('Legend of Seungeon, a commander under Jang Bogo, and his wife Mido.','장보고의 부하 승언과 아내 미도의 전설이 전해요.')]},
 tunnel:{n:L('Boryeong Undersea Tunnel','보령해저터널'),sub:L('Daecheon Port ↔ Wonsando','대천항 ↔ 원산도'),q:'보령해저터널',f:[L('6,927 m: Korea’s longest undersea tunnel, opened 30 Nov 2021; about 80 m below the sea surface.','6,927m, 국내 최장 해저터널. 2021년 11월 30일 개통, 해수면 아래 약 80m.'),L('With the Wonsan–Anmyeon Bridge (1.8 km), Daecheon Port → Yeongmok Port went from about 90 min to about 10 min by car.','원산안면대교(1.8km)와 함께 대천항 → 영목항이 차로 약 90분에서 약 10분이 됐어요.')]},
 daecheon:{n:L('Daecheon Beach','대천해수욕장'),sub:L('Boryeong','보령'),ll:[36.3091,126.5133],q:'대천해수욕장',f:[L('White sand about 3.5 km long, always open.','하얀 모래 약 3.5km, 늘 열려 있어요.'),L('Boryeong Mud Festival every summer (2026: 24 July–9 August). Mud Experience Center at the end of the beach.','해마다 여름 보령머드축제(2026년 7월 24일~8월 9일). 해변 끝에 보령머드체험관.'),L('Sky Bike: rails 8–15 m above the sea, 2.3 km round trip, about 40 min.','스카이바이크: 바다 위 8~15m 레일, 왕복 2.3km, 약 40분.')]},
 dctrain:{n:L('Daecheon → Yongsan','대천 → 용산'),sub:L('Janghang Line','장항선'),q:'대천역',f:[L('14–15 trains a day (06:17–21:11), 2 h 30–56 min. Mugunghwa ₩11,700, Saemaeul ₩17,400. (Nov 2026)','하루 14~15회(06:17~21:11), 2시간 30~56분. 무궁화 11,700원, 새마을 17,400원. (2026년 11월 기준)'),L('Daecheon Station to the beach: bus or taxi, about 10–15 min.','대천역 ↔ 해수욕장: 버스·택시로 약 10~15분.')]},
};
"""

R['qz']="""const QZ={
 yst:[[/Train to Cheonan|천안 가는 기차/,'nq1',L('How much is a Mugunghwa ticket from Yongsan to Cheonan?','용산 → 천안 무궁화호 요금은?'),['₩6,100','₩16,100','₩26,100'],0,L('₩6,100 (ITX ₩9,000).','6,100원이에요(ITX 9,000원).')]],
 cna:[[/Onyangoncheon|온양온천 가는/,'nq2',L('On which day is the Independence Hall closed?','독립기념관은 무슨 요일에 쉴까요?'),[L('Mondays','월요일'),L('Wednesdays','수요일'),L('Sundays','일요일')],0,L('Mondays (open if Monday is a public holiday).','월요일이에요(공휴일이면 열어요).')]],
 ony:[[/Dangjin|당진/,'nq3',L('About how old is the Onyang hot spring said to be?','온양온천은 약 몇 년 됐다고 할까요?'),[L('About 1,300 years','약 1,300년'),L('About 130 years','약 130년'),L('About 30 years','약 30년')],0,L('About 1,300 years: Korea’s oldest hot spring.','약 1,300년, 우리나라에서 가장 오래된 온천이에요.')]],
 wmk:[[/Haemieupseong|해미읍성까지/,'nq4',L('What is Waemok Village famous for?','왜목마을은 무엇으로 유명할까요?'),[L('Sunrise, sunset and moonrise in one place','해돋이·해넘이·달맞이를 한 곳에서'),L('A ski slope','스키장'),L('A desert','사막')],0,L('You can see sunrise, sunset and moonrise from one spot.','해돋이·해넘이·달맞이를 한 곳에서 볼 수 있어요.')]],
 hmi:[[/Anmyeondo|안면도 가는/,'nq5',L('When was Haemieupseong built?','해미읍성은 언제 쌓았을까요?'),['1491','1891','1991'],0,L('In 1491, under King Seongjong.','1491년, 성종 때예요.')]],
 kkj:[[/🚕/,'nq6',L('What are the two rocky islets at Kkotji called?','꽃지 앞 두 바위섬 이름은?'),[L('Halmi and Halabi Rocks','할미·할아비 바위'),L('Dragon Head Rock','용두암'),L('The Three Peaks','삼봉')],0,L('Halmi (grandma) and Halabi (grandpa) Rocks.','할미바위와 할아비바위예요.')]],
 dcb:[[/Yongsan|용산 가는/,'nq7',L('Which festival is held at Daecheon Beach every summer?','대천해수욕장에서 해마다 여름에 열리는 축제는?'),[L('Boryeong Mud Festival','보령머드축제'),L('Snow Festival','눈 축제'),L('Lantern Festival','등 축제')],0,L('The Boryeong Mud Festival (2026: 24 July–9 August).','보령머드축제예요(2026년 7월 24일~8월 9일).')]]};
"""

R['rem']="h(L('Remember','꼭 기억할 것'));[L('Yongsan → Cheonan train ₩6,100 (Mugunghwa) · about 1 h','용산 → 천안 기차 6,100원(무궁화) · 약 1시간'),L('Independence Hall free · closed Mondays · winter 09:30–17:00','독립기념관 무료 · 월요일 휴관 · 겨울 09:30~17:00'),L('Cheonan → Onyangoncheon train 13–16 min · ₩2,600','천안 → 온양온천 기차 13~16분 · 2,600원'),L('Asan → Dangjin bus ₩7,100 · Waemok by local bus or taxi','아산 → 당진 버스 7,100원 · 왜목은 시내버스·택시'),L('Haemieupseong free · open every day','해미읍성 무료 · 연중무휴'),L('Seosan → Anmyeondo bus about 1 h 5 min · ₩7,800','서산 → 안면도 버스 약 1시간 5분 · 7,800원'),L('Boryeong Undersea Tunnel 6,927 m: Anmyeondo ↔ Daecheon by car','보령해저터널 6,927m: 안면도 ↔ 대천 차로'),L('Daecheon → Yongsan train ₩11,700 · 2 h 30–56 min','대천 → 용산 기차 11,700원 · 2시간 30~56분'),"

R['areako']="const AREAKO={yongsan:'용산역',jhtrain:'용산역',indep:'천안 독립기념관',onytrain:'온양온천역',onyang:'아산 온양온천역',dgjbus:'당진버스터미널',waemok:'당진 왜목마을',haemi:'서산 해미읍성',amybus:'서산공용버스터미널',kkotji:'태안 꽃지해수욕장',tunnel:'보령 대천항',daecheon:'보령 대천해수욕장',dctrain:'대천역'};"

R['foods']="""
  {k:'호두과자',e:'hodu-gwaja (walnut cakes)',s:'Walnut cakes',ic:'🌰',re:/호두과자|walnut|hodu/i},
  {k:'간장게장',e:'ganjang-gejang (soy-marinated crab)',s:'Soy crab',ic:'🦀',re:/게장|gejang|crab/i},
  {k:'조개구이',e:'grilled shellfish',s:'Grilled shellfish',ic:'🦪',re:/조개|shellfish|clam/i},
  {k:'어리굴젓',e:'eorigul-jeot (spicy salted oysters)',s:'Salted oysters',ic:'🦪',re:/굴젓|oyster/i},
  {k:'해물칼국수',e:'seafood kalguksu',s:'Seafood noodles',ic:'🍜',re:/칼국수|kalguksu|noodle/i},"""

R['phrase']="['온양온천역 어디예요?','Onyang-oncheon-yeok eodi-yeyo?',L('Where is Onyangoncheon Station?','온양온천역 어디예요?')]"
R['stP']="$('stP').textContent=L('Take the train from Yongsan to Cheonan and see the Independence Hall, then soak your feet in Onyang, Korea’s oldest hot spring. Watch the sea at Waemok Village in Dangjin, walk the walls of Haemieupseong in Seosan and catch the sunset at the Halmi and Halabi Rocks on Anmyeondo. Cross the Boryeong Undersea Tunnel to Daecheon Beach before the train back to Seoul. Real fares, times and photos.','용산에서 기차로 천안에 가서 독립기념관을 보고, 우리나라에서 가장 오래된 온양온천에 발을 담가요. 당진 왜목마을 바다를 보고, 서산 해미읍성 성곽을 걷고, 안면도 할미·할아비 바위 해넘이를 봐요. 보령해저터널을 지나 대천해수욕장에 들렀다가 기차로 서울에 돌아와요. 실제 요금·시간·사진을 담았어요.');"
R['stR']="$('stR').textContent=L('Yongsan · Cheonan · Independence Hall · Onyang Hot Spring · Asan · Dangjin · Waemok Village · Seosan · Haemieupseong · Anmyeondo · Kkotji Beach · Boryeong Undersea Tunnel · Daecheon Beach · Yongsan','용산 · 천안 · 독립기념관 · 온양온천 · 아산 · 당진 · 왜목마을 · 서산 · 해미읍성 · 안면도 · 꽃지해수욕장 · 보령해저터널 · 대천해수욕장 · 용산');"
R['rgn']="const RGN={jh:'장항선 JANGHANG LINE  천안·온양온천·대천',yst0:L('Yongsan Station. Trains for Cheonan, Onyang and the west coast leave from here.','용산역이에요. 천안·온양·서해안 가는 기차가 여기서 떠나요.'),yst8:L('Buy tickets on the Korail Talk app, at a ticket window or a ticket machine.','표는 코레일톡 앱, 매표창구, 자동발매기에서 사요.'),arr:'용산역 YONGSAN STATION',arrLine:'1 용산역 · LINE 1',arrLineCol:'#0052a4',arrNotes:[[0,L('Yongsan Station. Welcome back to Seoul!','용산역이에요. 서울에 돌아왔어요!')],[.5,L('Change here to subway Line 1 or the Gyeongui–Jungang Line.','여기서 지하철 1호선과 경의중앙선으로 갈아타요.')]]};"
r=Region(S);r.build(R);r.save('cnm.html')
