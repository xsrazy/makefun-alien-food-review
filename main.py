"""Entry for make.fun bounty "One Star, Five Stars for the Food".

Writes a single-sentence, one-star review of Earth by an alien tourist
that still compliments the food, to /output/entry.txt.
Python standard library only, no network, deterministic.

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


def validate_entry(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.rstrip().count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate_entry(ENTRY)
    output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(output_dir, 0o755)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
