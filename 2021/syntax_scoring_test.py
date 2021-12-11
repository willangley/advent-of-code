#!/usr/bin/env python3
"""Tests for Day 10: Syntax Scoring"""

import unittest

import syntax_scoring


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], syntax_scoring.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
