#!/usr/bin/env python3
"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

import argparse
import sys
from typing import Callable, List


class Diagnostic:
  """A diagnostic report.

  The diagnostic report (your puzzle input) consists of a list of binary
  numbers.
  """

  def __init__(self, numbers: List[int], bits: int):
    self.numbers = numbers
    self.bits = bits

  @staticmethod
  def parse(raw_diagnostic: str):
    """Parses a diagnostic report from puzzle input."""
    numbers: List[int] = []
    bits: int = 0

    for line in raw_diagnostic.strip().splitlines():
      numbers.append(int(line, base=2))
      bits = len(line.strip())

    return Diagnostic(numbers, bits)

  def mask(self, bit: int):
    """Computes a mask for the bit_th bit of the diagnostic report.

    Following the puzzle, the "first" bit is the most significant bit.
    """
    return 1 << (self.bits - bit)

  def count_bits_at(self, bit: int):
    """Counts the number of bit_th bits set in the diagnostic report.

    This is essentially a transposed population count. Following the puzzle,
    the "first" bit is the most significant bit.
    """
    count = 0
    for number in self.numbers:
      if number & self.mask(bit):
        count += 1
    return count


def gamma(diagnostic: Diagnostic) -> int:
  """Computes gamma rate.

  Each bit in the gamma rate can be determined by finding the most common bit in
  the corresponding position of all numbers in the diagnostic report.
  """
  raw_gamma = 0
  for bit in range(1, diagnostic.bits + 1):
    count = diagnostic.count_bits_at(bit)
    if count > len(diagnostic.numbers) / 2:
      raw_gamma += diagnostic.mask(bit)
  return raw_gamma


def epsilon(diagnostic: Diagnostic) -> int:
  """Computes epsilon rate.

  The epsilon rate is calculated in a similar way [to :func:`gamma`]; rather
  than use the most common bit, the least common bit from each position is used.
  """
  # Negative numbers have an infinite number of leading 1s, so we mask them away
  # after NOT. Ref: https://wiki.python.org/moin/BitwiseOperators
  return ~gamma(diagnostic) & (1 << diagnostic.bits) - 1


def power_consumption(diagnostic: Diagnostic) -> int:
  """Determines power consumption of a submarine from a Diagnostic.

  Power consumption is found by multiplying the gamma rate by the epsilon rate,
  by definition. First half of Day 3.
  """
  return gamma(diagnostic) * epsilon(diagnostic)


def search(
    diagnostic: Diagnostic,
    bit_criteria: Callable[[Diagnostic, int], bool]) -> int:
  """Searches bit-by-bit for a rating in a diagnostic report.

  Each bit of each value is checked against `bit_criteria` and only values that
  pass the criteria are kept.

  :param diagnostic: the diagnostic
  :param bit_criteria: function that computes a criterion for a bit
  :return: the value, when only one is left
  """
  for bit in range(1, diagnostic.bits + 1):
    mask = diagnostic.mask(bit)
    search_bit = mask if bit_criteria(diagnostic, bit) else 0
    diagnostic = Diagnostic([number for number in diagnostic.numbers
                             if number & mask == search_bit],
                            diagnostic.bits)
    if len(diagnostic.numbers) == 1:
      break
  return diagnostic.numbers[0]


def oxygen_generator_rating(diagnostic: Diagnostic) -> int:
  """Determines oxygen rating.

  The oxygen generator rating is given by numbers that match the *most common*
  bit in the Diagnostic bit-for-bit for all leading positions.
  """

  def most_common_bit(diagnostic: Diagnostic, bit: int) -> bool:
    return diagnostic.count_bits_at(bit) >= len(diagnostic.numbers) / 2

  return search(diagnostic, most_common_bit)


def co2_scrubber_rating(diagnostic: Diagnostic) -> int:
  """Determines CO2 scrubber rating.

  The CO2 scrubber rating is given by numbers that match the *least common*
  bit in the Diagnostic bit-for-bit for all leading positions.
  """

  def least_common_bit(diagnostic: Diagnostic, bit: int) -> bool:
    return diagnostic.count_bits_at(bit) < len(diagnostic.numbers) / 2

  return search(diagnostic, least_common_bit)


def life_support_rating(diagnostic: Diagnostic) -> int:
  """Determines life support rating of a submarine from a Diagnostic.

  The life support rating is determined by multiplying the oxygen generator
  rating by the CO2 scrubber rating. Second half of Day 3.
  """
  return oxygen_generator_rating(diagnostic) * co2_scrubber_rating(diagnostic)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 3: Binary Diagnostic")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  diagnostic = Diagnostic.parse(args.infile.read())
  print('[Part 1] power consumption:', power_consumption(diagnostic))
  print('[Part 2] life support rating:', life_support_rating(diagnostic))
