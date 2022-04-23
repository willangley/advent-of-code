#!/usr/bin/env python3
"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""

import argparse
import sys
from typing import Callable


import networkx as nx


def parse_input(raw_input: str) -> nx.DiGraph:
    """Parses Day 12 puzzle input."""
    graph = nx.DiGraph()
    graph.add_nodes_from(['start', 'end'])

    for line in raw_input.strip().splitlines():
        edge = line.split('-')
        for candidate in [edge, list(reversed(edge))]:
            if candidate[0] == 'end':
                continue
            if candidate[1] == 'start':
                continue
            graph.add_edge(*candidate)

    return graph


CanVisit = Callable[[list[str], str], bool]


def dfs_impl(graph: nx.DiGraph, u: str, path: list[str], can_visit: CanVisit):
    if u == 'end':
        yield path

    for v in graph[u]:
        if can_visit(path, v):
            path.append(v)
            yield from dfs_impl(graph, v, path, can_visit)
            path.pop()


def dfs(graph: nx.DiGraph, can_visit: CanVisit):
    start = 'start'
    return [list(path) for path in dfs_impl(graph, start, [start], can_visit)]


def part_one(graph: nx.DiGraph):
    def can_visit(path: list[str], node: str) -> bool:
        return node not in path or not node.islower()
    return len(dfs(graph, can_visit))


def part_two(graph: nx.DiGraph):
    def can_visit(path: list[str], node: str) -> bool:
        if not node.islower():
            return True
        if node not in path:
            return True

        small_caves = [p for p in path if p.islower()]
        return len(small_caves) == len(set(small_caves))

    return len(dfs(graph, can_visit))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 12: Passage Pathing")
    parser.add_argument('infile',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    graph = parse_input(args.infile.read())
    print('Part one: ', part_one(graph))
    print('Part two: ', part_two(graph))
