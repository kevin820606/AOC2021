#!/usr/bin/env python3
# https://adventofcode.com/2021/day/8
from collections import Counter

try:
    from quest_data.parser import read

    raw_data = read(8)
except ModuleNotFoundError:
    with open("quest_data/data_08.txt", mode="r") as raw:
        raw_data = raw.read().splitlines()


def parse_data(line: str) -> tuple[list[str], list[str]]:
    usp_string, output_string = [string_list for string_list in line.split(" | ")]
    return (
        usp_string.split(),
        output_string.split(),
    )


def input_decode(usp: list[str]) -> dict[str, int]:
    """
    original string
    1 = cf
    7 = acf
    4 = bcdf
    8 = abcdefg
    2 = acdeg
    3 = acdfg
    5 = abdfg
    0 = abcefg
    6 = abdefg
    9 = abcdfg
    """
    number_to_digit: dict = dict()
    len_fiver: list = []
    len_sixer: list = []
    for number_str in usp:
        if len(number_str) == 2:
            number_to_digit[1] = "".join(sorted(number_str))
        if len(number_str) == 3:
            number_to_digit[7] = "".join(sorted(number_str))
        if len(number_str) == 4:
            number_to_digit[4] = "".join(sorted(number_str))
        if len(number_str) == 7:
            number_to_digit[8] = "".join(sorted(number_str))
        if len(number_str) == 5:
            len_fiver.append(number_str)
        if len(number_str) == 6:
            len_sixer.append(number_str)

    for fiver in len_fiver:
        if len(set(fiver) - set(number_to_digit[4])) == 3:
            number_to_digit[2] = "".join(sorted(fiver))
        elif len(set(fiver) - set(number_to_digit[7])) == 3:
            number_to_digit[5] = "".join(sorted(fiver))
        else:
            number_to_digit[3] = "".join(sorted(fiver))

    for sixer in len_sixer:
        if len(set(sixer) - set(number_to_digit[5])) == 2:
            number_to_digit[0] = "".join(sorted(sixer))
        elif len(set(sixer) - set(number_to_digit[3])) == 1:
            number_to_digit[9] = "".join(sorted(sixer))
        else:
            number_to_digit[6] = "".join(sorted(sixer))
    digit_to_number: dict = {v: k for k, v in number_to_digit.items()}

    return digit_to_number


def output_decode(output_string: list[str], decoder: dict) -> list[int]:
    output_number: list = []
    for string in output_string:
        output_number.append(decoder.get("".join(sorted(string))))

    return output_number


def Q1():
    ans_counter: Counter[int] = Counter()
    for line in raw_data:
        usp, ans = parse_data(line)
        ans_counter += Counter(output_decode(ans, input_decode(usp)))
    print(sum([ans_counter[1], ans_counter[4], ans_counter[7], ans_counter[8]]))


def Q2():
    ans_counter: int = 0
    for line in raw_data:
        usp, ans = parse_data(line)
        decode_list = output_decode(ans, input_decode(usp))

        ans_counter += (
            decode_list[0] * 1000
            + decode_list[1] * 100
            + decode_list[2] * 10
            + decode_list[3]
        )

    print(ans_counter)


Q1()
Q2()
