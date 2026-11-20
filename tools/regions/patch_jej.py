# 가상 제주 2박 3일 (jej.html): 김포공항 출발 · 제주시 · 성산 · 서귀포 · 김포공항 도착
# 공통 생성기(region_base.py)가 서울 엔진을 받고, 이 파일의 자료로 바꿔 끼웁니다.
# 사실 출처(2026-11-20 확인):
#  김포↔제주 비행 약 1시간 10분 (trvlogue 2026-08-14, 수정 2026-10-03), 약 1시간 15분·하루 약 105편·7개 항공사·11월 왕복 평균 97,442원 (hotelscombined, 요금 2026-11-14 갱신) — 요금은 날짜·항공사마다 바뀜
#  제주 버스 요금(2026년 1월 기준): 간선·지선·관광지순환 교통카드 1,150원·현금 1,200원(거리 상관없음), 급행 카드 2,000~3,000원(거리비례),
#   공항리무진 600번 공항→서귀포(칼호텔) 5,500원, 중문 경유 (jeju.com 2026-07-31, 수정 2026-11-17); 600번 전 구간 약 80분, 201번 제주버스터미널–성산일출봉–서귀포터미널 15~30분 간격 (trazy 2026-02-27)
#  112번 급행 제주공항→제주버스터미널→…→성산일출봉 입구→성산항, 약 2시간 10분, 06:40~21:10 (daily-dave, 2026년 10월 기준); 111번 급행 06:50~21:30 (my-blog 2026-08)
#  용두암: 무료, 상시, 연중무휴, 용·백마 전설 (ktriptips 2025-10-24); 공항에서 약 10분, 동문시장 약 15분, 8번 게이트 야시장 18시부터 (jeju.com 2026-11-16)
#  동문재래시장: 07:00~21:00(가게마다 다름), 연중무휴, 갈치·흑돼지 등 (ktriptips 2026-11-11)
#  성산일출봉: 어른 5,000원, 11~2월 06:00~18:00(매표 17:00), 3~4·9~10월 05:00~19:00, 5~8월 04:30~20:00, 매달 첫째 월요일 휴무(공휴일이면 다음 날), 해발 180m, 유네스코 세계자연유산 (ktriptips 2026-03-26);
#   정상까지 20~30분 (trvlogue 2026-09-30), 왕복 약 50분 (jeju.com 2026-11-16)
#  천지연폭포: 어른 2,000원, 09:00~22:00(입장 21:20), 연중무휴, 담팔수 자생지·무태장어 서식지 천연기념물 (ktriptips 2026-07-29)
#  외돌개: 무료, 상시(일몰 전 권장), 약 20m 돌기둥, 장군석·할망바위, 최영 장군 이야기, 올레 7코스 시작점 (ktriptips 2025-10-23)
#  김포공항역: 5·9호선, 공항철도, 서해선(2023-07-01), 김포골드라인 (itwiki)
import os,sys
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
sys.path.insert(0,S)
from region_base import Region
R=dict(id='jej',title='Virtual Jeju · 가상 제주 3일',money=300000,metro='jbus',start='gmp',
 top=['K_region_top.js','K_jnm_top.js','K_cbk_top.js','K_jej_top.js'],br=['K_region_br.js','K_jej_br.js'],ph='ph/PH_jej.json',
 enter=('Start at Gimpo Airport','김포공항에서 시작하기'),hotel=('Jeju','제주'),
 hotel_note=('Your hotel room for tonight: Jeju City on night 1, Seogwipo on night 2.','오늘 밤 묵을 호텔 방이에요. 첫날 밤은 제주시, 둘째 날 밤은 서귀포예요.'),
 chip=('Good black pork place nearby?','흑돼지 맛집 어디예요?'),deep=('dmm',.4),eyebrow='GIMPO → JEJU · SEONGSAN · SEOGWIPO',
 stH=('Virtual Jeju<br>3 days','가상 제주<br>2박 3일'),wx=('33.4996','126.5312'),city_name=('Jeju','제주'),
 stamps_title=('Jeju stamps','제주 스탬프'),guide_role=('Your Jeju tour guide','제주 여행 가이드'),
 course_ko='제주 2박 3일 코스',guide_line=('Ask me anything about Jeju!','제주에 대해 무엇이든 물어보세요!'),
 virtual=('Virtual Jeju','가상 제주','가상 제주로'))

R['stamps']="""const STAMPS=[{id:'ydm',name:L('Yongduam','용두암'),date:'D1',c:'#3d3b38'},{id:'dmm',name:L('Dongmun Market','동문시장'),date:'D1',c:'#f39a1e'},{id:'ssi',name:L('Seongsan Ilchulbong','성산일출봉'),date:'D2',c:'#4f9a3a'},{id:'cjy',name:L('Cheonjiyeon Falls','천지연폭포'),date:'D2',c:'#2e8fd0'},{id:'odg',name:L('Oedolgae','외돌개'),date:'D3',c:'#1f6fa8'}];
"""

