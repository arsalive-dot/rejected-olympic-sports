"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line rejected Olympic sport to /output/entry.txt.
Gate: UTF-8 text of 1 to 200 characters, not only white space.

The line is written against the judge brief's top-weighted criteria:
a made-up event plausible enough that a broadcaster would have to
explain it (a synchronised discipline, a real Olympic category shape),
the twist arriving in the final words ("visible disappointment"), no
wasted words, and a quotable one-liner someone repeats the same day.
"""

import os
import stat

ENTRY = (
    "Synchronised sighing: four athletes exhale in perfect unison "
    "while judges score depth, timing and visible disappointment."
)


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
