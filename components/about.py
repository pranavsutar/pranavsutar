"""About section component."""

from utils.helpers import render_html, icon_svg
from utils.config import get_profile


def render_about() -> None:
    profile = get_profile()

    html = f"""
    <div class="about-container">
        <div class="about-content">
            <p class="about-bio">{profile["bio"]}</p>
            <div class="about-meta">
                <span class="about-meta-item">
                    {icon_svg("location")}
                    {profile.get("location", "")}
                </span>
                <span class="about-meta-item">
                    {icon_svg("email")}
                    <a href="mailto:{profile.get("email", "")}">{profile.get("email", "")}</a>
                </span>
            </div>
        </div>
    </div>
    """
    render_html(html)
