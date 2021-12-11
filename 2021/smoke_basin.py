#!/usr/bin/env python3
"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""

import argparse
import sys
from typing import List


def parse_input(raw_input: str) -> List[List[int]]:
  """Parses input into a heightmap."""
  return [[int(c) for c in line.strip()] for line in
          raw_input.strip().splitlines()]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 9: Smoke Basin")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  _ = parse_input(args.infile.read())
