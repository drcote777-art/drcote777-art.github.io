import json,subprocess,urllib.parse,time,re,sys
UA='CruiseGameBuild/1.0 (family hobby site; contact via github drcote777-art)'
KEYS={
 'yongsan':['Yongsan Station Seoul','용산역'],
 'indep':['Independence Hall of Korea','독립기념관'],
 'onyang':['Onyang Oncheon','온양온천','Onyangoncheon station'],
 'waemok':['Waemok village','왜목마을'],
 'haemi':['Haemieupseong','해미읍성','Haemi fortress'],
 'kkotji':['Kkotji beach','꽃지해수욕장','할미할아비바위'],
 'daecheon':['Daecheon beach','대천해수욕장','Boryeong mud'],
}
FREE=re.compile(r'^(CC BY(-SA)? [0-9.]+|CC0|Public domain|PD)',re.I)
def api(q):
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','generator':'search','gsrsearch':q,'gsrnamespace':6,'gsrlimit':12,'prop':'imageinfo','iiprop':'url|extmetadata|size|mime','iiurlwidth':330,'iiextmetadatafilter':'LicenseShortName|Artist|ImageDescription','format':'json','maxlag':5})
    for k in range(5):
        r=subprocess.run(['curl','-s','-m','30','-A',UA,u],capture_output=True,text=True).stdout
        try:
            d=json.loads(r)
            if 'error' in d:time.sleep(15*(k+1));continue
            return d
        except Exception:time.sleep(15*(k+1))
    return {}
strip=lambda h:re.sub(r'<[^>]+>','',h or '').strip()
out={}
for key,qs in KEYS.items():
    seen=set();out[key]=[]
    for q in qs:
        d=api(q);time.sleep(6)
        for p in sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',99)):
            ii=(p.get('imageinfo') or [{}])[0];m=ii.get('extmetadata',{})
            lic=m.get('LicenseShortName',{}).get('value','');t=p.get('title','')
            if t in seen or ii.get('mime')!='image/jpeg' or not FREE.match(lic) or ii.get('width',0)<900:continue
            seen.add(t);out[key].append({'t':t,'w':ii.get('width'),'h':ii.get('height'),'thumb':ii.get('thumburl'),'lic':lic,'artist':strip(m.get('Artist',{}).get('value',''))[:60],'desc':strip(m.get('ImageDescription',{}).get('value',''))[:120]})
    print(key,len(out[key]),flush=True)
json.dump(out,open('cand_cnm.json','w'),ensure_ascii=False,indent=1)
print('done')
