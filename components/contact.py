"""Contact section — dual CTA + social grid."""

from utils.helpers import render_html, icon_svg
from utils.config import get_social_links, get_contact_info, get_profile


def render_contact() -> None:
    contact = get_contact_info()
    socials = get_social_links()
    profile = get_profile()

    cta_label = contact.get("cta_label", "Say Hello")
    resume_label = contact.get("cta_resume_label", "Download Resume")
    email = contact.get("email", profile.get("email", ""))

    social_links_html = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener" class="contact-social-card">'
        f'<span class="contact-social-icon">{icon_svg(s.get("icon", ""), 16)}</span>'
        f'<span class="contact-social-name">{s["platform"]}</span>'
        f"</a>"
        for s in socials
    )

    html = f"""
    <div class="contact-container animate-in">
        <p class="contact-subheading">{contact.get("subheading", "")}</p>
        <div class="contact-actions">
            <a href="mailto:{email}" class="contact-email-link">
                {icon_svg("email", 18)} {cta_label}
            </a>
            <a href="#" class="contact-resume-link" onclick="return false;">
                {icon_svg("download", 16)} {resume_label}
            </a>
        </div>
        <div class="contact-socials-grid">{social_links_html}</div>
    </div>
    """
    render_html(html)
