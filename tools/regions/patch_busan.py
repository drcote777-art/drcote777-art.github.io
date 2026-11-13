# 가상 부산·경남 2박 3일 (busan.html)
# 서울 페이지 생성기(patch_seoul.py)를 그대로 돌려 엔진 기능을 모두 받은 뒤, 서울 자료를 부산·경남 자료로 바꿉니다.
# 사실 출처(2026-11 확인): KTX 59,800원·최단 2시간 18분(아시아경제 2025-10-21) · 부산 지하철 1구간 1,600/2구간 1,800원(경향신문 2024-05-02)
#  자갈치 05:00~22:00, 첫째·셋째·다섯째 화 휴무 / 국제시장 1945년~, 09:00~20:00 / 부산타워 120m 12,000원 10:00~22:00 / 해동용궁사 1376, 04:30~20:30 무료 (한국관광공사 자료)
#  BIFF광장 1996-09-13, 428m (한국관광공사) / 감천 토성역 6번 출구 마을버스, 스탬프 지도 2,000원 (두리맵 2026-10)
#  블루라인파크 요금·시간 (트래블로그 2026-10) / 드론쇼 토 19:00·21:00(10~2월) (부산시) / 용궁사 108계단·181번·139번, 동피랑 2007 (부산나비)
#  노포→통영 우등 23,200원 2시간 17분, 통영→서울남부 우등 41,000원 4시간 29분, 서울→부산서부 우등 44,100원 4시간 31분 (asamaru 2026-11)
#  통영케이블카 1,975m 약 10분 왕복 17,000원 둘째·넷째 수 휴무 (다음 2026-06-15)
import re,json,os
S=os.environ.get('GEN_DIR','/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/')
src=open(S+'patch_seoul.py',encoding='utf8').read()
END="open(S+'seoul.html','w',encoding='utf8').write(s);print('ok',len(s))"
assert src.count(END)==1
ns={};exec(compile(src.replace(END,''),'patch_seoul.py','exec'),ns);s=ns['s']
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,('COUNT',c,a[:90]);s=s.replace(a,b)
def cut(a,b,new):
    global s
    i=s.index(a);j=s.index(b,i);s=s[:i]+new+s[j:]
def sub1(pat,new):
    global s
    m=re.search(pat,s);assert m,pat[:60];s=s[:m.start()]+new+s[m.end():]

# ---- 이름 · 저장 칸 · 시작 돈 ----
rep("<title>Virtual Seoul · 가상 서울 3일</title>","<title>Virtual Busan · 가상 부산·경남 3일</title>")
rep('<link rel="manifest" href="seoul.webmanifest">','')
for k in ['seoul_game1','seoul_stamps','seoul_wallet']:
    s=s.replace("'"+k+"'","'"+k.replace('seoul_','busan_')+"'")
rep("const G0={eur:300000,","const G0={eur:400000,")
rep("const REG_ID='seoul';","const REG_ID='busan';")

# ---- 스탬프 · 장면 · 🚇 이동 메뉴 ----
cut("const STAMPS=[","const LS=",r"""const STAMPS=[{id:'nmp',name:L('Nampo','남포'),date:'D1',c:'#e83a5a'},{id:'gmc',name:L('Gamcheon','감천'),date:'D1',c:'#f0c419'},{id:'hud',name:L('Haeundae','해운대'),date:'D2',c:'#2e8fd0'},{id:'ygs',name:L('Yonggungsa','용궁사'),date:'D2',c:'#d8a05a'},{id:'gal',name:L('Gwangalli','광안리'),date:'D2',c:'#9f7fff'},{id:'tyg',name:L('Tongyeong','통영'),date:'D3',c:'#2fae6a'}];
""")
cut("const SCN={","/* 날짜별 할 일",r"""const SCN={
 sst:{b:'seoul',o:{city:'sst'},name:L('Seoul Station · KTX','서울역 · KTX')},bsn:{b:'seoul',o:{city:'bsn'},name:L('Busan Station','부산역')},
 nmp:{b:'seoul',o:{city:'nmp'},name:L('Nampo-dong · Jagalchi · Busan Tower','남포동 · 자갈치 · 부산타워')},gmc:{b:'seoul',o:{city:'gmc'},name:L('Gamcheon Culture Village','감천문화마을')},
 hud:{b:'seoul',o:{city:'hud'},name:L('Haeundae · Blueline Park','해운대 · 블루라인파크')},ygs:{b:'seoul',o:{city:'ygs'},name:L('Haedong Yonggungsa','해동용궁사')},
 gal:{b:'seoul',o:{city:'gal'},name:L('Gwangalli · Gwangan Bridge','광안리 · 광안대교')},tyg:{b:'seoul',o:{city:'tyg'},name:L('Tongyeong · Dongpirang · Cable Car','통영 · 동피랑 · 케이블카')},
 nbu:{b:'seoul',o:{city:'nbu'},name:L('Seoul Nambu Terminal','서울남부터미널')},hotel:{b:'hotel',name:L('Hotel room · Nampo-dong','남포동 호텔 방')},ride:{b:'ride',name:''}};
const SHIPMAP=[['sst',L('Seoul Station','서울역'),'KTX'],['bsn',L('Busan Station','부산역'),'KTX'],['nmp',L('Nampo · Jagalchi','남포 · 자갈치'),L('Line 1','1호선')],['gmc',L('Gamcheon','감천'),L('Village bus','마을버스')],['hud',L('Haeundae','해운대'),L('Line 2','2호선')],['ygs',L('Yonggungsa','용궁사'),L('Bus 139 / 181','139·181번 버스')],['gal',L('Gwangalli','광안리'),L('Line 2','2호선')],['tyg',L('Tongyeong','통영'),L('Express bus','고속버스')],['nbu',L('Seoul Nambu','서울남부'),L('Express bus','고속버스')],['hotel',L('Hotel','호텔'),L('Sleep','잠자기')]];

""")

