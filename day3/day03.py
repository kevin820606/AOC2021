#! /usr/bin/env python3
# https://adventofcode.com/2021/day/3
import numpy as np

with open("data/data_03.txt", mode="r") as data:
    raw_data = data.read().splitlines()
    raw_matrix = list(map(lambda x: [int(i) for i in x], raw_data))
    mat: np.matrix = np.matrix(raw_matrix)

# Q1
# Gamma Rate
gamma_rate_judgement = (
    np.asarray(np.sum(mat, axis=0) > (len(raw_data) / 2)).reshape(-1).astype(int)
)
gamma_rate = int("".join(map(str, (gamma_rate_judgement).astype(int))), 2)
# Epsilon Rate
epsilon_rate_judgement = gamma_rate_judgement ^ True
epsilon_rate = int("".join(map(str, (epsilon_rate_judgement).astype(int))), 2)
# Answer
gamma_rate * epsilon_rate

# Q2
from scipy import stats

OGR_mat = mat.copy()
for i in range(0, 12):
    mode, _ = stats.mode(OGR_mat[:, i])
    row, _ = np.where(OGR_mat[:, i] == mode)
    print(i, mode)
    OGR_mat = OGR_mat[row]
OGRate = int("".join(map(str, OGR_mat.tolist()[0])), 2)
print(OGRate)

CSR_mat = mat.copy()
for i in range(0, 12):
    mode_old, _ = stats.mode(CSR_mat[:, i])
    mode = 1 - mode_old
    row, _ = np.where(CSR_mat[:, i] == mode)
    if row.size == 0:
        print(CSR_mat)
        break
    print(i, mode_old, mode)
    CSR_mat = CSR_mat[row]
CSRate = int("".join(map(str, CSR_mat.tolist()[0])), 2)
print(CSRate)
print(OGRate * CSRate)
