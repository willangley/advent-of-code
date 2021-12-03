#!/usr/bin/env python3
"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

from abc import ABC, abstractmethod
import argparse
from enum import Enum
import sys
from typing import NamedTuple

class Direction(Enum):
  FORWARD = 1  # increases the horizontal position by `X` units
  DOWN = 2  # *increases* the depth by `X` units
  UP = 3  # *decreases* the depth by `X` units


class Step(NamedTuple):
  direction: Direction
  distance: int


def parse_course(raw_course):
  """Parses a planned course (the puzzle input.)"""
  course = []
  raw_direction: str
  raw_distance: str

  for line in raw_course.strip().splitlines():
    raw_direction, raw_distance = line.split()
    course.append(
        Step(Direction.__members__[raw_direction.upper()], int(raw_distance)))
  return course


class Submarine(ABC):
  def __init__(self):
    self.horizontal: int = 0
    self.depth: int = 0

  @abstractmethod
  def move(self, step: Step):
    pass

  def position(self):
    return (self.horizontal, self.depth)


class Part1Submarine(Submarine):
  def move(self, step: Step):
    if step.direction == Direction.FORWARD:
      self.horizontal += step.distance
    elif step.direction == Direction.DOWN:
      self.depth += step.distance
    elif step.direction == Direction.UP:
      self.depth -= step.distance


class Part2Submarine(Submarine):
  def __init__(self):
    super().__init__()
    self.aim: int = 0

  def move(self, step: Step):
    if step.direction == Direction.FORWARD:
      self.horizontal += step.distance
      self.depth += self.aim * step.distance
    elif step.direction == Direction.DOWN:
      self.aim += step.distance
    elif step.direction == Direction.UP:
      self.aim -= step.distance


def calculate_position(course, submarine: Submarine):
  """Calculates a (horizontal, depth) position given a course."""
  for step in course:
    submarine.move(step)
  horizontal, depth = submarine.position()
  return horizontal * depth


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  course = parse_course(args.infile.read())
  print('[Part 1] horizontal position * depth =',
        calculate_position(course, Part1Submarine()))
  print('[Part 2] horizontal position * depth =',
        calculate_position(course, Part2Submarine()))
