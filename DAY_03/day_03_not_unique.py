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
            if char in punctuation:
                number1, number2 = element.split(char)
                print(element.split(char))
                symbols.append(number1)
                symbols.append(number2)
                symbols.append(char)
        print(symbols)
        print(list(filter(lambda x: x, symbols)))
        expanded_info += list(filter(lambda x: x, symbols))
    return expanded_info

def verify_adjacency(num_coordinates: List[Tuple], symbol_coors: List[Tuple]):
    times_to_add_number = 0
    if symbol_coors:
        for num in num_coordinates:
            for symbol in symbol_coors:
        # horizontal and diagonal
        # index = 1 = end of string and 0= start of string
                if symbol[1] == num[0]:
                    return 1
                if symbol[0] == num[1]:
                    return 1
                # vertical
                if symbol[0] == num[0]:
                    return 1
                if symbol[1] == num[1]:
                    return 1
                # overlapping
                if num[0] <= symbol[0] < num[1]:
                    return 1
    return times_to_add_number

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
            print('################')
            print(f'line {i}')
            characters = split_numbers_and_symbols(list(filter(lambda x: x,line.strip().split(delimiter))))
            characters = sort_symbols_first(characters)
            for char in characters:
                coordinates = finditer(line, char)
                if char in punctuation:
                    found_symbols[str(i)] += coordinates
                    continue
                if numbers_to_validate_forward and k < i:
                    for j, num in enumerate(numbers_to_validate_forward):
                        print('backward', numbers_to_validate_forward)
                        times_to_add_number = verify_adjacency(
                            coors_to_validate_forward[j], found_symbols[str(k+1)])
                        result += int(num) * times_to_add_number
                        print(f'num {num} added {times_to_add_number} times')
                    coors_to_validate_forward = []
                    numbers_to_validate_forward = []
                    k = i

                if char.isnumeric():
                    times_same_line = verify_adjacency(coordinates, found_symbols[str(i)])
                    times_backward = verify_adjacency(coordinates, found_symbols[str(i-1)])
                    times_to_add = times_backward + times_same_line
                    result += int(char) * times_to_add
                    print(f'num {char} adjacent same line {times_same_line} adjacent backward{times_backward}' )
                    print(f'num {char} added {times_to_add} times')
                    if times_to_add == 0:
                        coors_to_validate_forward.append(coordinates)
                        numbers_to_validate_forward.append(char)
                        k = i

        print(result)
    print(found_symbols)

validate_schematic('./test_case_2')

# print(split_numbers_and_symbols(list(filter(lambda x: x, '617*......'.split('.')))))
# verify_adjacency([(5,8)],[(3, 4), (5, 6), (6, 7), (7, 8)])
line = '32.480..665.....557......+...435..449..691..327....................#....921..535..........755...43...597........................322..7......'
data = split_numbers_and_symbols(line.split('.'))
# print(line)
# print(line.split('.'))
# print(data)