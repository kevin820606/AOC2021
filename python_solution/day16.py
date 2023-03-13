#!/usr/bin/env python3
# https://adventofcode.com/2021/day/16

from util import read
from functools import reduce

def word_to_bit(string: str) -> str:
    word_to_bit = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    bits = ""
    for i in string:
        bits += word_to_bit[i]
    return bits
def type_calculate(typeid:int, numbers:list[int]) -> int:
    # print(f'{typeid=}\n{numbers=}')
    match typeid:
        case 0:
            value =sum(numbers)
            print(value)
            return sum(numbers)
        case 1:
            value = reduce(lambda x, y: x*y, numbers, 1)
            print(value)
            return value 
        case 2:
            value = min(numbers)
            print(value)
            return min(numbers)
        case 3:
            value = max(numbers)
            print(value)
            return max(numbers)
        case 4:
            value = numbers
            print(value)
            return numbers
        case 5:
            value = 1 if numbers[0] > numbers[1] else 0
            print(value)
            return value
        case 6:
            value = 1 if numbers[0] < numbers[1] else 0
            print(value)
            return value
        case 7:
            value = 1 if numbers[0] == numbers[1] else 0
            print(value)
            return value
        
        
def bit_transfer(bits: str) -> tuple[list[int], list[int], str]:
    if len(bits) < 7:
        return [], [], bits
    package_version = [int(bits[0:3], 2)]
    type_id = bits[3:6]
    bits_label = bits[6] if type_id != "100" else "2"
    sub_label = {"0": 15, "1": 11, "2": 5}
    literal_value: list[int] = []
    remain_string = ""

    if bits_label == "2":
        literal_string = ""
        for bit in range(6, len(bits), 5):
            segment_bits = bits[bit : bit + 5]
            last_indicate = segment_bits[0]
            if len(segment_bits) < 5:
                break
            literal_string += segment_bits[1:]
            if last_indicate == "0":
                remain_string = bits[bit + 5 :]
                break
        literal_value.append(int(literal_string, 2))
        # literal_value = type_calculate(int(type_id, 2), literal_value)
        return (package_version, literal_value, remain_string)

    judge_line = bits[7 : 7 + sub_label[bits_label]]
    bits = bits[7 + sub_label[bits_label] :]

    if bits_label == "0":
        current:list[int] = []
        segment_length = int(judge_line, 2)
        version, value, remain_string = bit_transfer(bits[:segment_length])
        package_version.extend(version)
        current.extend(value)
        remain_string = remain_string + bits[segment_length:]
        while len(remain_string) > 7:
            version, value, remain_string = bit_transfer(remain_string)
            package_version.extend(version)
            current.extend(value)
        current = type_calculate(int(type_id, 2), current)
        literal_value.append(current) 
        return package_version, literal_value, remain_string

    if bits_label == "1":
        current:list[int] = []
        segments_times = int(judge_line, 2)
        times = 0
        while times < segments_times:
            version, value, remain_string = bit_transfer(bits)
            bits = remain_string
            package_version.extend(version)
            current.extend(value)
            times += 1
        current = type_calculate(int(type_id, 2), current)
        literal_value.append(current) 
        return package_version, literal_value, remain_string


if __name__ == "__main__":
    raw_data = read(16)
    for string in raw_data:
        print(string)
        a = word_to_bit(string)
        version, value, string = bit_transfer(bits=a)   
        print(value)