R['scn']="""const SCN={
 gmp:{b:'seoul',o:{city:'gmp'},name:L('Gimpo Airport · Domestic','김포공항 · 국내선')},cju:{b:'seoul',o:{city:'cju'},name:L('Jeju International Airport','제주국제공항')},
 ydm:{b:'seoul',o:{city:'ydm'},name:L('Yongduam','용두암')},dmm:{b:'seoul',o:{city:'dmm'},name:L('Dongmun Market','동문재래시장')},
 ssi:{b:'seoul',o:{city:'ssi'},name:L('Seongsan Ilchulbong','성산일출봉')},cjy:{b:'seoul',o:{city:'cjy'},name:L('Seogwipo · Cheonjiyeon Falls','서귀포 · 천지연폭포')},
 odg:{b:'seoul',o:{city:'odg'},name:L('Seogwipo · Oedolgae','서귀포 · 외돌개')},gmpa:{b:'seoul',o:{city:'gmpa'},name:L('Gimpo Airport · Arrivals','김포공항 · 도착')},
 hotel:{b:'hotel',name:L('Hotel room · Jeju City / Seogwipo','호텔 방 · 제주시 / 서귀포')},ride:{b:'ride',name:''}};
const SHIPMAP=[['gmp',L('Gimpo Airport','김포공항'),L('Flight','비행기')],['cju',L('Jeju Airport','제주공항'),L('Flight','비행기')],['ydm',L('Yongduam','용두암'),L('Taxi','택시')],['dmm',L('Dongmun Market','동문시장'),L('Bus · taxi','버스·택시')],['ssi',L('Seongsan Ilchulbong','성산일출봉'),L('Express bus','급행버스')],['cjy',L('Cheonjiyeon Falls','천지연폭포'),L('Bus 201','201번 버스')],['odg',L('Oedolgae','외돌개'),L('Taxi','택시')],['gmpa',L('Gimpo Airport','김포공항'),L('Flight','비행기')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

"""

R['days']="""const DAYS=[
 {tag:'DAY 1',title:L('Gimpo → Jeju City','김포 출발 · 제주시'),time:L('Flight Gimpo → Jeju (about 1 h 10 min) → Yongduam → Dongmun Market night market','김포 → 제주 비행기(약 1시간 10분) → 용두암 → 동문시장 야시장'),q:[
  {t:'',n:L('Find your flight on the departure board','전광판에서 항공편 확인'),sc:'gmp',at:.45,near:1,r:'gimpo'},
  {t:'',n:L('Board the flight to Jeju','제주 가는 비행기 타기'),sc:'gmp',at:.82,a:'flt',r:'flight'},
  {t:'',n:L('Meet the dol hareubang','돌하르방 만나기'),sc:'cju',at:.4,near:1,r:'dolhar'},
  {t:'',n:L('Taxi to Yongduam (about 10 min)','택시로 용두암 (약 10분)'),sc:'cju',at:.92,a:'l_ydm'},
  {t:'',n:L('The Dragon Head Rock','용 머리 바위'),sc:'ydm',at:.45,near:1,r:'yongduam'},
  {t:'',n:L('Yongduam stamp','용두암 스탬프'),sc:'ydm',at:.97,a:'stamp'},
  {t:'',n:L('Bus or taxi to Dongmun Market','버스·택시로 동문시장'),sc:'ydm',at:.9,a:'l_dmm'},
  {t:'',n:L('Dinner at the night market','야시장에서 저녁'),sc:'dmm',at:.75,a:'eat_nm',r:'dongmun'},
  {t:'',n:L('Dongmun Market stamp','동문시장 스탬프'),sc:'dmm',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Seongsan → Seogwipo','성산 · 서귀포'),time:L('Express bus to Seongsan (up to about 2 h 10 min) → climb Seongsan Ilchulbong → bus 201 to Seogwipo → Cheonjiyeon Falls in the evening','급행버스로 성산(최대 약 2시간 10분) → 성산일출봉 오르기 → 201번 버스로 서귀포 → 저녁 천지연폭포'),q:[
  {t:'',n:L('Express bus to Seongsan','성산 가는 급행버스'),sc:'dmm',at:.04,a:'b_ssi',r:'jbus'},
  {t:'',n:L('Climb Seongsan Ilchulbong (₩5,000)','성산일출봉 오르기 (5,000원)'),sc:'ssi',at:.5,a:'climb',r:'seongsan'},
  {t:'',n:L('Seongsan Ilchulbong stamp','성산일출봉 스탬프'),sc:'ssi',at:.99,a:'stamp'},
  {t:'',n:L('Bus 201 to Seogwipo','201번 버스로 서귀포'),sc:'ssi',at:.04,a:'b_sgp',r:'bus201'},
  {t:'',n:L('Cheonjiyeon Falls (₩2,000)','천지연폭포 (2,000원)'),sc:'cjy',at:.9,near:1,r:'cheonjiyeon'},
  {t:'',n:L('Cheonjiyeon stamp','천지연 스탬프'),sc:'cjy',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Seogwipo · back to Seoul','서귀포 · 서울로'),time:L('Oedolgae and Olle Route 7 → airport limousine 600 (about 80 min) → flight to Gimpo','외돌개 · 올레 7코스 → 공항리무진 600번(약 80분) → 김포 가는 비행기'),q:[
  {t:'',n:L('Taxi to Oedolgae','택시로 외돌개'),sc:'cjy',at:.08,a:'l_odg'},
  {t:'',n:L('The lone rock of Oedolgae','바다 위 외돌개'),sc:'odg',at:.45,near:1,r:'oedolgae'},
  {t:'',n:L('Oedolgae stamp','외돌개 스탬프'),sc:'odg',at:.97,a:'stamp'},
  {t:'',n:L('Airport limousine 600 (₩5,500)','공항리무진 600번 (5,500원)'),sc:'odg',at:.06,a:'b_600',r:'bus600'},
  {t:'',n:L('Flight back to Gimpo','김포로 돌아가는 비행기'),sc:'cju',at:.12,a:'flt_b',r:'flight'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'gmpa',at:.85,a:'trip'}]}];

"""

