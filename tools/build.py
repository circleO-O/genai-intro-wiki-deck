#!/usr/bin/env python3
"""把通過 check.py 的 slides.json 渲染成 index.html,並把 wiki/*.md 轉成可瀏覽的 HTML。
渲染階段只排版,不改任何一個字(S10 p.44 的設計)。用法: python3 -I tools/build.py
"""
import json, os, re, glob, html, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

if subprocess.call([sys.executable, "-I", os.path.join(HERE, "check.py")], stdout=subprocess.DEVNULL) != 0:
    sys.exit("check.py 未通過,拒絕渲染。先修內容,不要在渲染階段改字。")

deck = json.load(open(os.path.join(HERE, "slides.json"), encoding="utf-8"))
e = html.escape


# ---------- wiki md -> html ----------
def inline(s):
    s = e(s)
    s = re.sub(r"\[\[([a-z0-9\-]+)\]\]", lambda m: f'<a href="{m.group(1)}.html">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(S\d\d p\.[^\]]+)\]", r'<span class="cite">\1</span>', s)
    return s


def md_to_html(md):
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    out, in_ul, in_tbl = [], False, False
    for line in md.split("\n"):
        if in_ul and not re.match(r"\s*- ", line) and line.strip():
            out.append("</ul>"); in_ul = False
        if in_tbl and not line.startswith("|"):
            out.append("</table>"); in_tbl = False
        m = re.match(r"(#{1,3}) (.*)", line)
        if m:
            out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>")
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            if not in_tbl:
                out.append("<table>"); in_tbl = True
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
        elif re.match(r"\s*- ", line):
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(re.sub(r'^\s*- ', '', line))}</li>")
        elif re.match(r"\d+\. ", line):
            out.append(f"<p>{inline(line)}</p>")
        elif line.strip():
            out.append(f"<p>{inline(line)}</p>")
    if in_ul: out.append("</ul>")
    if in_tbl: out.append("</table>")
    return "\n".join(out)


WIKI_CSS = """
:root{--bg:#fbfaf7;--fg:#1f2430;--mut:#6b7280;--acc:#2f6fe4;--card:#fff;--line:#e5e2da}
@media (prefers-color-scheme:dark){:root{--bg:#14161b;--fg:#e8e9ee;--mut:#9aa0ad;--acc:#7aa7ff;--card:#1c1f26;--line:#2c303a}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 system-ui,"Noto Sans TC","PingFang TC",sans-serif}
main{max-width:820px;margin:0 auto;padding:24px 16px 80px}
a{color:var(--acc)}h1{font-size:1.7rem}h2{margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}
.cite{font:12px ui-monospace,monospace;color:var(--mut);background:var(--card);border:1px solid var(--line);border-radius:4px;padding:0 4px;white-space:nowrap}
code{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:0 4px}
table{border-collapse:collapse;width:100%}td{border:1px solid var(--line);padding:6px 8px;vertical-align:top}
nav{font-size:14px;color:var(--mut);margin-bottom:12px}
"""


def wiki_page(title, body, up):
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>
<style>{WIKI_CSS}</style></head><body><main>
<nav><a href="{up}index.html">← wiki 首頁</a> · <a href="../index.html">← 簡報</a></nav>
{body}</main></body></html>"""


os.makedirs(os.path.join(ROOT, "wiki-site"), exist_ok=True)
pages = {}
for f in sorted(glob.glob(os.path.join(ROOT, "wiki", "concepts", "*.md")) + glob.glob(os.path.join(ROOT, "wiki", "sources", "*.md")) + [os.path.join(ROOT, "wiki", "index.md"), os.path.join(ROOT, "wiki", "log.md")]):
    md = open(f, encoding="utf-8").read()
    slug = os.path.basename(f)[:-3]
    pages[slug] = (f, md)

# index.md links use relative md paths; rewrite to html
for slug, (f, md) in pages.items():
    body = md_to_html(md)
    body = re.sub(r'href="(?:concepts/|sources/)?([\w\-]+)\.html"', r'href="\1.html"', body)
    t = re.search(r"^# (.*)", md, re.M)
    open(os.path.join(ROOT, "wiki-site", slug + ".html"), "w", encoding="utf-8").write(wiki_page(t.group(1) if t else slug, body, ""))
# index.md uses markdown links [text](path.md): convert
ip = os.path.join(ROOT, "wiki-site", "index.html")
t = open(ip, encoding="utf-8").read()
t = re.sub(r"\[([^\]]+)\]\((?:concepts/|sources/)?([\w\-]+)\.md\)", r'<a href="\2.html">\1</a>', e(open(os.path.join(ROOT, "wiki", "index.md"), encoding="utf-8").read()))
body = md_to_html(open(os.path.join(ROOT, "wiki", "index.md"), encoding="utf-8").read())
body = re.sub(r"\[([^\]]+)\]\((?:concepts/|sources/)?([\w\-]+)\.md\)", r'<a href="\2.html">\1</a>', body)
open(ip, "w", encoding="utf-8").write(wiki_page("LLM Wiki 首頁", body, ""))


# ---------- deck ----------
def cite_html(tags):
    return "".join(f'<span class="cite">{e(t)}</span>' for t in tags)


slides_html = []
n = len(deck["slides"])
for s in deck["slides"]:
    pts = "".join(f'<li><span class="t">{e(p["t"])}</span> {cite_html(p["c"])}</li>' for p in s["points"])
    basis = " ".join(
        f'<a href="wiki-site/{e(w)}.html" target="_blank" rel="noopener">{e(w)}</a>' for w in s["wiki"]
    )
    cover = " cover" if s["id"] == 1 else ""
    slides_html.append(f"""
