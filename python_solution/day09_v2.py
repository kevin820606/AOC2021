#! /usr/bin/env python3

# Not Exactly solve by myself, and I have take a look how other manage this problem
import numpy as np
from util import read

raw_data = read(9, example=False)
mat: np.matrix = np.matrix([[int(word) for word in line] for line in raw_data])
logic = (mat - 9) < 0
mat_x, mat_y = mat.shape
zero_mat = np.zeros(shape=(mat_x, mat_y))
basin_num = 1


def search(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # four dimension
    inputlen = len(points)
    for x, y in points:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            findpoint = (x + dx, y + dy)
            if 0 <= findpoint[0] < mat_x and 0 <= findpoint[1] < mat_y:
                if logic[x + dx, y + dy] and findpoint not in points:
                    points.append(findpoint)

    if inputlen == len(points):
        return points
    else:
        points = search(points=points)
        return points


for x in range(mat_x):
    for y in range(mat_y):
        if not logic[x, y]:
            basin_num += 1
            continue
        get_connect_point = search([(x, y)])
        for i, j in get_connect_point:
            zero_mat[i, j] = basin_num

from collections import Counter
from functools import reduce

a = reduce(lambda x, y: x + Counter(y), zero_mat, Counter())
ans = 1
print(a)
a.pop(0)
for k, v in a.most_common(3):
    ans = ans * v
print(ans)
