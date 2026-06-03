

Here's what you need to add to your local copy:

---

### 1. Replace `components/hero.py` entirely

Your current file has experiment card content instead of hero content. Replace the whole file with:

```python
"""Hero section — name, headline, social links as text pills."""

from utils.helpers import render_html
from utils.config import get_profile, get_social_links


def render_hero() -> None:
    profile = get_profile()
    socials = get_social_links()

    badge_text = profile.get("status_badge", "")
    badge_html = ""
    if badge_text:
        badge_html = (
            '<div class="hero-badge">'
            f'<span class="hero-badge-dot"></span> {badge_text}'
            '</div>'
        )

    name_html = f'<h1 class="hero-name">{profile["name"]}</h1>'

    headline = profile.get("hero_headline", "")
    headline_html = ""
    if headline:
        headline_html = f'<p class="hero-headline">{headline}</p>'

    sub = profile.get("hero_subheadline", profile.get("tagline", ""))
    sub_html = f'<p class="hero-subheadline">{sub}</p>'

    social_links = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener" '
        f'class="hero-social-link">{s["platform"]}</a>'
        for s in socials
    )
    socials_html = f'<div class="hero-socials">{social_links}</div>'

    html = (
        '<div class="hero-wrapper">'
        '<div class="hero-bg">'
        '<div class="hero-orb hero-orb-1"></div>'
        '<div class="hero-orb hero-orb-2"></div>'
        '<div class="hero-orb hero-orb-3"></div>'
        '</div>'
        '<div class="hero-content">'
        f'{badge_html}'
        f'{name_html}'
        f'{headline_html}'
        f'{sub_html}'
        f'{socials_html}'
        '</div>'
        '</div>'
    )
    render_html(html)
```

---

### 2. Replace `views/home.py` entirely

Adds CTA button + nav hint bar:

```python
"""Home — Hero → CTA → Snapshot → Featured Work → Contact form."""

import streamlit as st

from utils.helpers import section_header, spacer, divider_line, render_html
from utils.config import (
    get_featured_projects, get_contact_info, get_profile,
    get_social_links, get_theme,
)
from components.hero import render_hero
from components.snapshot import render_snapshot
from components.project_card import render_project_cards


def render() -> None:
    render_hero()

    spacer(10)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        cta_label = get_profile().get("hero_cta_label", "See What I've Built")
        if st.button(cta_label, use_container_width=True, type="primary"):
            st.session_state["nav_target"] = get_theme().get("section_titles", {}).get("projects", "Work")
            st.rerun()

    spacer(30)

    titles = get_theme().get("section_titles", {})
    nav_links = ""
    for key in ["projects", "experience", "experiments", "skills", "achievements", "resume", "contact"]:
        label = titles.get(key, key.title())
        nav_links += f'<span class="nav-hint-item">{label}</span>'
    render_html(
        '<div class="nav-hint">'
        f'<span class="nav-hint-label">Explore:</span> {nav_links}'
        '</div>'
    )

    spacer(20)

    render_snapshot()
    spacer(30)
    divider_line()

    featured = get_featured_projects()
    if featured:
        section_header("Featured Work", "Selected projects — each one shipped or prototyped end-to-end.")
        spacer(10)
        render_project_cards(featured)
        spacer(30)
        divider_line()

    profile = get_profile()
    contact = get_contact_info()
    email = contact.get("email", profile.get("email", ""))

    link_buttons = ""
    for s in get_social_links():
        link_buttons += (
            f'<a href="{s["url"]}" target="_blank" rel="noopener" '
            f'class="contact-resume-link">{s["platform"]}</a>'
        )

    render_html(
        '<div style="text-align:center;padding:2rem 0;">'
        '<p style="font-size:1.2rem;font-weight:600;color:var(--text);margin:0 0 0.4rem;">'
        'Want to see more?</p>'
        '<p style="font-size:0.9rem;color:var(--text-secondary);margin:0 0 1.5rem;">'
        'Browse my experience, research, and full project list &mdash; or reach out directly.</p>'
        '<div class="contact-actions">'
        f'<a href="mailto:{email}" class="contact-email-link">Get in Touch &rarr;</a>'
        f'{link_buttons}'
        '</div></div>'
    )
```

