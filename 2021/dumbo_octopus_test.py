#!/usr/bin/env python3
"""Tests for Day 11: Dumbo Octopus"""

import unittest

import dumbo_octopus


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
"""

  def test_parse_input(self):
    self.assertListEqual([], dumbo_octopus.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
