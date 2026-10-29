from html import escape as e

import streamlit as st

from content import PROFILE
from ui import ext, html, mailto, page_head

page_head("Contact", "Let's work together.",
          "I am looking for a junior developer role. The fastest way to reach me is email.")

html(
    f'<div class="pf rv" style="--d:200ms;margin-top:2rem"><a class="mail" href="mailto:{e(PROFILE["email"], quote=True)}">'
    f'{e(PROFILE["email"])}</a></div>'
)

chan = [
    ("In", "LinkedIn", "Arbin Sigdel", PROFILE["linkedin"]),
    ("Gh", "GitHub", "arbinsigdel12", PROFILE["github"]),
    ("Ph", "Phone", PROFILE["phone"], "tel:" + PROFILE["phone"].replace(" ", "")),
    ("Lo", "Location", PROFILE["location"], ""),
]
cards = "".join(
    (f'<a class="card chan sc" style="--d:{i * 80}ms" href="{e(u, quote=True)}" target="_blank" rel="noopener noreferrer">'
     if u else f'<div class="card chan sc" style="--d:{i * 80}ms">')
    + f'<div class="icon">{ic}</div><div><small>{lab}</small><b>{e(val)}</b></div>'
    + ("</a>" if u else "</div>")
    for i, (ic, lab, val, u) in enumerate(chan))
html(f'<div class="pf grid g2" style="margin-top:2.5rem">{cards}</div>')

html('<div class="pf sec-head sc" style="margin-top:3.5rem"><span class="eyebrow">Quick message</span>'
     '<h2>Write it here, send it from your mail app</h2>'
     '<p>This opens your email program with the message filled in. Nothing is stored on this site.</p></div>')

c1, c2 = st.columns(2, gap="medium")
with c1:
    name = st.text_input("Your name", placeholder="Jane Doe")
with c2:
    subject = st.text_input("Subject", placeholder="Junior developer opportunity")
msg = st.text_area("Message", placeholder="Hi Arbin, ...", height=140)

body = (msg + ("\n\n" + name if name else "")).strip()
html(f'<div class="btns">{ext(mailto(subject or "Hello from your portfolio", body), "Open in my email app", "btn primary")}</div>')
