#! /usr/bin/env python3
from pathlib import Path


def read(day: int, example: bool = False, example_number: int = 0) -> list[str]:
    filename = (
        f"{Path(__file__).parents[1]}/data/data_{day:02d}"
        + "_example" * example
        + f"_{example_number}" * (example_number > 0)
    )
    with open(file=f"{filename}.txt", mode="r") as raw:
        data = raw.read().splitlines()
    return data


if __name__ == "__main__":
    print(read(7, True))
