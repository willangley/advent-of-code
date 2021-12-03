#!/usr/bin/env python3
"""Tests for Day 1: Sonar Sweep."""

import unittest

import sonar_sweep


class SonarSweepTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_report = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
    self.report = sonar_sweep.parse_report(self.raw_report)

  def test_parse_report(self):
    self.assertListEqual([199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
                         sonar_sweep.parse_report(self.raw_report))

  def test_pairwise(self):
    self.assertListEqual(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'],
                         [''.join(pair) for pair in
                          sonar_sweep.pairwise('ABCDEFG')])

  def test_count_depth_increases(self):
    self.assertEqual(7, sonar_sweep.count_depth_increases(self.report))

  def test_threewise(self):
    self.assertListEqual(['ABC', 'BCD', 'CDE', 'DEF', 'EFG'],
                         [''.join(triple) for triple in
                          sonar_sweep.threewise('ABCDEFG')])

  def test_count_depth_increases_windowed(self):
    self.assertEqual(5, sonar_sweep.count_depth_increases_windowed(self.report))


if __name__ == '__main__':
  unittest.main()
