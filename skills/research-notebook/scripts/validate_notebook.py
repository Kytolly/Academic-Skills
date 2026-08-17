#!/usr/bin/env python3
"""Validate portable local image references and math syntax in a notebook."""

from __future__ import annotations

import argparse
import re
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote


IMAGE_RE = re.compile(r"!\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+['\"][^'\"]*['\"])?\)")
FORBIDDEN_MATH_RE = re.compile(r"\\\(|\\\)|\\\[|\\\]")
SECOND_LEVEL_HEADING_RE = re.compile(r"(?m)^##\s+(.+?)\s*$")
FIRST_HEADING_LABELS = {"One-Sentence Takeaway", "\u4e00\u53e5\u8bdd\u7ed3\u8bba"}
SECOND_HEADING_LABELS = {"Paper Information Card", "\u8bba\u6587\u4fe1\u606f\u5361\u7247"}
FORBIDDEN_CAPTION_SOURCE_RE = re.compile(
    r"Source visual|screenshot from|cropped from|PDF\s+p\.|截图来源|截取自|论文来源",
    re.IGNORECASE,
)


def strip_fenced_code(text: str) -> str:
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)


def validate_math(text: str) -> list[str]:
    body = strip_fenced_code(text)
    errors: list[str] = []
    for match in FORBIDDEN_MATH_RE.finditer(body):
        line = body.count("\n", 0, match.start()) + 1
        errors.append(f"line {line}: forbidden math delimiter; use $...$ or $$...$$")

    display_count = body.count("$$")
    if display_count % 2:
        errors.append("unbalanced $$ display-math delimiters")

    inline_body = body.replace("$$", "").replace("\\$", "")
    if inline_body.count("$") % 2:
        errors.append("unbalanced $ inline-math delimiters")
    return errors


def validate_heading_order(text: str) -> list[str]:
    body = strip_fenced_code(text)
    headings = SECOND_LEVEL_HEADING_RE.findall(body)
    if len(headings) < 2:
        return ["notebook must contain at least two second-level headings"]
    if headings[0] not in FIRST_HEADING_LABELS or headings[1] not in SECOND_HEADING_LABELS:
        return [
            "first two second-level headings must be "
            "'One-Sentence Takeaway' and 'Paper Information Card' "
            "or their supported localized equivalents"
        ]
    return []


def is_absolute_reference(reference: str) -> bool:
    return Path(reference).is_absolute() or PureWindowsPath(reference).is_absolute()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    args = parser.parse_args()

    if not args.notebook.is_file():
        parser.error(f"Notebook does not exist: {args.notebook}")

    text = args.notebook.read_text(encoding="utf-8")
    lines = text.splitlines()
    root = args.notebook.parent.resolve()
    asset_root = (root / "assets").resolve()
    errors: list[str] = []
    image_count = 0

    errors.extend(validate_math(text))
    errors.extend(validate_heading_order(text))

    for line_number, line in enumerate(lines, start=1):
        for match in IMAGE_RE.finditer(line):
            image_count += 1
            reference = unquote(match.group(1) or match.group(2)).replace("\\", "/")
            lower = reference.lower()
            if lower.startswith(("http://", "https://", "file://", "data:")) or is_absolute_reference(reference):
                errors.append(f"line {line_number}: non-portable image reference: {reference}")
                continue

            target = (args.notebook.parent / reference).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"line {line_number}: image escapes notebook directory: {reference}")
                continue
            if target.parent != asset_root:
                errors.append(f"line {line_number}: image must be stored directly in assets/: {reference}")
            if not target.is_file():
                errors.append(f"line {line_number}: missing image: {reference}")

            nearby_caption = "\n".join(lines[line_number : min(line_number + 3, len(lines))])
            if FORBIDDEN_CAPTION_SOURCE_RE.search(nearby_caption):
                errors.append(f"line {line_number}: image caption must not describe screenshot or paper source")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} error(s), {image_count} image(s) checked")
        return 1

    print(f"OK: {image_count} portable image reference(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
