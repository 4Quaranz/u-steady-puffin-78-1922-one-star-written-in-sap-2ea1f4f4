#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

A houseplant's one-star review of its human owner, written as a single
line. The program is fully deterministic: no input, no network, no
randomness, so every run produces exactly the same review text.

The review is written to /output/entry.txt, where the sealed scorer
checks it (UTF-8, 1 to 279 characters) and the judge reads it.
"""

from pathlib import Path

# One line, in the voice of a houseplant reviewing its owner.
ENTRY = (
    "★☆☆☆☆ My owner repotted me into a mug with no drainage "
    "'for the aesthetic', then blamed me for drowning. I asked for "
    "sunlight, not a swimming pool with a handle."
)

OUTPUT = Path("/output/entry.txt")


def check(text: str) -> str:
    """Keep only a non-blank line inside the scorer's 1-279 range."""
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("entry must not be blank")
    if len(cleaned) > 279:
        raise SystemExit(
            f"entry must be at most 279 characters, got {len(cleaned)}"
        )
    if "\n" in cleaned:
        raise SystemExit("entry must be a single line")
    return cleaned


def main() -> None:
    text = check(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    again = OUTPUT.read_text(encoding="utf-8")
    if again != text:
        raise SystemExit("entry.txt does not match the review")
    print(f"Wrote {len(text)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
