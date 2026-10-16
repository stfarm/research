import json, shutil, os, csv
S = "/tmp/claude-0/-home-user-research/404927b5-0b29-5068-a916-9c45bd2a467c/scratchpad"
os.chdir(S)
tpl = open("report_template.md").read()
RANK = json.load(open("yt/ranking.json"))
FR = json.load(open("yt/frag.json"))
Y = json.load(open("yt/ytd.json"))

NAME = {
 "TH-am-cyanide": ("\"Am Cyanide\" poisonings", "TH"), "MY-mona-fandey": ("Mona Fandey", "MY"), "ID-wongso": ("Jessica Wongso / Mirna", "ID"),
 "PH-sabungeros": ("Missing sabungeros", "PH"), "ID-sambo": ("Ferdy Sambo / Brigadir J", "ID"), "ID-sumanto": ("Sumanto (cannibal)", "ID"),
 "VN-binh-phuoc": ("Bình Phước massacre", "VN"), "PH-maguindanao": ("Maguindanao massacre", "PH"), "PH-ruby-rose": ("Ruby Rose Barrameda", "PH"),
 "PH-chiong": ("Chiong sisters", "PH"), "PH-paloma": ("Pepsi Paloma", "PH"), "ID-vina": ("Vina Cirebon", "ID"), "MY-sosilawati": ("Sosilawati / Banting", "MY"),
 "TH-koh-tao": ("Koh Tao murders", "TH"), "SG-toa-payoh": ("Toa Payoh ritual murders", "SG"), "VN-luyen": ("Lê Văn Luyện", "VN"),
 "PH-vizconde": ("Vizconde massacre", "PH"), "PH-percy-lapid": ("Percy Lapid / Bantag", "PH"), "ID-ryan": ("Ryan \"Jombang\"", "ID"),
 "PH-dacera": ("Christine Dacera", "PH"), "MY-altantuya": ("Altantuya", "MY"), "MY-teoh": ("Teoh Beng Hock", "MY"), "PH-camilon": ("Catherine Camilon", "PH"),
 "PH-degamo": ("Degamo assassination", "PH"), "PH-salilig": ("Salilig hazing", "PH"), "PH-anson-que": ("Anson Que", "PH"), "TH-si-ouey": ("Si Ouey", "TH"),
 "PH-dacer": ("Dacer–Corbito", "PH"), "PH-ranara": ("Jullebee Ranara", "PH"), "TH-redbull": ("Red Bull heir hit-and-run", "TH"), "TH-korat": ("Korat shooting", "TH")}
STATUS = {"PH-vizconde": "SLATE · READY", "MY-mona-fandey": "SLATE · READY", "TH-am-cyanide": "SLATE · READY", "ID-wongso": "SLATE · READY",
          "PH-maguindanao": "SLATE · READY", "PH-sabungeros": "SLATE · RESEARCH", "PH-chiong": "SLATE · RESEARCH", "ID-sambo": "SLATE · RESEARCH",
          "PH-ruby-rose": "SLATE · RESEARCH", "PH-camilon": "SLATE · RESEARCH (cond.)", "PH-paloma": "HOLD", "ID-vina": "HOLD",
          "ID-sumanto": "Reserve (best swap)", "PH-percy-lapid": "Reserve (swap)", "SG-toa-payoh": "Reserve (ready)", "MY-sosilawati": "Reserve (ready)",
          "TH-koh-tao": "Reserve", "VN-binh-phuoc": "Reserve", "PH-dacera": "Reserve", "ID-ryan": "Reserve", "PH-degamo": "Reserve", "PH-ranara": "Reserve",
          "PH-salilig": "Reserve", "PH-dacer": "Reserve", "TH-si-ouey": "Reserve"}
rows = ["| # | Case | Ctry | Composite | Demand | Opport. | Story | Visual | Reliab. | 12-mo views (floor) | 180-day views (videos) | Status |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for k, o in enumerate(RANK, 1):
    n, c = NAME[o["case"]]
    rows.append(f"| {k} | {n} | {c} | **{o['composite']}** | {o['demand']} | {o['opp']} | {o['story']} | {o['visual']} | {o['rel']} | {o['v12']:,} | {o['v180']:,} ({o['n180']}) | {STATUS.get(o['case'], 'Dropped')} |")
rank_table = "\n".join(rows)

ev = []
for c, title in [("PH-vizconde", "Vizconde massacre"), ("MY-mona-fandey", "Mona Fandey"), ("TH-am-cyanide", "Am Cyanide"), ("PH-sabungeros", "Missing sabungeros"),
                 ("ID-wongso", "Wongso / Mirna"), ("PH-chiong", "Chiong sisters"), ("PH-maguindanao", "Maguindanao massacre"), ("ID-sambo", "Sambo / Brigadir J"),
                 ("PH-ruby-rose", "Ruby Rose Barrameda"), ("PH-camilon", "Catherine Camilon")]:
    ev.append(f"**{title}**\n" + FR["evidence"][c])
evidence = "\n\n".join(ev)
evidence += ("\n\n**Sabungeros, additional high-view items from the 12-month sweep (no full metadata):** "
             "[GMA Public Affairs, warrant for Atong Ang](https://youtu.be/RnGu7dZ1hTA) · 2026-01-19 · 641,465 views; "
             "[GMA News, Ang charged by DOJ](https://youtu.be/i_emdzS674g) · 2025-12-22 · 538,943 views; "
             "[DZMM Teleradyo, Patidongan report](https://youtu.be/2nZQy7GlWfU) · 2026-03-23 · 337,794 views.")
cov = ", ".join(f"{NAME[c][0]} {int(v['coverage']*100)}%" for c, v in sorted(Y.items(), key=lambda kv: kv[1]["coverage"]))

out = (tpl.replace("@@RANK_TABLE@@", rank_table).replace("@@EVIDENCE@@", evidence).replace("@@COVERAGE@@", cov)
          .replace("@@ABS_STATS@@", FR["abs_stats"]).replace("@@ABS_TABLE@@", FR["abs_table"])
          .replace("@@COMP_LONG@@", FR["comp_long"]).replace("@@COMP_SHORTS@@", FR["comp_shorts"]))
assert "@@" not in out
R = "/home/user/research"
open(f"{R}/thishappened-sea-nov2026-case-selection.md", "w").write(out)
# data + scripts
os.makedirs(f"{R}/data", exist_ok=True)
os.makedirs(f"{R}/scripts", exist_ok=True)
shutil.copy("yt/relevant2.csv", f"{R}/data/youtube_case_videos.csv")
for a, b in [("yt/case_metrics.json", "case_metrics.json"), ("yt/ranking.json", "ranking.json"), ("yt/ytd.json", "twelve_month_flat_metrics.json"),
             ("yt/competitor_flat.json", "competitor_channels.json")]:
    shutil.copy(a, f"{R}/data/{b}")
with open(f"{R}/data/abs_cbn_series.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["upload_date", "title", "views", "likes", "url"])
    for d in json.load(open("yt/abs_series.json")):
        w.writerow([d["upload_date"], d["title"], d["view_count"], d.get("like_count"), f"https://www.youtube.com/watch?v={d['id']}"])
for fn in ["collect.py", "datepass.py", "channels.py", "abs.py", "metrics.py", "ytd.py", "comp.py", "rank.py", "gen_frag.py", "build.py"]:
    shutil.copy(fn, f"{R}/scripts/{fn}")
print("lines", out.count("\n"), "chars", len(out))
