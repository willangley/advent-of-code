#!/usr/bin/env python3
"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4
"""

import argparse
import sys


def parse_input(raw_input: str):
  draws = []
  boards = []
  current_board = []

  def finish_board():
    nonlocal boards, current_board
    if len(current_board):
      boards.append(current_board)
      current_board = []

  for i, line in enumerate(raw_input.strip().splitlines()):
    if i == 0:
      draws = [int(i) for i in line.split(',')]
      continue

    if line == '':
      finish_board()
      continue

    current_board.append([int(i) for i in line.split()])
  else:
    finish_board()

  return draws, boards


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  draws, boards = parse_input(args.infile.read())
  print(draws)
  print(boards)