<section class="slide{cover}" id="s{s['id']}" data-title="{e(s['title'])}">
  <div class="inner">
    <div class="kicker">{e(s['section'])}</div>
    <h2>{e(s['title'])}</h2>
    <div class="take"><b>一句話:</b>{e(s['takeaway']['t'])} {cite_html(s['takeaway']['c'])}</div>
    <ul class="pts">{pts}</ul>
  </div>
  <footer><span>依據 wiki:{basis}</span></footer>
</section>""")

page = f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>生成式 AI 入門教學簡報</title>
<meta name="description" content="用 LLM Wiki 製作的生成式 AI 入門教學簡報:從神經網路、LLM 到 Agent 與工作流程。">
<style>
:root{{--bg:#fbfaf7;--fg:#1f2430;--mut:#6b7280;--acc:#2f6fe4;--card:#fff;--line:#e5e2da;--hl:#eef3ff}}
@media (prefers-color-scheme:dark){{:root{{--bg:#14161b;--fg:#e8e9ee;--mut:#9aa0ad;--acc:#7aa7ff;--card:#1c1f26;--line:#2c303a;--hl:#1b2540}}}}
*{{box-sizing:border-box}}
html,body{{margin:0;height:100%}}
body{{background:var(--bg);color:var(--fg);font:clamp(15px,1.42vw,19px)/1.62 system-ui,"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;overflow:hidden}}
.slide{{position:absolute;inset:0;display:none;flex-direction:column;padding:0 16px}}
.slide.on{{display:flex}}
.inner{{flex:1;overflow:auto;width:100%;max-width:1040px;margin:0 auto;padding:3vh 0 1.5vh}}
.kicker{{color:var(--acc);font-weight:600;letter-spacing:.08em;font-size:.8em}}
h2{{font-size:clamp(22px,3.2vw,40px);line-height:1.25;margin:.2em 0 .6em}}
.take{{background:var(--hl);border-left:4px solid var(--acc);padding:.7em 1em;border-radius:6px;margin-bottom:1em}}
.pts{{padding-left:1.1em;margin:0}}
.pts li{{margin:.38em 0}}
.cite{{display:inline-block;font:11px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut);background:var(--card);border:1px solid var(--line);border-radius:4px;padding:0 5px;margin-left:3px;white-space:nowrap;vertical-align:1px}}
footer{{width:100%;max-width:1040px;margin:0 auto;display:flex;align-items:center;color:var(--mut);font-size:13px;height:60px;padding:0 440px 0 0;border-top:1px solid var(--line)}}
footer a{{color:var(--acc);margin-right:6px}}
.cover h2{{font-size:clamp(28px,5vw,60px)}}
.nav{{position:fixed;right:16px;bottom:8px;display:flex;gap:8px;z-index:5}}
.nav button{{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;width:44px;height:44px;font-size:18px;cursor:pointer}}
.nav button:hover{{border-color:var(--acc)}}
#bar{{position:fixed;left:0;top:0;height:3px;background:var(--acc);width:0;z-index:6;transition:width .2s}}
#toc{{position:fixed;right:120px;bottom:8px;z-index:5}}
#toc select{{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;height:44px;padding:0 8px;width:min(320px,calc(100vw - 150px))}}
@media (max-width:760px){{footer{{height:112px;align-items:flex-start;padding:10px 0 0}}#toc{{left:16px;right:auto}}#toc select{{width:calc(100vw - 150px)}}}}
@media print{{body{{overflow:visible;height:auto}}.slide{{position:static;display:flex;page-break-after:always;min-height:100vh}}.nav,#toc,#bar{{display:none}}}}
</style></head><body>
<div id="bar"></div>
{''.join(slides_html)}
<div id="toc"><select id="sel" aria-label="跳到某一頁"></select></div>
<div class="nav"><button id="prev" aria-label="上一頁">←</button><button id="next" aria-label="下一頁">→</button></div>
<script>
(function(){{
  var slides=[].slice.call(document.querySelectorAll('.slide')),i=0,sel=document.getElementById('sel');
  slides.forEach(function(s,k){{var o=document.createElement('option');o.value=k;o.textContent=(k+1)+'. '+s.dataset.title;sel.appendChild(o)}});
  function go(k){{i=Math.max(0,Math.min(slides.length-1,k));slides.forEach(function(s,j){{s.classList.toggle('on',j===i)}});
    sel.value=i;document.getElementById('bar').style.width=((i+1)/slides.length*100)+'%';
    slides[i].querySelector('.inner').scrollTop=0;try{{history.replaceState(null,'','#'+(i+1))}}catch(e){{}}}}
  document.getElementById('prev').onclick=function(){{go(i-1)}};
  document.getElementById('next').onclick=function(){{go(i+1)}};
  sel.onchange=function(){{go(+sel.value)}};
  document.addEventListener('keydown',function(ev){{
    if(ev.target===sel)return;
    if(['ArrowRight','PageDown',' '].indexOf(ev.key)>-1){{ev.preventDefault();go(i+1)}}
    if(['ArrowLeft','PageUp'].indexOf(ev.key)>-1){{ev.preventDefault();go(i-1)}}
    if(ev.key==='Home')go(0);if(ev.key==='End')go(slides.length-1)}});
  var tx=0;document.addEventListener('touchstart',function(ev){{tx=ev.touches[0].clientX}});
  document.addEventListener('touchend',function(ev){{var d=ev.changedTouches[0].clientX-tx;if(Math.abs(d)>60)go(i+(d<0?1:-1))}});
  var h=parseInt(location.hash.slice(1),10);go(h>0?h-1:0);
}})();
</script></body></html>"""
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)
print("built index.html +", len(pages), "wiki pages")
