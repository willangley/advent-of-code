#!/usr/bin/env python3
"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""

import argparse
import sys


def parse_input(raw_input: str):
  for line in raw_input.strip().splitlines():
    pass


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 8: Seven Segment Search")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  _ = parse_input(args.infile.read())
