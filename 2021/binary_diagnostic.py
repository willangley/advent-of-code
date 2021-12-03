#!/usr/bin/env python3
"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

import argparse
import sys
from typing import List


class Diagnostic:
  def __init__(self, numbers: List[int], bits: int):
    self.numbers = numbers
    self.bits = bits

  @staticmethod
  def parse(raw_diagnostic: str):
    numbers: List[int] = []
    bits: int = 0

    for line in raw_diagnostic.strip().splitlines():
      numbers.append(int(line, base=2))
      bits = len(line.strip())

    return Diagnostic(numbers, bits)

  def count_bits_at(self, bit: int):
    count = 0
    mask = 1 << (self.bits - bit)
    for number in self.numbers:
      if number & mask:
        count += 1
    return count


def gamma(diagnostic: Diagnostic) -> int:
  raw_gamma = 0
  for bit in range(1, diagnostic.bits + 1):
    raw_gamma <<= 1
    count = diagnostic.count_bits_at(bit)
    if count > len(diagnostic.numbers) / 2:
      raw_gamma += 1
  return raw_gamma


def epsilon(diagnostic: Diagnostic) -> int:
  return ~gamma(diagnostic) & int('1' * diagnostic.bits, base=2)


def power_consumption(diagnostic: Diagnostic) -> int:
  """Determines power consumption of a submarine from a Diagnostic.

  First half of Day 3.

  :param diagnostic: a diagnostic
  :return: power consumption"""
  return gamma(diagnostic) * epsilon(diagnostic)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  diagnostic = Diagnostic.parse(args.infile.read())
  print('[Part 1] power consumption:', power_consumption(diagnostic))
