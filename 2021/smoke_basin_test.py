#!/usr/bin/env python3
"""Tests for Day 9: Smoke Basin"""

import unittest

import smoke_basin


class SmokeBasinTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], smoke_basin.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
