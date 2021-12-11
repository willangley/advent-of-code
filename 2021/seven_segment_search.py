#!/usr/bin/env python3
"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""

import argparse
import sys
from typing import List, Set


def parse_half_entry(half_entry: str):
  return [set(pattern) for pattern in half_entry.strip().split()]


def parse_input(raw_input: str):
  return [[parse_half_entry(he) for he in line.split('|')] for line in
          raw_input.strip().splitlines()]


def count_digits(entries: List[List[List[Set[str]]]]):
  return sum(
      sum(1 for digit in display if len(digit) in {2, 3, 4, 7}) for _, display
      in entries)


def find_encoding(test_signals: List[Set[str]]) -> List[Set[str]]:
  encoding = [set('') for i in range(10)]

  for ts in test_signals:
    if len(ts) == 2:
      encoding[1] = ts
    elif len(ts) == 3:
      encoding[7] = ts
    elif len(ts) == 4:
      encoding[4] = ts
    elif len(ts) == 7:
      encoding[8] = ts

  intersections = {
      (1, 2, 2, 5): 2,
      (2, 3, 3, 5): 3,
      (1, 3, 2, 5): 5,
      (2, 3, 3, 6): 0,
      (1, 3, 2, 6): 6,
      (2, 4, 3, 6): 9,
  }

  for ts in test_signals:
    index = tuple(len(ts & encoding[i]) for i in [1, 4, 7, 8])
    if index[3] in (5, 6):
      encoding[intersections[index]] = ts   # type: ignore

  return encoding


def encode(signal: List[Set[str]], encoding: List[Set[str]]) -> int:
  places = [1000, 100, 10, 1]
  output = 0
  for i, s in enumerate(signal):
    for j, enc in enumerate(encoding):
      if s == enc:
        output += j * places[i]
  return output


def sum_digits(entries: List[List[List[Set[str]]]]):
  running_sum = 0
  for test_signals, output in entries:
    encoding = find_encoding(test_signals)
    running_sum += encode(output, encoding)
  return running_sum


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 8: Seven Segment Search")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  entries = parse_input(args.infile.read())
  print('[Part 1] digits 1, 4, 7, 8 appear:', count_digits(entries))
  print('[Part 2] sum of digits:', sum_digits(entries))
