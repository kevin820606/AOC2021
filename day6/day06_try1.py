#! /usr/bin/env python3
# https://adventofcode.com/2021/day/6

# this approach is far too slow to solve Q2
from dataclasses import dataclass
from typing import Iterable

with open("data/data_06_example.txt", mode="r") as raw:
    data = list(map(int, raw.read().split(",")))


@dataclass
class Lanternfish:
    timer: int = 8

    def is_giving_birth(self) -> bool:
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return True
        return False


@dataclass
class SchoolofLaternfish:
    total_days: int
    fish_list: list[Lanternfish]

    def check_fish_birth(self) -> Iterable[bool]:
        return map(lambda fish: fish.is_giving_birth(), self.fish_list)

    def fish_increase(self):
        new_fish: int = sum(self.check_fish_birth())
        [self.fish_list.append(Lanternfish()) for _ in range(new_fish)]

    def get_fish_timer(self) -> list[int]:
        return list(map(lambda fish: fish.timer, self.fish_list))

    def day_passing(self) -> None:
        # print(f"Intitial State: {self.get_fish_timer()}")
        for i in range(1, self.total_days + 1):
            self.fish_increase()
            # print(f"After  {i} day:  {self.get_fish_timer()}")

    def get_fish_numbers(self):
        return len(self.fish_list)

    def __add__(self, other):
        return self.get_fish_numbers() + other.get_fish_numbers()

    def __radd__(self, other: int):
        return other + self.get_fish_numbers()

    def __mul__(self, other: int):
        return other * self.get_fish_numbers()

    def __repr__(self):
        return f"there are {self.get_fish_numbers()} fish in this school"


def fishyquestion(days: int, data: list[int]):
    school = SchoolofLaternfish(days, list(map(Lanternfish, data)))
    print(school.get_fish_numbers())
    school.day_passing()
    print(school.get_fish_numbers())


def tryplus():
    school1 = [SchoolofLaternfish(256, [Lanternfish(1)])]
    list(map(lambda school: school.day_passing(), school1))
    print(sum(school1))


if __name__ == "__main__":
    # Q1
    # fishyquestion(80, data)
    # Q2
    # fishyquestion(256, data)
    tryplus()
