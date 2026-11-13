# 가상 동해안 2박 3일 (east.html): 강릉 · 정동진 · 속초 · 설악산, 서울역 출발 · 동서울 도착
# 공통 생성기(region_base.py)가 서울 엔진을 받고, 이 파일의 자료로 바꿔 끼웁니다.
# 사실 출처(2026-11 확인):
#  KTX-이음 서울역→강릉 하루 14회 05:06~22:14, 최단 1시간 51분, 보통 2시간~2시간 11분, 일반실 27,600원 (train.asamaru.net 2026-11-13)
#  강릉→정동진 기차 약 15분, 누리로 2,600원 · ITX-마음 4,800원 · KTX-이음 8,400원, 하루 9~10회 (train.asamaru.net 2026-11-13)
#  정동진역: 바다와 가장 가까운 역, 광화문 정동쪽, 1962년, 드라마 모래시계 1995 (ktriptips)
#  모래시계공원: 1999년 강릉시·삼성전자 새 천년 기념, 모래가 1년 동안 떨어짐, 1월 1일 0시에 뒤집음, 무료 (ktriptips 128721, 2026-11-11)
#  오죽헌 어른 3,000원, 09:00~18:00 입장 마감 17:00, 연중무휴, 신사임당·율곡 이이 탄생, 몽룡실, 보물 (위키트리 2026-03-17, ktriptips 129784)
#  안목해변 500m (여행지 정보) · 안목→경포대 7.1km 차로 10분, 경포대→오죽헌 2.8km 4분 (한국관광공사 열린관광 코스, travelmapjourney 2026-10)
#  경포: 강릉역에서 버스·택시 10~15분, 경포대 무료 (travelmapjourney 2026-01-22)
#  강릉·속초 시내버스 어른 교통카드 1,530원 · 현금 1,700원 (2023-01-01부터, 나무위키 2026) · 속초 7·7-1번 소공원행, 속초고속버스터미널 경유
#  강릉→속초 시외버스 하루 20회 07:14~21:00, 1시간~1시간 46분, 7,800/8,400/10,800원 (asamaru 2026-11-10)
#  속초관광수산시장 08:00~24:00쯤, 닭강정·오징어순대·아바이순대 (ktriptips 1260275) · 아바이마을 함경도 실향민 (travelmapjourney 2026)
#  갯배 어른 편도 500원 · 어린이 300원, 11~4월 05:30~22:30, 5~10월 05:00~23:00, 50m 남짓 약 5분, 무동력 (ktriptips 129468, 2026-05-28)
#  설악케이블카 어른 왕복 16,000원, 편도 약 5분 (travelmapjourney 2026) · 신흥사 652년 자장율사, 무료 (koreatriptips 264210)
#  속초고속→동서울 하루 15회 06:45~20:30, 2시간 26분, 우등 22,800원 · 프리미엄 29,600원 (asamaru 2026-11-11)
#  동서울터미널: 2026-09 기준 운영 중, 2027년 상반기 테크노마트 임시 승차장 이전 추진(협의 중) (비즈워치 2026-09-16)
import os,sys
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
sys.path.insert(0,S)
from region_base import Region
R=dict(id='east',title='Virtual East Coast · 가상 동해안 3일',money=300000,metro='citybus',start='sst',
 top=['K_region_top.js','K_east_top.js'],br=['K_region_br.js','K_east_br.js'],ph='ph/PH_east.json',
 enter=('Start at Seoul Station','서울역에서 시작하기'),hotel=('Gangneung','강릉'),
 hotel_note=('Your hotel room for tonight: Gangneung on night 1, Sokcho on night 2.','오늘 밤 묵을 호텔 방이에요. 첫날 밤은 강릉, 둘째 날 밤은 속초예요.'),
 chip=('Good sundubu place nearby?','순두부 맛집 어디예요?'),deep=('gyp',.3),eyebrow='SEOUL → GANGNEUNG · SOKCHO',
 stH=('Virtual East Coast<br>3 days','가상 동해안<br>2박 3일'),wx=('37.7519','128.8761'),city_name=('Gangneung','강릉'),
 stamps_title=('East coast stamps','동해안 스탬프'),guide_role=('Your East coast tour guide','동해안 여행 가이드'),
 course_ko='동해안 2박 3일 코스',guide_line=('Ask me anything about Gangneung, Sokcho and Seoraksan!','강릉·속초·설악산에 대해 무엇이든 물어보세요!'),
 virtual=('Virtual East Coast','가상 동해안','가상 동해안으로'))

R['stamps']="""const STAMPS=[{id:'anm',name:L('Anmok','안목'),date:'D1',c:'#9a6a3a'},{id:'gyp',name:L('Gyeongpo','경포'),date:'D1',c:'#2e8fd0'},{id:'ojk',name:L('Ojukheon','오죽헌'),date:'D1',c:'#6f9a4a'},{id:'jdj',name:L('Jeongdongjin','정동진'),date:'D2',c:'#f0a419'},{id:'skc',name:L('Sokcho','속초'),date:'D2',c:'#e83a5a'},{id:'srk',name:L('Seoraksan','설악산'),date:'D3',c:'#2fae6a'}];
"""

R['scn']="""const SCN={
 sst:{b:'seoul',o:{city:'sst'},name:L('Seoul Station · KTX-Eum','서울역 · KTX-이음')},gns:{b:'seoul',o:{city:'gns'},name:L('Gangneung Station','강릉역')},
 anm:{b:'seoul',o:{city:'anm'},name:L('Anmok Beach · Coffee Street','안목해변 · 커피거리')},gyp:{b:'seoul',o:{city:'gyp'},name:L('Gyeongpodae · Gyeongpo Beach','경포대 · 경포해변')},
 ojk:{b:'seoul',o:{city:'ojk'},name:L('Ojukheon','오죽헌')},jdj:{b:'seoul',o:{city:'jdj'},name:L('Jeongdongjin · Sandglass Park','정동진 · 모래시계공원')},
 skc:{b:'seoul',o:{city:'skc'},name:L('Sokcho Market · Gaetbae · Abai Village','속초 시장 · 갯배 · 아바이마을')},srk:{b:'seoul',o:{city:'srk'},name:L('Seoraksan · Sinheungsa · Cable Car','설악산 · 신흥사 · 케이블카')},
 nbu:{b:'seoul',o:{city:'nbu'},name:L('Dong Seoul Bus Terminal','동서울종합터미널')},hotel:{b:'hotel',name:L('Hotel room · Gangneung / Sokcho','호텔 방 · 강릉 / 속초')},ride:{b:'ride',name:''}};
const SHIPMAP=[['sst',L('Seoul Station','서울역'),'KTX-이음'],['gns',L('Gangneung Station','강릉역'),'KTX-이음'],['anm',L('Anmok','안목'),L('Bus · taxi','버스·택시')],['gyp',L('Gyeongpo','경포'),L('Bus · taxi','버스·택시')],['ojk',L('Ojukheon','오죽헌'),L('Bus · taxi','버스·택시')],['jdj',L('Jeongdongjin','정동진'),L('Train','기차')],['skc',L('Sokcho','속초'),L('Intercity bus','시외버스')],['srk',L('Seoraksan','설악산'),L('Bus 7 / 7-1','7·7-1번 버스')],['nbu',L('Dong Seoul','동서울'),L('Express bus','고속버스')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

"""

