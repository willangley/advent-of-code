#!/usr/bin/env python3
"""Tests for Day 5: Hydrothermal Venture"""

import unittest

import hydrothermal_venture


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

  def test_parse_line(self):
    self.assertEqual(hydrothermal_venture.Line(0, 9, 5, 9),
                     hydrothermal_venture.parse_line("0,9 -> 5,9"))

  def test_parse_input(self):
    self.assertListEqual([hydrothermal_venture.Line(0, 9, 5, 9),
                          hydrothermal_venture.Line(8, 0, 0, 8),
                          hydrothermal_venture.Line(9, 4, 3, 4),
                          hydrothermal_venture.Line(2, 2, 2, 1),
                          hydrothermal_venture.Line(7, 0, 7, 4),
                          hydrothermal_venture.Line(6, 4, 2, 0),
                          hydrothermal_venture.Line(0, 9, 2, 9),
                          hydrothermal_venture.Line(3, 4, 1, 4),
                          hydrothermal_venture.Line(0, 0, 8, 8),
                          hydrothermal_venture.Line(5, 5, 8, 2)],
                         hydrothermal_venture.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
