#! /usr/bin/env python3
# https://adventofcode.com/2021/day/12
# Only reliable way
from typing import Iterable
from util import read

raw_data = read(12)

NODES = dict[str, list[str]]


def parse_data(lines: list[str]) -> NODES:
    init_dict: dict[str, list[str]] = dict()
    for line in lines:
        point_a, point_b = line.split("-", maxsplit=2)
        if point_b != "start":
            init_dict.setdefault(point_a, []).append(point_b)
        if point_a != "start":
            init_dict.setdefault(point_b, []).append(point_a)
    return init_dict


def make_line(node_dict: NODES, nodes: list[str], onetimer: bool) -> Iterable[str]:
    new_lines = node_dict[nodes[-1]]
    for line in new_lines:
        if line.islower() and line in nodes:
            if onetimer:
                continue
        yield line


def Q1_solution(node_dict: NODES):
    end: list[list[str]] = []
    nodes = [["start"]]
    while nodes:
        node = nodes.pop()
        for line in make_line(node_dict, nodes=node, onetimer=True):
            if line == "end":
                end.append(node + [line])
                continue
            nodes.append(node + [line])
    return end


def Q2_solution(node_dict: NODES):
    end: list[list[str]] = []
    onetime_list: list[list[str]] = []
    nodes = [["start"]]
    while nodes:
        node = nodes.pop()
        for line in make_line(node_dict, nodes=node, onetimer=False):
            if line.islower() and node.count(line) == 1:
                onetime_list.append(node + [line])
                continue
            if line == "end":
                end.append(node + [line])
                continue
            nodes.append(node + [line])

    nodes = onetime_list
    while nodes:
        node = nodes.pop()
        for line in make_line(node_dict, nodes=node, onetimer=True):
            if line == "end":
                end.append(node + [line])
                continue

            nodes.append(node + [line])
    return end


if __name__ == "__main__":
    node_dict = parse_data(raw_data)
    a = Q1_solution(node_dict=node_dict)
    b = Q2_solution(node_dict=node_dict)
    print(len(b))
