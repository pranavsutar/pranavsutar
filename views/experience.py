"""Experience page — timeline with section intro."""

from utils.helpers import section_header, spacer
from components.timeline import render_timeline


def render() -> None:
    section_header("Experience", "Where I've worked and what I've built.")
    spacer(20)
    render_timeline()
