#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

Writes the day's world-news image to /output/entry.png.

The image (assets/entry.png) was drawn at build time from the six biggest
world-news stories of Thursday 19 November 2026; this program simply copies
it to the output path, exactly like the kit's starter. No network, no clock,
no randomness, no third-party packages: two runs write byte-identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets" / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
