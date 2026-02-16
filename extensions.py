from __future__ import annotations

import subprocess
from jinja2.ext import Extension

from slugify import slugify


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default


def to_slugify(value: str, separator: str = "_"):
    return slugify(value, separator=separator)


def to_yaml_list(value: str) -> str:
    """Convert a comma-separated string to a YAML inline list. e.g. "3.11, 3.12" -> '["3.11", "3.12"]'."""
    items = [v.strip() for v in value.split(",") if v.strip()]
    return "[" + ", ".join(f'"{item}"' for item in items) + "]"


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["to_slugify"] = to_slugify


class YamlListExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["to_yaml_list"] = to_yaml_list
