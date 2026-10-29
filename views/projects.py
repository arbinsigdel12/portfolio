from content import PROJECTS
from ui import html, page_head, project_card

page_head("Projects", "Things I have built.",
          "A storefront, a classifier, a mobile app and a retrieval chatbot. Each one taught me something different.")

cards = "".join(project_card(i + 1, p, featured=(i == 0), delay=(i % 2) * 100) for i, p in enumerate(PROJECTS))
html(f'<div class="pf grid g2 rv" style="--d:200ms;margin-top:2.5rem">{cards}</div>')
