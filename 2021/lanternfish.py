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


def simulate_day(school: List[int]) -> List[int]:
  return ([fish - 1 if fish > 0 else 6 for fish in school] +
          [8 for fish in school if fish == 0])


def simulate(school: List[int], days: int) -> int:
  """Simulates a school of fish for ``days`` and returns the number of fish."""
  for day in range(1, days + 1):
    school = simulate_day(school)
  return len(school)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 6: Lanternfish")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  school = parse_input(args.infile.read())
  print('[Part 1] fish', simulate(school, 80))
