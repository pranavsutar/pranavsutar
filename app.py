"""Portfolio — entry point."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st

from utils.config import get_profile, get_theme
from utils.helpers import inject_css, load_css_file, render_html
from views import (
    home,
    experience,
    projects,
    experiments,
    achievements_page,
    skills_page,
    resume_page,
    contact_page,
)

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
profile = get_profile()
st.set_page_config(
    page_title=f"{profile['name']} — Portfolio",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Global styles
# ---------------------------------------------------------------------------
css = load_css_file("theme.css")
if css:
    inject_css(css)

# ---------------------------------------------------------------------------
# Sidebar — nav order optimized for recruiter scanning
# ---------------------------------------------------------------------------
theme = get_theme()
titles = theme.get("section_titles", {})

# Order: Home → Work → Experience → AI & Research → Skills → Achievements → Resume → Contact
NAV_ITEMS = [
    titles.get("hero", "Home"),
    titles.get("projects", "Work"),
    titles.get("experience", "Experience"),
    titles.get("experiments", "AI & Research"),
    titles.get("skills", "Skills"),
    titles.get("achievements", "Achievements"),
    titles.get("resume", "Resume"),
    titles.get("contact", "Contact"),
]

with st.sidebar:
    render_html(
        f'<div class="sidebar-header">'
        f'<div class="sidebar-logo">◆</div>'
        f'<div>'
        f'<div class="sidebar-name">{profile["name"]}</div>'
        f'<div class="sidebar-title">{profile.get("title", "")}</div>'
        f'</div>'
        f'</div>'
    )

    page = st.radio(
        "Navigate",
        options=NAV_ITEMS,
        label_visibility="collapsed",
    )

    render_html(
        '<div style="position:fixed;bottom:0;left:0;width:inherit;'
        'padding:0.75rem 1rem;border-top:1px solid var(--border);'
        'font-size:0.7rem;color:var(--text-muted);background:var(--surface);">'
        'Built with Streamlit</div>'
    )

# ---------------------------------------------------------------------------
# Page router
# ---------------------------------------------------------------------------
PAGE_MAP = {
    titles.get("hero", "Home"): home,
    titles.get("projects", "Work"): projects,
    titles.get("experience", "Experience"): experience,
    titles.get("experiments", "AI & Research"): experiments,
    titles.get("skills", "Skills"): skills_page,
    titles.get("achievements", "Achievements"): achievements_page,
    titles.get("resume", "Resume"): resume_page,
    titles.get("contact", "Contact"): contact_page,
}

module = PAGE_MAP.get(page, home)
module.render()