R['days']="""const DAYS=[
 {tag:'DAY 1',title:L('Seoul → Gangneung','서울 출발 · 강릉'),time:L('Seoul Station KTX-Eum (about 1 h 51 min+) → Gangneung Station → Anmok coffee street → Gyeongpodae · Gyeongpo Beach → Ojukheon','서울역 KTX-이음(약 1시간 51분~) → 강릉역 → 안목 커피거리 → 경포대 · 경포해변 → 오죽헌'),q:[
  {t:'',n:L('Find your train on the departure board','전광판에서 열차 확인'),sc:'sst',at:.45,near:1,r:'sst'},
  {t:'',n:L('Board the KTX-Eum to Gangneung (₩27,600)','강릉행 KTX-이음 타기 (27,600원)'),sc:'sst',at:.82,a:'ktx',r:'ktx'},
  {t:'',n:L('Bus or taxi to Anmok Beach','버스·택시로 안목해변'),sc:'gns',at:.78,a:'b_anm',r:'citybus'},
  {t:'',n:L('Coffee with a sea view','바다 보며 커피 한 잔'),sc:'anm',at:.45,a:'eat_cf',r:'anmok'},
  {t:'',n:L('Anmok stamp','안목 스탬프'),sc:'anm',at:.97,a:'stamp'},
  {t:'',n:L('To Gyeongpodae (7.1 km)','경포대로 (7.1km)'),sc:'anm',at:.93,a:'b_gyp'},
  {t:'',n:L('Gyeongpodae pavilion','경포대 누각'),sc:'gyp',at:.1,near:1,r:'gyeongpo'},
  {t:'',n:L('Lunch: Chodang sundubu','점심: 초당순두부'),sc:'gyp',at:.3,a:'eat_sd',r:'chodang'},
  {t:'',n:L('Gyeongpo Beach','경포해변'),sc:'gyp',at:.55,near:1,r:'gpbeach'},
  {t:'',n:L('Gyeongpo stamp','경포 스탬프'),sc:'gyp',at:.97,a:'stamp'},
  {t:'',n:L('To Ojukheon (2.8 km)','오죽헌으로 (2.8km)'),sc:'gyp',at:.93,a:'b_ojk'},
  {t:'',n:L('Ojukheon ticket (₩3,000)','오죽헌 입장권 (3,000원)'),sc:'ojk',at:.1,a:'tk_ojk',r:'ojk'},
  {t:'',n:L('Mongryongsil, where Yulgok was born','율곡이 태어난 몽룡실'),sc:'ojk',at:.5,near:1,r:'yulgok'},
  {t:'',n:L('Ojukheon stamp','오죽헌 스탬프'),sc:'ojk',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Jeongdongjin · Sokcho','정동진 · 속초'),time:L('Train to Jeongdongjin (about 15 min) → Sandglass Park → back to Gangneung → intercity bus to Sokcho (about 1 h+) → market · gaetbae · Abai Village','기차로 정동진(약 15분) → 모래시계공원 → 강릉으로 → 시외버스로 속초(약 1시간~) → 시장 · 갯배 · 아바이마을'),q:[
  {t:'',n:L('Train to Jeongdongjin (₩2,600)','정동진 가는 기차 (2,600원)'),sc:'gns',at:.12,a:'jtrain',r:'jdj'},
  {t:'',n:L('The station by the sea','바닷가 기차역'),sc:'jdj',at:.15,near:1,r:'jdj'},
  {t:'',n:L('Walk on Jeongdongjin beach','정동진 해변 걷기'),sc:'jdj',at:.55,near:1},
  {t:'',n:L('The giant hourglass','큰 모래시계'),sc:'jdj',at:.95,near:1,r:'sandglass'},
  {t:'',n:L('Jeongdongjin stamp','정동진 스탬프'),sc:'jdj',at:.97,a:'stamp'},
  {t:'',n:L('Train + intercity bus to Sokcho','기차 + 시외버스로 속초'),sc:'jdj',at:.06,a:'b_skc',r:'skbus'},
  {t:'',n:L('Dakgangjeong at the market','시장에서 닭강정'),sc:'skc',at:.27,a:'eat_dg',r:'skmarket'},
  {t:'',n:L('Cross on the gaetbae','갯배로 건너기'),sc:'skc',at:.58,near:1,r:'gaetbae'},
  {t:'',n:L('Pay the gaetbae fare (₩500)','갯배 요금 내기 (500원)'),sc:'skc',at:.69,a:'gaetbae'},
  {t:'',n:L('Abai sundae in Abai Village','아바이마을에서 아바이순대'),sc:'skc',at:.8,a:'eat_ab',r:'abai'},
  {t:'',n:L('Sokcho stamp','속초 스탬프'),sc:'skc',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Seoraksan · back to Seoul','설악산 · 서울로'),time:L('Bus 7 / 7-1 to Seoraksan → Sinheungsa → Seorak Cable Car → express bus to Dong Seoul (2 h 26 min)','7·7-1번 버스로 설악산 → 신흥사 → 설악케이블카 → 고속버스로 동서울(2시간 26분)'),q:[
  {t:'',n:L('Bus 7 / 7-1 to Seoraksan','7·7-1번 버스로 설악산'),sc:'skc',at:.04,a:'b_srk',r:'citybus'},
  {t:'',n:L('Sinheungsa and its bronze Buddha','신흥사와 청동 대불'),sc:'srk',at:.4,near:1,r:'sinheungsa'},
  {t:'',n:L('Lunch: sanchae bibimbap','점심: 산채비빔밥'),sc:'srk',at:.2,a:'eat_sc'},
  {t:'',n:L('Cable car to Gwongeumseong (₩16,000)','케이블카로 권금성 (16,000원)'),sc:'srk',at:.66,a:'scable',r:'scable'},
  {t:'',n:L('Seoraksan stamp','설악산 스탬프'),sc:'srk',at:.99,a:'stamp'},
  {t:'',n:L('Express bus to Dong Seoul (₩22,800)','동서울 가는 고속버스 (22,800원)'),sc:'srk',at:.08,a:'bus_dsl',r:'dongseoul'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'nbu',at:.85,a:'trip'}]}];

"""

