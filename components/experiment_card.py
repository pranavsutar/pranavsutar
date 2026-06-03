"""AI experiment cards — secondary accent, lab label."""

from utils.helpers import render_html, tech_badges, icon_svg


def _render_card(experiment: dict, index: int) -> str:
    badges = tech_badges(experiment.get("technologies", []))

    links = []
    if experiment.get("github_url"):
        links.append(
            f'<a href="{experiment["github_url"]}" target="_blank" rel="noopener" '
            f'class="project-link">{icon_svg("github", 14)} Code</a>'
        )
    if experiment.get("demo_url"):
        links.append(
            f'<a href="{experiment["demo_url"]}" target="_blank" rel="noopener" '
            f'class="project-link project-link-primary">{icon_svg("external", 14)} Live Demo</a>'
        )

    links_html = f'<div class="project-links">{"".join(links)}</div>' if links else ""

    return f"""
    <div class="experiment-card animate-in" style="animation-delay:{index * 0.08}s;">
        <span class="experiment-label">Experiment</span>
        <div class="project-card-content">
            <h3 class="project-title">{experiment["title"]}</h3>
            <p class="project-description">{experiment["description"]}</p>
            {badges}
            {links_html}
        </div>
    </div>
    """


def render_experiment_cards(experiments: list[dict]) -> None:
    if not experiments:
        return
    cards = "".join(_render_card(e, i) for i, e in enumerate(experiments))
    render_html(f'<div class="project-grid">{cards}</div>')
