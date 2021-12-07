#!/usr/bin/env python3
"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""

import argparse
import sys
from typing import List


def parse_input(raw_input: str) -> List[int]:
  return [int(i) for i in raw_input.strip().split(',')]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 7: The Treachery of Whales")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  _ = parse_input(args.infile.read())
