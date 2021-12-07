#!/usr/bin/env python3
# https://adventofcode.com/2021/day/7
import numpy as np

with open("data/data_07.txt", mode="r") as raw:
    arr = np.array(list(map(int, raw.readline().split(","))))


def Q1_get_minimun(arr: np.ndarray):
    uniqarr = np.unique(arr)
    return np.abs(arr - uniqarr[:, np.newaxis]).sum(axis=1).min()


def Q2_get_minimun(arr: np.ndarray):
    # this is far more fast than np.arange(0, x + 1).sum()
    # Math is matter!
    cum_sum = lambda x: ((1 + x) * x) / 2
    vec_cum_sum = np.vectorize(cum_sum)
    uniqarr = np.arange(arr.min(), arr.max())
    dist = np.abs(arr - uniqarr[:, np.newaxis])
    ans = vec_cum_sum(dist).sum(axis=1)
    return ans.min(), np.where(ans == ans.min())


print(Q1_get_minimun(arr))
print(arr)
print(Q2_get_minimun(arr))
