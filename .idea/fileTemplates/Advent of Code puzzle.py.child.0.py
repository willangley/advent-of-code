#!/usr/bin/env python3
"""Tests for Day $PUZZLE_DAY: $PUZZLE_NAME"""

import unittest

import ${PUZZLE_FILENAME}


class TestCase(unittest.TestCase):
    """Test cases for Day $PUZZLE_DAY: $PUZZLE_NAME"""

    def setUp(self):
        """Make input available to test cases.

        `raw_input` should be set to the text input for the day, usually near
        the top of the puzzle."""
        self.raw_input = """
"""

    def test_parse_input(self):
        """Test input parsing."""
        self.assertListEqual([], ${PUZZLE_FILENAME}.parse_input(self.raw_input))

    def test_part_one(self):
        """Test Part One of the puzzle."""

    def test_part_two(self):
        """Test Part Two of the puzzle."""


if __name__ == '__main__':
    unittest.main()
