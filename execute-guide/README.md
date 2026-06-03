# Portfolio

A personal portfolio website for Data Engineers transitioning toward AI/ML and MLOps roles. Built with Streamlit.

## Local Development

```bash
pip install -e .
streamlit run app.py
```

## Configuration

All personal content lives in `config/` as YAML files:

| File | Purpose |
|---|---|
| `config/profile.yaml` | Name, title, bio, avatar, resume path |
| `config/experience.yaml` | Work history for the timeline |
| `config/projects.yaml` | Project cards (featured + all) |
| `config/achievements.yaml` | Certifications, awards, publications |
| `config/socials.yaml` | Social links and contact info |
| `config/theme.yaml` | Colors, fonts, UI tuning |

Edit these files to update the site — no code changes needed.

## Deploying to Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **New app** → select the repo, branch `main`, and file `app.py`.
4. Click **Deploy**.

The `pyproject.toml` declares all dependencies — Streamlit Cloud installs them automatically.

## Project Structure

```
app.py                  # Entry point
components/             # Reusable UI components
pages/                  # Page-level modules
config/                 # YAML content files
assets/                 # Static assets (images, resume PDF)
utils/                  # Config loader, helpers
.streamlit/config.toml  # Streamlit theme
```
