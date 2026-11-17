import json,subprocess,time,urllib.parse,os,sys
S='/tmp/claude-0/-home-claude/488bc777-032c-51f3-86bf-b1b9a3a466f3/scratchpad/'
UA='CruiseGameBuild/1.0 (family hobby site; contact via github drcote777-art)'
PH=json.load(open(S+'ph/PH_busan.json'))
out={}
for k,p in PH.items():
    name,h=p[0],p[3]
    f=S+'ph/thb/'+k+'.jpg'
    u='https://upload.wikimedia.org/wikipedia/commons/thumb/%s/%s/960px-%s'%(h,name,name)
    if not (os.path.exists(f) and os.path.getsize(f)>10000):
        for t in range(4):
            r=subprocess.run(['curl','-s','-m','40','-A',UA,'-o',f,'-w','%{http_code}',u],capture_output=True,text=True).stdout
            if r=='200' and os.path.getsize(f)>10000:break
            print(k,'retry',r,flush=True);time.sleep(20*(t+1))
        time.sleep(4)
    ok=os.path.exists(f) and os.path.getsize(f)>10000
    print(k,'ok' if ok else 'FAIL',os.path.getsize(f) if os.path.exists(f) else 0,flush=True)
    if ok: out[urllib.parse.unquote(name)]=f
json.dump(out,open(S+'ph/local_busan.json','w'),ensure_ascii=False,indent=1)
print('done',len(out))
