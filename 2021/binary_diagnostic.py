#!/usr/bin/env python3
"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

import argparse
import sys
from typing import List


class Diagnostic:
  def __init__(self):
    self.popcount: List[int] = []
    self.lines: int = 0

  def parse(self, raw_diagnostic: str):
    for line in raw_diagnostic.strip().splitlines():
      self.lines += 1

      for i, bit in enumerate(line.strip()):
        if i >= len(self.popcount):
          self.popcount.append(0)
        if bit == '1':
          self.popcount[i] += 1

  def gamma(self):
    raw_gamma = ['1' if bit > (self.lines / 2) else '0'
                 for bit in self.popcount]
    return int(''.join(raw_gamma), base=2)

  def epsilon(self):
    raw_epsilon = ['0' if bit > (self.lines / 2) else '1'
                   for bit in self.popcount]
    return int(''.join(raw_epsilon), base=2)


def power_consumption(diagnostic: Diagnostic) -> int:
  return diagnostic.gamma() * diagnostic.epsilon()


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  diagnostic = Diagnostic()
  diagnostic.parse(args.infile.read())
  print('[Part 1] power consumption:', power_consumption(diagnostic))
