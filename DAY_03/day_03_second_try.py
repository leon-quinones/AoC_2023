from collections import defaultdict, OrderedDict
from functools import reduce
from string import punctuation
from typing import List, Tuple, Dict
from itertools import zip_longest
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

def extract_numbers(string: str, delimiter='.'):
    numbers = []
    data = list(filter(lambda x: x, string.split(delimiter)))
    for element in data:
        # print(element)
        if len(element) == 1:
            continue
        if element.isnumeric():
            numbers.append(element)
            continue
        # print(element, re.sub('\W', delimiter, element).split(delimiter))
        numbers += list(filter(lambda x: x, re.sub('\W', delimiter, element).split(delimiter)))
    return numbers

def extract_symbols(string: str, delimiter='.'):
    return [x.group(0) for x in re.finditer('\W', string.replace(delimiter,''))]

def get_coordinates(character: str, string: str):
    return finditer(string, character)

def verify_adjacency(symbol_coordinates: List[Tuple], numbers_coordinates: List[Dict]):
    if numbers_coordinates:
        for symbol in symbol_coordinates:
            for num_coor in numbers_coordinates:
                if num_coor[0] <= symbol[0] <= num_coor[1]:
                    return True
                if num_coor[0] == symbol[1]:
                    return True
        return False

def check_symbol_adjacency(symbol_coors: Dict, numbers_coors: List[Dict]):
    partial_sum = 0
    if numbers_coors:
        for number in numbers_coors:
            is_adjacent = verify_adjacency(*symbol_coors.values(), *number.values())
            if is_adjacent:
                partial_sum += int(*number.keys())

    return partial_sum

# def sort_symbols_first(data: List[str]):
#     symbols = list(filter(lambda x: x in punctuation, data))
#     numbers = list(filter(lambda x: x not in punctuation, data))
#     return list(OrderedDict.fromkeys((sorted(symbols) + sorted(numbers))))

def validate_schematic(file_path: str, delimiter='.', ) -> int:
    result = 0
    found_symbols = defaultdict(list)
    found_numbers = defaultdict(list)
    symbols_coors = defaultdict(list)
    numbers_coors = defaultdict(list)

    with open(file_path, 'r', encoding='UTF-8') as data:
        schematic_data = data.readlines()

    for i, line in enumerate(schematic_data):
        found_symbols[i].append(set(extract_symbols(line.strip())))
        found_numbers [i].append(set(extract_numbers(line.strip())))
    #
    print(found_symbols)
    print(found_numbers)

    line_size = len(schematic_data[0])
    for i, line in enumerate(schematic_data):
        for symbol, number in zip_longest(*found_symbols[i],
                                          *found_numbers[i]):
            # print(symbol, number)
            # print(symbol, number)
            if symbol:
                # print(symbol, line)
                symbols_coors[i].append({symbol: get_coordinates(symbol, line.strip())})
    #             # print(get_coordinates(symbol, line.strip()))
            if number:
                numbers_coors[i].append({number: get_coordinates(number, line.strip())})

    # print(numbers_coors)
    # print(symbols_coors)
    for i in symbols_coors.keys():
        for symbol in symbols_coors.get(i):
            numbers_in_previous_line = numbers_coors.get(i-1)
            numbers_in_line = numbers_coors.get(i)
            numbers_in_next_line = numbers_coors.get(i+1)

            prev_adj = check_symbol_adjacency(symbol, numbers_in_previous_line)
            inline_adj = check_symbol_adjacency(symbol, numbers_in_line)
            next_adj = check_symbol_adjacency(symbol, numbers_in_next_line)
            print(i, symbol, prev_adj, inline_adj, next_adj)
            result += (prev_adj + inline_adj + next_adj)
    print(result)




# validate_schematic('./test_case')
validate_schematic('./day_03_input') #  514969
# # print(split_numbers_and_symbols(list(filter(lambda x: x, '617*......'.split('.')))))
