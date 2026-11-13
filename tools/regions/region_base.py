# 지역 페이지 공통 생성기: 서울 페이지 생성기(patch_seoul.py)를 돌려 엔진 기능을 모두 받은 뒤,
# 지역 자료(일정·장소·사실·사진·퀴즈)와 지역 이름을 바꿔 끼웁니다. 지역 파일(patch_<지역>.py)은 자료만 갖습니다.
import re,json,os
class Region:
    def __init__(self,S):
        self.S=S
        src=open(S+'patch_seoul.py',encoding='utf8').read()
        END="open(S+'seoul.html','w',encoding='utf8').write(s);print('ok',len(s))"
        assert src.count(END)==1
        ns={};exec(compile(src.replace(END,''),'patch_seoul.py','exec'),ns);self.s=ns['s']
    def rep(self,a,b,n=1):
        c=self.s.count(a);assert c==n,('COUNT',c,a[:90]);self.s=self.s.replace(a,b)
    def cut(self,a,b,new):
        i=self.s.index(a);j=self.s.index(b,i);self.s=self.s[:i]+new+self.s[j:]
    def sub1(self,pat,new):
        m=re.search(pat,self.s);assert m,pat[:60];self.s=self.s[:m.start()]+new+self.s[m.end():]
    def build(self,R):
        """R: 지역 자료 사전. 키 설명은 patch_busan.py 참고."""
        rep,cut,sub1,S=self.rep,self.cut,self.sub1,self.S
        rid=R['id']
        # 이름 · 저장 칸 · 시작 돈
        rep("<title>Virtual Seoul · 가상 서울 3일</title>","<title>%s</title>"%R['title'])
        rep('<link rel="manifest" href="seoul.webmanifest">','')
        for k in ['seoul_game1','seoul_stamps','seoul_wallet']:
            self.s=self.s.replace("'"+k+"'","'"+k.replace('seoul_',rid+'_')+"'")
        rep("const G0={eur:300000,","const G0={eur:%d,"%R['money'])
        rep("const REG_ID='seoul';","const REG_ID='%s';"%rid)
        # 스탬프 · 장면 · 일정 · 장소 · AI 자료
        cut("const STAMPS=[","const LS=",R['stamps'])
        cut("const SCN={","/* 날짜별 할 일",R['scn'])
        cut("const DAYS=[","/* 메뉴 (게임 속 가상 가격) */",R['days'])
        cut("const mt=(id,t,side","const CRUISE_INFO=",R['city'])
        cut("const CRUISE_INFO=","const NPC_RULES=",R['info'])
        # 실제 정보 · 사진
        cut("const REAL={","const PH=",R['real'])
        PH=json.load(open(S+R['ph'],encoding='utf8'))
        for k in PH:
            if PH[k][1].startswith('by Junho Jung'):PH[k][1]='Junho Jung'
        sub1(r"const PH=\{.*?\};",'const PH='+json.dumps(PH,ensure_ascii=False)+';')
        sub1(r"const PANOS=\{.*?\};",'const PANOS={};')
        rep("if(id!=='icn'&&id!=='tmoney'&&id!=='kyoja'){const sm=","if(false){const sm=")
        # 🚇 '지역으로 바로 가기' 창: 지역 지하철 요금 안내, 서울 전용 S-Map·360 거리 사진 빼기
        rep("rb.innerHTML='<span>📷 '+REAL.subway.n+'</span>","rb.innerHTML='<span>📷 '+REAL.%s.n+'</span>"%R['metro'])
        rep("rb.onclick=()=>openReal('subway');b.append(rb);","rb.onclick=()=>openReal('%s');b.append(rb);"%R['metro'])
        cut("{const x=document.createElement('button');x.type='button';x.className='row';x.innerHTML='<span>🏙 '+L('S-Map","const gr=document.createElement('div');gr.className='grid';","")
        # 3D: 공통 소품 + 지역 소품 + 장소별 모양
        top=''.join(open(S+f,encoding='utf8').read() for f in R['top'])+R['rgn']+'\n'
        rep("/* ---------- 상태 ---------- */",top+"\n/* ---------- 상태 ---------- */")
        rep("if(city!=='hgr')ground(g,1000,1000,","if(city!=='hgr'&&!BSEA[city])ground(g,1000,1000,")
        rep("{id:'stamp',b:L('Stamp','스탬프'),s:'',city}];","{id:'stamp',b:L('Stamp','스탬프'),s:'',city}].filter(a=>a.id!=='stamp'||STAMPS.some(x=>x.id===city));")
        rep("L('✈ Arrival rehearsal','✈ 도착 예행연습')","L('🧭 Trip rehearsal','🧭 여행 예행연습')")
        rep("$('enter').textContent=L('Start at the airport','공항에서 시작하기')","$('enter').textContent=L(%r,%r)"%R['enter'])
        br=''.join(open(S+f,encoding='utf8').read() for f in R['br'])
        rep(" const curve=new T.CatmullRomCurve3(P,false,'centripetal');if(fac)",br+" const curve=new T.CatmullRomCurve3(P,false,'centripetal');if(fac)")
        hn=R.get('hotel_note')
        rep("Your hotel room in Myeongdong.",hn[0] if hn else "Your hotel room in %s."%R['hotel'][0])
        rep("명동 호텔 방이에요.",hn[1] if hn else "%s 호텔 방이에요."%R['hotel'][1])
        rep("b:'🛗 '+f.n,","b:(f.ic||'🛗')+' '+f.n,")
        rep("b:L('🛗 Elevator down','🛗 엘리베이터로 내려가기')","b:f.down||L('🛗 Elevator down','🛗 엘리베이터로 내려가기')")
        rep("say(f.say);playTune(10,true);markAct(f.id);}});});addQuiz(c,o.city);};","say(f.say);playTune(10,true);markAct(f.id);if(f.fx)f.fx();}});});if(D.fin){const q=S[Math.round(D.fin.t*(SN-1))];c.spots.push({x:q.x,z:q.z,y:q.y,r:7,b:L('🏁 Finish the trip','🏁 여행 마치기'),s:D.fin.s||'',fn:()=>doAct({id:'trip'})});}addQuiz(c,o.city);};")
        # 퀴즈 · 표현 · 꼭 기억할 것
        cut("const QZ={","function addQuiz",R['qz'])
        rep("['명동역 어디예요?','Myeongdong-yeok eodi-yeyo?',L('Where is Myeongdong Station?','명동역 어디예요?')]",R['phrase'])
        cut("h(L('Remember','꼭 기억할 것'));[","L('Meal and shop prices in this app are examples.",R['rem'])
        # 맛집 찾기
        sub1(r"const AREAKO=\{[^}]*\};",R['areako'])
        rep("const FOODS=[","const FOODS=["+R['foods'])
        rep("L('Good kimbap place nearby?','김밥 맛집 어디예요?')","L(%r,%r)"%R['chip'])
        rep("go('myd',.33);const n=cur.npcs.find(x=>x.id==='cit0')","go(%r,%s);const n=cur.npcs.find(x=>x.id==='cit0')"%(R['deep'][0],R['deep'][1]))
        # 시작 화면 · 지금 날씨 · 안내 문구
        rep('INCHEON AIRPORT → SEOUL',R['eyebrow'])
        rep("$('stH').innerHTML=L('Virtual Seoul<br>3 days','가상 서울<br>2박 3일');","$('stH').innerHTML=L(%r,%r);"%R['stH'])
        sub1(r"\$\('stP'\)\.textContent=L\('(?:[^'\\]|\\.)*','(?:[^'\\]|\\.)*'\);",R['stP'])
        sub1(r"\$\('stR'\)\.textContent=L\('(?:[^'\\]|\\.)*','(?:[^'\\]|\\.)*'\);",R['stR'])
        rep("latitude=37.5665&longitude=126.978","latitude=%s&longitude=%s"%R['wx'])
        en,ko=R['city_name']
        rep("L('Seoul now ','지금 서울 ')","L('%s now ','지금 %s ')"%(en,ko))
        rep("L('Live Seoul time and weather','지금 서울 시각·날씨 그대로')","L('Live %s time and weather','지금 %s 시각·날씨 그대로')"%(en,ko))
        rep("L('Seoul stamps','서울 스탬프')","L(%r,%r)"%R['stamps_title'])
        rep("Have a great real trip to Seoul!","Have a great real trip to %s!"%en)
        rep("'Good morning! A new day in Seoul.'","'Good morning! A new day of your trip.'")
        rep("role:L('Your Seoul tour guide','서울 여행 가이드')","role:L(%r,%r)"%R['guide_role'])
        self.s=self.s.replace("서울 2박 3일 코스",R['course_ko'])
        rep("L('Ask me anything about Seoul!','서울에 대해 무엇이든 물어보세요!')","L(%r,%r)"%R['guide_line'])
        v_en,v_ko,v_ko_ro=R['virtual']
        self.s=self.s.replace("가상 서울로",v_ko_ro).replace("가상 서울",v_ko).replace("Virtual Seoul",v_en)
        rep("else go(nextQ()?nextQ().q.sc:'icn',","else go(nextQ()?nextQ().q.sc:'%s',"%R['start'])
        rep("dayI=0;closePanel();go('icn');};b.append(rs);","dayI=0;closePanel();go('%s');};b.append(rs);"%R['start'])
    def save(self,name):
        open(self.S+name,'w',encoding='utf8').write(self.s);print('ok',name,len(self.s))
