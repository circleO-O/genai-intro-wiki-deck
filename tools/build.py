#!/usr/bin/env python3
"""把通過 check.py 的 quiz.json 渲染成 index.html(闖關問答),並把 wiki/*.md 轉成可瀏覽的 HTML。
渲染階段只排版,不改任何一個字。check.py 未通過就拒絕渲染。用法: python3 -I tools/build.py
"""
import json, os, re, glob, html, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

if subprocess.call([sys.executable, "-I", os.path.join(HERE, "check.py")], stdout=subprocess.DEVNULL) != 0:
    sys.exit("check.py 未通過,拒絕渲染。先修題庫內容,不要在渲染階段改字。")

quiz = json.load(open(os.path.join(HERE, "quiz.json"), encoding="utf-8"))
e = html.escape

THEME = """
:root{--bg:#070b14;--bg2:#0d1424;--panel:#111a2e;--panel2:#16213a;--line:#233152;--fg:#e6edf7;--mut:#8a98b5;
--cy:#22d3ee;--vi:#a78bfa;--ok:#34d399;--bad:#fb7185;--glow:0 0 0 1px rgba(34,211,238,.35),0 0 24px rgba(34,211,238,.12)}
*{box-sizing:border-box}
html,body{margin:0}
body{background:radial-gradient(1200px 600px at 80% -10%,rgba(167,139,250,.14),transparent 60%),radial-gradient(900px 500px at -10% 10%,rgba(34,211,238,.10),transparent 55%),var(--bg);
color:var(--fg);font:16px/1.75 system-ui,"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;min-height:100vh}
a{color:var(--cy)}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
"""

