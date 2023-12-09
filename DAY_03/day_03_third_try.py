from string import punctuation
from typing import List, Tuple
import re


def parse_data_from_line(string: str, delimiter='.') -> Tuple:
    symbols = [x.span() for x in re.finditer('\W', string)]
    data = list(filter(lambda x: x, string.split(delimiter)))
    numbers = []
    for element in data:
        # print(element)
        if len(element) == 1:
            continue
        if element.isnumeric():
            numbers.append(element)
            continue
        # print(element, re.sub('\W', delimiter, element).split(delimiter))
        numbers += list(filter(lambda x: x, re.sub('\W', delimiter, element).split(delimiter)))
    return numbers, symbols

def verify_adjacency(spans_to_check: List, spans_to_compare: List, shift: int):
    for span in spans_to_check:
        x, y = span
        for cspan in spans_to_compare:
            x1, y1, = cspan
            if x <= x1 <=y:
                pass



with open('./day_03_input') as schematic:
    data_in_lines = schematic.readlines()
    line_size = len(data_in_lines[0].strip()) + 1
    schem_data :str = ''.join(data_in_lines).replace('\n', '.')
    # print(schem_data , len(schem_data ), sep='\n')
    numbers, symbols_spans = parse_data_from_line(schem_data)
    result = 0

    numbers_spans = {}
    for number in numbers:
        numbers_spans[number] = [x.span() for x in re.finditer(number, schem_data)
                                 if x.group(0) == number]

    for number, spans in numbers_spans.items():
        for span in spans:
            # coors_to_check = [(span[0] - line_size, span[1] - line_size),
            # (span[0] + line_size, span[1] + line_size),
            # (span[0] - 1, span[1] - 1),
            # (span[0] + 1, span[1] + 1),
            # (span[0] - line_size - 1, span[1] - line_size -1),
            # (span[0] - line_size + 1, span[1] - line_size + 1),
            # (span[0] + line_size - 1, span[1] + line_size - 1),
            # (span[0] + line_size + 1, span[1] + line_size + 1)]


            adjacencies = list(filter( lambda x: x in symbols_spans, coors_to_check))
            if adjacencies:
                result += int(number)
                break
        print(result)















with open('./day_03_input', 'r', encoding='UTF-8') as schematics:
    for line in schematics:
        pass