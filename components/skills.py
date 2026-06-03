"""Skills section — grouped chips, no bars or percentages."""

from utils.helpers import render_html, icon_svg
from utils.config import get_profile


def _render_category(category: dict, delay: int) -> str:
    icon_name = category.get("icon", "layers")
    icon = icon_svg(icon_name, 16)

    items = category.get("items", [])
    # Support both old format (dicts with name/level) and new format (plain strings)
    chips = ""
    for item in items:
        name = item if isinstance(item, str) else item.get("name", "")
        chips += f'<span class="skill-chip">{name}</span>'

    return f"""
    <div class="skill-category animate-in" style="animation-delay:{delay * 0.08}s;">
        <div class="skill-category-header">
            <div class="skill-category-icon">{icon}</div>
            <h3 class="skill-category-title">{category["category"]}</h3>
        </div>
        <div class="skill-chips">{chips}</div>
    </div>
    """


def render_skills() -> None:
    profile = get_profile()
    categories = profile.get("skills", [])

    categories_html = "".join(
        _render_category(cat, i) for i, cat in enumerate(categories)
    )

    render_html(f'<div class="skills-grid">{categories_html}</div>')
