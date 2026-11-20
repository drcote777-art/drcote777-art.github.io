 if(city==='gmp'||city==='gmpa'){W=10;nP=40;ground(g,520,320,-100,-60,'#a8aaa4');
  box(g,130,16,30,M('#dfe6ec'),-60,0,-44);box(g,128,10,.4,M('#7fa3bf',{transparent:true,opacity:.6}),-60,2,-28.8);box(g,134,1.2,34,M('#8a96a2'),-60,16,-44);
  label(g,'김포공항 국내선 · GIMPO DOMESTIC',-60,18.8,-28.4,0,44,'#fff','#2e5a86');
  box(g,12,4.4,.4,M('#1d2a36',{emissive:'#0a1018'}),-34,6,-27.6);label(g,city==='gmp'?RGN.flt:RGN.arr,-34,8.9,-27.3,0,11,'#ffd84a','#1d2a36');label(g,city==='gmp'?'출발 DEPARTURES':'도착 ARRIVALS',-34,7,-27.3,0,11,'#fff','#1d2a36');
  for(let i=0;i<4;i++){box(g,1.6,1.2,1,M('#2e5a86'),-70-i*3,0,-26.5);label(g,'체크인',-70-i*3,1.6,-25.95,0,2.4,'#fff','#2e5a86');}
  jet(g,-70,0,-95,0,'#2e5a86');jet(g,-130,0,-100,.25,'#c8202a');jet(g,-10,0,-104,-.2,'#f08a24');jet(g,-200,60,-260,.6,'#2fa39a');
  for(const x of[-140,-100,-40,0])box(g,2,6,14,M('#c9ced4'),x,0,-66);
  P=pathFromXZ([[0,0,70],[0,0,30],[-10,0,0],[-40,0,-16],[-80,0,-20],[-120,0,-22],[-160,0,-24]]);ex=[];
  notes=city==='gmp'?[[0,RGN.gmp0],[.4,L('Domestic flights to Jeju leave all day: about 105 a day (Nov 2026). Check in on your airline’s app or at the counter.','제주 가는 국내선이 하루 종일 떠나요. 하루 약 105편(2026년 11월 기준). 항공사 앱이나 카운터에서 체크인해요.')],[.75,L('Bring your ID: domestic flights check it at the gate.','신분증을 꼭 챙겨요. 국내선도 탑승구에서 확인해요.')]]
   :[[0,L('Gimpo Airport, domestic arrivals. Welcome back to Seoul!','김포공항 국내선 도착이에요. 서울에 돌아왔어요!')],[.5,L('From Gimpo Airport Station: subway Lines 5 and 9, the AREX, the Seohae Line and the Gimpo Goldline.','김포공항역에서 지하철 5·9호선, 공항철도, 서해선, 김포골드라인으로 갈아타요.')]];}
 if(city==='cju'){W=10;nP=40;ground(g,520,320,-100,-60,'#a8aaa4');
  box(g,140,15,30,M('#e8eef2'),-80,0,-46);box(g,138,9,.4,M('#7fa3bf',{transparent:true,opacity:.6}),-80,2,-30.8);box(g,144,1.2,34,M('#2e8fd0'),-80,15,-46);
  label(g,'제주국제공항 · JEJU INTERNATIONAL AIRPORT',-80,17.8,-30.4,0,50,'#fff','#2e8fd0');
  jet(g,-60,0,-100,0,'#f08a24');jet(g,-130,0,-104,.2,'#2e5a86');jet(g,-200,70,-300,-.5,'#c8202a');
  for(let x=-150;x<=10;x+=16){palm(g,x,-24,8+rnd()*3);}for(let z=0;z<80;z+=14){palm(g,-9,z,8+rnd()*2);palm(g,9,z+7,8+rnd()*2);}
  dolHar(g,-48,-23,1.1);dolHar(g,-54,-23,1.1);
  box(g,6,3,3,M('#f4f6f7'),12,0,-6);label(g,RGN.bus,12,3.8,-4.45,0,12,'#fff','#2e8fd0');
  batDam(g,[20,10],[20,80]);batDam(g,[-20,10],[-20,80]);
  P=pathFromXZ([[-160,0,-22],[-120,0,-20],[-80,0,-18],[-40,0,-14],[-6,0,0],[0,0,30],[0,0,60],[0,0,90]]);ex=[];
  notes=[[0,L('Jeju International Airport. Flights from Gimpo take about 1 h 10 min.','제주국제공항이에요. 김포에서 비행기로 약 1시간 10분이에요.')],[.45,L('The stone grandfathers are dol hareubang, carved from Jeju’s black volcanic basalt.','돌 할아버지는 돌하르방이에요. 제주의 검은 현무암으로 깎았어요.')],[.75,L('Buses leave from the stops outside. Local buses ₩1,150 by card, any distance; airport limousine 600 to Seogwipo ₩5,500.','버스는 바깥 정류장에서 타요. 시내·간선버스 교통카드 1,150원(거리 상관없음), 서귀포 가는 공항리무진 600번 5,500원.')]];}
 if(city==='ydm'){seaY=-1.2;W=7;nP=26;ground(g,700,220,-40,-130,'#8f8a7a');
  for(let x=-150;x<120;x+=14)rocks(g,x,-14,2,1.6);dragonRock(g,-30,16,1);
  deck(g,[80,0,-27],[-150,0,-27],6,'#8a8070');batDam(g,[90,-34],[-160,-34]);
  for(let x=-140;x<100;x+=22){if(rnd()<.7)palm(g,x+rnd()*6,-40-rnd()*10,7+rnd()*3);}
  for(let i=0;i<4;i++)fBoat(g,-120+i*70,90+rnd()*60,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  jet(g,20,55,-120,2.6,'#2e5a86');
  box(g,.4,5,.4,M('#5a4a3a'),-10,0,-31);label(g,'용두암 · YONGDUAM',-10,5.6,-30.7,0,12,'#fff','#2f2d2a');
  P=pathFromXZ([[70,0,-40],[40,0,-30],[10,0,-27],[-20,0,-27],[-50,0,-27],[-90,0,-28],[-130,0,-30]]);ex=[];
  notes=[[0,L('Yongduam, the Dragon Head Rock, on the north coast close to the airport. Free and open all the time.','용두암이에요. 공항 가까운 북쪽 바닷가에 있어요. 입장 무료, 늘 열려 있어요.')],[.45,L('Legend: a dragon stole a jewel from the spirit of Hallasan and was shot down into the sea, its head turned to stone.','전설: 한라산 신령의 구슬을 훔친 용이 화살을 맞고 바다에 떨어져 머리가 돌이 됐대요.')],[.8,L('The waves and wind carved the black basalt into this shape. Planes fly low overhead to the airport.','파도와 바람이 검은 현무암을 이 모양으로 깎았어요. 머리 위로 공항에 내리는 비행기가 낮게 지나가요.')]];}
 if(city==='dmm'){fac=modern;off=13;hh=[8,16];W=9;nP=56;words=['감귤 TANGERINES','흑돼지 BLACK PORK','갈치 CUTLASSFISH','오메기떡 OMEGI','회 SASHIMI','한라봉 HALLABONG'];
  for(const x of[-6,6])box(g,.8,8,.8,M('#2e5a86'),x,0,44);box(g,13,1.6,1,M('#2e5a86'),0,8,44);label(g,'동문재래시장 · DONGMUN MARKET',0,8.8,44.6,0,12,'#fff','#2e5a86');
  box(g,9,.25,120,M('#c8d4dc',{transparent:true,opacity:.55}),0,7.5,-20);
  for(let z=30;z>-80;z-=7){stall(g,-4.2,z,Math.PI/2,['#e8604c','#f2b134','#2fa39a'][(z/7|0)%3]);if(rnd()<.6)stall(g,4.2,z-3,-Math.PI/2,['#4f74d6','#e9873c','#3fa865'][(z/7|0)%3]);}
  for(let z=-92;z>-140;z-=6){stall(g,-4.4,z,Math.PI/2,'#c8202a');stall(g,4.4,z-3,-Math.PI/2,'#f0c419');sph(g,.4,M('#ffe6a0',{emissive:'#ffcf60'}),0,6.2,z);}
  label(g,'야시장 NIGHT MARKET · 8번 GATE 8',0,7.6,-88,0,12,'#fff','#c8202a');
  box(g,3,2.6,1,M('#2e5a86'),7,0,58);label(g,'정류장 · BUS STOP',7,3.2,58.6,0,6,'#fff','#2e5a86');
  P=pathFromXZ([[0,0,64],[0,0,40],[0,0,10],[0,0,-30],[0,0,-70],[0,0,-110],[0,0,-140]]);ex=[[0,0,60]];
  notes=[[0,L('Dongmun Market, Jeju’s big traditional market. Open every day, about 07:00–21:00 (each shop differs).','동문재래시장이에요. 제주에서 가장 큰 전통시장이에요. 연중무휴, 약 07:00~21:00(가게마다 달라요).')],[.4,L('Try tangerines and hallabong, fresh cutlassfish (galchi), black pork and omegi rice cakes.','감귤과 한라봉, 싱싱한 갈치, 흑돼지, 오메기떡을 맛봐요.')],[.7,L('From about 18:00 the night market near Gate 8 fills with food stalls.','저녁 6시쯤부터 8번 게이트 근처 야시장에 먹거리 노점이 가득해요.')]];}
 if(city==='ssi'){seaY=-1.2;W=7;nP=26;ground(g,420,200,0,110,'#8f9a6a');ground(g,70,40,0,-4,'#8f9a6a');
  tuffCone(g,0,-80,60,40);
  for(let i=0;i<22;i++){const t=i/22,y=t*40.6,z=-14-t*23;box(g,4,.3,1.2,M('#8a8070'),0,y,z);}
  box(g,4,2.6,3,M('#e8e1d4'),7,0,8);label(g,'매표소 TICKETS',7,3.2,9.6,0,6,'#fff','#2f5a2e');
  box(g,.4,5,.4,M('#5a4a3a'),-9,0,20);label(g,'성산일출봉 · SEONGSAN ILCHULBONG',-9,5.6,20.3,0,18,'#fff','#2f5a2e');
  for(let x=-120;x<120;x+=10){if(Math.abs(x)<16)continue;gHouse(g,x,0,60+rnd()*40,6+rnd()*3,4+rnd()*3,6,GPAL[(rnd()*10)|0]);}
  batDam(g,[-14,30],[-14,100]);batDam(g,[14,30],[14,100]);
  box(g,3,2.6,1,M('#2e5a86'),9,0,96);label(g,'정류장 · BUS STOP',9,3.2,96.6,0,6,'#fff','#2e5a86');
  for(let i=0;i<5;i++)fBoat(g,80+i*25,-40-rnd()*60,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  P=pathFromXZ([[0,0,104],[0,0,70],[0,0,30],[0,0,0],[0,0,-14],[0,16.5,-21.5],[0,34.5,-29.8],[0,40.6,-33],[0,41,-37]]);ex=[];
  notes=[[0,L('Seongsan Ilchulbong, “Sunrise Peak”: a tuff cone rising from the sea, part of Jeju’s UNESCO World Natural Heritage.','성산일출봉이에요. 바다에서 솟은 응회구로, 제주 유네스코 세계자연유산이에요.')],[.4,L('Adult ₩5,000. Nov–Feb 06:00–18:00 (tickets until 17:00). Closed on the first Monday of each month.','어른 5,000원. 11~2월 06:00~18:00(매표 17:00까지). 매달 첫째 월요일 휴무.')],[.55,L('Steep stairs: about 20–30 minutes to the top, about 50 minutes up and down.','계단이 가팔라요. 정상까지 약 20~30분, 왕복 약 50분.')],[.97,L('The bowl-shaped crater from the rim, about 180 m above the sea.','분화구 가장자리에서 본 그릇 모양 분화구예요. 해발 약 180m.')]];}
 if(city==='cjy'){W=6;nP=26;ground(g,300,340,0,-60,'#6f7a58');
  for(const s of[-1,1]){box(g,10,24,200,M('#5f5a50'),s*15,0,-60);for(let z=30;z>-150;z-=12){if(rnd()<.7)pineAt(g,s*(13+rnd()*6),24,z+rnd()*6,.5);if(rnd()<.4)palm(g,s*(11+rnd()*2),z+rnd()*6,6+rnd()*3);}}
  box(g,6,.2,190,M('#3f8aa0',{emissive:'#0a2a33'}),6,-.05,-60);
  waterfall(g,4,-152,22,9);
  for(let z=30;z>-130;z-=10){cyl(g,.08,.08,2.4,M('#555'),-3.6,0,z,5);sph(g,.32,M('#ffe6a0',{emissive:'#ffcf60'}),-3.6,2.6,z);}
  box(g,4,2.6,3,M('#e8e1d4'),-6,0,46);label(g,'매표소 TICKETS',-6,3.2,47.6,0,6,'#fff','#2f5a2e');
  box(g,.4,5,.4,M('#5a4a3a'),3,0,40);label(g,'천지연폭포 · CHEONJIYEON FALLS',3,5.6,40.3,0,16,'#fff','#2f5a2e');
  P=pathFromXZ([[0,0,60],[0,0,30],[0,0,0],[-1,0,-40],[-1,0,-80],[-1,0,-115],[-2,0,-130]]);ex=[];
  notes=[[0,L('Cheonjiyeon Falls, Seogwipo. Adult ₩2,000. Open every day 09:00–22:00 (last entry 21:20).','서귀포 천지연폭포예요. 어른 2,000원. 연중무휴 09:00~22:00(입장 마감 21:20).')],[.45,L('A green gorge path with subtropical plants. The valley is a habitat of the dampalsu tree and the giant mottled eel, both natural monuments.','아열대 식물 사이 협곡 길이에요. 담팔수 자생지와 무태장어 서식지로, 둘 다 천연기념물이에요.')],[.9,L('The waterfall pours into a deep pool. Lights along the path make it a good evening walk.','폭포가 깊은 소로 떨어져요. 길에 조명이 있어 저녁 산책도 좋아요.')]];}
 if(city==='odg'){seaY=-1.2;W=6;nP=22;box(g,520,13.2,240,M('#4a463f'),0,-1.2,-150);ground(g,520,240,0,-150,'#7f8f5a',12);
  seaStack(g,-6,14,20);for(let x=-200;x<200;x+=20)rocks(g,x,-28,2,1.8);
  for(let x=-150;x<130;x+=9){if(rnd()<.8)pineAt(g,x+rnd()*4,12,-56-rnd()*40,.5);}
  rail(g,[80,12,-34],[-120,12,-34],0);
  for(let x=60;x>-100;x-=12){box(g,.12,.6,.12,M('#2e8fd0'),x,13.2,-35);box(g,.12,.6,.12,M('#f39a1e'),x+.3,13.2,-35);}
  box(g,.3,3,.3,M('#5a4a3a'),62,12,-44);label(g,'올레 7코스 · OLLE ROUTE 7',62,15.6,-43.7,0,10,'#fff','#2e8fd0');
  box(g,.4,5,.4,M('#5a4a3a'),-4,12,-36.5);label(g,'외돌개 · OEDOLGAE',-4,17.6,-36.2,0,10,'#fff','#2f2d2a');
  box(g,3,2.6,1,M('#2e8fd0'),70,12,-52);label(g,'리무진 600 · LIMOUSINE',70,15.2,-51.4,0,8,'#fff','#2e8fd0');
  for(let i=0;i<4;i++)fBoat(g,-160+i*90,80+rnd()*50,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  P=pathFromXZ([[76,12,-50],[50,12,-42],[20,12,-39],[-4,12,-38],[-30,12,-40],[-60,12,-44],[-90,12,-48]]);ex=[];
  notes=[[0,L('Oedolgae, Seogwipo: a lone sea stack about 20 m tall. Free and always open; best before sunset.','서귀포 외돌개예요. 바다에 홀로 선 약 20m 돌기둥이에요. 입장 무료, 늘 열려 있고 해 지기 전에 가는 게 좋아요.')],[.4,L('Also called the General Rock: legend says General Choe Yeong dressed it up as a giant soldier to scare off the enemy.','장군석이라고도 불러요. 최영 장군이 이 바위를 장군처럼 꾸며 적을 물리쳤다는 이야기가 전해요.')],[.7,L('Jeju Olle Route 7 starts here: follow the blue and orange ribbons along the cliffs.','제주 올레 7코스가 여기서 시작해요. 파랑·주황 리본을 따라 절벽 길을 걸어요.')]];}
