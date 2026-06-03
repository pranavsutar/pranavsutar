"""Contact page — prominent CTA."""

from utils.helpers import section_header, spacer
from components.contact import render_contact


def render() -> None:
    section_header("Get in Touch", "Let's connect.")
    spacer(20)
    render_contact()
