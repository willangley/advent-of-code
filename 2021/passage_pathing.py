#!/usr/bin/env python3
"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""

import argparse
from collections import defaultdict
import sys


def parse_input(raw_input: str):
    graph = defaultdict(set)
    for line in raw_input.strip().splitlines():
        edge = line.split('-')
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 12: Passage Pathing")
    parser.add_argument('infile',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    graph = parse_input(args.infile.read())
