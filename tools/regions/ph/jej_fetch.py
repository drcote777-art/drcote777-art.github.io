import json,subprocess,urllib.parse,time,re,sys
UA='CruiseGameBuild/1.0 (family hobby site; contact via github drcote777-art)'
KEYS={
 'gimpo':['Gimpo International Airport domestic terminal','김포국제공항 국내선'],
 'jejuair':['Jeju International Airport terminal','제주국제공항'],
 'yongduam':['Yongduam','용두암'],
 'dongmun':['Dongmun Market Jeju','동문재래시장','Jeju Dongmun market'],
 'seongsan':['Seongsan Ilchulbong','성산일출봉'],
 'cheonjiyeon':['Cheonjiyeon Falls','천지연폭포'],
 'oedolgae':['Oedolgae','외돌개'],
 'dolhareubang':['Dol hareubang','돌하르방'],
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
json.dump(out,open('cand_jej.json','w'),ensure_ascii=False,indent=1)
print('done')