FLT_EN='✈ Flight Gimpo → Jeju: about 1 h 10 min, about 105 flights a day on 7 airlines (Nov 2026). Fares change by date and airline; ₩50,000 here is only an example.'
FLT_KO='✈ 김포 → 제주 비행기: 약 1시간 10분, 7개 항공사가 하루 약 105편(2026년 11월 기준). 요금은 날짜·항공사마다 달라요. 여기 50,000원은 예시예요.'
R['city']="""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1150,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 gmp:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'flt',n:L('Flight to Jeju','제주 가는 비행기'),fare:50000,ride:{kind:'train',scen:'sky',title:L('Flight Gimpo → Jeju','비행기 김포 → 제주'),col:'#2e5a86',stops:[L('Gimpo','김포'),L('Jeju','제주')],gap:1100,vmax:50,intro:L('"""+FLT_EN+"""','"""+FLT_KO+"""'),intro2:L('Flight Gimpo → Jeju. Walk the aisle or take a free seat; look out of the window!','김포 → 제주 비행기예요. 통로를 걷거나 빈자리에 앉아 창밖을 봐요!'),dest:{sc:'cju',at:0}}},
   st('eat_gmp',.3,-1,L('Airport café','공항 카페'),L('Barista','바리스타'),[[L('Americano','아메리카노'),4500],[L('Sandwich','샌드위치'),6500],[L('Bottled water','생수'),1200]],'☕')],
  sights:[{t:.14,side:1,id:'gimpo'},{t:.75,side:-1,id:'flight'}],
  cit:[{t:.5,n:L('Seoyeon','서연'),role:L('Airline check-in staff','항공사 체크인 직원'),p:'김포공항 국내선 항공사 직원. 제주 가는 비행기는 약 1시간 10분이고 7개 항공사가 하루 약 105편 운항한다(2026년 11월 기준). 요금은 날짜·시간·항공사마다 달라 앱에서 비교하라고 권한다. 국내선도 신분증이 꼭 필요하고, 모바일 탑승권을 쓸 수 있다고 안내한다. 게임 속 50,000원은 예시다.'}]},
 cju:{noBoard:1,spots:[{t:.12,side:-1,k:'shuttle',id:'flt_b',n:L('Flight back to Gimpo','김포 가는 비행기'),fare:50000,ride:{kind:'train',scen:'sky',title:L('Flight Jeju → Gimpo','비행기 제주 → 김포'),col:'#2e5a86',stops:[L('Jeju','제주'),L('Gimpo','김포')],gap:1100,vmax:50,intro:L('✈ Flight Jeju → Gimpo: about 1 h 10 min. Fares change by date; ₩50,000 here is only an example.','✈ 제주 → 김포 비행기: 약 1시간 10분. 요금은 날짜마다 달라요. 여기 50,000원은 예시예요.'),dest:{sc:'gmpa',at:0}}}],
  links:[{t:.92,id:'l_ydm',n:L('🚕 Taxi to Yongduam','🚕 용두암까지 택시'),s:L('About 10 min','약 10분'),to:'ydm',at:0}],
  sights:[{t:.3,side:1,id:'jejuair'},{t:.42,side:-1,id:'dolhar'},{t:.72,side:1,id:'jbus'}],
  cit:[{t:.6,n:L('Mr. Ko','고 선생님'),role:L('Jeju tourist information desk','제주 관광안내소 직원'),p:'제주국제공항 관광안내소 직원. 제주 버스는 간선·지선 교통카드 1,150원(현금 1,200원, 거리 상관없음), 급행버스는 카드 2,000~3,000원(거리비례)이라고 안내한다. 성산 방면 급행 111·112번, 서귀포 가는 공항리무진 600번(중문 경유, 서귀포 칼호텔까지 5,500원, 전 구간 약 80분)과 800번을 알려 준다. 용두암은 공항에서 약 10분, 동문시장은 약 15분 거리다. 돌하르방은 제주 현무암으로 만든 돌 할아버지 석상이다.'}]},
 ydm:{noBoard:1,spots:[],links:[{t:.9,id:'l_dmm',n:L('🚌 Bus or taxi to Dongmun Market','🚌 동문시장까지 버스·택시'),s:L('About 15 min','약 15분'),to:'dmm',at:0}],
  sights:[{t:.45,side:1,id:'yongduam'}],
  cit:[{t:.6,n:L('Mrs. Kang','강 할머니'),role:L('Jeju local','제주 토박이'),p:'용두암 앞을 산책하는 제주 토박이 할머니. 용두암은 입장 무료에 늘 열려 있고, 한라산 신령의 구슬을 훔친 용이 화살을 맞고 바다에 떨어져 머리만 돌이 됐다는 이야기와, 용이 되고 싶던 백마가 장수에게 잡혀 바위가 됐다는 이야기를 들려준다. 해 질 녘 풍경이 좋고, 동문시장은 차로 약 15분이라고 말한다. 제주 사투리를 조금 섞어 말한다(예: 혼저 옵서예 = 어서 오세요).'}]},
 dmm:{noBoard:1,spots:[{t:.04,side:1,k:'bus',id:'b_ssi',n:L('Express bus to Seongsan','성산 가는 급행버스'),fare:3000,ride:{kind:'bus',scen:'country',title:L('Express bus 112 → Seongsan','급행버스 112번 → 성산'),col:'#c8202a',stops:[L('Jeju Bus Terminal','제주버스터미널'),L('Gyorae','교래'),L('Seongsan Ilchulbong','성산일출봉 입구')],gap:1100,vmax:30,intro:L('🚌 Express buses 111 and 112 run from Jeju Airport and Jeju Bus Terminal to Seongsan. Card fare ₩2,000–3,000 by distance. Bus 112 takes about 2 h 10 min to Seongsan Port.','🚌 급행버스 111·112번이 제주공항·제주버스터미널에서 성산까지 가요. 교통카드 2,000~3,000원(거리비례). 112번은 성산항까지 약 2시간 10분.'),dest:{sc:'ssi',at:0}}},
   st('eat_nm',.75,-1,L('Night market stall','야시장 노점'),L('Vendor','상인'),[[L('Black pork skewer','흑돼지 꼬치'),8000],[L('Hallabong juice','한라봉 주스'),5000],[L('Omegi rice cake (box)','오메기떡 (한 상자)'),10000],[L('Cutlassfish gimbap','갈치 김밥'),9000]],'🍢')],
  sights:[{t:.3,side:1,id:'dongmun'}],doors:[{t:.2,side:1,to:'hotel',n:L('Hotel in Jeju City','제주시 호텔'),lab:'HOTEL'}],
  cit:[{t:.5,n:L('Mrs. Moon','문 사장님'),role:L('Dongmun Market vendor','동문시장 상인'),p:'동문재래시장에서 감귤과 한라봉을 파는 상인. 시장은 연중무휴, 대략 07:00~21:00(가게마다 다름)이고, 저녁 6시쯤부터 8번 게이트 근처 야시장에 먹거리 노점이 선다고 말한다. 갈치, 흑돼지, 오메기떡, 고기국수 같은 제주 먹거리를 권한다. 메뉴 가격은 게임 속 예시다.'}]},
 ssi:{noBoard:1,spots:[{t:.04,side:1,k:'bus',id:'b_sgp',n:L('Bus 201 to Seogwipo','서귀포 가는 201번 버스'),fare:1150,ride:{kind:'bus',scen:'country',title:L('Bus 201 Seongsan → Seogwipo','201번 버스 성산 → 서귀포'),col:'#2e5a86',stops:[L('Seongsan Ilchulbong','성산일출봉'),L('Pyoseon','표선'),L('Seogwipo','서귀포')],gap:1100,vmax:28,intro:L('🚌 Bus 201 runs along the east and south coast: Jeju Bus Terminal – Seongsan Ilchulbong – Seogwipo, every 15–30 minutes. ₩1,150 by card, any distance.','🚌 201번 버스는 동쪽·남쪽 해안을 따라 제주버스터미널–성산일출봉–서귀포터미널을 15~30분 간격으로 다녀요. 교통카드 1,150원, 거리 상관없음.'),dest:{sc:'cjy',at:0}}}],
  sights:[{t:.22,side:-1,id:'seongsan'}],
  lifts:[{id:'climb',y:41,ic:'⛰',down:L('⛰ Walk back down','⛰ 걸어서 내려가기'),n:L('Seongsan Ilchulbong','성산일출봉'),fare:5000,msg:L('Up the steep stairs: about 20–30 minutes to the top…','가파른 계단을 올라가요. 정상까지 약 20~30분…'),top:L('The bowl-shaped crater, about 180 m above the sea.','그릇 모양 분화구예요. 해발 약 180m.')}],
  cit:[{t:.3,n:L('Ms. Hyun','현 해설사'),role:L('Seongsan Ilchulbong guide','성산일출봉 해설사'),p:'성산일출봉 문화관광해설사. 바다에서 솟은 응회구로 해발 약 180m이고 제주 유네스코 세계자연유산의 하나라고 설명한다. 어른 5,000원, 11~2월 06:00~18:00(매표 17:00까지), 3~4·9~10월 05:00~19:00, 5~8월 04:30~20:00, 매달 첫째 월요일 휴무(공휴일이면 다음 날). 정상까지 약 20~30분, 왕복 약 50분, 계단이 가파르다. 해돋이 명소라 이름이 일출봉이다. 새해 첫날 해맞이 등반은 따로 신청해야 할 수 있다.'}]},
 cjy:{noBoard:1,spots:[],links:[{t:.08,id:'l_odg',n:L('🚕 Taxi to Oedolgae','🚕 외돌개까지 택시'),s:L('Seogwipo coast','서귀포 해안'),to:'odg',at:0}],
  sights:[{t:.35,side:1,id:'cheonjiyeon'}],doors:[{t:.03,side:-1,to:'hotel',n:L('Hotel in Seogwipo','서귀포 호텔'),lab:'HOTEL'}],
  cit:[{t:.5,n:L('Mr. Boo','부 선생님'),role:L('Cheonjiyeon ticket office','천지연폭포 매표소 직원'),p:'천지연폭포 매표소 직원. 어른 2,000원, 연중무휴 09:00~22:00(입장 마감 21:20)이라 저녁에 조명 켜진 산책도 좋다고 안내한다. 협곡에 담팔수 자생지와 무태장어 서식지가 있고 둘 다 천연기념물이라고 설명한다.'}]},
 odg:{noBoard:1,spots:[{t:.06,side:1,k:'bus',id:'b_600',n:L('Airport limousine 600','공항리무진 600번'),fare:5500,ride:{kind:'bus',scen:'country',title:L('Airport limousine 600 → Jeju Airport','공항리무진 600번 → 제주공항'),col:'#2e8fd0',stops:[L('Seogwipo','서귀포'),L('Jungmun','중문'),L('Jeju Airport','제주공항')],gap:1100,vmax:32,intro:L('🚌 Airport limousine 600: Seogwipo (KAL Hotel) → Jungmun → Jeju Airport, ₩5,500. The whole route takes about 80 minutes.','🚌 공항리무진 600번: 서귀포(칼호텔) → 중문 → 제주공항, 5,500원. 전 구간 약 80분.'),dest:{sc:'cju',at:.06}}}],
  sights:[{t:.45,side:1,id:'oedolgae'},{t:.12,side:-1,id:'bus600'}],
  cit:[{t:.3,n:L('Ms. Oh','오 선생님'),role:L('Olle trail volunteer','올레길 안내 봉사자'),p:'외돌개에서 올레길을 안내하는 봉사자. 외돌개는 바다에 홀로 선 약 20m 돌기둥으로 입장 무료, 늘 열려 있지만 해 지기 전에 오기를 권한다. 장군석·할망바위라고도 부르고, 최영 장군이 이 바위를 장군처럼 꾸며 적을 물리쳤다는 이야기가 전한다. 제주 올레 7코스가 여기서 시작하며 파랑·주황 리본을 따라 걷는다.'}]},
 gmpa:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'gimpo'}],cit:[{t:.55,n:L('Mr. Seo','서 역무원'),role:L('Gimpo Airport Station staff','김포공항역 역무원'),p:'김포공항역 역무원. 지하철 5·9호선, 공항철도, 서해선, 김포골드라인으로 갈아탈 수 있다고 안내한다.'}],fin:{t:.85,s:L('3 days in Jeju','제주 2박 3일')}}};

"""

