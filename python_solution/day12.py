#! /usr/bin/env python3
# https://adventofcode.com/2021/day/12
from __future__ import annotations
from util import read
from dataclasses import dataclass, field

raw_data = read(12, True)


@dataclass
class node:
    node_name: str
    connect_to: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.is_smallpoint: bool = True if self.node_name.islower() else False

    def set_connection(self, connection: list[str]):
        self.connect_to = connection


NODES = dict[str, node]


def parse_data(lines: list[str]) -> NODES:
    init_dict: dict[str, list[str]] = diSct()
    for line in lines:
        point_a, point_b = line.split("-", maxsplit=2)
        init_dict.setdefault(point_a, []).append(point_b)
        init_dict.setdefault(point_b, []).append(point_a)
    node_dict: dict[str, node] = dict()
    for name in init_dict.keys():
        node_dict.setdefault(name, node(name)).set_connection(init_dict[name])
    return node_dict


NODE_DICT = parse_data(raw_data)


@dataclass
class way:
    come_from: list[str]

    def get_next_node(self) -> list[way]:
        next_way: list[way] = []
        now_point_name = self.come_from[-1]
        if now_point_name == "end":
            return [way(self.come_from)]
        now_point = node(now_point_name)
        for next in now_point.connect_to:
            next_point = NODE_DICT[next]
            if next_point.is_smallpoint and next_point in self.come_from:
                continue
            next_way.append(way(self.come_from + [next_point]))
        return next_way


def path_create(node_dict: NODES = NODE_DICT):
    full_paths: list[way] = [way("start")]
    while True:
        start = len(full_paths)
        now_way = full_paths.pop()
        full_paths.extend(now_way.get_next_node())
        if len(full_paths) == start:
            break
    return full_paths


test = path_create(node_dict=NODE_DICT)
