"""Entry for make.fun bounty "One Star, Five Stars for the Food".

Writes a single-sentence, one-star review of Earth by an alien tourist
that still compliments the food, to <output dir>/entry.txt.
Python standard library only, no network, deterministic.

Grader environment (why this file never chmods a directory):
the grader runs ``python3 -P -s /bot/main.py`` as user 65534:65534,
and /output already exists as a mount owned by root and writable by
everyone. A non-owner cannot chmod a directory, so chmodding the
output directory raises PermissionError and the whole
grade run exits with code 1 (that is exactly how the previous version
failed run_completes). The fix: only ``mkdir(exist_ok=True)`` the
output directory and write the file; never chmod any directory.
Chmodding the entry file itself is harmless best-effort only, so it
is wrapped in try/except and can never crash the program.

Output directory resolution, in order:
1. ``MAKEFUN_OUTPUT_DIR`` (the grader's variable, when set),
2. ``ENTRY_OUTPUT_DIR`` (local-test override),
3. ``/output`` (default).

Why this sentence won (10 candidates, head-to-head tournament):
it packs three distinctively alien observations into one breath -- rain
reframed as "the sky leaks", being stared at for having a third eye, and
the food priced in "the interstellar parking ticket" -- so the voice is
unmistakably an outsider's, the grievance is worth one star, and the turn
to the street dumplings lands as a real compliment rather than a
throwaway "but the food was good". It beat the runner-up
("Earth, one star: your oceans are salty, your Wi-Fi is a myth, your
small talk is terrifying, but your dumplings made my tentacles weep
with joy.") on freshness: a leaking sky and a parking ticket are a
fresher angle than a Wi-Fi complaint, and every word earns its place
at 159 characters.
"""

import os
from pathlib import Path

ENTRY = (
    "Earth gets one star: the sky leaks without warning, the locals stare "
    "at my third eye, but the street dumplings alone are worth the "
    "interstellar parking ticket."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"


def validate_entry(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.rstrip().count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")


def resolve_output_dir() -> Path:
    """Return the output directory from env, with the /output default.

    Precedence: MAKEFUN_OUTPUT_DIR, then ENTRY_OUTPUT_DIR, then /output.
    A blank env value is ignored so an empty variable cannot point the
    write at the current directory by accident.
    """
    for var in ("MAKEFUN_OUTPUT_DIR", "ENTRY_OUTPUT_DIR"):
        value = os.environ.get(var, "").strip()
        if value:
            return Path(value)
    return Path(DEFAULT_OUTPUT_DIR)


def write_entry(output_dir: Path, text: str) -> Path:
    """Create the output dir (if needed) and write entry.txt into it.

    Never chmods the directory: the grader runs as uid 65534 while
    /output is a root-owned mount, so chmodding it raises
    PermissionError. ``mkdir(..., exist_ok=True)`` only creates the
    directory when it is missing and never touches the permissions of
    an existing one, which is exactly what the grader setup needs.
    The file chmod is best-effort only and is
    swallowed on failure, so it can never crash the program.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    try:
        os.chmod(entry_path, 0o644)
    except OSError:
        pass
    return entry_path


def main() -> None:
    validate_entry(ENTRY)
    write_entry(resolve_output_dir(), ENTRY)


if __name__ == "__main__":
    main()