R['city']="""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1530,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 sst:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'ktx',n:L('KTX-Eum to Gangneung','강릉행 KTX-이음'),fare:27600,ride:{kind:'train',scen:'country',title:L('KTX-Eum Seoul → Gangneung','KTX-이음 서울 → 강릉'),col:'#1f4f91',stops:[L('Seoul','서울'),L('Cheongnyangni','청량리'),L('Gangneung','강릉')],gap:900,vmax:50,intro:L('🚆 KTX-Eum to Gangneung, standard class ₩27,600. The fastest trains take about 1 h 51 min; most take about 2 h. (Stops differ by train.)','🚆 강릉행 KTX-이음, 일반실 27,600원. 가장 빠른 열차는 약 1시간 51분, 보통 2시간쯤 걸려요. (정차역은 열차마다 달라요.)'),dest:{sc:'gns',at:0}}},
   st('eat_sst',.3,-1,L('Station kiosk','역 매점'),L('Clerk','직원'),[[L('Gimbap roll','김밥 한 줄'),4000],[L('Bottled water','생수'),1200],[L('Coffee','커피'),4500]],'🥤')],
  sights:[{t:.14,side:1,id:'sst'},{t:.75,side:-1,id:'ktx'}],
  shows:[{id:'cny',t:.2,b:L('🚉 Also from Cheongnyangni','🚉 청량리에서도 타요'),s:L('KTX-Eum to Gangneung','강릉행 KTX-이음'),say:L('KTX-Eum trains to Gangneung leave from Seoul Station, and you can also board them at Cheongnyangni Station. 14 trains a day leave Seoul Station (05:06–22:14, as of Nov 2026).','강릉 가는 KTX-이음은 서울역에서 떠나고, 청량리역에서도 탈 수 있어요. 서울역 출발은 하루 14회예요(05:06~22:14, 2026년 11월 기준).')}],
  cit:[{t:.5,n:L('Jihun','지훈'),role:L('Korail station staff','코레일 역무원'),p:'서울역 역무원. KTX-이음 표 사는 곳(코레일톡 앱·매표창구·자동발매기), 전광판 보는 법, 호차와 좌석 찾기를 안내한다. 강릉까지 일반실 27,600원, 서울역 출발 하루 14회(05:06~22:14), 가장 빠른 열차 약 1시간 51분, 보통 2시간쯤. 청량리역에서도 탈 수 있다.'}]},
 gns:{noBoard:1,spots:[{t:.12,side:1,k:'shuttle',id:'jtrain',n:L('Train to Jeongdongjin','정동진 가는 기차'),fare:2600,ride:{kind:'train',scen:'country',title:L('Train Gangneung → Jeongdongjin','기차 강릉 → 정동진'),col:'#c8202a',stops:[L('Gangneung','강릉'),L('Jeongdongjin','정동진')],gap:600,vmax:20,intro:L('🚆 About 15 minutes. Nuriro ₩2,600 (ITX-Maeum ₩4,800, KTX-Eum ₩8,400). About 9–10 trains a day.','🚆 약 15분 걸려요. 누리로 2,600원(ITX-마음 4,800원, KTX-이음 8,400원). 하루 9~10회쯤 있어요.'),dest:{sc:'jdj',at:0}}},
   {t:.78,side:1,k:'bus',id:'b_anm',n:L('Bus or taxi to Anmok','안목 가는 버스·택시'),fare:1530,ride:{kind:'bus',scen:'city',title:L('City bus → Anmok Beach','시내버스 → 안목해변'),col:'#2fae6a',stops:[L('Gangneung Station','강릉역'),L('Anmok','안목')],gap:700,vmax:14,intro:L('🚌 From Gangneung Station take a city bus or a taxi to Anmok Beach. Bus fare ₩1,530 by card. Check the route in a map app: there are stops on both sides of the road.','🚌 강릉역에서 시내버스나 택시로 안목해변에 가요. 버스는 교통카드 1,530원. 길 양쪽에 정류장이 있으니 지도 앱에서 노선을 확인해요.'),dest:{sc:'anm',at:0}}},
   st('eat_gns',.45,-1,L('Station café','역 카페'),L('Barista','바리스타'),[[L('Americano','아메리카노'),4500],[L('Bottled water','생수'),1200],[L('Gimbap roll','김밥 한 줄'),4000]],'☕')],
  sights:[{t:.36,side:1,id:'gns'},{t:.62,side:-1,id:'citybus'}],
  cit:[{t:.55,n:L('Seoyeon','서연'),role:L('Gangneung local','강릉 시민'),p:'강릉역에서 만난 친절한 강릉 시민. 시내버스 요금(어른 교통카드 1,530원, 현금 1,700원), 강릉역 정류장이 길 양쪽에 따로 있다는 것, 안목 커피거리·경포대·오죽헌 가는 법, 정동진 가는 기차(약 15분)를 알려 준다. 버스 번호는 지도 앱이나 강릉 버스정보에서 확인하라고 한다.'}]},
 anm:{noBoard:1,spots:[st('eat_cf',.45,1,L('Sea-view café','바다 보이는 카페'),L('Barista Yuna','바리스타 유나'),[[L('Hand-drip coffee','핸드드립 커피'),7000],[L('Iced Americano','아이스 아메리카노'),5500],[L('Cake slice','조각 케이크'),7500]],'☕'),
   {t:.93,side:1,k:'bus',id:'b_gyp',n:L('To Gyeongpodae','경포대로'),fare:1530,ride:{kind:'bus',scen:'port',title:L('Anmok → Gyeongpodae','안목 → 경포대'),col:'#2fae6a',stops:[L('Anmok','안목'),L('Gyeongpodae','경포대')],gap:700,vmax:14,intro:L('🚌 About 7.1 km north: around 10 minutes by car. Take a taxi or a city bus (₩1,530 by card).','🚌 북쪽으로 약 7.1km, 차로 10분쯤이에요. 택시나 시내버스(교통카드 1,530원)로 가요.'),dest:{sc:'gyp',at:0}}}],
  sights:[{t:.3,side:-1,id:'anmok'}],
  cit:[{t:.62,n:L('Yuna','유나'),role:L('Café barista','카페 바리스타'),p:'안목해변 커피거리 카페의 바리스타. 바다가 보이는 자리와 핸드드립 커피 이야기를 하고, 경포대까지 북쪽으로 약 7.1km, 차로 10분쯤이라고 알려 준다. 가게 메뉴 가격은 게임 속 예시라고 말한다.'}]},
 gyp:{noBoard:1,spots:[st('eat_sd',.3,1,L('Chodang sundubu restaurant','초당순두부집'),L('Chef Choi','최 사장님'),[[L('Sundubu set (soft tofu)','순두부 백반'),12000],[L('Spicy sundubu stew','순두부찌개'),12000],[L('Tofu pancake','두부전'),15000]],'🥣'),
   {t:.93,side:1,k:'bus',id:'b_ojk',n:L('To Ojukheon','오죽헌으로'),fare:1530,ride:{kind:'bus',scen:'city',title:L('Gyeongpodae → Ojukheon','경포대 → 오죽헌'),col:'#2fae6a',stops:[L('Gyeongpodae','경포대'),L('Ojukheon','오죽헌')],gap:500,vmax:12,intro:L('🚌 Only 2.8 km: about 4 minutes by car. Take a taxi or a city bus.','🚌 2.8km밖에 안 돼요. 차로 4분쯤. 택시나 시내버스로 가요.'),dest:{sc:'ojk',at:0}}}],
  sights:[{t:.08,side:-1,id:'gyeongpo'},{t:.36,side:-1,id:'chodang'},{t:.5,side:-1,id:'gpbeach'}],
  cit:[{t:.4,n:L('Chef Choi','최 사장님'),role:L('Chodang tofu cook','초당순두부 요리사'),p:'경포 근처 초당 순두부마을에서 순두부를 만드는 요리사. 간수 대신 동해 바닷물로 두부를 굳히는 초당두부 이야기, 경포대(경포호 옆 누각, 무료), 경포해변을 이야기하고, 오죽헌까지 2.8km, 차로 4분쯤이라고 알려 준다.'}]},
 ojk:{noBoard:1,spots:[st('tk_ojk',.1,1,L('Ticket office','매표소'),L('Staff','직원'),[[L('Adult ticket','어른 입장권'),3000]],'🎫')],
  sights:[{t:.42,side:-1,id:'ojk'},{t:.62,side:-1,id:'yulgok'}],doors:[{t:.97,side:1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  cit:[{t:.72,n:L('Ms. Kwon','권 해설사'),role:L('Culture guide','문화관광해설사'),p:'오죽헌 문화관광해설사. 신사임당과 아들 율곡 이이가 태어난 곳, 몽룡실(신사임당이 율곡을 낳기 전 용꿈을 꾸었다고 전하는 방), 오죽(까마귀처럼 검은 대나무), 5,000원권의 율곡 이이와 50,000원권의 신사임당 이야기를 한다. 조선 초기 한옥으로 보물이다. 입장 어른 3,000원, 09:00~18:00, 입장 마감 17:00, 연중무휴.'}]},
 jdj:{noBoard:1,spots:[{t:.06,side:1,k:'bus',id:'b_skc',n:L('Train + intercity bus to Sokcho','기차 + 시외버스로 속초'),fare:11000,ride:{kind:'bus',scen:'country',title:L('Jeongdongjin → Gangneung → Sokcho','정동진 → 강릉 → 속초'),col:'#2e5a86',stops:[L('Jeongdongjin','정동진'),L('Gangneung Station','강릉역'),L('Gangneung Intercity Bus Terminal','강릉시외버스터미널'),L('Sokcho Intercity Bus Terminal','속초시외버스터미널')],gap:900,vmax:26,intro:L('🚆🚌 Train back to Gangneung (about 15 min, ₩2,600), city bus or taxi to Gangneung Intercity Bus Terminal, then the intercity bus to Sokcho: 20 a day (07:14–21:00), about 1 h–1 h 46 min, ₩7,800–10,800 (₩8,400 on most buses).','🚆🚌 기차로 강릉에 돌아가(약 15분, 2,600원) 시내버스나 택시로 강릉시외버스터미널에 간 뒤 속초행 시외버스를 타요. 하루 20회(07:14~21:00), 약 1시간~1시간 46분, 7,800~10,800원(가장 흔한 요금 8,400원).'),dest:{sc:'skc',at:0}}}],
  sights:[{t:.15,side:-1,id:'jdj'},{t:.93,side:-1,id:'sandglass'}],
  cit:[{t:.45,n:L('Mr. Bae','배 역무원'),role:L('Jeongdongjin station staff','정동진역 역무원'),p:'정동진역 역무원. 전국에서 바다와 가장 가까운 역으로 꼽히는 이야기, 서울 광화문의 정동쪽이라 정동진이라는 이름(1962년 개업), 1995년 드라마 모래시계, 1999년 강릉시와 삼성전자가 새 천년 기념으로 만든 모래시계(모래가 다 떨어지는 데 1년, 1월 1일 0시에 뒤집음, 무료)를 이야기한다. 강릉까지 기차 약 15분.'}]},
 skc:{noBoard:1,spots:[{t:.04,side:1,k:'bus',id:'b_srk',n:L('Bus 7 / 7-1 to Seoraksan','설악산 가는 7·7-1번 버스'),fare:1530,ride:{kind:'bus',scen:'country',title:L('Bus 7 / 7-1 → Seoraksan','7·7-1번 버스 → 설악산'),col:'#2fae6a',stops:[L('Downtown Sokcho','속초 시내'),L('Sokcho Express Bus Terminal','속초고속버스터미널'),L('Seoraksan Sogongwon','설악산 소공원')],gap:900,vmax:20,intro:L('🚌 City buses 7 and 7-1 go to the Seoraksan Sogongwon entrance (₩1,530 by card). On the way they pass Sokcho Express Bus Terminal, where you will catch the bus back to Seoul.','🚌 시내버스 7번·7-1번이 설악산 소공원 입구까지 가요(교통카드 1,530원). 가는 길에 서울 가는 버스를 탈 속초고속버스터미널을 지나요.'),dest:{sc:'srk',at:0}}},
   st('eat_dg',.27,1,L('Dakgangjeong shop','닭강정 가게'),L('Auntie Okja','옥자 이모'),[[L('Dakgangjeong (medium box)','닭강정 (중)'),20000],[L('Dakgangjeong (cup)','닭강정 컵'),6000]],'🍗'),
   st('eat_os',.35,-1,L('Squid sundae stall','오징어순대 가게'),L('Halmeoni','할머니'),[[L('Squid sundae','오징어순대'),15000],[L('Shrimp tempura','새우튀김'),10000]],'🦑'),
   st('gaetbae',.69,1,L('Gaetbae fare','갯배 요금'),L('Fare box','요금 받는 곳'),[[L('Gaetbae, adult one way','갯배 어른 편도'),500]],'⛴'),
   st('eat_ab',.8,1,L('Abai sundae restaurant','아바이순대집'),L('Owner','사장님'),[[L('Abai sundae','아바이순대'),15000],[L('Mulhoe (cold raw fish soup)','물회'),15000]],'🌭')],
  sights:[{t:.1,side:-1,id:'skmarket'},{t:.5,side:1,id:'gaetbae'},{t:.86,side:-1,id:'abai'}],doors:[{t:.97,side:-1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  cit:[{t:.3,n:L('Auntie Okja','옥자 이모'),role:L('Market vendor','시장 상인'),p:'속초관광수산시장(옛 중앙시장) 상인. 시장은 가게마다 다르지만 08:00~24:00쯤 연다. 닭강정, 오징어순대, 아바이순대, 물회를 권하고, 인기 닭강정은 늦은 오후에 다 팔리기도 한다고 말한다.'},{t:.76,n:L('Grandpa Kim','김 할아버지'),role:L('Abai Village resident','아바이마을 주민'),p:'속초 청호동 아바이마을 주민. 6·25 전쟁 때 함경도에서 내려온 실향민들이 모여 살며 생긴 마을 이야기, 갯배(어른 편도 500원·어린이 300원, 사공 없이 탄 사람들이 갈고리로 줄을 당겨 50m 남짓한 물길을 약 5분에 건넘, 11~4월 05:30~22:30, 5~10월 05:00~23:00)를 이야기한다.'}]},
 srk:{noBoard:1,spots:[{t:.08,side:1,k:'bus',id:'bus_dsl',n:L('Express bus to Dong Seoul','동서울 가는 고속버스'),fare:22800,ride:{kind:'bus',scen:'country',title:L('Express bus Sokcho → Dong Seoul','고속버스 속초 → 동서울'),col:'#2e5a86',stops:[L('Sokcho Express Bus Terminal','속초고속버스터미널'),L('Dong Seoul Bus Terminal','동서울종합터미널')],gap:1300,vmax:30,intro:L('🚌 Bus 7 / 7-1 back to Sokcho Express Bus Terminal, then the express bus to Dong Seoul: 15 a day (06:45–20:30), 2 h 26 min, udeung (premium) ₩22,800.','🚌 7·7-1번 버스로 속초고속버스터미널에 가서 동서울행 고속버스를 타요. 하루 15회(06:45~20:30), 2시간 26분, 우등 22,800원.'),dest:{sc:'nbu',at:0}}},
   st('eat_sc',.2,1,L('Seorak-dong restaurant','설악동 식당'),L('Owner','사장님'),[[L('Sanchae bibimbap (wild greens)','산채비빔밥'),12000],[L('Potato pancake','감자전'),12000]],'🥗')],
  sights:[{t:.4,side:-1,id:'sinheungsa'},{t:.6,side:-1,id:'scable'}],
  lifts:[{id:'scable',y:60,ic:'🚡',down:L('🚡 Cable car down','🚡 케이블카로 내려가기'),n:L('Seorak Cable Car','설악케이블카'),fare:16000,msg:L('The cable car climbs to Gwongeumseong: about 5 minutes…','케이블카가 권금성으로 올라가요. 약 5분…'),top:L('Granite peaks all around, and Sokcho and the East Sea far below.','사방이 화강암 봉우리예요. 멀리 속초와 동해가 내려다보여요.')}],
  cit:[{t:.5,n:L('Ranger Jung','정 레인저'),role:L('National park ranger','국립공원 레인저'),p:'설악산 국립공원 레인저. 속초에서 시내버스 7번·7-1번으로 소공원에 오는 법, 신흥사(652년 자장율사가 처음 세움, 입장 무료, 큰 청동 좌불 통일대불), 설악케이블카(어른 왕복 16,000원, 편도 약 5분, 운행 시간은 계절과 날씨에 따라 다름)를 안내하고, 산에서는 안전하게 다니라고 당부한다.'}]},
 nbu:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'dongseoul'}],cit:[{t:.55,n:L('Ms. Yun','윤 선생님'),role:L('Terminal information desk','터미널 안내원'),p:'동서울종합터미널 안내원. 바로 옆 2호선 강변역 가는 길과 서울 시내로 가는 방법을 안내한다. 터미널 재건축 계획(2027년 상반기 옆 테크노마트 건물로 임시 승차장 이전 추진, 2026년 9월 기준 협의 중)도 알고 있다.'}],fin:{t:.85,s:L('3 days on the East coast','동해안 2박 3일')}}};

"""

