#!/usr/bin/env python3
"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""

import argparse
from enum import Enum
import sys
from typing import List


class Part(Enum):
  ONE = 1


def parse_input(raw_input: str):
  return [[pattern.strip().split() for pattern in line.split('|')] for line in
          raw_input.strip().splitlines()]


def count_digits(entries: List[List[List[str]]], part: Part = Part.ONE):
  return sum(
      sum(1 for digit in display if len(digit) in {2, 3, 4, 7}) for _, display
      in entries)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 8: Seven Segment Search")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  entries = parse_input(args.infile.read())
  print('[Part 1] digits 1, 4, 7, 8 appear:', count_digits(entries))
