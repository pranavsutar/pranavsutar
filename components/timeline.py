"""Experience timeline — vertical line with animated entries."""

from utils.helpers import render_html, tech_badges
from utils.config import get_experience


def _render_entry(entry: dict, index: int) -> str:
    badges = tech_badges(entry.get("technologies", []))
    return f"""
    <div class="timeline-entry animate-in" style="animation-delay:{index * 0.1}s;">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <div class="timeline-header">
                <h3 class="timeline-role">{entry["role"]}</h3>
                <span class="timeline-duration">{entry["duration"]}</span>
            </div>
            <p class="timeline-company">{entry["company"]}</p>
            <p class="timeline-description">{entry["description"]}</p>
            {badges}
        </div>
    </div>
    """


def render_timeline() -> None:
    experience = get_experience()
    entries = experience.get("entries", [])
    entries_html = "".join(_render_entry(e, i) for i, e in enumerate(entries))
    html = f"""
    <div class="timeline-container">
        <div class="timeline-line"></div>
        {entries_html}
    </div>
    """
    render_html(html)
