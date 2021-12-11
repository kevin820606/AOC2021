from typing_extensions import runtime
from util import read
import numpy as np
from pprint import pprint as print


def string_to_matrix(raw_data: list[str]) -> np.matrix:
    return np.matrix([[int(word) for word in line] for line in raw_data])


def _constrained_in_matrix(points: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    pointx, pointy = points
    return np.logical_and(
        np.logical_and(0 <= pointx, pointx <= 9),
        np.logical_and(0 <= pointy, pointy <= 9),
    )


def impact_range(
    explode_point: tuple[np.ndarray, np.ndarray]
) -> list[tuple[np.ndarray, np.ndarray]]:
    influnced_point = []
    og_x, og_y = explode_point
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            xdx = og_x + dx
            ydx = og_y + dy
            in_range = _constrained_in_matrix((xdx, ydx))
            influnced_point.append((xdx[in_range], ydx[in_range]))
    return influnced_point


def add_energy(octopus: np.matrix) -> tuple[np.matrix, int]:
    impacts = [np.where(octopus > -1)]
    flashed = np.zeros(shape=octopus.shape)
    while impacts:
        impact = impacts.pop(0)
        octopus[impact] += 1
        flash = octopus >= 10
        if np.logical_xor(flash, flashed).any():
            newspot = np.where(np.logical_xor(flash, flashed))
            impacts.extend(impact_range(newspot))
        flashed = np.logical_or(flash, flashed)
    octopus[flashed] = 0
    flashTimes = flashed.sum()
    return np.matrix(octopus), flashTimes


def Q1_multiple_impacts(times: int, octopus: np.matrix) -> int:
    totalFlash = 0
    for _ in range(times):
        octopus, flashTimes = add_energy(octopus=octopus)
        totalFlash += flashTimes
    return totalFlash


def Q2_simultaneously(octopus: np.matrix) -> int:
    run_time = 1
    while True:
        octopus, _ = add_energy(octopus=octopus)
        run_time += 1
        if octopus.sum() in range(0, 1000, 100):
            if (octopus == octopus[0, 0]).all():
                return run_time


if __name__ == "__main__":
    raw_data = read(11, False)
    octopus = string_to_matrix(raw_data=raw_data)
    print(Q1_multiple_impacts(100, octopus=octopus))
    print(Q2_simultaneously(octopus=octopus))
