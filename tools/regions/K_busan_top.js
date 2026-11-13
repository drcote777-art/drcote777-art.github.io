/* ---------- 가상 부산·경남 2박 3일: 3D 소품 ---------- */
const BSEA={nmp:1,hud:1,ygs:1,gal:1,tyg:1};
function mkKTX(len){const g=new T.Group(),w=M('#f4f6f8'),bl=M('#1f4f91'),dk=M('#24303c',{emissive:'#0a1018'});
 box(g,len,3.4,3.1,w,0,.5,0);box(g,len+.06,.45,3.16,bl,0,1.25,0);box(g,len-6,.9,3.18,dk,0,2.3,0);box(g,len,.5,2.4,M('#30343a'),0,0,0);
 for(let x=-len/2+20;x<len/2-4;x+=20)box(g,.18,3,3.22,M('#c9ced4'),x,.6,0);
 const n=new T.Mesh(new T.CylinderGeometry(.15,1.75,7,4,1),w);n.rotation.set(Math.PI/4,0,-Math.PI/2);n.position.set(len/2+3.5,2.05,0);g.add(n);
 const n2=n.clone();n2.rotation.set(Math.PI/4,0,Math.PI/2);n2.position.x=-len/2-3.5;g.add(n2);return g;}
function mkBusanTower(){const g=new T.Group();g.userData.pass=1;const w=M('#eef1f4',{emissive:'#1a2026'});
 cyl(g,2.4,3.2,40,w,0,0,0,8);for(let i=0;i<8;i++){const a=i/8*Math.PI*2;box(g,.4,40,.4,M('#c9d2da'),Math.cos(a)*3,0,Math.sin(a)*3);}
 cyl(g,4.2,6.4,3,M('#dfe6ec',{emissive:'#20303a'}),0,39,0,8);cyl(g,6.6,6.6,2.4,M('#7fb0d0',{emissive:'#1f4a6a'}),0,42,0,8);
 cone(g,6.9,3.2,M('#f2f4f6'),0,44.4,0,8);cyl(g,.22,.22,9,M('#c8202a'),0,47.4,0,6);return g;}
function mkBridge(len){const g=new T.Group();g.userData.pass=1;const c=M('#d9dde2',{emissive:'#1a2028'}),lt=['#7fd0ff','#ff7fd0','#ffe07f','#9f7fff'],tx=len*.18;
 box(g,len,1.4,8,c,0,13.6,0);box(g,len,1.2,8.4,M('#8a9098'),0,11.6,0);for(let x=-len/2+20;x<len/2;x+=60)box(g,3,13,3,M('#9aa0a8'),x,-2,0);
 for(const x of[-tx,tx]){for(const z of[-3.8,3.8])box(g,1.8,42,1.8,c,x,0,z);box(g,1.8,2,9.4,c,x,38,0);box(g,1.8,2,9.4,c,x,22,0);}
 for(let i=0;i<=72;i++){const x=-len/2+i*len/72;for(const z of[-4.3,4.3])sph(g,.38,M(lt[(i+(z>0?2:0))%4],{emissive:lt[(i+(z>0?2:0))%4]}),x,15.6,z);}
 for(const z of[-3.8,3.8]){const pts=[];for(let i=0;i<=48;i++){const x=-len/2+i*len/48;let y;if(Math.abs(x)<=tx)y=15.5+24*(x*x)/(tx*tx);else y=39.5-24*(Math.abs(x)-tx)/(len/2-tx);pts.push(new T.Vector3(x,y,z));}
  g.add(new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(pts),80,.2,4,false),M('#eef2f6',{emissive:'#7f8fa8'})));}
 return g;}
function droneShow(){if(!cur||!cur.g)return;const g=new T.Group();g.userData.pass=1;const cs=['#9fe8ff','#ff9fd8','#fff09f'];
 for(let i=0;i<240;i++){const a=i/240*Math.PI*2,x=16*Math.pow(Math.sin(a),3),y=13*Math.cos(a)-5*Math.cos(2*a)-2*Math.cos(3*a)-Math.cos(4*a);const c=cs[i%3];sph(g,.55,M(c,{emissive:c}),x*2.6,74+y*2.6,0);}
 for(let i=0;i<60;i++){const c=cs[i%3];sph(g,.45,M(c,{emissive:c}),-50+i*1.7,40+Math.sin(i*.5)*4,0);}
 g.position.set(-150,0,240);cur.g.add(g);let k=0;const tw=setInterval(()=>{k++;g.rotation.y=Math.sin(k*.05)*.25;if(k>320||!g.parent)clearInterval(tw);},40);setTimeout(()=>{if(g.parent)g.parent.remove(g);},13000);}
