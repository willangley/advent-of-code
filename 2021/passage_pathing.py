#!/usr/bin/env python3
"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""

import argparse
import sys
from typing import Callable, List


import networkx as nx


START = 'start'
END = 'end'
PATH = 'path'
CAN_VISIT = 'can_visit'


def parse_input(raw_input: str) -> nx.DiGraph:
    """Parses Day 12 puzzle input."""
    graph = nx.DiGraph()
    graph.add_nodes_from([START, END])

    for line in raw_input.strip().splitlines():
        edge = line.split('-')
        for candidate in [edge, list(reversed(edge))]:
            if candidate[0] == END:
                continue
            if candidate[1] == START:
                continue
            graph.add_edge(*candidate)

    return graph


def all_paths_impl(graph: nx.DiGraph, source: str, target: str):
    path = graph.graph[PATH]
    path.append(source)

    if source == target:
        yield path

    for v in graph[source]:
        if graph.graph[CAN_VISIT](path, v):
            yield from all_paths_impl(graph, v, target)

    path.pop()


def all_paths(graph: nx.DiGraph, source: str, target: str,
              can_visit: Callable[[List[str], str], bool]):
    graph.graph[PATH] = []
    graph.graph[CAN_VISIT] = can_visit
    return [list(path) for path in all_paths_impl(graph, source, target)]


def part_one(graph: nx.DiGraph):
    def can_visit(path: List[str], node: str) -> bool:
        return node not in path or not node.islower()
    return len(all_paths(graph, START, END, can_visit))


def part_two(graph: nx.DiGraph):
    def can_visit(path: List[str], node: str) -> bool:
        if not node.islower():
            return True
        if node not in path:
            return True

        small_caves = [p for p in path if p.islower()]
        return len(small_caves) == len(set(small_caves))

    return len(all_paths(graph, START, END, can_visit))


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
