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

  def test_position_cost(self):
    crabs = the_treachery_of_whales.parse_input(self.raw_input)
    self.assertEqual(37, the_treachery_of_whales.position_cost(crabs, 2))

    self.assertEqual(41, the_treachery_of_whales.position_cost(crabs, 1))
    self.assertEqual(39, the_treachery_of_whales.position_cost(crabs, 3))
    self.assertEqual(71, the_treachery_of_whales.position_cost(crabs, 10))

  def test_minimize_position_cost(self):
    crabs = the_treachery_of_whales.parse_input(self.raw_input)
    self.assertEqual(37, the_treachery_of_whales.minimize_position_cost(crabs))

  def test_minimize_position_cost_part_two(self):
    crabs = the_treachery_of_whales.parse_input(self.raw_input)
    self.assertEqual(168, the_treachery_of_whales.minimize_position_cost(
        crabs, the_treachery_of_whales.Part.TWO))


if __name__ == '__main__':
  unittest.main()