R['info']='const CRUISE_INFO="이 게임은 여행자가 서울역에서 KTX-이음을 타고 강릉에 가서 2박 3일 동안 강릉·정동진·속초·설악산을 돌고 고속버스로 동서울에 돌아오는 가상 3D 여행이다. 1일: 서울역 KTX-이음(일반실 27,600원, 서울역 출발 하루 14회 05:06~22:14, 가장 빠른 열차 약 1시간 51분, 보통 2시간~2시간 11분, 청량리역에서도 탐, 2026년 11월 기준) → 강릉역(정류장이 길 양쪽에 따로 있음) → 시내버스나 택시로 안목해변 커피거리(500m 모래 해변, 바닷가 카페) → 경포대(안목에서 북쪽 약 7.1km, 차로 10분쯤; 경포호 옆 언덕의 누각, 무료; 강릉역에서 버스·택시 10~15분)·경포해변·초당 순두부마을(간수 대신 바닷물로 굳힌 초당두부) → 오죽헌(경포대에서 2.8km, 차로 4분쯤; 어른 3,000원, 09:00~18:00, 입장 마감 17:00, 연중무휴; 신사임당과 아들 율곡 이이가 태어난 곳, 몽룡실, 오죽은 까마귀처럼 검은 대나무, 조선 초기 한옥으로 보물; 5,000원권 율곡 이이, 50,000원권 신사임당) → 강릉 호텔. 강릉·속초 시내버스 어른 교통카드 1,530원, 현금 1,700원(2023년 1월부터). 2일: 강릉역 → 정동진 기차(약 15분, 누리로 2,600원·ITX-마음 4,800원·KTX-이음 8,400원, 하루 9~10회쯤) → 정동진역(전국에서 바다와 가장 가까운 역으로 꼽힘, 서울 광화문의 정동쪽이라 정동진, 1962년 개업, 1995년 드라마 모래시계로 유명) → 모래시계공원(1999년 강릉시와 삼성전자가 새 천년 기념으로 조성, 모래가 다 떨어지는 데 꼭 1년, 해마다 1월 1일 0시에 뒤집음, 무료, 상시 개방) → 기차로 강릉 → 강릉시외버스터미널 → 속초시외버스터미널(하루 20회 07:14~21:00, 약 1시간~1시간 46분, 7,800~10,800원, 가장 흔한 요금 8,400원) → 속초관광수산시장(옛 중앙시장, 가게마다 다르지만 08:00~24:00쯤; 닭강정·오징어순대·아바이순대) → 갯배(속초 시내와 아바이마을 사이 50m 남짓한 물길, 약 5분, 엔진과 사공 없이 탄 사람들이 갈고리로 줄을 당김, 어른 편도 500원·어린이 300원, 11~4월 05:30~22:30, 5~10월 05:00~23:00, 날씨에 따라 바뀜) → 아바이마을(속초 청호동, 6·25 전쟁 때 함경도에서 내려온 실향민이 정착) → 속초 호텔. 3일: 시내버스 7번·7-1번(속초고속버스터미널 경유) → 설악산 소공원 → 신흥사(652년 자장율사가 처음 세움, 입장 무료, 청동 좌불 통일대불) → 설악케이블카(권금성, 어른 왕복 16,000원, 편도 약 5분, 운행 시간은 계절과 날씨에 따라 다름) → 7·7-1번 버스로 속초고속버스터미널 → 동서울 고속버스(하루 15회 06:45~20:30, 2시간 26분, 우등 22,800원, 프리미엄 29,600원) → 동서울종합터미널(2호선 강변역 바로 옆; 재건축 예정으로 2027년 상반기 옆 테크노마트 건물에 임시 승차장을 두는 계획이 2026년 9월 기준 협의 중). 게임 속 식사·가게 가격은 예시다.";\n'

