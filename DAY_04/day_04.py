import re
from typing import List, Tuple


def check_match_numbers(winner_numbers: List, ticket_numbers: List) -> List:
    return set(winner_numbers).intersection(set(ticket_numbers))

def extract_numbers(string: str, delimiter: str) -> List:
    return sorted(string.split(delimiter))

def extract_card_info(string: str, delimiter: str, ticket_delimiter='|') -> Tuple:
    winner_numbers_data, ticket_data = string.split(ticket_delimiter)
    card_label, card_id, *winner_numbers = list(filter(lambda x: x, winner_numbers_data.replace(':', delimiter).split(delimiter)))
    ticket_numbers = ticket_data.split(delimiter)
    return card_id, sorted(list(filter(lambda x: x, winner_numbers))), \
        sorted(list(filter(lambda x: x, ticket_numbers)))

def calculate_card_points(guess_numbers: list) -> int:
    return 0 if len(guess_numbers) == 0 else 2**(len(guess_numbers)-1)

def calculate_ticketpile_points(file_path: str, delimiter:str):
    points = []
    with open(file_path) as card_pile:
        for card in card_pile:
            card_id, winners, ticket = extract_card_info(card.strip(), delimiter)
            guess_numbers = check_match_numbers(winners, ticket)
            card_points = calculate_card_points(guess_numbers)
            points.append(card_points)
            print(f'card {card_id}: {guess_numbers}, {card_points}')
            print
    print(sum(points))


# card_id, winners, ticket = extract_card_info('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', ' ')
# #print(check_match_numbers(winners, ticket))
# data = [1,2,3]
# print(calculate_card_points(data))

# 21088
# 20055
# 18619

if __name__ == '__main__':
    calculate_ticketpile_points('./day_04_input', ' ')