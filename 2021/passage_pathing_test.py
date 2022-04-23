#!/usr/bin/env python3
"""Tests for Day 12: Passage Pathing"""

import unittest

import passage_pathing


class TestCase(unittest.TestCase):

    def setUp(self):
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
        self.assertEqual(
            {
                'start': {'A', 'b'},
                'A': {'start', 'end', 'c', 'b'},
                'b': {'start', 'A', 'd', 'end'},
                'c': {'A'},
                'd': {'b'},
                'end': {'A', 'b'}
            }, passage_pathing.parse_input(self.raw_input))


if __name__ == '__main__':
    unittest.main()
