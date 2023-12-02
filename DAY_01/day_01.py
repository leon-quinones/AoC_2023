#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:32:33 2023

@author: Leonard Quinones
"""
    
from typing import Union, Tuple, List

NUMBERS_ALP_NUM = {'one': '1',
                   'two': '2', 
                   'three': '3', 
                   'four': '4', 
                   'five': '5', 
                   'six': '6', 
                   'seven': '7', 
                   'eight': '8', 
                   'nine': '9',
                   'zero': '0'
                   }

def find_numbers(string: str, numeric_symbols: List[str]) -> List[Tuple] :
    found_numbers = []
    for number in numeric_symbols:
        found_index = string.find(number)
        found_rindex = string.rfind(number)
        if found_index > -1:
            found_numbers.append((found_index, number))
        if found_rindex > -1:
            found_numbers.append((found_rindex, number))
    found_numbers = sorted(found_numbers)
    if found_numbers:
        if len(found_numbers) == 1:
            return (found_numbers[0], found_numbers[0])
        if len(found_numbers) >= 2:
            return (found_numbers[0], found_numbers[-1])
    return None

def find_calibration_values(string: str) -> Union[Tuple,None]:
    alpha_numbers =  find_numbers(string, numeric_symbols=NUMBERS_ALP_NUM.keys())
    if alpha_numbers:
        alpha_numbers = tuple(map(
            lambda x: (x[0], NUMBERS_ALP_NUM.get(x[1])) if x[1] in NUMBERS_ALP_NUM.keys() 
                       else x, alpha_numbers))
    digits =  find_numbers(string, numeric_symbols=NUMBERS_ALP_NUM.values())
    if (alpha_numbers and digits):
        found_numbers = sorted(alpha_numbers + digits)
        return (found_numbers[0][1], found_numbers[-1][1])
    
    if alpha_numbers and not digits:
        return (alpha_numbers[0][1], alpha_numbers[-1][1])

    if not alpha_numbers and digits:
        return (digits[0][1], digits[-1][1])    
    
    return None


def build_number(numbers_symbols: iter):
    return int(''.join(numbers_symbols))


with open('/home/leonard/Documents/AOC2023/DAY_01/input_day01_half_two', 'r') as f:
    found_digits: list[int] = [] 
    for line in f:
        found_digits.append(build_number(find_calibration_values(line)))
    print(sum(found_digits))
    