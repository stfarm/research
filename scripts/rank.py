import json, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from metrics import REL, M
Y = json.load(open("yt/ytd.json"))
ED = {  # story, visual, reliability (editorial 1-5)
 "PH-sabungeros": (5, 4, 3), "TH-am-cyanide": (5, 4, 4), "PH-camilon": (4, 4, 2), "ID-wongso": (5, 5, 4), "PH-vizconde": (4, 3, 4),
 "MY-mona-fandey": (5, 5, 4), "SG-toa-payoh": (5, 4, 4), "PH-chiong": (4, 4, 3), "PH-maguindanao": (4, 3, 4), "PH-anson-que": (4, 4, 3),
 "TH-koh-tao": (4, 4, 3), "PH-degamo": (4, 3, 4), "PH-ruby-rose": (5, 4, 3), "MY-sosilawati": (5, 4, 4), "PH-percy-lapid": (4, 3, 3),
 "PH-dacer": (3, 2, 3), "PH-ranara": (3, 2, 5), "VN-binh-phuoc": (4, 3, 4), "ID-vina": (4, 3, 2), "ID-sambo": (4, 3, 5),
 "PH-dacera": (3, 3, 3), "PH-salilig": (3, 2, 3), "PH-paloma": (3, 2, 2), "TH-korat": (3, 2, 4), "TH-si-ouey": (4, 4, 3),
 "TH-redbull": (3, 3, 4), "ID-sumanto": (4, 3, 4), "ID-ryan": (4, 3, 3), "MY-altantuya": (4, 3, 3), "MY-teoh": (4, 3, 4), "VN-luyen": (3, 3, 3)}
cases = list(REL)


def pct(vals):
    n = len(vals)
    out = []
    for v in vals:
        below = sum(1 for x in vals if x < v)
        equal = sum(1 for x in vals if x == v)
        out.append((below + (equal - 1) / 2) / (n - 1) * 100)
    return out


v12 = [Y[c]["views"] for c in cases]
v180 = [M[c]["v180"] for c in cases]
small = [M[c]["small_wins"] for c in cases]
gap = [M[c]["local_v180"] / (M[c]["en_v180"] + 25000) for c in cases]
p12, p180, psm, pgap = pct(v12), pct(v180), pct(small), pct(gap)
out = []
for i, c in enumerate(cases):
    demand = 0.6 * p12[i] + 0.4 * p180[i]
    opp = 0.5 * psm[i] + 0.5 * pgap[i]
    s, v, r = ED[c]
    comp = 0.40 * demand + 0.15 * opp + 0.15 * (s / 5 * 100) + 0.15 * (r / 5 * 100) + 0.15 * (v / 5 * 100)
    out.append(dict(case=c, demand=round(demand), opp=round(opp), story=s, visual=v, rel=r, composite=round(comp, 1),
                    v12=v12[i], v180=v180[i], n180=M[c]["n180"], small=small[i], ratio=round(gap[i], 1),
                    local180=M[c]["local_v180"], en180=M[c]["en_v180"]))
out.sort(key=lambda o: -o["composite"])
json.dump(out, open("yt/ranking.json", "w"))
print(f"{'#':>2} {'case':15s} comp  dem opp  S V R  v12m        v180      n180 small gap")
for k, o in enumerate(out, 1):
    print(f"{k:2d} {o['case']:15s} {o['composite']:5.1f} {o['demand']:4d} {o['opp']:3d} {o['story']} {o['visual']} {o['rel']} {o['v12']:>10,} {o['v180']:>10,} {o['n180']:4d} {o['small']:3d} {o['ratio']:6.1f}")
