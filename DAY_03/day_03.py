import re
from collections import defaultdict
from typing import List, Tuple, Union, Dict
from functools import reduce
from string import punctuation


def extract_info(spec_line: str, delimiter='.') -> List[str]:
    return list(filter(lambda x: x, spec_line.split(delimiter)))

def split_numbers_and_symbols(extracted_info: List[str]):
    expanded_info = extracted_info.copy()
    for element in extracted_info:
        if len(element) == 1:
            continue
        if element.isnumeric():
            continue
        expanded_info.remove(element)
        expanded_info += list(filter(lambda x: x, re.split(r'\D', element)))
    return expanded_info


def finditer(string, sub_string):
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

def find_indexes(spec_data:str, sub_string: str) -> Union[List, None]:
    print(sub_string)
    sub_occurrences = finditer(spec_data, sub_string)
    print(sub_occurrences)
    return list(reduce(lambda x, y: x + [y] , sub_occurrences, []))

def find_coordinates(spec_lines: List[str], delimiter='.') -> Dict:
    numbers_symbols_found = []
    reduced_specification = ''.join(spec_lines)
    for line in spec_lines:
        print(line)
        numbers_symbols_found += extract_info(line, delimiter)
    print(numbers_symbols_found)
    spec_coordinates:Dict = defaultdict.fromkeys(
        sorted(split_numbers_and_symbols(numbers_symbols_found)))

    print(spec_coordinates.keys())

    for symbol in spec_coordinates.keys():
        spec_coordinates[symbol] = find_indexes(reduced_specification, symbol)
    print(spec_coordinates)




test_lines = ['467..114..', '...*......', '..35..633.', '......#...', '617*1*1...',
              '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']

find_coordinates(test_lines)
#print(finditer('467..114..', '1'))
# line = '467..114..'
# line2 = '...*......'
# print(extract_info(line))
# indexes = find_indexes(line, '467')
# print(indexes, line[indexes[0]:indexes[1]])
# indexes = find_indexes(line, '114')
# print(indexes, line[indexes[0]:indexes[1]])
# indexes = find_indexes(line2, '*')
# print(indexes, line2[indexes[0]:indexes[1]])