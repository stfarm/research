import json, os, subprocess, concurrent.futures as cf
from collect import CASES, run, detail, OUT
import urllib.parse
def s(a):
    c,q,sp=a
    url="https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(q)+"&sp="+sp
    out=run(["yt-dlp","--skip-download","--flat-playlist","--playlist-end","30","-J",url])
    try: d=json.loads(out)
    except Exception: return []
    if not isinstance(d,dict): return []
    return [{"case":c,"query":"YEAR:"+q,"id":e.get("id"),"title":e.get("title"),"channel":e.get("channel"),"channel_id":e.get("channel_id"),"views":e.get("view_count"),"duration":e.get("duration")} for e in (d.get("entries") or []) if e]
jobs=[(c,q,sp) for c,qs in CASES.items() for q in qs[:2] for sp in ('CAISBAgFEAE%253D','CAMSBAgFEAE%253D')]
flat=json.load(open(f"{OUT}/search_flat.json")); det=json.load(open(f"{OUT}/details.json"))
new=[]
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(s,jobs): new+=r
print(len(new),"date-pass rows")
ids=sorted({r["id"] for r in new if r["id"] and r["id"] not in det})
print(len(ids),"new ids",flush=True)
with cf.ThreadPoolExecutor(16) as ex:
    for vid,d in ex.map(detail,ids):
        if d: det[vid]=d
json.dump(flat+new,open(f"{OUT}/search_flat.json","w"),ensure_ascii=False)
json.dump(det,open(f"{OUT}/details.json","w"),ensure_ascii=False)
print("done",len(det))
