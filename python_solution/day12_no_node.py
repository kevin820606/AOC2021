#! /usr/bin/env python3
# https://adventofcode.com/2021/day/12
from __future__ import annotations
from pprint import pprint as print
from util import read
from dataclasses import dataclass

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
    dead = []
    for start, connect_to in init_dict.items():
        if (
            start.islower()
            and not start in ["start", "end"]
            and not "end" in connect_to
            and all(list(map(lambda x: x.islower(), connect_to)))
        ):
            dead.append(start)
    init_dict["dead_end"] = dead
    return init_dict


node_dict = parse_data(raw_data)


@dataclass
class way:
    went: list[str]
    twice_small_cave: bool = False

    def __post_init__(self):
        self.is_ended = True if self.went[-1] == "end" else False

    def get_next_node_q1(self) -> list[way]:
        next_way: list[way] = []
        now_point = self.went[-1]
        if self.is_ended:
            return [way(self.went)]
        for next_point in node_dict[now_point]:
            if next_point.islower() and next_point in self.went + node_dict["dead_end"]:
                continue
            new_way = way(self.went + [next_point])
            next_way.append(new_way)
        return next_way

    def get_next_node_q2(self) -> list[way]:
        next_way: list[way] = []
        now_point = self.went[-1]
        if self.is_ended:
            return [way(self.went)]
        for next_point in node_dict[now_point]:
            twice_small_cave = self.twice_small_cave
            if next_point.islower():
                if next_point in self.went:
                    if self.twice_small_cave:
                        continue
                    twice_small_cave = True
            new_way = way(self.went + [next_point], twice_small_cave=twice_small_cave)
            next_way.append(new_way)
        return next_way


def Q1_paths():
    full_paths: list[way] = [way(["start"])]
    while True:
        start = len(full_paths)
        for now_way in full_paths:
            if now_way.is_ended:
                continue
            full_paths.remove(now_way)
            full_paths.extend(now_way.get_next_node_q1())
        if len(full_paths) == start:
            break
    return full_paths


def Q2_paths():
    full_paths: list[way] = [way(["start"])]
    while True:
        start = len(full_paths)
        for now_way in full_paths:
            if now_way.is_ended:
                continue
            full_paths.remove(now_way)
            full_paths.extend(now_way.get_next_node_q2())
        if len(full_paths) == start:
            break
    return full_paths


if __name__ == "__main__":

    # Q1_all_path = Q1_paths()
    # print(len([p for p in Q1_all_path if p.is_ended]))
    Q2_all_path = Q2_paths()
    print(len([p for p in Q2_all_path if p.is_ended]))
