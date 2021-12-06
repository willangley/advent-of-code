#!/usr/bin/env python3
"""Tests for Day 6: Lanternfish"""

import unittest

import lanternfish


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], lanternfish.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
