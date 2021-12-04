#!/usr/bin/env python3
"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4
"""

import argparse
from enum import Enum
import sys
from typing import List, Tuple


def parse_input(raw_input: str) -> Tuple[
  List[int], List[List[List[int]]], List[List[List[bool]]]]:
  """Parses puzzle input and returns game state.

  - ``draws`` is a list of ints, read from input.
  - ``boards`` is a list of boards, read from input. each board is a
    two-dimensional list of ints.
  - ``marks`` is a list of marks, of the same length as ``boards``. each mark is
    a two-dimensional list of booleans, initially ``False``.

  :param raw_input: a string containing the puzzle input
  :return: game state, a tuple of (draws, boards, marks)
  """
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


def play_bingo_draw(draw: int, boards: List[List[List[int]]],
    marks: List[List[List[bool]]]) -> List[int]:
  """Plays a bingo draw.

  Marks off ``draw`` on any boards it appears on, and returns a list of boards
  that won.

  :param draw: the number drawn.
  :param boards: a list of bingo boards.
  :param marks: a list of marks. must correspond one-to-one with boards.
    will be updated in-place by this method.
  :return: a (possibly empty) list of indices of boards that won this round.
  """
  winning_boards = []
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
          winning_boards.append(i)

  return winning_boards


class Goal(Enum):
  WIN_FIRST = 1
  WIN_LAST = 2


def play_bingo_game(draws: List[int], boards: List[List[List[int]]],
    marks: List[List[List[bool]]], goal: Goal = Goal.WIN_FIRST) -> int:
  """Plays a bingo game.

  :param draws: the numbers drawn, in order.
  :param boards: a list of bingo boards.
  :param marks: a list of marks. must correspond one-to-one with boards.
    will be updated in-place by this method.
  :param goal: whether to win (WIN_FIRST) or let your opponent win (WIN_LAST).
  :return: the score of the board that won first if goal is WIN_FIRST; or,
    the score of the board that won last if goal is WIN_LAST.
  """
  scores = []

  for draw in draws:
    winning_boards = play_bingo_draw(draw, boards, marks)
    if not winning_boards:
      continue

    # Some rounds may have multiple winning boards. Sorting the list of indices
    # in reverse is the simplest thing that:
    #
    # - makes it safe to pop each index individually
    # - passes automatic scoring for my full puzzle input
    #
    # I have no way of knowing if this works in general.
    for winning_board_index in sorted(winning_boards, reverse=True):
      winning_board = boards.pop(winning_board_index)
      winning_marks = marks.pop(winning_board_index)

      score = 0
      for i in range(len(winning_board)):
        for j in range(len(winning_board[i])):
          if not winning_marks[i][j]:
            score += winning_board[i][j]

      score *= draw
      if goal == Goal.WIN_FIRST:
        return score

      scores.append(score)

  return scores[-1]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Day 1: Sonar Sweep")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin)
  args = parser.parse_args()

  draws, boards, marks = parse_input(args.infile.read())
  print('[Part 1] score:', play_bingo_game(draws, boards, marks))
  print('[Part 2] score:',
        play_bingo_game(draws, boards, marks, goal=Goal.WIN_LAST))
