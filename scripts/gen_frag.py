import json, io, contextlib, statistics as st, datetime as dt, csv
with contextlib.redirect_stdout(io.StringIO()):
    from metrics import REL, M
R2 = json.load(open("yt/relevant2.json"))
RANK = json.load(open("yt/ranking.json"))
Y = json.load(open("yt/ytd.json"))
COMP = json.load(open("yt/competitor_flat.json"))
ABS = json.load(open("yt/abs_series.json"))
CUT = "20260419"


def fmt(n):
    return f"{n:,}"


def vid(r):
    t = r["title"].replace("|", "/").replace("[", "(").replace("]", ")")[:58]
    lk = r["likes"] if r["likes"] is not None else "n/a"
    d = r["upload"]
    return f"[{t}]({r['url']}) · {r['channel'][:24]} · {d[:4]}-{d[4:6]}-{d[6:]} · {fmt(r['views'])} views · {lk} likes · {fmt(int(r['vpd']))}/day"


def evidence(c, n=3):
    rs = sorted([r for r in R2 if r["case"] == c], key=lambda r: -r["views"])
    rec = [r for r in rs if r["upload"] >= CUT][:n]
    top = rs[:2]
    lines = []
    for r in rec:
        lines.append("  - 180d: " + vid(r))
    for r in top:
        if r not in rec:
            lines.append("  - all-time: " + vid(r))
    return "\n".join(lines) if lines else "  - none retrieved"


out = {}
# ABS-CBN series table
eps = [d for d in ABS if d["title"].lower().find("ep") != -1 and "Best of" not in d["title"] and "Podcast" not in d["title"]]
vals = [d["view_count"] for d in eps]
out["abs_stats"] = f"{len(eps)} numbered episodes retrieved; median {fmt(int(st.median(vals)))} views, range {fmt(min(vals))}-{fmt(max(vals))}; 19.3M subscribers on the channel."
rows = []
for d in ABS:
    u = d["upload_date"]
    t = d["title"].replace("Philippines' Most Shocking Stories", "PMSS").replace("Philippines’ Most Shocking Stories", "PMSS").replace("|", "/")[:84]
    rows.append(f"| {u[:4]}-{u[4:6]}-{u[6:]} | [{t}](https://www.youtube.com/watch?v={d['id']}) | {fmt(d['view_count'])} | {fmt(d['like_count']) if d.get('like_count') else 'n/a'} |")
out["abs_table"] = "\n".join(rows)
# competitor table
crow = []
for o in sorted([o for o in COMP if o["tab"] == "videos"], key=lambda o: -o["median"]):
    crow.append(f"| {o['channel'][:34]} | {fmt(o['subs']) if o['subs'] else 'n/a'} | {fmt(o['median'])} | {fmt(o['p75'])} | {fmt(o['max'])} |")
out["comp_long"] = "\n".join(crow)
srow = []
for o in sorted([o for o in COMP if o["tab"] == "shorts"], key=lambda o: -o["median"]):
    srow.append(f"| {o['channel'][:34]} | {fmt(o['subs']) if o['subs'] else 'n/a'} | {o['n']} | {fmt(o['median'])} | {fmt(o['p75'])} | {fmt(o['max'])} |")
out["comp_shorts"] = "\n".join(srow)
# evidence per case
out["evidence"] = {c: evidence(c) for c in REL}
json.dump(out, open("yt/frag.json", "w"), ensure_ascii=False)
print(out["abs_stats"])
print(len(out["abs_table"].splitlines()), "abs rows")
