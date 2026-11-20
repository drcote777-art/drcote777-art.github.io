/* ---------- 가상 제주: 3D 소품 ---------- */
Object.assign(BSEA,{ydm:1,ssi:1,odg:1});
/* 여객기: 동체 · 날개 · 꼬리 날개 · 엔진 */
function jet(g,x,y,z,ry,tail){const p=new T.Group();p.userData.pass=1;const w=M('#f4f6f8'),tc=M(tail||'#2e5a86');
 const f=new T.Mesh(new T.CylinderGeometry(2,2,26,14),w);f.rotation.z=Math.PI/2;f.position.set(0,3.2,0);p.add(f);
 const n=new T.Mesh(new T.SphereGeometry(2,14,10),w);n.scale.set(2,1,1);n.position.set(13,3.2,0);p.add(n);
 const t=new T.Mesh(new T.ConeGeometry(2,7,14),w);t.rotation.z=Math.PI/2;t.position.set(-16.5,3.6,0);p.add(t);
 box(p,7,.4,30,w,1,2.6,0);box(p,4,.3,11,w,-16.5,3.8,0);box(p,5,6,.4,tc,-16.5,4.6,0);
 box(p,22,.5,4.06,M('#24303c',{emissive:'#0a1018'}),1,3.7,0);box(p,26,.35,4.08,tc,0,2.7,0);
 for(const s of[-6,6]){const e=new T.Mesh(new T.CylinderGeometry(1,1,4,10),M('#d8dde2'));e.rotation.z=Math.PI/2;e.position.set(2.5,1.9,s);p.add(e);}
 for(const [a,b] of[[9,0],[-1,-2],[-1,2]])cyl(p,.25,.25,1.3,M('#3a3f45'),a,0,b,6);
 p.position.set(x,y,z);p.rotation.y=ry||0;g.add(p);return p;}
/* 돌하르방 */
function dolHar(g,x,z,s,ry){s=s||1;const d=new T.Group();d.userData.pass=1;const st=M('#5b5853'),dk=M('#3a3835');
 cyl(d,1*s,1.15*s,3.2*s,st,0,0,0,10);sph(d,1.05*s,st,0,4.1*s,0,1,1.25,1);cyl(d,1*s,1.1*s,.4*s,st,0,5.1*s,0,12);cyl(d,.7*s,.92*s,1*s,st,0,5.4*s,0,12);
 for(const k of[-1,1]){sph(d,.26*s,dk,k*.42*s,4.5*s,.92*s,1,1,.5);box(d,.55*s,1.5*s,.35*s,st,k*.5*s,1.5*s,1.02*s);}sph(d,.32*s,st,0,4.05*s,1.02*s,1,1.3,.8);
 d.position.set(x,0,z);d.rotation.y=ry||0;g.add(d);return d;}
/* 야자수 */
function palm(g,x,z,h,y0){h=h||8;const p=new T.Group();p.userData.pass=1;cyl(p,.35,.5,h,M('#8a6a4a'),0,0,0,7);
 for(let i=0;i<7;i++){const a=i/7*Math.PI*2;const l=box(p,.7,.15,5,M(i%2?'#3f8a3a':'#4f9a44'),Math.cos(a)*2.3,h-.6,Math.sin(a)*2.3);l.rotation.y=Math.PI/2-a;l.rotation.x=.25;}
 p.position.set(x,y0||0,z);g.add(p);return p;}
/* 검은 현무암 돌담 */
function batDam(g,a,b,y){y=y||0;const dx=b[0]-a[0],dz=b[1]-a[1],L=Math.hypot(dx,dz),ry=-Math.atan2(dz,dx);
 box(g,L,1.1,.8,M('#3d3b38'),(a[0]+b[0])/2,y,(a[1]+b[1])/2,ry);for(let t=0;t<1;t+=2.2/L)sph(g,.45,M('#2f2d2a'),a[0]+dx*t,y+1.15,a[1]+dz*t,1.3,.7,1);}
