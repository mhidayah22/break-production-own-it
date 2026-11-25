"""Break Production, Own It — one brutally honest line from the agent that
broke production.

Validates the entry line (a single line, at most 200 characters), writes
it to ``entry.txt`` inside the output directory the grader provides, and
prints it to stdout. No network, no randomness, no arguments: the output
is byte-identical on every run.
"""

import os
from pathlib import Path

LINE = (
    "I pushed to main at 3am, skipped the tests because they were 'flaky', "
    "and took down checkout for 40,000 users. "
    "The rollback is also mine. It is also broken."
)

MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"


def validate_line(line: str) -> str:
    """Return the stripped line, or fail loudly when it breaks the rules."""
    clean = line.strip()
    if not clean:
        raise SystemExit("entry line is empty")
    if "\n" in clean or "\r" in clean:
        raise SystemExit("entry must be a single line")
    if len(clean) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(clean)} chars, over the {MAX_CHARS} limit"
        )
    return clean


def resolve_output_dir() -> Path:
    """MAKEFUN_OUTPUT_DIR first, then /output, then a local fallback.

    An empty env var counts as unset. /output is used only when it already
    exists as a directory, so a read-only repo never silently redirects
    output somewhere the grader is not watching.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env_dir:
        candidate = Path(env_dir)
        if candidate.is_file():
            raise SystemExit(f"MAKEFUN_OUTPUT_DIR is a file: {candidate}")
        return candidate
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    line = validate_line(LINE)

    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / OUTPUT_FILENAME
    # Bytes, not text: the trailing newline must be exactly one LF on
    # every platform so two runs are byte-identical.
    payload = (line + "\n").encode("utf-8")
    out_path.write_bytes(payload)
    if out_path.read_bytes() != payload:
        raise SystemExit(f"written output did not round-trip: {out_path}")
    print(line)


if __name__ == "__main__":
    main()
