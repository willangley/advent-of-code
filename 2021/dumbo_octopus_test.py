#!/usr/bin/env python3
"""Tests for Day 11: Dumbo Octopus"""

import unittest

import dumbo_octopus


class TestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

  def test_parse_input(self):
    self.assertListEqual(
        [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
         [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
         [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
         [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
         [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
         [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
         [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
         [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
         [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
         [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]],
        dumbo_octopus.parse_input(self.raw_input))

  def test_simulate_step(self):
    succ, flash_count = dumbo_octopus.simulate_step([[1, 1, 1, 1, 1],
                                                     [1, 9, 9, 9, 1],
                                                     [1, 9, 1, 9, 1],
                                                     [1, 9, 9, 9, 1],
                                                     [1, 1, 1, 1, 1]])
    self.assertEqual([[3, 4, 5, 4, 3],
                      [4, 0, 0, 0, 4],
                      [5, 0, 0, 0, 5],
                      [4, 0, 0, 0, 4],
                      [3, 4, 5, 4, 3]], succ)
    self.assertEqual(9, flash_count)

  def test_simulate(self):
    start = dumbo_octopus.parse_input(self.raw_input)
    self.assertEqual(1656, dumbo_octopus.simulate(start, 100))

  def test_simulate_until_all_flash(self):
    start = dumbo_octopus.parse_input(self.raw_input)
    self.assertEqual(195, dumbo_octopus.simulate_until_all_flash(start))


if __name__ == '__main__':
  unittest.main()
