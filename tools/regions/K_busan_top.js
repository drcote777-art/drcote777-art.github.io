/* ---------- 가상 부산·경남: 3D 소품 ---------- */
Object.assign(BSEA,{nmp:1,hud:1,ygs:1,gal:1,tyg:1});
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
