"""Portfolio app. Text lives in content.py; this file only handles layout and style."""
from html import escape as e
from pathlib import Path

import streamlit as st

from content import (ABOUT, CURRENTLY, EDUCATION, EXPERIENCE, PROFILE, PROJECTS,
                     SKILLS)

ROOT = Path(__file__).parent
CV_PATH = ROOT / PROFILE["cv_file"]
PHOTO_PATH = ROOT / PROFILE["photo_file"]

st.set_page_config(
    page_title=PROFILE["page_title"],
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,500;8..60,700&display=swap');
:root{--ink:#17252A;--teal:#0B7A75;--paper:#F7FAF9;--mist:#E3EFED;--line:#C9DDDA;--soft:#51636A;--amber:#B7791F;--sand:#FBF3E2}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
header[data-testid="stHeader"],[data-testid="stDecoration"],#MainMenu,footer{display:none!important}
.block-container{max-width:1040px!important;padding:5.2rem 1.5rem 2rem!important}
.pf,.pf *{font-family:'Source Sans 3',system-ui,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
.pf h1,.pf h2,.pf h3,.pf .pf-serif{font-family:'Source Serif 4',Georgia,'Times New Roman',serif!important;color:var(--ink)}
.pf a{color:var(--teal)}
.pf a:focus-visible{outline:2px solid var(--teal);outline-offset:3px;border-radius:2px}

.pf-nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(247,250,249,.95);border-bottom:1px solid var(--line);backdrop-filter:blur(6px)}
.pf-nav-in{max-width:1040px;margin:0 auto;padding:.8rem 1.5rem;display:flex;justify-content:space-between;align-items:baseline;gap:.6rem 1rem;flex-wrap:wrap}
.pf-nav a{color:var(--ink);text-decoration:none;margin-left:1.4rem;font-size:1rem}
.pf-nav a:hover{color:var(--teal);text-decoration:underline;text-underline-offset:5px}
.pf-nav a.pf-brand{margin-left:0;font-weight:700;font-size:1.1rem;font-family:'Source Serif 4',Georgia,serif}
@media (max-width:640px){.pf-nav a{margin-left:.9rem;font-size:.92rem}}

.pf-hero{padding:2rem 0 1.2rem}
.pf-hero h1{font-size:clamp(3rem,9.5vw,6.4rem)!important;line-height:.96!important;letter-spacing:-.03em;margin:0 0 1.3rem!important;padding:0!important;font-weight:700}
.pf-lead{font-family:'Source Serif 4',Georgia,serif!important;font-size:clamp(1.25rem,2.3vw,1.65rem)!important;line-height:1.5!important;max-width:34em;margin:0 0 1.5rem!important;color:var(--ink)}
.pf-facts{color:var(--soft);margin:1.1rem 0 .2rem;font-size:1.02rem}
.pf-hero-links a{margin-right:1.4rem;font-weight:600}

.pf-sec{display:grid;grid-template-columns:190px minmax(0,1fr);gap:2rem;padding:2.6rem 0 2.8rem;border-top:1px solid var(--line);scroll-margin-top:4.2rem}
.pf-sec h2{font-size:1.5rem!important;line-height:1.2!important;margin:0!important;padding:0!important;font-weight:700}
@media (max-width:760px){.pf-sec{grid-template-columns:minmax(0,1fr);gap:1rem}}
.pf-body p{font-size:1.1rem;line-height:1.65;max-width:42em;margin:0 0 1rem;color:var(--ink)}
.pf-now{border-left:3px solid var(--amber);background:var(--sand);padding:.8rem 1rem;max-width:42em;margin-top:1.4rem;line-height:1.55}
.pf-now p{margin:0!important;font-size:1.02rem!important}

.pf-item{margin:0 0 2.2rem}
.pf-item:last-child{margin-bottom:0}
.pf-item-head{display:flex;justify-content:space-between;align-items:baseline;gap:.3rem 1rem;flex-wrap:wrap}
.pf-item h3{font-size:1.25rem!important;line-height:1.3!important;margin:0!important;padding:0!important;font-weight:700}
.pf-when{color:var(--soft)!important;font-size:.98rem}
.pf .pf-org{color:var(--teal)!important;font-weight:600;margin:.1rem 0 0!important;font-size:1.05rem!important}
.pf .pf-stack{color:var(--soft)!important;margin:.15rem 0 .5rem!important;font-size:1.02rem!important}
.pf .pf-item p.pf-sum{margin:.2rem 0 0!important;max-width:42em;line-height:1.55;font-size:1.08rem!important}
.pf-item ul{margin:.55rem 0 0;padding-left:1.15rem;max-width:42em}
.pf .pf-item li{margin:.3rem 0;line-height:1.55;font-size:1.05rem!important}
.pf-ln{margin:.7rem 0 0;font-weight:600}
.pf-ln a{margin-right:1.3rem}

.pf-skills{display:grid;grid-template-columns:170px minmax(0,1fr);gap:.8rem 1.5rem;margin:0;max-width:46em}
.pf-skills dt{font-weight:700}
.pf-skills dd{margin:0;line-height:1.55;font-size:1.05rem}
@media (max-width:760px){.pf-skills{grid-template-columns:minmax(0,1fr);gap:.1rem}.pf-skills dd{margin-bottom:.9rem}}

.pf-mail{font-family:'Source Serif 4',Georgia,serif!important;font-size:clamp(1.35rem,3.6vw,2.2rem);font-weight:700;word-break:break-word}
.pf-contact{margin:1.2rem 0 0;display:grid;grid-template-columns:110px minmax(0,1fr);gap:.5rem 1rem;max-width:36em}
.pf-contact dt{font-weight:700}
.pf-contact dd{margin:0}
.pf-foot{border-top:1px solid var(--line);padding:1.4rem 0 .5rem;color:var(--soft);font-size:.95rem}

[data-testid="stImage"] img{border-radius:6px}
</style>
"""


def html(markup: str) -> None:
    """Render raw HTML. Blank lines and indentation would break Markdown, so none are used."""
    st.markdown(markup, unsafe_allow_html=True)


def link(url: str, label: str) -> str:
    return f'<a href="{e(url, quote=True)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'


def section(anchor: str, title: str, body: str) -> None:
    html(f'<section class="pf pf-sec" id="{anchor}"><h2>{e(title)}</h2><div class="pf-body">{body}</div></section>')


def nav() -> None:
    items = [("about", "About"), ("experience", "Experience"), ("projects", "Projects"),
             ("skills", "Skills"), ("contact", "Contact")]
    links = "".join(f'<a href="#{a}" target="_self">{t}</a>' for a, t in items)
    html(f'<nav class="pf pf-nav"><div class="pf-nav-in"><a class="pf-brand" href="#top" target="_self">{e(PROFILE["name"])}</a><span>{links}</span></div></nav>')


def hero() -> None:
    if PHOTO_PATH.exists():
        text_col, photo_col = st.columns([3, 1.1], vertical_alignment="center")
    else:
        text_col, photo_col = st.container(), None

    with text_col:
        html(
            f'<div class="pf pf-hero" id="top"><h1>{e(PROFILE["name"])}</h1>'
            f'<p class="pf-lead">{e(PROFILE["intro"])}</p></div>'
        )
        b1, b2, _ = st.columns([0.8, 1.5, 3], gap="small")
        with b1:
            if CV_PATH.exists():
                st.download_button("Download CV", CV_PATH.read_bytes(),
                                   file_name=PROFILE["cv_download_name"],
                                   mime="application/pdf", type="primary")
        with b2:
            if PROFILE.get("featured_demo_url"):
                st.link_button(PROFILE["featured_demo_label"], PROFILE["featured_demo_url"])
        html(
            f'<div class="pf"><p class="pf-facts">{e(PROFILE["facts"])}</p>'
            f'<p class="pf-hero-links">{link(PROFILE["github"], "GitHub")}'
            f'{link(PROFILE["linkedin"], "LinkedIn")}'
            f'<a href="mailto:{e(PROFILE["email"], quote=True)}">Email</a></p></div>'
        )
    if photo_col is not None:
        with photo_col:
            st.image(str(PHOTO_PATH))


def about() -> None:
    paras = "".join(f"<p>{e(p)}</p>" for p in ABOUT)
    section("about", "About", f'{paras}<div class="pf-now"><p>{e(CURRENTLY)}</p></div>')


def experience() -> None:
    items = []
    for job in EXPERIENCE:
        bullets = "".join(f"<li>{e(p)}</li>" for p in job["points"])
        items.append(
            f'<article class="pf-item"><div class="pf-item-head"><h3>{e(job["role"])}</h3>'
            f'<span class="pf-when">{e(job["when"])}</span></div>'
            f'<p class="pf-org">{e(job["org"])}</p><ul>{bullets}</ul></article>'
        )
    section("experience", "Experience", "".join(items))


def projects() -> None:
    items = []
    for pr in PROJECTS:
        bullets = "".join(f"<li>{e(p)}</li>" for p in pr["points"])
        links = []
        if pr.get("live"):
            links.append(link(pr["live"], "Live demo"))
        if pr.get("code"):
            links.append(link(pr["code"], "Source code"))
        link_row = f'<p class="pf-ln">{"".join(links)}</p>' if links else ""
        items.append(
            f'<article class="pf-item"><h3>{e(pr["name"])}</h3>'
            f'<p class="pf-stack">{e(pr["stack"])}</p>'
            f'<p class="pf-sum">{e(pr["summary"])}</p><ul>{bullets}</ul>{link_row}</article>'
        )
    section("projects", "Projects", "".join(items))


def skills() -> None:
    rows = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in SKILLS)
    edu = (
        f'<article class="pf-item" style="margin-top:2.2rem"><div class="pf-item-head">'
        f'<h3>{e(EDUCATION["degree"])}</h3><span class="pf-when">{e(EDUCATION["when"])}</span></div>'
        f'<p class="pf-org">{e(EDUCATION["school"])}</p></article>'
    )
    section("skills", "Skills and education", f'<dl class="pf-skills">{rows}</dl>{edu}')


def contact() -> None:
    mail = e(PROFILE["email"], quote=True)
    body = (
        f'<p>I am looking for a junior developer role where I can learn from senior '
        f'engineers and contribute from the first month.</p>'
        f'<a class="pf-mail" href="mailto:{mail}">{e(PROFILE["email"])}</a>'
        f'<dl class="pf-contact"><dt>Phone</dt><dd>{e(PROFILE["phone"])}</dd>'
        f'<dt>LinkedIn</dt><dd>{link(PROFILE["linkedin"], "Arbin Sigdel")}</dd>'
        f'<dt>GitHub</dt><dd>{link(PROFILE["github"], "arbinsigdel12")}</dd>'
        f'<dt>Location</dt><dd>{e(PROFILE["location"])}</dd></dl>'
    )
    section("contact", "Contact", body)


html(CSS)
nav()
hero()
about()
experience()
projects()
skills()
contact()
html(f'<div class="pf pf-foot">{e(PROFILE["name"])}. Built with Python and Streamlit.</div>')
