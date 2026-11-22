/* ---------- 가상 충남·서해안: 3D 소품 ---------- */
Object.assign(BSEA,{wmk:1,kkj:1,dcb:1});
/* 성곽: 두 점 사이 돌담 + 여장 */
function fortWall(g,a,b,h,col){const dx=b[0]-a[0],dz=b[2]-a[2],L=Math.hypot(dx,dz),ry=-Math.atan2(dz,dx),y0=Math.min(a[1],b[1]),hh=h+Math.abs(a[1]-b[1]);
 const o=box(g,L+.6,hh+1,1.6,M(col||'#bdb3a0'),(a[0]+b[0])/2,y0-1,(a[2]+b[2])/2);o.rotation.y=ry;
 for(let t=.08;t<1;t+=.14){const yy=a[1]+(b[1]-a[1])*t;const m=box(g,1.3,.9,1.7,M('#cfc6b4'),a[0]+dx*t,yy+h-.2,a[2]+dz*t);m.rotation.y=ry;}return o;}
/* 깃발 */
function flag(g,x,y,z,c){cyl(g,.08,.08,5,M('#6a5040'),x,y,z,6);box(g,.06,1.6,1.2,M(c,{emissive:c}),x,y+3.3,z+.6);}
/* 태극기 */
function tFlag(g,x,z){cyl(g,.08,.08,7,M('#d8dde2'),x,0,z,6);const f=TM('taeguk',96,64,(c,w,h)=>{c.fillStyle='#fff';c.fillRect(0,0,w,h);c.fillStyle='#c8202a';c.beginPath();c.arc(w/2,h/2,13,Math.PI,0);c.fill();c.fillStyle='#1f4f91';c.beginPath();c.arc(w/2,h/2,13,0,Math.PI);c.fill();c.fillStyle='#111';for(const [a,b] of[[16,14],[80,14],[16,50],[80,50]])c.fillRect(a-7,b-5,14,10);});
 const m=new T.Mesh(new T.PlaneGeometry(2.1,1.4),f);m.material.side=T.DoubleSide;m.position.set(x,6.2,z+1.1);m.rotation.y=Math.PI/2;g.add(m);}
/* 족욕탕: 긴 나무 물길 + 김 */
function footBath(g,x,z,L,ry){const f=new T.Group();f.userData.pass=1;box(f,L,.9,3.2,M('#8a6a4a'),0,0,0);box(f,L-.6,.12,2.4,M('#7ec0d8',{emissive:'#1a4a66',transparent:true,opacity:.85}),0,.82,0);
 for(const s of[-2.1,2.1])box(f,L,.5,1,M('#6a5040'),0,0,s);for(let i=0;i<6;i++)sph(f,.9,M('#ffffff',{transparent:true,opacity:.22}),-L/2+2+i*(L-4)/5,2,0,1,.6,1);
 f.position.set(x,0,z);f.rotation.y=ry||0;g.add(f);return f;}
/* 겨레의 탑: 하늘로 뻗은 두 날개 기둥 */
function nationTower(g,x,z,h){const t=new T.Group();t.userData.pass=1;const w=M('#e8e4dc');
 for(const s of[-1,1]){const p=new T.Mesh(new T.CylinderGeometry(.5,2.6,h,4),w);p.position.set(s*2,h/2,0);p.rotation.z=-s*.12;t.add(p);}
 box(t,9,1.2,9,M('#bdb3a0'),0,0,0);t.position.set(x,0,z);g.add(t);return t;}
/* 큰 기와 전시관 (겨레의 집 느낌) */
function bigHall(g,x,z,w,d){const h=new T.Group();h.userData.pass=1;box(h,w,2,d,M('#cfc6b4'),0,0,0);
 for(let i=-4;i<=4;i++)cyl(h,.6,.6,11,M('#e8e1d4'),i*w/9,2,d/2-1,10);box(h,w,9,d-4,M('#e8e1d4'),0,2,-1);
 const r=new T.Mesh(new T.ConeGeometry(w*.62,9,4,1),M('#4f5a62'));r.rotation.y=Math.PI/4;r.scale.set(1,1,d/w);r.position.set(0,17.5,0);h.add(r);
 h.position.set(x,0,z);g.add(h);return h;}
/* 고목 (해미읍성 회화나무 느낌) */
function bigTree(g,x,z,s){s=s||1;const t=new T.Group();t.userData.pass=1;cyl(t,1.1*s,1.6*s,7*s,M('#5a4636'),0,0,0,9);
 for(const [a,b,c] of[[-2,9,0],[2.4,10,1],[0,11.5,-1.6],[1,8.5,2.2]])sph(t,4.2*s,M('#4f6a3a'),a*s,b*s,c*s,1.2,.8,1.2);t.position.set(x,0,z);g.add(t);return t;}
/* 초가집 */
function thatch(g,x,z,ry){const h=new T.Group();h.userData.pass=1;box(h,6,2.6,4,M('#e8dcc4'),0,0,0);const r=new T.Mesh(new T.SphereGeometry(3.6,12,8,0,Math.PI*2,0,Math.PI/2),M('#b89a5a'));r.scale.set(1.15,.5,.85);r.position.set(0,2.6,0);h.add(r);
 h.position.set(x,0,z);h.rotation.y=ry||0;g.add(h);return h;}
/* 바다 위 바위섬 + 소나무 (할미·할아비 바위) */
function rockIslet(g,x,z,r,h){const p=new T.Group();p.userData.pass=1;cyl(p,r*.7,r,h,M('#6f6a5c'),0,-1.2,0,9);cyl(p,r*.5,r*.72,h*.35,M('#5d5a50'),0,h-1.4,0,9);
 for(let i=0;i<5;i++)pineAt(p,(rnd()-.5)*r,h+h*.3-1.6,(rnd()-.5)*r,.35+rnd()*.15);p.position.set(x,0,z);g.add(p);return p;}
/* 바다 레일바이크 (대천 스카이바이크) */
function seaRail(g,a,b,y){const dx=b[0]-a[0],dz=b[1]-a[1],L=Math.hypot(dx,dz),ry=-Math.atan2(dz,dx);box(g,L,.5,2.4,M('#d8dde2'),(a[0]+b[0])/2,y,(a[1]+b[1])/2,ry);
 for(let t=0;t<=1;t+=16/L)cyl(g,.4,.4,y+1.2,M('#aab2ba'),a[0]+dx*t,-1.2,a[1]+dz*t,8);
 for(let i=0;i<4;i++){const t=.15+i*.22;box(g,2,1.2,1.6,M(['#e8604c','#f2b134','#2fa39a','#4f74d6'][i]),a[0]+dx*t,y+.5,a[1]+dz*t,ry);}}