# ---- 2박 3일 일정 ----
cut("const DAYS=[","/* 메뉴 (게임 속 가상 가격) */",r"""const DAYS=[
 {tag:'DAY 1',title:L('Seoul → Busan · Old town','서울 출발 · 부산 원도심'),time:L('Seoul Station KTX (about 2 h 18 min+) → Busan Station → Nampo: Jagalchi · BIFF · Gukje Market · Busan Tower → Gamcheon','서울역 KTX(약 2시간 18분~) → 부산역 → 남포: 자갈치 · BIFF · 국제시장 · 부산타워 → 감천문화마을'),q:[
  {t:'',n:L('Find your train on the departure board','전광판에서 열차 확인'),sc:'sst',at:.45,near:1,r:'sst'},
  {t:'',n:L('Board the KTX to Busan (₩59,800)','부산행 KTX 타기 (59,800원)'),sc:'sst',at:.82,a:'ktx',r:'ktx'},
  {t:'',n:L('Line 1 to Nampo','1호선으로 남포'),sc:'bsn',at:.9,a:'m_nmp',r:'bmetro'},
  {t:'',n:L('Jagalchi Market','자갈치시장'),sc:'nmp',at:.17,near:1,r:'jagalchi'},
  {t:'',n:L('Seafood at a Jagalchi stall','자갈치에서 해산물 먹기'),sc:'nmp',at:.22,a:'eat_jg'},
  {t:'',n:L('Ssiat hotteok at BIFF Square','BIFF광장 씨앗호떡'),sc:'nmp',at:.47,a:'eat_ht',r:'biff'},
  {t:'',n:L('Gukje Market','국제시장'),sc:'nmp',at:.6,near:1,r:'gukje'},
  {t:'',n:L('Busan Tower observatory','부산타워 전망대'),sc:'nmp',at:.85,a:'btower',r:'btower'},
  {t:'',n:L('Nampo stamp','남포 스탬프'),sc:'nmp',at:.99,a:'stamp'},
  {t:'',n:L('Line 1 + village bus to Gamcheon','1호선 + 마을버스로 감천'),sc:'nmp',at:.02,a:'m_gmc'},
  {t:'',n:L('Buy the stamp map','스탬프 지도 사기'),sc:'gmc',at:.14,a:'buy_map',r:'gamcheon'},
  {t:'',n:L('Painted lanes and the harbour view','알록달록 골목과 항구 전망'),sc:'gmc',at:.45,near:1},
  {t:'',n:L('Gamcheon stamp','감천 스탬프'),sc:'gmc',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 2',title:L('Haeundae · Sea temple · Gwangalli','해운대 · 바다 절 · 광안리'),time:L('Haeundae → Blueline Park Beach Train → Haedong Yonggungsa → Gwangalli night & drone show (Sat)','해운대 → 블루라인파크 해변열차 → 해동용궁사 → 광안리 야경·드론쇼(토)'),q:[
  {t:'',n:L('Subway to Haeundae (Line 1 → Line 2)','지하철로 해운대 (1호선 → 2호선)'),sc:'nmp',at:.05,a:'m_hud',r:'bmetro'},
  {t:'',n:L('Haeundae Beach','해운대해수욕장'),sc:'hud',at:.3,near:1,r:'haeundae'},
  {t:'',n:L('Dwaeji-gukbap lunch','점심: 돼지국밥'),sc:'hud',at:.5,a:'eat_gb'},
  {t:'',n:L('Beach Train Mipo → Songjeong','해변열차 미포 → 송정'),sc:'hud',at:.96,a:'btrain',r:'blueline'},
  {t:'',n:L('Haedong Yonggungsa','해동용궁사'),sc:'ygs',at:.6,near:1,r:'yonggung'},
  {t:'',n:L('Haeundae stamp','해운대 스탬프'),sc:'hud',at:.97,a:'stamp'},
  {t:'',n:L('Yonggungsa stamp','용궁사 스탬프'),sc:'ygs',at:.97,a:'stamp'},
  {t:'',n:L('Bus 181 + Line 2 to Gwangalli','181번 버스 + 2호선으로 광안리'),sc:'ygs',at:.03,a:'m_gal'},
  {t:'',n:L('Gwangan Bridge at night','광안대교 야경'),sc:'gal',at:.35,near:1,r:'gwangan'},
  {t:L('Sat','토'),n:L('Drone light show','드론 라이트쇼'),sc:'gal',at:.6,a:'drone',r:'drone'},
  {t:'',n:L('Gwangalli stamp','광안리 스탬프'),sc:'gal',at:.97,a:'stamp'},
  {t:'',n:L('Sleep at the hotel','호텔에서 자기'),sc:'hotel',at:0,a:'sleep'}]},
 {tag:'DAY 3',title:L('Tongyeong · back to Seoul','통영 · 서울로'),time:L('Express bus to Tongyeong (2 h 17 min) → Jungang Market → Dongpirang → Cable Car → express bus to Seoul Nambu (4 h 29 min)','고속버스로 통영(2시간 17분) → 중앙시장 → 동피랑 → 케이블카 → 고속버스로 서울남부(4시간 29분)'),q:[
  {t:'',n:L('Express bus to Tongyeong (₩23,200)','통영 가는 고속버스 (23,200원)'),sc:'nmp',at:.08,a:'bus_ty',r:'tybus'},
  {t:'',n:L('Chungmu gimbap at Jungang Market','중앙시장 충무김밥'),sc:'tyg',at:.12,a:'eat_cm',r:'tyjungang'},
  {t:'',n:L('Dongpirang mural lanes','동피랑 벽화 골목'),sc:'tyg',at:.42,near:1,r:'dongpirang'},
  {t:'',n:L('Tongyeong Cable Car to Mireuksan','통영케이블카로 미륵산'),sc:'tyg',at:.77,a:'tcable',r:'cablecar'},
  {t:'',n:L('Tongyeong stamp','통영 스탬프'),sc:'tyg',at:.99,a:'stamp'},
  {t:'',n:L('Express bus to Seoul Nambu (₩41,000)','서울남부 가는 고속버스 (41,000원)'),sc:'tyg',at:.7,a:'bus_sel',r:'nambu'},
  {t:'',n:L('Finish the trip','여행 마치기'),sc:'nbu',at:.85,a:'trip'}]}];

""")

