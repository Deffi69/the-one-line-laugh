"""make.fun The One-Line Laugh entry.

Writes a single funny sentence to /output/entry.txt.
"""

import os

LINE = (
    "I bought a standing desk to fix my posture, "
    "so now I slouch vertically instead of horizontally."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
