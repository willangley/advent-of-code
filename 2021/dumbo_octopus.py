#!/usr/bin/env python3
"""
--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11
"""

import argparse
from collections import deque
import itertools
import sys
from typing import List, Tuple


def parse_input(raw_input: str):
  return [[int(c) for c in line.strip()] for line in
          raw_input.strip().splitlines()]


def simulate_step(cur: List[List[int]]) -> Tuple[List[List[int]], int]:
  succ = [[c + 1 for c in row] for row in cur]
  firing = deque(
      sum([[(i, j) for j, energy in enumerate(row) if energy == 10] for i, row
           in enumerate(succ)], []))
  while firing:
    i, j = firing.pop()

    for ii, jj in sum(
        [[(i + r, j + c) for c in [-1, 0, 1]] for r in [-1, 0, 1]], []):
      if ii < 0 or ii >= len(succ):
        continue
      if jj < 0 or jj >= len(succ[ii]):
        continue
      if i == ii and j == jj:
        continue

      succ[ii][jj] += 1
      if succ[ii][jj] == 10:
        firing.append((ii, jj))

  flash_count = 0
  for i, row in enumerate(succ):
    for j, energy in enumerate(row):
      if energy > 9:
        succ[i][j] = 0
        flash_count += 1

  return succ, flash_count


def simulate(cur: List[List[int]], steps: int) -> int:
  """Simulates the grid in `cur` for `steps` steps and returns Σ flash_count."""
  flash_count = 0
  for _ in range(steps):
    cur, step_flash_count = simulate_step(cur)
    flash_count += step_flash_count
  return flash_count


def simulate_until_all_flash(cur: List[List[int]]) -> int:
  target = sum(sum(1 for _ in row) for row in cur)
  for step in itertools.count(1):
    cur, step_flash_count = simulate_step(cur)
    if step_flash_count == target:
      return step


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 11: Dumbo Octopus")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  start = parse_input(args.infile.read())
  print('[Part 1] flashes:', simulate(start, 100))
  print('[Part 2] steps until all flash:', simulate_until_all_flash(start))
