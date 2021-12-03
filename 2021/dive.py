#!/usr/bin/env python3
"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

import argparse
from enum import Enum
import sys
from typing import NamedTuple

class Direction(Enum):
  FORWARD = 1  # increases the horizontal position by `X` units
  DOWN = 2  # *increases* the depth by `X` units
  UP = 3  # *decreases* the depth by `X` units


class Step(NamedTuple):
  direction: Direction
  distance: int


def parse_course(raw_course):
  """Parses a planned course (the puzzle input.)"""
  course = []
  raw_direction: str
  raw_distance: str

  for line in raw_course.strip().splitlines():
    raw_direction, raw_distance = line.split()
    course.append(
        Step(Direction.__members__[raw_direction.upper()], int(raw_distance)))
  return course


def calculate_position(course):
  """Calculates a (horizontal, depth) position given a course."""
  horizontal: int = 0
  depth: int = 0

  for step in course:
    if step.direction == Direction.FORWARD:
      horizontal += step.distance
    elif step.direction == Direction.DOWN:
      depth += step.distance
    elif step.direction == Direction.UP:
      depth -= step.distance

  return (horizontal, depth)


def multiply_position_depth(position):
  return position[0] * position[1]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  course = parse_course(args.infile.read())
  position = calculate_position(course)
  print('horizontal position * depth =', multiply_position_depth(position))
