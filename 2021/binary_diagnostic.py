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

  def mask(self, bit: int):
    return 1 << (self.bits - bit)

  def count_bits_at(self, bit: int):
    count = 0
    for number in self.numbers:
      if number & self.mask(bit):
        count += 1
    return count


def gamma(diagnostic: Diagnostic) -> int:
  raw_gamma = 0
  for bit in range(1, diagnostic.bits + 1):
    count = diagnostic.count_bits_at(bit)
    if count > len(diagnostic.numbers) / 2:
      raw_gamma += diagnostic.mask(bit)
  return raw_gamma


def epsilon(diagnostic: Diagnostic) -> int:
  # Negative numbers have an infinite number of leading 1s, so we mask them away
  # after NOT. Ref: https://wiki.python.org/moin/BitwiseOperators
  return ~gamma(diagnostic) & (1 << diagnostic.bits) - 1


def power_consumption(diagnostic: Diagnostic) -> int:
  """Determines power consumption of a submarine from a Diagnostic.

  First half of Day 3.

  :param diagnostic: a diagnostic
  :return: power consumption"""
  return gamma(diagnostic) * epsilon(diagnostic)


def oxygen_generator_rating(diagnostic: Diagnostic) -> int:
  for bit in range(1, diagnostic.bits + 1):
    count = diagnostic.count_bits_at(bit)
    mask = diagnostic.mask(bit)
    most_common_bit = mask if count >= len(diagnostic.numbers) / 2 else 0
    diagnostic = Diagnostic([number for number in diagnostic.numbers
                             if number & mask == most_common_bit],
                            diagnostic.bits)
    if len(diagnostic.numbers) == 1:
      break

  return diagnostic.numbers[0]


def co2_scrubber_rating(diagnostic: Diagnostic) -> int:
  for bit in range(1, diagnostic.bits + 1):
    count = diagnostic.count_bits_at(bit)
    mask = diagnostic.mask(bit)
    least_common_bit = mask if count < len(diagnostic.numbers) / 2 else 0
    diagnostic = Diagnostic([number for number in diagnostic.numbers
                             if number & mask == least_common_bit],
                            diagnostic.bits)
    if len(diagnostic.numbers) == 1:
      break

  return diagnostic.numbers[0]


def life_support_rating(diagnostic: Diagnostic) -> int:
  """Determines life support rating of a submarine from a Diagnostic.

  Second half of Day 3.

  :param diagnostic: a diagnostic
  :return: power consumption"""
  return oxygen_generator_rating(diagnostic) * co2_scrubber_rating(diagnostic)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  diagnostic = Diagnostic.parse(args.infile.read())
  print('[Part 1] power consumption:', power_consumption(diagnostic))
  print('[Part 2] life support rating:', life_support_rating(diagnostic))