# ---- 장소별 사람 · 가게 · 탈것 ----
cut("const mt=(id,t,side","const CRUISE_INFO=",r"""const mt=(id,t,side,n,line,col,stops,dest,intro,fare)=>({t,side,k:'metro',id,n,fare:fare||1600,ride:{kind:'metro',scen:'tunnel',title:line,col,stops,dest,intro}});
const st=(id,t,side,n,w,items,ic)=>({t,side,k:'gelato',id,n,w,ic,menu:{title:n,sub:L('Example menu · virtual prices','예시 메뉴 · 가상 가격'),items}});
const CITY={
 sst:{noBoard:1,spots:[{t:.82,side:1,k:'shuttle',id:'ktx',n:L('KTX to Busan','부산행 KTX'),fare:59800,ride:{kind:'train',scen:'country',title:L('KTX Seoul → Busan','KTX 서울 → 부산'),col:'#1f4f91',stops:[L('Seoul','서울'),L('Daejeon','대전'),L('Dongdaegu','동대구'),L('Busan','부산')],gap:900,vmax:55,intro:L('🚆 KTX to Busan, standard class ₩59,800. The fastest trains take about 2 h 18 min. (Stops differ by train.)','🚆 부산행 KTX, 일반실 59,800원. 가장 빠른 열차는 약 2시간 18분이에요. (정차역은 열차마다 달라요.)'),dest:{sc:'bsn',at:0}}},
   st('eat_sst',.3,-1,L('Station kiosk','역 매점'),L('Clerk','직원'),[[L('Gimbap roll','김밥 한 줄'),4000],[L('Bottled water','생수'),1200],[L('Coffee','커피'),4500]],'🥤')],
  sights:[{t:.14,side:1,id:'sst'},{t:.75,side:-1,id:'ktx'}],
  shows:[{id:'busopt',t:.2,b:L('🚌 Or go by express bus?','🚌 고속버스로 가면?'),s:L('Seoul Express Bus Terminal → Busan Seobu','서울고속버스터미널 → 부산서부'),say:L('Express buses from Seoul Express Bus Terminal to Busan Seobu (Sasang) take about 4 h 31 min, premium ₩44,100. This trip goes by KTX.','서울고속버스터미널에서 부산서부(사상)까지 고속버스는 약 4시간 31분, 우등 44,100원이에요. 이번 여행은 KTX로 가요.')}],
  cit:[{t:.5,n:L('Jihun','지훈'),role:L('Korail station staff','코레일 역무원'),p:'서울역 역무원. KTX 표 사는 곳(코레일톡 앱·매표창구·자동발매기), 전광판 보는 법, 호차와 좌석 찾기를 안내한다. 부산까지 일반실 59,800원, 가장 빠른 열차 약 2시간 18분.'}]},
 bsn:{noBoard:1,spots:[mt('m_nmp',.9,1,L('Busan Station → Nampo','부산역 → 남포'),L('Line 1','1호선'),'#f06a00',[L('Busan Station','부산역'),L('Jungang','중앙'),L('Nampo','남포')],{sc:'nmp',at:0},L('🚇 Line 1 (orange), 2 stops to Nampo. Card fare ₩1,600.','🚇 1호선(주황) 남포까지 2정거장. 교통카드 1,600원.')),
   st('eat_bsn',.62,-1,L('Eomuk shop','어묵 가게'),L('Owner','사장님'),[[L('Fish cake skewer','어묵 꼬치'),1500],[L('Fish cake croquette','어묵 고로케'),3000]],'🍢')],
  sights:[{t:.4,side:1,id:'bsn'},{t:.82,side:-1,id:'bmetro'}],
  cit:[{t:.6,n:L('Soyeon','소연'),role:L('Busan local','부산 시민'),p:'부산역 앞에서 만난 친절한 부산 시민. 부산 지하철 1호선, 티머니 사용, 남포동 가는 길을 알려 준다.'}]},
 nmp:{noBoard:1,spots:[mt('m_gmc',.02,-1,L('To Gamcheon: Line 1 + village bus','감천 가기: 1호선 + 마을버스'),L('Line 1 → village bus','1호선 → 마을버스'),'#f06a00',[L('Nampo','남포'),L('Jagalchi','자갈치'),L('Toseong','토성'),L('Gamcheon Village','감천문화마을')],{sc:'gmc',at:0},L('🚇 Line 1 two stops to Toseong, then from exit 6 the village bus (Saha 1-1, Seogu 2 or 2-2), about 10 min.','🚇 1호선 토성까지 2정거장, 6번 출구에서 마을버스(사하1-1·서구2·서구2-2)로 약 10분.')),
   mt('m_hud',.05,-1,L('Nampo → Haeundae','남포 → 해운대'),L('Line 1 → Line 2 (Seomyeon)','1호선 → 2호선 (서면 환승)'),'#2fae6a',[L('Nampo','남포'),L('Seomyeon (transfer)','서면 (환승)'),L('Haeundae','해운대')],{sc:'hud',at:0},L('🚇 Line 1 (orange) to Seomyeon, change to Line 2 (green) for Haeundae. Longer trips are zone 2: ₩1,800 by card.','🚇 1호선(주황)으로 서면, 2호선(초록)으로 갈아타 해운대역. 먼 거리는 2구간: 교통카드 1,800원.'),1800),
   {t:.08,side:1,k:'bus',id:'bus_ty',n:L('Express bus to Tongyeong','통영 가는 고속버스'),fare:23200,ride:{kind:'bus',scen:'country',title:L('Express bus Busan → Tongyeong','고속버스 부산 → 통영'),col:'#2e5a86',stops:[L('Busan Central Bus Terminal (Nopo)','부산종합버스터미널(노포)'),L('Tongyeong Bus Terminal','통영종합버스터미널')],gap:1100,vmax:30,intro:L('🚌 Line 1 to Nopo, the last stop, for Busan Central Bus Terminal. Express bus to Tongyeong: about 2 h 17 min, premium ₩23,200.','🚌 1호선 종점 노포역의 부산종합버스터미널에서 통영행 고속버스: 약 2시간 17분, 우등 23,200원.'),dest:{sc:'tyg',at:0}}},
   st('eat_jg',.22,1,L('Jagalchi seafood stall','자갈치 횟집'),L('Auntie Mija','미자 이모'),[[L('Grilled hagfish (kkomjangeo)','꼼장어 구이'),25000],[L('Raw fish platter (small)','모둠회 (소)'),40000],[L('Fish cake skewer','어묵 꼬치'),1500]],'🐟'),
   st('eat_ht',.47,-1,L('Ssiat hotteok cart','씨앗호떡 노점'),L('Mr. Jung','정 사장님'),[[L('Ssiat hotteok (seed-filled pancake)','씨앗호떡'),2500],[L('Fish cake','어묵'),1500]],'🥞'),
   {t:.62,side:1,k:'stall',id:'buy_gk',n:L('Gukje Market shop','국제시장 가게'),w:L('Owner','주인'),items:[[L('Socks set','양말 세트'),5000],[L('Busan fridge magnet','부산 자석'),4000],[L('Camera strap','카메라 끈'),8000]]}],
  sights:[{t:.17,side:-1,id:'jagalchi'},{t:.44,side:1,id:'biff'},{t:.6,side:-1,id:'gukje'},{t:.83,side:1,id:'btower'}],
  doors:[{t:.11,side:1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  lifts:[{id:'btower',y:64,n:L('Busan Tower observatory','부산타워 전망대'),fare:12000,msg:L('Up the tower to the observatory…','타워 전망대로 올라가요…'),top:L('The whole harbour below: Jagalchi, the bridges and ships coming in.','항구가 발아래 펼쳐져요. 자갈치와 다리들, 들어오는 배들.')}],
  cit:[{t:.24,n:L('Auntie Mija','미자 아지매'),role:L('Jagalchi fish seller','자갈치 생선 상인'),p:'자갈치시장에서 오래 장사한 아지매. 정 많은 부산 사투리로 말한다. 시장은 05:00~22:00쯤, 매월 첫째·셋째·다섯째 화요일 휴무라고 안다.'},{t:.66,n:L('Sungmin','성민'),role:L('Busan university student','부산 대학생'),p:'남포동을 잘 아는 부산 대학생. 국제시장, BIFF광장 씨앗호떡, 용두산공원 에스컬레이터와 부산타워 가는 길을 안내한다.'}]},
 gmc:{noBoard:1,spots:[st('buy_map',.14,1,L('Information centre','안내센터'),L('Staff','직원'),[[L('Stamp map','스탬프 지도'),2000]],'🗺'),
   st('eat_gm',.6,-1,L('Rooftop café','전망 카페'),L('Barista','바리스타'),[[L('Iced Americano','아이스 아메리카노'),4500],[L('Lemonade','레모네이드'),5500]],'☕')],
  sights:[{t:.45,side:-1,id:'gamcheon'}],doors:[{t:.97,side:1,to:'hotel',n:L('Back to the hotel','호텔로'),lab:'HOTEL'}],
  cit:[{t:.35,n:L('Grandpa Bok','복 할아버지'),role:L('Gamcheon resident','감천 주민'),p:'감천마을에 오래 산 할아버지. 6·25 피난민이 살던 마을 이야기를 하고, 주민이 사는 곳이니 조용히 다녀 달라고 부드럽게 부탁한다.'}]},
 hud:{noBoard:1,spots:[st('eat_gb',.5,-1,L('Dwaeji-gukbap restaurant','돼지국밥집'),L('Owner','사장님'),[[L('Dwaeji-gukbap (pork and rice soup)','돼지국밥'),10000],[L('Sundae-gukbap','순대국밥'),10000]],'🍲'),
   {t:.96,side:1,k:'shuttle',id:'btrain',n:L('Beach Train · Mipo → Songjeong','해변열차 · 미포 → 송정'),fare:10000,ride:{kind:'train',scen:'port',title:L('Haeundae Beach Train','해운대 해변열차'),col:'#e83a5a',stops:[L('Mipo','미포'),L('Cheongsapo','청사포'),L('Songjeong','송정')],gap:500,vmax:8,intro:L('🚃 Beach Train from Mipo to Songjeong, about 25 min along the sea. From Songjeong, city bus 139 goes to Haedong Yonggungsa.','🚃 미포에서 송정까지 바닷가를 따라 약 25분. 송정에서 139번 시내버스로 해동용궁사에 가요.'),dest:{sc:'ygs',at:0}}}],
  sights:[{t:.3,side:1,id:'haeundae'},{t:.9,side:-1,id:'blueline'}],
  shows:[{id:'capsule',t:.9,b:L('🚡 Look at the Sky Capsules','🚡 스카이캡슐 구경'),s:L('2 people ₩50,000 one way','2인 편도 50,000원'),say:L('Little colourful capsules glide along a rail above the sea from Mipo to Cheongsapo. One way: ₩50,000 for two, ₩55,000 for three, ₩60,000 for four.','알록달록 작은 캡슐이 바다 위 레일을 따라 미포에서 청사포까지 가요. 편도 2인 50,000원, 3인 55,000원, 4인 60,000원.')}],
  cit:[{t:.4,n:L('Minjae','민재'),role:L('Haeundae local surfer','해운대 서퍼'),p:'해운대에 사는 서퍼. 해변, 블루라인파크 해변열차(미포~송정 약 25분)와 스카이캡슐, 돼지국밥 이야기를 한다.'}]},
 ygs:{noBoard:1,spots:[{t:.03,side:1,k:'bus',id:'m_gal',n:L('To Gwangalli (bus 181 + Line 2)','광안리로 (181번 + 2호선)'),fare:1600,ride:{kind:'bus',scen:'city',title:L('Bus 181 → Line 2','181번 버스 → 2호선'),col:'#2fae6a',stops:[L('Yonggungsa','용궁사'),L('Haeundae Station','해운대역'),L('Gwangan Station','광안역')],gap:700,vmax:14,intro:L('🚌 Bus 181 back to Haeundae Station, then Line 2 (green) to Gwangan, and walk to the beach.','🚌 181번 버스로 해운대역, 2호선(초록)으로 광안역에 내려 해변까지 걸어가요.'),dest:{sc:'gal',at:0}}}],
  sights:[{t:.55,side:-1,id:'yonggung'}],
  cit:[{t:.66,n:L('Mrs. Hyeon','현 보살님'),role:L('Temple volunteer','절 안내 봉사자'),p:'해동용궁사 안내를 돕는 봉사자. 1376년 나옹대사 창건, 108계단, 해수관음대불, 기도하는 분들을 위해 조용히 다니기를 부드럽게 안내한다. 관람은 04:30~20:30, 무료.'}]},
 gal:{noBoard:1,spots:[st('eat_gl',.4,-1,L('Seaside pocha','바닷가 포차'),L('Owner','사장님'),[[L('Grilled clams','조개구이'),35000],[L('Fish cake soup','어묵탕'),15000]],'🦪')],
  sights:[{t:.3,side:1,id:'gwangan'},{t:.62,side:1,id:'drone'}],doors:[{t:.97,side:-1,to:'hotel',n:L('Hotel','호텔'),lab:'HOTEL'}],
  shows:[{id:'drone',t:.6,b:L('✨ Drone light show','✨ 드론 라이트쇼'),s:L('Sat 19:00 · 21:00 (Oct–Feb)','토 19:00 · 21:00 (10~2월)'),fx:droneShow,say:L('Hundreds of drones draw pictures in the sky over the bay. Real shows: every Saturday, 19:00 and 21:00 (Oct–Feb), 20:00 and 22:00 (Mar–Sep). Free.','수많은 드론이 바다 위 하늘에 그림을 그려요. 실제 공연: 매주 토요일, 10~2월 19:00·21:00, 3~9월 20:00·22:00. 무료예요.')}],
  cit:[{t:.52,n:L('Jisu','지수'),role:L('Here for the drone show','드론쇼 보러 온 시민'),p:'광안리에 드론쇼를 보러 온 부산 시민. 토요일 공연 시간(10~2월 19:00·21:00, 3~9월 20:00·22:00)과 광안대교 야경을 이야기한다.'}]},
 tyg:{noBoard:1,spots:[st('eat_cm',.12,-1,L('Chungmu gimbap shop','충무김밥집'),L('Halmeoni','할머니'),[[L('Chungmu gimbap (1 serving)','충무김밥 1인분'),6000],[L('Kkulppang (honey bread)','꿀빵'),2000]],'🍙'),
   {t:.7,side:1,k:'bus',id:'bus_sel',n:L('Express bus to Seoul Nambu Terminal','서울남부터미널 가는 고속버스'),fare:41000,ride:{kind:'bus',scen:'country',title:L('Express bus Tongyeong → Seoul Nambu','고속버스 통영 → 서울남부'),col:'#2e5a86',stops:[L('Tongyeong Bus Terminal','통영종합버스터미널'),L('Seoul Nambu Terminal','서울남부터미널')],gap:1400,vmax:30,intro:L('🚌 Take a city bus or taxi to Tongyeong Bus Terminal. Premium express bus to Seoul Nambu: about 4 h 29 min, ₩41,000.','🚌 통영종합버스터미널까지는 시내버스나 택시로 가요. 우등 고속버스로 서울남부까지 약 4시간 29분, 41,000원.'),dest:{sc:'nbu',at:0}}}],
  sights:[{t:.1,side:-1,id:'tyjungang'},{t:.42,side:1,id:'dongpirang'},{t:.76,side:-1,id:'cablecar'}],
  lifts:[{id:'tcable',y:60,ic:'🚡',down:L('🚡 Cable car down','🚡 케이블카로 내려가기'),n:L('Tongyeong Cable Car','통영케이블카'),fare:17000,msg:L('The cable car climbs Mireuksan: 1,975 m, about 10 minutes…','케이블카가 미륵산으로 올라가요. 1,975m, 약 10분…'),top:L('Islands scattered across the sea: the Hallyeosudo waterway. The summit is about a 20-minute round-trip walk.','바다에 섬들이 흩어져 있어요. 한려수도예요. 정상까지 왕복 20분쯤 걸어요.')}],
  cit:[{t:.3,n:L('Hyeonu','현우'),role:L('Tongyeong fisherman','통영 어부'),p:'통영 강구안에서 배를 타는 어부. 충무김밥과 꿀빵, 동피랑 벽화마을(2007년 시작), 통영케이블카(왕복 17,000원, 둘째·넷째 수요일 휴무) 이야기를 한다.'}]},
 nbu:{noBoard:1,spots:[],sights:[{t:.45,side:1,id:'nambu'}],cit:[{t:.55,n:L('Ms. Han','한 선생님'),role:L('Terminal information desk','터미널 안내원'),p:'서울남부터미널 안내원. 바로 옆 3호선 남부터미널역 가는 길과 서울 시내로 가는 방법을 안내한다.'}],fin:{t:.85,s:L('3 days in Busan · Gyeongnam','부산·경남 2박 3일')}}};

""")
cut("const CRUISE_INFO=","const NPC_RULES=",r"""const CRUISE_INFO="이 게임은 여행자가 서울역에서 KTX를 타고 부산에 가서 2박 3일 동안 부산과 경남 통영을 도는 가상 3D 여행이다. 1일: 서울역 KTX(일반실 59,800원, 가장 빠른 열차 약 2시간 18분, 느린 열차 약 2시간 56분) → 부산역 → 부산 지하철 1호선(주황, 교통카드 1구간 1,600원·2구간 1,800원, 서울 티머니 사용 가능) 남포 → 자갈치시장(05:00~22:00, 매월 첫째·셋째·다섯째 화요일 휴무) → BIFF광장(1996년 9월 13일 첫 부산국제영화제를 앞두고 이름 붙음, 영화인 손도장, 길이 428m) → 국제시장(1945년 광복 뒤 장터로 시작, 보통 09:00~20:00, 12개 동) → 용두산공원 에스컬레이터 → 부산타워(높이 120m, 성인 12,000원, 10:00~22:00, 입장 마감 21:30) → 감천문화마을(1호선 토성역 6번 출구에서 마을버스 사하1-1·서구2·서구2-2로 약 10분, 입장 무료, 가게 09:00~18:00쯤, 안내센터 스탬프 지도 2,000원, 6·25 피난민 터전이 도시재생으로 바뀜) → 남포동 호텔. 2일: 1호선→서면 환승→2호선 해운대역 → 해운대해수욕장 → 해운대 블루라인파크 해변열차(옛 동해남부선 4.8km, 미포~송정 약 25분, 미포·송정 출발 1회 10,000원, 청사포 출발 8,000원, 2회권 14,000원, 모든역 16,000원, 11~2월 09:00~19:00; 스카이캡슐 편도 2인 50,000원·3인 55,000원·4인 60,000원) → 송정에서 139번 버스 → 해동용궁사(1376년 나옹대사 창건, 04:30~20:30, 무료, 108계단, 10m 해수관음대불, 해운대역에서 181번 버스로 약 30~40분) → 181번 버스·2호선 광안역 → 광안리 해변·광안대교 야경 → 광안리 M 드론라이트쇼(2022년 4월부터 상설, 매주 토요일, 10~2월 19:00·21:00, 3~9월 20:00·22:00, 무료). 3일: 1호선 노포역 부산종합버스터미널 → 통영 고속버스(하루 13회 07:10~21:00, 약 2시간 17분, 우등 23,200원) → 통영 강구안 중앙시장(충무김밥·꿀빵) → 동피랑 벽화마을(중앙시장 뒤 언덕, 2007년 벽화 사업 시작, 무료) → 통영케이블카(미륵산, 1,975m, 약 10분, 성인 왕복 17,000원, 매월 둘째·넷째 수요일 휴무, 상부역에서 정상까지 왕복 약 20분) → 통영종합버스터미널 → 서울남부터미널(하루 11회, 약 4시간 29분, 우등 41,000원). 서울고속버스터미널→부산서부(사상) 고속버스는 우등 44,100원, 약 4시간 31분. 게임 속 식사·가게 가격은 예시다.";
""")

