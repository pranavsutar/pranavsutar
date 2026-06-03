"""Projects page — filterable project grid."""

import streamlit as st

from utils.helpers import section_header, spacer, render_html
from utils.config import get_all_projects
from components.project_card import render_project_cards


def render() -> None:
    section_header("Projects", "Things I've built and contributed to.")
    spacer(10)

    all_projects = get_all_projects()

    # Collect unique technologies for filter
    all_techs: set[str] = set()
    for p in all_projects:
        all_techs.update(p.get("technologies", []))
    tech_list = sorted(all_techs)

    # Filter controls
    col1, col2 = st.columns([1, 3])
    with col1:
        show = st.radio(
            "Show",
            ["All", "Featured"],
            horizontal=True,
            label_visibility="collapsed",
        )
    with col2:
        selected_tech = st.selectbox(
            "Filter by technology",
            ["All Technologies"] + tech_list,
            label_visibility="collapsed",
        )

    spacer(10)

    filtered = all_projects
    if show == "Featured":
        filtered = [p for p in filtered if p.get("featured")]
    if selected_tech != "All Technologies":
        filtered = [p for p in filtered if selected_tech in p.get("technologies", [])]

    if filtered:
        render_project_cards(filtered)
    else:
        render_html(
            '<p style="text-align:center;color:var(--text-muted);padding:2rem 0;">'
            "No projects match the current filter.</p>"
        )
