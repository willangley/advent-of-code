#!/usr/bin/env python3
"""Tests for Day 8: Seven Segment Search"""

import unittest

import seven_segment_search


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], seven_segment_search.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