R['info']='const CRUISE_INFO="이 게임은 여행자가 김포공항에서 비행기를 타고 제주에 가서 2박 3일 동안 제주시·성산·서귀포를 돌고 비행기로 김포공항에 돌아오는 가상 3D 여행이다. 1일: 김포공항 국내선(제주까지 약 1시간 10분, 7개 항공사 하루 약 105편, 2026년 11월 기준; 요금은 날짜·항공사마다 다르고 게임 속 50,000원은 예시; 국내선도 신분증 필요) → 제주국제공항(돌하르방: 제주 현무암 돌 할아버지 석상; 제주 버스 간선·지선 교통카드 1,150원·현금 1,200원 거리 상관없음, 급행 카드 2,000~3,000원 거리비례) → 택시로 약 10분 용두암(무료, 상시, 연중무휴; 한라산 신령의 구슬을 훔친 용이 화살을 맞아 머리가 돌이 됐다는 전설, 용이 되고 싶던 백마 전설; 해 질 녘 명소) → 차로 약 15분 동문재래시장(연중무휴, 약 07:00~21:00 가게마다 다름; 갈치·흑돼지·오메기떡·감귤·한라봉; 저녁 6시쯤부터 8번 게이트 야시장) → 제주시 호텔. 2일: 급행버스 111·112번(제주공항·제주버스터미널 출발, 112번은 성산항까지 약 2시간 10분) → 성산일출봉(바다에서 솟은 응회구, 해발 약 180m, 유네스코 세계자연유산; 어른 5,000원; 11~2월 06:00~18:00 매표 17:00, 3~4·9~10월 05:00~19:00, 5~8월 04:30~20:00; 매달 첫째 월요일 휴무, 공휴일이면 다음 날; 정상까지 약 20~30분, 왕복 약 50분, 계단 가파름; 새해 첫날 해맞이 등반은 따로 신청해야 할 수 있음) → 201번 버스(제주버스터미널–성산일출봉–서귀포터미널, 15~30분 간격, 교통카드 1,150원) → 천지연폭포(서귀포; 어른 2,000원, 연중무휴 09:00~22:00 입장 마감 21:20; 담팔수 자생지·무태장어 서식지 천연기념물; 저녁 조명) → 서귀포 호텔. 3일: 택시로 외돌개(약 20m 바다 돌기둥, 무료, 상시, 일몰 전 권장; 장군석·할망바위, 최영 장군 이야기; 제주 올레 7코스 시작점) → 공항리무진 600번(서귀포 칼호텔 → 중문 → 제주공항, 5,500원, 전 구간 약 80분; 800번은 중문을 거치지 않음) → 제주국제공항 → 비행기로 김포공항(지하철 5·9호선, 공항철도, 서해선, 김포골드라인). 게임 속 식사·가게 가격은 예시다.";\n'

