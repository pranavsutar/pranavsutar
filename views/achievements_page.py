"""Achievements page — filterable by category."""

import streamlit as st

from utils.helpers import section_header, spacer, render_html
from utils.config import get_achievements_list
from components.achievements import render_achievements


def render() -> None:
    section_header("Achievements", "Certifications, publications, talks, and awards.")
    spacer(10)

    achievements = get_achievements_list()
    categories = sorted({a.get("category", "other") for a in achievements})

    if len(categories) > 1:
        selected = st.radio(
            "Filter",
            ["All"] + [c.title() for c in categories],
            horizontal=True,
            label_visibility="collapsed",
        )
        spacer(10)

        if selected != "All":
            # Filter the config data temporarily via session
            filtered = [
                a for a in achievements if a.get("category", "").title() == selected
            ]
            from utils.helpers import icon_svg

            _CATEGORY_ICONS = {
                "certification": "cert", "publication": "publication",
                "talk": "talk", "award": "award",
            }
            _CATEGORY_LABELS = {
                "certification": "Certification", "publication": "Publication",
                "talk": "Talk", "award": "Award",
            }
            cards = ""
            for i, entry in enumerate(filtered):
                cat = entry.get("category", "award")
                icon = icon_svg(_CATEGORY_ICONS.get(cat, "award"), 16)
                label = _CATEGORY_LABELS.get(cat, cat.title())
                title_html = entry["title"]
                if entry.get("url"):
                    title_html = (
                        f'<a href="{entry["url"]}" target="_blank" rel="noopener" '
                        f'class="achievement-link">{entry["title"]} {icon_svg("external", 12)}</a>'
                    )
                cards += f"""
                <div class="achievement-card animate-in" style="animation-delay:{i*0.06}s;">
                    <div class="achievement-icon">{icon}</div>
                    <div class="achievement-content">
                        <div class="achievement-meta">
                            <span class="achievement-category">{label}</span>
                            <span class="achievement-date">{entry.get("date","")}</span>
                        </div>
                        <h3 class="achievement-title">{title_html}</h3>
                        <p class="achievement-description">{entry.get("description","")}</p>
                    </div>
                </div>
                """
            render_html(f'<div class="achievements-grid">{cards}</div>')
            return

    render_achievements()
