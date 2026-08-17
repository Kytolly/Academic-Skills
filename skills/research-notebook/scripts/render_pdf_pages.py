#!/usr/bin/env python3
"""Render selected PDF pages to portable PNG files using PyMuPDF."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def parse_pages(spec: str, page_count: int) -> list[int]:
    pages: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" in item:
            start_text, end_text = item.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start > end:
                raise ValueError(f"Invalid descending page range: {item}")
            pages.update(range(start, end + 1))
        else:
            pages.add(int(item))
    if not pages:
        raise ValueError("No pages selected")
    invalid = sorted(page for page in pages if page < 1 or page > page_count)
    if invalid:
        raise ValueError(f"Pages outside PDF range 1-{page_count}: {invalid}")
    return sorted(pages)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--pages", required=True, help="1-based list or ranges, for example 1,3-5")
    parser.add_argument("--dpi", type=int, default=180)
    parser.add_argument("--prefix", default="page")
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"PDF does not exist: {args.pdf}")
    if args.dpi < 72 or args.dpi > 600:
        parser.error("--dpi must be between 72 and 600")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    document = fitz.open(args.pdf)
    try:
        pages = parse_pages(args.pages, document.page_count)
        matrix = fitz.Matrix(args.dpi / 72.0, args.dpi / 72.0)
        for page_number in pages:
            page = document.load_page(page_number - 1)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            output = args.output_dir / f"{args.prefix}-{page_number:03d}.png"
            pixmap.save(output)
            print(output)
    finally:
        document.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

