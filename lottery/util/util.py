import random


def raffle(number_of_numbers: int, game_size: int):
    numbers_drawn = random.sample(range(1, game_size + 1), number_of_numbers)
    return sorted(numbers_drawn)


def match_number(numbers_drawn: list, numbers_chosen: list):
    lt = []
    for number in numbers_drawn:
        if number in numbers_chosen:
            lt.append(number)
    return lt


def total_match_number(match_num: list):
    return len(match_num)
