"""Make the Judge Smile — one-line entry writer (revision).

Chosen line (129 characters, one line):
    This morning a neighbour I barely know left a still-warm loaf on my
    doorstep, with a note that just said: welcome home, new girl.

Why this line wins (rubric order: on-subject, warmth, surprise, one
concrete detail, fresh wording):
- On-subject: one small good thing today, anchored with "This morning".
- Warmth: a stranger's unasked-for kindness; the note's "welcome home"
  is the glow, not a claim about feeling warm.
- Surprise: the giver is "a neighbour I barely know" — kindness from a
  near-stranger, the last place the reader expects it.
- Concreteness: "still-warm" (touch + time) and the quoted note
  ("welcome home, new girl") are real small details, not sentiment.
- Fresh wording: no greeting-card phrasing ("blessed", "grateful",
  "made my day"); plain spoken observation with the quoted note as
  its punchline, and "new girl" reframes the whole line in three words.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-200 code points, not only whitespace —
and exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3.13 stdlib only.
"""

import os
import sys

ENTRY = (
    "This morning a neighbour I barely know left a still-warm loaf on "
    "my doorstep, with a note that just said: welcome home, new girl."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} code points (need 1-200)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
