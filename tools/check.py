#!/usr/bin/env python3
"""闖關題庫的出處關卡(程式檢查)。用法: python3 -I tools/check.py

A  每關有存在的 wiki 頁面、剛好 5 題
B  每題 4 個不重複選項、答案索引合法、有解析與出處
C  引用的頁碼必須出現在 wiki 的 sources/concepts 中(不能憑空)
D  引用的頁碼必須在「已用圖片核對」白名單(tools/verified.json)
E  共 10 關
另外印出答案位置分布與「正確選項最長」的比例(警告,不擋關)。
"""
import json, re, sys, glob, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
wiki = os.path.join(ROOT, "wiki")


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
    quiz = json.load(open(os.path.join(HERE, "quiz.json"), encoding="utf-8"))
    verified = {k: expand(v) for k, v in json.load(open(os.path.join(HERE, "verified.json"))).items() if not k.startswith("_")}
    inwiki = wiki_cites()
    slugs = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(wiki, "concepts", "*.md"))}
    errs, pos, longest, total = [], collections.Counter(), 0, 0
    if len(quiz["levels"]) != 10:
        errs.append(f"E 關卡數 {len(quiz['levels'])} 不是 10")
    for L in quiz["levels"]:
        lid = L["id"]
        if len(L["questions"]) != 5:
            errs.append(f"A 第{lid}關 題數 {len(L['questions'])} 不是 5")
        for w in L.get("wiki", []):
            if w not in slugs:
                errs.append(f"A 第{lid}關 wiki 頁面不存在: {w}")
        if not L.get("wiki"):
            errs.append(f"A 第{lid}關 沒有對應的 wiki 頁面")
        for i, q in enumerate(L["questions"], 1):
            tag = f"第{lid}關 Q{i}"
            total += 1
            o = q["o"]
            if len(o) != 4 or len(set(o)) != 4:
                errs.append(f"B {tag} 選項不是 4 個不重複")
            if q["a"] not in range(len(o)):
                errs.append(f"B {tag} 答案索引不合法")
                continue
            if not q.get("e") or not q.get("c"):
                errs.append(f"B {tag} 缺解析或出處")
            pos[q["a"]] += 1
            if len(o[q["a"]]) == max(len(x) for x in o):
                longest += 1
            for t in q.get("c", []):
                m = re.fullmatch(r"S(\d\d) p\.(\d+)", t)
                if not m:
                    errs.append(f"C {tag} 出處格式錯誤: {t}")
                    continue
                n, p = m.group(1), int(m.group(2))
                if (n, p) not in inwiki:
                    errs.append(f"C {tag} {t} 不在 wiki 中")
                if p not in verified.get(n, set()):
                    errs.append(f"D {tag} {t} 未用圖片核對")
    for e in errs:
        print(e)
    print(f"-- {len(quiz['levels'])} 關, {total} 題, 答案位置 {dict(sorted(pos.items()))}, 正確選項最長 {longest}/{total}, {len(errs)} 個失敗")
    sys.exit(1 if errs else 0)


main()
