 if(city==='gsj'){fac=modern;off=15;hh=[10,26];W=10;nP=34;words=['편의점','커피 COFFEE','떡갈비','약국','관광안내 INFO'];
  const pl=new T.Group();pl.userData.pass=1;box(pl,130,1,8,M('#b9b4aa'),-10,0,60);const kt=mkKTX(110);kt.position.set(-10,1,52.4);pl.add(kt);g.add(pl);
  const st=new T.Group();st.userData.pass=1;box(st,60,12,28,new T.MeshPhongMaterial({color:'#a9c4d8',specular:'#ffffff',shininess:90,transparent:true,opacity:.6}),-20,0,26);box(st,64,1.2,32,M('#e9edf0'),-20,12,26);g.add(st);
  label(g,'광주송정역 GWANGJU SONGJEONG',-20,15.4,42.2,0,30,'#fff','#2e5a86');
  box(g,5,3,4,M('#f4f6f7'),-62,0,-40);label(g,'M 지하철 1호선 · METRO LINE 1',-62,4.2,-37.9,0,12,'#fff','#2e5a86');
  P=pathFromXZ([[40,1,60],[0,1,60],[-20,0,40],[-20,0,10],[-24,0,-14],[-60,0,-26],[-110,0,-30]]);ex=[[-10,60,70],[-20,26,44],[-62,-40,10]];
  notes=[[0,L('Gwangju Songjeong Station: KTX trains from Seoul arrive here.','광주송정역이에요. 서울에서 온 KTX가 여기 도착해요.')],[.45,L('Since 1 July 2026, Gwangju and Jeonnam are one city: the Jeonnam-Gwangju Integrated Special City.','2026년 7월 1일부터 광주와 전남이 하나로 합쳐 전남광주통합특별시가 됐어요.')],[.75,L('Subway Line 1 runs from this station into downtown Gwangju.','이 역에서 지하철 1호선을 타고 광주 시내로 가요.')]];}
 if(city==='acc'){fac=modern;off=24;hh=[10,24];W=10;nP=36;words=['카페 CAFE','편의점','약국','은행 BANK','서점 BOOKS'];
  fountain(g,-45,-24,9);clockTower(g,-22,-26);label(g,'5·18 민주광장 · MAY 18 DEMOCRACY SQUARE',-45,8.6,-13.6,0,20,'#fff','#2a2a3a');
  const bp=new T.Group();bp.userData.pass=1;box(bp,6,.6,6,M('#b8b0a0'),0,0,0);for(const a of[-2.2,2.2])for(const b of[-2.2,2.2])cyl(bp,.22,.22,3.4,KRED,a,.6,b,8);hanokRoof(bp,6,6,0,4,0);cyl(bp,1,1.3,1.8,M('#7a5a2a',{emissive:'#1a1006'}),0,1.8,0,14);bp.position.set(-70,0,-34);g.add(bp);label(g,'민주의 종 · BELL OF DEMOCRACY',-70,7.4,-30.6,0,11,'#fff','#5a3a26');
  provOffice(g,-100,-52,0);label(g,'옛 전남도청 · OLD PROVINCIAL OFFICE',-100,11.2,-45.2,0,18,'#fff','#2a2a3a');
  accRoof(g,-160,-72);label(g,'ACC 국립아시아문화전당',-160,4.4,-46.4,0,16,'#fff','#2e5a86');
  P=pathFromXZ([[0,0,60],[0,0,20],[-20,0,0],[-60,0,-6],[-100,0,-10],[-140,0,-24],[-180,0,-32]]);ex=[[-45,-24,16],[-22,-26,8],[-70,-34,9],[-100,-52,26],[-160,-72,52]];
  notes=[[0,L('Out of Munhwajeondang Station: the May 18 Democracy Square is right in front of you.','문화전당역에서 나왔어요. 바로 앞이 5·18민주광장이에요.')],[.25,L('The fountain and the clock tower are kept as they were in May 1980, when citizens gathered here.','분수대와 시계탑은 시민들이 모였던 1980년 5월 모습 그대로 남아 있어요.')],[.5,L('The Old South Jeolla Provincial Office, the last stand of the uprising, was restored and opened to the public on 18 May 2026.','옛 전남도청은 5·18의 마지막 항쟁지예요. 2026년 5월 18일 복원해서 시민에게 문을 열었어요.')],[.8,L('The Asia Culture Center (ACC) is built into the ground, with a park on its roof. Indoors usually 10:00–18:00; closed Mondays.','국립아시아문화전당(ACC)은 땅을 파서 지은 건물이라 지붕 위가 공원이에요. 실내는 보통 10:00~18:00, 월요일 휴관.')]];}
 if(city==='dmy'){W=6;nP=24;box(g,800,.1,800,M('#5f6f3f'),-120,-.1,0);
  const gt=new T.Group();gt.userData.pass=1;for(const x of[-5,5])cyl(gt,.4,.4,7.4,KRED,x,0,40,8);hanokRoof(gt,11,3,0,7.4,40);g.add(gt);label(g,'죽녹원 JUKNOKWON',0,9.6,41.7,0,10,'#fff','#2f5a2e');
  box(g,4,3,3,M('#efe9dc'),12,0,50);label(g,'매표소 TICKETS',12,3.6,51.6,0,6,'#fff','#2e5a86');
  for(const [x,z] of[[-2,-14],[14,2],[-30,-24],[-30,14],[-55,-28],[-58,8],[-85,-34],[-100,12],[-115,-24],[-20,28],[16,26]])bambooGreen(g,x,z,20,7);
  jPavilion(g,-80,0,-24);
  box(g,210,1,10,M('#7a7a5a'),-225,0,22);box(g,260,.1,30,M('#5f9fb8',{emissive:'#10303c'}),-220,-.05,46);
  for(let x=-150;x>-320;x-=17){oldTree(g,x,15,.9);oldTree(g,x-8,29.5,.8);}label(g,'관방제림 GWANBANGJERIM',-200,7.6,16.4,0,14,'#fff','#2f5a2e');
  P=pathFromXZ([[0,0,60],[0,0,20],[-20,0,0],[-50,0,-10],[-80,0,-14],[-110,0,-6],[-140,0,10],[-170,1,22],[-220,1,22],[-262,1,22]]);ex=[];
  notes=[[0,L('Juknokwon bamboo forest: adult ₩3,000. Nov–Feb 09:00–18:00 (last entry 17:30). Open every day.','죽녹원이에요. 어른 3,000원, 11~2월 09:00~18:00(입장 마감 17:30). 연중무휴.')],[.3,L('Eight themed walking paths wind through the bamboo: 2.2 km in all.','대숲 사이로 8가지 주제의 산책로가 이어져요. 모두 2.2km.')],[.72,L('Gwanbangjerim: trees planted along the river bank from 1648 to hold back floods. About 2 km, 185 trees, most over 300 years old.','관방제림이에요. 1648년 홍수를 막으려고 둑에 심기 시작한 숲이에요. 약 2km에 185그루, 대부분 300살이 넘어요.')]];}
 if(city==='scw'){W=6;nP=26;box(g,1200,.1,1200,M('#5c584c'),-150,-.1,-150);
  for(const [x,z,w] of[[-80,-32,150],[-85,38,130],[-140,-55,90]])box(g,w,.12,7,M('#5a8aa8',{emissive:'#10283a'}),x,-.05,z);
  reeds(g,-175,8,-62,-9,240);reeds(g,-175,-25,26,58,190);
  const pts=[[0,0,30],[-20,0,10],[-60,0,16],[-100,0,0],[-140,0,14],[-170,0,0]];for(let i=0;i<pts.length-1;i++)deck(g,pts[i],pts[i+1],4.4,'#b08a5a');
  const C=[-215,-58],R=40,H=16;cone(g,R,H,M('#5f6f45'),C[0],0,C[1],28);
  const ob=new T.Group();ob.userData.pass=1;box(ob,11,.5,11,M('#8a6a4a'),C[0],H-.9,C[1]);for(const a of[-5.2,5.2]){box(ob,.2,1.1,10.6,M('#6a5040'),C[0]+a,H-.4,C[1]);box(ob,10.6,1.1,.2,M('#6a5040'),C[0],H-.4,C[1]+a);}g.add(ob);
  box(g,.3,4,.3,M('#6a5040'),C[0]+4,H-.4,C[1]+6);label(g,'용산전망대 · YONGSAN OBSERVATORY',C[0]+4,H+4.6,C[1]+6.2,0,10,'#fff','#5a3a26');
  for(const x of[-8,8])box(g,.5,11,.5,M('#6a5040'),x,0,40);label(g,'순천만습지 · SUNCHEONMAN BAY',0,9.4,40.4,0,16,'#fff','#5a3a26');
  box(g,4,3,3,M('#efe9dc'),12,0,50);label(g,'매표소 TICKETS',12,3.6,51.6,0,6,'#fff','#2e5a86');
  const e=(d)=>[C[0]+d*.613,coneY(C[0],C[1],R,H,C[0]+d*.613,C[1]+d*.79),C[1]+d*.79];
  P=pathFromXZ([[0,0,60],[0,0,30],[-20,0,10],[-60,0,16],[-100,0,0],[-140,0,14],[-170,0,0],e(40),e(22),e(8),e(1)]);ex=[];
  notes=[[0,L('Suncheonman Bay Wetland: your Suncheonman Bay National Garden ticket (adult ₩10,000) lets you in on the same day.','순천만습지예요. 순천만국가정원 입장권(어른 10,000원)으로 같은 날 들어와요.')],[.3,L('A wooden boardwalk crosses the mud flats through the reeds. In autumn the reeds turn gold.','갯벌 위 나무 데크길이 갈대밭 사이로 이어져요. 가을엔 갈대가 황금빛이에요.')],[.65,L('From the trail entrance to the Yongsan Observatory: about 1.5 km, a 25–30 minute walk.','탐방로 입구에서 용산전망대까지 약 1.5km, 걸어서 25~30분이에요.')],[.99,L('Yongsan Observatory: the S-shaped channels and reed fields below, famous at sunset.','용산전망대예요. S자 물길과 갈대밭, 해 질 녘 노을이 유명해요.')]];}
 if(city==='odo'){seaY=-1.2;ground(g,700,320,-100,-160,'#b9ad98');W=7;nP=30;
  const pf=new T.Group();pf.userData.pass=1;box(pf,120,1,6,M('#b9b4aa'),20,0,-40);g.add(pf);for(const z of[-44.4,-45.6])box(g,300,.2,.2,M('#6a6f76'),20,0,z);const kt=mkKTX(80);kt.position.set(30,.2,-45);g.add(kt);
  box(g,40,10,16,M('#eef1f4'),10,0,-62);label(g,'여수EXPO역 · YEOSU EXPO',10,11.4,-53.9,0,20,'#fff','#2e5a86');
  deck(g,[-50,0,-4],[-158,0,65],10,'#b8b2a6');for(const s of[-1,1]){const o=box(g,128,.8,.4,M('#d8d4cc'),-104+s*4.6*.538,0,30.5+s*4.6*.842);o.rotation.y=-Math.atan2(69,-108);}
  tram(g,-86.2,23.2,-Math.atan2(69,-108)+Math.PI);label(g,'동백열차 · CAMELLIA TRAIN',-92,6.2,27.4,2.14,10,'#fff','#3fa865');
  const C=[-205,85],R=34,H=8;cone(g,R,H,M('#3f6a3a'),C[0],0,C[1],28);const cy=(x,z)=>coneY(C[0],C[1],R,H,x,z);
  for(let i=0;i<26;i++){const a=rnd()*6.28,d=6+rnd()*24,x=C[0]+Math.cos(a)*d,z=C[1]+Math.sin(a)*d;if(Math.abs((x-C[0])*.414+(z-C[1])*.911)<4&&(x-C[0])>-2)continue;camellia(g,x,z,cy(x,z));}
  lighthouse(g,-218,cy(-218,94),94);label(g,'오동도 ODONGDO',-170,6.4,66,Math.PI*.62,10,'#fff','#2f5a2e');
  for(let i=0;i<6;i++)fBoat(g,-40-i*30,90+rnd()*40,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  P=pathFromXZ([[60,1,-40],[20,1,-40],[0,0,-20],[-30,0,-12],[-50,0,-4],[-80,0,15.2],[-150,0,60],[-174,cy(-174,71),71],[-190,cy(-190,78),78],[-203,cy(-203,84),84]]);ex=[];
  notes=[[0,L('Yeosu EXPO Station. Odongdo and the Jasan cable car station are close by.','여수EXPO역이에요. 오동도와 해상케이블카 자산 정류장이 가까워요.')],[.45,L('The breakwater road to Odongdo. You can also ride the Camellia Train: ₩1,000 one way.','오동도로 가는 방파제 길이에요. 동백열차(편도 1,000원)를 타도 돼요.')],[.8,L('Odongdo is free and always open. Camellias start to bloom in mid-February and are at their best in mid-March.','오동도는 입장 무료, 늘 열려 있어요. 동백꽃은 2월 중순부터 피기 시작해 3월 중순에 가장 많이 펴요.')],[.97,L('The white Odongdo Lighthouse stands at the southern tip of the island.','섬 남쪽 끝에는 하얀 오동도 등대가 있어요.')]];}
 if(city==='ycb'){seaY=-1.2;ground(g,500,200,0,-130,'#b9ad98');W=7;nP=22;
  const st=new T.Group();st.userData.pass=1;for(const a of[-8.5,8.5])for(const b of[-6.5,6.5])box(st,.6,9,.6,M('#d8dde2'),a,0,-36+b);box(st,19,.8,15,M('#c8202a'),0,9,-36);box(st,5,2.6,2,M('#f4f6f7'),-6,0,-41);g.add(st);label(g,'여수 해상케이블카 · 자산 정류장',0,11.6,-43.6,Math.PI,18,'#fff','#c8202a');
  const cb=new T.Group();cb.userData.pass=1;const c1=[new T.Vector3(-3,10,-34),new T.Vector3(-3,66,40),new T.Vector3(-3,70,240)],c2=c1.map(v=>new T.Vector3(3,v.y,v.z));
  for(const cs of[c1,c2])cb.add(new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(cs),40,.12,4,false),M('#3a3f45')));
  for(let i=0;i<7;i++){const z=-10+i*36,y=10+Math.min(1,(z+34)/74)*56;box(cb,2.4,2.6,2.4,M(i%2?'#c8202a':'#2e8fd0'),i%2?3:-3,y-3.4,z);}
  box(cb,5,.25,5,M('#bfe3f2',{transparent:true,opacity:.4}),0,59.75,43);for(const a of[-2.4,2.4])for(const b of[-2.4,2.4])box(cb,.15,3,.15,M('#c8202a'),a,60,43+b);box(cb,5.2,.3,5.2,M('#c8202a'),0,63,43);g.add(cb);
  cone(g,90,55,M('#3f6a3a'),0,0,250,24);for(let i=0;i<6;i++)fBoat(g,-60+i*24,60+rnd()*120,rnd()*3,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);
  for(let i=0;i<14;i++)pine(g,(i&1?1:-1)*(9+rnd()*22),-60-rnd()*40,.5);
  P=pathFromXZ([[0,0,-90],[0,0,-60],[0,0,-40],[0,30,0],[0,60,40],[0,60,44]]);ex=[];
  notes=[[0,L('Yeosu Maritime Cable Car, Jasan station: it crosses the sea to Dolsan.','여수 해상케이블카 자산 정류장이에요. 바다 건너 돌산까지 가요.')],[.3,L('Standard cabin: adult ₩17,000 round trip. The glass-floored Crystal cabin: ₩24,000.','일반 캐빈 어른 왕복 17,000원, 바닥이 투명한 크리스탈 캐빈은 24,000원이에요.')],[.97,L('High above the sea: boats pass under your feet.','바다 위 높은 곳이에요. 발밑으로 배가 지나가요.')]];}
