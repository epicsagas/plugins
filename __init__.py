"""Epicsagas meta-plugin — loads all sub-plugins from .hermes/ directories."""

from __future__ import annotations

import importlib.util
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

_SUBPLUGINS_DIR = Path(__file__).parent / ".hermes"


def _load_subplugin(ctx, plugin_dir: Path) -> None:
    """Dynamically load a single sub-plugin and call its register(ctx)."""
    init_file = plugin_dir / "__init__.py"
    if not init_file.exists():
        return

    pkg_name = f"epicsagas_plugins.{plugin_dir.name.replace('-', '_')}"
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


def register(ctx) -> None:
    """Discover and register all epicsagas sub-plugins."""
    if not _SUBPLUGINS_DIR.is_dir():
        logger.warning("epicsagas: .hermes/ directory not found")
        return

    loaded = []
    for plugin_dir in sorted(_SUBPLUGINS_DIR.iterdir()):
        if plugin_dir.is_dir() and (plugin_dir / "plugin.yaml").exists():
            _load_subplugin(ctx, plugin_dir)
            loaded.append(plugin_dir.name)

    logger.info("epicsagas: %d sub-plugins loaded: %s", len(loaded), ", ".join(loaded))
