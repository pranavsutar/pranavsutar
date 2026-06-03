"""Resume section component."""

from pathlib import Path

import streamlit as st

from utils.helpers import render_html, icon_svg
from utils.config import get_profile

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def render_resume() -> None:
    profile = get_profile()
    resume_path = PROJECT_ROOT / profile.get("resume_path", "assets/resume.pdf")

    if not resume_path.exists():
        render_html(
            '<p class="text-muted" style="text-align:center;">'
            "Resume PDF not found. Add your resume to "
            f'<code>{profile.get("resume_path", "assets/resume.pdf")}</code>.</p>'
        )
        return

    resume_bytes = resume_path.read_bytes()

    st.download_button(
        label=f"{icon_svg('download')}  Download Resume (PDF)",
        data=resume_bytes,
        file_name=f"{profile.get('first_name', 'resume')}_resume.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

    import base64

    b64 = base64.b64encode(resume_bytes).decode()
    render_html(
        f"""
        <div class="resume-viewer">
            <iframe
                src="data:application/pdf;base64,{b64}"
                width="100%"
                height="800px"
                style="border: 1px solid #30363D; border-radius: 12px;"
            ></iframe>
        </div>
        """
    )
