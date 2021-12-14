#! /usr/bin/env python3
# https://adventofcode.com/2021/day/14
from util import read
from collections import Counter

from pprint import pprint

raw_data = read(14, True)
WORDDICT = Counter[str]
WORDMAP = dict[str, tuple[str, str, str]]


def clean_data(data: list[str]) -> tuple[WORDDICT, WORDMAP, str, Counter[str]]:
    startline = data[0]
    setence_start = startline[0]
    word_dict: WORDDICT = Counter()
    word_map: WORDMAP = dict()
    multiple: Counter[str] = Counter()
    for i in range(len(startline)):
        if i + 1 == len(startline):
            break
        word = startline[i] + startline[i + 1]
        word_dict[word] += 1
        multiple += Counter([word[1]])

    for line in data[2:]:
        word, mapping = line.split(" -> ")
        word_map[word] = (word[0] + mapping, mapping + word[1], mapping)
    return word_dict, word_map, setence_start, multiple


day14data, word_map, sentence_start, multi = clean_data(raw_data)


def wordinsertdict(
    word_dict: WORDDICT, word_map: WORDMAP = word_map
) -> tuple[WORDDICT, Counter[str]]:
    final_dict: WORDDICT = Counter()
    mutiple_word: Counter[str] = Counter()
    for key, number in word_dict.items():
        new_1, new_2, redundant = word_map[key]
        final_dict[new_1] += number
        final_dict[new_2] += number
        mutiple_word[redundant] += number
    return final_dict, mutiple_word


def multi_times(times: int):
    word_dict = day14data
    char_counter: Counter[str] = Counter()
    multi_word: Counter[str] = multi

    for _ in range(times):
        word_dict, muti = wordinsertdict(word_dict)
        multi_word += muti

    for key, times in word_dict.items():
        char_counter[key[0]] += times
        char_counter[key[1]] += times

    char_counter -= multi_word
    maxn, maxnumber = char_counter.most_common()[0]
    leam, leastnumber = char_counter.most_common()[-1]
    print(maxn, leam, char_counter)
    return word_dict, maxnumber - leastnumber


# print(wordinsertdict(word_dict=day14data))
print(multi_times(40))

# ANS is output -1, and honestly I'm not queit sure why.
