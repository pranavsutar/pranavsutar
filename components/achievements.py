"""Achievements — compact cards with icon badges."""

from utils.helpers import render_html, icon_svg
from utils.config import get_achievements_list

_CATEGORY_ICONS = {
    "certification": "cert",
    "publication": "publication",
    "talk": "talk",
    "award": "award",
}
_CATEGORY_LABELS = {
    "certification": "Certification",
    "publication": "Publication",
    "talk": "Talk",
    "award": "Award",
}


def _render_achievement(entry: dict, index: int) -> str:
    category = entry.get("category", "award")
    icon = icon_svg(_CATEGORY_ICONS.get(category, "award"), 16)
    label = _CATEGORY_LABELS.get(category, category.title())

    title_html = entry["title"]
    if entry.get("url"):
        title_html = (
            f'<a href="{entry["url"]}" target="_blank" rel="noopener" '
            f'class="achievement-link">{entry["title"]} {icon_svg("external", 12)}</a>'
        )

    return f"""
    <div class="achievement-card animate-in" style="animation-delay:{index * 0.06}s;">
        <div class="achievement-icon">{icon}</div>
        <div class="achievement-content">
            <div class="achievement-meta">
                <span class="achievement-category">{label}</span>
                <span class="achievement-date">{entry.get("date", "")}</span>
            </div>
            <h3 class="achievement-title">{title_html}</h3>
            <p class="achievement-description">{entry.get("description", "")}</p>
        </div>
    </div>
    """


def render_achievements() -> None:
    achievements = get_achievements_list()
    if not achievements:
        return
    cards = "".join(_render_achievement(a, i) for i, a in enumerate(achievements))
    render_html(f'<div class="achievements-grid">{cards}</div>')
