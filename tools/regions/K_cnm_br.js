 if(city==='yst'){fac=modern;off=13;hh=[16,40];W=10;nP=40;words=['편의점 CVS','카페','약국','ATM','관광안내 INFO'];
  const pf=new T.Group();pf.userData.pass=1;box(pf,150,1,8,M('#b9b4aa'),-196,0,-18);box(pf,150,.06,.5,M('#f0c419'),-196,1,-21.6);g.add(pf);
  const kt=mkKTX(120);kt.position.set(-196,1,-25.6);g.add(kt);
  const hall=new T.Group();hall.userData.pass=1;box(hall,96,1,34,new T.MeshPhongMaterial({color:'#9fb8cc',specular:'#ffffff',shininess:80,transparent:true,opacity:.5}),-80,15,-12);
  for(let x=-124;x<=-36;x+=11)for(const z of[-28,4])cyl(hall,.45,.45,15,M('#c9ced4'),x,0,z,8);g.add(hall);
  label(g,'용산역 YONGSAN STATION',-35.6,17,-12,Math.PI/2,26,'#fff','#1f4f91');
  box(g,.4,4.6,12,M('#1d2a36',{emissive:'#0a1018'}),-70,8.6,-10);label(g,RGN.jh,-69.7,11.6,-10,Math.PI/2,11,'#ffd84a','#1d2a36');label(g,'타는 곳 → PLATFORM',-69.7,9.6,-10,Math.PI/2,11,'#fff','#1d2a36');
  for(let i=0;i<4;i++){box(g,1.4,2,1,M('#2e5a86'),-48-i*2.6,0,-25);label(g,'승차권 TICKET',-48-i*2.6,2.4,-24.45,0,2.4,'#fff','#2e5a86');}
  P=pathFromXZ([[0,0,70],[0,0,30],[-10,0,0],[-50,0,-8],[-100,0,-12],[-128,1,-18],[-170,1,-18],[-230,1,-18]]);ex=[[-80,-12,64],[-196,-20,96]];
  notes=[[0,RGN.yst0],[.5,L('Janghang Line trains (Mugunghwa, ITX-Saemaeul, ITX-Maeum) leave here for Cheonan, Onyangoncheon and the west coast.','장항선 열차(무궁화·ITX-새마을·ITX-마음)가 여기서 천안·온양온천·서해안으로 떠나요.')],[.8,RGN.yst8]];}
 if(city==='cna'){W=10;nP=40;ground(g,520,420,-60,-80,'#b9b4aa');
  nationTower(g,0,-40,42);bigHall(g,0,-150,60,30);
  for(let z=10;z>-120;z-=10){tFlag(g,-14,z);tFlag(g,14,z);}
  for(let i=0;i<30;i++){const x=(rnd()<.5?-1:1)*(40+rnd()*120),z=-200+rnd()*240;pine(g,x,z,.6);}
  cone(g,140,60,M('#4f6a45'),-60,0,-330,18);cone(g,110,50,M('#56704a'),120,0,-300,18);
  box(g,.4,5,.4,M('#5a4a3a'),9,0,40);label(g,'독립기념관 · INDEPENDENCE HALL',9,5.6,40.3,0,18,'#fff','#1f4f91');
  box(g,3,2.6,1,M('#2e5a86'),12,0,62);label(g,'정류장 · BUS STOP',12,3.2,62.6,0,6,'#fff','#2e5a86');
  P=pathFromXZ([[0,0,70],[0,0,40],[-6,0,10],[-6,0,-20],[-6,0,-60],[-6,0,-100],[0,0,-126]]);ex=[];
  notes=[[0,L('The Independence Hall of Korea, Cheonan. Free. Nov–Feb 09:30–17:00, Mar–Oct 09:30–18:00 (last entry 1 h before). Closed Mondays (open if Monday is a public holiday).','천안 독립기념관이에요. 입장 무료. 11~2월 09:30~17:00, 3~10월 09:30~18:00(입장 마감은 닫기 1시간 전). 매주 월요일 휴관(공휴일이면 열어요).')],[.35,L('The tall white monument is the Tower of the Nation; beyond it, the great hall and the exhibition halls on Korea’s independence movement.','하얀 탑은 겨레의 탑이에요. 그 뒤로 큰 전시관과 독립운동 전시관이 있어요.')],[.85,L('The grounds are big. A shuttle is listed at adult ₩5,000: check on the day.','안이 아주 넓어요. 셔틀은 어른 5,000원으로 안내돼 있어요. 당일 확인해요.')]];}
 if(city==='ony'){fac=modern;off=13;hh=[8,18];W=9;nP=46;words=['온천 SPA','목욕탕 BATH','족욕 FOOT BATH','호텔 HOTEL','온천시장 MARKET','약국'];
  const st=new T.Group();st.userData.pass=1;box(st,30,9,14,M('#eef1f4'),0,0,0);box(st,31,.8,15,M('#2e5a86'),0,9,0);st.position.set(22,0,60);g.add(st);
  label(g,'온양온천역 ONYANGONCHEON',14.7,10.4,60,-Math.PI/2,20,'#fff','#2e5a86');
  footBath(g,-6,-6,16,Math.PI/2);label(g,'족욕장 · FOOT BATH',-6,4.2,-14.2,0,10,'#fff','#8a6a4a');
  for(let z=-40;z>-110;z-=14){box(g,12,10,10,M('#e8e1d4'),-18,0,z);label(g,['온천탕 SPA','♨ 온천','목욕탕','♨ SPA'][((-z/14)|0)%4],-11.9,7,z,Math.PI/2,7,'#fff','#c8553d');for(let i=0;i<3;i++)sph(g,1.2,M('#ffffff',{transparent:true,opacity:.25}),-18+rnd()*4,11+i*1.6,z+rnd()*3,1,.6,1);}
  box(g,3,2.6,1,M('#2e5a86'),7,0,40);label(g,'시외버스 · INTERCITY BUS',7,3.2,40.6,0,7,'#fff','#2e5a86');
  P=pathFromXZ([[0,0,60],[0,0,40],[0,0,10],[0,0,-20],[0,0,-60],[0,0,-100],[0,0,-130]]);ex=[[22,60,24],[-18,-75,16]];
  notes=[[0,L('Onyangoncheon Station. Onyang is said to be Korea’s oldest hot spring, used for about 1,300 years.','온양온천역이에요. 온양온천은 약 1,300년 역사를 가진 우리나라에서 가장 오래된 온천이라고 해요.')],[.3,L('Joseon kings such as Sejong, Sejo, Sukjong, Yeongjo and Jeongjo came here to rest and heal.','세종·세조·숙종·영조·정조 같은 조선 임금들이 쉬거나 병을 고치러 왔어요.')],[.6,L('Alkaline water, 37–54°C. Bathhouses sit around the station; Onyang Oncheon Land, for example, charges adults ₩10,000.','알칼리성 온천수, 37~54°C. 역 주변에 온천탕이 모여 있어요. 예: 온양 온천 랜드 어른 10,000원.')]];}
 if(city==='wmk'){seaY=-1.2;W=7;nP=24;ground(g,520,240,-60,-150,'#b9ad98');ground(g,260,40,-40,-14,'#e8d9b0',-.6);
  for(let i=0;i<6;i++)fBoat(g,-160+i*40,40+rnd()*60,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  box(g,60,1.6,6,M('#bdb3a0'),60,-1.2,20);rocks(g,-140,6,4,2);rocks(g,40,4,3,1.6);
  for(let x=-200;x<80;x+=12){gHouse(g,x,0,-60-rnd()*30,6+rnd()*3,4+rnd()*3,6,GPAL[(rnd()*10)|0]);}
  box(g,.4,5,.4,M('#5a4a3a'),-20,0,-38);label(g,'왜목마을 · WAEMOK VILLAGE',-20,5.6,-37.7,0,16,'#fff','#c8553d');
  P=pathFromXZ([[60,0,-44],[30,0,-36],[0,0,-32],[-30,0,-30],[-60,0,-30],[-100,0,-32],[-140,0,-36]]);ex=[];
  notes=[[0,L('Waemok Village, Dangjin, at the northern tip of the Taean Peninsula.','당진 왜목마을이에요. 태안반도 가장 북쪽 끝에 있어요.')],[.45,L('Famous as the only place in Korea where you can see sunrise, sunset and moonrise from one spot.','해돋이와 해넘이, 달맞이까지 한 곳에서 볼 수 있는 전국 유일의 곳으로 유명해요.')]];}
 if(city==='hmi'){W=8;nP=34;ground(g,500,420,-40,-80,'#b9b4aa');
  const C=[-30,-80],R=70;let prev=null;for(let i=0;i<=24;i++){const a=i/24*Math.PI*2,pt=[C[0]+Math.cos(a)*R,0,C[1]+Math.sin(a)*R*.8];if(prev&&!(i===6||i===7))fortWall(g,prev,pt,5,'#bdb3a0');prev=pt;}
  const gx=C[0],gz=C[1]+R*.8;box(g,14,6,6,M('#bdb3a0'),gx,0,gz);tHall(g,gx,6,gz,10,5,0,'#b9a27a');label(g,'진남문 · JINNAMMUN',gx,4.4,gz+3.1,0,9,'#fff','#5a3a26');
  bigTree(g,-50,-70,1.2);tHall(g,-10,0,-120,22,10,0,'#b9a27a');for(let i=0;i<7;i++)thatch(g,-90+rnd()*40,-60-rnd()*60,rnd()*3);
  for(let i=0;i<6;i++)flag(g,gx-12+i*4.6,6,gz-1,['#c8202a','#f0c419','#2e5a86','#3fa865','#f4f6f7','#c8202a'][i]);
  box(g,3,2.6,1,M('#2e5a86'),10,0,60);label(g,'해미 정류소 · BUS',10,3.2,60.6,0,6,'#fff','#2e5a86');
  P=pathFromXZ([[0,0,80],[-10,0,50],[-28,0,6],[-30,0,-20],[-40,0,-60],[-30,0,-100],[-12,0,-112]]);ex=[];
  notes=[[0,L('Haemieupseong Walled Town, Seosan. Free, parking free. Nov–Feb 06:00–19:00, Mar–Oct 05:00–21:00. Open every day.','서산 해미읍성이에요. 입장·주차 무료. 11~2월 06:00~19:00, 3~10월 05:00~21:00. 연중무휴.')],[.3,L('Built in 1491 (King Seongjong 22). The stone wall is about 1.8 km around and about 5 m high.','1491년(성종 22년)에 쌓았어요. 둘레 약 1.8km, 높이 약 5m 돌성이에요.')],[.6,L('During the persecutions many Catholics were brought here; about 1,000 are recorded as executed in 1866. An old tree in the plaza was used for torture.','박해 때 많은 천주교 신자가 이곳에 끌려왔어요. 1866년에 약 1,000명이 처형됐다고 기록돼 있어요. 광장의 오래된 나무는 고문에 쓰였대요.')]];}
 if(city==='kkj'){seaY=-1.2;W=7;nP=26;ground(g,620,220,0,-150,'#9a9a7a');ground(g,600,60,0,-20,'#e8d9b0',-.6);
  rockIslet(g,-30,60,10,14);rockIslet(g,14,74,6,9);
  for(let x=-240;x<240;x+=12){if(rnd()<.8)pine(g,x+rnd()*5,-58-rnd()*30,.55);}
  for(let x=-200;x<200;x+=40)gHouse(g,x,0,-90-rnd()*30,6,4,6,GPAL[(rnd()*10)|0]);
  box(g,.4,5,.4,M('#5a4a3a'),-8,0,-44);label(g,'꽃지해수욕장 · KKOTJI BEACH',-8,5.6,-43.7,0,16,'#fff','#c8553d');
  P=pathFromXZ([[80,0,-48],[50,0,-40],[20,0,-30],[0,0,-22],[-20,0,-16],[-50,0,-18],[-90,0,-24]]);ex=[];
  notes=[[0,L('Kkotji Beach, Anmyeon-eup, Taean: the largest beach on Anmyeondo, always open and famous for its sunsets.','태안 안면읍 꽃지해수욕장이에요. 안면도에서 가장 큰 해변으로, 늘 열려 있고 해넘이로 유명해요.')],[.35,L('The two rocky islets are Halmi (grandma) and Halabi (grandpa) Rocks, a national Scenic Site (No. 69, 2009).','두 바위섬은 할미바위와 할아비바위예요. 명승 제69호(2009년)예요.')],[.6,L('Legend: when Jang Bogo’s commander Seungeon never came back, his wife Mido waited on the rock until she turned to stone; later a second rock rose beside her.','전설: 장보고의 부하 승언이 돌아오지 않자 아내 미도가 바위에서 기다리다 돌이 됐고, 뒤에 그 곁에 바위가 하나 더 생겼대요.')]];}
 if(city==='dcb'){seaY=-1.2;W=8;nP=40;ground(g,700,220,0,-150,'#b9b4aa');ground(g,700,70,0,-14,'#cdb07a',-.6);
  seaRail(g,[-260,40],[60,40],9);
  box(g,30,12,18,M('#8a6a4a'),120,0,-70);label(g,'머드체험관 · MUD EXPERIENCE',120,13.4,-60.8,0,20,'#fff','#5a3a26');
  cyl(g,1.6,2,30,M('#c9ced4'),-150,0,-56,10);label(g,'집트랙 · ZIP TRACK',-150,31,-54,0,10,'#fff','#c8202a');
  for(let x=-280;x<260;x+=16){if(Math.abs(x-120)<24)continue;box(g,10,6+rnd()*14,10,M(['#e8e1d4','#c9ced4','#d8d2c6'][(rnd()*3)|0]),x,0,-80-rnd()*20);}
  for(let i=0;i<16;i++){const p=person(g,-200+rnd()*360,-.6,-4+rnd()*10,CLOTH[(rnd()*9)|0],SKIN[(rnd()*4)|0],1);p.rotation.y=rnd()*6;}
  box(g,.4,5,.4,M('#5a4a3a'),0,0,-44);label(g,'대천해수욕장 · DAECHEON BEACH',0,5.6,-43.7,0,16,'#fff','#2e8fd0');
  box(g,3,2.6,1,M('#2e5a86'),-36,0,-52);label(g,'대천역 가는 버스 · BUS',-36,3.2,-51.4,0,8,'#fff','#2e5a86');
  P=pathFromXZ([[120,0,-46],[80,0,-40],[40,0,-34],[0,0,-30],[-40,0,-30],[-80,0,-34],[-120,0,-40]]);ex=[];
  notes=[[0,L('Daecheon Beach, Boryeong: white sand about 3.5 km long. The Boryeong Mud Festival is held here every summer (2026: 24 July–9 August).','보령 대천해수욕장이에요. 길이 약 3.5km 하얀 모래사장이에요. 해마다 여름 보령머드축제가 열려요(2026년 7월 24일~8월 9일).')],[.35,L('The Sky Bike runs on rails 8–15 m above the sea between the beach and Daecheon Port: 2.3 km round trip, about 40 min.','스카이바이크는 바다 위 8~15m 레일을 달려 해수욕장과 대천항을 오가요. 왕복 2.3km, 약 40분.')],[.65,L('At the end of the beach, the Boryeong Mud Experience Center has a mud sauna and mud packs.','해변 끝 보령머드체험관에는 머드 사우나와 머드팩이 있어요.')]];}
