#!/usr/bin/env python3
"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""

import argparse
from collections import deque
from dataclasses import dataclass
import sys
from typing import Dict, List, Set


def parse_input(raw_input: str) -> List[List[int]]:
  """Parses input into a heightmap."""
  return [[int(c) for c in line.strip()] for line in
          raw_input.strip().splitlines()]


@dataclass(frozen=True)
class Point:
  i: int
  j: int


def get_neighbors(heightmap: List[List[int]], point: Point) -> List[Point]:
  neighbors = []
  if point.i - 1 >= 0:
    neighbors.append(Point(point.i - 1, point.j))
  if point.i + 1 < len(heightmap):
    neighbors.append(Point(point.i + 1, point.j))
  if point.j - 1 >= 0:
    neighbors.append(Point(point.i, point.j - 1))
  if point.j + 1 < len(heightmap[0]):
    neighbors.append(Point(point.i, point.j + 1))
  return neighbors


def find_low_points(heightmap: List[List[int]]) -> List[Point]:
  low_points = []
  for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
      cur = Point(i, j)
      neighbor_heights = [heightmap[n.i][n.j] for n in
                          get_neighbors(heightmap, cur)]
      if heightmap[i][j] < min(neighbor_heights):
        low_points.append(cur)
  return low_points


def find_risk_level(heightmap: List[List[int]], points: List[Point]) -> int:
  return sum(1 + heightmap[p.i][p.j] for p in points)


def find_basins(heightmap: List[List[int]]) -> Dict[Point, Set[Point]]:
  basins = {lp: set() for lp in find_low_points(heightmap)}
  for low_point in basins.keys():
    queue = deque([low_point])
    while len(queue):
      cur = queue.popleft()
      neighbors = {n for n in get_neighbors(heightmap, cur) if
                   heightmap[n.i][n.j] < 9 and n not in basins[low_point]}
      queue.extend(neighbors)
      basins[low_point] |= neighbors
  return basins


def largest_basins(heightmap: List[List[int]]) -> int:
  basins = find_basins(heightmap)
  product = 1
  for size in sorted(
      [len(basin) for basin in basins.values()], reverse=True)[:3]:
    product *= size
  return product


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 9: Smoke Basin")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  heightmap = parse_input(args.infile.read())
  print('[Part 1] risk level:',
        find_risk_level(heightmap, find_low_points(heightmap)))
  print('[Part 2] three largest basins:', largest_basins(heightmap))