#! /usr/bin/env python3
# https://adventofcode.com/2021/day/2
from dataclasses import dataclass
from typing import Protocol

with open("../data/data_02.txt", mode="r") as data:
    commands = data.read().splitlines()


@dataclass
class Point:
    xaxis: int
    yaxis: int

    def ans(self):
        return self.xaxis * self.yaxis


class Move(Protocol):
    def execute(self):
        ...


@dataclass
class MoveUp:
    point: Point
    distance: int

    def execute(self):
        print(f"from {self.point} move up {self.distance}")
        self.point.yaxis -= self.distance
        print(f"It's {self.point} now.")


@dataclass
class MoveDown:
    point: Point
    distance: int

    def execute(self):
        print(f"from {self.point} move down {self.distance}")
        self.point.yaxis += self.distance
        print(f"It's {self.point} now.")


@dataclass
class MoveForward:
    point: Point
    distance: int

    def execute(self):
        print(f"from {self.point} move forward {self.distance}")
        self.point.xaxis += self.distance
        print(f"It's {self.point} now.")


class Controller:
    def __init__(self, point: Point, commands: list[str]) -> None:
        self.point = point
        self.commands = commands
        self.movement: list[Move] = []
        for command in self.commands:
            move_str, dist = command.split()
            if move_str == "up":
                self.movement.append(MoveUp(point=self.point, distance=int(dist)))
            elif move_str == "down":
                self.movement.append(MoveDown(point=self.point, distance=int(dist)))
            elif move_str == "forward":
                self.movement.append(MoveForward(point=self.point, distance=int(dist)))

    def execute(self):
        self.movement.reverse()
        while self.movement:
            self.movement.pop().execute()


if __name__ == "__main__":
    origin = Point(xaxis=0, yaxis=0)
    controller = Controller(point=origin, commands=commands)
    controller.execute()
    print(controller.point.ans())
