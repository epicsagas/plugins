"""Tool handlers for the obsidian-forge Hermes plugin."""

from __future__ import annotations

import json
import subprocess

_TIMEOUT = 60  # vault operations can be slow


def _of(*args: str) -> str:
    """Run the 'of' (obsidian-forge) CLI and return stdout.

    Raises RuntimeError on non-zero exit.
    Raises subprocess.TimeoutExpired if the command exceeds _TIMEOUT seconds.
    """
    result = subprocess.run(
        ["of", *args],
        capture_output=True,
        text=True,
        timeout=_TIMEOUT,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(stderr or f"of exited with code {result.returncode}")
    return result.stdout.strip()


def _ok(data: object) -> str:
    """Wrap a successful result as JSON."""
    return json.dumps({"ok": data})


def _err(message: str) -> str:
    """Wrap an error result as JSON."""
    return json.dumps({"error": message})


# ---------- handlers ----------


def vault_health(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Diagnose vault health and status."""
    try:
        cmd = ["doctor"]
        vault_path = args.get("vault_path")
        if vault_path:
            cmd.extend(["--vault-path", vault_path])

        output = _of(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def process_inbox(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Process all inbox notes with AI classification and PARA routing."""
    try:
        cmd = ["process-all"]
        vault = args.get("vault")
        if vault:
            cmd.extend(["--vault", vault])

        output = _of(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def graph_strengthen(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Strengthen knowledge graph connections."""
    try:
        cmd = ["strengthen-graph"]
        vault_path = args.get("vault_path")
        if vault_path:
            cmd.extend(["--vault-path", vault_path])

        output = _of(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def sync(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Run full sync cycle (MOC -> Graph -> Git)."""
    try:
        cmd = ["sync"]
        vault_path = args.get("vault_path")
        if vault_path:
            cmd.extend(["--vault-path", vault_path])

        output = _of(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def update_mocs(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Rebuild all project hub files (Maps of Content)."""
    try:
        cmd = ["update-mocs"]
        vault_path = args.get("vault_path")
        if vault_path:
            cmd.extend(["--vault-path", vault_path])

        output = _of(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


# ---------- mapping ----------

HANDLERS: dict[str, callable] = {
    "obsidian_vault_health": vault_health,
    "obsidian_process_inbox": process_inbox,
    "obsidian_graph_strengthen": graph_strengthen,
    "obsidian_sync": sync,
    "obsidian_update_mocs": update_mocs,
}
