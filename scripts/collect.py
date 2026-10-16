import json, subprocess, sys, os, concurrent.futures as cf, datetime

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yt")
os.makedirs(OUT, exist_ok=True)

CASES = {
 "PH-sabungeros": ["missing sabungeros", "missing sabungeros Taal Lake", "nawawalang sabungero kaso", "Atong Ang sabungeros Patidongan"],
 "TH-am-cyanide": ["Am Cyanide Thailand serial killer", "Sararat Rangsiwuthaporn cyanide", "แอม ไซยาไนด์"],
 "PH-camilon": ["Catherine Camilon", "Catherine Camilon kaso Allan de Castro", "Catherine Camilon missing beauty queen"],
 "ID-wongso": ["Jessica Wongso Mirna cyanide coffee", "kasus kopi sianida Jessica Wongso", "Ice Cold murder coffee Jessica Wongso"],
 "PH-vizconde": ["Vizconde massacre", "Vizconde massacre Hubert Webb", "Vizconde massacre kwento"],
 "MY-mona-fandey": ["Mona Fandey", "Mona Fandey Mazlan Idris murder", "kes pembunuhan Mona Fandey"],
 "SG-toa-payoh": ["Toa Payoh ritual murders", "Adrian Lim Toa Payoh murders"],
 "PH-chiong": ["Chiong sisters murder", "Chiong sisters Larranaga", "Chiong sisters Cebu kaso"],
 "PH-maguindanao": ["Maguindanao massacre", "Maguindanao massacre Ampatuan", "Maguindanao massacre kwento"],
 "PH-anson-que": ["Anson Que kidnapping", "Anson Que kaso"],
 "TH-koh-tao": ["Koh Tao murders", "Koh Tao murders Hannah Witheridge David Miller"],
 "PH-degamo": ["Degamo killing Teves", "Roel Degamo pamamaslang"],
 "PH-ruby-rose": ["Ruby Rose Barrameda", "Ruby Rose Barrameda kaso"],
 "MY-sosilawati": ["Sosilawati murder Banting", "kes pembunuhan Sosilawati"],
 "PH-percy-lapid": ["Percy Lapid Bantag", "Percy Lapid kaso"],
 "PH-dacer": ["Dacer Corbito", "Bubby Dacer Corbito kaso"],
 "PH-ranara": ["Jullebee Ranara", "Jullebee Ranara kaso"],
 "VN-binh-phuoc": ["Binh Phuoc massacre 2015", "Thảm án Bình Phước Nguyễn Hải Dương"],
 "ID-vina": ["Vina Cirebon", "kasus Vina Cirebon Pegi Setiawan"],
 "ID-sambo": ["Ferdy Sambo Brigadir J", "kasus Brigadir J"],
 "PH-dacera": ["Christine Dacera", "Christine Dacera kaso"],
 "PH-salilig": ["John Matthew Salilig hazing", "Salilig Adamson hazing kaso"],
 "PH-paloma": ["Pepsi Paloma", "Pepsi Paloma kaso"],
 "TH-korat": ["Korat shooting 2020", "Jakrapanth Thomma"],
 "TH-si-ouey": ["Si Ouey cannibal Thailand", "ศรีอุทัย ซีอุยตัวน้อย"],
 "TH-redbull": ["Red Bull heir Vorayuth Yoovidhya hit and run", "Boss Yoovidhya police officer Vichian"],
 "ID-sumanto": ["Sumanto kanibal", "Sumanto cannibal Indonesia"],
 "ID-ryan": ["Ryan Jombang pembunuh berantai", "Very Idham Henyansyah Ryan Jombang"],
 "MY-altantuya": ["Altantuya Shaariibuu", "Altantuya Sirul Azilah"],
 "MY-teoh": ["Teoh Beng Hock", "Teoh Beng Hock MACC death"],
 "VN-luyen": ["Lê Văn Luyện tiệm vàng Ngọc Bích", "Le Van Luyen Bac Giang gold shop murders"],
 # generic regional discovery
 "GEN-PH": ["Philippine true crime", "Pinoy true crime kwento", "pinakasikat na krimen sa Pilipinas", "true crime Philippines documentary", "Philippines most shocking stories"],
 "GEN-SEA": ["Southeast Asia true crime", "Thailand true crime", "Indonesia true crime kasus pembunuhan", "Malaysia true crime kes pembunuhan"],
}

N = 15

def run(cmd, timeout=120):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.stdout
    except Exception as e:
        return ""

def search(args):
    case, q = args
    out = run(["yt-dlp", "--skip-download", "--flat-playlist", "-J", f"ytsearch{N}:{q}"])
    try:
        d = json.loads(out)
    except Exception:
        return case, q, []
    rows = []
    for e in d.get("entries", []):
        rows.append({"case": case, "query": q, "id": e.get("id"), "title": e.get("title"),
                     "channel": e.get("channel"), "channel_id": e.get("channel_id"),
                     "views": e.get("view_count"), "duration": e.get("duration")})
    return case, q, rows

def detail(vid):
    out = run(["yt-dlp", "--skip-download", "--no-playlist", "-J", f"https://www.youtube.com/watch?v={vid}"], 90)
    try:
        d = json.loads(out)
    except Exception:
        return vid, None
    if not isinstance(d, dict):
        return vid, None
    return vid, {k: d.get(k) for k in ("id","title","channel","channel_id","channel_follower_count","view_count","like_count","comment_count","upload_date","duration","language")}

if __name__ == "__main__":
    jobs = [(c, q) for c, qs in CASES.items() for q in qs]
    results = []
    with cf.ThreadPoolExecutor(8) as ex:
        for case, q, rows in ex.map(search, jobs):
            print(f"{case:18s} {q[:45]:45s} {len(rows)}", flush=True)
            results.extend(rows)
    json.dump(results, open(os.path.join(OUT, "search_flat.json"), "w"), ensure_ascii=False)
    print("total rows", len(results))