---

### 3. Replace `components/contact.py` entirely

Adds form with input fields:

```python
"""Contact section — form + social links."""

import streamlit as st

from utils.helpers import render_html
from utils.config import get_social_links, get_contact_info, get_profile


def render_contact() -> None:
    contact = get_contact_info()
    socials = get_social_links()
    profile = get_profile()
    email = contact.get("email", profile.get("email", ""))

    render_html(
        '<div style="text-align:center;max-width:560px;margin:0 auto 2rem;">'
        f'<p style="font-size:1rem;color:var(--text-secondary);line-height:1.7;">'
        f'{contact.get("subheading", "")}</p>'
        '</div>'
    )

    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
        with col2:
            sender_email = st.text_input("Your Email")

        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)

        submitted = st.form_submit_button(
            "Send Message", use_container_width=True, type="primary"
        )

        if submitted:
            if not name or not sender_email or not message:
                st.warning("Please fill in all fields.")
            else:
                mailto = (
                    f"mailto:{email}"
                    f"?subject={subject or 'Portfolio Contact'}"
                    f"&body=From: {name} ({sender_email})%0A%0A{message}"
                )
                st.success("Message ready! Click the link below to send via your email client.")
                st.markdown(f"[Open in email client]({mailto})")

    st.markdown("---")

    social_links_html = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener" '
        f'class="contact-social-card">{s["platform"]}</a>'
        for s in socials
    )

    render_html(
        '<div style="text-align:center;padding:1rem 0;">'
        '<p style="font-size:0.85rem;color:var(--text-muted);margin:0 0 0.75rem;">Or find me on</p>'
        f'<div class="contact-socials-grid">{social_links_html}</div>'
        '</div>'
    )
```

---

### 4. In `app.py`, find the `st.radio` block and replace it

Find this:

```python
    page = st.radio(
        "Navigate",
        options=NAV_ITEMS,
        label_visibility="collapsed",
    )
```

Replace with:

```python
    # Handle CTA navigation from home page
    default_index = 0
    if "nav_target" in st.session_state:
        target = st.session_state.pop("nav_target")
        if target in NAV_ITEMS:
            default_index = NAV_ITEMS.index(target)

    page = st.radio(
        "Navigate",
        options=NAV_ITEMS,
        index=default_index,
        label_visibility="collapsed",
    )
```

---

### 5. In `assets/theme.css`, add before `/* ---------- Utility ---------- */`

```css
/* ---------- Nav Hint ---------- */
.nav-hint {
    display: flex; align-items: center; justify-content: center;
    flex-wrap: wrap; gap: 0.4rem; padding: 0.75rem 0;
}
.nav-hint-label {
    font-size: 0.78rem; color: var(--text-muted); font-weight: 500; margin-right: 0.25rem;
}
.nav-hint-item {
    font-size: 0.78rem; color: var(--text-secondary); padding: 0.25rem 0.7rem;
    border-radius: 100px; border: 1px solid var(--border);
    transition: all 0.2s var(--ease);
}
.nav-hint-item:hover { border-color: var(--primary); color: var(--text); }
```

---

### 6. In `assets/theme.css`, find and replace the hero social link styles

Find:

```css
.hero-socials { display: flex; justify-content: center; gap: 0.75rem; }
.hero-social-link {
    display: flex; align-items: center; justify-content: center;
    width: 40px; height: 40px; border-radius: 50%;
```

Replace the entire `.hero-socials` and `.hero-social-link` blocks with:

```css
.hero-socials { display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap; }
.hero-social-link {
    display: inline-flex; align-items: center; padding: 0.45rem 1.1rem;
    border-radius: 100px; border: 1px solid var(--border);
    color: var(--text-secondary); font-size: 0.82rem; font-weight: 500;
    text-decoration: none; transition: all 0.25s var(--ease);
}
.hero-social-link:hover {
    border-color: var(--primary); color: var(--primary-light);
    background: rgba(108,99,255,0.06); transform: translateY(-2px);
}
```

---

That's everything. 4 file replacements, 2 edits in existing files.