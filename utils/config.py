"""YAML configuration loader with caching."""

from pathlib import Path

import yaml
import streamlit as st

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


@st.cache_data(ttl=300)
def _load_yaml(filename: str) -> dict:
    path = CONFIG_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_profile() -> dict:
    return _load_yaml("profile.yaml")


def get_experience() -> dict:
    return _load_yaml("experience.yaml")


def get_projects() -> dict:
    return _load_yaml("projects.yaml")


def get_achievements() -> dict:
    return _load_yaml("achievements.yaml")


def get_socials() -> dict:
    return _load_yaml("socials.yaml")


def get_theme() -> dict:
    return _load_yaml("theme.yaml")


def get_featured_projects() -> list[dict]:
    """Return featured projects sorted by rank (lower = higher priority)."""
    projects = get_projects().get("projects", [])
    featured = [p for p in projects if p.get("featured")]
    return sorted(featured, key=lambda p: p.get("rank", 999))


def get_all_projects() -> list[dict]:
    """Return all projects sorted by rank."""
    projects = get_projects().get("projects", [])
    return sorted(projects, key=lambda p: p.get("rank", 999))


def get_experiments() -> list[dict]:
    return get_achievements().get("experiments", [])


def get_achievements_list() -> list[dict]:
    return get_achievements().get("achievements", [])


def get_social_links() -> list[dict]:
    return get_socials().get("links", [])


def get_contact_info() -> dict:
    return get_socials().get("contact", {})


def get_snapshot() -> list[dict]:
    return get_profile().get("snapshot", [])
