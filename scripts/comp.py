import json, statistics as st, datetime as dt
det=json.load(open("yt/details.json")); lst=json.load(open("yt/channel_lists.json")); ids=json.load(open("yt/channel_ids.json"))
TODAY=dt.date(2026,10,16); CUT="20260419"
out=[]
for key,l in lst.items():
    name,tab=key.split("|")
    vs=[det[i] for i,_ in l if i in det and det[i].get("upload_date")]
    if not vs: continue
    rec=[v for v in vs if v["upload_date"]>=CUT]
    def vpd(v): return (v["view_count"] or 0)/max((TODAY-dt.datetime.strptime(v["upload_date"],"%Y%m%d").date()).days,1)
    subs=next((v.get("channel_follower_count") for v in vs if v.get("channel_follower_count")),None)
    out.append(dict(channel=name,tab=tab,subs=subs,n=len(vs),n180=len(rec),med_views_180=int(st.median([v["view_count"] or 0 for v in rec])) if rec else None,max_views_180=max([v["view_count"] or 0 for v in rec]) if rec else None,med_vpd_180=round(st.median([vpd(v) for v in rec]),0) if rec else None,
       best=(max(rec,key=lambda v:v["view_count"] or 0)["title"][:70],max(rec,key=lambda v:v["view_count"] or 0)["id"]) if rec else None))
json.dump(out,open("yt/competitors.json","w"),ensure_ascii=False)
for o in sorted(out,key=lambda o:(o["tab"],-(o["med_views_180"] or 0))):
    print(o["tab"][:6],f"{o['channel'][:30]:30s}",o["subs"],o["n180"],o["med_views_180"],o["max_views_180"],o["med_vpd_180"], (o["best"] or ("",))[0][:50])
