#! /usr/bin/env python3
# https://adventofcode.com/2021/day/5
from dataclasses import dataclass
from collections import Counter
from itertools import compress, count
from os import pipe


@dataclass(frozen=True)
class Point:
    x: int
    y: int


with open("data/data_05.txt", "r") as raw:
    raw_data: list[str] = raw.read().splitlines()
    data = [
        (list(map(int, a.split(","))), list(map(int, b.split(","))))
        for a, b in [line.split(" -> ") for line in raw_data]
    ]
    point_data = [[Point(*datum[0]), Point(*datum[1])] for datum in data]


def is_vertical_horizontal(point_a: Point, point_b: Point) -> bool:
    # check points are horizontal or vertical
    return point_a.x == point_b.x or point_a.y == point_b.y


def draw_vert_hori_line(point_a: Point, point_b: Point) -> list[Point]:
    if point_a.x == point_b.x:
        if point_a.y > point_b.y:
            passing_point = [
                Point(x=point_a.x, y=i) for i in range(point_b.y, point_a.y + 1)
            ]
        else:
            passing_point = [
                Point(x=point_a.x, y=i) for i in range(point_a.y, point_b.y + 1)
            ]

    if point_a.y == point_b.y:
        if point_a.x > point_b.x:
            passing_point = [
                Point(x=i, y=point_a.y) for i in range(point_b.x, point_a.x + 1)
            ]
        else:
            passing_point = [
                Point(x=i, y=point_a.y) for i in range(point_a.x, point_b.x + 1)
            ]
    return passing_point


def count_over_lap(points: list[Point]) -> int:
    c_f = Counter(points)
    overlap = 0
    print(c_f)
    for value in c_f.values():
        if value > 1:
            overlap += 1
    return overlap


hv_line_jud = list(map(lambda x: is_vertical_horizontal(*x), point_data))
hv_line = list(compress(point_data, hv_line_jud))

Q1_pass: list[Point] = []
for point_pairs in hv_line:
    pa, pb = point_pairs
    points = draw_vert_hori_line(pa, pb)
    Q1_pass.extend(points)

print(f"Q1 ans is {count_over_lap(Q1_pass)}")

# Q2
def is_45_degree(point_a: Point, point_b: Point) -> bool:
    return (abs(point_a.x - point_b.x) - abs(point_a.y - point_b.y)) == 0


def draw_45_line(point_a: Point, point_b: Point) -> list[Point]:
    if point_a.x > point_b.x:
        linex = [i for i in range(point_a.x, point_b.x - 1, -1)]
    else:
        linex = [i for i in range(point_a.x, point_b.x + 1)]
    if point_a.y > point_b.y:
        liney = [i for i in range(point_a.y, point_b.y - 1, -1)]
    else:
        liney = [i for i in range(point_a.y, point_b.y + 1)]
    return [Point(x=i, y=j) for i, j in zip(linex, liney)]


fortyfive_jud = list(map(lambda x: is_45_degree(*x), point_data))
fortyfive_line = list(compress(point_data, fortyfive_jud))

Q2_pass: list[Point] = []
for point_pairs in hv_line:
    pa, pb = point_pairs
    points = draw_vert_hori_line(pa, pb)
    print(points)
    Q2_pass.extend(points)

for point_pairs in fortyfive_line:
    pa, pb = point_pairs
    points = draw_45_line(pa, pb)
    print(points)
    Q2_pass.extend(points)

print(f"Q2 ans is {count_over_lap(Q2_pass)}")