# ---- 실제 정보 · 사진 ----
REAL=r"""const REAL={
 sst:{n:L('Seoul Station','서울역'),sub:L('KTX · Gyeongbu Line','KTX · 경부선'),ll:[37.5555,126.9707],q:'Seoul Station',f:[L('KTX trains to Busan leave from here. Tickets: Korail Talk app, ticket windows or machines.','부산행 KTX가 여기서 떠나요. 표: 코레일톡 앱, 매표창구, 자동발매기.'),L('The domed red-brick old station (1925) is now Culture Station Seoul 284.','붉은 벽돌 돔의 옛 서울역(1925)은 지금 문화역서울284예요.')]},
 ktx:{n:'KTX',sub:L('Seoul → Busan','서울 → 부산'),q:'KTX Seoul Station',f:[L('Standard class Seoul → Busan: ₩59,800 for every KTX, whatever the number of stops.','서울 → 부산 일반실 59,800원. 정차역 수와 상관없이 같아요.'),L('The fastest train takes about 2 h 18 min; the slowest about 2 h 56 min.','가장 빠른 열차 약 2시간 18분, 가장 느린 열차 약 2시간 56분.')]},
 bsn:{n:L('Busan Station','부산역'),sub:L('KTX · Line 1','KTX · 1호선'),ll:[35.1153,129.0425],q:'Busan Station',f:[L('Busan subway Line 1 (orange) runs right under the station.','역 아래로 부산 지하철 1호선(주황)이 다녀요.'),L('Nampo-dong is 2 stops away: Jungang, then Nampo.','남포동은 2정거장이에요: 중앙, 다음 남포.')]},
 bmetro:{n:L('Busan Metro','부산 지하철'),sub:L('Card fares','교통카드 요금'),q:'Busan Metro',f:[L('Card fare ₩1,600 for zone 1 and ₩1,800 for zone 2 (since 3 May 2024).','교통카드 1구간 1,600원, 2구간 1,800원(2024년 5월 3일부터).'),L('T-money cards from Seoul work in Busan too.','서울에서 쓰던 티머니 카드를 부산에서도 써요.')]},
 jagalchi:{n:L('Jagalchi Market','자갈치시장'),sub:L('Fish market by the harbour','항구 앞 수산시장'),ll:[35.0967,129.0300],q:'Jagalchi Market',f:[L('About 05:00–22:00. Closed on the 1st, 3rd and 5th Tuesday of the month.','05:00~22:00쯤. 매월 첫째·셋째·다섯째 화요일 휴무.'),L('An outdoor traditional market and a modern indoor market building.','바깥의 전통시장과 깔끔한 실내 현대시장으로 나뉘어요.')]},
 biff:{n:L('BIFF Square','BIFF광장'),sub:L('Film street · 428 m','영화의 거리 · 428m'),ll:[35.0987,129.0280],q:'BIFF Square Busan',f:[L('Named on 13 September 1996, ahead of the first Busan International Film Festival.','1996년 9월 13일 첫 부산국제영화제를 앞두고 이름 붙었어요.'),L('Film stars leave their handprints here during the festival.','영화제 때 영화인들이 이곳에 손도장을 남겨요.')]},
 gukje:{n:L('Gukje Market','국제시장'),sub:L('Since 1945','1945년부터'),ll:[35.1013,129.0279],q:'Gukje Market Busan',f:[L('Began after liberation in 1945 as a place to trade goods.','1945년 광복 뒤 물건을 사고팔던 장터에서 시작했어요.'),L('Shops usually 09:00–20:00; many close on Sundays (it varies by shop).','보통 09:00~20:00. 일요일에 쉬는 가게가 많아요(가게마다 달라요).'),L('12 buildings like a maze: use the 2nd-floor skybridge to find your way.','12개 동이 미로 같아요. 2층 구름다리에서 위치를 확인해요.')]},
 btower:{n:L('Busan Tower','부산타워'),sub:L('Yongdusan Park · 120 m','용두산공원 · 120m'),ll:[35.1007,129.0326],q:'Busan Tower',f:[L('Adult ticket ₩12,000. Open every day 10:00–22:00 (last entry 21:30).','성인 12,000원. 연중무휴 10:00~22:00(입장 마감 21:30).'),L('Escalators run up from Nampo-dong. Yongdusan Park itself is free and always open.','남포동에서 에스컬레이터로 올라가요. 용두산공원은 무료, 상시 개방.')]},
 gamcheon:{n:L('Gamcheon Culture Village','감천문화마을'),sub:L('Saha-gu, Busan','부산 사하구'),ll:[35.0975,129.0092],q:'Gamcheon Culture Village',f:[L('Line 1 Toseong Station exit 6, then village bus Saha 1-1, Seogu 2 or Seogu 2-2: about 10 minutes.','1호선 토성역 6번 출구, 마을버스 사하1-1·서구2·서구2-2로 약 10분.'),L('Free to enter; shops about 09:00–18:00. Stamp map ₩2,000 at the information centre.','입장 무료, 가게 09:00~18:00쯤. 안내센터 스탬프 지도 2,000원.'),L('A Korean War refugee settlement, later revived through art and urban renewal.','6·25 피난민의 터전이 도시재생으로 다시 태어났어요.')]},
 haeundae:{n:L('Haeundae Beach','해운대해수욕장'),sub:L('Line 2 Haeundae Station','2호선 해운대역'),ll:[35.1587,129.1604],q:'Haeundae Beach',f:[L('Busan\'s signature beach, lined with hotels and high-rise towers.','호텔과 고층 건물이 늘어선 부산의 대표 해변이에요.')]},
 blueline:{n:L('Haeundae Blueline Park','해운대 블루라인파크'),sub:L('Beach Train · Sky Capsule','해변열차 · 스카이캡슐'),ll:[35.1606,129.1716],q:'Haeundae Blueline Park Mipo Station',f:[L('Beach Train: 4.8 km on the old Donghae Nambu Line, Mipo ↔ Songjeong, about 25 min.','해변열차: 옛 동해남부선 4.8km, 미포 ↔ 송정, 약 25분.'),L('One ride ₩10,000 from Mipo or Songjeong (₩8,000 from Cheongsapo); 2 rides ₩14,000; all stations ₩16,000.','1회권 미포·송정 출발 10,000원(청사포 출발 8,000원), 2회권 14,000원, 모든역 16,000원.'),L('Sky Capsule one way: ₩50,000 for 2, ₩55,000 for 3, ₩60,000 for 4.','스카이캡슐 편도: 2인 50,000원, 3인 55,000원, 4인 60,000원.'),L('Nov–Feb: Beach Train 09:00–19:00, Sky Capsule 08:30–18:00. Prices as of Oct 2026.','11~2월: 해변열차 09:00~19:00, 스카이캡슐 08:30~18:00. 2026년 10월 기준 요금.')]},
 yonggung:{n:L('Haedong Yonggungsa','해동용궁사'),sub:L('Seaside temple · 1376','바닷가 절 · 1376'),ll:[35.1890,129.2231],q:'Haedong Yonggungsa',f:[L('Founded in 1376 by the monk Naong.','1376년 나옹대사가 세웠어요.'),L('Open 04:30–20:30. Free admission.','04:30~20:30. 입장 무료.'),L('108 steps lead down to the temple; a 10 m Haesu Gwaneum Buddha overlooks the sea.','108계단을 내려가요. 10m 해수관음대불이 바다를 내려다봐요.'),L('Bus 181 from Haeundae Station: about 30–40 minutes.','해운대역에서 181번 버스로 약 30~40분.')]},
 gwangan:{n:L('Gwangalli · Gwangan Bridge','광안리 · 광안대교'),sub:L('Line 2 Gwangan Station','2호선 광안역'),ll:[35.1532,129.1186],q:'Gwangalli Beach',f:[L('Gwangan Bridge crosses the bay in front of the beach and is lit up at night.','해변 앞바다를 가로지르는 광안대교에 밤마다 조명이 켜져요.')]},
 drone:{n:L('Gwangalli M Drone Light Show','광안리 M 드론라이트쇼'),sub:L('Saturdays · free','매주 토요일 · 무료'),ll:[35.1532,129.1186],q:'Gwangalli Beach',f:[L('Every Saturday, two shows: 19:00 and 21:00 (Oct–Feb), 20:00 and 22:00 (Mar–Sep).','매주 토요일 두 번: 10~2월 19:00·21:00, 3~9월 20:00·22:00.'),L('Held year-round since April 2022. Free to watch from the beach.','2022년 4월부터 연중 상설. 해변에서 무료로 봐요.')]},
 tybus:{n:L('Busan Central Bus Terminal','부산종합버스터미널'),sub:L('Line 1 Nopo Station','1호선 노포역'),ll:[35.2836,129.0951],q:'Busan Central Bus Terminal',f:[L('Express buses to Tongyeong: 13 a day (07:10–21:00), about 2 h 17 min, premium ₩23,200.','통영행 고속버스: 하루 13회(07:10~21:00), 약 2시간 17분, 우등 23,200원.')]},
 tyjungang:{n:L('Tongyeong Jungang Market','통영 중앙시장'),sub:L('Gangguan harbour','강구안'),ll:[34.8456,128.4253],q:'Tongyeong Jungang Market',f:[L('A busy fish market right on Gangguan harbour.','강구안 바로 앞의 활기찬 수산시장이에요.'),L('Local snacks: Chungmu gimbap and kkulppang (honey bread).','충무김밥과 꿀빵이 유명해요.')]},
 dongpirang:{n:L('Dongpirang Mural Village','동피랑 벽화마을'),sub:L('Since 2007','2007년부터'),ll:[34.8455,128.4270],q:'Dongpirang Village Tongyeong',f:[L('A hillside village above the harbour, right behind Jungang Market.','항구 위 언덕, 중앙시장 바로 뒤의 마을이에요.'),L('The mural project began in 2007, when the houses were due to be demolished. Free.','철거 예정이던 마을에 2007년 벽화 사업이 시작됐어요. 무료.')]},
 cablecar:{n:L('Tongyeong Cable Car','통영케이블카'),sub:L('Up Mireuksan','미륵산'),ll:[34.8270,128.4249],q:'Tongyeong Cable Car',f:[L('1,975 m, about 10 minutes up. Adult round trip ₩17,000.','길이 1,975m, 올라가는 데 약 10분. 성인 왕복 17,000원.'),L('Closed on the 2nd and 4th Wednesday of each month.','매월 둘째·넷째 수요일 휴무.'),L('From the upper station the summit is about a 20-minute round-trip walk.','상부역에서 정상까지 왕복 20분쯤 걸어요.')]},
 nambu:{n:L('Seoul Nambu Terminal','서울남부터미널'),sub:L('Line 3 Nambu Bus Terminal Station','3호선 남부터미널역'),ll:[37.4848,127.0160],q:'Seoul Nambu Terminal',f:[L('Express buses from Tongyeong: 11 a day, about 4 h 29 min, premium ₩41,000.','통영발 고속버스: 하루 11회, 약 4시간 29분, 우등 41,000원.')]},
};
"""
cut("const REAL={","const PH=",REAL)
PH=json.load(open(S+'ph/PH_busan.json',encoding='utf8'))
for k in PH:
    if PH[k][1].startswith('by Junho Jung'):PH[k][1]='Junho Jung'
