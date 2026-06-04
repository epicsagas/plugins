"""Tool handlers for the llm-transpile Hermes plugin."""

import json
import subprocess


_TIMEOUT = 30


def _transpile(*args: str) -> subprocess.CompletedProcess:
    """Run the transpile CLI with the given arguments.

    Returns the CompletedProcess. Raises CalledProcessError on non-zero exit,
    or TimeoutExpired if the command exceeds _TIMEOUT seconds.
    """
    return subprocess.run(
        ["transpile", *args],
        capture_output=True,
        text=True,
        timeout=_TIMEOUT,
    )


def transpile_file(args: dict, **kwargs) -> str:
    """Convert a document to LLM-optimized format.

    Parameters
    ----------
    args : dict
        Must contain 'input_path' (str). Optional: 'format' (str), 'fidelity' (str).

    Returns
    -------
    str
        JSON with 'output' (transpiled content) or 'error'.
    """
    try:
        input_path = args["input_path"]
        cmd: list[str] = ["-i", input_path]

        fmt = args.get("format")
        if fmt:
            cmd.extend(["-f", fmt])

        fidelity = args.get("fidelity")
        if fidelity:
            cmd.extend(["-l", fidelity])

        result = _transpile(*cmd)

        if result.returncode != 0:
            stderr = result.stderr.strip()
            return json.dumps({"error": stderr or f"transpile exited with code {result.returncode}"})

        return json.dumps({"output": result.stdout})

    except subprocess.TimeoutExpired:
        return json.dumps({"error": f"transpile timed out after {_TIMEOUT}s"})
    except FileNotFoundError:
        return json.dumps({"error": "transpile CLI not found — is llm-transpile installed and on PATH?"})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def transpile_stats(args: dict, **kwargs) -> str:
    """Show transpile usage statistics.

    Parameters
    ----------
    args : dict
        Optional: 'days' (int), 'agent' (str).

    Returns
    -------
    str
        JSON with 'output' (ASCII table) or 'error'.
    """
    try:
        cmd: list[str] = ["stats", "show"]

        days = args.get("days")
        if days is not None:
            cmd.extend(["--days", str(days)])

        agent = args.get("agent")
        if agent:
            cmd.extend(["--agent", agent])

        result = _transpile(*cmd)

        if result.returncode != 0:
            stderr = result.stderr.strip()
            return json.dumps({"error": stderr or f"transpile stats exited with code {result.returncode}"})

        return json.dumps({"output": result.stdout})

    except subprocess.TimeoutExpired:
        return json.dumps({"error": f"transpile stats timed out after {_TIMEOUT}s"})
    except FileNotFoundError:
        return json.dumps({"error": "transpile CLI not found — is llm-transpile installed and on PATH?"})
    except Exception as exc:
        return json.dumps({"error": str(exc)})
