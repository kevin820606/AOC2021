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
        self.small_point: bool = True if self.node_name.islower() else False

    def set_connection(self, connection: list[str]):
        self.connect_to = connection
nodes = dict[str, node]

def parse_data(lines: list[str]) -> dict[str, node]:
    init_dict: dict[str, list[str]] = dict()
    for line in lines:
        point_a, point_b = line.split("-", maxsplit=2)
        init_dict.setdefault(point_a, []).append(point_b)
        init_dict.setdefault(point_b, []).append(point_a)
    node_dict: dict[str, node] = dict()
    for name in init_dict.keys():
        node_dict.setdefault(name, node(name)).set_connection(init_dict[name])
    return node_dict


node_dict = parse_data(raw_data)


def path_create(node_dict: nodes):
    full_paths = []
    come = node_dict["start"]
    next_stop = come.connect_to
    have_been = [come.node_name]
    while next_stop:
        for stop in next_stop:
            