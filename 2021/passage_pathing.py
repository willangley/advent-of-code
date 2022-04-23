#!/usr/bin/env python3
"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""

import argparse
import sys


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


def dfs_impl(graph: nx.DiGraph, u: str, path: list[str]):
    if u == 'end':
        yield path

    for v in graph[u]:
        if v not in path or not v.islower():
            path.append(v)
            yield from dfs_impl(graph, v, path)
            path.pop()


def dfs(graph: nx.DiGraph):
    start = 'start'
    return [list(path) for path in dfs_impl(graph, start, [start])]


def part_one(graph: nx.DiGraph):
    return len(dfs(graph))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 12: Passage Pathing")
    parser.add_argument('infile',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    graph = parse_input(args.infile.read())
    print('Part one: ', part_one(graph))
