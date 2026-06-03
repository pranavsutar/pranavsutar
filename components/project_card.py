"""Project cards — problem / approach / what I built / what I learned."""

from utils.helpers import render_html, tech_badges, icon_svg


def _par(label: str, text: str) -> str:
    """Render a labeled paragraph block."""
    if not text:
        return ""
    return f"""
    <div class="project-par">
        <span class="project-par-label">{label}</span>
        <p class="project-par-text">{text}</p>
    </div>
    """


def _render_card(project: dict, index: int) -> str:
    badges = tech_badges(project.get("technologies", []))

    # Support multiple card formats:
    # 1. New: problem / approach / built / learned
    # 2. Legacy: problem / approach / result
    # 3. Fallback: description
    problem = project.get("problem", "")
    approach = project.get("approach", "")
    built = project.get("built", "")
    learned = project.get("learned", "")
    result = project.get("result", "")
    description = project.get("description", "")

    if problem:
        body_html = _par("Problem", problem)
        body_html += _par("Approach", approach)
        body_html += _par("What I Built", built)
        body_html += _par("What I Learned", learned)
        if not built and not learned:
            body_html += _par("Result", result)
    else:
        body_html = f'<p class="project-description">{description}</p>'

    links = []
    if project.get("github_url"):
        links.append(
            f'<a href="{project["github_url"]}" target="_blank" rel="noopener" '
            f'class="project-link">{icon_svg("github", 14)} Code</a>'
        )
    if project.get("demo_url"):
        links.append(
            f'<a href="{project["demo_url"]}" target="_blank" rel="noopener" '
            f'class="project-link project-link-primary">{icon_svg("external", 14)} Demo</a>'
        )

    links_html = ""
    if links:
        links_html = f'<div class="project-links">{"".join(links)}</div>'

    return f"""
    <div class="project-card animate-in" style="animation-delay:{index * 0.08}s;">
        <div class="project-card-content">
            <h3 class="project-title">{project["title"]}</h3>
            {body_html}
            {badges}
            {links_html}
        </div>
    </div>
    """


def render_project_cards(projects: list[dict]) -> None:
    if not projects:
        return
    cards = "".join(_render_card(p, i) for i, p in enumerate(projects))
    render_html(f'<div class="project-grid">{cards}</div>')
