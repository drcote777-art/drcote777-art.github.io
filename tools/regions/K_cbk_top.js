/* ---------- 가상 충북: 3D 소품 ---------- */
Object.assign(BSEA,{dyt:1,dds:1,mch:1,ulj:1,cpc:1,sag:1});
/* 만천하스카이워크: 둥근 탑 + 나선형 길 + 유리 바닥 전망대 세 갈래 */
function skyTower(g,x,z,h){const t=new T.Group();t.userData.pass=1;cyl(t,6,6.4,h,M('#d8dde2'),0,0,0,18);
 for(let i=0;i<46;i++){const a=i*.42,y=i*(h-1)/46;const s=box(t,3.4,.35,1.8,M('#b9c0c7'),Math.cos(a)*7.6,y,Math.sin(a)*7.6);s.rotation.y=-a;}
 cyl(t,9.5,9.5,.7,M('#aab2ba'),0,h,0,22);for(let i=0;i<24;i++){const a=i/24*Math.PI*2;box(t,.18,1.2,.18,M('#5a6068'),Math.cos(a)*9.3,h+.7,Math.sin(a)*9.3);}
 const gl=M('#bfe3f2',{transparent:true,opacity:.42});
 for(const a of[-Math.PI/2,-Math.PI/2+2.1,-Math.PI/2-2.1]){const w=new T.Group();box(w,4,.4,22,gl,0,0,-11);for(const s of[-2,2])box(w,.15,1.2,22,M('#8a9098'),s,.4,-11);box(w,4.3,.15,.15,M('#8a9098'),0,1.5,-22);w.position.set(0,h,0);w.rotation.y=a+Math.PI/2;t.add(w);}
 t.position.set(x,0,z);g.add(t);return t;}
/* 도담삼봉: 강 위 바위 봉우리 */
function rockPeak(g,x,z,rt,rb,h,y0){const p=new T.Group();p.userData.pass=1;cyl(p,rt,rb,h,M('#6f6b60'),0,0,0,9);cyl(p,rt*.7,rt*1.05,1.2,M('#5d5a50'),0,h-.4,0,9);p.position.set(x,y0||0,z);g.add(p);return p;}
/* 작은 소나무 (높이 지정) */
function pineAt(g,x,y,z,s){const p=pine(g,x,z,s);p.position.y=y;return p;}
/* 강가 데크길 난간 */
function rail(g,a,b,side){const dx=b[0]-a[0],dz=b[2]-a[2],L=Math.hypot(dx,dz),nx=-dz/L,nz=dx/L;const o=box(g,L,1.1,.18,M('#5a4a3a'),(a[0]+b[0])/2+nx*side,(a[1]||0),(a[2]+b[2])/2+nz*side);o.rotation.y=-Math.atan2(dz,dx);return o;}
