import json, re, statistics as st, datetime as dt, csv
OUT="yt"
flat=json.load(open(f"{OUT}/search_flat.json")); det=json.load(open(f"{OUT}/details.json"))
TODAY=dt.date(2026,10,16); CUT="20260419"
REL={
 "PH-sabungeros":(r"sabunger|e-?sabong|cockfight|atong ang|patidongan|dondon",r""),
 "TH-am-cyanide":(r"am cyanide|sararat|แอม|ไซยาไนด์|thai cyanide|cyanide.*thai|thailand.*cyanide",r""),
 "PH-camilon":(r"camilon",r""),
 "ID-wongso":(r"wongso|mirna|sianida|ice cold",r"lagu|lirik"),
 "PH-vizconde":(r"vizconde",r"full movie"),
 "MY-mona-fandey":(r"mona fandey|mazlan",r""),
 "SG-toa-payoh":(r"toa payoh|adrian lim",r""),
 "PH-chiong":(r"chiong",r""),
 "PH-maguindanao":(r"(maguindanao.*(massacre|minasaker|mass@cr|mass\W?cre|salvage|ampatuan))|ampatuan|minasaker",r"v-150|saf "),
 "PH-anson-que":(r"anson que",r""),
 "TH-koh-tao":(r"koh tao|witheridge",r""),
 "PH-degamo":(r"degamo",r"sara duterte|vp sara"),
 "PH-ruby-rose":(r"barrameda|ruby ?rose.*(kaso|case|navotas|drum|jimenez|murder|pinatay)",r"critical drinker|katy perry|megyn"),
 "MY-sosilawati":(r"sosilawati",r""),
 "PH-percy-lapid":(r"percy lapid|bantag",r"cayetano|lapid fire"),
 "PH-dacer":(r"dacer|corbito",r""),
 "PH-ranara":(r"ranara",r""),
 "VN-binh-phuoc":(r"bình phước|binh phuoc|hải dương|hai duong",r""),
 "ID-vina":(r"vina (cirebon|sebelum)|kasus vina|pegi setiawan|vina.*eky|cirebon.*vina|vina.*pegi",r"lagu|lirik|live|dangdut|adella"),
 "ID-sambo":(r"sambo|brigadir j|yosua",r""),
 "PH-dacera":(r"dacera",r""),
 "PH-salilig":(r"salilig",r""),
 "PH-paloma":(r"paloma",r"full movie|virgin people|krus sa bawat"),
 "TH-korat":(r"korat|jakrapanth|nakhon ratchasima",r""),
 "TH-si-ouey":(r"ouey|ศรีอุทัย|ซีอุย|si quey",r"alhamdulillah|habib|ahmad"),
 "TH-redbull":(r"red ?bull.*(heir|hit|vorayuth|yoovidhya|crash)|vorayuth|yoovidhya|ทายาทกระทิงแดง",r""),
 "ID-sumanto":(r"sumanto",r""),
 "ID-ryan":(r"ryan.*jombang|very idham|jombang",r"nessie"),
 "MY-altantuya":(r"altantuya",r""),
 "MY-teoh":(r"teoh beng hock",r""),
 "VN-luyen":(r"luyện|luyen",r""),
}
LOCAL=re.compile(r"\b(ang|ng|sa|ni|mga|kaso|kwento|pinatay|nawawala|nawawalang|ito|na|pa|ba|po|si|kay|ay|lang|talaga|tunay|totoong|ginahasa|sinapit|nasaan|hustisya|yang|dan|dari|ini|itu|dengan|untuk|kasus|pembunuhan|kisah|misteri|terbongkar|punca|sebenar|kes|pembunuh|dibunuh|dan|di|yg|bagaimana|siapa|apa|bisa|akhirnya|sekarang|dalam|tentang|nasib)\b",re.I)
def is_local(t):
    if re.search(r"[฀-๿À-ỹ぀-ヿ一-鿿]",t): 
        if not re.search(r"[A-Za-z]{4,}.*[A-Za-z]{4,}.*[A-Za-z]{4,}",re.sub(r"[^\x00-\x7F]","",t)): return True
        if re.search(r"[฀-๿Ạ-ỹ]",t): return True
    return len(LOCAL.findall(t))>=2
def age(u): return (TODAY-dt.datetime.strptime(u,"%Y%m%d").date()).days
rows=[]; seen=set()
for r in flat:
    c=r["case"]
    if c not in REL: continue
    d=det.get(r["id"])
    if not d or (c,r["id"]) in seen or not d.get("upload_date"): continue
    t=(d["title"] or "")
    inc,exc=REL[c]
    if not re.search(inc,t,re.I) or (exc and re.search(exc,t+" "+(d["channel"] or ""),re.I)): continue
    seen.add((c,r["id"]))
    a=age(d["upload_date"]); v=d["view_count"] or 0
    rows.append(dict(case=c,id=d["id"],title=t,channel=d["channel"],subs=d.get("channel_follower_count"),views=v,likes=d.get("like_count"),comments=d.get("comment_count"),upload=d["upload_date"],age_days=a,vpd=round(v/max(a,1),1),dur=d.get("duration"),local=is_local(t),url=f"https://www.youtube.com/watch?v={d['id']}"))
json.dump(rows,open(f"{OUT}/relevant2.json","w"),ensure_ascii=False)
with open(f"{OUT}/relevant2.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
M={}
for c in REL:
    rs=[r for r in rows if r["case"]==c]; rec=[r for r in rs if r["upload"]>=CUT]
    rec7=[r for r in rec if r["age_days"]>=7]
    en=[r for r in rec if not r["local"]]; lo=[r for r in rec if r["local"]]
    small=[r for r in rec if (r["subs"] or 0)<500000 and r["views"]>=50000]
    M[c]=dict(n=len(rs),total=sum(r["views"] for r in rs),n180=len(rec),v180=sum(r["views"] for r in rec),
      med_vpd180=round(st.median([r["vpd"] for r in rec7]),0) if rec7 else 0,
      p75_vpd180=round(sorted([r["vpd"] for r in rec7])[int(len(rec7)*0.75)],0) if rec7 else 0,
      ch180=len({r["channel"] for r in rec}),en_v180=sum(r["views"] for r in en),local_v180=sum(r["views"] for r in lo),
      en_n180=len(en),small_wins=len(small),
      top180=(max(rec,key=lambda r:r["views"])["url"],max(rec,key=lambda r:r["views"])["views"],max(rec,key=lambda r:r["views"])["title"][:60]) if rec else None)
json.dump(M,open(f"{OUT}/case_metrics.json","w"),ensure_ascii=False)
print("rows",len(rows), "details",len(det))
print(f"{'case':16s} {'n':>3} {'total':>11} {'n180':>4} {'v180':>10} {'medvpd':>7} {'ch180':>5} {'en_v':>9} {'loc_v':>10} {'small':>5}")
for c,m in sorted(M.items(),key=lambda kv:-kv[1]['v180']):
    print(f"{c:16s} {m['n']:3d} {m['total']:11,} {m['n180']:4d} {m['v180']:10,} {m['med_vpd180']:7.0f} {m['ch180']:5d} {m['en_v180']:9,} {m['local_v180']:10,} {m['small_wins']:5d}")
