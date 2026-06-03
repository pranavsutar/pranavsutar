"""AI & Research page — what I explore outside my primary responsibilities."""

from utils.helpers import section_header, spacer, render_html, icon_svg
from utils.config import get_experiments
from components.experiment_card import render_experiment_cards


def render() -> None:
    section_header(
        "AI & Research",
        "What I explore outside my primary responsibilities.",
    )
    spacer(10)

    render_html(f"""
    <div style="
        display:flex;align-items:flex-start;gap:0.75rem;
        padding:1rem 1.25rem;border-radius:var(--radius-sm);
        background:rgba(0,212,170,0.04);border:1px solid rgba(0,212,170,0.12);
        margin-bottom:1.5rem;
    ">
        <span style="color:var(--secondary);flex-shrink:0;margin-top:2px;">{icon_svg("flask", 18)}</span>
        <p style="font-size:0.85rem;color:var(--text-secondary);margin:0;line-height:1.6;">
            These are side projects and research work — object detection, LLM prototypes,
            ML monitoring tools. Not production systems, but evidence of where I'm heading.
        </p>
    </div>
    """)

    render_experiment_cards(get_experiments())