# ---------- wiki md -> html ----------
def inline(s):
    s = e(s)
    s = re.sub(r"\[\[([a-z0-9\-]+)\]\]", lambda m: f'<a href="{m.group(1)}.html">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(S\d\d p\.[^\]]+)\]", r'<span class="cite">\1</span>', s)
    s = re.sub(r"\[([^\]]+)\]\((?:concepts/|sources/)?([\w\-]+)\.md\)", r'<a href="\2.html">\1</a>', s)
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
        elif line.strip():
            out.append(f"<p>{inline(line)}</p>")
    if in_ul: out.append("</ul>")
    if in_tbl: out.append("</table>")
    return "\n".join(out)


WIKI_CSS = THEME + """
main{max-width:820px;margin:0 auto;padding:24px 16px 80px}
h1{font-size:1.7rem}h2{margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}
.cite{font:12px ui-monospace,monospace;color:var(--cy);background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:0 4px;white-space:nowrap}
code{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:0 4px}
table{border-collapse:collapse;width:100%}td{border:1px solid var(--line);padding:6px 8px;vertical-align:top}
nav{font-size:14px;color:var(--mut);margin-bottom:12px}
"""


def wiki_page(title, body):
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>
<style>{WIKI_CSS}</style></head><body><main>
<nav><a href="index.html">← wiki 首頁</a> · <a href="../index.html">← 闖關首頁</a></nav>
{body}</main></body></html>"""


os.makedirs(os.path.join(ROOT, "wiki-site"), exist_ok=True)
files = sorted(glob.glob(os.path.join(ROOT, "wiki", "concepts", "*.md")) + glob.glob(os.path.join(ROOT, "wiki", "sources", "*.md")) + [os.path.join(ROOT, "wiki", "index.md"), os.path.join(ROOT, "wiki", "log.md")])
for f in files:
    md = open(f, encoding="utf-8").read()
    slug = os.path.basename(f)[:-3]
    t = re.search(r"^# (.*)", md, re.M)
    open(os.path.join(ROOT, "wiki-site", slug + ".html"), "w", encoding="utf-8").write(wiki_page(t.group(1) if t else slug, md_to_html(md)))

# ---------- quiz page ----------
data = json.dumps(quiz["levels"], ensure_ascii=False).replace("</", "<\\/")
page = f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>生成式 AI 闖關問答</title>
<meta name="description" content="10 個關卡、50 題,用 LLM Wiki 整理的課程內容闖關;每題答完都有解析與出處。">
<style>
{THEME}
.wrap{{max-width:980px;margin:0 auto;padding:28px 16px 64px}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:6px}}
.tag{{color:var(--cy);font-size:12px;letter-spacing:.18em}}
h1{{font-size:clamp(26px,4.4vw,44px);line-height:1.2;margin:.15em 0 .25em;background:linear-gradient(90deg,var(--cy),var(--vi));-webkit-background-clip:text;background-clip:text;color:transparent}}
.sub{{color:var(--mut);margin:0 0 20px}}
.stat{{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 22px}}
.chip{{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:14px;color:var(--mut)}}
.chip b{{color:var(--fg)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}}
.card{{display:flex;flex-direction:column;justify-content:flex-start;text-align:left;background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:14px;padding:16px;color:var(--fg);cursor:pointer;font:inherit;transition:transform .15s,border-color .15s,box-shadow .15s}}
.card:hover,.card:focus-visible{{transform:translateY(-2px);border-color:var(--cy);box-shadow:var(--glow);outline:none}}
.card .lv{{font-size:12px;color:var(--cy);letter-spacing:.14em}}
.card h3{{margin:.2em 0 .3em;font-size:18px;line-height:1.35}}
.card p{{margin:0 0 14px;color:var(--mut);font-size:14px;line-height:1.6;flex:1}}
.bar{{height:6px;background:var(--bg2);border-radius:99px;overflow:hidden}}
.bar i{{display:block;height:100%;background:linear-gradient(90deg,var(--cy),var(--vi));width:0}}
.st{{display:flex;justify-content:space-between;font-size:13px;color:var(--mut);margin-top:8px}}
.st .done{{color:var(--ok)}}
.panel{{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:16px;padding:clamp(16px,3vw,28px)}}
.head{{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}}
.btn{{background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:10px;padding:8px 16px;font:inherit;cursor:pointer}}
.btn:hover,.btn:focus-visible{{border-color:var(--cy);outline:none}}
.btn.pri{{background:linear-gradient(90deg,#0891b2,#7c3aed);border-color:transparent;color:#fff}}
.segs{{display:flex;gap:6px;margin:6px 0 18px}}
.segs i{{flex:1;height:6px;border-radius:99px;background:var(--bg2)}}
.segs i.cur{{background:var(--cy)}}.segs i.ok{{background:var(--ok)}}.segs i.bad{{background:var(--bad)}}
.q{{font-size:clamp(18px,2.6vw,24px);line-height:1.5;margin:0 0 16px;font-weight:600}}
.opts{{display:grid;gap:10px}}
.opt{{display:flex;gap:12px;align-items:flex-start;text-align:left;width:100%;background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:12px 14px;color:var(--fg);font:inherit;cursor:pointer}}
.opt:hover:not(:disabled),.opt:focus-visible{{border-color:var(--cy);outline:none}}
.opt .k{{flex:none;width:28px;height:28px;border-radius:8px;border:1px solid var(--line);display:grid;place-items:center;font-size:13px;color:var(--mut)}}
.opt:disabled{{cursor:default}}
.opt.right{{border-color:var(--ok);background:rgba(52,211,153,.10)}}.opt.right .k{{background:var(--ok);color:#04130d;border-color:var(--ok)}}
.opt.wrong{{border-color:var(--bad);background:rgba(251,113,133,.10)}}.opt.wrong .k{{background:var(--bad);color:#1b0509;border-color:var(--bad)}}
.opt.dim{{opacity:.55}}
.exp{{margin-top:16px;border-left:4px solid var(--vi);background:rgba(167,139,250,.08);border-radius:0 12px 12px 0;padding:14px 16px}}
.exp .v{{font-weight:700;margin-bottom:4px}}.exp .v.ok{{color:var(--ok)}}.exp .v.bad{{color:var(--bad)}}
.exp p{{margin:.3em 0}}
.cite{{display:inline-block;font:12px/1.6 ui-monospace,Menlo,monospace;color:var(--cy);background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:0 6px;margin:2px 4px 2px 0}}
.note{{color:var(--mut);font-size:13px;margin-top:8px}}
.actions{{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}}
.big{{font-size:clamp(40px,8vw,72px);font-weight:800;line-height:1;background:linear-gradient(90deg,var(--cy),var(--vi));-webkit-background-clip:text;background-clip:text;color:transparent}}
.rv{{margin:12px 0 0;padding:12px 14px;background:var(--bg2);border:1px solid var(--line);border-radius:12px}}
.rv b{{color:var(--bad)}}.rv span.a{{color:var(--ok)}}
.foot{{margin-top:28px;color:var(--mut);font-size:13px}}
.hide{{display:none!important}}
</style></head><body>
<div class="wrap">
 <section id="home">
  <div class="top"><span class="tag mono">GENERATIVE AI · QUEST</span><span class="chip mono" id="total"></span></div>
  <h1>生成式 AI 闖關問答</h1>
  <p class="sub">10 個關卡對應課程 10 個單元,每關 5 題。自己選關卡,答完每題都有解析與出處。</p>
  <div class="stat" id="stat"></div>
  <div class="grid" id="grid"></div>
  <p class="foot">題目與解析整理自 <a href="wiki-site/index.html">LLM Wiki</a>(每個答案都標出處,例如 <span class="cite">S06 p.16</span> = 第 06 份投影片第 16 頁);錯誤選項是出題時編寫的常見誤解,不出自 wiki。
  · <a href="https://github.com/circleO-O/genai-intro-wiki-deck">GitHub</a></p>
 </section>
 <section id="play" class="hide"></section>
</div>
<script>
(function(){{
var LEVELS={data};
var $=function(s){{return document.querySelector(s)}};
var store={{}};
try{{store=JSON.parse(localStorage.getItem('genai-quest')||'{{}}')}}catch(e){{store={{}}}}
function save(){{try{{localStorage.setItem('genai-quest',JSON.stringify(store))}}catch(e){{}}}}
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function shuffle(a){{a=a.slice();for(var i=a.length-1;i>0;i--){{var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}}return a}}
var LET=['A','B','C','D'];
function home(){{
  $('#play').classList.add('hide');$('#home').classList.remove('hide');
  var done=0,pts=0;
  var g=$('#grid');g.innerHTML='';
  LEVELS.forEach(function(L){{
    var b=store[L.id];if(b!=null){{done++;pts+=b}}
    var c=document.createElement('button');c.className='card';
    c.innerHTML='<div class="lv mono">LEVEL '+L.unit+'</div><h3>'+esc(L.title)+'</h3><p>'+esc(L.blurb)+'</p>'+
      '<div class="bar"><i style="width:'+(b==null?0:b/5*100)+'%"></i></div>'+
      '<div class="st"><span>'+(b==null?'尚未挑戰':'最佳 '+b+' / 5')+'</span><span class="'+(b===5?'done':'')+'">'+(b===5?'全對 ✓':'5 題')+'</span></div>';
    c.onclick=function(){{start(L.id)}};g.appendChild(c);
  }});
  $('#stat').innerHTML='<span class="chip">已挑戰 <b>'+done+'</b> / '+LEVELS.length+' 關</span><span class="chip">累計最佳 <b>'+pts+'</b> / '+LEVELS.length*5+' 分</span>';
  $('#total').textContent=LEVELS.length+' LEVELS · '+LEVELS.length*5+' QUESTIONS';
  try{{history.replaceState(null,'',location.pathname)}}catch(e){{}}
  window.scrollTo(0,0);
}}
var S=null;
function start(id){{
  var L=LEVELS.filter(function(x){{return x.id===id}})[0];
  S={{L:L,i:0,score:0,res:[],qs:L.questions.map(function(q){{
    var idx=shuffle([0,1,2,3]);
    return {{q:q,opts:idx.map(function(k){{return q.o[k]}}),ans:idx.indexOf(q.a)}};
  }}),locked:false}};
  try{{history.replaceState(null,'','#L'+id)}}catch(e){{}}
  $('#home').classList.add('hide');$('#play').classList.remove('hide');
  render();window.scrollTo(0,0);
}}
function segs(){{
  return '<div class="segs">'+S.qs.map(function(_,k){{
    var c=k<S.res.length?(S.res[k]?'ok':'bad'):(k===S.i?'cur':'');return '<i class="'+c+'"></i>'}}).join('')+'</div>';
}}
function render(){{
  var Q=S.qs[S.i],L=S.L;
  var h='<div class="panel"><div class="head"><span class="tag mono">LEVEL '+L.unit+' · '+esc(L.title)+' · Q'+(S.i+1)+' / 5</span>'+
    '<button class="btn" id="back">← 回關卡選單</button></div>'+segs()+
    '<p class="q">'+esc(Q.q.q)+'</p><div class="opts" role="group" aria-label="選項">'+
    Q.opts.map(function(o,k){{return '<button class="opt" data-k="'+k+'"><span class="k mono">'+LET[k]+'</span><span>'+esc(o)+'</span></button>'}}).join('')+
    '</div><div id="exp" aria-live="polite"></div></div>';
  $('#play').innerHTML=h;S.locked=false;
  $('#back').onclick=home;
  [].forEach.call(document.querySelectorAll('.opt'),function(b){{b.onclick=function(){{pick(+b.dataset.k)}}}});
}}
function pick(k){{
  if(S.locked)return;S.locked=true;
  var Q=S.qs[S.i],ok=k===Q.ans;S.res.push(ok);if(ok)S.score++;
  S.qs[S.i].picked=k;
  [].forEach.call(document.querySelectorAll('.opt'),function(b,j){{
    b.disabled=true;
    if(j===Q.ans)b.classList.add('right');else if(j===k)b.classList.add('wrong');else b.classList.add('dim');
  }});
  var last=S.i===S.qs.length-1;
  var cites=Q.q.c.map(function(c){{return '<span class="cite">'+esc(c)+'</span>'}}).join('');
  var wk=S.L.wiki.map(function(w){{return '<a href="wiki-site/'+w+'.html" target="_blank" rel="noopener">'+w+'</a>'}}).join('、');
  $('#exp').innerHTML='<div class="exp"><div class="v '+(ok?'ok':'bad')+'">'+(ok?'答對了':'答錯了,正確答案是 '+LET[Q.ans])+'</div>'+
    '<p>'+esc(Q.q.e)+'</p><p>'+cites+'</p><p class="note">延伸閱讀(wiki):'+wk+'</p></div>'+
    '<div class="actions"><button class="btn pri" id="next">'+(last?'看結果 →':'下一題 →')+'</button></div>';
  $('#next').onclick=next;$('#next').focus({{preventScroll:true}});
  $('#exp').scrollIntoView({{behavior:'smooth',block:'nearest'}});
  document.querySelector('.segs').outerHTML=segs();
}}
function next(){{
  if(S.i<S.qs.length-1){{S.i++;render();window.scrollTo(0,0)}}else result();
}}
function result(){{
  var L=S.L,s=S.score;
  if(store[L.id]==null||s>store[L.id]){{store[L.id]=s;save()}}
  var msg=s===5?'全對!這一關你已經掌握了。':s>=3?'不錯!看看下面答錯的題目,再挑戰一次吧。':'先看解析再重來,第二次一定更好。';
  var wrong=S.qs.map(function(Q,k){{return S.res[k]?'':
    '<div class="rv"><b>Q'+(k+1)+'</b> '+esc(Q.q.q)+'<br><span class="a">正確:'+esc(Q.opts[Q.ans])+'</span><br>'+esc(Q.q.e)+
    '<br>'+Q.q.c.map(function(c){{return '<span class="cite">'+esc(c)+'</span>'}}).join('')+'</div>'}}).join('');
  var nxt=LEVELS.filter(function(x){{return x.id===L.id+1}})[0];
  $('#play').innerHTML='<div class="panel"><div class="head"><span class="tag mono">LEVEL '+L.unit+' · 結算</span></div>'+
    '<div class="big mono">'+s+' / 5</div><p>'+msg+'</p>'+segs()+
    (wrong?'<h3>答錯的題目</h3>'+wrong:'')+
    '<div class="actions"><button class="btn pri" id="again">重玩這一關</button>'+
    (nxt?'<button class="btn" id="nx">下一關:'+esc(nxt.title)+'</button>':'')+
    '<button class="btn" id="menu">回關卡選單</button></div></div>';
  $('#again').onclick=function(){{start(L.id)}};
  if(nxt)$('#nx').onclick=function(){{start(nxt.id)}};
  $('#menu').onclick=home;window.scrollTo(0,0);
}}
document.addEventListener('keydown',function(ev){{
  if($('#play').classList.contains('hide')||!S)return;
  var k={{'1':0,'2':1,'3':2,'4':3,'a':0,'b':1,'c':2,'d':3}}[ev.key.toLowerCase()];
  if(k!=null&&!S.locked&&document.querySelector('.opt')){{pick(k)}}
  else if((ev.key==='Enter'||ev.key==='ArrowRight')&&S.locked&&$('#next')){{ev.preventDefault();next()}}
  else if(ev.key==='Escape')home();
}});
var m=/^#L(\\d+)$/.exec(location.hash);
if(m&&LEVELS.some(function(x){{return x.id===+m[1]}}))start(+m[1]);else home();
}})();
</script></body></html>"""
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)
print("built index.html +", len(files), "wiki pages")
