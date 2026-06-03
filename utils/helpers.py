"""Shared helper utilities.

NOTE: Streamlit's st.markdown() with unsafe_allow_html=True breaks when
inline <svg> elements are present — the entire HTML block renders as
escaped text. All icons use Unicode/HTML entities instead.
"""

from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def inject_css(css: str) -> None:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def load_css_file(filename: str) -> str:
    path = PROJECT_ROOT / "assets" / filename
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def render_html(html: str) -> None:
    """Render raw HTML.

    Collapses whitespace to a single line before rendering. Streamlit's
    markdown-it parser and DOMPurify both break on indented, multi-line
    HTML with blank lines between block elements.
    """
    import re
    # Collapse all runs of whitespace (including newlines) to a single space
    collapsed = re.sub(r"\s+", " ", html).strip()
    st.markdown(collapsed, unsafe_allow_html=True)


def spacer(height: int = 40) -> None:
    render_html(f'<div style="height: {height}px;"></div>')


def divider_line() -> None:
    render_html('<hr class="section-divider">')


def section_header(title: str, subtitle: str = "") -> None:
    html = f"""
    <div class="section-header">
        <h2 class="section-title">
            <span class="section-title-accent"></span>
            {title}
        </h2>
        {"<p class='section-subtitle'>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """
    render_html(html)


def tech_badge(name: str) -> str:
    return f'<span class="tech-badge">{name}</span>'


def tech_badges(technologies: list[str]) -> str:
    badges = " ".join(tech_badge(t) for t in technologies)
    return f'<div class="tech-badges">{badges}</div>'


def icon(name: str) -> str:
    """Return a Unicode/HTML entity icon. No SVGs — they break st.markdown."""
    icons = {
        "github": "&#9679;",       # bullet — styled via CSS
        "linkedin": "&#9679;",
        "twitter": "&#9679;",
        "blog": "&#9679;",
        "email": "&#9993;",        # ✉
        "external": "&#8599;",     # ↗
        "download": "&#8595;",     # ↓
        "award": "&#9733;",        # ★
        "cert": "&#9670;",         # ◆
        "talk": "&#9672;",         # ◈
        "publication": "&#9776;",  # ☰
        "location": "&#9906;",     # ⚲
        "flask": "&#9883;",        # ⚗
        "database": "&#9707;",     # ◫
        "cloud": "&#9729;",        # ☁
        "brain": "&#10047;",       # ✿
        "layers": "&#9776;",       # ☰
        "home": "&#8962;",         # ⌂
        "briefcase": "&#9776;",    # ☰
        "code": "&#10094;&#10095;",# <>
        "file": "&#9744;",         # ☐
        "arrow-right": "&#8594;",  # →
    }
    char = icons.get(name, "&#8226;")
    return f'<span class="icon icon-{name}">{char}</span>'


# Keep backward compatibility — old code calls icon_svg()
def icon_svg(name: str, size: int = 20) -> str:
    """Alias for icon(). Kept for backward compatibility."""
    return icon(name)