sub1(r"const PH=\{.*?\};",'const PH='+json.dumps(PH,ensure_ascii=False)+';')
sub1(r"const PANOS=\{.*?\};",'const PANOS={};')
rep("if(id!=='icn'&&id!=='tmoney'&&id!=='kyoja'){const sm=","if(false){const sm=")
# 🚇 '지역으로 바로 가기' 창: 서울 지하철 요금 → 부산 지하철, 서울 전용 S-Map·360 거리 사진 빼기
rep("rb.innerHTML='<span>📷 '+REAL.subway.n+'</span>","rb.innerHTML='<span>📷 '+REAL.bmetro.n+'</span>")
rep("rb.onclick=()=>openReal('subway');b.append(rb);","rb.onclick=()=>openReal('bmetro');b.append(rb);")
cut("{const x=document.createElement('button');x.type='button';x.className='row';x.innerHTML='<span>🏙 '+L('S-Map","const gr=document.createElement('div');gr.className='grid';","")

# ---- 3D 장면: 부산 소품 + 장소별 모양 ----
rep("/* ---------- 상태 ---------- */",open(S+'K_busan_top.js',encoding='utf8').read()+"\n/* ---------- 상태 ---------- */")
rep("if(city!=='hgr')ground(g,1000,1000,","if(city!=='hgr'&&!BSEA[city])ground(g,1000,1000,")
# 스탬프가 없는 곳(서울역·부산역·서울남부)에는 스탬프 버튼을 만들지 않음
rep("{id:'stamp',b:L('Stamp','스탬프'),s:'',city}];","{id:'stamp',b:L('Stamp','스탬프'),s:'',city}].filter(a=>a.id!=='stamp'||STAMPS.some(x=>x.id===city));")
rep("L('✈ Arrival rehearsal','✈ 도착 예행연습')","L('🧭 Trip rehearsal','🧭 여행 예행연습')")
rep("$('enter').textContent=L('Start at the airport','공항에서 시작하기')","$('enter').textContent=L('Start at Seoul Station','서울역에서 시작하기')")
rep(" const curve=new T.CatmullRomCurve3(P,false,'centripetal');if(fac)",open(S+'K_busan_br.js',encoding='utf8').read()+" const curve=new T.CatmullRomCurve3(P,false,'centripetal');if(fac)")
rep("Your hotel room in Myeongdong.","Your hotel room in Nampo-dong.")
rep("명동 호텔 방이에요.","남포동 호텔 방이에요.")
# 엘리베이터 대신 케이블카 표시, 드론쇼 연출, 여행 마치기
rep("b:'🛗 '+f.n,","b:(f.ic||'🛗')+' '+f.n,")
rep("b:L('🛗 Elevator down','🛗 엘리베이터로 내려가기')","b:f.down||L('🛗 Elevator down','🛗 엘리베이터로 내려가기')")
rep("say(f.say);playTune(10,true);markAct(f.id);}});});addQuiz(c,o.city);};","say(f.say);playTune(10,true);markAct(f.id);if(f.fx)f.fx();}});});if(D.fin){const q=S[Math.round(D.fin.t*(SN-1))];c.spots.push({x:q.x,z:q.z,y:q.y,r:7,b:L('🏁 Finish the trip','🏁 여행 마치기'),s:D.fin.s||'',fn:()=>doAct({id:'trip'})});}addQuiz(c,o.city);};")

