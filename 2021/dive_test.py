#!/usr/bin/env python3
"""Tests for Day 2: Dive!"""

import unittest

import dive
from dive import Direction


class DiveTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_course = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    self.course = dive.parse_course(self.raw_course)

  def test_parse_course(self):
    self.assertListEqual(dive.parse_course(self.raw_course),
                         [(Direction.FORWARD, 5), (Direction.DOWN, 5),
                          (Direction.FORWARD, 8), (Direction.UP, 3),
                          (Direction.DOWN, 8), (Direction.FORWARD, 2)])

  def test_calculate_position_part1(self):
    self.assertEqual(
      dive.calculate_position(self.course, dive.Part1Submarine()), 150)

  def test_calculate_position_part2(self):
    self.assertEqual(
      dive.calculate_position(self.course, dive.Part2Submarine()), 900)

if __name__ == '__main__':
  unittest.main()
