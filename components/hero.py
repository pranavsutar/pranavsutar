"""Hero section — premium landing with animated orbs, portrait, stats."""

from pathlib import Path

from utils.helpers import render_html, icon_svg
from utils.config import get_profile, get_social_links

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def render_hero() -> None:
    profile = get_profile()
    socials = get_social_links()

    # Portrait (optional)
    portrait_html = ""
    avatar_path = profile.get("avatar", "")
    if avatar_path and (PROJECT_ROOT / avatar_path).exists():
        portrait_html = (
            '<div class="hero-portrait">'
            f'<img src="app/static/{avatar_path}" alt="{profile["name"]}">'
            "</div>"
        )

    # Status badge
    badge_text = profile.get("status_badge", "")
    badge_html = ""
    if badge_text:
        badge_html = (
            f'<div class="hero-badge">'
            f'<span class="hero-badge-dot"></span> {badge_text}'
            f"</div>"
        )

    # Headline — use hero_headline if set, else name
    headline = profile.get("hero_headline", "")
    name_html = f'<h1 class="hero-name">{profile["name"]}</h1>'
    headline_html = ""
    if headline:
        headline_html = f'<p class="hero-headline">{headline}</p>'

    # Subheadline
    sub = profile.get("hero_subheadline", profile.get("tagline", ""))
    sub_html = f'<p class="hero-subheadline">{sub}</p>'

    # Highlights
    highlights = profile.get("highlights", [])
    highlights_html = ""
    if highlights:
        chips = "".join(
            f'<span class="hero-highlight">{h}</span>' for h in highlights
        )
        highlights_html = f'<div class="hero-highlights">{chips}</div>'

    # Stats
    stats = profile.get("stats", [])
    stats_html = ""
    if stats:
        items = "".join(
            f'<div class="hero-stat">'
            f'<div class="hero-stat-value">{s["value"]}</div>'
            f'<div class="hero-stat-label">{s["label"]}</div>'
            f"</div>"
            for s in stats
        )
        stats_html = f'<div class="hero-stats">{items}</div>'

    # Social links
    social_links_html = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener" '
        f'class="hero-social-link" title="{s["platform"]}">'
        f'{icon_svg(s.get("icon", ""))}</a>'
        for s in socials
    )

    # CTA
    cta_label = profile.get("hero_cta_label", "")
    cta_html = ""
    if cta_label:
        cta_html = (
            f'<button class="hero-cta" onclick="void(0)">'
            f"{cta_label} →</button>"
        )

    html = f"""
    <div class="hero-wrapper">
        <div class="hero-bg">
            <div class="hero-orb hero-orb-1"></div>
            <div class="hero-orb hero-orb-2"></div>
            <div class="hero-orb hero-orb-3"></div>
        </div>
        <div class="hero-content">
            {portrait_html}
            {badge_html}
            {name_html}
            {headline_html}
            {sub_html}
            {highlights_html}
            {stats_html}
            <div class="hero-actions">
                {cta_html}
                <div class="hero-socials">{social_links_html}</div>
            </div>
        </div>
    </div>
    """
    render_html(html)
