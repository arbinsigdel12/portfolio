from html import escape as e

from content import EXPERIENCE
from ui import badges, html, page_head

page_head("Experience", "Where I have worked.",
          "Two internships: Django on the backend, then React and Next.js on the frontend.")

items = []
for i, job in enumerate(EXPERIENCE):
    bullets = "".join(f"<li>{e(p)}</li>" for p in job["points"])
    items.append(
        f'<div class="tl-item sc" style="--d:{i * 100}ms"><div class="card">'
        f'<div class="tl-head"><h3>{e(job["role"])}</h3><span class="when">{e(job["when"])}</span></div>'
        f'<p class="org">{e(job["org"])}</p><ul>{bullets}</ul></div></div>'
    )
html(f'<div class="pf tl rv" style="--d:200ms;margin-top:2.5rem">{"".join(items)}</div>')
