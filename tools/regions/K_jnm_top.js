/* ---------- 가상 전남·광주: 3D 소품 ---------- */
Object.assign(BSEA,{dmy:1,scw:1,odo:1,ycb:1});
/* 분수: 둥근 수반 + 물 + 가운데 물줄기 */
function fountain(g,x,z,r){const f=new T.Group();f.userData.pass=1;cyl(f,r,r+.4,1,M('#c9c2b4'),0,0,0,28);cyl(f,r-.5,r-.5,.2,M('#6fb4d6',{emissive:'#1a4a66'}),0,.9,0,28);
 cyl(f,1.2,1.6,1.4,M('#b9b2a4'),0,.9,0,16);for(let i=0;i<6;i++){const a=i/6*Math.PI*2;cyl(f,.12,.05,3,M('#cfeaf6',{transparent:true,opacity:.7}),Math.cos(a)*1.4,1.8,Math.sin(a)*1.4,6);}
 cyl(f,.25,.08,5,M('#e6f4fb',{transparent:true,opacity:.75}),0,2,0,8);f.position.set(x,0,z);g.add(f);}
/* 시계탑: 네모 기둥 + 네 면 시계 */
function clockTower(g,x,z){const c=new T.Group();c.userData.pass=1;box(c,2.6,15,2.6,M('#d8d2c4'),0,0,0);box(c,3.2,3.2,3.2,M('#efe9dc'),0,15,0);
 for(const [dx,dz,ry] of[[0,1.62,0],[0,-1.62,Math.PI],[1.62,0,Math.PI/2],[-1.62,0,-Math.PI/2]]){const d=new T.Mesh(new T.CircleGeometry(1.15,24),M('#ffffff'));d.position.set(dx,16.6,dz);d.rotation.y=ry;c.add(d);}
 cone(c,2.2,2,M('#5a6068'),0,18.2,0,4);c.position.set(x,0,z);g.add(c);}
/* 옛 전남도청: 하얀 2층 건물 */
function provOffice(g,x,z,ry){const o=new T.Group();box(o,40,9,12,M('#ece8de'),0,0,0);box(o,41,.8,13,M('#8a8f96'),0,9,0);
 for(let i=-4;i<=4;i++){box(o,2.2,2.6,.2,M('#3a4a5a',{emissive:'#0c141c'}),i*4.2,1.8,6.1);box(o,2.2,2.6,.2,M('#3a4a5a',{emissive:'#0c141c'}),i*4.2,5.6,6.1);}
 box(o,7,5,1.6,M('#d9d2c3'),0,0,6.8);o.position.set(x,0,z);o.rotation.y=ry||0;g.add(o);}
/* 국립아시아문화전당: 땅 아래 건물, 지붕은 잔디 공원 + 유리 채광창 + 움푹한 마당 */
function accRoof(g,x,z){const a=new T.Group();a.userData.pass=1;box(a,90,1.2,50,M('#7fa35a'),0,0,0);
 for(let i=0;i<10;i++)box(a,4,1.6,4,M('#bcd6e6',{transparent:true,opacity:.75,emissive:'#20384a'}),-36+i*8,1,(i%2?-8:8));
 box(a,40,.2,16,M('#9a9488'),-10,1.25,-18);for(let i=0;i<6;i++)box(a,40,.5,2,M('#b9b2a4'),-10,1.2-i*.0,-27+i*.01);
 a.position.set(x,0,z);g.add(a);}
/* 푸른 대나무 숲 (죽녹원) */
function bambooGreen(g,x,z,n,r){const m=M('#7aa24a'),lf=M('#5f8f3a'),lf2=M('#6fa046');for(let i=0;i<n;i++){const a=rnd()*6.28,d=rnd()*r,h=11+rnd()*6,px=x+Math.cos(a)*d,pz=z+Math.sin(a)*d;cyl(g,.11,.14,h,m,px,0,pz,6);for(let k=0;k<2;k++)sph(g,.85,k?lf:lf2,px+(rnd()-.5)*1.2,h*(.66+k*.24),pz+(rnd()-.5)*1.2,.7,2.4,.7);}}
/* 정자 */
function jPavilion(g,x,y,z){const p=new T.Group();p.userData.pass=1;box(p,8,.8,8,M('#b8b0a0'),0,0,0);for(const a of[-3,3])for(const b of[-3,3])cyl(p,.25,.25,3.2,KRED,a,.8,b,8);hanokRoof(p,8,8,0,4,0);p.position.set(x,y,z);g.add(p);}
/* 오래된 큰 나무 (관방제림) */
function oldTree(g,x,z,s){s=s||1;cyl(g,.8*s,1.2*s,6*s,M('#6a5040'),x,0,z,8);sph(g,5*s,M('#5e7f3e'),x,8*s,z,1.2,.8,1.2);sph(g,3.5*s,M('#6e8f46'),x+2*s,10*s,z-1*s,1,.8,1);}
/* 갈대 덤불 (순천만): 가을빛 */
function reeds(g,x0,x1,z0,z1,n){const cs=['#b89a5a','#a8884a','#c8a868','#9a7c48'];for(let i=0;i<n;i++){const x=x0+rnd()*(x1-x0),z=z0+rnd()*(z1-z0);cone(g,.45+rnd()*.4,3+rnd()*1.6,M(cs[i&3]),x,0,z,5);}}
/* 나무 데크 길: 두 점 사이 */
function deck(g,a,b,w,col){const dx=b[0]-a[0],dz=b[2]-a[2],L=Math.hypot(dx,dz);const o=box(g,L+.6,.3,w,M(col||'#8a6a4a'),(a[0]+b[0])/2,-.15,(a[2]+b[2])/2);o.rotation.y=-Math.atan2(dz,dx);}
/* 동백나무: 짙은 초록 + 빨간 꽃 */
function camellia(g,x,z,y){y=y||0;sph(g,2.6,M('#2f5a2e'),x,y+2.6,z,1,1.1,1);for(let i=0;i<6;i++){const a=rnd()*6.28,h=1.4+rnd()*2.6;sph(g,.35,M('#d8202a'),x+Math.cos(a)*2.3,y+h,z+Math.sin(a)*2.3);}cyl(g,.25,.3,1.2,M('#5a4030'),x,y,z,6);}
/* 원뿔 언덕 위 높이 (길이 언덕을 따라 오르도록) */
function coneY(cx,cz,r,h,x,z){return Math.max(0,h*(1-Math.hypot(x-cx,z-cz)/r));}
/* 동백열차: 작은 관광 열차 */
function tram(g,x,z,ry){const t=new T.Group();t.userData.pass=1;for(let i=0;i<3;i++){box(t,5,2.4,2.4,M(i?'#f4f6f7':'#3fa865'),-i*5.6,.4,0);box(t,5.1,.5,2.5,M('#3fa865'),-i*5.6,2.8,0);for(const k of[-1.6,1.6])for(const s of[-1.1,1.1])cyl(t,.35,.35,.3,M('#222'),-i*5.6+k,0,s,8).rotation.x=Math.PI/2;}t.position.set(x,0,z);t.rotation.y=ry||0;g.add(t);}
/* 하얀 등대 */
function lighthouse(g,x,y,z){const l=new T.Group();l.userData.pass=1;cyl(l,1.6,2.2,12,M('#f4f6f7'),0,0,0,12);cyl(l,1.8,1.8,2,M('#c9e6f2',{emissive:'#2a5a7a'}),0,12,0,12);cone(l,2,1.6,M('#c8202a'),0,14,0,12);l.position.set(x,y,z);g.add(l);}
