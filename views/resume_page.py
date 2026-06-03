"""Resume page — PDF viewer and download."""

from utils.helpers import section_header, spacer
from components.resume import render_resume


def render() -> None:
    section_header("Resume", "Download or view my resume.")
    spacer(20)
    render_resume()
