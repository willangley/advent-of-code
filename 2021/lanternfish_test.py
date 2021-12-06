#!/usr/bin/env python3
"""Tests for Day 6: Lanternfish"""

import unittest

import lanternfish


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = "3,4,3,1,2"

  def test_parse_input(self):
    self.assertListEqual([3, 4, 3, 1, 2],
                         lanternfish.parse_input(self.raw_input))

  def test_simulate_day(self):
    self.assertListEqual([2, 3, 2, 0, 1],
                         lanternfish.simulate_day([3, 4, 3, 1, 2]))
    self.assertListEqual([1, 2, 1, 6, 0, 8],
                         lanternfish.simulate_day([2, 3, 2, 0, 1]))

  def test_simulate(self):
    self.assertEqual(26,
                     lanternfish.simulate(lanternfish.parse_input("3,4,3,1,2"),
                                          18))
    self.assertEqual(5934,
                     lanternfish.simulate(lanternfish.parse_input("3,4,3,1,2"),
                                          80))

if __name__ == '__main__':
  unittest.main()
