#! /usr/bin/env python3
# https://adventofcode.com/2021/day/14

# too slow for Question 2
from util import read
from collections import Counter

raw_data = read(14)


def clean_data(data: list[str]) -> tuple[str, dict[str, str]]:
    startline = data[0]
    word_map: dict[str, str] = dict()
    for line in data[2:]:
        word, mapping = line.split(" -> ")
        word_map[word] = mapping

    return startline, word_map


day14data, word_map = clean_data(raw_data)


def wordinsert(startline: str, word_map: dict[str, str] = word_map) -> str:
    newline: str = ""
    for i in range(len(startline)):
        if i + 1 == len(startline):
            break
        newline += startline[i] + word_map[startline[i] + startline[i + 1]]
    newline += startline[-1]
    return newline


def Q1_solution(times: int) -> int:
    startline = day14data
    for _ in range(times):
        startline = wordinsert(startline=startline)
    ans_counter = Counter(startline)
    _, most_number = ans_counter.most_common()[0]
    _, least_number = ans_counter.most_common()[-1]
    print(ans_counter)
    return startline, most_number - least_number


# Q1_solution(10)
print(Q1_solution(2))
