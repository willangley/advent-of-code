#!/usr/bin/env python3
"""Tests for Day 3: Binary Diagnostic"""
import unittest

import binary_diagnostic


class BinaryDiagnosticTestCase(unittest.TestCase):
  def setUp(self) -> None:
    self.raw_diagnostic = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
    self.diagnostic = binary_diagnostic.Diagnostic.parse(self.raw_diagnostic)

  def test_parse_diagnostic(self):
    diagnostic = binary_diagnostic.Diagnostic.parse(self.raw_diagnostic)
    self.assertListEqual([4, 30, 22, 23, 21, 15, 7, 28, 16, 25, 2, 10],
                         diagnostic.numbers)
    self.assertEqual(5, diagnostic.bits)

  def test_power_consumption(self):
    self.assertEqual(22, binary_diagnostic.gamma(self.diagnostic))
    self.assertEqual(9, binary_diagnostic.epsilon(self.diagnostic))
    self.assertEqual(198, binary_diagnostic.power_consumption(self.diagnostic))

  def test_life_support(self):
    self.assertEqual(23,
                     binary_diagnostic.oxygen_generator_rating(self.diagnostic))
    self.assertEqual(10, binary_diagnostic.co2_scrubber_rating(self.diagnostic))
    self.assertEqual(230,
                     binary_diagnostic.life_support_rating(self.diagnostic))


if __name__ == '__main__':
  unittest.main()
