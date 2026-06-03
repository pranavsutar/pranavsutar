"""Home — Hero → Snapshot → Featured Work → CTA.

Designed so a recruiter understands the candidate within 30 seconds.
"""

from utils.helpers import section_header, spacer, divider_line, render_html, icon_svg
from utils.config import get_featured_projects, get_contact_info, get_profile
from components.hero import render_hero
from components.snapshot import render_snapshot
from components.project_card import render_project_cards


def render() -> None:
    # 1. Hero — who is this person, what do they do
    render_hero()
    spacer(40)

    # 2. Snapshot — why keep reading (education, role, focus)
    render_snapshot()
    spacer(30)
    divider_line()

    # 3. Featured Work — evidence of ability, above experience
    featured = get_featured_projects()
    if featured:
        section_header("Featured Work", "Selected projects — each one shipped or prototyped end-to-end.")
        spacer(10)
        render_project_cards(featured)
        spacer(30)
        divider_line()

    # 4. Quick CTA — don't make them hunt for contact info
    profile = get_profile()
    contact = get_contact_info()
    email = contact.get("email", profile.get("email", ""))
    github = ""
    linkedin = ""
    from utils.config import get_social_links
    for s in get_social_links():
        if s.get("icon") == "github":
            github = s["url"]
        if s.get("icon") == "linkedin":
            linkedin = s["url"]

    links_html = ""
    if github:
        links_html += (
            f'<a href="{github}" target="_blank" rel="noopener" class="contact-resume-link">'
            f'{icon_svg("github", 16)} GitHub</a>'
        )
    if linkedin:
        links_html += (
            f'<a href="{linkedin}" target="_blank" rel="noopener" class="contact-resume-link">'
            f'{icon_svg("linkedin", 16)} LinkedIn</a>'
        )

    render_html(f"""
    <div style="text-align:center;padding:2rem 0;">
        <p style="font-size:1.2rem;font-weight:600;color:var(--text);margin:0 0 0.4rem;">
            Want to see more?
        </p>
        <p style="font-size:0.9rem;color:var(--text-secondary);margin:0 0 1.5rem;">
            Browse my experience, research, and full project list — or reach out directly.
        </p>
        <div class="contact-actions">
            <a href="mailto:{email}" class="contact-email-link">
                {icon_svg("email", 16)} Get in Touch
            </a>
            {links_html}
        </div>
    </div>
    """)
