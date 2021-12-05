#! /usr/bin/env python3
# https://adventofcode.com/2021/day/4
from dataclasses import dataclass
import numpy as np

with open("data/data_04.txt", mode="r") as data:
    lines = data.read().splitlines()
    guessnumber = list(map(int, lines.pop(0).split(",")))
guess_boards = []
board = []
for line in lines:
    if not line:
        continue
    board.append(list(map(int, line.split())))
    if len(board) == 5:
        guess_boards.append(board)
        board = []


@dataclass
class BoardGame:
    ID: int
    boards: list[list[int]]
    Win: bool = False

    def __post_init__(self):
        self.originboard = self.boards.copy()[:5]
        for n in range(0, 5):
            vertline = []
            for line in self.boards:
                vertline.append(line[n])
            self.boards.append(vertline)

    def cal_win_score(self) -> int:
        score = 0
        for board in self.boards[:5]:
            score += sum(board)
        return score

    def guess_number(self, number: int) -> bool:
        if self.Win:
            return False
        for line in self.boards:
            try:
                line.remove(number)
                if len(line) == 0:
                    score = self.cal_win_score()
                    print(
                        f"{self.ID=} Bingo! in number {number}, unmark sum is {score} score = {number * score}\n{self.originboard}"
                    )
                    self.Win = True
                    return True
            except ValueError:
                continue
        return False


@dataclass
class BoardGame_matrix:
    ID: int
    boards: list[list[int]]
    Win: bool = False

    def __post_init__(self):
        self.boards: np.matrix = np.matrix(self.boards)

    def check_win(self) -> bool:
        for i in range(0, 5):
            if (self.boards[i] == np.array([-1, -1, -1, -1, -1])).all() | (
                self.boards[:, i] == np.array([-1, -1, -1, -1, -1]).all()
            ).all():
                return True
        return False

    def cal_win_score(self):
        return self.boards[self.boards != -1].sum()

    def guess_number(self, number: int) -> bool:
        if self.Win:
            return False
        self.boards[self.boards == number] = -1
        if self.check_win():
            score = self.cal_win_score()
            print(
                f"{self.ID=} Bingo! in number {number}, unmark sum is {score} score = {number * score}"
            )
            self.Win = True
        return False


games = [BoardGame_matrix(ID=i, boards=game) for i, game in enumerate(guess_boards)]
for number in guessnumber:
    for game in games:
        game.guess_number(number=number)
