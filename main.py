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
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets" / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def _verify(path):
    """Fail loudly instead of handing the grader a broken image."""
    data = path.read_bytes()
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        raise SystemExit(f"error: {path} is not a valid PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            f"error: {path} is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    if data != SRC.read_bytes():
        raise SystemExit(f"error: {path} differs from {SRC}")
    return len(data)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    size = _verify(OUT)
    print(f"wrote {OUT} ({size} bytes, 1024x1024 PNG)", file=sys.stderr)


if __name__ == "__main__":
    main()