R['real']="""const REAL={
 sst:{n:L('Seoul Station','서울역'),sub:L('KTX-Eum to Gangneung','강릉행 KTX-이음'),ll:[37.5555,126.9707],q:'Seoul Station',f:[L('KTX-Eum trains to Gangneung leave from here; you can also board at Cheongnyangni. Tickets: Korail Talk app, ticket windows or machines.','강릉 가는 KTX-이음이 여기서 떠나요. 청량리역에서도 탈 수 있어요. 표: 코레일톡 앱, 매표창구, 자동발매기.'),L('The domed red-brick old station (1925) is now Culture Station Seoul 284.','붉은 벽돌 돔의 옛 서울역(1925)은 지금 문화역서울284예요.')]},
 ktx:{n:L('KTX-Eum','KTX-이음'),sub:L('Seoul → Gangneung','서울 → 강릉'),q:'KTX-Eum Gangneung',f:[L('Standard class Seoul → Gangneung: ₩27,600.','서울 → 강릉 일반실 27,600원.'),L('14 trains a day from Seoul Station (05:06–22:14). The fastest takes about 1 h 51 min; most take 2 h–2 h 11 min. (Nov 2026)','서울역에서 하루 14회(05:06~22:14). 가장 빠른 열차 약 1시간 51분, 보통 2시간~2시간 11분. (2026년 11월 기준)')]},
 gns:{n:L('Gangneung Station','강릉역'),sub:L('KTX-Eum · Gangneung','KTX-이음 · 강릉'),ll:[37.7638,128.8991],q:'강릉역',f:[L('Trains to Jeongdongjin also leave from here: about 15 minutes.','정동진 가는 기차도 여기서 타요. 약 15분.'),L('Gyeongpo is about 10–15 minutes away by bus or taxi.','경포까지 버스나 택시로 10~15분쯤.')]},
 citybus:{n:L('Gangneung · Sokcho city buses','강릉·속초 시내버스'),sub:L('Adult fares','어른 요금'),q:'강릉역 버스정류장',f:[L('Adult fare: ₩1,530 by transport card, ₩1,700 in cash (both cities, since January 2023).','어른 요금: 교통카드 1,530원, 현금 1,700원(두 도시 모두, 2023년 1월부터).'),L('Gangneung Station has separate stops on both sides of the road: check the route in a map app before you ride.','강릉역은 길 양쪽에 정류장이 따로 있어요. 타기 전에 지도 앱에서 노선을 확인해요.'),L('In Sokcho, buses 7 and 7-1 go to Seoraksan (Sogongwon).','속초에서는 7번·7-1번이 설악산 소공원까지 가요.')]},
 anmok:{n:L('Anmok Beach · Coffee Street','안목해변 · 커피거리'),sub:L('Gangneung','강릉'),ll:[37.7735,128.9473],q:'안목해변 커피거리',f:[L('Cafés line the seafront road along a 500 m sandy beach.','500m 모래 해변을 따라 바닷가 길에 카페가 늘어서 있어요.'),L('Gyeongpodae is about 7.1 km north: around 10 minutes by car.','경포대까지 북쪽으로 약 7.1km, 차로 10분쯤이에요.')]},
 gyeongpo:{n:L('Gyeongpodae','경포대'),sub:L('Pavilion by Gyeongpo Lake','경포호 옆 누각'),ll:[37.795,128.8944],q:'경포대',f:[L('A pavilion on a low hill beside Gyeongpo Lake. Free to visit.','경포호 옆 낮은 언덕 위 누각이에요. 무료예요.'),L('About 10–15 minutes from Gangneung Station by bus or taxi.','강릉역에서 버스나 택시로 10~15분쯤.')]},
 chodang:{n:L('Chodang sundubu','초당순두부'),sub:L('Chodang-dong, Gangneung','강릉 초당동'),q:'초당순두부마을',f:[L('Chodang tofu is set with clean East Sea seawater instead of the usual coagulant.','초당두부는 간수 대신 깨끗한 동해 바닷물로 굳혀요.'),L('The tofu village is right next to Gyeongpo Lake.','순두부마을이 경포호 바로 옆에 있어요.')]},
 gpbeach:{n:L('Gyeongpo Beach','경포해변'),sub:L('Pine trees and sand','솔숲과 모래 해변'),ll:[37.8057,128.9108],q:'경포해변',f:[L('A long sandy beach backed by pine trees, next to Gyeongpo Lake.','경포호 옆, 솔숲 뒤로 긴 모래 해변이 펼쳐져요.')]},
 ojk:{n:L('Ojukheon','오죽헌'),sub:L('Early-Joseon house · Treasure','조선 초기 한옥 · 보물'),ll:[37.7786,128.8778],q:'오죽헌',f:[L('Adult ₩3,000. Open every day 09:00–18:00 (last entry 17:00).','어른 3,000원. 연중무휴 09:00~18:00(입장 마감 17:00).'),L('Shin Saimdang and her son Yi I (Yulgok) were born here.','신사임당과 아들 율곡 이이가 여기서 태어났어요.'),L('Ojuk means black bamboo: dark stems grow around the house.','오죽은 검은 대나무라는 뜻이에요. 집 둘레에 검은 대나무가 자라요.')]},
 yulgok:{n:L('Mongryongsil · Yulgok and Saimdang','몽룡실 · 율곡과 신사임당'),sub:L('On the ₩5,000 and ₩50,000 notes','5,000원권 · 50,000원권 인물'),ll:[37.7786,128.8778],q:'오죽헌 몽룡실',f:[L('Mongryongsil is the room where Saimdang is said to have dreamed of a dragon before Yulgok was born.','몽룡실은 신사임당이 율곡을 낳기 전 용꿈을 꾸었다고 전하는 방이에요.'),L('Yi I (Yulgok) is on the ₩5,000 note; his mother Shin Saimdang is on the ₩50,000 note.','5,000원권에는 율곡 이이, 50,000원권에는 어머니 신사임당이 있어요.')]},
 jdj:{n:L('Jeongdongjin Station','정동진역'),sub:L('A station by the sea','바닷가 기차역'),ll:[37.6914,129.033],q:'정동진역',f:[L('Often called the station closest to the sea in Korea. Opened in 1962.','전국에서 바다와 가장 가까운 역으로 꼽혀요. 1962년에 문을 열었어요.'),L('The name: it lies due east (jeong-dong) of Gwanghwamun in Seoul.','서울 광화문의 정동쪽에 있어서 정동진이에요.'),L('Gangneung → Jeongdongjin by train about 15 min: Nuriro ₩2,600, ITX-Maeum ₩4,800, KTX-Eum ₩8,400.','강릉 → 정동진 기차 약 15분: 누리로 2,600원, ITX-마음 4,800원, KTX-이음 8,400원.'),L('It became famous through the 1995 TV drama Sandglass.','1995년 드라마 「모래시계」로 유명해졌어요.')]},
 sandglass:{n:L('Sandglass Park','모래시계공원'),sub:L('Giant hourglass · free','큰 모래시계 · 무료'),q:'정동진 모래시계공원',f:[L('Made in 1999 by Gangneung City and Samsung Electronics for the new millennium.','1999년 강릉시와 삼성전자가 새 천년을 기념해 만들었어요.'),L('The sand takes exactly one year to fall; it is turned over at midnight on 1 January.','모래가 다 떨어지는 데 꼭 1년이 걸려요. 해마다 1월 1일 0시에 뒤집어요.'),L('Open all the time, free.','늘 열려 있고 무료예요.')]},
 skbus:{n:L('Gangneung → Sokcho intercity bus','강릉 → 속초 시외버스'),sub:L('Gangneung Intercity Bus Terminal','강릉시외버스터미널'),q:'강릉시외버스터미널',f:[L('20 buses a day (07:14–21:00), about 1 h to 1 h 46 min.','하루 20회(07:14~21:00), 약 1시간~1시간 46분.'),L('₩7,800–10,800 depending on the bus; ₩8,400 is the most common fare. (Nov 2026)','버스마다 7,800~10,800원, 가장 흔한 요금은 8,400원이에요. (2026년 11월 기준)')]},
 skmarket:{n:L('Sokcho Tourist & Fishery Market','속초관광수산시장'),sub:L('Formerly Jungang Market','옛 중앙시장'),ll:[38.2045,128.5899],q:'속초관광수산시장',f:[L('About 08:00–24:00, depending on the shop.','가게마다 다르지만 08:00~24:00쯤 열어요.'),L('Famous for dakgangjeong (sweet crispy fried chicken), squid sundae and abai sundae.','닭강정, 오징어순대, 아바이순대가 유명해요.'),L('Popular dakgangjeong can sell out by late afternoon.','인기 닭강정은 늦은 오후에 다 팔리기도 해요.')]},
 gaetbae:{n:L('Gaetbae','갯배'),sub:L('Hand-pulled ferry · ₩500','손으로 끄는 배 · 500원'),q:'속초 갯배',f:[L('Crosses a channel of about 50 m between downtown Sokcho and Abai Village, in about 5 minutes.','속초 시내와 아바이마을 사이 50m 남짓한 물길을 약 5분에 건너요.'),L('No engine and no ferryman: passengers pull the wire with a hook.','엔진도 사공도 없어요. 탄 사람들이 갈고리로 줄을 당겨요.'),L('Adult ₩500, child ₩300, one way. Nov–Apr 05:30–22:30, May–Oct 05:00–23:00 (may change with the weather).','어른 500원, 어린이 300원(편도). 11~4월 05:30~22:30, 5~10월 05:00~23:00(날씨에 따라 바뀔 수 있어요).')]},
 abai:{n:L('Abai Village','아바이마을'),sub:L('Cheongho-dong, Sokcho','속초 청호동'),ll:[38.2069,128.5919],q:'속초 아바이마을',f:[L('Settled by people who fled Hamgyeong Province during the Korean War.','6·25 전쟁 때 함경도에서 내려온 실향민들이 모여 살며 생긴 마을이에요.'),L('Abai sundae and squid sundae are the village dishes.','아바이순대와 오징어순대가 이 마을 음식이에요.')]},
 sinheungsa:{n:L('Sinheungsa','신흥사'),sub:L('Seoraksan · first founded 652','설악산 · 652년 창건'),ll:[38.1743,128.487],q:'설악산 신흥사',f:[L('First founded in 652 by the monk Jajang. Entry is free.','652년 자장율사가 처음 세웠어요. 입장은 무료예요.'),L('A huge bronze seated Buddha, Tongil Daebul, sits at the temple.','큰 청동 좌불인 통일대불이 있어요.'),L('City buses 7 and 7-1 from Sokcho stop at the Sogongwon entrance.','속초에서 7번·7-1번 버스가 소공원 입구에 서요.')]},
 scable:{n:L('Seorak Cable Car','설악케이블카'),sub:L('Up to Gwongeumseong','권금성까지'),ll:[38.173,128.4891],q:'설악케이블카',f:[L('Adult round trip ₩16,000; about 5 minutes each way.','어른 왕복 16,000원, 편도 약 5분.'),L('Hours change with the season and the weather: check before you go.','운행 시간은 계절과 날씨에 따라 달라요. 가기 전에 확인하세요.')]},
 dongseoul:{n:L('Dong Seoul Bus Terminal','동서울종합터미널'),sub:L('Line 2 Gangbyeon Station','2호선 강변역'),ll:[37.535,127.0947],q:'동서울종합터미널',f:[L('Express buses from Sokcho: 15 a day (06:45–20:30), 2 h 26 min. Udeung (premium) ₩22,800, Premium ₩29,600.','속초발 고속버스: 하루 15회(06:45~20:30), 2시간 26분. 우등 22,800원, 프리미엄 29,600원.'),L('A rebuild is planned: a temporary boarding area in the Techno Mart building next door is proposed for the first half of 2027 (under review, Sept 2026).','재건축이 예정돼 있어요. 2027년 상반기에 옆 테크노마트 건물로 임시 승차장을 옮기는 계획이 협의 중이에요(2026년 9월 기준).')]},
};
"""

