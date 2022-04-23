#!/usr/bin/env python3
"""
--- Day $PUZZLE_DAY: $PUZZLE_NAME ---
https://adventofcode.com/$PUZZLE_YEAR/day/$PUZZLE_DAY
"""

import argparse
import sys


def parse_input(raw_input: str):
    """Parses Day $PUZZLE_DAY puzzle input."""
    for line in raw_input.strip().splitlines():
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day $PUZZLE_DAY: $PUZZLE_NAME")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    _ = parse_input(args.infile.read())