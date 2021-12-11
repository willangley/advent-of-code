#!/usr/bin/env python3
"""Tests for Day 9: Smoke Basin"""

import unittest

import smoke_basin


class SmokeBasinTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

  def test_parse_input(self):
    self.assertListEqual([2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                         smoke_basin.parse_input(self.raw_input)[0])

  def test_find_low_points(self):
    Point = smoke_basin.Point
    self.assertListEqual([Point(0, 1), Point(0, 9), Point(2, 2), Point(4, 6)],
                         smoke_basin.find_low_points(
                             (smoke_basin.parse_input(self.raw_input))))

  def test_find_risk_level(self):
    heightmap = smoke_basin.parse_input(self.raw_input)
    self.assertEqual(
        15, smoke_basin.find_risk_level(heightmap,
                                        smoke_basin.find_low_points(
                                            heightmap)))


if __name__ == '__main__':
  unittest.main()
