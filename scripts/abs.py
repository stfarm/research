import json, urllib.parse, concurrent.futures as cf
from collect import run, detail, OUT
det=json.load(open(f"{OUT}/details.json"))
ids=set()
for q in ["Philippines' Most Shocking Stories ABS-CBN News EP","Philippines Most Shocking Stories Jessie Cruzat","Philippines' Most Shocking Stories full episode"]:
  for sp in ("EgIQAQ%253D%253D","CAMSAhAB","CAISAhAB"):
    url="https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(q)+"&sp="+sp
    out=run(["yt-dlp","--skip-download","--flat-playlist","--playlist-end","40","-J",url])
    try: d=json.loads(out)
    except: continue
    if not isinstance(d,dict): continue
    for e in d.get("entries") or []:
        if e and "shocking" in (e.get("title") or "").lower() and e.get("channel")=="ABS-CBN News": ids.add(e["id"])
print(len(ids))
with cf.ThreadPoolExecutor(12) as ex:
    for vid,d in ex.map(detail,sorted(ids)):
        if d: det[vid]=d
json.dump(det,open(f"{OUT}/details.json","w"),ensure_ascii=False)
eps=sorted([det[i] for i in ids if i in det],key=lambda d:d["upload_date"])
json.dump(eps,open(f"{OUT}/abs_series.json","w"),ensure_ascii=False)
for d in eps: print(d["upload_date"],f"{d['view_count']:>9,}",d['like_count'],d["title"][:100])
