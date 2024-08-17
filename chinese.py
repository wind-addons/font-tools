import argparse
from pathlib import Path

from fontTools.ttLib import TTFont
from utils import (
    better_chinese_dot,
    enforce_corner_brackets,
    zhu_to_dot,
    update_name_with,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Modify the Chinese font file for better WoW game experience."
    )
    parser.add_argument(
        "-f", "--font", type=str, required=True, help="Path to the input font file"
    )
    parser.add_argument("-o", "--output", type=str, help="Path to the output font file")
    parser.add_argument(
        "--better-chinese-dot",
        action="store_true",
        help="Replace '‧' with '·' in the font",
    )
    parser.add_argument(
        "--zhu-to-dot",
        action="store_true",
        help="Replace '丶' with '·' in the font",
    )
    parser.add_argument(
        "--enforce-corner-brackets",
        action="store_true",
        help="Enforce corner brackets for quotes",
    )

    parser.add_argument(
        "--font-name",
        type=str,
        default="$NAME$ WindModified",
        help="Template for the new font name. Use $NAME$ for the original name. Default: '$NAME$ WindModified'",
    )
    parser.add_argument(
        "--force-output",
        action="store_true",
        help="Overwrite existing output file",
    )
    return parser.parse_args()


def process_font(font, args):
    if args.zhu_to_dot:
        zhu_to_dot(font)

    if args.better_chinese_dot:
        better_chinese_dot(font)

    if args.enforce_corner_brackets:
        enforce_corner_brackets(font)

    update_name_with(font, lambda name: args.font_name.replace("$NAME$", name))

    return font


def main(args):
    input_path = Path(args.font)
    if not input_path.exists():
        print(f"Input file does not exist: {args.font}")
        return

    if args.output:
        output_path = Path(args.output)
    else:
        new_name = input_path.stem + "_modified" + input_path.suffix
        output_path = input_path.with_name(new_name)

    if not args.force_output and output_path.exists():
        print(f"Output file already exists: {args.output}")
        return

    font = TTFont(input_path)
    process_font(font, args)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    font.save(str(output_path))

    print(f"Font has been updated and saved to: {args.output}")


if __name__ == "__main__":
    main(parse_args())
