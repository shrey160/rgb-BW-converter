"""
RGB -> Black & White (Grayscale) image converter.

Usage:
  python rgb_to_bw_converter.py path/to/image.jpg

Output:
  Saves next to the input file as: <original_name>_BW<original_ext>
  Example: photo.png -> photo_BW.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def build_output_path(input_path: Path, suffix: str = "_BW") -> Path:
    # Keep the same directory and extension, just add suffix to the stem.
    return input_path.with_name(f"{input_path.stem}{suffix}{input_path.suffix}")


def convert_to_bw(input_path: Path, output_path: Path) -> None:
    # Pillow can convert many formats; force load then convert to grayscale ("L").
    with Image.open(input_path) as img:
        bw = img.convert("L")
        bw.save(output_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert an RGB image to black & white (grayscale) and save alongside the original."
    )
    parser.add_argument(
        "image_path",
        type=str,
        help="Path to the input image (e.g., C:\\images\\photo.jpg).",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="_BW",
        help="Suffix to append to the output filename (default: _BW).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output file if it already exists.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.image_path).expanduser()

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if not input_path.is_file():
        raise SystemExit(f"Input path is not a file: {input_path}")

    output_path = build_output_path(input_path, suffix=args.suffix)

    if output_path.exists() and not args.overwrite:
        raise SystemExit(
            f"Output file already exists: {output_path}\n"
            f"Re-run with --overwrite to replace it, or change --suffix."
        )

    convert_to_bw(input_path, output_path)
    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

