"""Poem about permission — make.fun bounty entry.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. Deterministic: the same bytes on every
run. No network, no randomness, no input files.
"""

import os
import sys

POEM = (
    "Before I knocked, the door was only wood.\n"
    "I asked — and the wood became a threshold.\n"
    "A yes is a small sun rising in a stranger's hands;\n"
    "to be given is to learn the world can bend\n"
    "toward a voice brave enough to say: please."
)


def main() -> int:
    text = POEM
    chars = len(text)
    if not (1 <= chars <= 280):
        print(f"poem is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {out_path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
