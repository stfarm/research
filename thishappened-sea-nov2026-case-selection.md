# ThisHappened — Southeast Asia Case Selection, November 2026 (v2, data-backed)

Prepared 2026-10-16 · Research and selection only · No scripts written, no production started

**Status key:** `READY` = core facts verified against at least two credible sources and legal status current as of the date shown; safe to hand to scripting with the listed conditions. `RESEARCH` = a named gap must close before scripting. `RESERVE` / `HOLD` = not in the November ten.

---

## 1. Executive summary

1. **YouTube data is now real.** I collected public metadata with yt-dlp (no API key, no credentials needed): about 3,800 search results, 2,074 videos with full metadata (views, likes, upload date, channel, subscriber count), view counts for the 40 newest uploads of 25 channels, and 33 items from ABS-CBN's *Philippines' Most Shocking Stories* series. A YouTube rate limit (HTTP 429) stopped the last ~830 lookups; per-case metadata coverage is 79–95% (section 3.3).
2. **ThisHappened's own analytics were not found.** I searched the environment, repository, Google Drive, Notion and Gmail. There is nothing to baseline against, so no baseline is invented. Section 9 lists the exact export I need.
3. **Not obtained:** TikTok, Facebook, Instagram and Google Trends data (Trends returns HTTP 429; the other platforms have no public extraction path that I could reach). Section 2 documents each blocker.
4. **Recommended November slate (10 cases, 6 Philippine):** Vizconde, Mona Fandey, Am Cyanide, Sabungeros, Jessica Wongso/Mirna, Chiong sisters, Maguindanao massacre, Ferdy Sambo/Brigadir J, Ruby Rose Barrameda, Catherine Camilon.
5. **Readiness:** 5 `READY` (Vizconde, Mona Fandey, Am Cyanide, Wongso/Mirna, Maguindanao). 5 `RESEARCH` (Sabungeros, Chiong, Sambo, Ruby Rose, Camilon). Each has a named gap and a due date in section 5.
6. **The evidence changed the plan.** Anson Que, Degamo, Toa Payoh and Koh Tao fell out of the ten because measured demand is low (section 3). Sambo, a case v1 never listed in the top ten, entered on measured demand.
7. **Version 1 contained errors, corrected in section 2.1.** The most important: the Chiong sisters' body-discovery claim, the Pepsi Paloma "acquitted 1985" claim, the Sabungeros charging status, and the Wongso review status.

---

## 2. Method, blockers and corrections

### 2.1 Corrections to v1 (verified this session)