R['qz']="""const QZ={
 sst:[[/KTX-Eum to Gangneung|강릉행 KTX-이음/,'ek1',L('How much is a standard-class KTX-Eum ticket from Seoul to Gangneung?','서울 → 강릉 KTX-이음 일반실 요금은?'),['₩17,600','₩27,600','₩59,800'],1,L('₩27,600 in standard class.','일반실 27,600원이에요.')]],
 gns:[[/Jeongdongjin|정동진/,'ek2',L('About how long is the train from Gangneung to Jeongdongjin?','강릉에서 정동진까지 기차로 얼마나 걸리나요?'),[L('About 15 min','약 15분'),L('About 1 h','약 1시간'),L('About 2 h','약 2시간')],0,L('About 15 minutes.','약 15분이에요.')]],
 anm:[[/Gyeongpodae|경포대/,'ek3',L('How far is Gyeongpodae from Anmok Beach?','안목해변에서 경포대까지 얼마나 되나요?'),[L('About 1 km','약 1km'),L('About 7 km','약 7km'),L('About 30 km','약 30km')],1,L('About 7.1 km: around 10 minutes by car.','약 7.1km, 차로 10분쯤이에요.')]],
 gyp:[[/Ojukheon|오죽헌/,'ek4',L('What makes Chodang tofu special?','초당두부는 무엇이 특별한가요?'),[L('It is set with seawater','바닷물로 굳혀요'),L('It is made with rice','쌀로 만들어요'),L('It is fried twice','두 번 튀겨요')],0,L('It is set with clean East Sea seawater instead of the usual coagulant.','간수 대신 깨끗한 동해 바닷물로 굳혀요.')]],
 ojk:[[/Ticket office|매표소/,'ek5',L('Who is on the ₩5,000 note?','5,000원권 지폐의 인물은?'),[L('King Sejong','세종대왕'),L('Yi I (Yulgok)','율곡 이이'),L('Yi Hwang (Toegye)','퇴계 이황')],1,L('Yi I (Yulgok), born here at Ojukheon. His mother Shin Saimdang is on the ₩50,000 note.','여기 오죽헌에서 태어난 율곡 이이예요. 어머니 신사임당은 50,000원권에 있어요.')]],
 jdj:[[/Sokcho|속초/,'ek6',L('Why is it called Jeongdongjin?','왜 정동진이라고 부를까요?'),[L('It is due east of Gwanghwamun','광화문의 정동쪽이라서'),L('A king named it','임금이 지어서'),L('It is the newest station','가장 새 역이라서')],0,L('It lies due east (jeong-dong) of Gwanghwamun in Seoul.','서울 광화문의 정동쪽에 있어서 정동진이에요.')]],
 skc:[[/Seoraksan|설악산/,'ek7',L('How does the gaetbae move?','갯배는 어떻게 움직이나요?'),[L('With an engine','엔진으로'),L('Passengers pull a wire','승객이 줄을 당겨서'),L('With sails','돛으로')],1,L('No engine and no ferryman: passengers pull the wire with a hook.','엔진도 사공도 없이, 탄 사람들이 갈고리로 줄을 당겨요.')]],
 srk:[[/Cable Car|케이블카/,'ek8',L('How much is an adult round trip on the Seorak Cable Car?','설악케이블카 어른 왕복 요금은?'),['₩6,000','₩16,000','₩36,000'],1,L('₩16,000 round trip, about 5 minutes each way.','왕복 16,000원, 편도 약 5분이에요.')],
  [/Dong Seoul|동서울/,'ek9',L('About how long is the express bus from Sokcho to Dong Seoul?','속초 → 동서울 고속버스는 약 얼마나 걸리나요?'),[L('About 1 h','약 1시간'),L('About 2.5 h','약 2시간 반'),L('About 5 h','약 5시간')],1,L('2 h 26 min (udeung ₩22,800).','2시간 26분이에요(우등 22,800원).')]]};
"""

