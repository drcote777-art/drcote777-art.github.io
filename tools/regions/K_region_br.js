 if(city==='sst'){fac=modern;off=13;hh=[18,46];W=10;nP=46;words=['KTX','KORAIL','편의점 CVS','카페','약국','ATM'];
  const o=new T.Group();box(o,36,10,14,M('#b5523b'),0,0,0);box(o,36.6,.8,14.6,M('#e9e2d0'),0,10,0);for(const x of[-14,-7,0,7,14])box(o,2.6,6.4,.3,M('#e9e2d0'),x,1.6,7.2);
  const dm=new T.Mesh(new T.SphereGeometry(5.2,20,12,0,Math.PI*2,0,Math.PI/2),M('#4f8a7a'));dm.position.set(0,10.8,0);o.add(dm);cyl(o,.25,.25,3,M('#4f8a7a'),0,15.8,0,8);
  label(o,'문화역서울284 · CULTURE STATION SEOUL 284',0,8.2,7.4,0,18,'#3a2a20','#e9e2d0');o.position.set(34,0,26);o.rotation.y=-Math.PI/2;g.add(o);
  const hall=new T.Group();hall.userData.pass=1;box(hall,96,1,34,new T.MeshPhongMaterial({color:'#9fb8cc',specular:'#ffffff',shininess:80,transparent:true,opacity:.5}),-80,15,-12);
  for(let x=-124;x<=-36;x+=11)for(const z of[-28,4])cyl(hall,.45,.45,15,M('#c9ced4'),x,0,z,8);
  const pf=new T.Group();pf.userData.pass=1;box(pf,150,1,8,M('#b9b4aa'),-196,0,-18);box(pf,150,.06,.5,M('#f0c419'),-196,1,-21.6);hall.add(pf);g.add(hall);
  label(g,'서울역 SEOUL STATION',-35.6,17,-12,Math.PI/2,26,'#fff','#1f4f91');
  box(g,.4,4.6,12,M('#1d2a36',{emissive:'#0a1018'}),-70,8.6,-10);label(g,RGN.ktx,-69.7,11.6,-10,Math.PI/2,11,'#ffd84a','#1d2a36');label(g,'타는 곳 → PLATFORM',-69.7,9.6,-10,Math.PI/2,11,'#fff','#1d2a36');
  for(let i=0;i<4;i++){box(g,1.4,2,1,M('#2e5a86'),-48-i*2.6,0,-25);label(g,'승차권 TICKET',-48-i*2.6,2.4,-24.45,0,2.4,'#fff','#2e5a86');}
  const kt=mkKTX(120);kt.position.set(-196,1,-25.6);g.add(kt);
  P=pathFromXZ([[0,0,70],[0,0,30],[-10,0,0],[-50,0,-8],[-100,0,-12],[-128,1,-18],[-170,1,-18],[-230,1,-18]]);ex=[[34,26,30],[-80,-12,64],[-196,-20,96]];
  notes=[[0,RGN.sst0],[.14,L('The domed red-brick building is the old Seoul Station (1925), now the arts space Culture Station Seoul 284.','붉은 벽돌 돔 건물은 옛 서울역(1925)이에요. 지금은 문화역서울284라는 전시 공간이에요.')],[.45,L('Check the departure board for your train and platform. Your car number and seat are on the ticket.','전광판에서 열차와 타는 곳을 확인해요. 호차와 좌석 번호는 표에 적혀 있어요.')],[.8,RGN.sst8]];}
 if(city==='nbu'){fac=modern;off=13;hh=[12,30];W=9;nP=30;words=['고속버스 EXPRESS BUS','매표소 TICKETS','편의점','카페'];
  box(g,60,10,22,M('#e8e1d4'),-40,0,-30);label(g,RGN.term,-40,11.4,-18.9,0,30,'#fff','#2e5a86');for(let i=0;i<5;i++)busA(g,-14-i*12,-12,0,['#2e5a86','#c8202a','#2fae6a'][i%3]);
  box(g,6,3,4,M('#f4f6f7'),-80,0,6);label(g,RGN.line,-80,4,3.95,Math.PI,14,'#fff',RGN.lineCol);
  P=pathFromXZ([[0,0,40],[0,0,0],[-40,0,-6],[-90,0,-6]]);ex=[[-40,-30,40],[-80,6,8]];
  notes=RGN.termNotes;}
 if(city==='sar'){fac=modern;off=13;hh=[16,40];W=10;nP=40;words=['편의점 CVS','카페','약국','ATM','관광안내 INFO'];
  const pf=new T.Group();pf.userData.pass=1;box(pf,150,1,8,M('#b9b4aa'),40,0,-18);box(pf,150,.06,.5,M('#f0c419'),40,1,-21.6);g.add(pf);
  const kt=mkKTX(120);kt.position.set(40,1,-25.6);g.add(kt);
  const hall=new T.Group();hall.userData.pass=1;box(hall,90,1,34,new T.MeshPhongMaterial({color:'#9fb8cc',specular:'#ffffff',shininess:80,transparent:true,opacity:.5}),-60,15,-10);
  for(let x=-100;x<=-20;x+=11)for(const z of[-26,6])cyl(hall,.45,.45,15,M('#c9ced4'),x,0,z,8);g.add(hall);
  label(g,RGN.arr,-14.6,17,-10,Math.PI/2,26,'#fff','#1f4f91');
  box(g,6,3,4,M('#f4f6f7'),-110,0,9);label(g,RGN.arrLine,-110,4,6.95,Math.PI,14,'#fff',RGN.arrLineCol);
  P=pathFromXZ([[100,1,-18],[40,1,-18],[0,1,-18],[-20,0,-10],[-60,0,-6],[-100,0,0],[-130,0,4]]);ex=[[40,-20,80],[-60,-10,60]];
  notes=RGN.arrNotes;}
