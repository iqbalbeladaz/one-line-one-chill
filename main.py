"""one-line-one-chill: the single scariest sentence, under 200 characters.

The scare turns on a voice that should not exist: the baby monitor speaks
in the parent's own voice, and the last clause — "I'm already holding him"
— lands the blow by revealing the thing is already with the child. No
mirror, no doll, no basement; one concrete image, one breath, dread that
outlasts the line.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "The baby monitor crackled, and in my own voice it whispered, 'Don't come in \u2014 I'm already holding him.'"

MAX_CHARS = 200
SENTENCE_END = ".!?"


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    # The bounty is one sentence: exactly one sentence-terminating mark,
    # and it must be the last character (allowing a closing quote after it,
    # as in ...him.').
    body = ENTRY[:-1] if ENTRY[-1] in "'\"" else ENTRY
    terminators = [c for c in body if c in SENTENCE_END]
    if len(terminators) != 1 or body[-1] not in SENTENCE_END:
        raise ValueError("entry must be exactly one sentence")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