R['rem']="h(L('Remember','꼭 기억할 것'));[L('KTX-Eum Seoul → Gangneung ₩27,600 (standard) · fastest about 1 h 51 min','KTX-이음 서울 → 강릉 일반실 27,600원 · 가장 빠른 열차 약 1시간 51분'),L('City bus in Gangneung and Sokcho: card ₩1,530, cash ₩1,700','강릉·속초 시내버스: 교통카드 1,530원, 현금 1,700원'),L('Ojukheon ₩3,000 · 09:00–18:00 (last entry 17:00)','오죽헌 3,000원 · 09:00~18:00(입장 마감 17:00)'),L('Gangneung → Jeongdongjin train about 15 min (Nuriro ₩2,600)','강릉 → 정동진 기차 약 15분(누리로 2,600원)'),L('Gaetbae ₩500 one way · Nov–Apr 05:30–22:30','갯배 편도 500원 · 11~4월 05:30~22:30'),L('Seorak Cable Car ₩16,000 round trip · hours change with the season','설악케이블카 왕복 16,000원 · 운행 시간은 계절마다 달라요'),L('Express bus Sokcho → Dong Seoul 2 h 26 min, udeung ₩22,800','고속버스 속초 → 동서울 2시간 26분, 우등 22,800원'),"

R['areako']="const AREAKO={sst:'서울역',gns:'강릉역',citybus:'강릉역',anmok:'강릉 안목해변',gyeongpo:'강릉 경포대',chodang:'강릉 초당동',gpbeach:'강릉 경포해변',ojk:'강릉 오죽헌',yulgok:'강릉 오죽헌',jdj:'정동진',sandglass:'정동진',skbus:'강릉시외버스터미널',skmarket:'속초관광수산시장',gaetbae:'속초 아바이마을',abai:'속초 아바이마을',sinheungsa:'설악산 소공원',scable:'설악산 소공원',dongseoul:'동서울터미널'};"