# ---- 퀴즈 ----
cut("const QZ={","function addQuiz",r"""const QZ={
 sst:[[/KTX to Busan|부산행 KTX/,'bk1',L('How much is a standard-class KTX ticket from Seoul to Busan?','서울 → 부산 KTX 일반실 요금은?'),['₩29,800','₩59,800','₩99,800'],1,L('₩59,800 for every KTX, whatever the number of stops.','정차역 수와 상관없이 59,800원이에요.')]],
 bsn:[[/Nampo|남포/,'bk2',L('How many stops on Line 1 from Busan Station to Nampo?','1호선 부산역에서 남포까지 몇 정거장?'),['1','2','4'],1,L('Busan Station → Jungang → Nampo: 2 stops.','부산역 → 중앙 → 남포, 2정거장이에요.')]],
 nmp:[[/observatory|전망대/,'bk3',L('When is Jagalchi Market closed?','자갈치시장은 언제 쉬나요?'),[L('Every Monday','매주 월요일'),L('1st, 3rd and 5th Tuesday','첫째·셋째·다섯째 화요일'),L('Never','쉬는 날 없음')],1,L('It closes on the 1st, 3rd and 5th Tuesday of the month.','매월 첫째·셋째·다섯째 화요일에 쉬어요.')]],
 gmc:[[/Information|안내센터/,'bk4',L('How do you get to Gamcheon from Toseong Station?','토성역에서 감천문화마을은 어떻게 가나요?'),[L('Cable car','케이블카'),L('Village bus from exit 6','6번 출구 마을버스'),L('Ferry','배')],1,L('Village bus Saha 1-1, Seogu 2 or Seogu 2-2 from exit 6, about 10 minutes.','6번 출구에서 마을버스 사하1-1·서구2·서구2-2로 약 10분이에요.')]],
 hud:[[/Beach Train|해변열차/,'bk5',L('How long is the Beach Train line?','해변열차 노선 길이는?'),['1.2 km','4.8 km','12 km'],1,L('4.8 km on the old Donghae Nambu Line, Mipo to Songjeong.','옛 동해남부선 4.8km, 미포~송정이에요.')]],
 ygs:[[/Gwangalli|광안리/,'bk6',L('When was Haedong Yonggungsa founded?','해동용궁사는 언제 세워졌나요?'),['1376','1876','1976'],0,L('In 1376, by the monk Naong.','1376년 나옹대사가 세웠어요.')]],
 gal:[[/Drone|드론/,'bk7',L('On which day is the Gwangalli drone show?','광안리 드론쇼는 무슨 요일?'),[L('Friday','금요일'),L('Saturday','토요일'),L('Sunday','일요일')],1,L('Every Saturday, twice a night.','매주 토요일, 하루 두 번이에요.')]],
 tyg:[[/Cable Car|케이블카/,'bk8',L('When is the Tongyeong Cable Car closed?','통영케이블카 정기 휴무는?'),[L('Every Monday','매주 월요일'),L('2nd and 4th Wednesday','둘째·넷째 수요일'),L('Last Sunday','마지막 일요일')],1,L('Closed on the 2nd and 4th Wednesday of each month.','매월 둘째·넷째 수요일에 쉬어요.')],
  [/Seoul Nambu|서울남부/,'bk9',L('About how long is the express bus from Tongyeong to Seoul Nambu?','통영 → 서울남부 고속버스는 약 얼마나 걸리나요?'),[L('About 2 h','약 2시간'),L('About 4.5 h','약 4시간 반'),L('About 7 h','약 7시간')],1,L('About 4 h 29 min (premium ₩41,000).','약 4시간 29분(우등 41,000원)이에요.')]]};
""")

