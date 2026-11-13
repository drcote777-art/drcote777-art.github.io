/* ---------- 지역 공통 3D 소품 (KTX · 집 · 배 · 절 · 버스) ---------- */
const BSEA={};
function mkKTX(len){const g=new T.Group(),w=M('#f4f6f8'),bl=M('#1f4f91'),dk=M('#24303c',{emissive:'#0a1018'});
 box(g,len,3.4,3.1,w,0,.5,0);box(g,len+.06,.45,3.16,bl,0,1.25,0);box(g,len-6,.9,3.18,dk,0,2.3,0);box(g,len,.5,2.4,M('#30343a'),0,0,0);
 for(let x=-len/2+20;x<len/2-4;x+=20)box(g,.18,3,3.22,M('#c9ced4'),x,.6,0);
 const n=new T.Mesh(new T.CylinderGeometry(.15,1.75,7,4,1),w);n.rotation.set(Math.PI/4,0,-Math.PI/2);n.position.set(len/2+3.5,2.05,0);g.add(n);
 const n2=n.clone();n2.rotation.set(Math.PI/4,0,Math.PI/2);n2.position.x=-len/2-3.5;g.add(n2);return g;}
function gHouse(g,x,y,z,w,h,d,c,ry){box(g,w,h,d,M(c),x,y,z,ry);box(g,w+.25,.35,d+.25,M('#4f6372'),x,y+h,z,ry);const wi=M('#2c3a46',{emissive:'#0c141c'});box(g,.9,.9,d+.06,wi,x-w*.2,y+h*.55,z,ry);if(w>3)box(g,.9,.9,d+.06,wi,x+w*.22,y+h*.55,z,ry);}
const GPAL=['#e8604c','#f2b134','#2fa39a','#4f74d6','#e9873c','#9466d0','#3fa865','#df4f74','#2fa9d6','#d4b93a'];
function mural(i){return repMat('mural'+i,64,64,(c)=>{c.fillStyle=GPAL[i%10];c.fillRect(0,0,64,64);c.fillStyle=GPAL[(i+3)%10];for(let k=0;k<5;k++){c.beginPath();c.arc(8+k*12,40+Math.sin(k+i)*10,7,0,6.3);c.fill();}c.fillStyle=GPAL[(i+6)%10];c.fillRect(0,54,64,10);c.fillStyle='#ffffff';c.fillRect(10+i%30,10,18,6);},[1,1]);}
function fBoat(g,x,z,ry,c){const b=new T.Group();b.userData.pass=1;box(b,7,1.4,2.6,M(c||'#f4f6f7'),0,-1,0);box(b,2.2,1.6,1.8,M('#e9edf0'),-1.2,.4,0);box(b,7.2,.2,2.8,M('#2e5a86'),0,-.2,0);cyl(b,.08,.08,4,M('#8a8f96'),1.6,.4,0,5);b.position.set(x,-.4,z);b.rotation.y=ry||0;g.add(b);return b;}
function tHall(g,x,y,z,w,d,ry,col){box(g,w,3.6,d,M(col||'#b9a27a'),x,y,z,ry);const c=Math.cos(ry||0),s=Math.sin(ry||0);for(const k of[-1,-.33,.33,1])cyl(g,.32,.32,3.6,KRED,x+c*k*w/2,y,z-s*k*w/2,8);hanokRoof(g,w,d,x,y+3.6,z,ry);}
function pagoda(g,x,y,z){for(let i=0;i<3;i++){box(g,3-i*.6,1.1,3-i*.6,M('#a8a39a'),x,y+i*1.6,z);box(g,3.8-i*.6,.35,3.8-i*.6,M('#9a958c'),x,y+i*1.6+1.1,z);}cone(g,.4,1.2,M('#9a958c'),x,y+4.9,z,6);}
function rocks(g,x,z,n,r){for(let i=0;i<n;i++){const m=new T.Mesh(new T.DodecahedronGeometry((r||2)*(.6+rnd()*.8),0),M(['#6f6a62','#7d776d','#5f5a53'][i%3]));m.position.set(x+(rnd()-.5)*r*6,-.6,z+(rnd()-.5)*r*3);m.rotation.set(rnd()*3,rnd()*3,rnd()*3);g.add(m);}}
function busA(g,x,z,ry,c,t){const b=new T.Group();b.userData.pass=1;box(b,11,3.2,2.6,M(c||'#2e5a86'),0,.3,0);box(b,11.05,1,2.65,M('#1d2a36',{emissive:'#0a1018'}),0,2,0);for(const k of[-3.6,3.6])for(const s of[-1.3,1.3])cyl(b,.5,.5,.4,M('#222'),k,0,s,10).rotation.x=Math.PI/2;if(t)label(b,t,0,3.9,1.36,0,6,'#fff',c||'#2e5a86');b.position.set(x,0,z);b.rotation.y=ry||0;g.add(b);return b;}
