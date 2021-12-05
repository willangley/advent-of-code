#!/usr/bin/env python3
"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""

import argparse
import re
import sys
from typing import List, NamedTuple


class Line(NamedTuple):
  x1: int
  y1: int
  x2: int
  y2: int


def parse_line(raw_line: str) -> Line:
  """Parses a line of input into a Line."""
  line_match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", raw_line)
  return Line(*(int(i) for i in line_match.groups()))


def parse_input(raw_input: str) -> List[Line]:
  """Parses input and returns a list of lines."""
  return [parse_line(line) for line in raw_input.strip().splitlines()]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 5: Hydrothermal Venture")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  lines = parse_input(args.infile.read())
  print(lines)
