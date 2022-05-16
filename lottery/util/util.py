import random


def raffle(number_of_numbers, game_size):
    numbers_drawn = random.sample(range(1, game_size + 1), number_of_numbers)
    return sorted(numbers_drawn)


def match_number(a, b):
    lt = []
    for c in a:
        if c in b:
            lt.append(c)
    return lt


def total_match_number(lista):
    return len(lista)
