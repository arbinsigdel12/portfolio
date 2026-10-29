"""Small HTML helpers shared by every page."""
from html import escape as e
from pathlib import Path
from urllib.parse import quote

import streamlit as st

from content import PROFILE

ROOT = Path(__file__).parent


def html(markup: str) -> None:
    """Render raw HTML. Keep it on one line: blank lines would break Markdown."""
    st.markdown(markup, unsafe_allow_html=True)


def ext(url: str, label: str, cls: str = "btn", arrow: bool = True) -> str:
    arr = ' <span class="arr">&#8599;</span>' if arrow else ""
    return (f'<a class="{cls}" href="{e(url, quote=True)}" target="_blank" '
            f'rel="noopener noreferrer">{e(label)}{arr}</a>')


def cv_button(cls: str = "btn primary") -> str:
    if not (ROOT / PROFILE["cv_file"]).exists():
        return ""
    return (f'<a class="{cls}" href="/{PROFILE["cv_url"]}" download="{e(PROFILE["cv_download_name"])}" '
            f'target="_self">Download CV <span class="arr">&#8595;</span></a>')


def badges(csv: str, mono: bool = True) -> str:
    cls = "badge mono" if mono else "badge"
    return '<div class="badges">' + "".join(
        f'<span class="{cls}">{e(t.strip())}</span>' for t in csv.split(",") if t.strip()) + "</div>"


def reveal(i: int = 0, scroll: bool = True) -> str:
    """Class + delay for the entrance animation. Items lower on the page reveal on scroll."""
    return f'class="rv{" sc" if scroll else ""}" style="--d:{i * 90}ms"'


def head(eyebrow: str, title: str, sub: str = "") -> str:
    p = f"<p>{e(sub)}</p>" if sub else ""
    return (f'<div class="pf sec-head sc"><span class="eyebrow">{e(eyebrow)}</span>'
            f'<h2>{e(title)}</h2>{p}</div>')


def page_head(eyebrow: str, title: str, sub: str) -> None:
    html(f'<div class="pf page-head"><span class="eyebrow rv">{e(eyebrow)}</span>'
         f'<h1 class="rv" style="--d:80ms">{e(title)}</h1><p class="rv" style="--d:160ms">{e(sub)}</p></div>')


def project_card(i: int, pr: dict, featured: bool = False, delay: int = 0) -> str:
    links = []
    if pr.get("live"):
        links.append(ext(pr["live"], "Live demo", "btn sm primary"))
    if pr.get("code"):
        links.append(ext(pr["code"], "Source", "btn sm"))
    link_row = f'<div class="proj-links">{"".join(links)}</div>' if links else ""
    bullets = "".join(f"<li>{e(p)}</li>" for p in pr["points"])
    tag = '<span class="tag-feat">Featured</span>' if featured else ""
    return (f'<article class="card proj {"glow" if featured else ""} sc" style="--d:{delay}ms">'
            f'<div class="proj-top"><span class="idx">0{i}</span>{tag}</div>'
            f'<h3>{e(pr["name"])}</h3><p class="sum">{e(pr["summary"])}</p><ul>{bullets}</ul>'
            f'{link_row}{badges(pr["stack"])}</article>')


def mailto(subject: str = "", body: str = "") -> str:
    q = []
    if subject:
        q.append("subject=" + quote(subject))
    if body:
        q.append("body=" + quote(body))
    return f'mailto:{PROFILE["email"]}' + ("?" + "&".join(q) if q else "")
