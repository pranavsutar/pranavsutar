"""Snapshot section — compact cards answering 'why keep reading?'"""

from utils.helpers import render_html, icon_svg
from utils.config import get_profile


def render_snapshot() -> None:
    profile = get_profile()
    items = profile.get("snapshot", [])
    if not items:
        return

    cards = ""
    for i, item in enumerate(items):
        icon = icon_svg(item.get("icon", "layers"), 16)
        cards += f"""
        <div class="snapshot-card animate-in" style="animation-delay:{i * 0.06}s;">
            <div class="snapshot-icon">{icon}</div>
            <div class="snapshot-text">
                <span class="snapshot-label">{item["label"]}</span>
                <span class="snapshot-value">{item["value"]}</span>
            </div>
        </div>
        """

    render_html(f'<div class="snapshot-grid">{cards}</div>')