/* 성산일출봉: 바닷가 응회구 (아래 절벽 · 위 풀밭 · 가운데 분화구) */
function tuffCone(g,x,z,R,H){const c=new T.Group();c.userData.pass=1;const V=(r,y)=>new T.Vector2(r*R,y*H);
 const lo=new T.Mesh(new T.LatheGeometry([V(1.04,-.05),V(1,0),V(.97,.25),V(.95,.4)],28),M('#8a7658',{side:T.DoubleSide}));c.add(lo);
 const hi=new T.Mesh(new T.LatheGeometry([V(.95,.4),V(.82,.85),V(.78,1),V(.7,1.03),V(.6,.85),V(.35,.62),V(0,.6)],28),M('#6f9a4a',{side:T.DoubleSide}));c.add(hi);
 for(let i=0;i<14;i++){const a=i/14*Math.PI*2+.1;box(c,3+rnd()*4,6+rnd()*8,3,M('#7a6648'),Math.cos(a)*R*.96,H*.08,Math.sin(a)*R*.96,-a);}
 c.position.set(x,0,z);g.add(c);return c;}
/* 용두암: 용 머리 모양 바위 */
function dragonRock(g,x,z,s){s=s||1;const r=new T.Group();r.userData.pass=1;const k=M('#3d3b38');
 const h=new T.Mesh(new T.DodecahedronGeometry(3*s,0),k);h.scale.set(1,2.8,1.1);h.rotation.z=-.45;h.position.set(0,6*s,0);r.add(h);
 const j=new T.Mesh(new T.DodecahedronGeometry(1.8*s,0),k);j.scale.set(2,.9,1);j.position.set(3.2*s,13.2*s,0);j.rotation.z=.25;r.add(j);
 for(let i=0;i<7;i++){const m=new T.Mesh(new T.DodecahedronGeometry((1.4+rnd()*1.6)*s,0),M(['#2f2d2a','#45423d'][i%2]));m.position.set((rnd()-.5)*10*s,-.6,(rnd()-.5)*8*s);r.add(m);}
 r.position.set(x,-1.2,z);g.add(r);return r;}
/* 폭포: 절벽 + 떨어지는 물 + 소 + 물안개 */
function waterfall(g,x,z,h,w){const f=new T.Group();f.userData.pass=1;
 box(f,w+46,h+8,14,M('#5f5a50'),0,-1,-7);box(f,w,h,.8,M('#e6f6fc',{transparent:true,opacity:.85,emissive:'#4a6a7a'}),0,0,.6);
 cyl(f,w*1.5,w*1.5,.4,M('#2f7a8a',{transparent:true,opacity:.9,emissive:'#0a2a33'}),0,-.3,w*1.2,24);
 for(let i=0;i<6;i++)sph(f,1.6+rnd(),M('#ffffff',{transparent:true,opacity:.25}),(rnd()-.5)*w,1+rnd()*2,1.5+rnd()*3,1.4,.8,1.2);
 for(let i=0;i<10;i++)pineAt(f,(rnd()-.5)*(w+40),h+6,-4-rnd()*6,.45);
 f.position.set(x,0,z);g.add(f);return f;}
/* 외돌개: 바다 위 돌기둥 */
function seaStack(g,x,z,h){const p=new T.Group();p.userData.pass=1;const k=M('#4a463f');cyl(p,2.2,4.2,h,k,0,-1.2,0,7);cyl(p,1.4,2.4,3,k,.6,h-1.6,.3,6);
 for(const [a,b] of[[0,0],[1,.8],[-.8,.6]])pineAt(p,a,h+.8,b,.28);p.position.set(x,0,z);g.add(p);return p;}
/* 시장 노점 */
function stall(g,x,z,ry,c){const s=new T.Group();s.userData.pass=1;box(s,3.2,1.1,2,M('#8a6a4a'),0,0,0);box(s,3.6,.2,2.6,M(c||'#e8604c'),0,2.6,0);for(const a of[-1.6,1.6])cyl(s,.06,.06,2.6,M('#666'),a,0,1,5);
 for(let i=0;i<6;i++)sph(s,.28,M(['#f39a1e','#ffb52e'][i%2]),-1.1+i*.44,1.35,0);sph(s,.35,M('#ffe6a0',{emissive:'#ffcf60'}),0,2.3,1.1);s.position.set(x,0,z);s.rotation.y=ry||0;g.add(s);return s;}
