#!/usr/bin/env python3
"""Tests for Day $PUZZLE_DAY: $PUZZLE_NAME"""

import unittest

import ${PUZZLE_FILENAME}


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], ${PUZZLE_FILENAME}.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
