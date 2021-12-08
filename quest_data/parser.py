#! /usr/bin/env python3
def read(day: int, example: bool = False) -> list[str]:
    filename = f"data_{day:2d}" + "_example" * example
    with open(file=f"{filename}.txt", mode="r") as raw:
        data = raw.read().splitlines()
    return data
