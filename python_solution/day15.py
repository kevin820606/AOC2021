#! /usr/bin/env python3
# https://adventofcode.com/2021/day/15
# https://ithelp.ithome.com.tw/articles/10209593
from util import read
import numpy as np

raw_data = read(15, True)
day15 = np.matrix([[int(word) for word in line] for line in raw_data], dtype=int)


def find_sortest_dist(from_point: tuple[int, int], to_point: tuple[int, int]) -> int:
    pass


def q1_solution(data_points: np.matrix) -> int:
    data_points = data_points.T
    x, y = data_points.shape
    shortest_point = np.zeros(shape=data_points.shape)
    shortest_point[shortest_point == 0] = np.inf
    for i in range(x):
        for j in range(y):
            for k in range(i):
                for l in range(j):
                    


def dijkstra_algorithm(data_point: np.matrix) -> int:
    data_point = data_point.T
    data_point[0, 0] = 0
    x, y = data_point.shape
    points_num = x * y
    dist_mat = np.zeros(shape=(points_num, points_num))
    dist_mat[dist_mat == 0] = 10

    for i in range(x):
        for j in range(y):
            point = i * x + j
            dist_mat[point, point] = 0
            if j + 1 != y:
                dist_mat[point, point + 1] = data_point[i, j + 1] - data_point[i, j]
            if i + 1 != x:
                dist_mat[point, point + y] = data_point[i + 1, j] - data_point[i, j]

    dis_from_origin = dist_mat[0]
    book_for_known = np.zeros(points_num, dtype=int)
    for i in range(points_num):
        min = 10
        for j in range(points_num):
            if book_for_known[j] == 0 and dis_from_origin[j] < min:
                min = dis_from_origin[j]
                u = j
        book_for_known[u] = 1
        for v in range(points_num):
            if dist_mat[u][v] < np.inf:
                if dis_from_origin[v] > dis_from_origin[u] + dist_mat[u][v]:
                    dis_from_origin[v] = dis_from_origin[u] + dist_mat[u][v]

    return dis_from_origin


print(dijkstra_algorithm(day15))
