import json, subprocess, concurrent.futures as cf, re
from collect import run, detail, OUT
det=json.load(open(f"{OUT}/details.json"))
want=["Tagalog Crime Stories","Alamin PH","Papa Dudut","Senyora Buzz","Utol Ford","Philippine Shocking History","Dark Asia with Megan","Sneaky Sushii","Coffeehouse Crime","Nadia Omara","Tagalog Crime Story Archive","CREEPY SARDINAS","Rahsia Silam","MysMania","Detektif Mat Despatch","Kronika","Dokyu sa Dilim","Dark Crimes Reel","Crime & Conspiracy","Manunudlo Archive","Grim Asia","Insider Stories"]
ids={}
for v in det.values():
    for w in want:
        if v["channel"] and v["channel"].lower().startswith(w.lower()[:14]): ids[v["channel"]]=v["channel_id"]
print(len(ids),ids)
def listing(a):
    name,cid,tab=a
    out=run(["yt-dlp","--skip-download","--flat-playlist","--playlist-end","40","-J",f"https://www.youtube.com/channel/{cid}/{tab}"],150)
    try: d=json.loads(out)
    except Exception: return name,tab,[]
    if not isinstance(d,dict): return name,tab,[]
    return name,tab,[(e["id"],e.get("view_count")) for e in (d.get("entries") or []) if e and e.get("id")]
jobs=[(n,c,t) for n,c in ids.items() for t in ("videos","shorts")]
lst={}
with cf.ThreadPoolExecutor(8) as ex:
    for n,t,l in ex.map(listing,jobs):
        lst[(n,t)]=l; print(n,t,len(l),flush=True)
allids=sorted({i for l in lst.values() for i,_ in l if i not in det})
print(len(allids),"to fetch",flush=True)
with cf.ThreadPoolExecutor(16) as ex:
    for vid,d in ex.map(detail,allids):
        if d: det[vid]=d
json.dump(det,open(f"{OUT}/details.json","w"),ensure_ascii=False)
json.dump({f"{k[0]}|{k[1]}":v for k,v in lst.items()},open(f"{OUT}/channel_lists.json","w"),ensure_ascii=False)
json.dump(ids,open(f"{OUT}/channel_ids.json","w"),ensure_ascii=False)
