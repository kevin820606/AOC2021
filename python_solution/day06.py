#! /usr/bin/env python3
from collections import Counter


# Fish birth day counters
def fishes_reproduct(days: int, data=list[int]):
    fishes: Counter[int] = Counter(data)
    print(f"Initial State: {fishes}")
    for _ in range(1, days + 1):
        new_fish = fishes[0]
        fishes[0] = fishes[1]
        fishes[1] = fishes[2]
        fishes[2] = fishes[3]
        fishes[3] = fishes[4]
        fishes[4] = fishes[5]
        fishes[5] = fishes[6]
        fishes[6] = fishes[7]
        fishes[7] = fishes[8]
        fishes[8] = new_fish
        fishes[6] += new_fish

    print(sum(fishes.values()))


if __name__ == "__main__":
    with open("data/data_06.txt", mode="r") as raw:
        data = list(map(int, raw.read().split(",")))
    # Q1
    fishes_reproduct(80, data)
    # Q2
    fishes_reproduct(256, data)