R['real']="""const REAL={
 gimpo:{n:L('Gimpo International Airport','김포국제공항'),sub:L('Domestic terminal','국내선'),ll:[37.5587,126.7945],q:'김포공항 국내선',f:[L('About 105 flights a day to Jeju on 7 airlines (Nov 2026).','제주 가는 비행기가 7개 항공사, 하루 약 105편(2026년 11월 기준).'),L('Gimpo Airport Station: subway Lines 5 and 9, AREX, the Seohae Line and the Gimpo Goldline.','김포공항역: 지하철 5·9호선, 공항철도, 서해선, 김포골드라인.'),L('Domestic flights need ID too.','국내선도 신분증이 필요해요.')]},
 flight:{n:L('Gimpo ↔ Jeju flights','김포 ↔ 제주 비행기'),sub:L('About 1 h 10 min','약 1시간 10분'),q:'김포공항 국내선',f:[L('Flight time about 1 h 10–15 min, about 451 km.','비행시간 약 1시간 10~15분, 약 451km.'),L('Fares change by date, time and airline: in November 2026 round trips averaged about ₩97,000 on one fare site.','요금은 날짜·시간·항공사마다 달라요. 2026년 11월 한 항공권 사이트 기준 왕복 평균 약 97,000원.'),L('₩50,000 in this game is only an example.','게임 속 50,000원은 예시예요.')]},
 jejuair:{n:L('Jeju International Airport','제주국제공항'),sub:L('Jeju City','제주시'),ll:[33.5104,126.4914],q:'제주국제공항',f:[L('Yongduam is about 10 minutes away by car; Dongmun Market about 15 minutes.','용두암은 차로 약 10분, 동문시장은 약 15분.'),L('Airport limousine 600 goes to Jungmun and Seogwipo; 800 goes to Seogwipo without Jungmun.','공항리무진 600번은 중문·서귀포, 800번은 중문을 거치지 않고 서귀포로 가요.')]},
 dolhar:{n:L('Dol hareubang','돌하르방'),sub:L('Stone grandfathers','돌 할아버지'),q:'돌하르방',f:[L('Stone statues carved from Jeju’s black volcanic basalt, a symbol of the island.','제주의 검은 현무암으로 깎은 돌 석상으로, 제주의 상징이에요.')]},
 yongduam:{n:L('Yongduam (Dragon Head Rock)','용두암'),sub:L('North coast, Jeju City','제주시 북쪽 바닷가'),ll:[33.5163,126.5121],q:'용두암',f:[L('Free; open all the time, every day.','입장 무료, 늘 열려 있어요. 연중무휴.'),L('Legend: a dragon that stole a jewel from the spirit of Hallasan was shot down, and its head turned to stone.','전설: 한라산 신령의 구슬을 훔친 용이 화살을 맞고 떨어져 머리가 돌이 됐대요.'),L('Next to it, the Yongyeon gorge trail (about 20 min). A sunset spot.','옆에 용연 계곡 산책길(약 20분)이 있어요. 노을 명소예요.')]},
 dongmun:{n:L('Dongmun Traditional Market','동문재래시장'),sub:L('Jeju City','제주시'),q:'동문재래시장',f:[L('Open every day, about 07:00–21:00 (each shop differs).','연중무휴, 약 07:00~21:00(가게마다 달라요).'),L('Night market near Gate 8 from about 18:00.','8번 게이트 근처 야시장은 저녁 6시쯤부터.'),L('Cutlassfish (galchi), black pork, tangerines and hallabong.','갈치, 흑돼지, 감귤, 한라봉.')]},
 jbus:{n:L('Jeju buses','제주 버스'),sub:L('Fares (Jan 2026)','요금 (2026년 1월 기준)'),q:'제주버스터미널',f:[L('Trunk, feeder and sightseeing loop buses: ₩1,150 by card, ₩1,200 cash, any distance.','간선·지선·관광지순환: 교통카드 1,150원, 현금 1,200원, 거리 상관없음.'),L('Express buses: ₩2,000–3,000 by card, by distance.','급행버스: 카드 2,000~3,000원(거리비례).'),L('Express 111 and 112 go to Seongsan; 112 takes about 2 h 10 min to Seongsan Port.','급행 111·112번이 성산으로 가요. 112번은 성산항까지 약 2시간 10분.')]},
 seongsan:{n:L('Seongsan Ilchulbong','성산일출봉'),sub:L('Sunrise Peak · UNESCO World Natural Heritage','해돋이 봉우리 · 유네스코 세계자연유산'),ll:[33.4589,126.9407],q:'성산일출봉',f:[L('Adult ₩5,000. Nov–Feb 06:00–18:00 (tickets until 17:00); Mar–Apr and Sep–Oct 05:00–19:00; May–Aug 04:30–20:00.','어른 5,000원. 11~2월 06:00~18:00(매표 17:00까지), 3~4·9~10월 05:00~19:00, 5~8월 04:30~20:00.'),L('Closed on the first Monday of each month (the next day if that Monday is a holiday).','매달 첫째 월요일 휴무(공휴일이면 다음 날).'),L('About 180 m high. About 20–30 min to the top; about 50 min up and down.','해발 약 180m. 정상까지 약 20~30분, 왕복 약 50분.')]},
 bus201:{n:L('Bus 201','201번 버스'),sub:L('Jeju – Seongsan – Seogwipo','제주–성산–서귀포'),q:'서귀포버스터미널',f:[L('Along the east and south coast, every 15–30 minutes.','동쪽·남쪽 해안을 따라 15~30분 간격.'),L('₩1,150 by card, any distance.','교통카드 1,150원, 거리 상관없음.')]},
 cheonjiyeon:{n:L('Cheonjiyeon Falls','천지연폭포'),sub:L('Seogwipo','서귀포'),ll:[33.2471,126.5544],q:'천지연폭포',f:[L('Adult ₩2,000. Open every day 09:00–22:00 (last entry 21:20).','어른 2,000원. 연중무휴 09:00~22:00(입장 마감 21:20).'),L('Habitat of the dampalsu tree and the giant mottled eel, both natural monuments.','담팔수 자생지와 무태장어 서식지로, 둘 다 천연기념물이에요.')]},
 oedolgae:{n:L('Oedolgae','외돌개'),sub:L('Seogwipo coast','서귀포 해안'),ll:[33.2397,126.5451],q:'외돌개',f:[L('A lone sea stack about 20 m tall. Free; always open, best before sunset.','바다에 홀로 선 약 20m 돌기둥. 입장 무료, 늘 열려 있고 해 지기 전에 가는 게 좋아요.'),L('Also called the General Rock: General Choe Yeong is said to have dressed it up as a soldier to scare off the enemy.','장군석이라고도 해요. 최영 장군이 장군처럼 꾸며 적을 물리쳤다는 이야기가 전해요.'),L('The start of Jeju Olle Route 7.','제주 올레 7코스 시작점이에요.')]},
 bus600:{n:L('Airport limousine 600','공항리무진 600번'),sub:L('Seogwipo – Jungmun – Jeju Airport','서귀포–중문–제주공항'),q:'공항리무진 600',f:[L('Seogwipo (KAL Hotel) ↔ Jeju Airport ₩5,500; Jungmun ₩5,000. Students get discounts.','서귀포(칼호텔) ↔ 제주공항 5,500원, 중문 5,000원. 학생 할인이 있어요.'),L('The whole route takes about 80 minutes.','전 구간 약 80분.')]},
};
"""

