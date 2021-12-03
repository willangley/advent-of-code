#!/usr/bin/env python3
"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

from abc import ABC, abstractmethod
import argparse
from enum import Enum
import sys
from typing import List, NamedTuple


class Direction(Enum):
  FORWARD = 1
  DOWN = 2
  UP = 3


class Step(NamedTuple):
  direction: Direction
  distance: int


def parse_course(raw_course: str) -> List[Step]:
  """Parses a planned course (the puzzle input.)"""
  course: List[Step] = []
  raw_direction: str
  raw_distance: str

  for line in raw_course.strip().splitlines():
    raw_direction, raw_distance = line.split()
    course.append(
        Step(Direction.__members__[raw_direction.upper()], int(raw_distance)))
  return course


class Submarine(ABC):
  """A submarine."""

  def __init__(self):
    self.horizontal: int = 0
    self.depth: int = 0

  @abstractmethod
  def move(self, step: Step):
    pass

  def follow(self, course: List[Step]) -> int:
    """Follows a course and returns the submarine's position.

    :param course: a course
    :return: horizontal position * depth
    """
    for step in course:
      self.move(step)
    return self.horizontal * self.depth


class Part1Submarine(Submarine):
  """Submarine interpreting a course as described in Part 1."""

  def move(self, step: Step):
    """Move a submarine by `step`.

    - `forward X` increases the horizontal position by `X` units.
    - `down X` *increases* the depth by `X` units.
    - `up X` *decreases* the depth by `X` units.
    """
    if step.direction == Direction.FORWARD:
      self.horizontal += step.distance
    elif step.direction == Direction.DOWN:
      self.depth += step.distance
    elif step.direction == Direction.UP:
      self.depth -= step.distance


class Part2Submarine(Submarine):
  """Submarine interpreting a course as described in Part 2."""

  def __init__(self):
    super().__init__()
    self.aim: int = 0

  def move(self, step: Step):
    """Move a submarine by `step`.

    - `down X` *increases* your aim by `X` units.
    - `up X` *decreases* your aim by X units.
    - `forward X` does two things:
        - It increases your horizontal position by `X` units.
        - It increases your depth by your aim *multiplied by* `X`.
    """
    if step.direction == Direction.FORWARD:
      self.horizontal += step.distance
      self.depth += self.aim * step.distance
    elif step.direction == Direction.DOWN:
      self.aim += step.distance
    elif step.direction == Direction.UP:
      self.aim -= step.distance


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  course = parse_course(args.infile.read())
  print('[Part 1] position:', Part1Submarine().follow(course))
  print('[Part 2] position:', Part2Submarine().follow(course))
