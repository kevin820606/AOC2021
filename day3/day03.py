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
# pure loop solution
from collections import Counter

ogclists = raw_data.copy()
csrlists = raw_data.copy()
csrnum = ""
ogcnum = ""
for i in range(0, 12):

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
    # print(f"{zeroogc=}, {oneogc=}")
    # print(f"{zerocsr=}, {onecsr=}")

    if zeroogc > oneogc:
        mode_num_ogc = "0"
    if zerocsr > onecsr:
        mode_num_csr = "1"
    ogcnum += mode_num_ogc
    csrnum += mode_num_csr

    for ogclist in ogclists:
        if ogclist[i] != mode_num_ogc:
            ogclists.remove(ogclist)

    for csrlist in csrlists:
        if csrlist[i] != mode_num_csr:
            csrlists.remove(csrlist)
# for i in list(map(lambda x: int(x, 2), ogclists)):
#     for j in list(map(lambda x: int(x, 2), csrlists)):
#          print(i * j == 4474944)
# print(int(ogcnum, 2) * int(csrnum, 2))
# print(ogclist)

print(list(map(lambda x: int(x, 2), raw_data)))
"100000000000"
numbers = list(map(lambda x: int(x, 2), raw_data))

for i in range(12, -1, -1):
    comparenumber = int("1" + i * "0", 2)
    one_chooser = [number > comparenumber for number in numbers]
    print(one_chooser)
    zero_chooser = [number < comparenumber for number in numbers]
    result = sum(one_chooser) >= sum(zero_chooser)
    if result:
        numbers = [i for (i, v) in zip(numbers, one_chooser) if v]
    else:
        numbers = [i for (i, v) in zip(numbers, zero_chooser) if v]
print(numbers)
