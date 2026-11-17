import json,subprocess,os,sys,time
from PIL import Image,ImageDraw,ImageFont
UA='CruiseGameBuild/1.0 (family hobby site; contact via github drcote777-art)'
d=json.load(open(os.environ.get('CAND','cand_east.json')))
try:d.update(json.load(open('cand_east2.json')) if 'CAND' not in os.environ else {})
except Exception:pass
PICK=json.loads(sys.argv[1]);out=sys.argv[2]
cells=[]
for k,idx in PICK.items():
    for i in idx:
        if i>=len(d.get(k,[])):continue
        x=d[k][i];fn='the/%s_%d.jpg'%(k,i)
        if not os.path.exists(fn) or os.path.getsize(fn)<2000:
            for a in range(3):
                subprocess.run(['curl','-s','-m','30','-A',UA,'-o',fn,x['thumb'].split('?')[0].replace('thumb.wikimedia.org','upload.wikimedia.org')])
                if os.path.exists(fn) and os.path.getsize(fn)>2000:break
                time.sleep(20)
            time.sleep(5)
        cells.append((k,i,fn))
W=330;H=250;cols=4;rows=(len(cells)+cols-1)//cols
sh=Image.new('RGB',(cols*W,rows*(H+22)),'white');dr=ImageDraw.Draw(sh)
try:f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
except Exception:f=None
for n,(k,i,fn) in enumerate(cells):
    c,r=n%cols,n//cols
    try:
        im=Image.open(fn).convert('RGB');im.thumbnail((W-6,H-6));sh.paste(im,(c*W+3,r*(H+22)+3))
    except Exception as e:dr.text((c*W+10,r*(H+22)+100),'ERR',fill='red',font=f)
    dr.text((c*W+4,r*(H+22)+H+2),'%s %d'%(k,i),fill='black',font=f)
sh.save(out,quality=80);print('ok',len(cells),out)
