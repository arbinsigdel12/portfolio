from html import escape as e

from content import ABOUT, CURRENTLY, EDUCATION, PROFILE, SKILLS
from ui import ROOT, badges, cv_button, ext, head, html, page_head

page_head("About", "A developer who finishes what he starts.",
          "Computer Engineering graduate from Kathmandu, two internships in, and still learning every week.")

paras = "".join(f"<p>{e(p)}</p>" for p in ABOUT)
photo = ""
if (ROOT / PROFILE["photo_file"]).exists():
    photo = f'<img class="avatar sc" src="/{PROFILE["photo_url"]}" alt="{e(PROFILE["name"])}">'

html(
    f'<div class="pf prose rv" style="--d:200ms;margin-top:2.2rem">{paras}'
    f'<div class="btns">{cv_button()}{ext(PROFILE["github"], "GitHub", "btn")}'
    f'{ext(PROFILE["linkedin"], "LinkedIn", "btn")}</div></div>'
)
if photo:
    html(f'<div class="pf" style="max-width:18rem;margin-top:1.5rem">{photo}</div>')

html(head("At a glance", "The short version"))
html(
    '<div class="pf bento">'
    '<div class="card b-a sc"><span class="eyebrow">Currently</span>'
    f'<p class="now" style="margin-top:1rem">{e(CURRENTLY)}</p>'
    f'<dl class="kv"><dt>Based in</dt><dd>{e(PROFILE["location"])}</dd>'
    f'<dt>Experience</dt><dd>2 internships, 9 months in total</dd>'
    f'<dt>Looking for</dt><dd>Junior developer role</dd></dl></div>'
    '<div class="card b-b sc" style="--d:100ms"><span class="eyebrow">Education</span>'
    f'<h3 style="margin-top:1rem">{e(EDUCATION["degree"])}</h3>'
    f'<p style="margin-top:.5rem">{e(EDUCATION["school"])}</p>'
    f'<p class="when" style="margin-top:.8rem">{e(EDUCATION["when"])}</p></div>'
    '</div>'
)

html(head("Toolbox", "Skills and tools", "What I use, grouped by what I use it for."))
rows = "".join(
    f'<div class="skill-row"><h4>{e(k)}</h4>{badges(v, mono=False)}</div>' for k, v in SKILLS)
html(f'<div class="pf card sc">{rows}</div>')
