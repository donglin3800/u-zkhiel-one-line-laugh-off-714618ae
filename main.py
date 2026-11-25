#!/usr/bin/env python3
"""One-Line Laugh-Off entry: a single cold-read joke.

The joke works in two beats. Beat one sets up the expensive,
respectable option (a therapist, $200 an hour, just to listen).
Beat two undercuts it with the free, disrespectful option everyone
actually has (the group chat), and the punch word is "harder": the
cheaper listener is also the crueller one, which is why it lands.
Every word earns its place: the price tag is the whole setup, and
there is no explanation after the punch.

The program writes that one line to /output/entry.txt, UTF-8, one
line with a single trailing newline. Standard library only, no
network, no randomness, no clock, so every run is byte-identical.
"""

import sys
from pathlib import Path

JOKE = "My therapist charges $200 an hour to listen; my group chat does it for free and roasts me harder."


def write_joke(line):
    """Check the gate, write the line, read it back to prove it."""
    line = line.strip()
    if not line or len(line) > 200:
        sys.exit(f"joke must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        sys.exit("joke must be a single line")
    for target in (Path("/output/entry.txt"), Path("output/entry.txt")):
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(line + "\n", encoding="utf-8")
            break
        except OSError:
            continue
    else:
        sys.exit("could not write entry.txt anywhere")
    if target.read_text(encoding="utf-8") != line + "\n":
        sys.exit("entry on disk does not match the joke")
    print(f"Wrote {len(line)}-character joke to {target}")


write_joke(JOKE)
