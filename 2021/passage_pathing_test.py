#!/usr/bin/env python3
"""Tests for Day 12: Passage Pathing"""

import unittest

import passage_pathing


class TestCase(unittest.TestCase):

    def setUp(self):
        """Make input available to test cases.

        `raw_input` should be set to the text input for the day, usually near
        the top of the puzzle."""
        self.raw_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

    def test_parse_input(self):
        """Test input parsing."""
        self.assertEqual(
            {
                'start': {'A', 'b'},
                'A': {'start', 'end', 'c', 'b'},
                'b': {'start', 'A', 'd', 'end'},
                'c': {'A'},
                'd': {'b'},
                'end': {'A', 'b'}
            }, passage_pathing.parse_input(self.raw_input))

    def test_part_one(self):
        """Test Part One of the puzzle."""

    def test_part_two(self):
        """Test Part Two of the puzzle."""


if __name__ == '__main__':
    unittest.main()