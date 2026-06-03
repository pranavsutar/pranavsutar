"""Skills page."""

from utils.helpers import section_header, spacer
from components.skills import render_skills


def render() -> None:
    section_header("Skills", "Technologies and tools I work with.")
    spacer(20)
    render_skills()
