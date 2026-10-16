import json,re,statistics as st
from metrics import REL, flat, det
res={}
for c,(inc,exc) in REL.items():
    ids={}
    for r in flat:
        if r["case"]!=c or not r["query"].startswith("YEAR:"): continue
        t=r["title"] or ""
        if not re.search(inc,t,re.I) or (exc and re.search(exc,t+" "+(r["channel"] or ""),re.I)): continue
        ids[r["id"]]=(t,r["channel"],r["views"] or 0)
    allflat=[r for r in flat if r["case"]==c and r["id"]]
    cov=len([i for i in {r['id'] for r in allflat} if i in det])/max(len({r['id'] for r in allflat}),1)
    vals=sorted([v[2] for v in ids.values()],reverse=True)
    res[c]=dict(n=len(ids),views=sum(vals),median=int(st.median(vals)) if vals else 0,top=vals[0] if vals else 0,channels=len({v[1] for v in ids.values()}),coverage=round(cov,2))
json.dump(res,open("yt/ytd.json","w"))
print(f"{'case':16s} {'n2026':>5} {'views2026':>11} {'median':>8} {'top':>9} {'ch':>3} {'detail_cov':>10}")
for c,m in sorted(res.items(),key=lambda kv:-kv[1]['views']): print(f"{c:16s} {m['n']:5d} {m['views']:11,} {m['median']:8,} {m['top']:9,} {m['channels']:3d} {m['coverage']:10}")
