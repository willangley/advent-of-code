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
  marks = []

  current_board = []

  def finish_board():
    nonlocal boards, current_board, marks
    if len(current_board):
      boards.append(current_board)
      ii, jj = len(current_board), len(current_board[0])
      marks.append([[False for _ in range(jj)]
                    for _ in range(ii)])
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

  return draws, boards, marks


def play_bingo_draw(draw, boards, marks):
  for i in range(len(boards)):
    for j in range(len(boards[i])):
      for k in range(len(boards[i][j])):
        if boards[i][j][k] != draw:
          continue

        marks[i][j][k] = True

        winning_row = True
        winning_col = True
        for jj in range(len(boards[i])):
          winning_col &= marks[i][jj][k]
        for kk in range(len(boards[i][j])):
          winning_row &= marks[i][j][kk]

        if winning_row or winning_col:
          return i

  return None


def play_bingo_game(draws, boards, marks):
  score = 0
  for draw in draws:
    winning_board_index = play_bingo_draw(draw, boards, marks)
    if winning_board_index is not None:
      winning_board = boards[winning_board_index]
      winning_marks = marks[winning_board_index]

      for i in range(len(winning_board)):
        for j in range(len(winning_board[i])):
          if not winning_marks[i][j]:
            score += winning_board[i][j]

      score *= draw
      return score


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  draws, boards, marks = parse_input(args.infile.read())
  print('[Part 1] score:', play_bingo_game(draws, boards, marks))