R['qz']="""const QZ={
 gmp:[[/Flight to Jeju|제주 가는 비행기/,'jq1',L('About how long is the flight from Gimpo to Jeju?','김포 → 제주 비행기는 약 얼마나 걸릴까요?'),[L('About 1 h 10 min','약 1시간 10분'),L('About 3 h','약 3시간'),L('About 5 h','약 5시간')],0,L('About 1 h 10 min. About 105 flights a day.','약 1시간 10분이에요. 하루 약 105편이 다녀요.')]],
 cju:[[/Yongduam|용두암/,'jq2',L('What are Jeju’s stone grandfather statues called?','제주의 돌 할아버지 석상 이름은?'),[L('Dol hareubang','돌하르방'),L('Dokkaebi','도깨비'),L('Haetae','해태')],0,L('Dol hareubang, carved from black basalt.','돌하르방이에요. 검은 현무암으로 깎았어요.')]],
 ydm:[[/Dongmun|동문시장/,'jq3',L('In the legend, Yongduam is the head of which animal?','전설에서 용두암은 어떤 동물의 머리일까요?'),[L('A dragon','용'),L('A tiger','호랑이'),L('A turtle','거북')],0,L('A dragon: Yong-du-am means “dragon head rock”.','용이에요. 용두암은 “용 머리 바위”라는 뜻이에요.')]],
 dmm:[[/Seongsan|성산/,'jq4',L('From about what time does the night market near Gate 8 start?','8번 게이트 근처 야시장은 몇 시쯤 시작할까요?'),[L('About 18:00','저녁 6시쯤'),L('About 06:00','새벽 6시쯤'),L('About 12:00','낮 12시쯤')],0,L('From about 18:00.','저녁 6시쯤부터예요.')]],
 ssi:[[/⛰ (Seongsan|성산)/,'jq5',L('How much is adult admission to Seongsan Ilchulbong?','성산일출봉 어른 입장료는?'),['₩5,000','₩15,000','₩50,000'],0,L('₩5,000. Closed on the first Monday of each month.','5,000원이에요. 매달 첫째 월요일은 쉬어요.')]],
 cjy:[[/Oedolgae|외돌개/,'jq6',L('Until what time is Cheonjiyeon Falls open?','천지연폭포는 몇 시까지 열까요?'),['15:00','18:00','22:00'],2,L('Until 22:00 (last entry 21:20).','22:00까지예요(입장 마감 21:20).')]],
 odg:[[/600/,'jq7',L('Oedolgae is the start of which Jeju Olle route?','외돌개는 제주 올레 몇 코스의 시작점일까요?'),[L('Route 7','7코스'),L('Route 1','1코스'),L('Route 21','21코스')],0,L('Route 7.','7코스예요.')]]};
"""

