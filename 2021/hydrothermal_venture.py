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


def parse_line(raw_line: str) -> Line:
  """Parses a line of input into a ``Line``."""
  line_match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", raw_line)
  return Line(*(int(i) for i in line_match.groups()))


def parse_input(raw_input: str) -> List[Line]:
  """Parses input and returns a list of lines."""
  return [parse_line(line) for line in raw_input.strip().splitlines()]


class Point(NamedTuple):
  x: int
  y: int


def points(line: Line) -> List[Point]:
  """Returns points covered by line ``line``."""
  norm_x = abs(line.x2 - line.x1)
  norm_y = abs(line.y2 - line.y1)
  if norm_x and norm_y and norm_x != norm_y:
    raise ValueError("Expected horizontal, vertical, or 45 degree diagonal "
                     "line.")

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


class Part(Enum):
  ONE = 1
  TWO = 2


Diagram = List[List[int]]


def draw_diagram(lines: List[Line], part: Part = Part.ONE) -> Diagram:
  """Draws a diagram of hydrothermal vents on the ocean floor.

  Each position in the diagram contains the number of vents detected at that
  position, following the rules for the requested ``part`` of the puzzle:

  - if ``part == Part.ONE`` (the default), only horizontal and vertical lines
    will be considered.
  - if ``part == Part.TWO``, all lines will be considered.

  :param lines: lines detected by the submarine's sensors.
  :param part: the part of the puzzle.
  :return: diagram of vents.
  """
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
  """Calculates the score for a given diagram.

  Each point in the diagram with two or more vents contributes one point to the
  score.
  """
  return sum(sum(1 for c in row if c > 1) for row in diagram)


def print_diagram(diagram: Diagram) -> str:
  """Prints the diagram, following the format used by the puzzle."""
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
