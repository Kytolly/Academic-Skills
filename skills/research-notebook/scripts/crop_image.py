#!/usr/bin/env python3
"""Crop a rendered paper page or source image with a checked pixel box."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        parts = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("box must contain integer pixels") from exc
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom")
    return parts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--box", required=True, type=parse_box, help="left,top,right,bottom in pixels")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"Input image does not exist: {args.input}")

    with Image.open(args.input) as image:
        left, top, right, bottom = args.box
        if left < 0 or top < 0 or right > image.width or bottom > image.height:
            parser.error(f"Crop box {args.box} exceeds image size {image.width}x{image.height}")
        if left >= right or top >= bottom:
            parser.error("Crop box must have positive width and height")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        image.crop(args.box).save(args.output, format="PNG", optimize=True)
        print(f"{args.output} ({right-left}x{bottom-top})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

