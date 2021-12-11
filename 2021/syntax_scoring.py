#!/usr/bin/env python3
"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""

import argparse
import sys
from typing import List, Tuple, Union


def parse_input(raw_input: str) -> List[str]:
  return raw_input.strip().splitlines()


pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def parse_line(line: str) -> Tuple[Union[List[str], None], Union[str, None]]:
  stack = []
  for c in line:
    if c in '([{<':
      stack.append(c)
      continue

    opening = stack.pop()
    if pairs[opening] != c:
      return None, c

  return stack, None


def first_illegal_character(line: str) -> Union[str, None]:
  return parse_line(line)[1]


def score_illegal_character(c: str) -> int:
  return {
      ')': 3,
      ']': 57,
      '}': 1197,
      '>': 25137
  }.get(c, 0)


def score_errors(file: List[str]) -> int:
  return sum(
      score_illegal_character(first_illegal_character(line)) for line in file)


def score_completion(stack: List[str]) -> int:
  point_values = {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4,
  }
  score = 0
  while stack:
    score *= 5
    score += point_values[pairs[stack.pop()]]
  return score


def score_completions(file:List[str]) -> int:
  scores = []
  for line in file:
    stack, err = parse_line(line)
    if err is not None:
      continue
    scores.append(score_completion(stack))

  scores.sort()
  return scores[len(scores)//2]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 10: Syntax Scoring")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  file = parse_input(args.infile.read())
  print('[Part 1] syntax error score:', score_errors(file))
  print('[Part 2] completion score:', score_completions(file))
