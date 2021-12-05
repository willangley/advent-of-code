#!/usr/bin/env python3
"""Tests for Day 5: Hydrothermal Venture"""

import unittest

import hydrothermal_venture
from hydrothermal_venture import Line, Part, Point


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
    self.lines = hydrothermal_venture.parse_input(self.raw_input)

  def test_parse_line(self):
    self.assertEqual(Line(0, 9, 5, 9),
                     hydrothermal_venture.parse_line("0,9 -> 5,9"))

  def test_parse_input(self):
    self.assertListEqual([Line(0, 9, 5, 9),
                          Line(8, 0, 0, 8),
                          Line(9, 4, 3, 4),
                          Line(2, 2, 2, 1),
                          Line(7, 0, 7, 4),
                          Line(6, 4, 2, 0),
                          Line(0, 9, 2, 9),
                          Line(3, 4, 1, 4),
                          Line(0, 0, 8, 8),
                          Line(5, 5, 8, 2)],
                         self.lines)

  def test_points(self):
    self.assertListEqual([Point(1, 1), Point(1, 2), Point(1, 3)],
                         hydrothermal_venture.points(Line(1, 1, 1, 3)))
    self.assertListEqual([Point(9, 7), Point(8, 7), Point(7, 7)],
                         hydrothermal_venture.points(Line(9, 7, 7, 7)))
    self.assertListEqual([Point(1, 1), Point(2, 2), Point(3, 3)],
                         hydrothermal_venture.points(
                             hydrothermal_venture.parse_line("1,1 -> 3,3")))
    self.assertListEqual([Point(9, 7), Point(8, 8), Point(7, 9)],
                         hydrothermal_venture.points(
                             hydrothermal_venture.parse_line("9,7 -> 7,9")))

  def test_print_diagram_part_one(self):
    self.assertEqual("""
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
""".strip(), hydrothermal_venture.print_diagram(
        hydrothermal_venture.draw_diagram(self.lines)))

  def test_score_diagram_part_one(self):
    self.assertEqual(5, hydrothermal_venture.score_diagram(
        hydrothermal_venture.draw_diagram(self.lines)))

  def test_print_diagram_part_two(self):
    self.assertEqual("""
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
""".strip(), hydrothermal_venture.print_diagram(
        hydrothermal_venture.draw_diagram(self.lines, part=Part.TWO)))

  def test_score_diagram_part_two(self):
    self.assertEqual(12, hydrothermal_venture.score_diagram(
        hydrothermal_venture.draw_diagram(self.lines, part=Part.TWO)))


if __name__ == '__main__':
  unittest.main()
