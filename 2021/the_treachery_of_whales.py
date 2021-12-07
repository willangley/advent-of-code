#!/usr/bin/env python3
"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""

import argparse
from enum import Enum
import sys
from typing import List


def parse_input(raw_input: str) -> List[int]:
  return [int(i) for i in raw_input.strip().split(',')]


class Part(Enum):
  ONE = 1
  TWO = 2


def position_cost(
    crabs: List[int], position: int, part: Part = Part.ONE) -> int:
  if part == Part.ONE:
    return sum(abs(crab - position) for crab in crabs)
  else:
    return sum((abs(crab - position) * (abs(crab - position) + 1)) // 2
               for crab in crabs)


def minimize_position_cost(
    crabs: List[int], part: Part = Part.ONE, start=None, end=None) -> int:
  if start is None:
    start = 0
  if end is None:
    end = len(crabs) - 1

  if start == end:
    return position_cost(crabs, start, part)
  elif start + 1 == end:
    return min(position_cost(crabs, start, part),
               position_cost(crabs, end, part))

  center = (start + end) // 2
  if center > 0:
    left, right = center - 1, center
  else:
    left, right = center, center + 1

  left_cost = position_cost(crabs, left, part)
  right_cost = position_cost(crabs, right, part)

  return (
      minimize_position_cost(crabs, part, start, left) if left_cost < right_cost
      else minimize_position_cost(crabs, part, right, end))


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 7: The Treachery of Whales")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  crabs = parse_input(args.infile.read())
  print('[Part 1] fuel:', minimize_position_cost(crabs))
  print('[Part 2] fuel:', minimize_position_cost(crabs, part=Part.TWO))
