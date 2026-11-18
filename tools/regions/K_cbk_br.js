 if(city==='dyt'){seaY=-2;fac=modern;off=13;hh=[7,16];W=9;nP=26;words=['마늘 GARLIC','닭강정','마늘빵','순대','카페','약국'];
  ground(g,340,330,40,35,'#b9b4aa');
  const st=new T.Group();st.userData.pass=1;box(st,10,8,26,M('#eef1f4'),0,0,0);box(st,11,.8,27,M('#3f6a8a'),0,8,0);st.position.set(20,0,62);g.add(st);
  label(g,'단양역 DANYANG STATION',14.7,10.4,62,-Math.PI/2,16,'#fff','#2e5a86');
  for(const z of[-6,7])cyl(g,.45,.45,7.6,KRED,-30,0,z,8);box(g,.8,1,15,KRED,-30,7.4,.5);label(g,'단양구경시장 · GUGYEONG MARKET',-29.4,8.4,.5,Math.PI/2,13,'#fff','#c8202a');
  box(g,150,36,40,M('#7a7266'),-205,-2,0.3);for(let x=-140;x>-270;x-=18)pineAt(g,x+rnd()*6,34,2+rnd()*12,.6);for(let x=-135;x>-275;x-=9)box(g,4+rnd()*4,3+rnd()*10,1.2,M('#6a6458'),x,4+rnd()*20,-19.8);
  deck(g,[-126,0,-22],[-272,0,-22],4.4,'#5e4a38');rail(g,[-126,0,-22],[-272,0,-22],2.3);
  for(let x=-136;x>-270;x-=12)sph(g,.16,M('#ffe6a0',{emissive:'#ffcf60'}),x,1.3,-24.3);
  label(g,'단양강 잔도 · DANYANGGANG JANDO',-150,7,-19.9,Math.PI,12,'#fff','#5a3a26');
  cone(g,90,70,M('#4f6a45'),-200,-2,-140,20);cone(g,70,50,M('#56704a'),-60,-2,-170,18);
  P=pathFromXZ([[0,0,72],[0,0,40],[-4,0,16],[-20,0,2],[-60,0,-4],[-100,0,-10],[-126,0,-22],[-160,0,-22],[-210,0,-22],[-268,0,-22]]);
  ex=[[20,62,18],[-150,-22,30],[-200,-22,30],[-250,-22,30]];
  notes=[[0,L('Danyang Station: the KTX-Eum from Seoul arrives here. Town buses run infrequently, so a taxi into Danyang-eup is often easier.','단양역이에요. 서울에서 온 KTX-이음이 여기 도착해요. 시내버스 배차가 길어서 단양읍까지는 택시가 편할 때가 많아요.')],[.3,L('Gugyeong Market: Danyang is known for garlic, and the market is full of garlic snacks such as black-garlic dakgangjeong.','단양구경시장이에요. 단양은 마늘로 유명해서 흑마늘 닭강정 같은 마늘 먹거리가 많아요.')],[.62,L('The Danyanggang Jando: a deck path fixed to the cliff above the Namhan River, about 1.12 km one way (about 30 min). Free, and lit up at night.','단양강 잔도예요. 남한강 절벽에 붙여 만든 데크길로 편도 약 1.12km(약 30분). 무료이고 밤에는 조명이 켜져요.')]];}
 if(city==='dds'){seaY=-1.2;W=7;nP=16;ground(g,420,130,-60,95,'#b9b4aa');
  rockPeak(g,-80,8,4,10,21,-1.2);rockPeak(g,-70.5,13,4.6,5.4,3,-1.2);jPavilion(g,-70.5,1.8,13);
  rockPeak(g,-99,3,2.6,6,12,-1.2);pineAt(g,-99,10.8,3,.35);rockPeak(g,-63,12,2.4,5.5,9,-1.2);pineAt(g,-63,7.8,12,.3);
  box(g,.4,5,.4,M('#5a4a3a'),-98,0,52.4);label(g,'도담삼봉 · DODAMSAMBONG',-98,5.6,52,Math.PI,14,'#fff','#2f5a2e');
  cone(g,90,50,M('#4f6a45'),-60,-1.2,-110,20);cone(g,70,40,M('#56704a'),-200,-1.2,-90,18);cone(g,60,36,M('#4a6440'),90,-1.2,-90,18);
  for(let x=-250;x<130;x+=22){const z=118+rnd()*20;pine(g,x+rnd()*8,x>-60?z+20:z-40,.55);}fBoat(g,-36,-8,.4,'#f0c419');
  P=pathFromXZ([[40,0,112],[10,0,98],[-30,0,80],[-56,0,62],[-72,0,46],[-84,0,38],[-112,0,40],[-160,0,46],[-200,0,58],[-226,0,72]]);ex=[];
  notes=[[0,L('Dodamsambong: three rock peaks rising from the Namhan River, the first of the Eight Scenic Views of Danyang. Free; open every day.','도담삼봉이에요. 남한강 가운데 솟은 세 바위 봉우리로 단양팔경 제1경이에요. 입장 무료, 연중무휴.')],[.4,L('The pavilion on the largest peak is Samdojeong. Joseon scholars and painters such as Yi Hwang and Kim Hong-do left works about this place.','가장 큰 봉우리 위 정자가 삼도정이에요. 퇴계 이황과 단원 김홍도 같은 조선의 선비·화가가 이곳을 글과 그림으로 남겼어요.')],[.75,L('Hours 09:00–18:00 (each facility differs). Parking: small cars ₩3,000.','운영 09:00~18:00(시설마다 달라요). 주차는 소형차 3,000원.')]];}
 if(city==='mch'){seaY=-50;W=7;nP=14;box(g,320,50,188,M('#6f6a5c'),-40,-50,86);ground(g,320,188,-40,86,'#8a9a6a');
  cone(g,110,80,M('#4f6a45'),-40,-50,-170,20);cone(g,90,70,M('#56704a'),-200,-50,-130,18);cone(g,80,60,M('#4a6440'),130,-50,-150,18);
  skyTower(g,-50,0,30);box(g,.4,5,.4,M('#5a4a3a'),12,0,30);label(g,'만천하스카이워크 · MANCHEONHA SKYWALK',12,5.6,30.3,0,16,'#fff','#2e5a86');
  for(let i=0;i<22;i++){const x=-170+rnd()*260,z=40+rnd()*120;if(Math.abs(x)<14&&z<80)continue;pine(g,x,z,.6);}
  P=pathFromXZ([[0,0,70],[0,0,44],[-16,0,26],[-36,0,14],[-44,0,9],[-48,15,4],[-50,30,-4],[-50,30,-12],[-50,30,-20]]);ex=[];
  notes=[[0,L('Mancheonha Skywalk. Adult ₩4,000. Nov–Mar 09:00–17:00 (tickets until 16:00); Apr–Oct 09:00–18:00 (tickets until 17:00).','만천하스카이워크예요. 어른 4,000원. 11~3월 09:00~17:00(매표 16:00까지), 4~10월 09:00~18:00(매표 17:00까지).')],[.3,L('The zipwire (980 m), alpine coaster (1,000 m) and slide cost extra. The shuttle bus from the car park does not run on Tuesdays.','짚와이어(980m), 알파인코스터(1,000m), 슬라이드는 따로 요금을 내요. 주차장 셔틀버스는 화요일에 다니지 않아요.')],[.97,L('The glass decks hang out over a cliff 80–90 m above the Namhan River.','유리 전망대가 남한강 위 80~90m 절벽 밖으로 뻗어 있어요.')]];}
 if(city==='ulj'){seaY=-1;W=7;nP=18;
  ground(g,520,200,-100,114,'#7f8f5a');ground(g,520,160,-100,-180,'#7f8f5a');ground(g,200,120,-320,-43,'#7f8f5a');ground(g,200,120,90,-43,'#7f8f5a');
  ground(g,16,16,-120,8,'#7f8f5a');jPavilion(g,-120,0,7);
  for(let x=-230;x<10;x+=15){if(rnd()<.25)pine(g,x+rnd()*5,14.6,.45);if(rnd()<.7)pine(g,x+rnd()*6,34+rnd()*12,.6);}for(let x=-210;x<0;x+=40)oldTree(g,x,30,.8);
  box(g,.4,4.6,.4,M('#5a4a3a'),-60,0,15.2);label(g,'의림지 · UIRIMJI',-60,5.2,15,0,10,'#fff','#2f5a2e');
  box(g,3,2.6,1,M('#2e5a86'),14,0,58);label(g,'의림지 정류장 · BUS STOP',14,3.2,58.6,0,7,'#fff','#2e5a86');
  cone(g,90,40,M('#4f6a45'),-100,-1,-280,20);cone(g,70,35,M('#56704a'),-330,-1,-120,18);cone(g,80,38,M('#4a6440'),140,-1,-170,18);
  P=pathFromXZ([[40,0,80],[20,0,46],[0,0,26],[-40,0,21],[-100,0,22],[-150,0,21],[-200,0,26],[-236,0,40]]);ex=[];
  notes=[[0,L('Uirimji. From Jecheon Station, city buses 31 or 35 take about 20 minutes to the Uirimji stop.','의림지예요. 제천역에서 시내버스 31·35번 등으로 의림지 정류장까지 약 20분이에요.')],[.35,L('A reservoir said to date from the Samhan period, before the Three Kingdoms. Free and always open.','삼한 시대에 만들었다고 전하는 오래된 저수지예요. 입장 무료, 늘 열려 있어요.')],[.7,L('Legend says the musician Ureuk first dammed the stream in Silla times, and magistrate Park Ui-rim later rebuilt the bank.','신라 때 우륵이 처음 둑을 쌓았고, 뒤에 현감 박의림이 더 튼튼히 고쳐 쌓았다는 이야기가 전해요.')]];}
 if(city==='cpc'){seaY=-1.2;ground(g,500,200,0,-140,'#9a9a7a');W=7;nP=14;
  const st=new T.Group();st.userData.pass=1;for(const a of[-8.5,8.5])for(const b of[-6.5,6.5])box(st,.6,9,.6,M('#d8dde2'),a,0,-36+b);box(st,19,.8,15,M('#2e8fd0'),0,9,-36);box(st,5,2.6,2,M('#f4f6f7'),-6,0,-41);g.add(st);
  label(g,'청풍호반케이블카 · 물태리역',0,11.6,-43.6,Math.PI,18,'#fff','#2e8fd0');
  const cb=new T.Group();cb.userData.pass=1;const c1=[new T.Vector3(-3,10,-34),new T.Vector3(-3,40,14),new T.Vector3(-3,59,62)],c2=c1.map(v=>new T.Vector3(3,v.y,v.z));
  for(const cs of[c1,c2])cb.add(new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(cs),40,.12,4,false),M('#3a3f45')));
  for(let i=0;i<5;i++){const z=-14+i*16,y=10+(z+34)/96*49;box(cb,2.4,2.6,2.4,M(i%2?'#2e8fd0':'#f0c419'),i%2?3:-3,y-3.4,z);}g.add(cb);
  cone(g,80,58,M('#3f6a3a'),0,-1.2,72,24);box(g,12,.6,12,M('#4f4a44'),0,56.4,66);for(const a of[-5.8,5.8]){box(g,.2,1.1,12,M('#3a3430'),a,57,66);box(g,12,1.1,.2,M('#3a3430'),0,57,66+a);}
  box(g,.3,4,.3,M('#6a5040'),5,57,72);label(g,'비봉산 · BIBONGSAN',5,61.4,72.2,0,9,'#fff','#5a3a26');
  cone(g,70,30,M('#4f6a45'),-170,-1.2,120,18);cone(g,60,26,M('#56704a'),170,-1.2,150,18);cone(g,90,34,M('#4a6440'),-60,-1.2,320,20);
  for(let i=0;i<4;i++)fBoat(g,-80+i*50,30+rnd()*60,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  P=pathFromXZ([[0,0,-110],[0,0,-80],[0,0,-46],[0,28,8],[0,57,58],[0,57,64],[0,57,70]]);ex=[];
  notes=[[0,L('Cheongpung Lake Cable Car, Multae-ri station. It climbs 2.3 km to the top of Bibongsan.','청풍호반케이블카 물태리역이에요. 비봉산 정상까지 2.3km를 올라가요.')],[.25,L('Standard cabin: adult ₩18,000 round trip. Glass-floored Crystal cabin: ₩23,000. About 10 minutes one way.','일반 캐빈 어른 왕복 18,000원, 바닥이 투명한 크리스탈 캐빈 23,000원. 편도 약 10분.')],[.97,L('The top of Bibongsan: Cheongpung Lake spreads out below like an inland sea.','비봉산 정상이에요. 발아래로 청풍호가 바다처럼 펼쳐져요.')]];}
 if(city==='sag'){W=6;nP=22;ground(g,900,700,-120,-40,'#8f8a80');
  for(let x=-300;x<70;x+=16)for(let z=-52;z>-220;z-=18){if(rnd()<.75)box(g,10+rnd()*4,6+rnd()*26,10+rnd()*4,M(['#d8d2c6','#c9ced4','#e8e1d4','#b8b0a0'][(rnd()*4)|0]),x,0,z);}
  const lane=new T.Group();lane.userData.pass=1;const LP=[[20,.4,50],[0,2,20],[-30,6,4],[-60,10,-4],[-90,13,-2],[-120,15,2],[-150,16,0],[-180,16,-8],[-205,16,-20]];
  for(let i=0;i<LP.length-1;i++){const a=LP[i],b=LP[i+1],dx=b[0]-a[0],dz=b[2]-a[2],L2=Math.hypot(dx,dz),y=Math.min(a[1],b[1]);box(lane,L2+6,y,8,M('#b8b0a0'),(a[0]+b[0])/2,0,(a[2]+b[2])/2,-Math.atan2(dz,dx));}g.add(lane);
  const lp=(x,k)=>{for(let i=0;i<LP.length-1;i++){const a=LP[i],b=LP[i+1];if(x<=a[0]&&x>=b[0]){const f=(a[0]-x)/((a[0]-b[0])||1);return a[k]+(b[k]-a[k])*f;}}return LP[LP.length-1][k];};
  for(let r=0;r<4;r++)for(let x=-26;x>-200;x-=5.8+rnd()*1.6){const up=r<3,z=lp(x,2)+(up?9.5+r*8.5:-9.5),y0=lp(x,1),base=up?y0-1.5+r*4.2:Math.max(0,y0-6),h=3.2+rnd()*2.2;if(base>0)box(g,5.4,base,5,M('#a89f90'),x,0,z);gHouse(g,x,base,z,4.4+rnd()*1.2,h,4.6,GPAL[((x*7|0)+r*3+100)%10],0);}
  box(g,24,1.1,.2,M('#5a4a3a'),-196,16,-24.6);label(g,'수암골 · SUAMGOL',-120,21.6,12.4,Math.PI,12,'#fff','#c8202a');
  P=pathFromXZ(LP);ex=[];
  notes=[[0,L('Suamgol, on the slopes of Uamsan. Free and always open, but people live here: please avoid visiting after 21:00.','우암산 자락의 수암골이에요. 입장 무료, 늘 열려 있지만 주민이 사는 곳이라 21시 이후 방문은 삼가요.')],[.35,L('Refugees settled here after the Korean War. In 2007 a public art project painted murals on the walls and brought the village back to life.','6·25 전쟁 뒤 피란민이 모여 살던 마을이에요. 2007년 공공미술 프로젝트로 담장에 벽화를 그리며 다시 살아났어요.')],[.7,L('It became known as a TV drama filming location; cafés now stand on former sets. At sunset, central Cheongju spreads out below.','드라마 촬영지로 알려졌고, 촬영 세트 자리에 카페와 식당이 들어섰어요. 해 질 녘이면 청주 시내가 내려다보여요.')]];}
 if(city==='cjk'){fac=modern;off=16;hh=[8,22];W=10;nP=30;words=['카페 CAFE','편의점','약국','서점 BOOKS','인쇄 PRINT'];
  tHall(g,-40,0,-36,22,12,0,'#c8b89a');label(g,'청주고인쇄박물관 · EARLY PRINTING MUSEUM',-40,11.4,-29.4,0,20,'#fff','#5a3a26');
  box(g,70,18,26,M('#d9d2c4'),-150,0,32);box(g,70.6,.8,26.6,M('#8a8f96'),-150,18,32);for(let i=-3;i<=3;i++)box(g,6,8,.2,M('#3a4a5a',{emissive:'#0c141c'}),-150+i*9.5,4,18.9);
  label(g,'MMCA 국립현대미술관 청주',-150,21.6,18.6,Math.PI,22,'#fff','#2e5a86');
  box(g,46,9,18,M('#e8e1d4'),-240,0,-30);label(g,'청주고속버스터미널 · EXPRESS BUS TERMINAL',-240,10.6,-20.8,0,22,'#fff','#2e5a86');for(let i=0;i<3;i++)busA(g,-222-i*12,-12,0,['#2e5a86','#c8202a','#2fae6a'][i%3]);
  P=pathFromXZ([[0,0,60],[0,0,20],[-20,0,0],[-60,0,-6],[-110,0,-4],[-160,0,4],[-210,0,0],[-250,0,-6]]);ex=[[-40,-34,24],[-150,32,44],[-240,-28,32]];
  notes=[[0,L('Cheongju Early Printing Museum: the story of Jikji and Heungdeoksa, the Cheongju temple where it was printed. Free; 09:00–18:00; closed Mondays and 1 January.','청주고인쇄박물관이에요. 직지와, 직지를 찍은 청주 흥덕사 이야기를 보여 줘요. 입장 무료, 09:00~18:00, 매주 월요일과 1월 1일 휴관.')],[.45,L('MMCA Cheongju is in Naedeok-dong, in the old Cheongju tobacco factory: take a taxi or bus between the two. Floors 1–4 free (5th-floor shows ₩2,000); 10:00–18:00, last entry 17:00; closed Mondays.','국립현대미술관 청주는 내덕동, 옛 청주 연초제조창 건물에 있어요. 두 곳 사이는 택시나 버스로 가요. 1~4층 무료(5층 기획전 2,000원), 10:00~18:00(입장 17:00까지), 월요일 휴관.')],[.85,L('Cheongju Express Bus Terminal: 76 buses a day to Seoul Express Bus Terminal, about 2 h 4 min.','청주고속버스터미널이에요. 서울고속버스터미널 가는 버스가 하루 76회, 약 2시간 4분 걸려요.')]];}
