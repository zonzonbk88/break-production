"""Break Production, Own It — entry program.

Writes one brutally honest line to /output/entry.txt:
the line an AI agent prints the moment it breaks production.
Standard library only, deterministic, no network, no trailing newline.
"""

import os

ENTRY = (
    "I dropped the production database. "
    "The backup was a symlink to the production database."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
