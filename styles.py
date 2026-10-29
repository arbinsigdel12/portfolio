"""Global CSS: a dark, shadcn-style theme with CSS-only animations (no JavaScript needed)."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500&display=swap');

:root{
  --bg:#050506; --card:rgba(255,255,255,.03); --card-hi:rgba(255,255,255,.055);
  --line:rgba(255,255,255,.09); --line-hi:rgba(255,255,255,.2);
  --fg:#fafafa; --muted:#a1a1aa; --dim:#71717a;
  --accent:#2dd4bf; --accent2:#818cf8; --ok:#4ade80;
  --r:14px;
  --sans:'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --mono:'Geist Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@property --n{syntax:'<integer>';initial-value:0;inherits:false}
@property --ang{syntax:'<angle>';initial-value:0deg;inherits:false}

/* ---------- Streamlit chrome ---------- */
html{scroll-behavior:smooth}
.stApp{background:var(--bg)!important;color:var(--fg)}
.stApp,.stApp div,.stApp p,.stApp a,.stApp li,.stApp label,.stApp input,.stApp textarea,.stApp button,.stApp h1,.stApp h2,.stApp h3,.stApp h4,.stApp dt,.stApp dd,.stApp b{font-family:var(--sans)}
.stApp code,.stApp pre,.pf-mono{font-family:var(--mono)!important}
[data-testid="stDecoration"],#MainMenu,footer,[data-testid="stStatusWidget"],[data-testid="stAppDeployButton"]{display:none!important}
[data-testid="stMainBlockContainer"],.block-container{
  max-width:1120px!important;padding:6.2rem 1.5rem 3rem!important;
  animation:pagein .6s cubic-bezier(.16,1,.3,1) both}
@keyframes pagein{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
[data-testid="stVerticalBlock"]{gap:0}

/* Page backdrop: faint grid + colour glows that slowly drift */
.stApp::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);
  background-size:56px 56px;
  -webkit-mask-image:radial-gradient(ellipse 80% 60% at 50% 0%,#000 30%,transparent 75%);
  mask-image:radial-gradient(ellipse 80% 60% at 50% 0%,#000 30%,transparent 75%)}
.stApp::after{content:"";position:fixed;z-index:0;pointer-events:none;width:60vmax;height:60vmax;left:50%;top:-38vmax;
  transform:translateX(-50%);border-radius:50%;filter:blur(90px);opacity:.5;
  background:radial-gradient(circle at 35% 40%,rgba(45,212,191,.28),transparent 55%),radial-gradient(circle at 70% 55%,rgba(129,140,248,.22),transparent 55%);
  animation:drift 18s ease-in-out infinite alternate}
@keyframes drift{from{transform:translateX(-56%) scale(1)}to{transform:translateX(-44%) scale(1.12)}}
[data-testid="stMain"],[data-testid="stAppViewContainer"]{position:relative;z-index:1}

/* ---------- Top navigation (st.navigation) ---------- */
header[data-testid="stHeader"]{background:rgba(5,5,6,.72)!important;backdrop-filter:blur(14px) saturate(1.4);
  -webkit-backdrop-filter:blur(14px) saturate(1.4);border-bottom:1px solid var(--line);height:3.6rem}
header[data-testid="stHeader"] *{color:var(--muted)}
header[data-testid="stHeader"] a,header[data-testid="stHeader"] button{
  border-radius:9px!important;font-weight:500!important;transition:color .2s,background .2s}
header[data-testid="stHeader"] a:hover,header[data-testid="stHeader"] button:hover{
  color:var(--fg)!important;background:rgba(255,255,255,.07)!important}
header[data-testid="stHeader"] a[aria-current="page"],
header[data-testid="stHeader"] a[aria-current="page"] *{color:var(--fg)!important;background:rgba(255,255,255,.09)!important}

/* ---------- Generic building blocks ---------- */
.pf{color:var(--fg)}
.pf *{box-sizing:border-box}
.pf a,.pf a:hover{color:inherit;text-decoration:none!important}
.pf h1,.pf h2,.pf h3,.pf h4{font-family:var(--sans)!important;color:var(--fg);letter-spacing:-.025em;padding:0!important;margin:0}
:where(.pf) p{margin:0}
.eyebrow{font-family:var(--mono)!important;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.sec{margin-top:5.5rem}
.sec-head{margin:4.5rem 0 2rem;max-width:40rem}
.sec-head h2{font-size:clamp(1.9rem,4.4vw,2.7rem)!important;line-height:1.1!important;font-weight:700!important;margin-top:.6rem!important}
.sec-head p{color:var(--muted);font-size:1.08rem;line-height:1.6;margin-top:.8rem}
.page-head{padding:1rem 0 .5rem;max-width:44rem}
.page-head h1{font-size:clamp(2.4rem,6.4vw,4.2rem)!important;line-height:1.02!important;font-weight:800!important;margin:.7rem 0 1rem!important;
  background:linear-gradient(180deg,#fff 30%,#a1a1aa);-webkit-background-clip:text;background-clip:text;color:transparent!important}
.page-head p{margin-top:.2rem!important;color:var(--muted);font-size:1.15rem;line-height:1.65}

/* Buttons (shadcn look) */
.btns{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.8rem}
.btn{display:inline-flex;align-items:center;gap:.5rem;height:2.7rem;padding:0 1.15rem;border-radius:10px;font-weight:600;font-size:.95rem;
  border:1px solid var(--line);background:rgba(255,255,255,.03);color:var(--fg)!important;position:relative;overflow:hidden;
  transition:transform .2s,background .2s,border-color .2s,box-shadow .2s;cursor:pointer}
.btn:hover{transform:translateY(-2px);border-color:var(--line-hi);background:rgba(255,255,255,.08)}
.btn.primary{background:#fafafa;color:#09090b!important;border-color:#fafafa}
.btn.primary:hover{background:#fff;box-shadow:0 0 0 4px rgba(250,250,250,.12),0 10px 40px -8px rgba(45,212,191,.55)}
.btn.primary::after{content:"";position:absolute;inset:0;background:linear-gradient(110deg,transparent 35%,rgba(45,212,191,.35) 50%,transparent 65%);
  transform:translateX(-120%);animation:sheen 3.8s ease-in-out infinite}
@keyframes sheen{0%,55%{transform:translateX(-120%)}100%{transform:translateX(120%)}}
.btn .arr{transition:transform .2s}
.btn:hover .arr{transform:translateX(4px)}
.btn.sm{height:2.2rem;padding:0 .9rem;font-size:.86rem;border-radius:8px}

/* Badges */
.badge{display:inline-flex;align-items:center;gap:.45rem;padding:.28rem .7rem;border-radius:999px;border:1px solid var(--line);
  background:rgba(255,255,255,.04);color:var(--muted);font-size:.8rem;font-weight:500;transition:all .2s;white-space:nowrap}
.badge:hover{color:var(--fg);border-color:var(--line-hi);background:rgba(255,255,255,.08)}
.badge.mono{font-family:var(--mono)!important;font-size:.76rem}
.badges{display:flex;flex-wrap:wrap;gap:.45rem}
.live{display:inline-flex;align-items:center;gap:.55rem;padding:.35rem .85rem .35rem .65rem;border-radius:999px;border:1px solid rgba(74,222,128,.28);
  background:rgba(74,222,128,.07);color:#bbf7d0;font-size:.82rem;font-weight:500}
.dot{width:.5rem;height:.5rem;border-radius:50%;background:var(--ok);position:relative}
.dot::after{content:"";position:absolute;inset:0;border-radius:50%;background:var(--ok);animation:ping 1.8s cubic-bezier(0,0,.2,1) infinite}
@keyframes ping{75%,100%{transform:scale(3.2);opacity:0}}

/* Cards */
.card{position:relative;border:1px solid var(--line);background:var(--card);border-radius:var(--r);padding:1.5rem;
  transition:transform .35s cubic-bezier(.16,1,.3,1),border-color .3s,background .3s,box-shadow .3s;overflow:hidden}
.card::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .4s;
  background:radial-gradient(420px circle at 50% -10%,rgba(45,212,191,.16),transparent 60%)}
.card:hover{transform:translateY(-4px);border-color:var(--line-hi);background:var(--card-hi);box-shadow:0 24px 60px -24px rgba(0,0,0,.9)}
.card:hover::before{opacity:1}
.card h3{font-size:1.22rem!important;font-weight:650!important;line-height:1.3!important}
.card p{color:var(--muted);line-height:1.6;font-size:.98rem}
.card ul{margin:.9rem 0 0;padding-left:1.1rem;color:var(--muted)}
.card li{margin:.4rem 0;line-height:1.55;font-size:.96rem}
.card li::marker{color:var(--accent)}
.grid{display:grid;gap:1rem}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media(max-width:900px){.g3,.g4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){.g2,.g3,.g4{grid-template-columns:minmax(0,1fr)}}

/* Animated gradient border for featured cards */
.glow{border:1px solid transparent;background:linear-gradient(#0b0b0e,#0b0b0e) padding-box,
  conic-gradient(from var(--ang),rgba(255,255,255,.08),var(--accent),rgba(255,255,255,.08) 40%,var(--accent2),rgba(255,255,255,.08)) border-box;
  animation:spin 6s linear infinite}
.glow:hover{background:linear-gradient(#101014,#101014) padding-box,
  conic-gradient(from var(--ang),rgba(255,255,255,.08),var(--accent),rgba(255,255,255,.08) 40%,var(--accent2),rgba(255,255,255,.08)) border-box}
@keyframes spin{to{--ang:360deg}}

/* ---------- Scroll / load reveal ---------- */
.rv{animation:rise .8s cubic-bezier(.16,1,.3,1) both;animation-delay:var(--d,0ms)}
@keyframes rise{from{opacity:0;transform:translateY(26px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
@supports (animation-timeline:view()){
  .sc{animation:rise linear both;animation-timeline:view();animation-range:entry 5% entry 45%;animation-delay:0ms}
}

/* ---------- Home: hero ---------- */
.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:3rem;align-items:center;padding:1.5rem 0 1rem}
@media(max-width:900px){.hero{grid-template-columns:minmax(0,1fr);gap:2.5rem}}
.hero h1{font-size:clamp(2.7rem,7vw,5rem)!important;line-height:1!important;font-weight:800!important;letter-spacing:-.04em!important;margin:1.4rem 0 0!important}
.shine{background:linear-gradient(100deg,#fff 20%,#2dd4bf 40%,#818cf8 60%,#fff 80%);background-size:250% 100%;
  -webkit-background-clip:text;background-clip:text;color:transparent!important;animation:shine 7s linear infinite}
@keyframes shine{to{background-position:-250% 0}}
.roll-line{font-size:clamp(1.5rem,3.4vw,2.2rem);font-weight:600;letter-spacing:-.03em;margin-top:.9rem;color:var(--muted);display:flex;gap:.55rem;flex-wrap:wrap}
.roll{display:inline-block;height:1.3em;overflow:hidden;vertical-align:bottom}
.roll-in{display:flex;flex-direction:column;animation:roll 12s cubic-bezier(.7,0,.2,1) infinite}
.roll-in b{display:block;height:1.3em;line-height:1.3em;font-weight:600;color:var(--fg);white-space:nowrap}
@keyframes roll{0%,20%{transform:translateY(0)}25%,45%{transform:translateY(-1.3em)}50%,70%{transform:translateY(-2.6em)}75%,95%{transform:translateY(-3.9em)}100%{transform:translateY(-5.2em)}}
.lead{color:var(--muted);font-size:1.16rem;line-height:1.7;max-width:34rem;margin-top:1.4rem!important}
.facts{color:var(--dim);font-size:.92rem;margin:1.6rem 0 0!important}

/* Code window */
.win{border:1px solid var(--line);border-radius:16px;background:rgba(10,10,13,.8);backdrop-filter:blur(8px);overflow:hidden;
  box-shadow:0 40px 100px -30px rgba(45,212,191,.28),0 0 0 1px rgba(255,255,255,.02) inset;animation:float 7s ease-in-out infinite}
@keyframes float{50%{transform:translateY(-10px)}}
.win-bar{display:flex;align-items:center;gap:.45rem;padding:.75rem 1rem;border-bottom:1px solid var(--line);background:rgba(255,255,255,.025)}
.win-bar i{width:.7rem;height:.7rem;border-radius:50%;background:#3f3f46;display:block}
.win-bar i:nth-child(1){background:#f87171}.win-bar i:nth-child(2){background:#fbbf24}.win-bar i:nth-child(3){background:#4ade80}
.win-bar span{margin-left:.6rem;font-family:var(--mono)!important;font-size:.76rem;color:var(--dim)}
.win-body{padding:1.1rem 1.2rem 1.3rem;font-family:var(--mono)!important;font-size:.86rem;line-height:1.85;color:#d4d4d8;overflow-x:auto}
.cl{display:block;white-space:pre;opacity:0;animation:typeline .5s ease-out forwards;animation-delay:calc(.6s + var(--i)*.28s)}
@keyframes typeline{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}
.k{color:#c084fc}.s{color:#86efac}.v{color:#7dd3fc}.n{color:#fda4af}.c{color:#52525b}
.caret{display:inline-block;width:.55ch;height:1.1em;background:var(--accent);vertical-align:-.18em;margin-left:2px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}

/* Marquee */
.marq{margin-top:4rem;overflow:hidden;position:relative;border-block:1px solid var(--line);padding:1.05rem 0;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.marq-in{display:flex;gap:2.6rem;width:max-content;animation:marq 38s linear infinite}
.marq:hover .marq-in{animation-play-state:paused}
.marq-in span{font-family:var(--mono)!important;font-size:.95rem;color:var(--dim);white-space:nowrap;transition:color .2s;display:flex;align-items:center;gap:2.6rem}
.marq-in span::after{content:"";width:5px;height:5px;border-radius:50%;background:var(--line-hi)}
.marq-in span:hover{color:var(--fg)}
@keyframes marq{to{transform:translateX(-50%)}}

/* Stats */
.stat{text-align:left;padding:1.4rem 1.5rem}
.num{font-size:clamp(2.2rem,5vw,3.2rem);font-weight:800;letter-spacing:-.04em;line-height:1;color:var(--fg);
  animation:count 1.8s cubic-bezier(.2,.8,.2,1) both;animation-delay:var(--d,0ms);counter-reset:n var(--n)}
.num::after{content:counter(n) attr(data-suf)}
@keyframes count{from{--n:0}to{--n:var(--to)}}
.stat p{margin-top:.5rem;font-size:.9rem;color:var(--muted)}

/* Focus cards */
.icon{width:2.6rem;height:2.6rem;border-radius:10px;display:grid;place-items:center;border:1px solid var(--line);
  background:linear-gradient(135deg,rgba(45,212,191,.2),rgba(129,140,248,.14));font-family:var(--mono)!important;font-weight:500;color:var(--fg);font-size:.95rem;margin-bottom:1.1rem}

/* Project cards */
.proj{display:flex;flex-direction:column;height:100%;min-height:18rem}
.proj-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.1rem}
.idx{font-family:var(--mono)!important;font-size:.78rem;color:var(--dim)}
.proj h3{margin-bottom:.35rem!important}
.proj .sum{color:var(--fg);opacity:.85;margin:.2rem 0 .9rem}
.proj .badges{margin-top:auto;padding-top:1.1rem}
.proj-links{display:flex;gap:.6rem;margin-top:1.1rem;flex-wrap:wrap}
.tag-feat{font-family:var(--mono)!important;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:linear-gradient(90deg,var(--accent),#a5b4fc);padding:.15rem .55rem;border-radius:999px;font-weight:600}

/* Timeline */
.tl{position:relative;padding-left:2.2rem;margin-top:.5rem}
.tl::before{content:"";position:absolute;left:.55rem;top:.4rem;bottom:.4rem;width:2px;border-radius:2px;
  background:linear-gradient(var(--accent),var(--accent2),transparent);transform-origin:top;animation:draw 1.6s cubic-bezier(.16,1,.3,1) both}
@keyframes draw{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.tl-item{position:relative;margin-bottom:1.4rem}
.tl-item::before{content:"";position:absolute;left:-2.2rem;top:1.65rem;width:1.15rem;height:1.15rem;border-radius:50%;
  background:var(--bg);border:2px solid var(--accent);box-shadow:0 0 0 5px rgba(45,212,191,.12),0 0 24px rgba(45,212,191,.5)}
.tl-head{display:flex;justify-content:space-between;align-items:baseline;gap:.4rem 1rem;flex-wrap:wrap}
.when{font-family:var(--mono)!important;font-size:.8rem;color:var(--dim)}
.org{color:var(--accent)!important;font-weight:500;font-size:.98rem!important;margin:.25rem 0 0!important}

/* About: skill groups, bento */
.bento{display:grid;gap:1rem;grid-template-columns:repeat(6,minmax(0,1fr))}
.bento>.b-a{grid-column:span 4}.bento>.b-b{grid-column:span 2}.bento>.b-c{grid-column:span 3}.bento>.b-d{grid-column:span 3}
@media(max-width:800px){.bento>*{grid-column:span 6!important}}
.kv{display:grid;grid-template-columns:auto 1fr;gap:.7rem 1.2rem;margin-top:1rem;font-size:.95rem}
.kv dt{color:var(--dim)}.kv dd{margin:0;color:var(--fg)}
.now{border-left:2px solid var(--accent);padding:.2rem 0 .2rem 1rem;color:var(--fg)!important;font-size:1.02rem!important}
.prose p{font-size:1.1rem;line-height:1.75;color:#d4d4d8;margin-bottom:1.1rem;max-width:44rem}
.avatar{width:100%;aspect-ratio:1;border-radius:var(--r);object-fit:cover;border:1px solid var(--line)}
.skill-row{padding:1.15rem 0;border-top:1px solid var(--line)}
.skill-row:first-child{border-top:0;padding-top:0}
.skill-row h4{font-size:.8rem!important;font-family:var(--mono)!important;text-transform:uppercase;letter-spacing:.12em;color:var(--dim)!important;font-weight:500!important;margin-bottom:.7rem!important}

/* CTA */
.cta{text-align:center;padding:3.5rem 1.5rem;border-radius:20px;border:1px solid var(--line);position:relative;overflow:hidden;
  background:radial-gradient(600px circle at 50% 0%,rgba(45,212,191,.16),transparent 60%),rgba(255,255,255,.02)}
.cta h2{font-size:clamp(1.8rem,4.4vw,2.8rem)!important;font-weight:700!important;line-height:1.1!important}
.cta p{color:var(--muted);margin:1rem auto 0;max-width:30rem;line-height:1.6}
.cta .btns{justify-content:center}

/* Contact */
.mail{display:block;font-size:clamp(1.3rem,3.6vw,2.2rem);font-weight:700;letter-spacing:-.03em;word-break:break-word;
  background:linear-gradient(90deg,#fff,#2dd4bf,#818cf8,#fff);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;
  color:transparent!important;animation:shine 8s linear infinite;margin-top:.8rem}
.chan{display:flex;align-items:center;gap:1rem}
.chan .icon{margin:0;flex:none}
.chan small{display:block;color:var(--dim);font-size:.78rem;font-family:var(--mono)!important;text-transform:uppercase;letter-spacing:.1em}
.chan b{display:block;font-weight:600;font-size:1rem;word-break:break-word}

.foot{margin-top:5rem;padding:1.6rem 0 .5rem;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;color:var(--dim);font-size:.88rem}
.foot a:hover{color:var(--fg)}

/* ---------- Streamlit widgets, restyled ---------- */
[data-testid="stTextInput"] input,[data-testid="stTextArea"] textarea{background:rgba(255,255,255,.03)!important;border:1px solid var(--line)!important;
  border-radius:10px!important;color:var(--fg)!important;transition:border-color .2s,box-shadow .2s}
[data-testid="stTextInput"] input:focus,[data-testid="stTextArea"] textarea:focus{border-color:var(--accent)!important;box-shadow:0 0 0 3px rgba(45,212,191,.18)!important}
[data-testid="stTextInput"] label p,[data-testid="stTextArea"] label p{color:var(--muted)!important;font-size:.88rem!important}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="base-input"]{background:transparent!important;border-color:transparent!important}
[data-testid="stCode"]{border:1px solid var(--line);border-radius:10px;overflow:hidden}
[data-testid="stCode"] pre{background:rgba(255,255,255,.03)!important}
[data-testid="stPageLink"]{margin-top:1.1rem}
[data-testid="stPageLink"] a{border-radius:10px!important;border:1px solid var(--line);background:rgba(255,255,255,.03);transition:all .2s}
[data-testid="stPageLink"] a:hover{border-color:var(--line-hi);background:rgba(255,255,255,.08);transform:translateX(3px)}
[data-testid="stPageLink"] p{color:var(--fg)!important;font-weight:500}
::selection{background:rgba(45,212,191,.35)}
::-webkit-scrollbar{width:10px}::-webkit-scrollbar-thumb{background:#27272a;border-radius:10px;border:2px solid var(--bg)}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;scroll-behavior:auto!important}
  .marq-in{animation:none}
}
</style>
"""
