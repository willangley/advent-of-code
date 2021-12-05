#!/usr/bin/env python3
"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""

import argparse
from enum import Enum
import itertools
import re
import sys
from typing import List, NamedTuple


class Line(NamedTuple):
  x1: int
  y1: int
  x2: int
  y2: int


class Point(NamedTuple):
  x: int
  y: int


class Part(Enum):
  ONE = 1
  TWO = 2


def parse_line(raw_line: str) -> Line:
  """Parses a line of input into a Line."""
  line_match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", raw_line)
  return Line(*(int(i) for i in line_match.groups()))


def parse_input(raw_input: str) -> List[Line]:
  """Parses input and returns a list of lines."""
  return [parse_line(line) for line in raw_input.strip().splitlines()]


Diagram = List[List[int]]


def points(line: Line) -> List[Point]:
  def cmp(a, b):
    return (a > b) - (a < b)

  step_x = cmp(line.x2, line.x1)
  step_y = cmp(line.y2, line.y1)

  points: List[Point] = [Point(line.x1, line.y1)]
  while True:
    current = points[-1]
    if current.x == line.x2 and current.y == line.y2:
      break
    points.append(Point(x=current.x + step_x, y=current.y + step_y))
  return points


def draw_diagram(lines: List[Line], part: Part = Part.ONE) -> Diagram:
  if part == Part.ONE:
    lines = [line for line in lines if line.x1 == line.x2 or line.y1 == line.y2]

  max_x = max(itertools.chain(*((line.x1, line.x2) for line in lines)))
  max_y = max(itertools.chain(*((line.y1, line.y2) for line in lines)))

  diagram = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
  for line in lines:
    for point in points(line):
      diagram[point.y][point.x] += 1

  return diagram


def score_diagram(diagram: Diagram) -> int:
  return sum(sum(1 for c in row if c > 1) for row in diagram)


def print_diagram(diagram: Diagram) -> str:
  return '\n'.join(
      ''.join('.' if c == 0 else str(c) for c in row) for row in diagram)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 5: Hydrothermal Venture")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  lines = parse_input(args.infile.read())
  print('[Part 1] score:', score_diagram(draw_diagram(lines)))
  print('[Part 2] score:', score_diagram(draw_diagram(lines, part=Part.TWO)))
