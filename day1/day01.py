#! /usr/bin/env python3
# https://adventofcode.com/2021/day/1
import numpy as np

with open("../data/data_01.txt", mode="r") as data:
    digits = list(map(int, data.readlines()))
ans_raw: np.ndarray = np.subtract(np.array(digits[1:]), np.array(digits[:-1]))
print(sum(ans_raw > 0))

sumarr: np.ndarray = (
    np.array(digits[:-2]) + np.array(digits[1:-1]) + np.array(digits[2:])
)
print(sum((sumarr[1:] - sumarr[:-1]) > 0))
