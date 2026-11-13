 if(city==='gns'){fac=modern;off=15;hh=[10,24];W=10;nP=34;words=['초당순두부','커피 COFFEE','감자옹심이','편의점','관광안내 INFO'];
  const pl=new T.Group();pl.userData.pass=1;box(pl,130,1,8,M('#b9b4aa'),-10,0,60);const kt=mkKTX(100);kt.position.set(-10,1,52.4);pl.add(kt);g.add(pl);
  const st=new T.Group();st.userData.pass=1;box(st,60,11,28,new T.MeshPhongMaterial({color:'#a9c4d8',specular:'#ffffff',shininess:90,transparent:true,opacity:.6}),-20,0,26);for(let i=0;i<5;i++){const w=box(st,13,.8,32,M('#e9edf0'),-46+i*13,11.6+(i%2)*.8,26);w.rotation.z=i%2?.06:-.06;}g.add(st);
  label(g,'강릉역 GANGNEUNG STATION',-20,14.6,40.6,0,28,'#fff','#2e5a86');busA(g,-62,-40,0,'#2fae6a','경포 · 안목');box(g,.3,3,.3,M('#5a6068'),-50,0,-33);label(g,'🚌 BUS',-50,3.4,-32.8,0,3,'#fff','#2fae6a');
  P=pathFromXZ([[40,1,60],[0,1,60],[-20,0,40],[-20,0,10],[-24,0,-14],[-60,0,-26],[-110,0,-30]]);ex=[[-10,60,70],[-20,26,44],[-62,-40,10]];
  notes=[[0,L('Gangneung Station: the KTX-Eum from Seoul Station arrives here.','강릉역이에요. 서울역에서 온 KTX-이음이 여기 도착해요.')],[.45,L('Trains to Jeongdongjin leave from here too: about 15 minutes.','정동진 가는 기차도 여기서 타요. 약 15분 걸려요.')],[.75,L('City buses and taxis go to Gyeongpo in about 10–15 minutes.','시내버스·택시로 경포까지 10~15분쯤 걸려요.')]];}
 if(city==='gyp'){seaY=-1.2;ground(g,1200,600,-200,-290,'#8f8f8c');box(g,360,.3,16,M('#ead9a8'),-130,-.25,18);box(g,360,.4,2,M('#c9ced4'),-130,0,9.6);W=8;nP=38;
  const hl=new T.Group();hl.userData.pass=1;hill(hl,18,-12,18,8,'#6f8a5a');const pv=mkPavilion();pv.position.set(18,7.2,-12);hl.add(pv);g.add(hl);label(g,'경포대 GYEONGPODAE',18,15.6,-17.9,Math.PI,12,'#fff','#7a2a1e');
  box(g,260,.08,120,M('#4f8fa8'),-170,0,-120);for(let i=0;i<26;i++)pine(g,-20-i*9,-16-rnd()*6,.55);
  for(let i=0;i<18;i++){const p=person(g,-30-rnd()*200,0,13+rnd()*8,CLOTH[(rnd()*9)|0],SKIN[(rnd()*4)|0],1);p.rotation.y=rnd()*6.28;list.push(p);}
  P=pathFromXZ([[0,0,-70],[0,0,-30],[-20,0,-6],[-60,0,4],[-120,0,6],[-180,0,6],[-240,0,4]]);
  notes=[[0,L('Gyeongpo. A bus or taxi from Gangneung Station takes about 10–15 minutes.','경포예요. 강릉역에서 버스나 택시로 10~15분쯤 걸려요.')],[.12,L('Gyeongpodae pavilion stands on a low hill over Gyeongpo Lake. Free to visit.','경포대 누각이 경포호 옆 언덕 위에 있어요. 무료예요.')],[.5,L('Gyeongpo Beach: a long sandy beach backed by pine trees.','소나무 숲 뒤로 길게 펼쳐진 경포해변이에요.')]];}
 if(city==='anm'){seaY=-1.2;ground(g,1200,600,-200,-290,'#8f8f8c');box(g,360,.3,16,M('#ead9a8'),-130,-.25,18);box(g,360,.4,2,M('#c9ced4'),-130,0,9.6);W=8;nP=34;
  const cs=['#c8202a','#2e5a86','#2fae6a','#f0c419','#8a4fd0','#e9873c'];for(let x=-20,i=0;x>-240;x-=13,i++){const h=7+rnd()*12;bld(g,x,-14,11,h,10,0,facade('cf'+(i%3),['#efe9df','#e0d6c4','#d9dde2'][i%3],{rows:Math.max(2,h/3.5|0),cols:3,glass:'#7a9cb0'}));label(g,['카페 CAFE','COFFEE ☕','ROASTERY','BAKERY · CAFE'][i%4],x,h*.55,-8.9,0,8,'#fff',cs[i%6]);}
  for(let i=0;i<14;i++){const p=person(g,-30-rnd()*200,0,13+rnd()*8,CLOTH[(rnd()*9)|0],SKIN[(rnd()*4)|0],1);p.rotation.y=Math.PI*(.8+rnd()*.4);list.push(p);}
  P=pathFromXZ([[0,0,-50],[0,0,-4],[-60,0,4],[-130,0,6],[-200,0,4],[-240,0,-6]]);
  notes=[[0,L('Anmok Beach: Gangneung\'s coffee street, with cafés lined up along the shore.','안목해변 커피거리예요. 바닷가를 따라 카페가 줄지어 있어요.')],[.5,L('Pick a café with a sea view and try a hand-drip coffee.','바다가 보이는 카페에서 핸드드립 커피를 마셔 봐요.')]];}
 if(city==='ojk'){W=6;nP=24;
  const gt=new T.Group();gt.userData.pass=1;for(const x of[-5,5])cyl(gt,.4,.4,7.4,KRED,x,0,30,8);hanokRoof(gt,11,3,0,7.4,30);g.add(gt);label(g,'오죽헌 OJUKHEON',0,9.6,31.7,0,9,'#fff','#2a2018');for(const sx of[-1,1]){box(g,30,2.2,.8,M('#d8cfc0'),sx*21,0,30);box(g,30.6,.4,1.4,KHAN,sx*21,2.2,30);}
  box(g,4,3,3,M('#efe9dc'),12,0,42);label(g,'매표소 TICKETS',12,3.6,43.6,0,6,'#fff','#2e5a86');
  hanok(g,-50,0,-22,12,8,0);hanok(g,-92,0,-24,10,7,0);hanok(g,-118,0,10,9,7,0);hanok(g,-30,0,14,8,6,0);hanok(g,-76,0,17,10,7,0);hanok(g,-128,0,-30,9,7,0);hanok(g,-168,0,-9,12,8,0);bamboo(g,-170,-30,20,7);bamboo(g,-160,14,16,6);label(g,'몽룡실 · 율곡 이이 태어난 곳',-50,4.6,-17.9,0,12,'#fff','#2a2018');
  for(const [x,z] of[[-50,-36],[-92,-38],[-140,-28],[-20,-24],[-70,16]])bamboo(g,x,z,26,7);
  for(let i=0;i<10;i++)pine(g,30+rnd()*30,-20+rnd()*60,.5);
  P=pathFromXZ([[0,0,60],[0,0,20],[-20,0,0],[-50,0,-6],[-80,0,-6],[-110,0,-14],[-140,0,-10]]);ex=[];
  notes=[[0,L('Ojukheon: adult ticket ₩3,000, open 09:00–18:00 (last entry 17:00), every day.','오죽헌: 어른 3,000원, 09:00~18:00(입장 마감 17:00), 연중무휴.')],[.4,L('The scholar Yi I (Yulgok) was born here, in the room called Mongryongsil.','학자 율곡 이이가 이곳 몽룡실에서 태어났어요.')],[.75,L('Ojuk means black bamboo: look at the dark stems around the houses.','오죽은 검은 대나무라는 뜻이에요. 집 둘레의 검은 줄기를 보세요.')]];}
 if(city==='jdj'){seaY=-1.2;ground(g,1200,600,-200,-290,'#8f8f8c');box(g,360,.3,16,M('#ead9a8'),-130,-.25,18);W=7;nP=26;
  const pf=new T.Group();pf.userData.pass=1;box(pf,120,1,6,M('#b9b4aa'),0,0,-8);g.add(pf);for(const z of[-12.4,-13.6])box(g,400,.2,.2,M('#6a6f76'),-60,0,z);const kt=mkKTX(70);kt.position.set(10,.2,-13);g.add(kt);
  box(g,14,5,8,M('#f4f6f7'),-10,0,-24);label(g,'정동진역 JEONGDONGJIN STATION',-10,6,-19.9,0,16,'#fff','#2e5a86');hourglass(g,-210,-30);
  for(let i=0;i<10;i++)pine(g,-60-i*14,-26-rnd()*8,.5);for(let i=0;i<10;i++){const p=person(g,-40-rnd()*150,0,13+rnd()*8,CLOTH[(rnd()*9)|0],SKIN[(rnd()*4)|0],1);p.rotation.y=Math.PI*(.8+rnd()*.4);list.push(p);}
  P=pathFromXZ([[30,1,-8],[0,1,-8],[-30,1,-8],[-50,0,0],[-90,0,6],[-140,0,6],[-180,0,0],[-200,0,-12]]);ex=[];
  notes=[[0,L('Jeongdongjin Station: often called the station closest to the sea in Korea. Gangneung to here is about 15 minutes by train.','정동진역이에요. 전국에서 바다와 가장 가까운 역으로 꼽혀요. 강릉에서 기차로 약 15분.')],[.35,L('The name means it lies due east (jeong-dong) of Gwanghwamun in Seoul.','서울 광화문에서 정동쪽에 있다고 해서 정동진이에요.')],[.65,L('Famous for sunrise; it became known nationwide through the 1995 TV drama Sandglass.','해돋이 명소예요. 1995년 드라마 「모래시계」로 전국에 알려졌어요.')]];}
 if(city==='skc'){seaY=-1.2;ground(g,1200,600,-200,-294,'#8f8f8c');ground(g,300,40,-140,52,'#b9ad98');W=6;nP=40;
  canopy(g,-14,-70,-38,12,8);for(let x=-18;x>-68;x-=7){box(g,4.6,3.4,3,M(['#d8c9ad','#c9c2b4','#e9e0cf'][(x/7|0)&1]),x,0,-46.5);box(g,4.6,3.4,3,M(['#e9e0cf','#d8c9ad'][(x/7|0)&1]),x,0,-29.5);}
  label(g,'속초관광수산시장 · SOKCHO MARKET',-40,9.6,-31.6,0,22,'#fff','#c8202a');label(g,'닭강정 · 오징어순대',-30,4.2,-31.4,0,9,'#fff','#2e5a86');
  const bg=new T.Group();bg.userData.pass=1;box(bg,7,.6,26,M('#c9a26a'),-90,-.6,18);g.add(bg);box(g,.15,.15,30,M('#3a3f45'),-93.6,1.4,18);for(const z of[4,32])box(g,.3,1.6,.3,M('#3a3f45'),-93.6,0,z);
  busA(g,40,-50,0,'#2fae6a','7 · 7-1 설악산');box(g,.3,3,.3,M('#5a6068'),48,0,-45);label(g,'🚌 BUS',48,3.4,-44.8,0,3,'#fff','#2fae6a');label(g,'갯배 GAETBAE',-90,3.2,5.2,0,7,'#fff','#2e5a86');label(g,'아바이마을 ABAI VILLAGE',-130,5.6,33.2,Math.PI,16,'#fff','#2e5a86');
  for(let x=-110,i=0;x>-200;x-=8,i++){abaiH(g,x,55,5.6,3.6,5,i);if(x<-120)abaiH(g,x,35.5,5.6,3.4,4,i+2);}
  for(let i=0;i<8;i++){const x=-20-i*22;if(Math.abs(x+90)<16)continue;fBoat(g,x,22+rnd()*4,rnd()*.4,['#f4f6f7','#2e8fd0','#e8e1d4'][i%3]);}
  P=pathFromXZ([[60,0,-38],[20,0,-38],[-20,0,-38],[-60,0,-38],[-82,0,-20],[-90,0,0],[-90,0,30],[-110,0,44],[-160,0,45],[-200,0,44]]);ex=[];
  notes=[[0,L('Sokcho Tourist & Fishery Market (the old Jungang Market): about 08:00–24:00, depending on the shop.','속초관광수산시장(옛 중앙시장)이에요. 가게마다 다르지만 08:00~24:00쯤 열어요.')],[.15,L('Famous here: dakgangjeong (sweet fried chicken), squid sundae and abai sundae.','닭강정, 오징어순대, 아바이순대가 유명해요.')],[.48,L('The gaetbae crosses a 50 m channel to Abai Village. No engine: passengers pull the wire. ₩500 one way.','갯배가 50m 물길을 건너 아바이마을로 가요. 엔진이 없어 승객이 줄을 당겨요. 편도 500원.')],[.8,L('Abai Village, across the channel from downtown Sokcho.','속초 시내에서 물길 건너편의 아바이마을이에요.')]];}
 if(city==='srk'){W=6;nP=26;box(g,600,.1,600,M('#4a5a38'),-150,-.1,-150);for(let z=-40;z<=100;z+=22){granite(g,-270-rnd()*30,z,34+rnd()*30,15+rnd()*6);granite(g,70+rnd()*30,z,30+rnd()*26,14+rnd()*6);}
  const gt=new T.Group();gt.userData.pass=1;for(const x of[-5,5])cyl(gt,.4,.4,7.4,KRED,x,0,30,8);hanokRoof(gt,12,3,0,7.4,30);g.add(gt);label(g,'설악산 신흥사 · SINHEUNGSA',0,9.6,31.7,0,14,'#fff','#2a2018');
  bronzeBuddha(g,-60,-34);busA(g,16,44,Math.PI/2,'#2fae6a','7 · 7-1 속초');box(g,.3,3,.3,M('#5a6068'),10,0,36);label(g,'🚌 BUS',10.2,3.4,36,Math.PI/2,3,'#fff','#2fae6a');tHall(g,-100,0,-36,12,8,0,'#9a7a4e');
  for(let i=0;i<28;i++){const a=-.15-rnd()*2.85,d=80+rnd()*120;granite(g,-150+Math.cos(a)*d,-62+Math.sin(a)*d*.8,30+rnd()*48,13+rnd()*14);}
  for(let i=0;i<9;i++)granite(g,-260+i*14,-110,40+i%3*12,12);for(let i=0;i<30;i++)pine(g,30-rnd()*200,-20-rnd()*50,.5);
  const cb=new T.Group();cb.userData.pass=1;box(cb,12,6,9,M('#f4f6f7'),-142,0,-22);label(cb,'설악케이블카 · CABLE CAR',-142,7,-17.4,0,14,'#fff','#c8202a');
  const cpts=[new T.Vector3(-142,8,-22),new T.Vector3(-152,62,-66)];cb.add(new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(cpts),20,.12,4,false),M('#3a3f45')));
  for(let i=1;i<5;i++){const k=i/5;box(cb,2,2,2,M('#c8202a'),-142-10*k,8+54*k-2.6,-22-44*k);}granite(cb,-160,-74,26,16);granite(cb,-150,-64,36,17);box(cb,16,1,18,M('#aab2bb',{transparent:true,opacity:.5}),-153,59,-66);for(let i=0;i<7;i++){const a=-1.1-rnd()*1.2,d=48+rnd()*26;granite(cb,-152+Math.cos(a)*d,-66+Math.sin(a)*d,40+rnd()*22,12+rnd()*6);}g.add(cb);
  P=pathFromXZ([[0,0,60],[0,0,20],[-30,0,0],[-70,0,-6],[-110,0,-8],[-136,0,-12],[-142,30,-38],[-150,60,-64],[-157,60,-73]]);ex=[];
  notes=[[0,L('Seoraksan National Park, Seorak-dong. Buses 7 and 7-1 from Sokcho go to the park entrance.','설악산 국립공원 설악동이에요. 속초에서 7번·7-1번 버스로 와요.')],[.25,L('Sinheungsa temple, first founded in 652. Entry is free.','652년에 처음 세워진 신흥사예요. 입장은 무료예요.')],[.7,L('Seorak Cable Car to Gwongeumseong: adult round trip ₩16,000, about 5 minutes up. Hours change with the season and weather.','권금성 가는 설악케이블카: 어른 왕복 16,000원, 올라가는 데 약 5분. 운행 시간은 계절과 날씨에 따라 달라요.')],[.99,L('Granite peaks all around, and the East Sea in the distance.','사방이 화강암 봉우리고, 멀리 동해가 보여요.')]];}
