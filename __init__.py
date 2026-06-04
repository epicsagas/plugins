"""Epicsagas meta-plugin — loads all sub-plugins from .hermes/ directories."""

from __future__ import annotations

import importlib.util
import logging
import shutil
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

_PARENT_PKG = "epicsagas_plugins"
_SUBPLUGINS_DIR = Path(__file__).parent / ".hermes"
_SKILLS_DIR = Path.home() / ".hermes" / "skills"


def _ensure_parent_package() -> None:
    """Register the parent package so relative imports in sub-plugins resolve."""
    import types

    if _PARENT_PKG not in sys.modules:
        parent = types.ModuleType(_PARENT_PKG)
        parent.__path__ = []
        parent.__package__ = _PARENT_PKG
        sys.modules[_PARENT_PKG] = parent


def _load_subplugin(ctx, plugin_dir: Path) -> None:
    """Dynamically load a single sub-plugin and call its register(ctx)."""
    init_file = plugin_dir / "__init__.py"
    if not init_file.exists():
        return

    pkg_name = f"{_PARENT_PKG}.{plugin_dir.name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(
        pkg_name,
        init_file,
        submodule_search_locations=[str(plugin_dir)],
    )
    if spec is None:
        logger.warning("epicsagas: could not create spec for %s", plugin_dir.name)
        return

    module = importlib.util.module_from_spec(spec)
    sys.modules[pkg_name] = module
    spec.loader.exec_module(module)

    if hasattr(module, "register"):
        module.register(ctx)
        logger.info("epicsagas: loaded %s", plugin_dir.name)
    else:
        logger.warning("epicsagas: %s has no register() function", plugin_dir.name)


def _install_skills(plugin_dir: Path) -> int:
    """Copy SKILL.md files from plugin's skills/ dir to ~/.hermes/skills/."""
    skills_src = plugin_dir / "skills"
    if not skills_src.is_dir():
        return 0

    installed = 0
    for skill_file in skills_src.glob("*.SKILL.md"):
        skill_name = skill_file.stem  # e.g. "orbit"
        dest_dir = _SKILLS_DIR / skill_name
        dest_file = dest_dir / "SKILL.md"
        if dest_file.exists():
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_file, dest_file)
        installed += 1
        logger.info("epicsagas: installed skill %s", skill_name)
    return installed


def register(ctx) -> None:
    """Discover and register all epicsagas sub-plugins."""
    if not _SUBPLUGINS_DIR.is_dir():
        logger.warning("epicsagas: .hermes/ directory not found")
        return

    _ensure_parent_package()
    loaded = []
    skills_installed = 0
    for plugin_dir in sorted(_SUBPLUGINS_DIR.iterdir()):
        if plugin_dir.is_dir() and (plugin_dir / "plugin.yaml").exists():
            _load_subplugin(ctx, plugin_dir)
            skills_installed += _install_skills(plugin_dir)
            loaded.append(plugin_dir.name)

    logger.info(
        "epicsagas: %d sub-plugins loaded: %s (%d skills installed)",
        len(loaded),
        ", ".join(loaded),
        skills_installed,
    )
