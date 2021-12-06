#!/usr/bin/env python3
"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""

import argparse
import sys
from typing import List


def parse_input(raw_input: str) -> List[int]:
  return [int(i) for i in raw_input.strip().split(',')]


def flatten_school(school: List[int]) -> List[int]:
  """Flattens a school of fish into their counts.

  The problem doesn't require distinguishing lanternfish from each other. This
  makes the exponential growth involved manageable.
  """
  flat_school = [0 for _ in range(9)]
  for fish in school:
    flat_school[fish] += 1
  return flat_school


def simulate_day(school: List[int]) -> List[int]:
  """Simulates a school of fish for one day and returns the school."""
  return [*school[1:7], school[0] + school[7], school[8], school[0]]


def simulate(school: List[int], days: int) -> int:
  """Simulates a school of fish for ``days`` and returns the number of fish."""
  school = flatten_school(school)
  for day in range(1, days + 1):
    school = simulate_day(school)
  return sum(school)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 6: Lanternfish")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  school = parse_input(args.infile.read())
  print('[Part 1] fish', simulate(school, 80))
  print('[Part 2] fish', simulate(school, 256))
