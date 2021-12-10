#! /usr/bin/env python3
# https://adventofcode.com/2021/day/10
# EZ
from typing import Iterator
from util import read
from pprint import pprint as print
from functools import reduce
from collections import Counter
import re


brackets = r"\(\)|\{\}|\<\>|\[\]"
half_brackets = r"\)|\}|\]|\>"


def remove_close_item(line: str) -> str:
    while re.findall(brackets, line):
        line = re.sub(brackets, "", line)
    return line


def find_corrupted_lines(lines: list[str]) -> Iterator[str]:
    for line in lines:
        trimline = remove_close_item(line)
        if re.findall(half_brackets, trimline):
            yield trimline


def find_incomplete_lines(lines: list[str]) -> Iterator[str]:
    for line in lines:
        trimline = remove_close_item(line)
        if not re.findall(half_brackets, trimline):
            yield trimline


def Q1_Score(lines: list[str]) -> int:
    scoreboard = {")": 3, "]": 57, "}": 1197, ">": 25137}
    count: Counter[str] = Counter()
    for corrupt in find_corrupted_lines(lines):
        count += Counter(re.findall(half_brackets, corrupt)[0])
    return reduce(lambda x, y: x + (count[y] * scoreboard[y]), scoreboard.keys(), 0)


def Q2_Score(lines: list[str]) -> int:
    scoreboard = {"(": 1, "[": 2, "{": 3, "<": 4}
    scorelist: list[int] = []
    for incomplete in find_incomplete_lines(lines):
        score = 0
        for sign in incomplete[::-1]:
            score = score * 5 + scoreboard[sign]
        scorelist.append(score)
    return sorted(scorelist)[int(len(scorelist) / 2)]


if __name__ == "__main__":
    raw_data = read(10, False)
    print(Q1_Score(raw_data))
    print(Q2_Score(raw_data))
