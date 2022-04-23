#!/usr/bin/env python3
"""Tests for Day 12: Passage Pathing"""

import unittest

import networkx as nx
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
                'start': {
                    'A': {},
                    'b': {}
                },
                'end': {},
                'A': {
                    'c': {},
                    'b': {},
                    'end': {}
                },
                'b': {
                    'A': {},
                    'd': {},
                    'end': {}
                },
                'c': {
                    'A': {}
                },
                'd': {
                    'b': {}
                }
            },
            nx.to_dict_of_dicts(passage_pathing.parse_input(self.raw_input)))

    def test_part_one(self):
        """Test Part One of the puzzle."""
        self.assertEqual(10, passage_pathing.part_one(
            passage_pathing.parse_input(self.raw_input)))

    def test_part_two(self):
        """Test Part Two of the puzzle."""
        self.assertEqual(36, passage_pathing.part_two(
            passage_pathing.parse_input(self.raw_input)))


if __name__ == '__main__':
    unittest.main()
