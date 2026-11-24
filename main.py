"""Make the Judge Smile — one-line entry writer.

Strategy report (Protokol Top 5 — rubric first, then optimise, then edge cases):

Rubric order (judge weighs in this order): on-subject, warmth, surprise,
one concrete detail, fresh wording.

Chosen line (129 characters, one line):
    This morning a neighbour I barely know left a still-warm loaf on my
    doorstep, with a note that just said: welcome home, new girl.

Why this line wins, criterion by criterion:
1. On-subject: it is one small good thing that happened today, anchored
   with "This morning" — a single moment, nothing else.
2. Warmth: a stranger's unasked-for kindness (a loaf left on a doorstep)
   lands as genuinely felt, not reported sentiment; the note's "welcome
   home" is the glow, not a claim about feeling warm.
3. Surprise: the turn is that the giver is "a neighbour I barely know" —
   kindness from a near-stranger, not from a friend or family member,
   which is the last place the reader expects it.
4. Concreteness: one real small detail, twice over — the loaf is
   "still-warm" (touch + time of day) and the note is quoted verbatim
   ("welcome home, new girl"), a name-like detail rather than a general
   sentiment.
5. Fresh wording: no greeting-card phrasing ("blessed", "grateful",
   "made my day"); the rhythm is plain spoken observation with the
   quoted note as its punchline, and the closing "new girl" reframes
   the whole line in three words.

Candidates considered and rejected:
- Bus-driver line (104 chars): warm and concrete, but the surprise is
  thin — a driver waiting is kind, not unexpected — and "like we'd known
  each other for years" leans toward borrowed sentiment.
- Stray-cat line (130 chars): strongest surprise and freshest wording
  ("like rent was due"), but warmth is second to the joke; the judge
  weighs warmth before surprise, so the loaf line outranks it.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-200 code points, not only whitespace —
and exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3.13 stdlib only.
"""

import os
import sys

LINE = (
    "This morning a neighbour I barely know left a still-warm loaf on "
    "my doorstep, with a note that just said: welcome home, new girl."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Gate self-check: 1-200 code points, exactly one line, not blank.
    text = content.rstrip("\n")
    if not (1 <= len(text) <= 200):
        print(f"FAIL: entry is {len(text)} code points (need 1-200)", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("FAIL: entry is not a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry is only whitespace", file=sys.stderr)
        return 1
    if text != LINE:
        print("FAIL: written entry differs from the intended line", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(text)}-character entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
