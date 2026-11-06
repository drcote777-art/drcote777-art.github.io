/* claude-web.js — claude.ai 밖(일반 웹사이트)에서 고요암·빛의 숲 성당이 돌아가게 하는 연결부
   함께 걷기·기록: Firebase 실시간 데이터베이스(무료 Spark 요금제)
   날씨: Open-Meteo (가입·키 없음, 비상업 무료)
   스님·신부님 대화: 페이지 안에 넣어 둔 대답 (AI 호출 없음) */
(function(){
  if(window.claude&&window.claude.use)return;
  const SITE=window.WEB_SITE||"site";
  const CFG=window.FB_CONFIG||null;
  const ok=!!(CFG&&CFG.databaseURL&&window.firebase&&firebase.initializeApp);
  let fdb=null;
  if(ok){try{(firebase.apps&&firebase.apps.length?firebase.app():firebase.initializeApp(CFG));fdb=firebase.database()}catch(e){console.warn("firebase",e);fdb=null}}
  const ls={get(k){try{return localStorage.getItem(k)}catch(e){return null}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
  const rnd=()=>Math.random().toString(36).slice(2,10)+Date.now().toString(36).slice(-4);
  let UID=ls.get("web_uid");if(!UID){UID="u"+rnd();ls.set("web_uid",UID)}
  const PEER="p"+rnd();
  const clean=v=>JSON.parse(JSON.stringify(v===undefined?null:v));
  const safeKey=k=>String(k).replace(/[.#$\[\]\/]/g,"_");
  const root=()=>fdb.ref(SITE);

  /* ---------- db: Firestore 모양을 흉내 낸 작은 층 ---------- */
  function mkDoc(path,id){const ref=root().child(path).child(safeKey(id));
    const snap=s=>({id:safeKey(id),exists:s.exists(),data:()=>s.val()});
    return{id:safeKey(id),
      get:()=>ref.once("value").then(snap),
      set:d=>ref.set(clean(d)),
      update:d=>ref.update(clean(d)),
      delete:()=>ref.remove(),
      onSnapshot(fn,err){const h=s=>{try{fn(snap(s))}catch(e){console.warn(e)}};ref.on("value",h,e=>err&&err(e));return()=>ref.off("value",h)}}}
  function mkQuery(path,q){q=q||{};
    const build=()=>{let r=root().child(path);
      if(q.where){r=r.orderByChild(q.where[0]).equalTo(q.where[2])}
      else if(q.order){r=r.orderByChild(q.order[0]);if(q.lim)r=r.limitToLast(q.lim)}
      else if(q.lim)r=r.limitToLast(q.lim);return r};
    const toSnap=s=>{let docs=[];s.forEach(c=>{const v=c.val();docs.push({id:c.key,exists:true,data:()=>v})});
      if(q.order){const f=q.order[0],dir=q.order[1]==="desc"?-1:1;docs.sort((a,b)=>{const x=(a.data()||{})[f],y=(b.data()||{})[f];return (x>y?1:x<y?-1:0)*dir})}
      if(q.lim)docs=docs.slice(0,q.lim);return{docs,size:docs.length,empty:!docs.length}};
    return{
      doc:id=>mkDoc(path,id==null?rnd():id),
      where:(f,op,v)=>mkQuery(path,{...q,where:[f,op,v]}),
      orderBy:(f,dir)=>mkQuery(path,{...q,order:[f,dir||"asc"]}),
      limit:n=>mkQuery(path,{...q,lim:n}),
      add:d=>{const id=rnd();return root().child(path).child(id).set(clean(d)).then(()=>mkDoc(path,id))},
      get:()=>build().once("value").then(toSnap),
      onSnapshot(fn,err){const r=build(),h=s=>{try{fn(toSnap(s))}catch(e){console.warn(e)}};r.on("value",h,e=>err&&err(e));return()=>r.off("value",h)}}}
  const DB={collection:p=>mkQuery(String(p).split("/").map(safeKey).join("/")),doc:p=>{const a=String(p).split("/");const id=a.pop();return mkDoc(a.map(safeKey).join("/"),id)}};

  /* ---------- room: 함께 걷기 (위치는 작게 자주, 나머지는 바뀔 때만) ---------- */
  const FAST=["x","z","ry","y","lv","act","actAt"];
  function mkRoom(){const base=root().child("_room"),posR=base.child("pos"),metaR=base.child("meta"),evR=base.child("ev");
    const myPos=posR.child(PEER),myMeta=metaR.child(PEER);myPos.onDisconnect().remove();myMeta.onDisconnect().remove();
    const peers=new Map(),subs=new Set();let lastMeta="",lastPos="",posTimer=0,pendingPos=null,lastPosAt=0;
    const list=()=>[...peers.entries()].filter(([,v])=>v.m||v.p).map(([id,v])=>({peer:id,isMe:id===PEER,sameTab:id===PEER,kind:"viewer",guest:true,presence:{...(v.m||{}),...(v.p||{})}}));
    const emitPeers=()=>{const ch={peers:list()};subs.forEach(f=>{try{f(ch)}catch(e){}})};
    const up=(id,k,v)=>{const o=peers.get(id)||{};o[k]=v;o.t=Date.now();peers.set(id,o);emitPeers()};
    const rm=(id,k)=>{const o=peers.get(id);if(!o)return;delete o[k];if(!o.m&&!o.p)peers.delete(id);emitPeers()};
    posR.on("child_added",s=>up(s.key,"p",s.val()));posR.on("child_changed",s=>up(s.key,"p",s.val()));posR.on("child_removed",s=>rm(s.key,"p"));
    metaR.on("child_added",s=>up(s.key,"m",s.val()));metaR.on("child_changed",s=>up(s.key,"m",s.val()));metaR.on("child_removed",s=>rm(s.key,"m"));
    // 오래 멈춘 접속(창을 그냥 닫은 경우 등) 정리
    setInterval(()=>{myMeta.child("_t").set(Date.now()).catch(()=>{});const now=Date.now();
      metaR.once("value").then(s=>s.forEach(c=>{const v=c.val()||{};if(c.key!==PEER&&now-(v._t||0)>120000){metaR.child(c.key).remove();posR.child(c.key).remove()}})).catch(()=>{})},45000);
    const writePos=()=>{posTimer=0;if(!pendingPos)return;const s=JSON.stringify(pendingPos);if(s!==lastPos){lastPos=s;lastPosAt=Date.now();myPos.set(pendingPos).catch(()=>{})}pendingPos=null};
    const joinT=Date.now();const evSubs={};
    return{
      presence(p){p=clean(p||{});const fp={},mp={};for(const k in p){if(FAST.includes(k))fp[k]=p[k];else mp[k]=p[k]}
        const ms=JSON.stringify(mp);if(ms!==lastMeta){lastMeta=ms;mp._t=Date.now();myMeta.set(mp).catch(()=>{})}
        pendingPos=fp;const wait=Math.max(0,220-(Date.now()-lastPosAt));if(!posTimer)posTimer=setTimeout(writePos,wait);return Promise.resolve()},
      peers:()=>list(),
      onPeers(fn){subs.add(fn);setTimeout(()=>fn({peers:list()}),0);return()=>subs.delete(fn)},
      emit(topic,data){const r=evR.child(safeKey(topic)).push();return r.set({d:clean(data),f:PEER,t:firebase.database.ServerValue.TIMESTAMP}).then(()=>{setTimeout(()=>r.remove().catch(()=>{}),20000)})},
      on(topic,fn){const q=evR.child(safeKey(topic)).orderByChild("t").startAt(joinT-2000);const h=s=>{const v=s.val()||{};try{fn({data:v.d,isMe:v.f===PEER,sameTab:v.f===PEER,peer:v.f})}catch(e){}};q.on("child_added",h);return()=>q.off("child_added",h)},
      leave(){myPos.remove();myMeta.remove()}}}

  /* ---------- 사용자 ---------- */
  const USER={id:async()=>UID,me:async()=>({id:UID,name:""}),isOwner:async()=>false,canEdit:async()=>false,can:async()=>true,profiles:async()=>({})};

  /* ---------- 날씨: AccuWeather 자리에 Open-Meteo ---------- */
  const PLACES={"2330378":[36.2746,127.2489]};const BCN=[41.4036,2.1744];
  function wmoToAcc(c){if(c===0)return 1;if(c===1)return 2;if(c===2)return 4;if(c===3)return 7;if(c===45||c===48)return 11;
    if(c>=51&&c<=57)return 12;if(c>=61&&c<=67)return 18;if(c>=71&&c<=77)return 22;if(c===80||c===81||c===82)return 12;if(c===85||c===86)return 19;if(c>=95)return 15;return 4}
  const WMO_KO=c=>c===0?"맑음":c<=2?"구름 조금":c===3?"흐림":c<=48?"안개":c<=57?"이슬비":c<=67?"비":c<=77?"눈":c<=82?"소나기":c<=86?"눈":"뇌우";
  const MCP={async callTool(server,tool,input){const key=((input||{}).queryParams||{}).locationKey;const [la,lo]=PLACES[key]||BCN;
      const u=`https://api.open-meteo.com/v1/forecast?latitude=${la}&longitude=${lo}&current=temperature_2m,weather_code,wind_speed_10m,wind_gusts_10m&timezone=auto`;
      const r=await fetch(u);if(!r.ok)throw{code:"tool_error",retryable:true};const j=await r.json(),c=j.current||{};const wc=c.weather_code|0;
      return{payload:{currentConditions:{iconCode:wmoToAcc(wc),temperatureValue:c.temperature_2m,phrase:WMO_KO(wc),extended:{windValue:c.wind_speed_10m||0,gusts:String(c.wind_gusts_10m||0)}}}}}};

  /* ---------- AI 대화: Cloudflare Worker 를 거쳐 Gemini ---------- */
  const AI_URL=window.AI_URL||"";
  const SAMPLE=AI_URL?async function(input,opts){opts=opts||{};
    const prompt=typeof input==="string"?input:(input||[]).map(m=>(m.role==="assistant"?"대답: ":"")+m.content).join("\n");
    const ac=new AbortController(),tm=setTimeout(()=>ac.abort(),30000);
    let r;try{r=await fetch(AI_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt}),signal:ac.signal})}
    catch(e){clearTimeout(tm);throw{code:"network",message:String(e&&e.message||e)}}
    clearTimeout(tm);
    let j={};try{j=await r.json()}catch(e){}
    if(r.status===429)throw{code:"rate_limited",message:"rate"};
    if(!r.ok||!j.text)throw{code:"upstream",message:String(j.error||r.status)};
    try{opts.onText&&opts.onText({text:j.text,delta:j.text})}catch(e){}
    return{text:j.text,truncated:false}}:null;

  let roomP=null;
  window.claude={WEB:true,use(name){
    if(name==="user")return Promise.resolve(USER);
    if(name==="mcp")return Promise.resolve(MCP);
    if(name==="sample")return Promise.resolve(SAMPLE);
    if(!fdb)return Promise.resolve(null);
    if(name==="db")return Promise.resolve(DB);
    if(name==="room"){if(!roomP)roomP=Promise.resolve(mkRoom());return roomP}
    return Promise.resolve(null)}};
})();