function gHouse(g,x,y,z,w,h,d,c,ry){box(g,w,h,d,M(c),x,y,z,ry);box(g,w+.25,.35,d+.25,M('#4f6372'),x,y+h,z,ry);const wi=M('#2c3a46',{emissive:'#0c141c'});box(g,.9,.9,d+.06,wi,x-w*.2,y+h*.55,z,ry);if(w>3)box(g,.9,.9,d+.06,wi,x+w*.22,y+h*.55,z,ry);}
const GPAL=['#e8604c','#f2b134','#2fa39a','#4f74d6','#e9873c','#9466d0','#3fa865','#df4f74','#2fa9d6','#d4b93a'];
function mural(i){return repMat('mural'+i,64,64,(c)=>{c.fillStyle=GPAL[i%10];c.fillRect(0,0,64,64);c.fillStyle=GPAL[(i+3)%10];for(let k=0;k<5;k++){c.beginPath();c.arc(8+k*12,40+Math.sin(k+i)*10,7,0,6.3);c.fill();}c.fillStyle=GPAL[(i+6)%10];c.fillRect(0,54,64,10);c.fillStyle='#ffffff';c.fillRect(10+i%30,10,18,6);},[1,1]);}
function fBoat(g,x,z,ry,c){const b=new T.Group();b.userData.pass=1;box(b,7,1.4,2.6,M(c||'#f4f6f7'),0,-1,0);box(b,2.2,1.6,1.8,M('#e9edf0'),-1.2,.4,0);box(b,7.2,.2,2.8,M('#2e5a86'),0,-.2,0);cyl(b,.08,.08,4,M('#8a8f96'),1.6,.4,0,5);b.position.set(x,-.4,z);b.rotation.y=ry||0;g.add(b);return b;}
function tHall(g,x,y,z,w,d,ry,col){box(g,w,3.6,d,M(col||'#b9a27a'),x,y,z,ry);const c=Math.cos(ry||0),s=Math.sin(ry||0);for(const k of[-1,-.33,.33,1])cyl(g,.32,.32,3.6,KRED,x+c*k*w/2,y,z-s*k*w/2,8);hanokRoof(g,w,d,x,y+3.6,z,ry);}
function pagoda(g,x,y,z){for(let i=0;i<3;i++){box(g,3-i*.6,1.1,3-i*.6,M('#a8a39a'),x,y+i*1.6,z);box(g,3.8-i*.6,.35,3.8-i*.6,M('#9a958c'),x,y+i*1.6+1.1,z);}cone(g,.4,1.2,M('#9a958c'),x,y+4.9,z,6);}
function rocks(g,x,z,n,r){for(let i=0;i<n;i++){const m=new T.Mesh(new T.DodecahedronGeometry((r||2)*(.6+rnd()*.8),0),M(['#6f6a62','#7d776d','#5f5a53'][i%3]));m.position.set(x+(rnd()-.5)*r*6,-.6,z+(rnd()-.5)*r*3);m.rotation.set(rnd()*3,rnd()*3,rnd()*3);g.add(m);}}
function busA(g,x,z,ry,c,t){const b=new T.Group();b.userData.pass=1;box(b,11,3.2,2.6,M(c||'#2e5a86'),0,.3,0);box(b,11.05,1,2.65,M('#1d2a36',{emissive:'#0a1018'}),0,2,0);for(const k of[-3.6,3.6])for(const s of[-1.3,1.3])cyl(b,.5,.5,.4,M('#222'),k,0,s,10).rotation.x=Math.PI/2;if(t)label(b,t,0,3.9,1.36,0,6,'#fff',c||'#2e5a86');b.position.set(x,0,z);b.rotation.y=ry||0;g.add(b);return b;}
