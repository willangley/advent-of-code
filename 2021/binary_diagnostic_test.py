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
    self.diagnostic = binary_diagnostic.Diagnostic()
    self.diagnostic.parse(self.raw_diagnostic)

  def test_parse_diagnostic(self):
    diagnostic = binary_diagnostic.Diagnostic()
    diagnostic.parse(self.raw_diagnostic)
    self.assertEqual(diagnostic.gamma(), 22)
    self.assertEqual(diagnostic.epsilon(), 9)

  def test_power_consumption(self):
    self.assertEqual(binary_diagnostic.power_consumption(self.diagnostic), 198)


if __name__ == '__main__':
  unittest.main()