R['foods']="""
  {k:'초당순두부',e:'Chodang sundubu',s:'Soft tofu',ic:'🥣',re:/순두부|두부|sundubu|tofu/i},
  {k:'닭강정',e:'dakgangjeong',s:'Sweet fried chicken',ic:'🍗',re:/닭강정|dakgangjeong/i},
  {k:'오징어순대',e:'squid sundae',s:'Squid sundae',ic:'🦑',re:/오징어순대|squid sundae/i},
  {k:'아바이순대',e:'abai sundae',s:'Abai sundae',ic:'🌭',re:/아바이순대|abai/i},
  {k:'물회',e:'mulhoe',s:'Cold raw fish soup',ic:'🐟',re:/물회|mulhoe/i},
  {k:'산채비빔밥',e:'sanchae bibimbap',s:'Wild greens bibimbap',ic:'🥗',re:/산채|sanchae/i},"""

R['phrase']="['강릉역 어디예요?','Gangneung-yeok eodi-yeyo?',L('Where is Gangneung Station?','강릉역 어디예요?')]"
R['stP']="$('stP').textContent=L('Leave Seoul Station by KTX-Eum. Drink coffee by the sea at Anmok, walk Gyeongpodae and Gyeongpo Beach, and visit Ojukheon, where Yulgok was born. Take the train to Jeongdongjin, the station by the sea, then the bus to Sokcho for dakgangjeong and the hand-pulled gaetbae ferry. On the last day ride the cable car up Seoraksan and take the express bus back to Seoul. Real fares, times and photos.','서울역에서 KTX-이음으로 출발해요. 안목 커피거리에서 바다를 보며 커피를 마시고, 경포대와 경포해변을 걷고, 율곡 이이가 태어난 오죽헌에 가요. 기차로 바닷가 정동진역에 가서 큰 모래시계를 보고, 버스로 속초에 가서 닭강정을 먹고 줄을 당겨 가는 갯배를 타요. 마지막 날엔 케이블카로 설악산에 오른 뒤 고속버스로 서울에 돌아와요. 실제 요금·시간·사진을 담았어요.');"
R['stR']="$('stR').textContent=L('Seoul Station · KTX-Eum · Gangneung · Anmok · Gyeongpodae · Ojukheon · Jeongdongjin · Sokcho market · Gaetbae · Abai Village · Sinheungsa · Seorak Cable Car · Dong Seoul','서울역 · KTX-이음 · 강릉역 · 안목 · 경포대 · 오죽헌 · 정동진 · 속초 시장 · 갯배 · 아바이마을 · 신흥사 · 설악케이블카 · 동서울');"
R['rgn']="const RGN={ktx:'KTX-이음  강릉 GANGNEUNG',sst0:L('Seoul Station. KTX-Eum trains to Gangneung leave from here. Buy tickets on the Korail Talk app, at a ticket window or a ticket machine.','서울역이에요. 강릉 가는 KTX-이음이 여기서 떠나요. 표는 코레일톡 앱, 매표창구, 자동발매기에서 사요.'),sst8:L('KTX-Eum Seoul → Gangneung: ₩27,600 in standard class. The fastest train takes about 1 h 51 min.','KTX-이음 서울 → 강릉: 일반실 27,600원. 가장 빠른 열차는 약 1시간 51분.'),term:'동서울종합터미널 · DONG SEOUL BUS TERMINAL',line:'2 강변역 · GANGBYEON',lineCol:'#2fae6a',termNotes:[[0,L('Dong Seoul Bus Terminal. Welcome back to Seoul!','동서울종합터미널이에요. 서울에 돌아왔어요!')],[.5,L('Gangbyeon Station on Line 2 (green) is right next door.','바로 옆이 2호선(초록) 강변역이에요.')]]};"
r=Region(S);r.build(R);r.save('east.html')
