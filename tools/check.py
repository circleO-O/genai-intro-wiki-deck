#!/usr/bin/env python3
"""簡報出處關卡(程式檢查)。用法: python3 -I tools/check.py [--wiki ../wiki]

關卡 A  每頁至少一個 wiki 頁面,且該頁面存在
關卡 B  每個主張都有出處(只有明確標記的「回顧/總結句」可以沒有)
關卡 C  引用的頁碼必須出現在 wiki 的 sources/concepts 中(不能憑空出現)
關卡 D  引用的頁碼必須在「已用圖片核對」白名單內(tools/verified.json)
關卡 E  頁數 8-15
輸出:每個失敗項目;全過則 exit 0。
"""
import json, re, sys, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
wiki = os.path.join(ROOT, "wiki")
if "--wiki" in sys.argv:
    wiki = os.path.abspath(sys.argv[sys.argv.index("--wiki") + 1])


def expand(spec):
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return out


def wiki_cites():
    found = set()
    for f in glob.glob(os.path.join(wiki, "*", "*.md")):
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\[S(\d\d)([^\]]*)\]", t):
            body = m.group(2).replace("–", "-")
            for a, b in re.findall(r"(\d+)\s*-\s*(\d+)", body):
                found |= {(m.group(1), p) for p in range(int(a), int(b) + 1)}
            for p in re.findall(r"\d+", re.sub(r"\d+\s*-\s*\d+", "", body)):
                found.add((m.group(1), int(p)))
    return found


def main():
    deck = json.load(open(os.path.join(HERE, "slides.json"), encoding="utf-8"))
    verified = {k: expand(v) for k, v in json.load(open(os.path.join(HERE, "verified.json"))).items() if not k.startswith("_")}
    inwiki = wiki_cites()
    slugs = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(wiki, "concepts", "*.md"))} | {"index"}
    errs = []
    slides = deck["slides"]
    if not 8 <= len(slides) <= 15:
        errs.append(f"E 頁數 {len(slides)} 不在 8-15")
    for s in slides:
        sid = s["id"]
        if not s.get("wiki"):
            errs.append(f"A 第{sid}頁 沒有對應的 wiki 頁面")
        for w in s.get("wiki", []):
            if w not in slugs:
                errs.append(f"A 第{sid}頁 wiki 頁面不存在: {w}")
        claims = [("takeaway", s["takeaway"])] + [(f"點{i+1}", p) for i, p in enumerate(s["points"])]
        for label, c in claims:
            if not c["c"] and not c.get("meta"):
                errs.append(f"B 第{sid}頁 {label} 沒有出處: {c['t'][:24]}…")
            for tag in c["c"]:
                m = re.fullmatch(r"S(\d\d) p\.(\d+)", tag)
                if not m:
                    errs.append(f"C 第{sid}頁 出處格式錯誤: {tag}")
                    continue
                n, p = m.group(1), int(m.group(2))
                if (n, p) not in inwiki:
                    errs.append(f"C 第{sid}頁 {label} {tag} 不在 wiki 中")
                if p not in verified.get(n, set()):
                    errs.append(f"D 第{sid}頁 {label} {tag} 未用圖片核對")
    for e in errs:
        print(e)
    n_claims = sum(1 + len(s["points"]) for s in slides)
    n_cites = sum(len(c["c"]) for s in slides for c in [s["takeaway"]] + s["points"])
    print(f"-- {len(slides)} 頁, {n_claims} 個主張, {n_cites} 個出處引用, {len(errs)} 個失敗")
    sys.exit(1 if errs else 0)


main()