R['rem']="h(L('Remember','꼭 기억할 것'));[L('Flight Gimpo → Jeju about 1 h 10 min · fares change by date','김포 → 제주 비행기 약 1시간 10분 · 요금은 날짜마다 달라요'),L('Bring ID for domestic flights','국내선도 신분증 필요'),L('Jeju buses ₩1,150 by card (any distance) · express ₩2,000–3,000','제주 버스 교통카드 1,150원(거리 상관없음) · 급행 2,000~3,000원'),L('Yongduam free · Dongmun night market from about 18:00','용두암 무료 · 동문시장 야시장 저녁 6시쯤부터'),L('Seongsan Ilchulbong ₩5,000 · closed 1st Monday · winter 06:00–18:00','성산일출봉 5,000원 · 매달 첫째 월요일 휴무 · 겨울 06:00~18:00'),L('Cheonjiyeon Falls ₩2,000 · open until 22:00','천지연폭포 2,000원 · 22:00까지'),L('Oedolgae free · Olle Route 7 starts here','외돌개 무료 · 올레 7코스 시작점'),L('Airport limousine 600 Seogwipo → airport ₩5,500 · about 80 min','공항리무진 600번 서귀포 → 공항 5,500원 · 약 80분'),"

R['areako']="const AREAKO={gimpo:'김포공항',flight:'김포공항',jejuair:'제주국제공항',dolhar:'제주국제공항',yongduam:'제주 용두암',dongmun:'제주 동문재래시장',jbus:'제주버스터미널',seongsan:'성산일출봉',bus201:'서귀포',cheonjiyeon:'서귀포 천지연폭포',oedolgae:'서귀포 외돌개',bus600:'서귀포'};"