| v1 claim | Verified finding | Source |
|---|---|---|
| Chiong sisters' "bodies never found" | A body was found in a ravine in Tanawan, Carcar City about two days after the 16 Jul 1997 abduction; the family said it was Marijoy. Only **Jacqueline** was never found. Advocacy-sourced material (cited by Wikipedia from Fair Trials International) says the body was never formally identified and was later determined not to be a Chiong sister; I could not reach that primary document. Status: **identification disputed, unresolved**. | [SunStar](https://www.sunstar.com.ph/cebu/local-news/film-hopes-to-quell-rumors-of-daughters-disappearance), [Sugbo.ph](https://sugbo.ph/2024/the-chiong-sisters/), [Wikipedia](https://en.wikipedia.org/wiki/Chiong_murder_case) |
| Larrañaga co-convict releases "2013" | The good-conduct releases were in **Sept 2019** (Aznar, Balansag, Caño, Uy); all four re-surrendered after public outcry. | [Wikipedia](https://en.wikipedia.org/wiki/Chiong_murder_case) |
| Pepsi Paloma accused "acquitted 1985" | No acquittal found. Sources describe the 1982 complaint being **withdrawn** via an affidavit of desistance; Tito Sotto has called the stories "fake news". Her 1985 death is not confirmed by a reliable source I could reach. | [ABS-CBN](https://news.abs-cbn.com/news/08/02/18/sotto-pepsi-paloma-rape-stories-are-fake-news), [Wikipedia](https://en.wikipedia.org/wiki/Pepsi_Paloma) |
| Sabungeros complaint "submitted for resolution"; Barretto named | DOJ indicted Atong Ang and others on **9 Dec 2025**; the complaints against **Gretchen Barretto and Gen. Jonnel Estomo were dismissed** (without prejudice). Cases filed 19 Dec 2025. Arrest warrants: 14 Jan 2026 (Sta. Cruz RTC Br. 26, no bail on kidnapping with homicide), third warrant 6 Feb 2026. Reward raised to P20M. **Ang still at large as of 10 Apr 2026**; I found nothing newer. | [Philstar](https://www.philstar.com/headlines/2025/12/10/2493099/atong-ang-21-others-indicted-sabungero-case/amp/), [Rappler](https://www.rappler.com/philippines/warrant-arrest-atong-ang-no-bail-missing-sabungeros-case/), [Rappler bounty](https://www.rappler.com/philippines/monetary-reward-atong-ang-missing-sabungeros-case-february-12-2026/), [Philstar Apr 2026](https://www.philstar.com/nation/2026/04/10/2519860/atong-ang-eludes-arrest) |
| Wongso review "reportedly processed" | The Supreme Court **rejected her second judicial review (PK) on 14 Aug 2025** (first rejected Dec 2018). She was paroled 18 Aug 2024. No clemency was found. | [JawaPos](https://www.jawapos.com/kasuistika/2508150340/pk-ditolak-ma-jessica-wongso-tetap-dinyatakan-sebagai-pembunuh-mirna-salihin-di-kasus-kopi-sianida), [Tempo](https://en.tempo.co/amp/1905349/jessica-wongso-gets-5-years-remission-on-parole-today) |
| Am Cyanide: "third death sentence 22 Sep 2026; counts differ" | Counts reconcile: 15 cases filed; **8 decided = 3 death, 2 life, 3 acquittals**. Death sentences: 20 Nov 2024 (Siriporn Khanwong), 25 Aug 2026 (Darinee "Fah" Thepwi, the 7th judgment), 22 Sep 2026 (Phetchaburi creditor, the 8th). All under appeal. | [Nation, 25 Aug](https://www.nationthailand.com/news/general/40070234), [The Star, 22 Sep](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/09/22/thai-court-hands-am-cyanide-third-death-sentence-on-sept-22), [Khaosod, 22 Sep](https://www.khaosodenglish.com/news/crimecourtscalamity/courts/2026/09/22/am-cyanide-sentenced-to-death-in-eighth-poisoning-case/) |
| Camilon suspects held with no bail | Charges were first dismissed (May 2024), refiled, and the suspects were later **released on bail**; a friend-witness **withdrew in Aug 2025** citing death threats. I found no 2026 trial reporting. | [Philstar, Aug 2025](https://www.philstar.com/nation/2025/08/04/2462982/witness-withdraws-missing-beauty-queen-case), [Inquirer](https://newsinfo.inquirer.net/1984841/ex-policeman-driver-tagged-in-camilons-disappearance-nabbed-in-batangas/amp) |
| Anson Que court "Pampanga" | Bodies were found in **Rodriguez, Rizal**; no trial court was identified in my sources. | [Wikipedia](https://en.wikipedia.org/wiki/Kidnapping_and_killing_of_Anson_Que) |
| Red Bull heir case "lapsed 2022" | All charges were dropped in 2020, the reckless-driving charge was reinstated, and one report puts its limitation date at **2027**. Officials were moved against in 2024. | [NPR](https://www.npr.org/2020/07/24/894985857/thai-authorities-drop-charges-against-red-bull-billionaire-in-2012-hit-and-run-d), [Malay Mail](https://www.malaymail.com/news/world/2024/08/27/thailand-to-go-after-ex-police-chief-deputy-ag-over-red-bull-heirs-deadly-hit-and-run-case/148333) |
| Lê Văn Luyện "released 2026" (YouTube titles) | Not supported. The first-instance court gave the **maximum 18 years** because of his age. I found no appellate result and no release report; the "ra tù" titles are unverified. | [Tiền Phong](https://tienphong.vn/Phap-Luat/564067/Toi-khong-the-tuyen-an-tu-hinh-Le-Van-Luyen-tpol.html), [VietnamNet](https://vietnamnet.vn/trao-doi-nong-voi-chu-toa-phien-toa-xu-luyen-56747.html) |
| Maguindanao: graves dug *before* the victims arrived | **Unsettled.** The backhoe driver's deposition (AFP) says he dug the pits minutes *after* the shootings; an opinion column says before. Do not state either as fact. | [Inquirer](https://newsinfo.inquirer.net/437157/backhoe-driver-describes-maguindanao-massacre-burial/amp), [Inquirer opinion](https://opinion.inquirer.net/?p=125983) |

### 2.2 Data collection and what was blocked

| Requirement | Result | Detail |
|---|---|---|
| Existing ThisHappened credentials / analytics | **None found** | No YouTube/Google env vars; no matches in the repo; searches of Google Drive, Notion and Gmail found no ThisHappened analytics. A public search for the channel returned several similarly named channels (for example `@ThisHappenedTV`, 6,720 subs) and I cannot tell which is yours. I did not guess. |
| YouTube metadata | **Collected** | yt-dlp 2026.08.19 over the proxy. No API key or login. Search: relevance, plus YouTube "This year" filtered results sorted by date and by views. |
| YouTube rate limit | **Partial blocker** | After ~2,000 detail lookups YouTube returned HTTP 429 and later "confirm you're not a bot". ~830 videos lack upload dates and likes. Slow retry did not recover in this session. |
| Google Trends | **Blocked** | HTTP 429 from the fetch tool. No numbers shown. |
| TikTok / Facebook / Instagram | **Not obtained** | No public API access from this environment. No numbers shown. |
| Local-language search | **Done** | Filipino/Tagalog (kaso, nawawala, totoong kwento), Indonesian/Malay (kasus, kes), Thai, Vietnamese queries run per case. |
| Official YouTube API | **Not required** | Recommended for reliability; see section 9. |

### 2.3 How to read the numbers

- **Views per day** = lifetime views ÷ days since upload. It understates old viral videos' current pace and overstates videos under 7 days old; I exclude videos under 7 days from medians.
- **"12-month views"** uses YouTube's "This year" filter, which returned uploads back to late 2025, so treat it as a rolling ~12 months. It is built from the top ~30 date-sorted and top ~30 view-sorted results per query, so it is a **floor**, not a census.
- **"180-day views"** counts only videos uploaded on or after 2026-04-19 with full metadata. It is also a floor.
- **Title relevance** was filtered with per-case patterns and manually spot-checked. False positives were removed for Ruby Rose (the actress), Vina (music), and Maguindanao military news; some remain possible.
- **English vs local** is a keyword heuristic on titles, not a language detector. Use it directionally.
- **View counts show interest, not quality or conversion.** Nothing here measures subscribers gained.

---

## 3. Verified demand evidence

### 3.1 Ranking (all 31 candidates)

Demand and Opportunity are **computed from YouTube data** (percentile among the 31 cases). Story, Visual and Reliability are **editorial 1–5 scores**, shown separately and weighted explicitly.

**Composite = 40% Demand + 15% Opportunity + 15% Story + 15% Reliability + 15% Visual.**
- **Demand** = 0.6 × pct(12-month views) + 0.4 × pct(180-day views).
- **Opportunity** = 0.5 × pct(count of 180-day videos with ≥50k views from channels under 500k subs) + 0.5 × pct(local-language 180-day views ÷ (English 180-day views + 25k)). High = proven by small channels and thin English supply.

| # | Case | Ctry | Composite | Demand | Opport. | Story | Visual | Reliab. | 12-mo views (floor) | 180-day views (videos) | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "Am Cyanide" poisonings | TH | **88.0** | 98 | 65 | 5 | 4 | 4 | 4,741,507 | 3,843,090 (27) | SLATE · READY |
| 2 | Mona Fandey | MY | **85.9** | 77 | 88 | 5 | 5 | 4 | 1,237,252 | 829,806 (26) | SLATE · READY |
| 3 | Jessica Wongso / Mirna | ID | **81.4** | 76 | 60 | 5 | 5 | 4 | 3,422,029 | 163,528 (18) | SLATE · READY |
| 4 | Missing sabungeros | PH | **79.9** | 87 | 62 | 5 | 4 | 3 | 5,004,512 | 563,861 (23) | SLATE · RESEARCH |
| 5 | Ferdy Sambo / Brigadir J | ID | **78.8** | 77 | 79 | 4 | 3 | 5 | 1,272,004 | 804,303 (39) | SLATE · RESEARCH |
| 6 | Sumanto (cannibal) | ID | **76.0** | 89 | 50 | 4 | 3 | 4 | 1,528,540 | 1,361,016 (15) | Reserve (best swap) |
| 7 | Bình Phước massacre | VN | **74.8** | 69 | 96 | 4 | 3 | 4 | 991,312 | 665,523 (35) | Reserve |
| 8 | Maguindanao massacre | PH | **74.6** | 83 | 55 | 4 | 3 | 4 | 2,825,017 | 583,843 (16) | SLATE · READY |
| 9 | Ruby Rose Barrameda | PH | **74.6** | 84 | 33 | 5 | 4 | 3 | 2,643,342 | 794,708 (11) | SLATE · RESEARCH |
| 10 | Chiong sisters | PH | **68.2** | 76 | 32 | 4 | 4 | 3 | 1,002,927 | 1,022,760 (23) | SLATE · RESEARCH |
| 11 | Pepsi Paloma | PH | **68.0** | 83 | 91 | 3 | 2 | 2 | 1,314,180 | 1,072,070 (13) | HOLD |
| 12 | Vina Cirebon | ID | **66.9** | 71 | 78 | 4 | 3 | 2 | 1,393,752 | 274,406 (13) | HOLD |
| 13 | Sosilawati / Banting | MY | **65.8** | 50 | 45 | 5 | 4 | 4 | 807,808 | 68,616 (4) | Reserve (ready) |
| 14 | Koh Tao murders | TH | **62.5** | 58 | 42 | 4 | 4 | 3 | 587,770 | 576,544 (7) | Reserve |
| 15 | Toa Payoh ritual murders | SG | **62.2** | 37 | 57 | 5 | 4 | 4 | 258,833 | 62,185 (5) | Reserve (ready) |
| 16 | Lê Văn Luyện | VN | **62.2** | 56 | 85 | 3 | 3 | 3 | 611,966 | 424,641 (24) | Dropped |
| 17 | Vizconde massacre | PH | **60.3** | 53 | 40 | 4 | 3 | 4 | 564,554 | 494,942 (18) | SLATE · READY |
| 18 | Percy Lapid / Bantag | PH | **59.9** | 45 | 80 | 4 | 3 | 3 | 475,500 | 146,496 (5) | Reserve (swap) |
| 19 | Ryan "Jombang" | ID | **59.8** | 53 | 57 | 4 | 3 | 3 | 846,537 | 111,199 (26) | Reserve |
| 20 | Christine Dacera | PH | **51.9** | 45 | 45 | 3 | 3 | 3 | 328,825 | 224,121 (14) | Reserve |
| 21 | Altantuya | MY | **48.0** | 29 | 42 | 4 | 3 | 3 | 246,084 | 6,518 (7) | Dropped |
| 22 | Teoh Beng Hock | MY | **45.8** | 23 | 25 | 4 | 3 | 4 | 48,715 | 6,846 (8) | Dropped |
| 23 | Catherine Camilon | PH | **45.2** | 30 | 22 | 4 | 4 | 2 | 77,284 | 44,097 (3) | SLATE · RESEARCH (cond.) |
| 24 | Degamo assassination | PH | **44.9** | 16 | 37 | 4 | 3 | 4 | 8,028 | 1,764 (1) | Reserve |
| 25 | Salilig hazing | PH | **42.7** | 27 | 52 | 3 | 2 | 3 | 58,208 | 58,208 (2) | Reserve |
| 26 | Anson Que | PH | **42.2** | 17 | 17 | 4 | 4 | 3 | 8,368 | 1,611 (1) | Dropped |
| 27 | Si Ouey | TH | **40.7** | 9 | 28 | 4 | 4 | 3 | 3,434 | 481 (5) | Reserve |
| 28 | Dacer–Corbito | PH | **36.5** | 20 | 30 | 3 | 2 | 3 | 59,996 | 612 (8) | Reserve |
| 29 | Jullebee Ranara | PH | **34.0** | 0 | 27 | 3 | 2 | 5 | 60 | 60 (1) | Reserve |
| 30 | Red Bull heir hit-and-run | TH | **33.8** | 3 | 17 | 3 | 3 | 4 | 424 | 354 (1) | Dropped |
| 31 | Korat shooting | TH | **33.2** | 9 | 17 | 3 | 2 | 4 | 1,037 | 1,037 (3) | Dropped |

Reading the table: **Am Cyanide's** demand is dominated by one 3.16M-view video (Nadia Omara); treat its lead as event-driven (court verdicts 25 Aug and 22 Sep 2026). **Wongso's** 12-month figure is mostly one Nov 2025 video (1.97M); 180-day demand is modest (164k). **Sabungeros** has the broadest base (83 videos, 5.0M) but mostly from news outlets, not storytellers.

### 3.2 Evidence for the slate (links verified from yt-dlp output; counts as of 2026-10-16)

**Vizconde massacre**
  - 180d: [THE VIZCONDE FAMILY CASE / DOKYU SA DILIM](https://www.youtube.com/watch?v=wneiObaooBk) · Papa Dudut · 2026-07-24 · 441,565 views · 4552 likes · 5,256/day
  - 180d: [DALAGA GINAHASA NG ANAK NI CONGRESSMAN / Vizconde Massacre](https://www.youtube.com/watch?v=ED6UHv1e2xE) · Alamin PH · 2026-06-14 · 44,076 views · 407 likes · 355/day
  - 180d: [Vizconde Massacre: Sino Talaga ang Pumatay sa Pamilyang Vi](https://www.youtube.com/watch?v=ZrtIYNquLNs) · Manunudlo Archive · 2026-09-08 · 2,126 views · 23 likes · 55/day
  - all-time: [BUONG ISTORYA NG VIZCONDE MASSACRE (Tagalog Crime Story)](https://www.youtube.com/watch?v=XooxkmRZreE) · Tagalog Crime Stories · 2023-04-09 · 1,440,373 views · 16877 likes · 1,120/day
  - all-time: [TV Patrol: A look back: The Vizconde massacre](https://www.youtube.com/watch?v=Npe506tp1E0) · ABS-CBN News · 2010-04-23 · 950,132 views · 3230 likes · 157/day

**Mona Fandey**
  - 180d: [THE TIGER SHOW PODCAST/ S2 / EP85 / Bomoh, jenayah dan pol](https://www.youtube.com/watch?v=nZbSYrraLGg) · The Tiger Show Podcast · 2026-09-17 · 222,131 views · 1641 likes · 7,659/day
  - 180d: [【膽小勿看】快點走！不走會S！多人敲碗的Mona Fandey的祭壇！拋X案發地！很多靈動！強行救走小鬼？殘留許多黑](https://www.youtube.com/watch?v=MWZUcqupLDU) · 蟬團長 InsectAngTV · 2026-06-03 · 133,803 views · 3258 likes · 991/day
  - 180d: [Punca Sebenar Mona Fandey Bunuh Datuk — Terbongkar](https://www.youtube.com/watch?v=hw9EQE0xT_c) · Rahman Azman · 2026-06-03 · 105,205 views · 806 likes · 779/day
  - all-time: [B:File - Mona Fandey](https://www.youtube.com/watch?v=Za4z6F_ZZKc) · BERNAMA TV · 2016-10-10 · 1,142,494 views · 4870 likes · 312/day
  - all-time: [The Real Life Witch Of Malaysia... Mona Fandey / Mysteries](https://www.youtube.com/watch?v=CkglqxceqYY) · Sneaky Sushii · 2024-09-12 · 716,623 views · 13052 likes · 938/day

**Am Cyanide**
  - 180d: [KASUS PALING MENGGEGERKAN THAILAND - THE THAI CYANIDE KILL](https://www.youtube.com/watch?v=IbopsT02t04) · Nadia Omara · 2026-05-30 · 3,157,020 views · 80745 likes · 22,712/day
  - 180d: [พิพากษาประหารชีวิต “แอม ไซยาไนด์” วางยาฆ่า “ฟ้า”](https://www.youtube.com/watch?v=suAopLK7vvA) · ครอบครัวข่าว3 · 2026-08-25 · 504,208 views · 3168 likes · 9,696/day
  - 180d: [ศาลอาญา สั่งประหารชีวิต “แอม ไซยาไนด์” คดีที่ 7 วางยาเพื่อ](https://www.youtube.com/watch?v=wEnKyP-pgV4) · Bright TV · 2026-08-25 · 60,056 views · 461 likes · 1,154/day
  - all-time: [ตอน 1 คดี "แอม ไซยาไนด์" l EP.1444 l 25 เม.ย.66 #โหนกระแส](https://www.youtube.com/watch?v=B7HxkgPp-5s) · โหนกระแส [Hone-Krasae] o · 2023-04-25 · 2,486,708 views · 27109 likes · 1,958/day

**Missing sabungeros**
  - 180d: [2 PNP officials, sinibak sa pwesto sa umano’y pakikialam s](https://www.youtube.com/watch?v=giLqZI2ZRIw) · TV5 News Philippines · 2026-05-21 · 222,741 views · 1577 likes · 1,505/day
  - 180d: [Pamilya ng mga missing sabungero, sinusuhulan umano para h](https://www.youtube.com/watch?v=lnG5GYSla90) · UNTV News and Rescue · 2026-05-20 · 190,127 views · 1555 likes · 1,276/day
  - 180d: [₱30-M Per Complainant? Aregluhan sa kaso ng missing sabung](https://www.youtube.com/watch?v=G3HDuFCjfOA) · Bilyonaryo News Channel · 2026-07-21 · 71,519 views · 485 likes · 822/day
  - all-time: [Mastermind diumano sa pagdukot sa Lost Sabungeros, pinanga](https://www.youtube.com/watch?v=0BU6zpThLSY) · GMA Public Affairs · 2025-07-07 · 3,749,971 views · 19442 likes · 8,047/day
  - all-time: [Paghaharap ni Dondon Patidongan at ng pamilya ng mga nawaw](https://www.youtube.com/watch?v=GqerYtj3UnI) · GMA Public Affairs · 2025-07-17 · 1,874,529 views · 7381 likes · 4,110/day

**Wongso / Mirna**
  - 180d: [Ini kata Jessica jika bertemu ayah Mirna Salihin #podcast ](https://www.youtube.com/watch?v=1HCK98-2Xto) · Mereka Berbicara  · 2026-07-18 · 111,914 views · 993 likes · 1,243/day
  - 180d: [CONDENADA por ENVENENAR a su MEJOR AMIGA con una TAZA DE C](https://www.youtube.com/watch?v=24FPACqIR9Y) · RELATOS CRIMINALES · 2026-09-02 · 30,557 views · 595 likes · 694/day
  - 180d: [KASUS KOPI SIANIDA: MISTERI KEM4T1AN MIRNA YANG MASIH DIPE](https://www.youtube.com/watch?v=KEQ2uTS6EqU) · Kronika · 2026-05-23 · 14,166 views · n/a likes · 97/day
  - all-time: [Ice Cold: Murder, Coffee and Jessica Wongso / Trailer Resm](https://www.youtube.com/watch?v=SoBwAbSTVSE) · Netflix Indonesia · 2023-08-31 · 44,329,851 views · 268344 likes · 38,817/day
  - all-time: [DR. DJAJA : MIRNA BUKAN MATI KARENA SIANIDA?! INI FAKTA FO](https://www.youtube.com/watch?v=taSECI9NQ4g) · dr. Richard Lee, MARS · 2023-10-06 · 8,192,193 views · 157064 likes · 7,407/day

**Chiong sisters**
  - 180d: [EP26: Abduction in the Rain: The Chiong Sisters Case / Phi](https://www.youtube.com/watch?v=naUtL2yGwfE) · ABS-CBN News · 2026-04-21 · 901,758 views · 6138 likes · 5,066/day
  - 180d: [THE CHIONG SISTERS CASE / DOKYU SA DILIM](https://www.youtube.com/watch?v=kZaYIf1uigo) · Papa Dudut · 2026-07-21 · 91,936 views · 1229 likes · 1,056/day
  - 180d: [ANG KASO NG MAGKAPATID NA CHIONG SA CEBU - DOCUMENTARY (Ta](https://www.youtube.com/watch?v=WrdvqGsju00) · Tagalog Crime Story Arch · 2026-08-10 · 13,611 views · 121 likes · 203/day
  - all-time: [THE CONTROVERSIAL CASE OF CHIONG SISTERS!](https://www.youtube.com/watch?v=okQpWse6AK0) · Raffy Tulfo in Action · 2018-07-20 · 2,575,272 views · 26403 likes · 855/day
  - all-time: [ANG MAGULONG KASO NA YUMANIG SA CEBU - CHIONG SISTERS (Tag](https://www.youtube.com/watch?v=0XMtPU1XwtU) · Tagalog Crime Stories · 2023-02-10 · 1,688,952 views · 20302 likes · 1,256/day

**Maguindanao massacre**
  - 180d: [Puntod ng mga Minasaker sa Maguindanao, Nasa Bundok!](https://www.youtube.com/watch?v=b_0YP1M6lXs) · MASTER GALA  · 2026-09-12 · 375,044 views · 5471 likes · 11,030/day
  - 180d: [Madugong kasaysayan ng Maguindanao Massacre (Full Episode)](https://www.youtube.com/watch?v=Jr6PmLTFdT0) · GMA Public Affairs · 2026-08-26 · 138,081 views · 865 likes · 2,707/day
  - 180d: [Pagkilala kay Reynaldo Momay, bilang 58th victim sa Maguin](https://www.youtube.com/watch?v=WWgTdZbM7bw) · UNTV News and Rescue · 2026-08-15 · 35,939 views · 257 likes · 579/day
  - all-time: [Maguindanao Massacre Story / Kababaihan kalunos-lunos ang ](https://www.youtube.com/watch?v=2IkFXo54nqc) · Alamin PH · 2023-03-03 · 2,874,337 views · 19700 likes · 2,172/day
  - all-time: [EP 14: Sins of A Ruling Clan: The 2009 Ampatuan Massacre /](https://www.youtube.com/watch?v=4to5nXRnZHU) · ABS-CBN News · 2025-11-18 · 1,805,135 views · 11070 likes · 5,437/day

**Sambo / Brigadir J**
  - 180d: [Skenario Sang Jenderal: Kasus Kematian Brigadir J yang Men](https://www.youtube.com/watch?v=sV7dx6lE5hE) · ScaryLine · 2026-09-27 · 196,635 views · 411 likes · 10,349/day
  - 180d: [Ada Dugaan Ferdy Sambo Tinggal di "Apartemen Mewah" Lapas ](https://www.youtube.com/watch?v=Wazh8VTWcmA) · Kompascom Reporter on Lo · 2026-09-24 · 113,117 views · 220 likes · 5,141/day
  - 180d: [Begini Kondisi Ferdy Sambo Sekarang di Dalam Lapas Cibinon](https://www.youtube.com/watch?v=cChJF8k-WwA) · VIVA.CO.ID · 2026-10-03 · 60,991 views · 207 likes · 4,691/day
  - all-time: [(FULL) Pengakuan Sopir Ambulans Saat Evakuasi Jenazah Brig](https://www.youtube.com/watch?v=ZriDaJlL0lU) · KOMPASTV · 2022-11-07 · 10,992,804 views · 81520 likes · 7,639/day
  - all-time: [Sketsa Peristiwa Pembunuhan Brigadir J: Ditembak dari Jara](https://www.youtube.com/watch?v=dnfHyeKEByo) · Najwa Shihab · 2022-08-21 · 5,252,003 views · 83036 likes · 3,462/day

**Ruby Rose Barrameda**
  - 180d: [EP29: A Secret Sealed in Steel: The Ruby Rose Barrameda Ca](https://www.youtube.com/watch?v=taXQoFRSa6s) · ABS-CBN News · 2026-05-12 · 641,351 views · 5294 likes · 4,085/day
  - 180d: [RUBY ROSE BARRAMEDA STORY / DOKYU SA DILIM](https://www.youtube.com/watch?v=i-md2dl48Ho) · Papa Dudut · 2026-06-05 · 66,470 views · 1062 likes · 499/day
  - 180d: [SOCO: Rose Barrameda murder case / SOCO sa DZMM](https://www.youtube.com/watch?v=Ty_M9K70fAY) · DZMM Teleradyo · 2026-07-19 · 38,855 views · 264 likes · 436/day
  - all-time: [MAILAP NA HUSTISYA NI RUBY ROSE BARRAMEDA (Tagalog Crime S](https://www.youtube.com/watch?v=JShEoX6nu5E) · Tagalog Crime Stories · 2023-07-07 · 1,120,097 views · 14899 likes · 935/day

**Catherine Camilon**
  - 180d: [Ang pagkawala nina Geneva Lopez at Catherine Camilon (Full](https://www.youtube.com/watch?v=ThzaaOpjTGQ) · GMA Public Affairs · 2026-10-14 · 44,011 views · 122 likes · 22,005/day
  - 180d: [Ang Misteryo ng Pagkawala at Huling Biyahe ng Isang Beauty](https://www.youtube.com/watch?v=Jae3eOxUqL8) · Manunudlo Archive · 2026-08-29 · 83 views · 2 likes · 1/day
  - 180d: [CATHERINE CAMILON: 1,093 ARAW NAWAWALA](https://www.youtube.com/watch?v=MPPn5J760GU) · Dokyu sa Dilim · 2026-10-09 · 3 views · n/a likes · 0/day
  - all-time: [Nasaan na nga ba ang beauty queen na si Catherine Camilon?](https://www.youtube.com/watch?v=ZDEwJevU4NM) · GMA Public Affairs · 2023-11-20 · 2,532,850 views · 16406 likes · 2,387/day
  - all-time: [CATHERINE CAMILON LATEST UPDATE / SUSPEK ALLAN DE CASTRO K](https://www.youtube.com/watch?v=cQjnRaF3Z1E) · Senyora Buzz · 2024-03-19 · 2,196,758 views · 14807 likes · 2,334/day

**Sabungeros, additional high-view items from the 12-month sweep (no full metadata):** [GMA Public Affairs, warrant for Atong Ang](https://youtu.be/RnGu7dZ1hTA) · 2026-01-19 · 641,465 views; [GMA News, Ang charged by DOJ](https://youtu.be/i_emdzS674g) · 2025-12-22 · 538,943 views; [DZMM Teleradyo, Patidongan report](https://youtu.be/2nZQy7GlWfU) · 2026-03-23 · 337,794 views.

### 3.3 Metadata coverage per case

Share of search results for which full metadata was retrieved: Koh Tao murders 79%, Ryan "Jombang" 79%, Anson Que 80%, Ruby Rose Barrameda 80%, Pepsi Paloma 80%, Ferdy Sambo / Brigadir J 82%, Maguindanao massacre 83%, Bình Phước massacre 84%, Altantuya 84%, Vizconde massacre 85%, Vina Cirebon 85%, Korat shooting 85%, Mona Fandey 86%, Percy Lapid / Bantag 86%, Christine Dacera 86%, Si Ouey 86%, Lê Văn Luyện 86%, Missing sabungeros 87%, Jessica Wongso / Mirna 87%, Chiong sisters 87%, Sumanto (cannibal) 87%, Salilig hazing 88%, Dacer–Corbito 89%, Teoh Beng Hock 90%, Toa Payoh ritual murders 91%, Jullebee Ranara 93%, "Am Cyanide" poisonings 94%, Catherine Camilon 94%, Degamo assassination 94%, Sosilawati / Banting 95%, Red Bull heir hit-and-run 95%

---

## 4. Competitive landscape

### 4.1 ABS-CBN News — *Philippines' Most Shocking Stories* (19.3M subscribers)

28 numbered episodes retrieved; median 928,720 views, range 290,252-2,153,963; 19.3M subscribers on the channel. Cases already covered by ABS-CBN in the retrieved set: **Maguindanao (EP14, 1.81M), Chiong (EP26, 0.90M), Ruby Rose Barrameda (EP29, 0.64M)**, Dindin Palma, Joanna Demafelis, Flor Contemplacion and others. I did **not** find Sabungeros, Vizconde or Camilon episodes in the retrieved set (the set is incomplete: EP1–4, 6, 8, 12–13, 23–24 were not retrieved).

Implication: for Maguindanao, Chiong and Ruby Rose we compete against a 19M-subscriber channel's 45-minute episodes. Our differentiator is format (Shorts-length, English with Taglish text), not coverage.

| Date | Episode | Views | Likes |
|---|---|---|---|
| 2025-08-12 | [PMSS / EP 5: Stuffed in a Suitcase: The Dindin Palma Murder Case](https://www.youtube.com/watch?v=U9j3onxZ5BI) | 1,489,644 | 10,058 |
| 2025-08-26 | [PMSS / EP 7: A Body in the Freezer: The Murder of OFW Joanna Demafelis](https://www.youtube.com/watch?v=U0vuQZkfrJE) | 992,687 | 6,273 |
| 2025-09-09 | [PMSS / EP 9: A Crime of Passion and Mutilation](https://www.youtube.com/watch?v=1_OJDBNLmVc) | 1,576,994 | 8,490 |
| 2025-09-16 | [PMSS / EP 10: Left for Dead: Myrna Diones Pins Police in Massacre](https://www.youtube.com/watch?v=Qo4kwIiejl0) | 2,153,963 | 16,144 |
| 2025-10-28 | [EP 11: A Fourteen-Year Manhunt: The Ecleo Murder Case / PMSS](https://www.youtube.com/watch?v=dD3mOTgN7gc) | 1,463,453 | 9,312 |
| 2025-11-18 | [EP 14: Sins of A Ruling Clan: The 2009 Ampatuan Massacre / PMSS](https://www.youtube.com/watch?v=4to5nXRnZHU) | 1,805,135 | 11,070 |
| 2025-11-25 | [EP 15: Star Fights Back for Justice: The Maggie de la Riva Case / PMSS](https://www.youtube.com/watch?v=UY0jK7hvhGQ) | 933,551 | 6,491 |
| 2025-12-02 | [EP 16: The Christine Silawan Case / PMSS](https://www.youtube.com/watch?v=8NBz4jiQ3kA) | 1,198,381 | 5,841 |
| 2025-12-09 | [EP17: The Baby-Faced Killer: The Gonzales Family Murders / PMSS](https://www.youtube.com/watch?v=N3Spuz4DVCE) | 1,255,206 | 6,698 |
| 2025-12-16 | [EP18: Hell and High Water: The 1991 Ormoc Tragedy / PMSS](https://www.youtube.com/watch?v=LK0t6-Szi4s) | 865,679 | 5,252 |
| 2026-01-06 | [EP19: Buried in the Septic Tank: The Evelyn Sayos Case / PMSS](https://www.youtube.com/watch?v=HrTW2avTu-8) | 1,432,314 | 9,102 |
| 2026-01-14 | [EP20: What Really Happened in the Maguad Sibling Case? / PMSS](https://www.youtube.com/watch?v=PUzA-7wKQnQ) | 457,672 | 2,923 |
| 2026-03-10 | [EP21: Death of a Love Story: The Cochise-Beebom Case / PMSS](https://www.youtube.com/watch?v=-JA3FB13tC4) | 923,889 | 5,881 |
| 2026-03-17 | [EP22: High Rise Killing: The Murder of a Bank Teller / PMSS](https://www.youtube.com/watch?v=j5QVP6K4PbM) | 692,455 | 4,820 |
| 2026-04-14 | [EP25: Betrayed and Disposed: The Tania Camille Dee Case / PMSS](https://www.youtube.com/watch?v=LktjkHpw4Ys) | 619,702 | 3,392 |
| 2026-04-21 | [EP26: Abduction in the Rain: The Chiong Sisters Case / PMSS](https://www.youtube.com/watch?v=naUtL2yGwfE) | 901,758 | 6,138 |
| 2026-04-28 | [EP27: Fall of an Action Star: The Eddie Fernandez Case / PMSS](https://www.youtube.com/watch?v=nJh7H0KQA2I) | 650,110 | 4,292 |
| 2026-05-05 | [EP28: Made in the Philippines: The ILOVEYOU Virus Web Outbreak / PMSS](https://www.youtube.com/watch?v=es4UA3_0aow) | 424,393 | 3,038 |
| 2026-05-12 | [EP29: A Secret Sealed in Steel: The Ruby Rose Barrameda Case / PMSS](https://www.youtube.com/watch?v=taXQoFRSa6s) | 641,351 | 5,294 |
| 2026-05-19 | [EP30: 'Til Death Do Us Part: The Case of Mayor Gisela Boniel / PMSS](https://www.youtube.com/watch?v=KKcB1gdNIY0) | 586,683 | 3,681 |
| 2026-05-26 | [PMSS: A Podcast Special (Part 1) / ABS-CBN News](https://www.youtube.com/watch?v=nKOOsyjk25s) | 122,497 | 1,065 |
| 2026-08-06 | [Best of PMSS Season 2 (Hosted by Gus Abelgas) / ABS-CBN News](https://www.youtube.com/watch?v=AvGlf_8Ypps) | 974,793 | 6,333 |
| 2026-08-13 | [Best of PMSS Season 3 (Hosted by Gus Abelgas) / ABS-CBN News](https://www.youtube.com/watch?v=8eDtPFj_mWk) | 1,645,073 | 8,794 |
| 2026-08-20 | [Best of PMSS (Hosted by Gus Abelgas) / ABS-CBN News](https://www.youtube.com/watch?v=sLqnpEg9P0Y) | 832,741 | 5,253 |
| 2026-08-25 | [EP31: Appetite for Death: Did A Wedding Guest Become the Meal? / PMSS](https://www.youtube.com/watch?v=4Ngn2pwRpFA) | 1,591,010 | 10,188 |
| 2026-09-01 | [EP 32: Ride and Die — The Dominguez Carnap Gang Killings / PMSS](https://www.youtube.com/watch?v=Q99EFBX-iIM) | 971,846 | 4,019 |
| 2026-09-08 | [EP 33: The Scammer Who Faked Her Death to Rob Manila's Rich / PMSS](https://www.youtube.com/watch?v=GQkO5CbfNAk) | 1,377,961 | 4,665 |
| 2026-09-15 | [EP 34: The Finish Line — Murder of Race Car Driver Enzo Pastor / PMSS](https://www.youtube.com/watch?v=iWGOfncvWpA) | 1,040,570 | 4,123 |
| 2026-09-22 | [EP 35: A Hanging Suspicion — The Story of Flor Contemplacion / PMSS](https://www.youtube.com/watch?v=7V6NkbFHT34) | 871,968 | 3,682 |
| 2026-09-29 | [EP 36: Condemned to Die — The Execution of Leo Echegaray / PMSS](https://www.youtube.com/watch?v=XJd4kPgsB9o) | 606,886 | 2,300 |
| 2026-10-06 | [EP 37: Waray-Waray Gang Kidnap-Slay: The Betti Chua Sy Case / PMSS](https://www.youtube.com/watch?v=Yt6MmyJqpLU) | 580,059 | 2,929 |
| 2026-10-13 | [EP 38: Faith Laced with Poison — The 1985 Sinasa Tragedy / PMSS](https://www.youtube.com/watch?v=tfpdgXrJR6g) | 290,252 | 1,296 |

### 4.2 Independent regional channels — newest 40 long-form uploads

Medians come from the channel's newest 40 uploads (listing order), so they reflect recent typical performance, not a date window.

| Channel | Subs | Median views | 75th pct | Max |
|---|---|---|---|---|
| Nadia Omara | 16,800,000 | 3,750,000 | 8,500,000 | 15,000,000 |
| Coffeehouse Crime | 2,200,000 | 511,000 | 675,000 | 1,000,000 |
| MysMania - มิสมาเนีย | 426,000 | 466,500 | 664,000 | 1,600,000 |
| Alamin PH | 409,000 | 424,000 | 1,700,000 | 3,400,000 |
| Dark Asia with Megan | 1,280,000 | 324,500 | 574,000 | 1,400,000 |
| Utol Ford | 387,000 | 277,000 | 539,000 | 2,000,000 |
| Sneaky Sushii | 730,000 | 275,000 | 443,000 | 1,300,000 |
| Tagalog Crime Stories | 889,000 | 230,000 | 323,000 | 583,000 |
| Detektif Mat Despatch | 871,000 | 114,000 | 155,000 | 1,000,000 |
| Papa Dudut | 2,590,000 | 105,500 | 135,000 | 234,000 |
| Philippine Shocking History | 869,000 | 89,500 | 200,000 | 843,000 |
| Tagalog Crime Files  | 32,500 | 63,000 | 102,000 | 894,000 |
| Rahsia Silam | 31,800 | 48,500 | 100,000 | 433,000 |
| Grim Asia | 20,800 | 11,000 | 25,000 | 243,000 |
| Tagalog Crime Real Stories | 113,000 | 10,500 | 17,000 | 77,000 |
| Crime & Conspiracy | 3,500 | 2,900 | 9,600 | 125,000 |
| Dark Crimes Reel | 7,240 | 2,200 | 4,500 | 52,000 |
| Senyora Buzz | 340,000 | 1,400 | 1,900 | 6,000 |
| Kronika | 449 | 1,300 | 3,700 | 77,000 |
| Tagalog Crime Story Archives | 434 | 1,182 | 4,600 | 48,000 |
| CREEPY SARDINAS -Tagalog Horror St | 176 | 322 | 517 | 1,400 |
| Insider Stories | 3,370 | 292 | 687 | 366,000 |
| Manunudlo Archive | 2,800 | 174 | 549 | 7,700 |

**Findings (descriptive only):**
- **Alamin PH** (409k subs) has a median of 424k and a 75th percentile of 1.7M, ahead of channels with 2–6× its subscribers. Its Pepsi Paloma video drew 700k views in 180 days. A small Filipino channel can win with a single dark-history angle.
- **Tagalog Crime Stories** (889k) is steady: median 230k, best 583k.
- **Papa Dudut / Dokyu sa Dilim** (2.59M subs) sits at a 105k median. Its Vizconde (442k), Dacera (164k) and Chiong (92k) videos are among the strongest Filipino storyteller case videos of the last 180 days (Alamin PH's Paloma video, 700k, is higher).
- English-language regional channels: **Dark Asia with Megan** (1.28M) median 325k; **Sneaky Sushii** (730k) median 275k; **Coffeehouse Crime** (2.2M) median 511k.

### 4.3 Shorts (newest ≤40 Shorts per channel; only channels that have a Shorts tab)

| Channel | Subs | Shorts sampled | Median views | 75th pct | Max |
|---|---|---|---|---|---|
| Nadia Omara | 16,800,000 | 40 | 319,500 | 534,000 | 2,800,000 |
| Coffeehouse Crime | 2,200,000 | 9 | 122,000 | 220,000 | 266,000 |
| Sneaky Sushii | 730,000 | 40 | 27,500 | 41,000 | 675,000 |
| Dark Asia with Megan | 1,280,000 | 40 | 23,000 | 39,000 | 136,000 |
| Detektif Mat Despatch | 871,000 | 17 | 20,000 | 33,000 | 161,000 |
| Senyora Buzz | 340,000 | 9 | 12,000 | 12,000 | 27,000 |
| Papa Dudut | 2,590,000 | 40 | 5,500 | 6,800 | 17,000 |
| Tagalog Crime Real Stories | 113,000 | 8 | 636 | 1,800 | 4,000 |
| Grim Asia | 20,800 | 10 | 172 | 227 | 775 |
| CREEPY SARDINAS -Tagalog Horror St | 176 | 17 | 23 | 53 | 1,300 |

**Findings:** Filipino storytellers' Shorts are weak (Papa Dudut median 5.5k on 2.59M subs; Tagalog Crime Real Stories 636). English SEA Shorts are mixed: Nadia Omara 320k (a 16.8M-sub Indonesian channel), Sneaky Sushii 27.5k, Dark Asia 23k. **Hypothesis, not a finding:** a Shorts-first English/Taglish Southeast Asia lane has little direct competition. Whether Shorts viewers subscribe is untested; section 8 tests it.

---

## 5. November slate (10 cases, 6 Philippine)

Order alternates Philippine and regional cases and puts `READY` cases first so research can close on the others. Dates are Mon/Thu with one Saturday.

| # | Date | Case | Country | Status | Confidence | Gate |
|---|---|---|---|---|---|---|
| 1 | Mon 2 Nov | Vizconde massacre | PH | **READY** | High | Resolve SC docket numbers (sources conflict) before on-screen text |
| 2 | Thu 5 Nov | Mona Fandey | MY | **READY** | Medium-High | Avoid exact murder date and cash amount; verify 2001 execution date against Dawn/Bernama archive |
| 3 | Mon 9 Nov | "Am Cyanide" | TH | **READY** | High | State "as of" date; 7 of 15 cases still pending |
| 4 | Thu 12 Nov | Missing sabungeros | PH | **RESEARCH** | Medium | By 6 Nov: Ang's status after Apr 2026; Manila RTC case; Patidongan statements (Mar 2026 reports of changed testimony unverified); DNA results; legal read |
| 5 | Mon 16 Nov | Jessica Wongso / Mirna | ID | **READY** | High (legal) / Medium (forensics) | Frame as "convicted; evidence disputed"; verify forensic claims against court record |
| 6 | Thu 19 Nov | Chiong sisters | PH | **RESEARCH** | Medium-Low | By 13 Nov: primary source on body identification; Larrañaga's current status |
| 7 | **Mon 23 Nov** | Maguindanao massacre (17th anniversary) | PH | **READY** | Medium-High | Do not claim pre-dug graves; verify Court of Appeals status on the day; confirm what the "58" count includes before stating body totals |
| 8 | Thu 26 Nov | Ferdy Sambo / Brigadir J | ID | **RESEARCH** | High (verdict) / Medium (timeline) | By 20 Nov: incident timeline from Indonesian court documents; Sept 2026 prison-conditions story |
| 9 | Sat 28 Nov | Ruby Rose Barrameda | PH | **RESEARCH** | Medium | By 20 Nov: status after Aug 2019 dismissals; **no one is convicted; use "dismissed"/"alleged"** |
| 10 | Mon 30 Nov | Catherine Camilon | PH | **RESEARCH (conditional)** | Low-Medium | By 20 Nov: bail status, trial status, 2026 developments. Demand is weak (77k 12-month views). **Swap rule:** if unresolved, replace with Percy Lapid or Sumanto |

### 5.1 Hooks and thumbnails (concepts only; no scripts)

Hooks use only facts verified above.

| Case | Proposed hook | Thumbnail concept |
|---|---|---|
| Vizconde | "In 2010 the Supreme Court acquitted the men convicted of killing a mother and her two daughters." | Split frame: 1991 Parañaque house exterior / red "ACQUITTED 2010" stamp. Text: "WHO DID IT?" |
| Mona Fandey | "Prosecutors said a shaman told a politician money would fall from the sky." | Axe silhouette over falling banknotes, desaturated archival look. No gore. |
| Am Cyanide | "Police say she poisoned friends she owed money to. Eight verdicts so far. Three death sentences." | Row of cup icons, counter "15 CASES / 3 DEATH SENTENCES". |
| Sabungeros | "A whistleblower alleged 100+ men were killed and dumped in Taal Lake. Prosecutors charged a businessman. He denies it, and as of April police could not find him." | Calm Taal Lake at dusk, rooster silhouette, "100+" tally. No faces of accused. |
| Wongso / Mirna | "She served 8½ years for a murder with no autopsy." | Iced coffee glass, cracked-ice question mark, "NO AUTOPSY". |
| Chiong | "Two sisters vanished outside a Cebu mall. A body was reported found in a ravine two days later. The other sister has never been found." | Two empty chairs / shoes on a Cebu street at dusk. |
| Maguindanao | "58 people. 32 journalists. One roadside in Maguindanao." | 58 candles, one lit red labelled "32 JOURNALISTS". |
| Sambo | "A police general's aide was shot dead. The Supreme Court cut the general's death sentence to life." | Police cap and a taped crime-scene line. No victim photo. |
| Ruby Rose | "She was found sealed in a drum off Navotas two years after she vanished. No one has been convicted." | Steel drum silhouette on dark water. |
| Camilon | "Police say blood and hair from an abandoned vehicle matched her parents' DNA. She has not been found." | Pageant sash on an empty gas-station forecourt. |

**Thumbnail rules:** no photos of minors or victims unless published by a reputable outlet and used non-sensationally; no faces of accused in ongoing cases; no gore; sexual-violence cases (Vizconde, Chiong) stay non-graphic.

### 5.2 Why these ten, and what fell out

- **Philippine mix (6):** Evidence supports five strong Philippine cases (Sabungeros, Maguindanao, Ruby Rose, Chiong, Vizconde) and one weak (Camilon). I kept six per your instruction, flagged Camilon as conditional, and named swaps.
- **Dropped on data:** Anson Que (8k 12-month views), Degamo (8k), Percy Lapid (475k, mostly political clickbait), Toa Payoh (259k, no English-language demand signal in 180 days), Koh Tao (disputed conviction plus sexual violence; kept in reserve).
- **Added on data:** Sambo (804k 180-day views, 39 videos, final verdict).
- **Strong demand but excluded:** **Pepsi Paloma** (1.07M 180-day views): allegations against living, named persons, sexual violence against a minor, and unreliable sourcing. `HOLD`. **Christine Dacera** (all-time 57M, 2026 modest): official finding is natural causes; high risk of victim-blaming framing. `RESERVE`. **Sumanto** (1.36M 180-day views) is the strongest reserve: well-sourced (five years for theft; released 2006) but corpse-eating rather than murder, and he is a living, rehabilitated person.

---

## 6. Case dossiers (slate)

Facts are labelled: **Proven** (court record or consistent major reporting), **Alleged**, **Disputed**, **Open**.

### 6.1 Vizconde massacre (PH) — READY · Confidence: High
- **Proven:** Night of 29–30 Jun 1991, 80 Vinzons St., BF Homes, Parañaque. Estrellita (49), Carmela (19) and Jennifer (7) were killed. Lauro Vizconde was in the US. Six burglars arrested Oct 1991 were acquitted Sept 1993. Witness Jessica Alfaro came forward 28 Apr 1995. RTC Judge Tolentino convicted Hubert Webb and five others on 6 Jan 2000; the Court of Appeals upheld in Dec 2005.
- **Proven:** The Supreme Court acquitted Webb and six others on 14 Dec 2010, 7–4 (4 not participating), finding Alfaro's testimony and the prosecution's case insufficient. The NBI could not produce the semen specimen for DNA testing. A motion to reverse was denied 18 Jan 2011.
- **Disputed:** Whether Webb was in the US; the Court called his alibi the strongest, while Justice Secretary de Lima said in 2011 that immigration records and new witnesses placed him in the Philippines. Double jeopardy bars retrial. Lobbying allegations were denied.
- **Open:** Nobody is currently convicted.
- **Sources:** [Wikipedia (cites SC decision, Inquirer, GMA)](https://en.wikipedia.org/wiki/Vizconde_murders), [GMA: Webb SC](https://www.gmanetwork.com/news/topstories/nation/204557/hubert-webb-asks-sc-for-acquittal-release-from-prison/story/), [GMA: Guingona](https://www.gmanews.tv/story/209999/ex-vp-guingona-to-sc-reverse-webbs-acquittal-to-give-justice-to-vizconde)
- **Gaps:** Wikipedia gives two SC docket numbers (G.R. 176389, 176864); confirm from the SC e-library.

### 6.2 Mona Fandey (MY) — READY · Confidence: Medium-High
- **Proven:** Pahang assemblyman Datuk Mazlan Idris was murdered in early July 1993. His body, in 18 parts, was found 22 Jul 1993. Mona Fandey (Nur Maznah Ismail), her husband Mohamad Nor Affandi and assistant Juraimi Hassan were charged 3 Aug 1993. A seven-person jury at Temerloh High Court heard 70 witnesses and returned a unanimous verdict in about 70 minutes. The Federal Court dismissed their appeals in 1999.
- **Alleged (by prosecution/testimony):** Mazlan was lured for a "cleansing" ritual; Juraimi's testimony described the dismemberment.
- **Disputed / conflicting sources:** Murder date (2 Jul to 18 Jul), money withdrawn (RM30,000 / RM315,000 / RM300,000), whether the body was "partially skinned".
- **Execution:** Reported as 2 Nov 2001 at Kajang. NST's own timeline is internally inconsistent on this date; verify before on-screen use.
- **Sources:** [NST175](https://www.nst.com.my/amp/news/nation/2020/07/610905/nst175-gruesome-tale-mona-fandey), [FMT](https://www.freemalaysiatoday.com/category/nation/2023/06/18/dukun-mona-fandey-and-a-politicians-gruesome-murder), [Wikipedia](https://en.wikipedia.org/wiki/Mona_Fandey)
- **Demand note:** Mona Fandey content is mostly Malay and Chinese-language; English-titled supply in 180 days is about 255k views vs 575k local. A Philippine audience may know her less, which is the point: unfamiliar to Americans and many Filipinos, well known across Malaysia.

### 6.3 "Am Cyanide" Sararat Rangsiwuthaporn (TH) — READY · Confidence: High
- **Proven (verdicts):** 8 of 15 cases decided: 3 death sentences (20 Nov 2024; 25 Aug 2026; 22 Sep 2026), 2 life sentences (reduced for useful testimony), 3 acquittals. All under appeal. Seven cases remain pending.
- **Case detail (25 Aug 2026 verdict):** Darinee "Fah" Thepwi died 13 Dec 2020 in Sam Phran, Nakhon Pathom; both women were in a rotating savings group and Sararat owed her 60,000 baht; a Siriraj forensic specialist found multi-organ failure after cyanide exposure.
- **Alleged:** Prosecutors say 14 poisonings between 2015 and 2023, motivated by debts and gambling. She denies the charges. Her ex-husband, a police lieutenant colonel, received 1y4m for evidence tampering (Khaosod, 2024).
- **Sources:** [Nation](https://www.nationthailand.com/news/general/40070234), [Khaosod Sep 2026](https://www.khaosodenglish.com/news/crimecourtscalamity/courts/2026/09/22/am-cyanide-sentenced-to-death-in-eighth-poisoning-case/), [The Star](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/09/22/thai-court-hands-am-cyanide-third-death-sentence-on-sept-22), [Khaosod Nov 2024](https://www.khaosodenglish.com/news/crimecourtscalamity/2024/11/20/thai-court-hands-down-death-sentence-in-high-profile-cyanide-murder-case/), [Thai PBS](https://www.thaipbsworld.com/crime/'am-cyanide'-cleared-of-2022-greengrocer-murder)
- **Ongoing:** More verdicts are expected; refresh the "as of" line on the publish date.

### 6.4 Missing sabungeros (PH) — RESEARCH · Confidence: Medium
- **Proven:** Men tied to online cockfighting (e-sabong) disappeared from 2021. About 887 bone fragments were retrieved from Taal Lake by Sept 2025, with no positive DNA identification then reported; the search was suspended in Oct 2025 (weather).
- **Proven (legal):** DOJ indicted Atong Ang and others 9 Dec 2025; cases filed 19 Dec 2025; warrants 14 Jan and 6 Feb 2026; reward P20M; Ang at large as of 10 Apr 2026. Whistleblower Julie "Dondon" Patidongan and his brother became state witnesses.
- **Alleged:** The prosecution's case relies heavily on whistleblower testimony; DOJ says its findings "have not been proven in court". Ang denies involvement. Barretto and Estomo were cleared at the prosecutor stage, without prejudice.
- **Open / unverified:** A 23 Mar 2026 report says Ang's lawyer asked the DOJ to drop him from the Manila case citing changes in Patidongan's statements; the search summary was garbled and I could not confirm details. Ang's status after Apr 2026 is unknown.
- **Sources:** [Philstar Dec 2025](https://www.philstar.com/headlines/2025/12/10/2493099/atong-ang-21-others-indicted-sabungero-case/amp/), [Rappler warrant](https://www.rappler.com/philippines/warrant-arrest-atong-ang-no-bail-missing-sabungeros-case/), [Philstar Apr 2026](https://www.philstar.com/nation/2026/04/10/2519860/atong-ang-eludes-arrest), [GMA: state witnesses](https://www.gmanetwork.com/news/topstories/nation/969090/missing-sabungeros-julie-patidongan-brother-state-witnesses-wpp/story/), [GMA: lawyer](https://www.gmanetwork.com/news/topstories/nation/981063/lawyer-doj-atong-ang-manila-case-sabungeros/story/), [Tribune: bones](https://tribune.net.ph/2025/09/09/doj-more-bones-retrieved-from-taal-lake)
- **Demand:** 5.0M 12-month views, 83 videos; GMA's Jan 2026 warrant video alone drew 641k. Mostly news channels, few storytellers.

### 6.5 Jessica Wongso / Mirna Salihin (ID) — READY · Confidence: High (legal), Medium (forensics)
- **Proven:** Jessica Wongso was convicted of murdering Wayan Mirna Salihin by cyanide in an iced coffee (Jakarta, Jan 2016) and sentenced to 20 years; the Supreme Court cassation on 21 Jun 2017 upheld it. First PK rejected Dec 2018; second filed 9 Oct 2024 and rejected 14 Aug 2025. Paroled 18 Aug 2024 after 8.5 years. She maintains innocence.
- **Disputed:** No autopsy was done (the family refused). A forensic doctor testified to about 0.2 mg of cyanide in the stomach sample; defence experts argued that was too small and could be post-mortem; prosecution experts said the lab figures showed a lethal dose was consumed.
- **Context:** Netflix's *Ice Cold* (28 Sep 2023) logged 3M viewing hours in four days.
- **Sources:** [JawaPos](https://www.jawapos.com/kasuistika/2508150340/pk-ditolak-ma-jessica-wongso-tetap-dinyatakan-sebagai-pembunuh-mirna-salihin-di-kasus-kopi-sianida), [Tempo: parole](https://en.tempo.co/amp/1905349/jessica-wongso-gets-5-years-remission-on-parole-today), [Jakarta Post: no autopsy](https://www.thejakartapost.com/news/2016/08/31/with-no-autopsy-can-we-be-sure-mirna-died-from-cyanide-jessicas-lawyer), [Tempo: expert](https://en.tempo.co/amp/802633/expert-witness-says-mirnas-death-not-caused-by-cyanide-poisoning), [Jakarta Post: experts](https://www.thejakartapost.com/news/2016/08/04/experts-confirm-mirna-was-poisoned-cyanide)
- **Gap:** Forensic numbers come from news reports of testimony; confirm against the verdict text before using any figure on screen.

### 6.6 Chiong sisters (PH) — RESEARCH · Confidence: Medium-Low
- **Proven:** Marijoy (19) and Jacqueline (21) Chiong were abducted outside Ayala Center Cebu on 16 Jul 1997. RTC Branch 7 convicted the accused on 15 May 1999; the Supreme Court ruled 3 Feb 2004 (death by lethal injection), later commuted to life after RA 9346 (2006). Larrañaga was transferred to Spain in Oct 2009. Jacqueline has never been found.
- **Disputed:** Whether the Carcar ravine body (found about two days after the abduction) was Marijoy. The family says yes; an advocacy source says it was never formally identified. Larrañaga's alibi (reported midterm exams in Manila, bar until about 3 a.m., no flight records) is widely discussed; he maintains innocence.
- **Proven:** In Sept 2019, four co-convicts were released under a good-conduct ruling and re-surrendered after outcry.
- **Sources:** [Wikipedia](https://en.wikipedia.org/wiki/Chiong_murder_case), [SunStar](https://www.sunstar.com.ph/cebu/local-news/film-hopes-to-quell-rumors-of-daughters-disappearance), [Sugbo.ph](https://sugbo.ph/2024/the-chiong-sisters/), [Inquirer](https://newsinfo.inquirer.net/1159452/present-men-jailed-for-chiong-sisters-slay-bucor-dared)
- **Gap:** Need the Supreme Court decision text and contemporaneous 1997 reporting on the body identification. Secondary sources only so far.

### 6.7 Maguindanao massacre (PH) — READY · Confidence: Medium-High
- **Proven:** 23 Nov 2009: a convoy of seven vehicles left Buluan for Shariff Aguak to file Esmael Mangudadatu's certificate of candidacy; armed men stopped it about 10:00 a.m. in Brgy. Masalay, Ampatuan. 58 people were killed, including 32 journalists (PCIJ). Three mass graves were found (35 bodies); a provincial backhoe was used.
- **Proven (legal):** The Quezon City court on 19 Dec 2019 convicted 28 as principals and 15 as accessories and acquitted 56 (partial decision). Appeals were pending at the Court of Appeals in the latest report I found (undated, about 2025). No 2026 ruling found.
- **Caveat:** An Aug 2026 UNTV segment covers Reynaldo Momay's recognition as the "58th victim". Confirm whether his remains were recovered before stating any body count.
- **Anniversary:** The 17th falls on Mon 23 Nov 2026, the slot chosen.
- **Sources:** [Inquirer timeline](https://www.inquirer.net/143183/maguindanao-massacre-how-it-happened/), [PCIJ](https://old.pcij.org/stories/maguindanao-massacre-one-year-after/), [Inquirer: Ampatuan Jr. appeal](https://newsinfo.inquirer.net/1208521/andal-ampatuan-jr-takes-maguindanao-massacre-convictions-to-court-of-appeals/amp), [GMA](https://gmanetwork.com/news/topstories/nation/720877/ampatuans-convicted-in-maguindanao-massacre-case-file-appeals/story), [Plaridel](https://www.tinigngplaridel.net/RjYdh)

### 6.8 Ferdy Sambo / Brigadir J (ID) — RESEARCH · Confidence: High (verdict), Medium (timeline)
- **Proven:** The Supreme Court on 8 Aug 2023 (3–2) reduced Sambo's death sentence to life for the premeditated murder of aide Nofriansyah Yosua Hutabarat ("Brigadir J"). Putri Candrawathi's sentence fell from 20 to 10 years; Ricky Rizal from 13 to 8; Kuat Ma'ruf from 15 to 10.
- **Open:** My sources here cover the sentencing only. Incident details and the "staged shooting" account still need Indonesian court-document sourcing. A Sept 2026 story (Ombudsman alleging a luxury cell) appears in Kompas/Viva videos but is unverified.
- **Sources:** [Jakarta Post](https://www.thejakartapost.com/paper/2023/08/10/death-sentence-reduced-to-life-for-ex-police-general-ferdy-sambo), [Tempo](https://en.tempo.co/read/1757608/supreme-court-discounts-ferdy-sambos-death-penalty-to-life-imprisonment-law-minister-responds), [Katadata](https://databoks.katadata.co.id/en/education/statistics/e711d46887909e9/ferdy-sambos-death-sentence-overturned-sentences-of-other-convicts-in-brigadier-j-murder-case-reduced)

### 6.9 Ruby Rose Barrameda (PH) — RESEARCH · Confidence: Medium
- **Proven:** Ruby Rose disappeared in Mar 2007 during a custody dispute. Her body was recovered in 2009, sealed in a drum, off Navotas. Witness Manuel Montero confessed, later recanted by letter (2013) and disappeared. The Malabon RTC dismissed the parricide case against estranged husband Manuel "Third" Jimenez III on 15 Aug 2019 (no probable cause) and the murder case against his father and two others; a later motion to reverse was denied.
- **Disputed:** Defence challenged whether the recovered body was Ruby Rose; the family disputes the dismissals.
- **Legal posture:** **No conviction exists.** Script must say "charges dismissed" and avoid implying guilt.
- **Sources:** [Inquirer: motion denied](https://newsinfo.inquirer.net/1205920/motion-to-reverse-ruling-on-2009-ruby-rose-murder-denied), [Inquirer: CA](https://newsinfo.inquirer.net/369053/rose-barrameda-kin-score-in-ca-ruling), [Philstar 2009](https://www.philstar.com/metro/2009/07/14/486204/doj-starts-probe-ruby-rose-case/amp/)
- **Gaps:** Appeal status after 2019; the exact date of the denial.

### 6.10 Catherine Camilon (PH) — RESEARCH (conditional) · Confidence: Low-Medium
- **Proven:** Miss Grand Philippines 2023 contestant last heard from 12 Oct 2023 in Bauan, Batangas. Blood and hair in an abandoned vehicle matched her parents' DNA (police). Former police major Allan de Castro and bodyguard Jeffrey Magpantay were arrested 14 Sep 2024 (Batangas RTC Br. 3, kidnapping and serious illegal detention).
- **Open / changed:** Earlier dismissal (May 2024) then refiling; defendants later released on bail; a friend-witness withdrew in Aug 2025 citing threats. No 2026 trial reporting found. A GMA Reporter's Notebook episode (14 Oct 2026) pairs her case with Geneva Lopez's.
- **Sources:** [Philstar Aug 2025](https://www.philstar.com/nation/2025/08/04/2462982/witness-withdraws-missing-beauty-queen-case), [Inquirer](https://newsinfo.inquirer.net/1984841/ex-policeman-driver-tagged-in-camilons-disappearance-nabbed-in-batangas/amp), [PNA](https://www.pna.gov.ph/articles/1213569), [Wikipedia](https://en.wikipedia.org/wiki/Disappearance_of_Catherine_Camilon)

---

## 7. The other 21 candidates (all now sourced)

Every candidate has at least one URL verified this session. "Conf." = research confidence.

| Case | Country | Verified status | Conf. | Slate? | Sources |
|---|---|---|---|---|---|
| Toa Payoh ritual murders | SG | Agnes Ng (9) and Ghazali Marzuki (10) killed Jan-Feb 1981; Adrian Lim, Tan Mui Choo and Hoe Kah Hong convicted 25 May 1983 after a 41-day trial; hanged 25 Nov 1988. Motive linked to a 1980 rape complaint (secondary sources); "ritual" label contested by defendants. Child victims. | High | RESERVE (READY) | [Wikipedia](https://en.wikipedia.org/wiki/Toa_Payoh_ritual_murders), [SAL](https://sal.org.sg/articles/the-toa-payoh-ritual-murders-a-case-of-insanity-or-was-it-just-a-wayang-part-1/) |
| Koh Tao murders | TH | Witheridge and Miller killed 2014; two Myanmar men sentenced to death, upheld by the Supreme Court Aug 2019; DNA handling and confessions disputed; pardon petition. | Medium | RESERVE | [Al Jazeera](https://www.aljazeera.com/amp/news/2019/8/29/death-sentences-stand-for-myanmar-men-in-britons-murders), [RFA](https://rfa.org/english/news/myanmar/myanmar-thailand-tourist-murder-appeal-08292019161737.html) |
| Sosilawati / Banting murders | MY | Aug 2010; three men's death sentences upheld by the Federal Court (2017), review denied Oct 2024; one acquitted. | High | RESERVE (READY) | [Malay Mail](https://www.malaymail.com/news/malaysia/2024/10/08/no-reprieve-federal-court-stands-firm-on-death-sentences-for-cosmetic-billionaire-sosilawatis-killers/152915), [Wikipedia](https://en.wikipedia.org/wiki/Banting_murders) |
| Sumanto (cannibal) | ID | Arrested 13 Jan 2003 for eating corpses; five years for theft (no cannibalism offence); released 2006 (or after three years, sources differ). Living person. | Medium-High | RESERVE (best swap) | [Wikipedia](https://en.wikipedia.org/wiki/Sumanto), [Hukumonline](https://www.hukumonline.com/berita/a/kasus-sumanto-ilhami-masuknya-pasal-314-ruu-kuhp-hol12559/) |
| Bình Phước massacre | VN | 7 Jul 2015 six family members killed; Nguyễn Hải Dương executed 17 Nov 2017; Vũ Văn Tiến 2018. Vietnamese sources needed. | Medium-High | RESERVE | [Wikipedia](https://en.wikipedia.org/wiki/2015_B%C3%ACnh_Ph%C6%B0%E1%BB%9Bc_massacre), [Nghệ An](https://baonghean.vn/en/da-thi-hanh-an-tu-tu-nguyen-hai-duong-10155332.html) |
| Vina Cirebon | ID | 27 Aug 2016 killings; suspect designation of Pegi Setiawan voided in a pretrial ruling 8 Jul 2024 (not a trial acquittal); eleven gang members were previously the accused. | Low | HOLD | [Kompas](https://www.kompas.com/tren/read/2024/07/08/163000765/perjalanan-kasus-pegi-setiawan-dari-dituduh-bunuh-vina-cirebon-sampai?page=all), [Bisnis](https://kabar24.bisnis.com/read/20240708/16/1780333/pegi-setiawan-batal-jadi-tersangka-kasus-vina-begini-kronologinya/1) |
| Degamo assassination | PH | 4 Mar 2023, ten killed; Teves in Manila RTC Br. 51, not-guilty plea entered, pre-trial 2025; acquitted of a separate 2019 case 5 Jan 2026; presumed innocent. | High | RESERVE | [Tribune](https://tribune.net.ph/2026/01/17/teves-not-off-the-hook-widow), [ABS-CBN](https://www.abs-cbn.com/news/nation/2025/6/10/court-enters-not-guilty-plea-for-teves-in-degamo-assassination-case-1737) |
| Percy Lapid / Bantag | PH | Murder charges vs Gerald Bantag; case archived pending his capture (Jul 2025); co-accused Zulueta's DNA ID stalled; Las Piñas RTC Br. 254 hearings Sept 2025. | Medium | SWAP | [Tribune](https://tribune.net.ph/2025/07/01/percy-lapid-case-hits-snag), [Malaya](https://malaya.com.ph/news/preliminary-hearing-held-today-on-percy-lapid-slay-case) |
| Anson Que | PH | Kidnapped 29 Mar 2025, found 9 Apr 2025 in Rodriguez, Rizal; DOJ ordered charges vs "Kelly" Gong Wen Li (Jun 2025) and cleared son Alvin; POGO link alleged by police only. | Medium | DROPPED (low demand) | [ABS-CBN](https://www.abs-cbn.com/news/nation/2025/6/18/doj-absolves-son-of-businessman-anson-que-in-kidnap-slay-case-2112), [Inquirer](https://globalnation.inquirer.net/281115/doj-files-charges-against-suspect-in-anson-que-kidnap-slay-case) |
| Dacer–Corbito | PH | Abducted Nov 2000; Lacson's charges dismissed; one officer convicted 2017 (Wikipedia). | Medium-Low | RESERVE | [GMA](https://www.gmanetwork.com/news/topstories/nation/181008/murder-case-filed-vs-lacson-for-dacer-corbito-killings/story/), [Inquirer](https://newsinfo.inquirer.net/?p=319917) |
| Jullebee Ranara | PH | Found burned in Kuwait 21 Jan 2023; employer's 17-year-old son got 15 years; appeal upheld. Minor perpetrator. | High | RESERVE | [ABS-CBN](https://news.abs-cbn.com/news/09/14/23/jullebee-ranaras-killer-sentenced-to-15-year-imprisonment), [GMA](https://gmanetwork.com/news/pinoyabroad/dispatch/898211/kuwaiti-appellate-court-affirms-guilty-verdict-in-jullebee-ranara-s-murder/story) |
| Christine Dacera | PH | Makati prosecutors dismissed rape-homicide complaints (Apr 2021); autopsy: ruptured aortic aneurysm; family disputes. | Medium | RESERVE | [Inquirer](https://newsinfo.inquirer.net/1551239/makati-prosecutor-dismisses-all-criminal-complaints-in-dacera-case-doj/amp), [BusinessWorld](https://www.bworldonline.com/?p=364303) |
| John Matthew Salilig hazing | PH | Adamson student died Feb 2023, "severe blunt force trauma"; DOJ complaint submitted for resolution; no verdict found. | Low | RESERVE | [Inquirer](https://newsinfo.inquirer.net/1737179/adamson-students-death-due-to-severe-blunt-force-trauma/amp), [GMA](https://gmanetwork.com/news/topstories/nation/863483/hazing-complaint-vs-suspects-in-salilig-s-death-submitted-for-resolution/story) |
| Pepsi Paloma | PH | 1982 allegations against named entertainers; complaint withdrawn; accused deny. | Low | HOLD | [ABS-CBN](https://news.abs-cbn.com/news/08/02/18/sotto-pepsi-paloma-rape-stories-are-fake-news), [Wikipedia](https://en.wikipedia.org/wiki/Pepsi_Paloma) |
| Korat shooting | TH | 8–9 Feb 2020; soldier Jakrapanth Thomma shot dead after 17+ hours; death toll 20–29 depending on source. | Medium | DROPPED | [Bangkok Post](https://www.bangkokpost.com/print/1853824/), [Wikipedia](https://en.wikipedia.org/wiki/Nakhon_Ratchasima_shootings) |
| Si Ouey | TH | Executed 1959; body displayed at Siriraj for decades, cremated Jul 2020; museum dropped "cannibal" label in 2019; modern research suggests he was framed. | Medium | RESERVE | [Khaosod](https://www.khaosodenglish.com/news/crimecourtscalamity/2019/05/31/justice-at-last-museum-amends-display-of-iconic-cannibal/amp/), [AP](https://spectrumlocalnews.com/nys/rochester/ap-online/2020/07/23/thai-serial-killer-cremated-after-decades-as-museum-display) |
| Red Bull heir hit-and-run | TH | 2012 crash killed a police officer; charges dropped 2020, reckless driving reinstated; heir's whereabouts reportedly unknown. | Medium | DROPPED | [NPR](https://www.npr.org/2020/07/24/894985857/thai-authorities-drop-charges-against-red-bull-billionaire-in-2012-hit-and-run-d), [Bangkok Post](https://www.bangkokpost.com/thailand/general/1084644/nacc-probes-red-bull-heir-case-delay) |
| Ryan "Jombang" | ID | Very Idham Henyansyah; 11 victims; death sentence 2009; Supreme Court rejected review 5 Jul 2012. | Medium | RESERVE | [Jakarta Post](https://www.thejakartapost.com/news/2009/04/07/court-sentences-ryan-death), [Republika](https://news.republika.co.id/berita/m6vmpg/ma-tolak-pk-ryan-jombang-tetap-divonis-mati) |
| Altantuya | MY | Azilah and Sirul convicted by the Federal Court Jan 2015; Azilah's sentence commuted to 40 years in 2023; civil suit hearing set 27 Oct 2026. | Medium | DROPPED (political) | [The Star](https://www.thestar.com.my/news/nation/2026/07/15/hearing-of-altatuya-family039s-leave-to-appeal-rescheduled-to-oct-27), [Malay Mail](https://www.malaymail.com/news/malaysia/2026/07/15/federal-court-postpones-altantuya-familys-bid-to-restore-rm5m-damages-award-to-oct-27/227717) |
| Teoh Beng Hock | MY | 2011 inquest open verdict; Court of Appeal 2014 found unlawful acts by unknown persons; probe reopened Aug 2024; a High Court mandamus required a complete investigation paper by May 2025. No outcome found. | Medium | DROPPED | [Malay Mail](https://www.malaymail.com/news/malaysia/2024/08/02/who-was-teoh-beng-hock-and-why-is-the-probe-into-his-death-being-reopened-15-years-later/145801), [The Sun](https://thesun.my/malaysia-news/police-to-recall-witnesses-in-teoh-beng-hock-case-for-renewed-investigation-JP13582920/) |
| Lê Văn Luyện | VN | 24 Aug 2011 gold-shop killings (Bắc Giang); 18 years at first instance (minor); no appellate result or release found. | Low | DROPPED | [Tiền Phong](https://tienphong.vn/Phap-Luat/564067/Toi-khong-the-tuyen-an-tu-hinh-Le-Van-Luyen-tpol.html), [Báo Pháp luật](https://baophapluat.vn/dieu-tra-mo-rong-vu-tham-an-tai-tiem-vang-o-bac-giang-post81856.html) |

---

## 8. Growth experiment: English narration vs Taglish text

**Principle:** subtitles alone are not assumed to cause better engagement. The test separates language, topic and audience.

**Arms (Philippine stories only, matched in pairs by 12-month demand and sensitivity):**
- **A — English narration, English captions** (control).
- **B — English narration, Taglish on-screen hook and captions.**
- **C (later, only if B wins) — Taglish narration.**

**Design**
1. Pair the six Philippine stories into three matched pairs (suggested: Vizconde/Chiong, Maguindanao/Ruby Rose, Sabungeros/Camilon). Randomise which of each pair gets arm B. Do not post the same story twice in two languages.
2. **Within-video check:** for every video, compare retention of Philippine viewers with non-Philippine viewers. That isolates the language effect from topic effects.
3. Keep length, posting time, thumbnail style and title structure identical within a pair.
4. Run the three non-Philippine `READY` stories (Mona Fandey, Am Cyanide, Wongso) as an English-only benchmark.

**Metrics (14 days per video; read at day 7 and day 14)**

| Metric | Definition | Source |
|---|---|---|
| Geography | % of views from PH, US, UK, CA, AU, MY, ID, other | YouTube Analytics > Audience > Geography |
| Retention | Viewed (not swiped away) %, average % viewed, 3-second and 10-second hold | Shorts analytics |
| Shares | Shares per 1,000 views | Analytics |
| Subscribers | Subscribers gained per 1,000 views | Analytics |
| Return | New vs returning viewer share | Audience tab |

**Decision rule:** `Scale arm B` only if, against matched A videos, median subs per 1,000 views is higher **and** Philippine-viewer average % viewed is not lower **and** Philippine share of views rises. Thresholds must be set from your own trailing-90-day medians; none exist in this report because no baseline was provided. With three pairs, results are directional, not statistically conclusive. Extend by two weeks if any video gets under 5,000 views.

**Benchmarks from the competitor data (context, not targets):** Filipino storyteller Shorts medians are low (Papa Dudut 5.5k), and English SEA Shorts range from 23k to 320k. Expect large variance.

### Baseline needed from you (nothing here is invented)

Export from YouTube Studio > Analytics > Advanced mode, last 90 days, by video: views, viewed-vs-swiped-away, average % viewed, shares, subscribers gained, top 10 countries, new vs returning viewers. Provide the equivalent TikTok, Facebook and Instagram exports. Confirm the exact channel handle. With that I can compute your medians and set the decision thresholds.

---

## 9. Credentials and secure setup

- **YouTube Data API key — not required**, but recommended. yt-dlp worked without credentials, then YouTube rate-limited it (HTTP 429), which cost about 830 video lookups. An official key avoids that.
- **How to add it securely:** create an API key in Google Cloud Console with only YouTube Data API v3 enabled and restrict the key to that API. In the cloud environment's settings (environment menu in the session title bar, then Edit), add it under Network secrets / API credentials if offered, otherwise as an environment variable named `YOUTUBE_API_KEY`. A new session picks it up. **Never paste keys into chat or commit them.**
- **Your own channel's analytics:** the public API cannot give subscribers gained or retention. Either send the CSV exports above through your private storage, or create a read-only OAuth credential with scope `https://www.googleapis.com/auth/yt-analytics.readonly` and store `YT_OAUTH_CLIENT_ID`, `YT_OAUTH_CLIENT_SECRET` and `YT_OAUTH_REFRESH_TOKEN` as environment secrets.
- This repository contains no credentials. The scripts under `scripts/` read none.

---

## 10. Appendix

### 10.1 Pronunciation guide (approximate; confirm with native speakers)

Vizconde (vis-KON-deh) · Chiong (CHONG) · Larrañaga (lah-rahn-YAH-gah) · Camilon (kah-mee-LON) · Sabungero (sah-boong-GEH-ro) · Maguindanao (mah-gin-DAH-now) · Ampatuan (am-pah-TWAN) · Barrameda (bah-rah-MEH-dah) · Rangsiwuthaporn (rahng-see-woo-tah-PORN) · Wongso (WONG-so) · Salihin (sah-LEE-hin) · Fandey (fan-DAY) · Mazlan Idris (MAZ-lahn ID-ris) · Hutabarat (hoo-tah-BAH-raht) · Toa Payoh (TWAH pay-OH).

### 10.2 Search terms by language (observed in video titles; popularity not measured)

- **Filipino/Tagalog:** "kaso", "nawawalang sabungero", "ang tunay na nangyari", "walang hustisya", "buong kwento", "totoong krimen", "pinatay", "sinapit".
- **Indonesian/Malay:** "kasus", "kronologi", "misteri", "terbongkar", "kes pembunuhan", "bomoh".
- **Thai:** "คดี", "แอม ไซยาไนด์", "ประหารชีวิต".
- **Taglish caption opportunities:** "hanggang ngayon, hindi pa rin nahuhuli" (still not caught to this day); "walang katawan, walang hustisya" (no body, no justice).

### 10.3 Reproducibility

- Raw and processed data are in `data/` (CSV/JSON). Scripts are in `scripts/` (Python, yt-dlp). They read no credentials.
- yt-dlp version 2026.08.19. Collection date 2026-10-16.
- Files: `data/youtube_case_videos.csv` (1,298 relevant videos), `data/case_metrics.json`, `data/ranking.json`, `data/competitor_channels.json`, `data/abs_cbn_series.csv`.