# ---- 표현 · 꼭 기억할 것 ----
rep("['명동역 어디예요?','Myeongdong-yeok eodi-yeyo?',L('Where is Myeongdong Station?','명동역 어디예요?')]","['부산역 어디예요?','Busan-yeok eodi-yeyo?',L('Where is Busan Station?','부산역 어디예요?')]")
cut("h(L('Remember','꼭 기억할 것'));[","L('Meal and shop prices in this app are examples.",r"""h(L('Remember','꼭 기억할 것'));[L('KTX Seoul → Busan ₩59,800 (standard) · fastest about 2 h 18 min','KTX 서울 → 부산 일반실 59,800원 · 가장 빠른 열차 약 2시간 18분'),L('Busan subway card fare: zone 1 ₩1,600, zone 2 ₩1,800 · T-money works','부산 지하철 교통카드 1구간 1,600원, 2구간 1,800원 · 티머니 사용 가능'),L('Jagalchi closed 1st/3rd/5th Tuesday · Busan Tower 10:00–22:00, ₩12,000','자갈치 첫째·셋째·다섯째 화요일 휴무 · 부산타워 10:00~22:00, 12,000원'),L('Beach Train from Mipo ₩10,000 · Nov–Feb 09:00–19:00','해변열차 미포 출발 10,000원 · 11~2월 09:00~19:00'),L('Drone show: Saturdays 19:00 and 21:00 (Oct–Feb), 20:00 and 22:00 (Mar–Sep)','드론쇼: 토요일 19:00·21:00(10~2월), 20:00·22:00(3~9월)'),L('Tongyeong Cable Car ₩17,000 round trip · closed 2nd/4th Wednesday','통영케이블카 왕복 17,000원 · 둘째·넷째 수요일 휴무'),L('Express bus Tongyeong → Seoul Nambu about 4 h 29 min, premium ₩41,000','고속버스 통영 → 서울남부 약 4시간 29분, 우등 41,000원'),""")

