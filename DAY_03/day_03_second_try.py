from collections import defaultdict, OrderedDict
from string import punctuation
from typing import List, Tuple
import re


def finditer(string: str, sub_string: str) -> List[Tuple]:
    indexes = []
    k = 0
    string_length = len(string)
    sub_length = len(sub_string)
    while k < string_length:
        index = string[k:].find(sub_string)
        if index == -1:
            break
        if index >= -1:
            start = k + index
            end = start + sub_length
            indexes.append((start, end))
            k += index + sub_length
    return indexes

def split_numbers_and_symbols(extracted_info: List[str]):
    expanded_info = extracted_info.copy()
    for element in extracted_info:
        if len(element) == 1:
            continue
        if element.isnumeric():
            continue
        expanded_info.remove(element)
        k = 0
        symbols = []
        for i, char in enumerate(element):
            if char.isnumeric():
                continue
            if i > 0:
                symbols.append(element[k:i])
                k = i
            symbols.append(char)
        expanded_info += symbols
    return expanded_info

def verify_adjacency(num_coordinates: List[Tuple], symbol_coors: List[Tuple]):
    if symbol_coors:
        for num in num_coordinates:
            for symbol in symbol_coors:
        # horizontal and diagonal
        # index = 1 = end of string and 0= start of string
                if symbol[1] == num[0]:
                    return True
                if symbol[0] == num[1]:
                    return True
                # vertical
                if symbol[0] == num[0]:
                    return True
                if symbol[1] == num[1]:
                    return True
                # overlapping
                if num[0] <= symbol[0] < num[1]:
                    return True
    return False

def sort_symbols_first(data: List[str]):
    symbols = list(filter(lambda x: x in punctuation, data))
    numbers = list(filter(lambda x: x not in punctuation, data))
    return list(OrderedDict.fromkeys((sorted(symbols) + sorted(numbers))))

def validate_schematic(file_path: str, delimiter='.', size=10, ) -> int:
    found_symbols=defaultdict(list)
    numbers_to_validate_forward = []
    result = 0
    coors_to_validate_forward = []
    k = 0

    with open(file_path, 'r', encoding='UTF-8') as data:
        for i, line in enumerate(data):
            characters = split_numbers_and_symbols(list(filter(lambda x: x,line.strip().split(delimiter))))
            characters = sort_symbols_first(characters)
            for char in characters:
                coordinates = finditer(line, char)
                if char in punctuation:
                    found_symbols[str(i)] += coordinates
                    continue
                if numbers_to_validate_forward and k <= i:
                    for j, num in enumerate(numbers_to_validate_forward):
                        is_adjacent_forward = verify_adjacency(
                            coors_to_validate_forward[j], found_symbols[str(k+1)])
                        if is_adjacent_forward:
                            result += int(num)
                            continue
                    coors_to_validate_forward = []
                    numbers_to_validate_forward = []
                    k == i


                if char.isnumeric():
                    is_adjacent = verify_adjacency(coordinates, found_symbols[str(i)])
                    if is_adjacent:
                        result += int(char)
                        continue
                    is_adjacent_backward = verify_adjacency(coordinates, found_symbols[str(i-1)])
                    if is_adjacent_backward:
                        result += int(char)
                        continue
                    coors_to_validate_forward.append(coordinates)
                    numbers_to_validate_forward.append(char)
                    k = i


        print(result)
    print(found_symbols)

validate_schematic('./day_03_input')
# print(split_numbers_and_symbols(list(filter(lambda x: x, '617*......'.split('.')))))