R['foods']="""
  {k:'흑돼지',e:'Jeju black pork',s:'Black pork BBQ',ic:'🥓',re:/흑돼지|black pork/i},
  {k:'고기국수',e:'gogi-guksu (pork noodle soup)',s:'Pork noodles',ic:'🍜',re:/고기국수|gogi|noodle/i},
  {k:'갈치조림',e:'braised cutlassfish',s:'Cutlassfish',ic:'🐟',re:/갈치|cutlassfish|galchi/i},
  {k:'전복죽',e:'abalone porridge',s:'Abalone porridge',ic:'🥣',re:/전복|abalone/i},
  {k:'오메기떡',e:'omegi rice cake',s:'Omegi rice cake',ic:'🍡',re:/오메기|omegi/i},"""

R['phrase']="['동문시장 어디예요?','Dongmun-sijang eodi-yeyo?',L('Where is Dongmun Market?','동문시장 어디예요?')]"
R['stP']="$('stP').textContent=L('Fly from Gimpo to Jeju. Meet the dol hareubang, see the Dragon Head Rock of Yongduam and eat at the Dongmun night market. Take the express bus to Seongsan Ilchulbong and climb to its crater, follow the coast on bus 201 to Seogwipo, walk to Cheonjiyeon Falls in the evening and the sea stack of Oedolgae before the limousine bus and the flight back to Gimpo. Real fares, times and photos.','김포에서 비행기로 제주에 가요. 돌하르방을 만나고 용두암을 보고 동문시장 야시장에서 저녁을 먹어요. 급행버스로 성산일출봉에 가서 분화구까지 오르고, 201번 버스로 해안을 따라 서귀포에 가요. 저녁에는 천지연폭포, 다음 날은 외돌개를 보고 리무진 버스와 비행기로 김포에 돌아와요. 실제 요금·시간·사진을 담았어요.');"
R['stR']="$('stR').textContent=L('Gimpo Airport · Flight · Jeju Airport · Dol hareubang · Yongduam · Dongmun Market · Express bus · Seongsan Ilchulbong · Bus 201 · Cheonjiyeon Falls · Oedolgae · Olle Route 7 · Limousine 600 · Gimpo Airport','김포공항 · 비행기 · 제주공항 · 돌하르방 · 용두암 · 동문시장 · 급행버스 · 성산일출봉 · 201번 버스 · 천지연폭포 · 외돌개 · 올레 7코스 · 리무진 600번 · 김포공항');"
R['rgn']="const RGN={flt:'✈ 제주 JEJU  탑승 BOARDING',arr:'✈ 제주 JEJU  도착 LANDED',bus:'5 · 600 · 800 리무진 LIMOUSINE',gmp0:L('Gimpo Airport, domestic terminal. Flights to Jeju leave from here all day.','김포공항 국내선이에요. 제주 가는 비행기가 하루 종일 여기서 떠나요.')};"

r=Region(S);r.build(R)
# 비행기 창밖: 구름과 멀리 아래 바다 (P.scen==='sky')
r.rep("if(P.scen==='tunnel'){dark=true;","if(P.scen==='sky'){seaY=-140;for(let k=0;k<16;k++){const gg=new T.Group();for(let c=0;c<3;c++){const sx=rnd()<.5?-1:1,x=sx*(14+rnd()*60),y=-34+rnd()*46,z=-12+rnd()*24;for(let b=0;b<4;b++)sph(gg,3+rnd()*4,M('#ffffff',{transparent:true,opacity:.92}),x+rnd()*8,y+rnd()*3,z+rnd()*8,1.6,.7,1.2);}add(gg,k*30);}for(let i=0;i<6;i++){const h=new T.Mesh(new T.SphereGeometry(70,14,8,0,Math.PI*2,0,Math.PI/2),M('#5f7a4a'));h.scale.y=.3;h.position.set((i%2?1:-1)*(220+rnd()*160),-140,-600+i*240);g.add(h);}sky='day';}\n else if(P.scen==='tunnel'){dark=true;")
r.save('jej.html')
