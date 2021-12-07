#!/usr/bin/env python3
"""Tests for Day 7: The Treachery of Whales"""

import unittest

import the_treachery_of_whales


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = "16,1,2,0,4,2,7,1,2,14"

  def test_parse_input(self):
    self.assertListEqual([16, 1, 2, 0, 4, 2, 7, 1, 2, 14],
                         the_treachery_of_whales.parse_input(self.raw_input))


if __name__ == '__main__':
  unittest.main()
