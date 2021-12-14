#! /usr/bin/env python3
# https://adventofcode.com/2021/day/13

from util import read
import numpy as np

raw_data = read(13)


def clean_data(
    data: list[str],
) -> tuple[tuple[np.ndarray, np.ndarray], list[tuple[int, int]], tuple[int, int]]:
    xarr = []
    yarr = []
    action = []
    max_x = 0
    max_y = 0
    for line in data:
        if "," in line:
            a, b = line.split(",")
            inta, intb = int(a), int(b)
            max_x = intb if intb > max_x else max_x
            max_y = inta if inta > max_y else max_y
            xarr.append(intb)
            yarr.append(inta)
            continue

        if "x" in line:
            _, number = line.split("=")
            action.append((0, int(number)))
            continue

        if "y" in line:
            _, number = line.split("=")
            action.append((int(number), 0))
            continue
    return ((np.array(xarr), np.array(yarr)), action, (max_x + 1, max_y + 1))


def folding_mat(
    data_point: tuple[np.ndarray, np.ndarray],
    action: list[tuple[int, int]],
    max_point: tuple[int, int],
    folder: int = None,
) -> tuple[np.matrix, int]:
    if folder is None:
        folder = len(action)
    mat = np.zeros(shape=max_point)
    mat[data_point] = 1
    xarr, yarr = data_point
    action = action[0:folder]
    actionx, actiony = max_point

    for x, y in action:
        if x == 0:
            actiony = y
            dy = yarr[yarr > y] - y
            yarr[yarr > y] = y - dy
        if y == 0:
            actionx = x
            dx = xarr[xarr > x] - x
            xarr[xarr > x] = x - dx
    mat[(xarr, yarr)] = 1
    newmat: np.matrix = mat[0:actionx, 0:actiony]
    return newmat, newmat.sum()


data_point, action, max_point = clean_data(raw_data)
print(folding_mat(data_point=data_point, action=action, max_point=max_point, folder=1))


# Q2 read matrix by human
q2mat, count_point = folding_mat(
    data_point=data_point, action=action, max_point=max_point
)
np.savetxt("d13q2.txt", q2mat, fmt="%d")
