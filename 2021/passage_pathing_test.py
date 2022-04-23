#!/usr/bin/env python3
"""Tests for Day 12: Passage Pathing"""

import unittest

import passage_pathing


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], passage_pathing.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
