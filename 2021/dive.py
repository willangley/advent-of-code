#!/usr/bin/env python3
"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

import argparse
from enum import Enum
import sys


class Direction(Enum):
  FORWARD = 1  # increases the horizontal position by `X` units
  DOWN = 2  # *increases* the depth by `X` units
  UP = 3  # *decreases* the depth by `X` units


def parse_course(raw_course):
  """Parses a planned course (the puzzle input.)"""
  course = []
  raw_direction: str
  raw_units: str

  for line in raw_course.strip().splitlines():
    raw_direction, raw_units = line.split()
    course.append(
        (Direction.__members__[raw_direction.upper()], int(raw_units)))
  return course


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  course = parse_course(args.infile.read())
