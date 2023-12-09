from collections import defaultdict

from day_04 import extract_card_info, check_match_numbers

def calculate_cardpiles_guesses(file_path: str, delimiter:str):
    card_pile = defaultdict()
    cards_counter = defaultdict()
    with open(file_path) as data:
        for card in data:
            card_id, winners, ticket = extract_card_info(card.strip(), delimiter)
            guess_numbers = check_match_numbers(winners, ticket)
            card_pile[int(card_id)] = len(guess_numbers)
            cards_counter[int(card_id)] = 1

    cards_number = len(card_pile)

    print(cards_counter)
    for card in card_pile:
        for card_amount in range(cards_counter.get(card)):
            last_card = card + card_pile.get(card) \
                if card + card_pile.get(card) <= cards_number \
                else cards_number
            print(f'card {card}, {list(range(card + 1, last_card + 1))}')
            for duplicate_card in range(card + 1, last_card + 1):
                cards_counter[duplicate_card] += 1
    print(cards_counter)

    print(sum(cards_counter.values()))
calculate_cardpiles_guesses('test_case', ' ')
calculate_cardpiles_guesses('./day_04_input', ' ')