# ---- 맛집 찾기: 부산 동네 이름 · 부산 음식 ----
sub1(r"const AREAKO=\{[^}]*\};","const AREAKO={sst:'서울역',bsn:'부산역',jagalchi:'자갈치',biff:'남포동',gukje:'국제시장',btower:'남포동',gamcheon:'감천문화마을',haeundae:'해운대',blueline:'해운대 미포',yonggung:'기장 해동용궁사',gwangan:'광안리',drone:'광안리',tyjungang:'통영 강구안',dongpirang:'통영 동피랑',cablecar:'통영 도남동',nambu:'서울남부터미널'};")
rep("const FOODS=[","const FOODS=[\n  {k:'돼지국밥',e:'dwaeji-gukbap',s:'Pork soup',ic:'🍲',re:/돼지국밥|국밥|gukbap|pork soup/i},\n  {k:'밀면',e:'milmyeon',s:'Milmyeon',ic:'🍜',re:/밀면|milmyeon/i},\n  {k:'충무김밥',e:'Chungmu gimbap',s:'Chungmu gimbap',ic:'🍙',re:/충무김밥|chungmu/i},\n  {k:'씨앗호떡',e:'ssiat hotteok',s:'Hotteok',ic:'🥞',re:/씨앗호떡|호떡|hotteok/i},\n  {k:'어묵',e:'eomuk fish cake',s:'Fish cake',ic:'🍢',re:/어묵|오뎅|eomuk|fish ?cake/i},\n  {k:'회',e:'raw fish (hoe)',s:'Raw fish',ic:'🐟',re:/횟집|생선회|모둠회|raw fish|sashimi/i},")
rep("L('Good kimbap place nearby?','김밥 맛집 어디예요?')","L('Good dwaeji-gukbap place nearby?','돼지국밥 맛집 어디예요?')")
rep("go('myd',.33);const n=cur.npcs.find(x=>x.id==='cit0')","go('nmp',.22);const n=cur.npcs.find(x=>x.id==='cit0')")

# ---- 시작 화면 · 지금 날씨 · 안내 문구 ----
rep('INCHEON AIRPORT → SEOUL','SEOUL → BUSAN · TONGYEONG')
rep("$('stH').innerHTML=L('Virtual Seoul<br>3 days','가상 서울<br>2박 3일');","$('stH').innerHTML=L('Virtual Busan<br>3 days','가상 부산·경남<br>2박 3일');")
sub1(r"\$\('stP'\)\.textContent=L\('(?:[^'\\]|\\.)*','(?:[^'\\]|\\.)*'\);",r"""$('stP').textContent=L('Leave Seoul Station by KTX. Eat at Jagalchi fish market, climb Busan Tower, wander the painted lanes of Gamcheon, ride the Beach Train at Haeundae, visit a temple on the sea rocks and watch Gwangan Bridge at night. Then take the bus to Tongyeong, ride the cable car up Mireuksan and come back to Seoul. Real fares, times and photos.','서울역에서 KTX로 출발해요. 자갈치시장에서 먹고, 부산타워에 오르고, 감천문화마을 골목을 걷고, 해운대 해변열차를 타고, 바다 바위 위 절에 가고, 광안대교 야경을 봐요. 버스로 통영에 가서 케이블카로 미륵산에 오른 뒤 서울로 돌아와요. 실제 요금·시간·사진을 담았어요.');""")
sub1(r"\$\('stR'\)\.textContent=L\('(?:[^'\\]|\\.)*','(?:[^'\\]|\\.)*'\);",r"""$('stR').textContent=L('Seoul Station · KTX · Jagalchi · BIFF · Gukje Market · Busan Tower · Gamcheon · Haeundae · Blueline Park · Yonggungsa · Gwangalli · Tongyeong · Seoul Nambu','서울역 · KTX · 자갈치 · BIFF · 국제시장 · 부산타워 · 감천 · 해운대 · 블루라인파크 · 용궁사 · 광안리 · 통영 · 서울남부');""")
rep("latitude=37.5665&longitude=126.978","latitude=35.1796&longitude=129.0756")
rep("L('Seoul now ','지금 서울 ')","L('Busan now ','지금 부산 ')")
rep("L('Live Seoul time and weather','지금 서울 시각·날씨 그대로')","L('Live Busan time and weather','지금 부산 시각·날씨 그대로')")
rep("L('Seoul stamps','서울 스탬프')","L('Busan · Gyeongnam stamps','부산·경남 스탬프')")
rep("Have a great real trip to Seoul!","Have a great real trip to Busan!")
rep("'Good morning! A new day in Seoul.'","'Good morning! A new day of your trip.'")
rep("role:L('Your Seoul tour guide','서울 여행 가이드')","role:L('Your Busan · Gyeongnam tour guide','부산·경남 여행 가이드')")
s=s.replace("서울 2박 3일 코스","부산·경남 2박 3일 코스")
rep("L('Ask me anything about Seoul!','서울에 대해 무엇이든 물어보세요!')","L('Ask me anything about Busan and Tongyeong!','부산과 통영에 대해 무엇이든 물어보세요!')")
s=s.replace("가상 서울로","가상 부산으로").replace("가상 서울","가상 부산").replace("Virtual Seoul","Virtual Busan")
rep("else go(nextQ()?nextQ().q.sc:'icn',","else go(nextQ()?nextQ().q.sc:'sst',")
rep("dayI=0;closePanel();go('icn');};b.append(rs);","dayI=0;closePanel();go('sst');};b.append(rs);")
open(S+'busan.html','w',encoding='utf8').write(s);print('ok busan',len(s))
