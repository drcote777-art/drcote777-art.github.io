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
  /* 실시간 자료: 날씨를 물으면 Open-Meteo(무료)로 그 지역의 지금 날씨를 받아 함께 보냄 */
  const HOME={goyoam:["계룡시",36.2746,127.2489],cathedral:["바르셀로나",41.3874,2.1686]}[SITE]||["서울",37.5665,126.978];
  const STOP=new Set("오늘 내일 모레 지금 이번 주말 날씨 기온 어때요 어때 어떤가요 어떻습니까 알려줘 알려주세요 궁금해요 스님 신부님 수녀님 보살님 거기 여기 그쪽 요즘 아침 저녁 낮 밤 비가 눈이 우산 미세먼지 덥나요 춥나요 많이 혹시 좀 정말".split(" "));
  async function liveWeather(q){if(!/날씨|기온|온도|비\s*(가|와|오|올|소식)|눈\s*(이|와|오|올)|덥|춥|우산|미세먼지|일기\s*예보/.test(q))return"";
    let place=HOME;const words=(q.match(/[\uAC00-\uD7A3A-Za-z]{2,}/g)||[]).map(w=>w.replace(/(은|는|이|가|에|의|에서|쪽|지역)$/,"")).filter(w=>w.length>=2&&!STOP.has(w));
    for(const w of words.slice(0,3)){try{const g=await (await fetch("https://geocoding-api.open-meteo.com/v1/search?count=1&language=ko&name="+encodeURIComponent(w))).json();const x=(g.results||[])[0];if(x){place=[x.name+(x.country&&x.country!=="대한민국"?" ("+x.country+")":""),x.latitude,x.longitude];break}}catch(e){}}
    try{const u="https://api.open-meteo.com/v1/forecast?latitude="+place[1]+"&longitude="+place[2]+"&current=temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=2";
      const j=await (await fetch(u)).json(),c=j.current||{},d=j.daily||{};const f=n=>n==null?"?":Math.round(n);
      return "\n\n[실시간 자료 · Open-Meteo 기상 정보, 방금 받음]\n"+place[0]+" 지금: "+WMO_KO(c.weather_code|0)+", "+f(c.temperature_2m)+"°C, 습도 "+f(c.relative_humidity_2m)+"%, 바람 "+f(c.wind_speed_10m)+"km/h. 오늘: "+WMO_KO(d.weather_code?d.weather_code[0]:0)+", 최고 "+f(d.temperature_2m_max&&d.temperature_2m_max[0])+"°C 최저 "+f(d.temperature_2m_min&&d.temperature_2m_min[0])+"°C, 강수확률 "+f(d.precipitation_probability_max&&d.precipitation_probability_max[0])+"%. 내일: "+WMO_KO(d.weather_code?d.weather_code[1]:0)+", 최고 "+f(d.temperature_2m_max&&d.temperature_2m_max[1])+"°C 최저 "+f(d.temperature_2m_min&&d.temperature_2m_min[1])+"°C, 강수확률 "+f(d.precipitation_probability_max&&d.precipitation_probability_max[1])+"%."}catch(e){return""}}
  const SAMPLE=AI_URL?async function(input,opts){opts=opts||{};
    let prompt=typeof input==="string"?input:(input||[]).map(m=>(m.role==="assistant"?"대답: ":"")+m.content).join("\n");
    try{const lines=prompt.split("\n").filter(l=>/^방문객/.test(l));const q=(lines[lines.length-1]||"").replace(/^방문객[^:]*:\s*/,"");const lw=await liveWeather(q);if(lw)prompt+=lw}catch(e){}
    const send=async code=>{const ac=new AbortController(),tm=setTimeout(()=>ac.abort(),30000);
      try{const r=await fetch(AI_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt,code,search:window.AI_SEARCH!==false}),signal:ac.signal});
        let j={};try{j=await r.json()}catch(e){}return{r,j}}
      catch(e){throw{code:"network",message:String(e&&e.message||e)}}finally{clearTimeout(tm)}};
    let code=ls.get("family_code")||"";let {r,j}=await send(code);
    if(r.status===401&&j.error==="code"&&!window.__askedCode){window.__askedCode=true;
      const c=(window.prompt("스님·신부님과의 AI 대화는 가족만 쓸 수 있어요.\n가족 암호를 입력해 주세요.")||"").trim();
      if(c){ls.set("family_code",c);code=c;({r,j}=await send(code));if(r.status===401){ls.set("family_code","");window.__askedCode=false;try{alert("가족 암호가 맞지 않아요. 다음에 말을 걸 때 다시 입력해 주세요.")}catch(e){}}}}
    if(j.error==="budget")throw{code:"upstream",message:"budget"};
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
