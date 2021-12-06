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


def flatten_school(school: List[int]) -> List[int]:
  flat_school = [0 for _ in range(9)]
  for fish in school:
    flat_school[fish] += 1
  return flat_school


def fast_simulate_day(flat_school: List[int]) -> List[int]:
  spawning = flat_school[0]
  flat_school[:8], flat_school[8] = flat_school[1:], spawning
  flat_school[6] += spawning
  return flat_school


def fast_simulate(school: List[int], days: int) -> int:
  flat_school = flatten_school(school)
  for day in range(1, days + 1):
    flat_school = fast_simulate_day(flat_school)
  return sum(flat_school)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 6: Lanternfish")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  school = parse_input(args.infile.read())
  print('[Part 1] fish', simulate(school, 80))
  print('[Part 2] fish', fast_simulate(school, 256))