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
print(gamma_rate * epsilon_rate)

# Q2
# # pure loop solution
from collections import Counter

ogclists = raw_data.copy()
csrlists = raw_data.copy()
csrnum = ""
ogcnum = ""
for i in range(0, len(raw_matrix[0])):

    mode_ogc = Counter({"0": 0, "1": 0})
    mode_csr = Counter({"0": 0, "1": 0})
    # find mode
    for numberlist in ogclists:
        mode_ogc += Counter(numberlist[i])
    for numberlist in csrlists:
        mode_csr += Counter(numberlist[i])
    zeroogc = mode_ogc["0"]
    oneogc = mode_ogc["1"]
    zerocsr = mode_csr["0"]
    onecsr = mode_csr["1"]
    mode_num_ogc = "1"
    mode_num_csr = "0"

    if zeroogc > oneogc:
        mode_num_ogc = "0"

    if zerocsr > onecsr:
        mode_num_csr = "1"

    ogcnum += mode_num_ogc
    csrnum += mode_num_csr

    for ogclist in ogclists:
        if ogclist[i] != mode_num_ogc:
            ogclists = [ogc for ogc in ogclists if ogc != ogclist]
    for csrlist in csrlists:
        print(csrlist, i, mode_num_csr)
        if len(csrlists) == 1:
            break
        if csrlist[i] != mode_num_csr:
            csrlists = [csr for csr in csrlists if csr != csrlist]
        print(csrlists)

print(int(ogclists[0], 2) * int(csrlists[0], 2))
