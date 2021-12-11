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


if __name__ == '__main__':
  unittest.main()
