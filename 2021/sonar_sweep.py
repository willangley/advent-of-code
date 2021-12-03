#!/usr/bin/env python3
"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""

import argparse
import itertools
import sys
from typing import List


def parse_report(raw_report: str) -> List[int]:
  """Parses a report from a sonar sweep."""
  return [int(line) for line in raw_report.strip().splitlines()]


def pairwise(iterable):
  """`itertools.pairwise` from Python 3.10."""
  # pairwise('ABCDEFG') --> AB BC CD DE EF FG
  a, b = itertools.tee(iterable)
  next(b, None)
  return zip(a, b)


def count_depth_increases(report: List[int]) -> int:
  """Counts depth increases in a sonar sweep.

  First half of Day 1.

  :param report: Report from the sonar sweep
  :return: the number of depth increases.
  """
  return sum(j > i for i, j in pairwise(report))


def threewise(iterable):
  """like `itertools.pairwise`, but returns triples."""
  a, b, c = itertools.tee(iterable, 3)
  next(b, None)
  next(c, None)
  next(c, None)
  return zip(a, b, c)


def count_depth_increases_windowed(report: List[int]) -> int:
  """Counts depth increases in a windows of a sonar sweep.

  Second half of Day 1.

  :param report: Report from the sonar sweep
  :return: the number of depth increases.
  """
  return sum(j > i for i, j in pairwise(
      sum(window) for window in threewise(report)
  ))


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  report = parse_report(args.infile.read())
  print('Depth increases:', count_depth_increases(report))
  print('Depth increases (windowed):', count_depth_increases_windowed(report))
