"""Portfolio entry point: page setup, global styles and top navigation.

Text lives in content.py, styles in styles.py, and each page in views/.
"""
import streamlit as st

from content import PROFILE
from styles import CSS
from ui import html

st.set_page_config(
    page_title=PROFILE["page_title"],
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html(CSS)

pages = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/about.py", title="About", url_path="about"),
    st.Page("views/experience.py", title="Experience", url_path="experience"),
    st.Page("views/projects.py", title="Projects", url_path="projects"),
    st.Page("views/contact.py", title="Contact", url_path="contact"),
]
st.navigation(pages, position="top").run()

html(
    f'<div class="pf foot"><span>&copy; 2026 {PROFILE["name"]}. Built with Python and Streamlit.</span>'
    f'<span><a href="{PROFILE["github"]}" target="_blank" rel="noopener noreferrer">GitHub</a> &nbsp;&middot;&nbsp; '
    f'<a href="{PROFILE["linkedin"]}" target="_blank" rel="noopener noreferrer">LinkedIn</a></span></div>'
)
