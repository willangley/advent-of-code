#!/usr/bin/env python3
"""Tests for Day 10: Syntax Scoring"""

import unittest

import syntax_scoring


class SyntaxScoringTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

  def test_score_file(self):
    file = syntax_scoring.parse_input(self.raw_input)
    self.assertEqual(26397, syntax_scoring.score_errors(file))

  def test_score_completions(self):
    file = syntax_scoring.parse_input(self.raw_input)
    self.assertEqual(288957, syntax_scoring.score_completions(file))

if __name__ == '__main__':
  unittest.main()
