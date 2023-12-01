#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:32:33 2023

@author: leonard
"""

from typing import Union, Tuple

def find_indexes(string: str) -> Tuple[int, int]:
    indexes: list[int] = list(filter(lambda x: x if x.isnumeric() else False, string))
    number_of_digits = len(indexes)
    if number_of_digits:
        if number_of_digits == 1:
            return (indexes[0], indexes[0])
        if number_of_digits >= 2:
            return (indexes[0], indexes[-1])
    return None

def build_number(indexes: iter):
    return int(''.join(indexes))


"""
print(find_indexes('1abc2'))
print(find_indexes('pqr3stu8vwx'))
print(find_indexes('a1b2c3d4e5f'))
print(find_indexes('treb7uchet'))
"""

with open('/home/leonard/Documents/AOC2023/DAY_01/input_day01', 'r') as f:
    found_digits: list[int] = [] 
    for line in f:
        found_digits.append(build_number(find_indexes(line)))
    print(sum(found_digits))
    