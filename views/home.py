from html import escape as e

import streamlit as st

from content import FEATURED, FOCUS, PROFILE, PROJECTS, ROLES, SKILLS, STATS
from ui import badges, cv_button, ext, head, html, project_card


def code_card() -> str:
    lines = [
        '<span class="k">const</span> <span class="v">arbin</span> = {',
        f'  <span class="v">role</span>: <span class="s">"Developer"</span>,',
        f'  <span class="v">based</span>: <span class="s">"{e(PROFILE["location"])}"</span>,',
        '  <span class="v">stack</span>: [<span class="s">"React"</span>, <span class="s">"Next.js"</span>, <span class="s">"TypeScript"</span>, <span class="s">"Django"</span>],',
        '  <span class="v">learning</span>: [<span class="s">"Jest"</span>, <span class="s">"Vitest"</span>, <span class="s">"SQL"</span>],',
        '  <span class="v">openToWork</span>: <span class="n">true</span>,',
        '};<span class="caret"></span>',
    ]
    body = "".join(f'<span class="cl" style="--i:{i}">{ln}</span>' for i, ln in enumerate(lines))
    return ('<div class="win"><div class="win-bar"><i></i><i></i><i></i><span>arbin.ts</span></div>'
            f'<div class="win-body">{body}</div></div>')


def hero() -> None:
    rolls = "".join(f"<b>{e(r)}</b>" for r in ROLES + ROLES[:1])
    html(
        '<div class="pf hero"><div>'
        f'<span class="live rv"><span class="dot"></span>Open to Developer roles</span>'
        f'<h1 class="rv" style="--d:100ms">Hi, I\'m <span class="shine">{e(PROFILE["name"].split()[0])}.</span></h1>'
        f'<div class="roll-line rv" style="--d:200ms">I build <span class="roll"><span class="roll-in">{rolls}</span></span></div>'
        f'<p class="lead rv" style="--d:300ms">{e(PROFILE["intro"])}</p>'
        f'<div class="btns rv" style="--d:400ms">{cv_button()}'
        f'{ext(PROFILE["featured_demo_url"], PROFILE["featured_demo_label"])}</div>'
        f'<p class="facts rv" style="--d:500ms">{e(PROFILE["facts"])}</p>'
        f'</div><div class="rv" style="--d:300ms">{code_card()}</div></div>'
    )
    st.page_link("views/projects.py", label="See all projects  →", width="content")


def marquee() -> None:
    techs = [t.strip() for _, v in SKILLS[:4] for t in v.split(",")]
    seen, uniq = set(), []
    for t in techs:
        if t.lower() not in seen:
            seen.add(t.lower())
            uniq.append(t)
    row = "".join(f"<span>{e(t)}</span>" for t in uniq)
    html(f'<div class="pf marq"><div class="marq-in">{row}{row}</div></div>')


def stats() -> None:
    cells = "".join(
        f'<div class="card stat sc" style="--d:{i * 90}ms"><div class="num" data-suf="{e(suf)}" '
        f'style="--to:{n};--d:{i * 120}ms"></div><p>{e(label)}</p></div>'
        for i, (n, suf, label) in enumerate(STATS))
    html(f'<div class="pf grid g4" style="margin-top:2rem">{cells}</div>')


def focus() -> None:
    html(head("What I do", "From design file to working feature",
              "The three areas I have worked in so far."))
    cards = "".join(
        f'<div class="card sc" style="--d:{i * 100}ms"><div class="icon">{e(t[0])}</div><h3>{e(t)}</h3>'
        f'<p style="margin:.5rem 0 1rem">{e(d)}</p>{badges(s)}</div>'
        for i, (t, d, s) in enumerate(FOCUS))
    html(f'<div class="pf grid g3">{cards}</div>')


def featured() -> None:
    html(head("Selected work", "Featured projects", "A few things I have built and can walk you through."))
    by_name = {p["name"]: p for p in PROJECTS}
    cards = "".join(
        project_card(i + 1, by_name[n], featured=(i == 0), delay=i * 100)
        for i, n in enumerate(FEATURED) if n in by_name)
    html(f'<div class="pf grid g2">{cards}</div>')
    st.page_link("views/projects.py", label="View every project  →", width="content")


def cta() -> None:
    html(
        '<div class="pf sec"><div class="cta sc"><span class="eyebrow">Let\'s talk</span>'
        '<h2 style="margin-top:.7rem!important">Looking for a developer?</h2>'
        '<p>I would like to learn from senior engineers and contribute from the first month.</p>'
        f'<div class="btns">{cv_button()}'
        f'{ext("mailto:" + PROFILE["email"], "Email me", "btn", arrow=False)}</div></div></div>'
    )


hero()
marquee()
stats()
focus()
featured()
cta()
